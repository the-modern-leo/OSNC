### Local Packages ###
from Network.Router import Router
from auth import SSH


### Global Packages ###
import re
import logging
from ipaddress import IPv4Address,IPv4Network


def _exception(e):
    logging.error(e,exc_info=True)
    raise


class CryptoMap:

    def __init__(self, concentrator_ip):
        self.object_local = None
        self.object_remote = None
        self.number = None
        self.insideips = []
        self.inside_network = []
        self.outsideip = None
        self.concentrator_ip = concentrator_ip

    def __str__(self):
        networks = ''
        if hasattr(self, "inside_network"):
            if isinstance(self.inside_network, set):
                for count, x in enumerate(self.inside_network):
                    if count == len(self.inside_network) - 1:
                        networks += f"{str(x)}\r\n"
                    else:
                        networks += f"{str(x)},"
            else:
                networks += f"{str(self.inside_network)}\r\n"
        ips = ''
        if hasattr(self, "insideips"):
            if isinstance(self.insideips, set):
                for count, x in enumerate(self.insideips):
                    if count == len(self.insideips) - 1:
                        ips += f"{str(x)}\r\n"
                    else:
                        ips += f"{str(x)},"
            else:
                ips += f"{str(self.insideips)}\r\n"

        string = f"----------------------------------------------------------\r\n" \
                 f"{self.object_remote if hasattr(self, 'object_remote') else ''}\r\n" \
                 f"{f'Concentrator: {self.concentrator_ip} to Inside Ip Addresses: {ips}' if hasattr(self, 'insideips') else ''}" \
                 f"{f'Concentrator: {self.concentrator_ip} to Inside Networks: {networks}' if hasattr(self, 'inside_network') else ''}" \
                 f"Public Ip address:{self.outsideip if hasattr(self, 'outsideip') else ''}\r\n"
        return string

