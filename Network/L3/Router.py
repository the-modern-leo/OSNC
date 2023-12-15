### Local Package ###
from Network.L2.Switch import Stack, Blade, Neighbor
from Network.L1.Port import SFP, Interface,PortChannel
from Network.L2.Vlan import vlan


### Global Packages ###
import logging
import re
from ipaddress import IPv4Network,ip_network,ip_address,IPv4Address
from dateutil.relativedelta import relativedelta
from datetime import datetime
from netaddr import EUI, mac_cisco


def _exception(e):
    logging.error(e,exc_info=True)
    raise

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

class routing_protocol():
    def __int__(self):
        self.neighbors = None
        self.networks = None
        self.routerid = None
        self.ASNumber = None
        self.interfaces = []
        self.neighbors = []

    def assign_config_attributes(self,config_text):
        """
        Function for assigning all the aspects of the EIGRP
        """
        self.config_text = config_text
        self._assign_networks()
        self._assign_AS()
        self._assign_interface()
        self._assign_router_id()
        self._assign_vrf()
        self._assign_neighbors()

    def _assign_vrf(self):
        router_line = re.findall(r"router [A-Za-z]{0,10} [\d]{0,10}.*", self.config_text, re.MULTILINE)
        if "vrf" in router_line[0]:
            self.vrf = True
            self.vrfName = re.sub(r"router [A-Za-z]{0,10} [\d]{0,10} vrf ","",re.sub(r"\r", "", router_line[0]))

    def _assign_router_id(self):
        routerid = re.findall(r".*router-id.*$", self.config_text, re.MULTILINE)
        for id in routerid:
            id = re.sub("\r", "", id)
            ipaddress = re.sub(" router-id ", "", id)
            self.routerid = ip_address(ipaddress)

    def _assign_networks(self):
        """
        a list of the configuration lines for a network
        """
        try:
            self.networks = []
            networks = re.findall(r"network .*$",self.config_text,re.MULTILINE)
            for line in networks:
                r = Routing_Network()
                r.assign_config(line)
                self.networks.append(r)
        except:
            pass
    def _assign_AS(self):
        """
        grab the AS number
        """
        self.ASNumber = int(re.findall(r"router [A-Za-z]{0,10} ([0-9]{0,109}|[0-9]{0,109})",self.config_text, re.MULTILINE)[0])
    def _assign_interface(self):
        """
        Assign the interfaces associated with this routing protocol
        """
        self.interfaces = []
        interfaces = re.findall(r".*passive-interface .*$", self.config_text, re.MULTILINE)
        for int in interfaces:
            int = re.sub("\r", "", int)
            if "default" in int:
                self.passiveInterfaces = True
            elif "no passive-interface" in int and "Vlan" in int:
                v = vlan(re.sub("no passive-interface Vlan","",int))
                self.interfaces.append(v)
            elif "no passive-interface" in int:
                i = Interface()
                i.fullname = re.sub("no passive-interface ","",int)
                i.assign_config_attributes_from_full_name()
                i.shortname()
                self.interfaces.append(i)
    def _assign_neighbors(self):
        self.neighbors = [] = []
        neighborsText = re.findall(r"neighbor [\d]{0,3}.[\d]{0,3}.[\d]{0,3}.[\d]{0,3}", self.config_text, re.MULTILINE)
        for nei in neighborsText:
            nei = re.sub("\r", "", int)

class eigrp(routing_protocol):
    def __int__(self,*args, **kwargs):
        super(eigrp, self).__init__(*args, **kwargs)

class ospf(routing_protocol):
    def __int__(self,*args, **kwargs):
        super(ospf, self).__init__(*args, **kwargs)

class bgp(routing_protocol):
    def __int__(self,*args, **kwargs):
        super(bgp, self).__init__(*args, **kwargs)

class rip(routing_protocol):
    def __int__(self,*args, **kwargs):
        super(rip, self).__init__(*args, **kwargs)

