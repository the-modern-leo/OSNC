from __future__ import absolute_import
from builtins import str
from builtins import object
import requests, logging
from collections import namedtuple
from datetime import datetime
from netaddr import IPAddress, IPNetwork
from functools import wraps

from . import settings

MAX_ACCESS_TIME = 300 # maximum time between CSV accesses, in seconds
def csv_wrapper(poc_function):
    """
    Internal wrapper/decorator: Check time since last CSV access, and
    redownload if above a certain duration.

    Args:
        poc_function (function): Function that checks last CSV access.
    """
    @wraps(poc_function)
    def wrapper(self, *args, **kwargs):
        # check every MAX_ACCESS_TIME seconds
        if (datetime.now() - self.csvtimeout).seconds < MAX_ACCESS_TIME:
            return poc_function(self, *args, **kwargs)
        else:
            self.load_csv()
            return poc_function(self, *args, **kwargs)
    return wrapper

class NetInfo(object):
    """
    Network information. This is used as values in the internal dictionary,
    keyed by either POC or Network.

    Args:
        ip (IPNetwork): Subnet/IP of the POC.
        status (str): Status of the Subnet.
        description (str): Description of the Subnet.
        node (str): The node the Subnet is on.
        sensitive (bool): Optional - Whether or not the Subnet is sensitive 
            (Y/N).
        poclist (set): Optional - A list of other POCs.
    """
    def __init__(self, ip, status, description, node, sensitive=False,
            poclist=set()):
        self.ip = ip
        self.status = status
        self.description = description
        self.node = node
        self.sensitive = sensitive
        self.poclist = poclist

    def __str__(self):
        return ("NetInfo(" + ', '.join(["ip='" + str(self.ip) + "'",
                "status='" + str(self.status) + "'",
                "desc='" + str(self.description) + "'",
                "node='" + str(self.node) + "'",
                "sensitive='" + str(self.sensitive) + "'",
                "[" + ', '.join(str(p) for p in self.poclist) + "]"]) + ")")
    
    def __repr__(self):
        return self.__str__()

    def asdict(self):
        """
        Fetches object information in a dictionary.

        Returns:
            dict: Information from object under the keys: ip, status, 
            description, node, sensitive, poclist.
        """
        return {'ip': str(self.ip), 'status': self.status,
                'description': self.description,
                'node': self.node,
                'sensitive': self.sensitive,
                'poclist': [dict(p._asdict()) for p in self.poclist]}

POC = namedtuple('POC', ['name', 'unid', 'type', 'email',
        'phone_desk', 'phone_cell'])