class ASA(Router):
    def __init__(self, *args, **kwargs):
        self.snmp_host_group_wrong = False
        super(ASA, self).__init__(*args, **kwargs)

    def connect_to_ASA(self):
        """
        Figures out which ASA to log into, and creates a connection for that device
        Connection to device assigned to self.con
        """
        self.login()
        result = self.conn.send_command(f"sh run", manypages=True)
        result = result.split("\r\n")
        crypto_objs = []
        for line in result:
            if "access-list outside_cryptomap_" in line:
                c = CryptoMap(concentrator_ip=self.ip)
                line = re.sub("access-list outside_cryptomap_", "", line)
                c.number = line.split(' ')[0]
                line = ' '.join(line.split(' ')[1:])
                line = re.sub("extended permit ip any4 ", "", line)
                line = re.sub("extended permit ip ", "", line)
                line = re.sub("<--- More --->", "", line)
                if 'object-group' in line or 'object' in line:
                    object_groups = line.split('object-group')
                    object_groups = [x for x in object_groups if x]
                    object_groups = [x for x in object_groups if x != ' ']
                    if len(object_groups) == 1:
                        if 'host' in object_groups[0]:
                            object_groups_2 = object_groups[0].split('host')
                            object_local = [x for x in object_groups_2[0] if x]
                            object_local = [x for x in object_groups_2[0] if x != ' ']
                            object_local = ''.join(object_local)
                            c.object_local = object_local
                            object_remote = [x for x in object_groups_2[1] if x]
                            object_remote = [x for x in object_groups_2[1] if x != ' ']
                            c.insideips = IPv4Address(''.join(object_remote))
                        elif 'object' in object_groups[0]:
                            object_groups_2 = object_groups[0].split('object')
                            object_local = [x for x in object_groups_2[0] if x]
                            object_local = [x for x in object_groups_2[0] if x != ' ']
                            object_local = ''.join(object_local)
                            c.object_local = object_local
                            object_remote = [x for x in object_groups_2[1] if x]
                            object_remote = [x for x in object_groups_2[1] if x != ' ']
                            object_remote = ''.join(object_remote)
                            c.object_remote = object_remote
                        else:
                            object_remote = [x for x in object_groups[0] if x]
                            object_remote = [x for x in object_groups[0] if x != ' ']
                            object_remote = ''.join(object_remote)
                            c.object_remote = object_remote
                    elif len(object_groups) == 2:
                        object_local = [x for x in object_groups[0] if x]
                        object_local = [x for x in object_groups[0] if x != ' ']
                        object_local = ''.join(object_local)
                        c.object_local = object_local
                        object_remote = [x for x in object_groups[1] if x]
                        object_remote = [x for x in object_groups[1] if x != ' ']
                        object_remote = ''.join(object_remote)
                        c.object_remote = object_remote
                    crypto_objs.append(c)

        result = self.conn.send_command(f"show object-group", manypages=True)
        result = result.split("object-group network")
        for c in crypto_objs:
            for group in result:
                if group == '':
                    continue
                if hasattr(c, 'object_remote'):
                    if c.object_remote:
                        if c.object_remote in group:
                            lines = group.split("\r\n")
                            c.insideips = set()
                            c.inside_network = set()
                            for line in lines:
                                line = line.rstrip()
                                line = re.sub("\r", "", line)
                                if c.object_remote in line:
                                    continue
                                elif 'description' in line:
                                    continue
                                elif 'host' in line:
                                    ip = re.sub("network-object host ", "", line)
                                    ip = re.sub(" ", "", ip)
                                    ip = [x for x in ip if x]
                                    ip = [x for x in ip if x != ' ']
                                    ip = ''.join(ip)
                                    ip = IPv4Address(ip)
                                    c.insideips.add(ip)
                                    continue
                                else:
                                    line = re.sub("network-object ", "", line)
                                    if 'object' in line:
                                        continue
                                    line = line.split(' ')
                                    line = [x for x in line if x]
                                    line = [x for x in line if x != ' ']
                                    if len(line) == 2:
                                        ip = line[0]
                                        ip = re.sub(" ", "", ip)
                                        ip = [x for x in ip if x]
                                        ip = [x for x in ip if x != ' ']
                                        ip = ''.join(ip)
                                        subnet = line[1]
                                        subnet = re.sub(" ", "", subnet)
                                        subnet = [x for x in subnet if x]
                                        subnet = [x for x in subnet if x != ' ']
                                        subnet = ''.join(subnet)
                                        network = IPv4Network(f"{ip}/{subnet}")
                                        c.inside_network.add(network)
                                        continue
                                    else:
                                        pass
        if self.ip == '155.98.175.84':
            result = self.conn.send_command(f"show run crypto map", manypages=True)
        else:
            result = self.conn.send_command(f"show run | in CryptoMap map outside_map0", manypages=True)
        result = result.split("\r\n")
        crypto_numbers = set()
        for group in result:
            if group == '':
                continue
            number = re.sub("crypto map vpn ", "", group)
            number = re.sub('crypto map inside_map ', "", number)
            number = re.sub("CryptoMap map outside_map0 ", "", number)
            number = re.sub("\r", "", number)
            number = number.rstrip("\r")
            number = number.split(" ")
            number = [x for x in number if x]
            number = [x for x in number if x != ' '][0]
            if number == 'interface':
                continue
            crypto_numbers.add(int(number))

        grouped_crypto_lines = []
        for num in crypto_numbers:
            Crypto_group = []
            for group in result:
                number = re.sub("crypto map vpn ", "", group)
                number = re.sub('crypto map inside_map ', "", number)
                number = re.sub("CryptoMap map outside_map0 ", "", number)
                number = re.sub("\r", "", number)
                number = number.rstrip("\r")
                number = number.split(" ")
                number = [x for x in number if x]
                number = [x for x in number if x != ' '][0]
                if number == 'interface':
                    continue
                if int(number) == num:
                    Crypto_group.append(group)
            lines = '\r\n'.join(Crypto_group)
            grouped_crypto_lines.append(lines)

        crypto_dict = {}
        for lines in grouped_crypto_lines:
            line = lines.split("\r\n")
            for l in line:
                if "match address outside_cryptomap_" in l:
                    number = re.sub("match address outside_cryptomap_", "", l)
                    number = re.sub("\r", "", number)
                    number = number.rstrip("\r")
                    number = number.split(" ")
                    number = [x for x in number if x]
                    number = [x for x in number if x != ' ']
                    number = number[len(number) - 1]
                    crypto_dict[number] = lines

        for c in crypto_objs:
            for key, lines in crypto_dict.items():
                if c.number == key:
                    line = lines.split("\r\n")
                    for l in line:
                        if 'peer' in l:
                            ip = re.sub(f"set peer ", "", l)
                            ip = re.sub("crypto map vpn ", "", ip)
                            ip = re.sub("CryptoMap map outside_map0 ", "", ip)
                            ip = re.sub("\r", "", ip)
                            ip = ip.rstrip("\r")
                            ip = ip.split(" ")
                            ip = [x for x in ip if x]
                            ip = [x for x in ip if x != ' '][1]
                            ip = IPv4Address(ip)
                            c.outsideip = ip

        for c in crypto_objs:
            print(c)

    def assignattributes(self, con=None):
        """
        takes the responses from get switch info, and applies those responses to the object attributes

        """
        logging.info(f"Assigning Data to Router Object - Starting")
        try:
            self.sortVersion(versionresult=self.version_result)
            self.sort_acl()
            self.sort_object_groups()
            self.sortsnmp()

        except Exception as e:
            logging.info(f"Assigning Data to Router Object - Failed")
            logging.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            logging.info(f"Assigning Data to Router Object - Success")

    def getSwitchInfo(self):
        """
        Gathers all the essential information from the switch, and creates a switch object based off the
        results for better use in python coding projects
        Args:
            con (Connection): an active Parimko Connection to a switch

        """
        logging.info(f"Scraping Router Data - Starting")
        try:
            self.conn.enable_cisco(password=SSH.password)
            self.hostname = re.sub("hostname", "", self.conn.send_command('show run | inc hostname', manypages=True))
            self.hostname = re.sub(" ", "", self.hostname)
            self.hostname = self.hostname.rstrip("\r")
            self.version_result = self.conn.send_command('show version', manypages=True)
            self.acl_result = self.conn.send_command('show access-list',manypages=True)
            self.object_results = self.conn.send_command('show run object',manypages=True)
            self.snmp_result = self.conn.send_command('show run snmp-server', manypages=True)

        except Exception as e:
            logging.info(f"Scraping Router Data - Failed")
            logging.error(e, exc_info=True)
        else:
            logging.info(f"Scraping Router Data - Success")

    def sortVersion(self, versionresult):
        """
        This functions pulls out the Stack information, Version number, Model Number, Serial number,
        and switch uptime for the 'show version' response
        Args:
            versionresult (str): A response from running 'show version' on a switch
        """
        assert isinstance(versionresult, str), f'versionresult: must be str, but got {type(versionresult)}'
        logging.info("Sorting 'show Version' - Starting")
        try:
            # run code here
            # search through response to gather the indivigual info
            ver = versionresult.split('\r\n')

            for count, line in enumerate(ver):
                if line == '':
                    continue
                # discover if there is more than one blade in this stack by counting serial numbers
                if 'Serial Number: ' in line or 'System serial number' in line or 'Processor board ID' in line:
                    line = re.sub('System Serial Number', '', line)
                    line = re.sub('System serial number', '', line)
                    line = re.sub('Processor board ID', '', line)
                    line = re.sub('Serial Number: ', '', line)
                    line = re.sub(':', '', line)
                    line = re.sub(' ', '', line)
                    self.serial = line
                elif 'Device Manager Version' in line:
                    self.version = re.sub('Device Manager Version ','',line)
                elif 'Hardware: ' in line:
                    self.modelnumber = re.sub('Hardware: ','',line)
                    self.modelnumber = self.modelnumber.split(',')[0]
                    self.modelnumber = re.sub(' ', '', self.modelnumber)
                    pass

        except Exception as e:
            logging.info("Sorting 'show Version' - failed")
            logging.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            logging.info("Sorting 'show Version' - Success")