class Router(Stack):
    """
    A router Object that extends the function of a Switch object
    """
    def __int__(self,*args, **kwargs):
        """
        :return:
        """
        self.object_results = None
        self.network_objects = None
        self.network_object_wrong = False
        super(Router, self).__init__(*args, **kwargs)

    def get_started(self):
        self.login()
        self.conn.enable_cisco()
        self.getSwitchInfo()
        self.assignattributes()
        self._get_route_protocols()
        self._sort_arp()
        pass

    def sort_object_groups(self):
        """
        Sorts the command 'Show Objects' on routers
        Returns:
        """
        network_objects = []
        objects = None
        if "object network" in self.object_results:
            objects = self.object_results.split('object network')
        for object in objects:
            if object == '':
                continue
            result = self._sort_object_lines(object)
            network_objects.append(result)
        self.network_objects = network_objects

    def _sort_object_lines(self,line):
        """

        Args:
            line (str): A string with Object \r\n dividing lines

        Returns:
            obj
        """
        network = None
        nobj = self.Network_Object()
        output = line.split('\r\n')
        nobj.name = output[0]
        for l in output:
            if 'subnet' in l:
                l = re.sub("subnet ","",l)
                l = ' '.join([x for x in l.split(' ') if x != ''])
                try:
                    if l == '0.0.0.0 0.0.0.0':
                        nobj.subnet.append('0.0.0.0 0.0.0.0')
                    else:
                        l = '/'.join([x for x in l.split(' ') if x != ''])
                        l = l.rstrip('\r')
                        nobj.subnet.append(IPv4Network(l))
                except Exception as e:
                    logging.error(e, exc_info=True)
                    _exception(e)
                    raise
        return nobj

    def _get_interface_physical(self, st):
        """
        Args:
            st (str): Takes in the a port configuration from show run, and handes back an interface object

        Returns (Interface): an Interface object
        """
        try:
            interface = Interface()
            interface.rawdata = st
            lines = st.split("\r\n")
            interface.fullname = lines[0]
            interface.fullname = re.sub(" ", "", interface.fullname)
            blandpo = lines[0]
            blandpo = re.sub("FortyGigabitEthernet", "", blandpo)
            blandpo = re.sub("TenGigabitEthernet", "", blandpo)
            blandpo = re.sub("TwoGigabitEthernet", "", blandpo)
            blandpo = re.sub("GigabitEthernet", "", blandpo)
            blandpo = re.sub("FastEthernet", "", blandpo)
            blandpo = re.sub("Ethernet", "", blandpo)
            blandpo = re.sub(" ", "", blandpo)
            blandpo = blandpo.split("/")
            if len(blandpo) > 2:  # the 3 number system
                interface.blade = int(blandpo[0])
                interface.portnumber = int(blandpo[2])
                interface.module = int(blandpo[1])
            else:
                interface.blade = int(blandpo[0])
                interface.portnumber = int(blandpo[1])

            for line in lines:
                reaesc = re.compile(r'\x1b[^m]*m')
                line = reaesc.sub('', line)
                line = line.replace('\r', '')
                if "switchport" in lines:  # layer 2 interface
                    if "description" in line:
                        interface.description = re.sub("description ", "", line)
                        interface.description = re.sub(" ", "", interface.description)
                    elif "trunk allowed vlan" in line or "trunk allowed vlan add" in line:
                        vlans = re.sub("switchport trunk allowed vlan add ", "", line)
                        vlans = re.sub("switchport trunk allowed vlan ", "", vlans)
                        vlans = re.sub("add", "", vlans)
                        vlans = re.sub(" ", "", vlans)
                        vlans = vlans.split(",")
                        for vla in vlans:
                            if "-" in vla:  # get all the vlans in this range
                                vl = vla.split("-")
                                for i in range(int(vl[0]), int(vl[1]) + 1):
                                    v = vlan(int(i))
                                    interface.trunkvlan.append(v)
                            else:
                                v = vlan(int(vla))
                                interface.trunkvlan.append(v)
                    elif "mode trunk" in line:
                        interface.trunk = True
                    elif "channel-group" in line:
                        po = PortChannel()
                        po.number = re.sub("channel-group ", "", line)
                        po.number = int(re.sub(" mode active", "", po.number))
                    elif "ip dhcp snooping trust" in line:
                        interface.snooping = True
                else:  # Layer 2 interface set up as Layer 3
                    if "mtu " in line:
                        interface.mtu = int(re.sub("mtu", "", line))
                    elif "ip address " in line:
                        ip, subnet = self._sort_l3_ip(line)
                        interface.ip = ip
                        interface.subnet = subnet

        except Exception as e:
            logging.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            return interface

    def _sort_l3_ip(self, line):
        """

        Args:
            line (str): the un edited interface line containing the ip address
            interface (Interface): the interface object you want updated

        Returns:
            (tuple): (ip_address,ip_network)
        """
        # sort a layer 3 network Address
        try:
            ipline = None
            line = re.sub("ip address ", "", line)
            line = re.sub("secondary", "", line).strip()
            if "255.255." in line:
                ipline = re.sub(" ","/",line)
            else: # ip is probably a network not an ip address
                ipline = re.sub(" ", "", line)
            subnet = ip_network(ipline,strict=False)
            ip = list(subnet.hosts())[1]
        except Exception as e:
            logging.info("Sorting 'show run | section interface | section Vlan' - failed")
            logging.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            return ip, subnet

    def sort_vlan_interfaces(self, vlan_interface_result):
        """
        This function sorts through every single interface on the device, and applies those interfaces to the blade object
        :param vlan_interface_result (str) a response from the command "show run | section interface":
        """
        logging.info("Sorting 'show run | section interface | section Vlan' - Starting")
        try:
            vlan_interface_result = vlan_interface_result.split('interface ')

            vlans = []
            for vlanstr in vlan_interface_result:
                # skip empty lines in the text results
                if vlanstr == "":
                    continue
                if 'remark' in vlanstr:
                    continue
                if 'Vlan1 ' in vlanstr: # skip vlan1
                    continue
                vlan = self._get_vlan(vlanstr)
                vlans.append(vlan)

            if vlans == []:
                raise
        except Exception as e:
            logging.info("Sorting 'show run | section interface | section Vlan' - failed")
            logging.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            self.vlansints = vlans
            logging.info("Sorting 'show run | section interface | section Vlan' - Success")

    def _get_vlan(self, vlanstr,V=None):
        """

        Args:
            vlanstr:

        Returns:

        """
        try:
            shutdown = None
            if "shutdown" not in vlanstr or "no shutdown" in vlanstr:
                shutdown = False
            if '!Command: show running-config interface ' in vlanstr:
                vlanstr = re.sub('!Command: show running-config interface ','',vlanstr)
            vlanlist = vlanstr.split('\r\n')
            # set the Vlan number
            if V:
                v = V
            else:
                v = vlan(int(re.sub("Vlan", "", vlanlist[0])))
                v.shutdown
            v.rawdata = vlanstr
            # get the Vlan configuration information
            for line in vlanlist:
                line = line.replace('\r', '')
                line = line.rstrip()
                line = line.strip()
                if "description" in line:
                    v.description = re.sub("description ", "", line)
                elif "vrf" in line:
                    v.vrf = re.sub("ip vrf forwarding ", "", line)
                    v.vrf = re.sub(" ", "", v.vrf)
                elif "no ip address" in line:
                    continue
                elif "ip address" in line:
                    ip, subnet = self._sort_l3_ip(line)
                    v.subnets.append(subnet)
                elif "ip helper-address" in line:
                    line = re.sub("ip helper-address ", "", line)
                    line = re.sub(" ", "", line)
                    line = re.sub("global", "", line)
                    v.helperip.append(ip_address(line))
                elif "shutdown" in line and "no" not in line:
                    v.shutdown = True

        except Exception as e:
            logging.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            return v

    def _get_mod_card(self, modeline):
        """
        This helper function will take in the mod line from the "show module" response, and returns
        a Blade Object
        Args:
            modeline (str):

        Returns (Blade):
        """
        try:
            blade = None
            SUP = False
            if "SUP" in modeline:
                SUP = True
            modeline = modeline.split(' ')
            modeline = [x for x in modeline if x]
            if self.blades:  # update the Blade with more information
                for b in self.blades:
                    if b.stacknumber == int(modeline[0]):
                        b.portcount = int(modeline[1])
                        b.modelnumber = modeline[len(modeline) - 2]
                        b.serialnumber = modeline[len(modeline) - 1]
                        b.SUP = SUP
                        modeline.remove(modeline[len(modeline) - 1])
                        modeline.remove(modeline[len(modeline) - 1])
                        modeline.remove(modeline[0])
                        modeline.remove(modeline[0])
                        b.cardtype = " ".join(modeline)
                        blade = b
                        break

            else:  # create a blade, and add the information
                b = Blade(modeline[len(modeline) - 1])
                b.stacknumber = int(modeline[0])
                b.portcount = int(modeline[1])
                b.modelnumber = modeline[len(modeline) - 2]
                b.SUP = SUP
                modeline.remove(modeline[len(modeline) - 1])
                modeline.remove(modeline[len(modeline) - 1])
                modeline.remove(modeline[0])
                modeline.remove(modeline[0])
                b.cardtype = " ".join(modeline)
                blade = b

        except Exception as e:
            logging.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            return blade

    def _get_mod_mac(self, macline):
        """
        This helper function will take in the Mac Addresses line from the "show module" response, and returns
        a Blade Object
        Args:
            macline (str):

        Returns (dict):
        """
        try:
            blade = None
            macline = macline.split(' ')
            macline = [x for x in macline if x]
            if self.blades:
                for b in self.blades:
                    if b.stacknumber == int(macline[0]):
                        b.hwversion = macline[len(macline) - 4]
                        b.fwversion = macline[len(macline) - 3]
                        b.ISOversion = macline[len(macline) - 2]
                        b.status = macline[len(macline) - 1]
                        macline.remove(macline[len(macline) - 1])
                        macline.remove(macline[len(macline) - 1])
                        macline.remove(macline[len(macline) - 1])
                        macline.remove(macline[len(macline) - 1])
                        macline.remove(macline[0])
                        b.macaddresses = " ".join(macline)
                        blade = b
                        break
            else:
                b = Blade()
                b.stacknumber = int(macline[0])
                b.hwversion = macline[len(macline) - 4]
                b.fwversion = macline[len(macline) - 3]
                b.ISOversion = macline[len(macline) - 2]
                b.status = macline[len(macline) - 1]
                macline.remove(macline[len(macline) - 1])
                macline.remove(macline[len(macline) - 1])
                macline.remove(macline[len(macline) - 1])
                macline.remove(macline[len(macline) - 1])
                macline.remove(macline[0])
                b.macaddresses = " ".join(macline)
                blade = b

        except Exception as e:
            logging.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            return blade

    def _get_serial(self, line):
        """
        Processes text, and removes only the Serial number. Only for processing show version Command.
        :param line (str): Takes the Line from the Version results

        :return (str): the Serial numbers
        """
        try:
            line = re.sub('System Serial Number', '', line[0])
            line = re.sub('System serial number', '', line)
            line = re.sub('Processor board ID', '', line)
            line = re.sub('Processor Board ID', '', line)
            line = re.sub(':', '', line)
            line = re.sub(' ', '', line)
        except Exception as e:
            logging.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            return [line]

    def _get_version(self, line):
        """
        Processes text, and removes only the version number. Only for processing show version Command.
        :param line (str): Takes the Line from the Version results

        :return (str): the Version
        """
        try:
            if self.nexus:
                line = re.sub("   system:    version ", "", line)
                line = re.sub("system:", "", line)
                line = re.sub("version", "", line)
                line = re.sub(" ", "", line)
            else:
                line = line.split(",")
                line = [x for x in line if "Version" in x]
                line = re.sub('version', '', line[0])
                line = re.sub('Version', '', line)
                line = re.sub('system:', '', line)
                line = re.sub(' ', '', line)
        except Exception as e:
            logging.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            return line

    def _get_uptime(self, line):
        """
        Processes text, and removes only the date and time info.
        Converts the text to datetime.datetime object
        :param line (str): Takes the Line from the Version results

        :return (datetime.dateime): the length of time the device has be running
        """
        text = ["years", "months", "weeks", "day", "hours", "minutes"]
        try:
            # filter out none useful info to a standard line
            line = re.sub(self.hostname, '', line)
            line = re.sub('uptime is', '', line)
            line = re.sub('Kernel', '', line)
            line = re.sub(' ', '', line)

            deltadic = self._create_time(line.split(","))
            # create a time object
            delta = None
            delta = relativedelta(year=-deltadic["years"],
                                  months=-deltadic["months"],
                                  weeks=-deltadic["days"],
                                  hours=-deltadic["hours"],
                                  minutes=-deltadic["minutes"])

            # create Datetime object
            lastrestart = datetime.now() - delta

        except Exception as e:
            logging.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            return (delta, lastrestart)

    def _create_time(self, timelist):
        """
        This is a helper function that creates a standard dictionary that can be passed into deltatime function
        Args:
            timelist (list): A list of ["1year","2months",...]

        Returns (dict): A diction to be fed into deltatime
        """
        try:
            deltadict = {"years": 0,
                         "months": 0,
                         "weeks": 0,
                         "days": 0,
                         "hours": 0,
                         "minutes": 0}

            for t in timelist:
                t = re.sub("s", "", t)
                t = re.sub("\(\)", "", t)
                if "years" in t or "year" in t:
                    deltadict["years"] = int(re.sub("year", "", t))
                if "months" in t or "month" in t:
                    deltadict["months"] = int(re.sub("month", "", t))
                if "weeks" in t or "week" in t:
                    deltadict["weeks"] = int(re.sub("week", "", t))
                if "days" in t or "day" in t:
                    deltadict["days"] = int(re.sub("day", "", t))
                if "hours" in t or "hour" in t:
                    deltadict["hours"] = int(re.sub("hour", "", t))
                if "minutes" in t or "minute" in t:
                    deltadict["minutes"] = int(re.sub("minute", "", t))

        except Exception as e:
            logging.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            return deltadict

    def _get_modelnumber(self, line):
        """
        Processes text, and removes only the model Number. Only for processing show version Command.
        :param line (str): Takes the Line from the Version results

        :return (str): the model number
        """
        try:
            if self.nexus:
                line = line.split(" ")
                line = [x for x in line if x]
                line = " ".join(line[1:3])
            else:
                line = line.split(" ")
                line = line[1]
        except Exception as e:
            logging.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            return line

    def _update_network_object(self,object):
        """
        Modifies the network object from the provided object
        Returns:
        """

    def _delete_network_object(self):
        """
        Removes the whole network object configuration from the provided object
        Returns:
        """
    def _create_network_object(self):
        """
        creates a network object from the provided object
        Returns:
        """

    def sort_one_vlan(self,v):
        """
        Takes a Vlan object, and adds all the Vlan information from a router into it.
        Args:
            v (Vlan): A vlan object

        Returns:
            v (Vlan):

        """
        try:
            self.login()
            v = self._get_vlan(self.conn.send_command(f"show run int Vlan {str(v.number)}"),v)
            self.logout(self.conn)
        except Exception as e:
            logging.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            return v
    def _get_route_protocols(self):
        self.route_protocols = []
        self.route_protocols_results = self.conn.send_command('show run | sec router ', manypages=True)
        router_configs = self.route_protocols_results.split("router ")
        for router in router_configs:
            if router == "":
                continue
            if "eigrp" in router:
                e = eigrp()
                e.assign_config_attributes("router " + router)
                self.route_protocols.append(e)
            if "ospf" in router:
                e = ospf()
                e.assign_config_attributes("router " + router)
                self.route_protocols.append(e)
            if "bgp" in router:
                e = bgp()
                e.assign_config_attributes("router " + router)
                self.route_protocols.append(e)
            if "rip" in router:
                e = rip()
                e.assign_config_attributes("router " + router)
                self.route_protocols.append(e)
    def _sort_sub_interface(self,interface_lines):
        """
        Sorts the routed interfaces on a port.
        """
        pass

    def _sort_arp(self):
        self.arps = []
        self.arp_result = self.conn.send_command('show ip arp', manypages=True)
        arps = re.findall(
            r"(Internet  ([\d]{0,3}.[\d]{0,3}.[\d]{0,3}.[\d]{0,3})\s*([\d]{0,3}|-)\s*([\da-z]{0,4}.[\da-z]{0,4}.[\da-z]{0,4})\s*ARPA\s*(Vlan([\d]{0,10})|[A-za-z]{0,20}([\d]{0,2}/[\d]{0,3}/[\d]{0,3}|[\d]{0,2}\/[\d]{0,3})))",
            self.arp_result, re.MULTILINE)
        for line in arps:
            a = arp_line()
            a.assign_arp(line)
            self.arps.append(a)

    # def find_port(self,ip=None,mac=None):
    #     neighbor_ip = None
    #     if ip:
    #         for arp in self.arps:
    #             if arp.ip == ip:
    #                 mac = arp.mac
    #     if mac:
    #         mac.dialect = mac_cisco
    #         mac_results = self.conn.send_command(f'show mac address-table | in {str(mac)}', manypages=True)
    #         result = re.findall(r"([A-Za-z]{0,10}[\d]{0,3}\/[\d]{0,3}|[A-Za-z]{0,10}[\d]{0,3}\/[\d]{0,3}\/[\d]{0,3})",mac_results)
    #         for neighbor in self.cdpneighbors:
    #             if neighbor.interface.short.lower() == result[0].lower():
    #                 neighbor_ip = neighbor.ip
    #         if not neighbor_ip:
    #             return self.get_interface_obj(result[0])
    #     if neighbor_ip:
    #         s = Stack(neighbor_ip)
    #         s.login()
    #         s.conn.enable_cisco()
    #         s.getSwitchInfo()
    #         s.assignattributes()
    #         s.find_port(mac)