class POCUtilities(object):
    """
    Point of Contact utilities. This tracks point-of-contact information for
    particular subnets.
    Notes about the poc_dict internal object
    This is an internal dictionary to track network and POCs. This is keyed by
    IPNetworks as well as POCs - IPNetwork keyed values are NetInfos, while
    POC keyed values are a set of NetInfos. Each NetInfo may be a reference to
    the same objects, so updating one NetInfo should apply changes for any key
    reference.

    Args:
        poc_csv_url (str): The URL of the CSV containing the organization's POCs.
        subnet_csv_url (str):  The URL of the CSV containing the organization's 
            subnets.
    """
    def __init__(self, poc_csv_url, subnet_csv_url):
        # set super early so load_csv() is triggered on first read
        self.csvtimeout = datetime.fromordinal(1)

        # warning: state is bad, but this is better than using a second database
        self.poc_csv_url = poc_csv_url
        self.subnet_csv_url = subnet_csv_url
        self.poc_dict = {}

    def load_csv(self):
        """
        Download the CSV from the URL given in the class initialization.
        This is most likely implementation-specific, based on how the
        organization's POC is currently kept. Right now this assumes that the
        POC can be retrieved with a handful of REST calls to particular URLs.
        Assumed CSV format:
        List of POCs by subnet/IP, with the following fields:
        Subnet,uNID,First name,Last name,POC Type,Phone number,email
        List of subnets by subnet IP, with the following fields:
        Subnet,Status code,Node,Sensitive,Description

        Raises:
            Exception: Caused if provided an invalid url.
            ValueError: Caused if no POC Type is provided.
        """
        # clear saved dictionary
        self.poc_dict = {}

        # download the contact CSV
        csv_req = requests.get(self.poc_csv_url)
        if csv_req.status_code >= 400:
            raise Exception('invalid response ' + str(csv_req.status_code) +
                    'from contact URL: ' + str(csv_req.text)[:150])
        csv = csv_req.text.splitlines()
        for line in csv:
            line = line.split(',')
            subnet = IPNetwork(line[0])
            if line[4] == '%null%':
                line[4] = None
            elif line[4] not in settings.POC_TYPES:
                raise ValueError('warning: Unknown POC Type "' + line[4] + '"')
            phone_desk = line[5].replace('-', '')
            poc = POC(line[2] + ' ' + line[3], line[1], line[4], line[6],
                    phone_desk, None)

            # add NetInfo by keyed subnet
            netinfo = None
            if self.poc_dict.get(subnet):
                netinfo = self.poc_dict[subnet]
                netinfo.poclist.add(poc)
            else:
                netinfo = NetInfo(subnet, '', '', '', poclist=set([poc]))
                self.poc_dict[subnet] = netinfo

            # add NetInfo by keyed POC
            if self.poc_dict.get(poc):
                self.poc_dict[poc].add(netinfo)
            else:
                self.poc_dict[poc] = set([netinfo])

        # download the subnet CSV
        csv_req = requests.get(self.subnet_csv_url)
        if csv_req.status_code >= 400:
            raise Exception('invalid response ' + str(csv_req.status_code) +
                    'from subnet URL: ' + str(csv_req.text)[:150])
        csv = csv_req.text.splitlines()
        for line in csv:
            line = line.split(',')
            subnet = IPNetwork(line[0])

            # Add network information in to existing (or create new) entries
            if self.poc_dict.get(subnet):
                netinfo = self.poc_dict[subnet]
                netinfo.status = line[1]
                netinfo.description = ','.join(line[4:])
                netinfo.node = line[2]
                netinfo.sensitive = ('Y' in line[3])
            else:
                self.poc_dict[subnet] = NetInfo(subnet, line[1],
                        ','.join(line[4:]), line[2], sensitive=('Y' in line[3]))

        # update last access timestamp
        self.csvtimeout = datetime.now()

    @csv_wrapper
    def poc_keys(self):
        """
        Retrieve POC keyed values from the POC dictionary/database.

        Returns:
            list: A list of POC keys.
        """
        return [n for n in list(self.poc_dict.keys()) if isinstance(n, POC)]

    @csv_wrapper
    def net_keys(self):
        """
        Retrieve Network keyed values from the POC dictionary/database.

        Returns:
            list: A list of Network keys.
        """
        return [n for n in list(self.poc_dict.keys()) if isinstance(n, IPNetwork)]

    @csv_wrapper
    def search_ip(self, ip, inclusive=False):
        """
        Search for an IP address or network in the POC.

        Args:
            ip (str): IP address or network as a CIDR string or IPNetwork 
                object. inclusive: If True, return subnets that are contained by
                ip. This is useful for getting multiple matches in a large 
                network (such as a /16).
            inclusive (bool): Represents whether the search is inclusive.

        Returns:
            dict: A dictionary of matching IPNetwork/NetInfo objects.
        """
        ip = IPNetwork(ip)
        net_list = [n for n in self.net_keys() if ip in n or
                (inclusive and n in ip)]

        return {n: self.poc_dict[n] for n in net_list}

    @csv_wrapper
    def search_poc(self, unid=None, name=None, phone=None, email=None,
            type=None):
        """
        Search for a POC's assigned networks by contact.

        Args:
            unid (str): Optional - Exact UNID.
            name (str): Optional - Name (partial or full).
            phone (str): Optional - Phone number (partial or full).
            email (str): Optional - Exact TestEmail address.
            type (str): Optional - POC Type.

        Returns:
            dict: A dictionary of matching POC/NetInfo objects.

        Raises:
            ValueError: Caused if no parameters have been provided.
        """
        if not unid and not name and not phone and not email:
            raise ValueError("At least one parameter must be given")

        poc_list = self.poc_keys()
        if unid:
            poc_list = [p for p in poc_list if p.unid == unid]
        if name:
            poc_list = [p for p in poc_list if name.lower() in p.name.lower()]
        if phone:
            phone = phone.replace('-', '').replace(' ', '')  # normalize input
            poc_list = [p for p in poc_list if
                    (p.phone_desk and phone in p.phone_desk)
                    or (p.phone_cell and phone in p.phone_cell)]
        if email:
            poc_list = [p for p in poc_list if p.email.lower() == email.lower()]
        if type:
            poc_list = [p for p in poc_list if p.type == type]

        return {p: self.poc_dict[p] for p in poc_list}

    def search_csv(self, csv):
        """
        Parse a CSV that has one ip or subnet per line and use search_ip
        to build a list that can be converted to a csv to the user

        Args:
            csv (str): a csv, with IPs/Subnets separated by newlines
            
        Returns:
            str: a string that can be read as a csv containing the POC details
        """
        subnet_list = csv.splitlines()
        return_list = ["Searched IP,Found Subnet,Status,Node,Sensitive,"+
                "Description,POC Name,POC Type,POC Cell,POC Desk Phone," +
                "POC TestEmail,POC uNID"]
        for subnet in subnet_list:
            result_dict = self.search_ip(subnet, inclusive=True)
            result_dict = result_dict[result_dict.keys()[0]].asdict()
            result_keys = result_dict.keys()
            if result_keys:
                result_str = (subnet + "," + result_dict['ip'] + "," +
                        result_dict['status'] + "," + result_dict['node'] +
                        "," + str(result_dict['sensitive']) + "," + "\"" +
                        result_dict['description'] + "\"")
                return_list.append(result_str)
                poc_list = result_dict['poclist']
                for poc in poc_list:
                    poc_info = (",,,,,," + poc['name'] + "," + poc['type'] +
                            "," + str(poc['phone_cell']) + "," +
                            poc['phone_desk'] + "," + poc['email'] + "," +
                            poc['unid'])
                    return_list.append(poc_info)

        return '\n'.join(return_list)
