from builtins import str, object
import requests, json, dns.zone, dns.query, socket, logging, netaddr, time
from dns import rdatatype
from collections import namedtuple
from netaddr import IPNetwork, IPAddress
from . import settings
## only used in gen_range()
from itertools import groupby
from operator import itemgetter

class Infoblox(object):
    """
    A simplified module for common Infoblox actions, such as adding hostnames,
    networks and DHCP pools. May eventually have support for things
    such as POC database searches (in a separate module) and pool utilization.

    Args:
        url (str): Infoblox URL
        username (str): Infoblox Username
        password (str): Infoblox Password
        rf (Routefinder): routefinder object
        verify (bool): Optional - defaults to true. Verification variable for
            internal session object.
    """
    def __init__(self, url, username, password, rf, verify=True):
        self._infoblox_url = url
        self._infoblox_usr = username
        self._infoblox_pwd = password
        self.session = requests.Session()
        self.session.verify = verify
        self.routefinder = rf

    class InfobloxServerError(Exception):
        """
        An InfobloxServerError occurs when there is a problem retrieving any
        data from the Infoblox API. This could be because the given username
        and password is unable to authenticate, or because that user does not
        have API access enabled.
        """
        pass

    class InfobloxAPIError(Exception):
        """
        An InfobloxAPIError occurs when the API is misused or an unexpected
        command is sent. This should almost never happen.
        """
        pass

    class InfobloxObjectError(Exception):
        """
        An InfobloxObjectError occurs when there is a problem retrieving or
        adding an object (host, network, etc.) to Infoblox.
        """
        pass

    class InfobloxAccessError(Exception):
        """
        An InfobloxAccessError occurs when the API access credentials don't
        work, or if the API username does not have permission to read/write to a
        certain resource.
        """
        pass

    class InfobloxRoutefinderError(Exception):
        """
        An InfobloxRoutefinderError occurs when an exception is raised by
        routefinder.
        """
        pass

    DNSRecord = namedtuple('DNSRecord', ['name', 'type', 'data'])

    # Private functions
    def _check_http_errors(self, response):
        """
        Internal function to check for HTTP codes that shouldn't happen.

        Args:
            response (Response): Response object.

        Raises:
            InfobloxServerError: Caused if user is not authenticated.
        """
        if response.status_code == 401:
            raise self.InfobloxServerError(
                    "API Username and/or password is unauthorized")
        elif response.status_code == 403:
            raise self.InfobloxServerError(
                    "API User authenticated, but does not have API access")

    def _check_api_errors(self, response):
        """
        Internal function to check for errors when interacting with the API.

        Args:
            response (Response): Response Object.

        Raises:
            InfobloxAPIError: Caused if the server has an error.
        """
        # ignore if list is empty - no errors in an empty response
        if len(response) > 0:
            # un-list response (un-listify first, if needed)
            if not isinstance(response, dict):
                response = response[0]

            if isinstance(response, dict) and response.get('Error'):
                raise self.InfobloxAPIError(response['Error'])

    def _get_json(self, url, skip_apicheck=False):
        """
        Send GET messages to Infoblox, using saved WAPI URL and auths.
        Just an internal subroutine to help other functions.

        Args:
            url (str): WAPI URL
            skip_apicheck (bool): Optional - defaults to false. Skips apicheck
            if true.

        Return:
            None or dict: None if no repsonse; Otherwise, JSON enocded content.
        """
        _response = self.session.get(self._infoblox_url + url,
                                 auth=(self._infoblox_usr, self._infoblox_pwd))
        self._check_http_errors(_response) # check for communication errors
        _response_json = _response.json()

        if not skip_apicheck:
            self._check_api_errors(_response_json) # check for API errors

        # if there is nothing in the response, return nothing
        if len(_response.text) <= 2:
            return None
        else:
            return _response_json

    def _post_json(self, url, payload):
        """
        Send POST messages to Infoblox, using saved WAPI URL and auths.
        Just an internal subroutine to help other functions.

        Args:
            url (str): WAPI URL.
            payload (dict): Serialized obj to a json formatted string.
        """
        _post_header = {'content-type': 'application/json'}
        _response = self.session.post(self._infoblox_url + url,
                                  json.dumps(payload),
                                  #params=payload,
                                  headers=_post_header,
                                  auth=(self._infoblox_usr,
                                        self._infoblox_pwd))
        self._check_http_errors(_response) # check for communication errors
        _response_json = _response.json()
        self._check_api_errors(_response_json) # check for API errors

        # if there is nothing in the json response, return nothing
        if len(_response.text) <= 2:
            return None
        else:
            return _response_json

    def _put_json(self, url, payload):
        """
        Description...

        Args:
            url (str): WAPI URL.
            payload (dict): Serialized obj to a json formatted string.
        """
        _put_header = {'content-type': 'application/json'}
        _response = self.session.put(self._infoblox_url + url,
                                  json.dumps(payload),
                                  headers=_put_header,
                                  auth=(self._infoblox_usr,
                                        self._infoblox_pwd))
        self._check_http_errors(_response) # check for communication errors
        _response_json = _response.json()
        self._check_api_errors(_response_json) # check for API errors

        # if there is nothing in the json response, return nothing
        if len(_response.text) <= 2:
            return None
        else:
            return _response_json

    def _delete_obj(self, obj):
        """
        Send DELETE to Infoblox, using saved WAPI URL and auths.

        Args:
            obj (str): _ref of object to delete

        Return:
            None or dict: None if no repsonse; Otherwise, JSON enocded content.
        """
        _response = self.session.delete(self._infoblox_url + obj,
                                 auth=(self._infoblox_usr, self._infoblox_pwd))
        self._check_http_errors(_response) # check for communication errors
        _response_json = _response.json()

        # if there is nothing in the response, return nothing
        if len(_response.text) <= 2:
            return None
        else:
            return _response_json

    def _search_records_for_name(self, name, zone):
        """
        Search all Infoblox records for a DNS name in a specific zone.
        If it already exists, return an Infoblox Name object.  Otherwise,
        return null (no records found).

        Args:
            name (str): DNS name.
            zone (str): Specified zone.

        Return:
            none or dict: None if no repsonse; Otherwise, JSON enocded content.
        """
        _request_url = 'allrecords?zone=' + zone + '&name=' + name
        return self._get_json(_request_url)

    def _search_records_for_host(self, ip):
        """
        Search all host records in Infoblox by IP.  If one already exists,
        this will return the host object reference. Otherwise, return null
        (no hosts for that IP found).

        Args:
            ip (str): IP address.

        Returns:
            none or dict: None if no repsonse; Otherwise, JSON enocded content.
        """
        _request_url = 'record:host?ipv4addr=' + ip
        return self._get_json(_request_url)

    def check_routefinder(self, ip):
        """
        Args:
            ip (str): ip address to check route for.

        Returns:
            Boolean False if no route found
            Message (str) if a route was found or other error
        """
        try:
            rf_result = self.routefinder.findroute(ip)
            route_info = rf_result['route']
            ## campus check
            if isinstance(route_info, str) and \
                    '0.0.0.0/0' in route_info:
                #logging.info(f'No route found for {ip} on core routers')
                return False
            ## datacenter check
            elif 'mac' not in route_info.keys():
                #logging.info(f'{ip} not found in ACI')
                return False
            else:
                return str(rf_result['message'])
        except:
            #logging.info('', exc_info=True)
            return str(rf_result['message'])

    #
    # Public functions
    #
    def get_dev_info(self):
        """
        Fetches the development information.

        Returns:
            str: Returns "Development" if ddi.utah.edu is not in _infoblox_url.
        """
        if "ddi.utah.edu" in self._infoblox_url:
            return "Production"
        else:
            return "Development"

    def get_subnet_types(self):
        """
        Get a list of valid subnet types, defined in settings.py.

        Returns:
            list: A list of strings.
        """
        return settings.SUBNET_TYPES

    def get_device_types(self):
        """
        Get a list of valid device types when adding hostnames. These are
        also defined in settings.py.

        Returns:
            list: A list of strings.
        """
        # Note: hopefully there will be an API call that returns available ones
        # for Infoblox extensible attributes
        return settings.DEVICE_TYPES

    def search_obj_types(self):
        """
        Provide list of specific object types used in search.

        Returns:
            list: A list of strings.
        """
        return settings.QUERY_OBJECT_TYPES

    def get_infoblox_servers(self, is_clinical=False):
        """
        Return a list of Infoblox servers (campus or clinical).

        Args:
            is_clinical (bool): Determines whether to return Campus or Clinical
                DHCP/DNS servers.

        Returns:
            list: A list of strings.
        """
        return (settings.CLINICAL_SERVERS if is_clinical
                else settings.CAMPUS_SERVERS)

    def add_comment(self, objectref, comment):
        """Add comment to objects

        Args:
            objectref (str): the _ref from Infoblox for the object
            comment (str): Any string, 256 character limit
        Returns:
            string: the put_response as a string (typically the _ref)

        """
        put_response = self._put_json(objectref, {'comment': comment})
        return str(put_response)

    ## Extensible Attributes
    def get_ea(self, target_ea):
        """List values for an extensible attribute

        Args:
            target_ea (str): the extensible attribute to get values for

        Returns:
            list: A list of the specified EAs' values.
        """
        if target_ea not in settings.ALL_EXTENSIBLE_ATTRIBUTES:
            raise ValueError ('Specified EA does not exist')

        ea_url = ('extensibleattributedef' +
                f'?name={target_ea.replace(" ", "+")}' +
                '&_return_fields=list_values')
        _get_response = self._get_json(ea_url)
        _ret = _get_response[0]["list_values"]
        val_list = []
        for val in range(len(_ret)):
            val_list.append(_ret[val]['value'])

        return list(sorted(val_list))

    def add_extensible_attr(self, objectref, ext_attr):
        """Add Extensible Attributes to target objects

        Args:
            objectref (str): the _ref from Infoblox for the object
            ext_attr (dict): extensible attributes and their values

        Returns:
            string: the put_response as a string (typically the _ref)

        #Extensible Attribute example:
        #{"extattrs": {
        #    "Device Type": {"value": "Client (DHCP)"},
        #    "Ticket Number": {"value": "INC0588054"}
        #    }
        }

        """
        put_response = self._put_json(objectref, ext_attr)
        return str(put_response)

    ## Records and DNS
    def add_hostname(self, ip, hostname, zone, devicetype, mac=None, alias=None,
                     force=False, update=True, ticketnumber=None):
        """
        Add a Host record to an existing Infoblox network. This requires an IP,
        the desired hostname, and a DNS zone.

        Args:
            ip (str): IP address of the host record.
            hostname (str): Hostname (not FQDN) of the host record.
            zone (str): DNS zone.
            devicetype (str): Device type as a string, which should be one of
                the options from get_device_types().
            mac (str): Optional - Used to associate a MAC address with the host.
                record for manual DHCP reservations.
            alias (str): Optional - Used to add a CNAME alias to the host
                record.
            force (bool): Optional - If set to True, overwrite existing records
                (if any).
            update (bool): Optional - If set to True, update an existing record
                instead of creating a new one.
            ticketnumber (str?): Optional ticket number to add to the record.

        Raises:
            ValueError or InfobloxObjectError: Caused for invalid inputs; Caused
            if there is a problem pushing records - for instance, if a record
            already exists and force is false.
        """
        # First, check all function input (device type, etc.)
        if devicetype not in settings.DEVICE_TYPES:
            raise ValueError("devicetype not in list of device types")

        # Check to see if the IP is valid
        _ip_info = self.get_ipaddr_info(ip)
        if _ip_info is None:
            raise ValueError("IP is not in a valid subnet")

        # Check to see if the hostname is already being used
        _result_name = self._search_records_for_name(hostname, zone)
        _result_host = self._search_records_for_host(ip)

        _hostrecord = { 'name': hostname + '.' + zone,
            'ipv4addrs': [{ 'ipv4addr': ip }],
            'extattrs': {
                "Device Type": { "value": devicetype }
            }
        }
        if mac is not None and mac.strip():
            _hostrecord['ipv4addrs'][0]['mac'] = mac.strip()

        if alias is not None and alias.strip():
            _hostrecord['aliases'] = [alias,]

        if ticketnumber is not None and ticketnumber.strip():
            _hostrecord['extattrs']["Ticket Number"] = {
                    "value": ticketnumber.strip() }

        def _put_host():
            _response = self._put_json(_result_host[0]['_ref'], _hostrecord)
            if not _response.startswith('record:host'): # should return host ref
                raise self.InfobloxObjectError(_response)

        if _result_name is not None:
            _result_dns = _result_name[0]['name'] +"."+ _result_name[0]['zone']
            if (_result_host is not None and
                    _result_dns in _result_host[0]['ipv4addrs'][0]['host']):
                # Update existing host record
                _put_host()
            else:
                raise self.InfobloxObjectError("Hostname already in use")
        elif _result_host is not None:
            # Update existing host record, if allowed
            if force and update:
                _put_host()
            elif force and not update:
                _response = self._post_json('record:host', _hostrecord)
                if not _response.startswith('record:host'): # should return host ref
                    raise self.InfobloxObjectError(_response)
            else:
                raise self.InfobloxObjectError("IP is already a Host")
        else:
            # add host to Infoblox
            _response = self._post_json('record:host', _hostrecord)
            if not _response.startswith('record:host'): # should return host ref
                raise self.InfobloxObjectError(_response)

    def add_alias(self, ip, alias):
        """
        Add an Alias (CNAME record) to a Host record. Note that the hostname
        must already be in Infoblox.

        Args:
            ip (str): IP address of the existing Host record.
            alias (str): Alias/FQDN string (includes zone).

        Raises:
            InfobloxObjectError: Caused if the existing Host record was not
            found by IP.
        """
        result_host = self._search_records_for_host(ip)
        hostrecord = { 'aliases' : [alias,] }

        response = self._put_json(result_host[0]['_ref'], hostrecord)
        if not response.startswith('record:host'): # should return host ref
            raise self.InfobloxObjectError(response)

    def add_fixed_address(self, ip, mac, devicetype, force=False,
            ticketnumber=None):
        """
        Add a fixed address to an existing Infoblox network. Note that this
        will also add a MAC address to a host record if there is no MAC already
        entered. Also note that this is different from add_host() in that this
        function does not require a host/DNS name.

        Args:
            ip (str): IP of the fixed address as a string.
            mac (str): MAC address for the fixed address as a string.
            devicetype (str): Device type as a string, which should be one of
                the options from get_device_types().
            force (bool): Optional - Defaults to false. If set to True,
                overwrite existing records (if any). If there is an active DHCP
                lease with a different MAC and this is False, this will fail.
            ticketnumber (str): Optional ticket number to add to the record.

        Raises:
            InfobloxObjectError: Caused if the DHCP lease is already in use, or
            is not already in a DHCP range.
        """
        # First, check all function input (device type, etc.)
        if devicetype not in settings.DEVICE_TYPES:
            raise ValueError("devicetype not in list of device types")

        # Check to see if the IP is valid
        _ip_info = self.get_ipaddr_info(ip)
        if _ip_info is None:
            raise ValueError("IP is not in a valid subnet")

        # Check to see if the IP has a lease
        _response_json = self._get_json('ipv4address?ip_address=' + ip +
                                        '&_return_fields=lease_state',
                                        skip_apicheck=True)

        if not isinstance(_response_json, dict):    # de-listify json response
            _response_json = _response_json[0]

        _lease_state = _response_json.get('lease_state', None)

        if _lease_state is None:
            raise ValueError("IP is not in DHCP range")

        if _lease_state == 'FREE' or force: # no lease, okay to take
            if "HOST" in _ip_info['types']:
                _reference = _ip_info['objects'][0]
                _record = { 'ipv4addrs': [{ 'ipv4addr': ip, 'mac': mac }],
                    'extattrs': { "Device Type": { "value": devicetype } }
                }

                if ticketnumber is not None and ticketnumber.strip():
                    _record['extattrs']["Ticket Number"] = {
                            "value": ticketnumber.strip() }

                _response = self._put_json(_reference, _record)
            else:
                _record = { 'ipv4addr': ip, 'mac': mac,
                    'extattrs': { "Device Type": { "value": devicetype } }
                }

                if ticketnumber is not None and ticketnumber.strip():
                    _record['extattrs']["Ticket Number"] = {
                            "value": ticketnumber.strip() }

                _response = self._post_json('fixedaddress', _record)
        else:
            raise self.InfobloxObjectError("DHCP lease is in use")

    def add_cname_record(self, cname, canonical, force=False):
        """
        Add or modify a CNAME record.

        Args:
            cname (str): Full hostname/FQDN as a string for the CNAME.
            canonical (str): Canonical/destination hostname.
            force (bool): Optional - Defaults to false. If true, overwrite an
                existing record.

        Raises:
            InfobloxObjectError: Caused if force is False and the record already
            exists or is not a CNAME.
        """
        _response = self.get_dns_record(cname)
        if _response is None: # record does not exist
            _response = self._post_json('record:cname', {
                "canonical": canonical,
                "name": cname,
            })
            if _response is not None:
                raise self.InfobloxObjectError(_response)
        elif "record:cname" in _response['type']:
            if force:
                _response = self._put_json(_response['_ref'], {
                    "canonical": canonical, })
            else:
                raise self.InfobloxObjectError("Record already exists")
        else:
            raise self.InfobloxObjectError("Record is not a CNAME")

    def get_ipaddr_info(self, ip):
        """
        Get information about a particular IPV4 address.

        Args:
            ip (str): IP address.

        Returns:
            None or dict: None if there is no existing record; otherwise, a
            dictionary with Infoblox information (reference, address, usage,
            etc.) will be returned.
        """
        _response_json = self._get_json('ipv4address?ip_address=' +
            ip, skip_apicheck=True)

        if _response_json is None:
            return None

        if not isinstance(_response_json, dict):    # de-listify json response
            _response_json = _response_json[0]

        if (_response_json.get('Error') and
                "network was not found for this address" in
                _response_json['Error']):
            return None
        else:
            return _response_json

    def search_hosts(self, searchstring):
        """
        Search Infoblox hosts with a given Regex string.

        Args:
            searchstring (str): a Regex.

        Returns:
            dict: A dictionary of hostnames and IP addresses.
        """
        _response_json = self._get_json(
                'search?objtype=record:host&search_string~=' + searchstring)

        if _response_json is None:
            return {}

        response = {}
        for host in _response_json:
            response[host['name']] = host['ipv4addrs'][0]['ipv4addr']

        return response

    def get_dns_record(self, hostname):
        """
        Get DNS Record information about a particular hostname. Note that the
        hostname must include the zone as well (an example would be
        test.net.utah.edu).

        Args:
            hostname (str): Full hostname/FQDN.

        Returns:
            dict: An Infoblox-formatted dictionary.
        """
        zone = hostname.partition('.')[2]
        name = hostname.partition('.')[0]
        _response_json = self._get_json('allrecords?zone=' +
                                        zone + "&name=" + name)
        if _response_json is None:
            return None

        recordtype = _response_json[0]['type'] + "?name="
        if "host_ipv4addr" in recordtype:
            recordtype = "record:host?name="
        elif "UNSUPPORTED" in recordtype: # a HOST record alias
            recordtype = "record:host?alias="

        _response2 = self._get_json(recordtype + hostname)
        _response2[0]['type'] = recordtype
        return _response2[0]

    def dig_subdomain(self, subdomain, nameserver=None):
        """
        Run a zone transfer and return a list of DNSRecord objects that
        represent a subdomain.

        Args:
            subdomain (str): The subdomain to transfer as a string.
            nameserver (str): Optional - Parameter for the specific nameserver
                to query.

        Returns:
            list: A list of DNSRecord objects. The objects' format is as
            follows:
            ('name': Record name
            'type': <'a', 'cname', 'mx', 'txt'>
            'data': <record data (IP if A record, etc.)>)
            Note that this is not a complete zone transfer - NS and SOA records
            are dropped.

        Raises:
            ValueError: Caused when an unknown record type is encountered.
        """
        if nameserver:
            nameserver = socket.gethostbyname(nameserver)
        else:
            nameserver = socket.gethostbyname(settings.NAME_SERVER)

        zxfr = dns.zone.from_xfr(dns.query.xfr(nameserver, subdomain))

        zonelist = []
        # sort names to be in DNSSEC order
        for n in sorted(zxfr.nodes.keys()):
            for dataset in zxfr[n].rdatasets:
                for dataitem in dataset.items:
                    if int(dataset.rdtype) == rdatatype.CNAME:
                        zonelist.append(self.DNSRecord(str(n), 'CNAME',
                                str(dataitem.target)))
                    elif int(dataset.rdtype) == rdatatype.A:
                        zonelist.append(self.DNSRecord(str(n), 'A',
                                str(dataitem.address)))
                    elif int(dataset.rdtype) == rdatatype.AAAA:
                        zonelist.append(self.DNSRecord(str(n), 'AAAA',
                                str(dataitem.address)))
                    elif int(dataset.rdtype) == rdatatype.MX:
                        zonelist.append(self.DNSRecord(str(n), 'MX',
                                (str(dataitem.preference),
                                str(dataitem.exchange))))
                    elif int(dataset.rdtype) == rdatatype.TXT:
                        zonelist.append(self.DNSRecord(str(n), 'TXT',
                                dataitem.strings[0].decode()))
                    elif int(dataset.rdtype) == rdatatype.SRV:
                        zonelist.append(self.DNSRecord(str(n), 'SRV',
                                (dataitem.priority, dataitem.weight,
                                dataitem.port, str(dataitem.target))))
                    elif int(dataset.rdtype) == rdatatype.SOA:
                        continue
                    elif int(dataset.rdtype) == rdatatype.NS:
                        continue
                    elif int(dataset.rdtype) == rdatatype.RP:
                        continue
                    else:
                        raise ValueError('Type ' + str(dataset.rdtype) +
                                ' not supported')
        return zonelist

    def generate_infoblox_dns_csv(self, zonelist, subdomain):
        """
        Generate an Infoblox-formatted CSV from DNS record data. The CSV
        format is defined in settings.py.

        Args:
            zonelist (list): A list of DNSRecord objects.
            subdomain (str): String specifying the domain for each
                record.

        Returns:
            A CSV string formatted to be able to be written directly to a file.
        """
        tld = subdomain.split('.')[-1] # get subdomain TLD
        # sort zonelist by record type, to simplify things
        zonelist = sorted(zonelist, key=lambda t: t[1])
        csvfile = settings.IMPORT_CSV_FORMAT
        for record in zonelist:
            fqdn = ((record[0] + '.' if record[0] and record[0] != '@' else '')+
                    subdomain)
            # enter in the record
            if record[1] == 'A':
                # A records: change to HostAddress and HostRecord
                csvitems = ["hostrecord", fqdn, record[2], 'TRUE', 'TRUE',
                        'FALSE', 'TRUE', 'FALSE', settings.NETWORK_VIEW,'FALSE',
                        'FALSE', 'Internal', 'Client (Static)']
                csvfile += ','.join(csvitems) + '\n'
                csvitems = ["hostaddress", record[2], fqdn, 'FALSE', 'TRUE',
                        '00:00:00:00:00:00', settings.NETWORK_VIEW, 'TRUE',
                        'Internal']
            elif record[1] == 'CNAME':
                csvitems = ["cnamerecord", fqdn, (subdomain if record[2] == '@'
                        else ((record[2].rstrip('.') + ('' if
                        record[2].rstrip('.').endswith(tld) else
                        ('.' + subdomain))))), 'STATIC', 'TRUE', 'FALSE',
                        'Internal']
            elif record[1] == 'MX':
                csvitems = ["mxrecord", fqdn, (record[2][1].rstrip('.') +
                        ('' if record[2][1].rstrip('.').endswith(tld) else
                        ('.' + subdomain))), str(record[2][0]), 'STATIC','TRUE',
                        'FALSE', 'Internal']
            elif record[1] == 'SRV':
                csvitems = ["srvrecord", fqdn, str(record[2][2]),
                        str(record[2][0]), (record[2][3].rstrip('.') + ('' if
                        record[2][3].rstrip('.').endswith(tld) else
                        ('.' + subdomain))), str(record[2][1]), 'STATIC','TRUE',
                        'FALSE', 'Internal']
            elif record[1] == 'TXT':
                csvitems = ["txtrecord", fqdn, record[2], 'STATIC', 'TRUE',
                        'FALSE', 'Internal']

            csvfile += ','.join(csvitems) + '\n'
        return csvfile

    def get_simple_device_list(self, subnet):
        """
        Get a non-detailed list of hosts from a certain subnet. This may be
        used to quickly calculate DHCP range utilization, etc.

        Args:
            subnet (str): Subnet IP and/or CIDR block as a string.

        Returns:
            dict: A list of dictionaries with Infoblox records per IP (IP & MAC
            address, usage, lease state, etc.)
        """
        if '/' not in subnet:
            _response = self.get_ipaddr_info(subnet)
            if _response is None:
                return None
            subnet = _response.get('network')

        _response_json = self._get_json('ipv4address?network=' + subnet +
                                        '&_return_fields=ip_address,' +
                                        'mac_address,usage,lease_state,' +
                                        'names,status,types,is_conflict' +
                                        '&_max_results=992')
        return _response_json

    ## Network
    def create_new_network(self, cidr, subnet_type=None, dhcp=False):
        """
        Create a new network with the first available subnet. The network
        container this function searches is determined by subnet_type.

        Args:
            cidr (int): CIDR size, from 16 to 32.
            subnet_type (str): Subnet type from SUBNET_TYPES in
                settings.py.
            dhcp (bool): A Boolean that enables or disables DHCP for that network.
                The first few addresses are not included in the DHCP range -
                this amount may also be modified in settings.py

        Returns:
            dict: The new subnet in an Infoblox dictionary, with the subnet
            address and size.
        """
        subnet_type = subnet_type.split('(')[0].rstrip()
        # Argument checks
        if (subnet_type is not None
                and subnet_type not in settings.SUBNET_TYPES):
            # subnettype was passed, but not defined in settings.py
            raise ValueError("Subnet type given is not defined")
        elif subnet_type is None:
            subnet_type = 'default'

        # get first available container, if there are nested containers
        _response_json = self._get_json(
            'networkcontainer?_return_fields=network')

        _net_containers = []
        for _nc in _response_json:
            if (IPNetwork(settings.SUBNET_TYPES[subnet_type]).ip
                in IPNetwork(_nc['network'])):
                _net_containers.append(_nc)

        _parent_container_id = _net_containers[-1]['_ref']

        # Then look for the first free subnet in the container
        _post_payload = {'cidr': int(cidr)}
        _response_json = self._post_json(_parent_container_id +
                                         '?_function=next_available_network',
                                         _post_payload)

        # Add the network with the discovered free space
        self.add_network(subnet=_response_json['networks'][0])
                # TODO figure out which failover association is the correct one

        # return chosen subnet
        return _response_json['networks'][0]

    def add_network(self, subnet, check_first=False):
        """
        Add a specific subnet to Infoblox.

        If the specific subnet IP is not already known, and the first available
        space just needs to be chosen, use create_new_network(type) instead.

        Args:
            subnet (str): Subnet IP and CIDR block as a string.
            check_first (bool): Optional - check if network already exists in
                Infoblox

        Raises:
            InfobloxObjectError: Caused if the subnet/network already exists.

        Returns:
            dict: Typically key will be the _ref for the newly created network
                with value being human readable subnet
        """

        if check_first:
            # Make sure the network does not already exist
            _response_json = self._get_json('network?network=' + subnet)
            if _response_json is not None:
                raise self.InfobloxObjectError("Network already exists")

            # check to see if the subnet is part of a larger network - we WANT
            # _ip_info to be blank so we don't overwrite anything
            _ip_info = self.get_ipaddr_info(str(IPNetwork(subnet).ip))
            if _ip_info is not None:
                raise self.InfobloxObjectError("network exists, part of " +
                        _ip_info['network'])

        # Actually allocate in Infoblox
        _post_payload = {'network': subnet}
        _post_response = self._post_json('network', _post_payload)
        return _post_response

    def add_rev_zone(self, network, nsgroup='Internal'):
        '''
        Create matching reverse zone for a network
        Prefix can be alphanumeric characters, such as 128/26 , 128-189 , or
        sub-B. We are going with a range for our standard.

        When network created, can only use 'auto_create_reversezone: True' if
            the network is /8, /16, /24. Infoblox does not allow reverse zones
            for /32 networks.

        These actually do go into the restart queue

        Args:
            network (str): The cidr form of the forward network
            nsgroup (str): The short name for DNS Name Server Group (see wizard)

        Returns:
            dict: Typically will be the _ref for the newly created network

        '''

        def gen_range(_net):
            """
            Returns appropriate range for specified network

            Alternatively, returns the last octet w/cidr: 128/26 which NIOS
            allows for reverse zone prefix
            """
            subnet = netaddr.IPNetwork(_net)
            ip_list = [ str(ip).split('.')[3] for ip in list(subnet) ]
            ## use groupby with lambda function as key to make consecutive keys and groups
            ## lambda expression subtracts i[1] from i[0], setting value as the key
            ## groupby generates a break or new group every time the value of the key function changes
            ## Example is [(0,128),(1,129)]: key will remain -128 until ^
            for key, group in groupby(enumerate(ip_list), lambda i: int(i[0]) - int(i[1])):
                ## map applies itemgetter to each item in iterable = group
                group = list(map(itemgetter(1), group))
                if len(group) > 1:
                    return str(f'{group[0]}-{group[-1]}')
                else:
                    return str(_net).split('.')[3]

        if nsgroup == 'Internal':
            _nsg = 'UofU - Internal - Reverse'
            _view = 'Internal'
        elif nsgroup == 'External':
            _nsg = 'UofU - External'
            _view = 'External'
        else:
            raise ValueError ('Invalid Name Server Group provided')

        network = netaddr.IPNetwork(network)
        try:
            if network.prefixlen in range(8,24,1):
                ## if the network provided has a cidr in the range 8-23, chunk it up
                ## and make as many individual /24 as needed
                logging.info('Making individual /24 reverse networks')
                subnets = list(network.subnet(24))
                subnet_list = [str(i) for i in subnets]
                for s in subnet_list:
                    _post_payload = {"fqdn":f"{s}", "zone_format":"IPV4", \
                                    "ns_group": f"{_nsg}", "view": f"{_view}"}
                    _post_response = self._post_json('zone_auth', _post_payload)
                _post_response = 'Making individual /24 reverse networks'
            elif network.prefixlen == '24':
                _post_payload = {"fqdn":f"{network}", "zone_format":"IPV4", \
                                "ns_group": f"{_nsg}", "view": f"{_view}"}
                _post_response = self._post_json('zone_auth', _post_payload)
            elif network.prefixlen in range(1,8,1):
                ## this should not be done, no good reason
                logging.info('Ma! They\'re posting weird shit again!')
                return {'error': "The hell you try'na do?!"}
            elif network.prefixlen in range(24,32,1):
                _prefix = gen_range(network)
                _post_payload = {"fqdn":f"{network}", "zone_format":"IPV4", "prefix": \
                                f"{_prefix}", "ns_group": f"{_nsg}", "view": f"{_view}"}
                _post_response = self._post_json('zone_auth', _post_payload)
            elif network.prefixlen == 32:
                #_prefix = str(network.ip).split('.')[3]
                #logging.info(f'Using prefix {_prefix}')
                #_post_payload = {"fqdn":f"{network}", "zone_format":"IPV4", "prefix": \
                #                f"{_prefix}", "ns_group": f"{_nsg}", "view": f"{_view}"}
                #_post_response = self._post_json('zone_auth', _post_payload)
                logging.info('Infoblox does not allow /32 reverse zones')
                _post_response = 'Infoblox does not allow /32 reverse zones'
        except:
            raise

        return {'result': _post_response}

    def add_dhcp(self, subnet):
        """
        Add a DHCP range to a network. Should be done using templates.

        Args:
            subnet (str): Subnet IP and CIDR block as a string.

        Raises:
            InfobloxObjectError: Caused if the subnet/network already exists.
        """
        # Fields required (besides subnet):
        # - comment

        # Make sure the network does not already exist
        _response_json = self._get_json('network?network=' + subnet)
        if _response_json is not None:
            raise self.InfobloxObjectError("Network already exists")

        # check to see if the subnet is part of a larger network - we WANT
        # _ip_info to be blank so we don't overwrite anything
        _ip_info = self.get_ipaddr_info(str(IPNetwork(subnet).ip))
        if _ip_info is not None:
            raise self.InfobloxObjectError("network exists, part of " +
                    _ip_info['network'])

        # finally, add network to Infoblox
        print("[dry run] adding subnet " + subnet)  # TODO
        #_response = self._post_json('network', {
        #    'network': subnet
        #})
        # note: this also needs to be added to the correct grid members

        # Add an automatic DHCP range after network creation, if requested
        _dhcp_start = IPNetwork(subnet)[settings.NUM_RESERVED_ADDRS + 1]
        _dhcp_end = IPNetwork(subnet)[-2] # don't include broadcast

        # add DHCP scope to new subnet
        print("[dry run] adding DHCP range to " +
              subnet + ": [" +
              str(_dhcp_start) +
              " - " + str(_dhcp_end) + "]") # TODO

    def next_avail_ips(self, target_net, quantity=1, use_range=False):
        '''
        Get the _ref of the network. Use this to get the next available IP. Pass
        to routefinder to validate they are not in use

        Add additional desired data: mac, comment, EA, etc. later

        Args:
            target_net (str): A network to get the next available ip(s) from
            quantity (int): The number of ips to gather, limit 20 per request
            use_range (bool): Use the range of the specified network instead

        Returns:
            dict: 'valid' key (list) for ip's that returned usable and 'error'
                    key (dict) for those ip's (key) that failed and the
                    associated message (value)
        '''

        try:
            if use_range:
                net_ref = self.get_dhcprange_info(target_net)["_ref"]
            else:
                net_ref = self.get_subnet_info(target_net)["_ref"]
        except TypeError:
            raise self.InfobloxObjectError ('Network or Range does not exist')

        valid_list = []
        error = {}
        func_ref = net_ref + '?_function=next_available_ip'
        exclude = []
        timeout = False
        start = time.time()
        na_target_net = netaddr.IPNetwork(target_net)

        ## handle the space reserved by NOC
        exc_range_upper = na_target_net
        exc_range_lower = na_target_net
        exc_range_lower.value += 1
        if na_target_net.prefixlen <= 27:
            exc_range_upper.value += 5
        else:
            exc_range_upper.value += 3

        try:
            exc_range = netaddr.IPRange(str(exc_range_lower.ip),
                    str(exc_range_upper.ip))
            logging.info(f'Range to exclude: {exc_range}')
            exclude = [str(i) for i in exc_range]
        except:
            raise

        ## Loop to get and validate requested number of ip's
        while len(valid_list) != int(quantity) and not timeout:
            if exclude:
                post_payload = {"num": 1, 'exclude': exclude}
            else:
                post_payload = {"num": 1} #"_function":"next_available_ip",

            ip = self._post_json(func_ref, post_payload)["ips"][0]
            try:
                rf_check = self.check_routefinder(ip)
                if isinstance(rf_check, bool) and not rf_check:
                    valid_list.append(ip)
                else:
                    #raise self.InfobloxRoutefinderError(rf_check)
                    error[ip] = rf_check
            except Exception as e:
                error[ip] = e

            exclude.append(ip)

            if ((time.time() - start)) > ((int(quantity) * 15)):
                timeout = True
                error['Timeout'] = 'Threshold reached...15 sec * quantity'
                logging.info('Timeout reached')

        return {'valid': valid_list, 'errors': error}

    def next_avail_subnets(self, container, cidr, quantity=1):
        """
        Create a specified quantity of networks within the specified container.

        Args:
            container (str): A container to get the next available network(s) from
            cidr (str): CIDR size, from 22 to 32. Will be converted to int.
            quantity (int): Optional - The number of networks to create

        Returns:
            dictionary: 'success' key is a dictionary of subnets (key) that were
            allocated and the _ref (value) for the new object and a 'failed'
            key (dict) those that failed (dict). 'refs' key (list) with _ref for
            each new network. A fourth key 'timeout' (str) will be added if
            timeout is reached.
        """
        ## Validate specified container
        _cont_ref = self._get_json(f'networkcontainer?network={container}')[0]['_ref']
        if not _cont_ref:
            return {'error': 'Invalid container provided'}

        # Then look for the first free subnet(s) in the container
        func_ref = _cont_ref + '?_function=next_available_network'
        exclude = []
        timeout = False
        start = time.time()
        net_dict = {'success': {}, 'failed': {}, 'refs': []}
        while len(net_dict['success']) != int(quantity) and not timeout:
            if exclude:
                post_payload = {"num": 1, 'cidr': int(cidr), 'exclude': exclude}
            else:
                post_payload = {"num": 1, 'cidr': int(cidr)} #"_function":"next_available_ip",

            response_json = self._post_json(func_ref, post_payload)

            # Add the network + reverse zone
            for n in response_json['networks']:
                ## handle NOC reserved space in network, find the first address a
                ## host could use
                net_obj = netaddr.IPNetwork(n)
                host_ip = net_obj
                if net_obj.prefixlen <= 27:
                    host_ip.value += 5
                else:
                    host_ip.value += 3
                rf_check = self.check_routefinder(str(host_ip.ip))
                if isinstance(rf_check, bool) and not rf_check:
                    try:
                        ## new_ref will be a string of the _ref
                        new_ref = self.add_network(n)
                        self.add_rev_zone(n)
                        net_dict['refs'].append(new_ref)
                        net_dict['success'].update({f'{n}': new_ref})
                    except Exception as e:
                        net_dict['failed'].update({f'{n}':f'{e}'})
                else:
                    net_dict['failed'].update({f'{n}': \
                                        'Route exists for network'})

            if ((time.time() - start)) > ((int(quantity) * 15)):
                timeout = True
                net_dict['timeout'] = 'Threshold reached...15 sec * quantity'
                logging.info('Timeout reached')

        return net_dict

    def get_subnet_info(self, subnet):
        """
        Get information about a subnet/IP network.

        Args:
            subnet (str): A subnet formatted as an IP/CIDR block.

        Returns:
            None or dict: None if there is no existing record; Otherwise, a
            dictionary with Infoblox information (reference, address, usage,
            etc.) will be returned.
        """
        IPNetwork(subnet) # test to make sure it's a valid IP
        _response_json = self._get_json('network?network=' + subnet,
                skip_apicheck=True)

        if _response_json is None:
            return None
        if not isinstance(_response_json, dict):    # de-listify json response
            _response_json = _response_json[0]

        return _response_json

    def get_dhcprange_info(self, subnet_ip):
        """
        Get information about DHCP range(s) from Infoblox.

        Args:
            subnet_ip (str): Subnet IP and/or CIDR block as a string.

        Returns:
            list: List of dictionaries with Infoblox records (reference,
            comments, options, etc.).
        """
        # two possible options: if the subnet given is in CIDR form, just use
        # that - otherwise, find the parent network
        if '/' not in subnet_ip:
            _response = self.get_ipaddr_info(subnet_ip)
            if _response is None:
                return None
            subnet_ip = _response.get('network')

        _response_json = self._get_json('range?network=' + subnet_ip +
            '&_return_fields=comment,network,start_addr,end_addr,options')

        if _response_json is None:
            _response_json = {} # exists, but no DHCP ranges
        return _response_json

    ## Miscellanous
    def restart_services(self, username='', dns=False, dhcp=False):
        """
        Force restart services to update/clear cache in Infoblox.

        Args:
            username (str): User name to tag to restart the service.
            dns (bool): If True, restart DNS services.
            dhcp (bool): If True, restart DHCP services.

        Raises:
            ValueError: Caused if all services given are False.
        """
        if not dns and not dhcp:
            raise ValueError("No services selected")

        # get grid object ID
        _response = self._get_json('grid')
        if not _response:
            raise ValueError("Could not get grid ID")

        grid_id = _response[0]['_ref']
        services = []
        if dns:
            services.append("DNS")
        if dhcp:
            services.append("DHCP")

        self._post_json(grid_id + '?_function=restartservices',
                {"restart_option": "RESTART_IF_NEEDED", "services": services,
                "user_name": username, })

    def object_query(self, obj, query, max_ret=500):
        """
        See wapi documentation for valid object references
            AllZone
            member:dns
            network
            networkcontainer
            networktemplate
            nsgroup
            rangetemplate
            record:a
            record:aaaa
            record:cname
            record:host
            record:mx
            record:ptr
            record:txt

        A search argument can use the following modifiers:
            Modifier    Functionality
            !           Negates the condition
            :           Makes string matching case insensitive
            ~           Regular expression search, Expressions are unanchored
            <           Less than or equal
            >           Greater than or equal

        Args:
            obj (str): the object type to reference, see above
            query: unanchored, case-insensitive regex to use as the search
            max_ret (int): Optional - Limit the number of items returned. Default is 500.
        Returns:
            list: list of dictionaries with the information for each matching object

        """

        search_url = 'search?objtype={}'.format(obj) +\
                    '&search_string:~={}'.format(query) +\
                    '&_max_results={}'.format(int(max_ret))
        response = self._get_json(search_url, skip_apicheck=True)

        return response