class Routing_Network():
    def __int__(self):
        """
        :return:
        """
        self.object_results = None
        self.network_objects = None
        self.network_object_wrong = False
    def assign_config(self,line):
        self.network = None
        config_line = line
        line = re.sub("\r", "", line)
        wildcard = re.findall(
            r"network [\d]{0,3}.[\d]{0,3}.[\d]{0,3}.[\d]{0,3} ([\d]{0,3}.[\d]{0,3}.[\d]{0,3}.[\d]{0,3})",
            line, re.MULTILINE)
        line = line.split(" ")
        if len(line) >= 3:
            self.network = IPv4Network(line[1] + "/" + str(IPv4Address(int(IPv4Address(wildcard[0])) ^ (2 ** 32 - 1))))
        else:
            self.network = IPv4Network(line[1])
        if "area" in line:
            area = re.findall(r"network .* area ([\d]{0,3}.[\d]{0,3}.[\d]{0,3}.[\d]{0,3}|[\d])", config_line, re.MULTILINE)
            self.area = area[0]

class arp_line():
    def __int__(self):
        """
        :return:
        """
        self.ip = None
        self.mac = None
        self.interface = False
        self.vlan = None
    def assign_arp(self,arp_list):
        if "Vlan" in arp_list[0]:
            self.vlan = int(arp_list[5])
            self.mac = EUI(arp_list[3])
            self.ip = arp_list[1]
        else:
            self.interface = arp_list[4]
            self.mac = EUI(arp_list[3])
            self.ip = arp_list[1]

class VRF():
    def __init__(self,name,instancenumber):
        self.name = name
        self.instancenumber = instancenumber
