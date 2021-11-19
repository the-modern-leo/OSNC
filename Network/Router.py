### Local Package ###
from Network.Switch import Stack, Blade, Neighbor
from Network.Port import SFP, Interface,PortChannel
from Network.Network import Network_Object
from Network.Vlan import vlan


### Global Packages ###
import logging
import re
from ipaddress import IPv4Network,ip_network,ip_address
from dateutil import relativedelta
from datetime import datetime


def _exception(e):
    logging.error(e,exc_info=True)
    raise

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

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

    def getSwitchInfo(self):
        """
        Gathers all the essential information from the switch, and creates a switch object based off the
        results for better use in python coding projects
        Args:
            con (Connection): an active Parimko Connection to a switch

        """
        logging.info(f"Scraping Router Data - Starting")
        try:
            try:
                teststring = self.conn.send_command('enable', manypages=True)
            except ValueError:
                pass
            self.hostname = re.sub("hostname", "", self.conn.send_command('show run | inc hostname', manypages=True))
            self.hostname = re.sub(" ", "", self.hostname)
            self.hostname = self.hostname.rstrip("\r")
            self.version_result = self.conn.send_command('show version', manypages=True)
            if "r1-remote" in self.version_result:
                self.vlan_interface_result = self.conn.send_command('show run | section in Vlan',
                                                              manypages=True)
                self.interface_result = self.conn.send_command('show run | section in Ethernet',
                                                         manypages=True)
            elif "WS-C6509-E" in self.version_result or "C6816-X-LE" in self.version_result:
                self.vlan_interface_result = self.conn.send_command('show run | section interface Vlan',
                                                              manypages=True)
                self.interface_result = self.conn.send_command('show run | section in Ethernet',
                                                         manypages=True)
            else:
                self.vlan_interface_result = self.conn.send_command('show run | section Vlan',
                                                              manypages=True)
                self.interface_result = self.conn.send_command('show run | section interface | section Ethernet',
                                                         manypages=True)
                self.port_channel_result = self.conn.send_command('show run | section interface | section port-channel',
                                                            manypages=True)
            self.inv_result = self.conn.send_command('show inventory', manypages=True)
            self.portcount_result = self.conn.send_command('show interface counters', manypages=True)
            self.cdpnei_result = self.conn.send_command('show cdp nei detail', manypages=True)
            self.module_result = self.conn.send_command('show module', manypages=True)

        except Exception as e:
            logging.info(f"Scraping Router Data - Failed")
            logging.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            logging.info(f"Scraping Router Data - Success")

    def assignattributes(self):
        """
        takes the responses from get switch info, and applies those responses to the object attributes

        """
        logging.info(f"Assigning Data to Router Object - Starting")
        try:
            self.sortVersion(versionresult=self.version_result)
            self.sortInventory(self.inv_result)
            # gathers blades for chassis
            self.sortmodule(self.module_result)
            # sort interfaces seperately
            self.sortinterfaces(self.interface_result)
            # sort vlan information
            self.sort_vlan_interfaces(self.vlan_interface_result)
            # applies the uplinks
            self.sortCdpNeiDetail(self.cdpnei_result)
            self.sortportcounters(self.portcount_result)

        except Exception as e:
            logging.info(f"Assigning Data to Router Object - Failed")
            logging.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            logging.info(f"Assigning Data to Router Object - Success")

    def sortInventory(self, invresult='', ):
        """
        takes the string for Invresults, and grabs the serial numbers, SFPs, and blades for the system out of it.
        This assigns those values to Self.serial, self.SFPs, and self.blades
        Args:
            invresult (str): a result for 'show inventory'

        Returns ():
        """
        assert isinstance(invresult, str), f'invresult: must be str, but got {type(invresult)}'
        logging.info("Sorting 'show Inventory' - Starting")
        try:
            inv = invresult.split('NAME:')
            serial = []
            SFPs = []
            blades = []
            # get the serial number for the whole system
            for hdevice in inv:
                hdeviceparts = hdevice.split(',')
                # collect the blades in a Chassis
                name = hdeviceparts[0].replace('\"', '')
                name = name.replace('\"', '')
                name = name.replace('Slot ', '')
                if 'Switch System' in hdevice:
                    for line in hdeviceparts:
                        if 'SN:' in line:
                            switchserial = line.split(':')[1].rstrip()
                            serial.append(switchserial)
                            logging.info("Sorting 'show Inventory' - Success")

                elif 'System' in hdevice:
                    for line in hdeviceparts:
                        if 'SN:' in line:
                            switchserial = line.split(':')[1].rstrip()
                            serial.append(switchserial)
                            logging.info("Sorting 'show Inventory' - Success")

                # get the sfps that are in this device
                elif 'Transceiver' in hdevice:
                    Transceiver = SFP()
                    Transceiver.port = re.sub("Transceiver ", "", hdeviceparts[0].replace("\"", ""))
                    Transceiver.port = re.sub(" ", "", Transceiver.port.replace("\"", ""))
                    for line in hdeviceparts:
                        if 'DESCR:' in line:
                            word = line.split(" ")
                            for w in word:
                                if 'base' in w or "Base" in w:
                                    Transceiver.speed = w
                        if 'SN:' in line:
                            line = re.sub(" SN: ", "", line)
                            line = re.sub("SN: ", "", line)
                            line = line.replace('\r', '')
                            line = line.replace('\n', '')
                            line = re.sub(" ", "", line)
                            Transceiver.SN = re.sub("SN:", "", line.rstrip(""))
                    SFPs.append(Transceiver)

                elif 'N77-M348XP-23L' in hdevice:
                    serialnumber = None
                    for line in hdeviceparts:
                        if 'SN:' in line:
                            line = re.sub(" SN: ", "", line)
                            line = re.sub("SN: ", "", line)
                            line = line.replace('\"', '')
                            line = line.replace('\r', '')
                            line = line.replace('\n', '')
                            line = re.sub(" ", "", line)
                            serialnumber = re.sub("SN:", "", line.rstrip('\"'))
                    b = Blade(serialnumber)
                    b.stacknumber = int(name)
                    blades.append(b)
                elif 'N77-M324FQ-25L' in hdevice:
                    pass
                # get the blades in this chassis
                elif RepresentsInt(name):
                    serialnumber = None
                    for line in hdeviceparts:
                        if 'SN:' in line:
                            line = re.sub(" SN: ", "", line)
                            line = re.sub("SN: ", "", line)
                            line = line.replace('\"', '')
                            line = line.replace('\r', '')
                            line = line.replace('\n', '')
                            line = re.sub(" ", "", line)
                            serialnumber = re.sub("SN:", "", line.rstrip('\"'))
                    b = Blade(serialnumber)
                    b.stacknumber = int(name)
                    blades.append(b)

            if blades == set():
                raise ValueError("blades not assigned")

        except Exception as e:
            logging.info("Sorting 'show Inventory' - Failed")
            logging.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            logging.info("Sorting 'show Inventory' - Success")
            self.serial = serial
            self.SFPs = SFPs
            self.blades = blades

    def sortinterfaces(self, interface_result):
        """
        This function sorts through every single interface on the device, and applies those interfaces to the blade object
        :param interface_result (str) a response from the command "show run | section interface":
        """
        logging.info("Sorting 'show run | section interface | section Ethernet' - Starting")
        assert isinstance(interface_result, str), f"interface results must be str, got {type(interface_result)} instead"
        assert hasattr(self, 'blades'), f'the blades have not been set on this object'
        assert self.blades is not None, f'the blades have not been set on this object'
        try:
            # seperate each section into it's own string.
            interface_result = interface_result.split('interface ')

            interfaces = []
            for st in interface_result:
                if re.match('(?:(?:Ethernet|FastEthernet|GigabitEthernet|TwoGigabitEthernet|TenGigabitEthernet|FortyGigabitEthernet)(?:[\d][\/][\d]{0,2}[^\S]|[\d][\/][\d][\/][\d]{0,2}))',st):
                    if 'both' in st:
                        continue
                    interface = self._get_interface_physical(st)
                    interfaces.append(interface)

            for interface in interfaces:  # add the interface to the correct blade
                for b in self.blades:
                    if interface.blade == b.stacknumber:
                        b.interfaces[interface.portnumber] = interface

        except Exception as e:
            logging.info("Sorting 'show run | section interface | section Ethernet' - failed")
            logging.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            logging.info("Sorting 'show run | section interface | section Ethernet' - Success")

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
        nobj = Network_Object()
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

    def sortmodule(self, module):
        """
        Used to collect the blade information for chassis units.
        Args:
            module (str): A response from the command 'show module all'
            switchobj (Switch): A Switch Object

        Returns (Switch): a switch object with the blade objects
                            having been added
        """
        logging.info("Sorting 'show module all' - Starting")
        try:
            # create blade list if not already done
            if not self.blades:
                self.blades = set()
            # splits the response by breakdown
            module = module.split('Mod ')
            modulelist = []
            for m in module:
                if "Card Type" in m:
                    for line in m.split("\r\n"):
                        if "---" in line:
                            pass
                        elif "Mod" in line:
                            pass
                        elif "" == line:
                            pass
                        else:
                            blade = self._get_mod_card(line)
                            modulelist.append(blade)
                elif "MAC addres" in m:
                    for line in m.split("\r\n"):
                        if "---" in line:
                            pass
                        elif "MAC" in line:
                            pass
                        elif "" == line:
                            pass
                        else:
                            blade = self._get_mod_mac(line)
                            modulelist.append(blade)
                elif "Sub-Module" in m:
                    pass
                elif "Online Diag Status" in m:
                    pass
        except Exception as e:
            logging.info("Sorting 'show module all' - failed")
            logging.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            logging.info("Sorting 'show module all' - Success")
            return

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

    def sortVersion(self, versionresult=''):
        """
        This functions pulls out the Stack information, Version number, Model Number, Serial number,
        and switch uptime for the 'show version' response
        Args:
            versionresult (str): A response from running 'show version' on a switch
            :param chassislist (list): A List of models that are switch chassis
        """
        assert isinstance(versionresult, str), f'versionresult: must be str, but got {type(versionresult)}'
        logging.info("Sorting 'show Version' - Starting")
        try:
            # run code here
            # search through response to gather the indivigual info
            if "Cisco IOS Software" in versionresult:
                self.nexus = None
            elif "Cisco Nexus Operating System" in versionresult:
                self.nexus = True
            else:
                self.nexus = None

            ver = versionresult.split('\r\n')

            # Begin the looping to gather all the information needed
            for count, line in enumerate(ver):
                # locate Nexus Info
                if self.nexus:
                    if "system:" in line:
                        self.version = line
                    elif "Hardware" in line:
                        self.modelnumber = ver[count + 1]
                    elif "Processor Board ID" in line:
                        self.serial = []
                        self.serial.append(line)
                    elif "Kernel uptime is" in line:
                        self.uptime = line
                else:  # locate ISO Info
                    # get the Serial # info
                    if "Processor board ID" in line:
                        self.serial = []
                        self.serial.append(line)
                    # get Version Info
                    elif "Cisco IOS Software" in line and "Version" in line:
                        self.version = line
                    # get up time Info
                    elif "uptime is" in line:
                        self.uptime = line
                    # get Model # info
                    elif "processor" in line and "Cisco" in line:
                        self.modelnumber = line

            # process Serial Number
            self.serial = self._get_serial(self.serial)

            # process Version Info
            self.version = self._get_version(self.version)

            # process uptime info
            self.uptime, self.lastrestart = self._get_uptime(self.uptime)

            # process Model #
            self.modelnumber = self._get_modelnumber(self.modelnumber)

        except Exception as e:
            logging.info("Sorting 'show Version' - failed")
            logging.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            logging.info("Sorting 'show Version' - Success")

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

    def sortCdpNeiDetail(self, cdpnei):
        """
        This function pulls the neighboring device information from the command 'show cdp nei detail' creating a neighbor
        obj for each cdp neighbor while marking the interfaces with that object as well. Assigns all the objects to
        the self.cdpneighbors list

        Args:
            cdpnei (str): ipaddress of uplink switch

        """
        assert isinstance(cdpnei, str), f'cdpnei must be a str, got {type(cdpnei)}'
        assert cdpnei is not None, f'cdpnei is an empty string. please pass through response from "show cdp nei detail"'
        logging.info("Sorting 'show cdp nei detail' - Starting")
        try:
            # seperate out all the CDP Sections
            cdpneidetail = cdpnei.split('-------------------------')
            neighbors = []
            for neighborstr in cdpneidetail:
                if neighborstr == "":
                    continue
                neighborobj = self._get_neighbor(neighborstr)
                neighbors.append(neighborobj)

        except Exception as e:
            logging.info("Sorting 'show cdp nei detail' - Failed")
            logging.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            logging.info("Sorting 'show cdp nei detail' - Success")
            self.cdpneighbors = neighbors

    def _get_neighbor(self, neighborstr):
        """
        sorts through the cdp neigbor sections, creates a neigbor obj, assigns all the attributes, and returns the object
        Args:
            neighborstr:

        Returns:

        """
        try:
            localportnumber = None
            localport = None
            neighborlist = neighborstr.split("\r\n")
            neighborlist = [x for x in neighborlist if x]
            n = Neighbor()
            n.deviceid = re.sub("Device ID: ", "", neighborlist[0])
            for line in neighborlist:
                if "IP address:" in line or "IPv4 Address:" in line or re.match('[\d]{0,3}\.[\d]{0,3}\.[\d]{0,3}\.[\d]{0,3}',line):
                    line = re.sub("IP address:", "", line)
                    line = re.sub("IPv4 Address:", "", line)
                    line = re.sub("IP address:", "", line).rstrip('\r')
                    line = re.sub("\r", "", line)
                    line = line.split(" ")
                    line = [x for x in line if x]
                    n.ip = ip_address(line[0])
                elif "Device ID:" in line:
                    n.deviceid = re.sub("Device ID: ", "", line)
                elif "Platform:" in line:
                    line = re.sub("Platform: ", "", line)
                    line = re.sub(" ", "", line)
                    n.platform = line.split(",")[0]
                elif "Interface:" in line:
                    line = re.sub("Interface: ", "", line)
                    line = re.sub(" ", "", line)
                    line = line.split(",")
                    localport = line[0]
                    localport = self._get_interface_numbers(localport)
                    localport = localport.split("/")
                    if len(localport) > 2:
                        localportnumber = localport[2]
                    else:
                        if 'mgmt0' in localport:
                            localportnumber = 'mgmt0'
                        else:
                            localportnumber = localport[1]
                    remoteport = re.sub("PortID(outgoingport):", "", line[1])
                    remoteport = self._get_interface_numbers(remoteport)
                    remoteport = remoteport.split("/")
                    if len(localport) > 2:
                        remoteportnumber = remoteport[2]
                    else:
                        remoteportnumber = remoteport[1]
                    i = Interface()
                    i.portnumber = remoteportnumber
                    i.blade = remoteport[0]
                    i.rawdata = line[1]
                    n.remote_interface = i
                    if localportnumber != 'mgmt0':
                        for blade in self.blades:  # assign the interface obj to the neighbor object
                            if blade.stacknumber == int(localport[0]):
                                localint = blade.interfaces[int(localportnumber)]
                                n.interface = localint
                                break
                elif "VTP Management Domain:" in line or "VTP Management Domain Name:":
                    n.VTPDomain = re.sub("VTP Management Domain: ", "", line)
                    n.VTPDomain = re.sub(" ", "", n.VTPDomain)
                elif "Duplex:" in line:
                    n.duplex = re.sub("Duplex: ", "", line)
                    n.duplex = re.sub(" ", "", n.duplex)

            # assign the neigbor object to the interface
            if localport:
                for blade in self.blades:
                    if blade.stacknumber == localport[0]:
                        localint = blade.interfaces[localportnumber]
                        localint.neighbor = n
        except Exception as e:
            logging.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            return n

    def _get_interface_numbers(self, intstr):
        """
        This function will remove all the letters in an interface leaving just the numbers, and special characters
        Args:
            intstr (str): any interface title

        Returns (str): just stack/module/port numbers or vlan number
        """
        try:
            intstr = re.sub("FortyGigabitEthernet", "", intstr)
            intstr = re.sub("TenGigabitEthernet", "", intstr)
            intstr = re.sub("TwoGigabitEthernet", "", intstr)
            intstr = re.sub("GigabitEthernet", "", intstr)
            intstr = re.sub("FastEthernet", "", intstr)
            intstr = re.sub("Ethernet", "", intstr)
            intstr = re.sub(" ", "", intstr)
        except Exception as e:
            logging.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            return intstr

    def update_orion_migration(self, switch_connection):
        """
        Update logging, SNMP, and ACL for the Orion migration.
        """
        logging.info("Orion Migration: Updating - Starting ")
        try:
            if self.network_objects_wrong:
                for object in self.network_objects:
                    if 'Monitoring' in object.name.lower():
                        self._update_network_object(object)
            if self.snmp_group_wrong:
                pass
            if self.snmp_user_wrong:
                pass
            if self.snmp_host_group_wrong:
                pass
            if self.snmp_logging_wrong:
                pass
        except Exception as e:
            logging.info("Orion Migration: Updating - Failed ")
            logging.error(e, exc_info=True)
        else:
            logging.info("Orion Migration: Updating - Success ")

    def _update_SNMP(self, object):
        """
        Modifies the network object from the provided object
        Returns:
        """

    def _delete_SNMP(self):
        """
        Removes the whole network object configuration from the provided object
        Returns:
        """

    def _create_SNMP(self):
        """
        creates a network object from the provided object
        Returns:
        """

    def write_SNMP(self):
        """
        Writes the configuration of a network object to the device
        Returns:
        """

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


class VRF():
    def __init__(self):
        pass