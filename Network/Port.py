import socket, re, logging, time, threading
from collections import namedtuple
from __future__ import print_function
from builtins import str
from builtins import range
from builtins import object
import sys, traceback, re, socket
from Network import Network
from collections import namedtuple
class Interface:
    """
    For collecting, and using Interface information for multiple interfaces on a device
    """

    def __init__(self):
        super(Interface, self).__init__()
        self.number = ''
        self.longtype = ''
        self.fullname = ''
        self.description = ''
        self.vlan = 0
        self.trunk = False
        self.trunkvlan = []
        self.voicevlan = ''
        self.dualmode = False
        self.stpf = False
        self.InOctets = None
        self.InUcastPkts = None
        self.InMcastPkts = None
        self.InBcastPkts = None
        self.outOctets = None
        self.outUcastPkts = None
        self.outMcastPkts = None
        self.outBcastPkts = None
        self.downtime = None
        self.portnumber = 0
        self.type = ''
        self.Duplex = None
        self.mgmt = False
        self.rawdata = None
        self.snooping = False
        self.blade = None
        self.neighbor = False
        self.mac_addresses = []
        self.portchannel = None
        self.power_admin = None
        self.power_oper = None
        self.power_power = None
        self.power_device = None
        self.Class = None
        self.Max = None
        self.empty = True

    def __repr__(self):
        return self.fullname
    def shortname(self):
        assert self.fullname != '', f'Interface must have a fullname before running shortname'
        self.short = re.sub('interface', '', self.fullname)
        self.short = re.sub('FastEthernet', 'Fa', self.short)
        self.short = re.sub(' ', '', self.short)
        self.short = re.sub('TenGigabitEthernet', 'Te', self.short)
        self.short = re.sub('GigabitEthernet', 'Gi', self.short)
        self.short = re.sub('FastEthernet1', 'Fa', self.short)
        self.short = re.sub('Ethernet100/', 'Eth', self.short)
        return self.short

    def run_config(self):
        """
        Returns (list): a run configuration for this Interface
        """
        if self.empty:
            interface_config = [f'{self.fullname}']
        else:
            interface_config = []
            interface_config.append(f"int {self.fullname}")
            interface_config.append(f"{f'description {self.description}' if self.description else ''}")
            interface_config.append(f"{'switchport mode trunk' if self.trunk else 'switchport mode access'}")
            interface_config.append(f"{f'switchport trunk allowed vlan {self.trunkvlan}' if self.trunkvlan else '!'}")
            interface_config.append(f"{f'switchport access vlan {self.vlan}' if self.vlan else '!'}")
            interface_config.append(f"{f'switchport voice vlan {self.voicevlan.rstrip()}' if self.voicevlan else '!'}")
            interface_config.append(f"{'ip dhcp snooping trust' if self.trunk else 'spanning-tree portfast'}")
        # f"""{self.fullname}
        # {f'description {self.description}' if self.vlan else ''}
        # {'switchport mode trunk' if self.trunk else 'switchport mode access'}
        # {f'switchport trunk allowed vlan {self.trunkvlan}' if self.trunkvlan else '!'}
        # {f'switchport access vlan {self.vlan}' if self.vlan else '!'}
        # {f'switchport access vlan {self.voicevlan}' if self.dualmode else '!'}
        # {'ip dhcp snooping trust' if self.trunk else 'spanning-tree portfast'}
        # !"""
        return interface_config

class PortChannel(Interface):

    def __init__(self):
        super(PortChannel, self).__init__()
        self.ponumber = None
        self.interfaces = []
        self.testthismethod = []

class SFP:
    def __init__(self):
        self.speed = None
        self.port = None
        self.SN = None
        self.type = None

TrunkChecked = namedtuple('TrunkChecked', ['switchname', 'vlan', 'message'])

class InvalidVlanError(Exception):
    """
    Raised when something is submitted in the VLAN box that is not just numbers.
    """
    pass

class FoundryError(Exception):
    """
    Raised when the program comes across a foundry switch
    """
    pass

class InvalidSwitchError(Exception):
    """
    Raised when the given or found IP/hostname of a switch does not exist on
    the DNS server
    """
    pass

class NoInputError(Exception):
    """
    This exception should be thrown when wither the vlan or switch inputs are
    empty.
    """
    pass

class TrunkChecker(object):
    """
    This class will take in a switch name and a vlan and will chack to see if
    that VLAN is trunked correctly on each of the connections up to the router.

    Args:
        switchaccess (SwitchAccess): Object for accessing and running
            commands on switches.
    """

    def __init__(self, switchaccess):
        self.switchaccess = switchaccess
        self.ip_pattern = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")

    def get_dev_info(self):
        """
        Returns production information.

        Returns:
            str: Returns "Dev"
        """
        return "Dev"

    def connect(self, switch):
        """
        This helper function will log into a switch.

        Args:
            switch (str): a DNS name or IP

        Returns:
            Connection: A connection to a switch that can be used with the
            SwitchAccess class
        """
        try:
            connection = self.switchaccess.login(switch)
            return connection
        except Exception as e:
            traceback.print_exc()
            raise e

    def config_analyzer(self, vlan, port_config):
        """
        This helper function detects if the port configuration contains the VLAN
        or if it has all VLANs trunked.

        Args:
            vlan (str): VLAN to search for.
            port_config (str): The config of the port.

        Returns:
            bool: True if VLAN is trunked, False if VLAN is not trunked.
        """
        # runs if all vlans are allowed through the trunk
        if 'allowed' not in port_config and 'trunk' in port_config:
            return True
        # these commands will trim the vlan list and parse
        # it so that compressed vlans (102-105) can be searched
        vlan_list = re.sub("[^0-9,-]", "",
                           port_config.split('allowed vlan', 1)[1].replace("\n", ","))
        vlan_list = vlan_list.split(',')
        for index, item in enumerate(vlan_list):
            if '-' in item and re.match("[0-9]", item[0]) and re.match("[0-9]", item[-1]):
                vlan_range = item.split('-')
                vlan_list[index] = vlan_range[0]
                num_between = int(vlan_range[1]) - int(vlan_range[0])
                for num_to_add in range(1, num_between + 1):  # ArraysStartAtOne
                    vlan_list.append(str(int(vlan_range[0]) + num_to_add))
        # this runs to see if the vlan is in the vlan list
        return vlan in vlan_list

    def clean_list(self, _string):
        """
        This is a helper frunction that will remove whitespace, new line, and
        return characters

        Args:
            _string (str): Input string.
        Returns:
            list: A list of strings.
        """
        _list = _string.replace('\r', ' ').replace('\n', ' ').split(' ')
        # _list = _list.replace('\n', ' ')
        # _list = _list.split(' ')
        _list = [_f for _f in _list if _f]

        return _list

    def find_next_hop(self, connection, cdp_port):
        """
        This is a helper function to find the IP of the next hop.

        Args:
            connection (Connection): The switch session.
            cdp_port (str): The port the neighbor is on.

        Returns:
            str: A string containing the IP of the next hop.
        """
        cdp_detail = connection.send_command('show cdp neighbor ' +
                                             cdp_port + ' detail')

        # If the output contains the word 'Invalid', we try the other syntax.
        if 'Invalid' in cdp_detail:
            cdp_detail = connection.send_command('show cdp neighbor int ' +
                                                 cdp_port + ' detail')
        cdp_detail = cdp_detail.split('Management')
        return self.ip_pattern.search(cdp_detail[-1]).group(0)

    def check_config(self, connection, cdp_port, vlan):
        """
        This function queries the switch for the config and then
        sends that to the helper method config_analyzer.

        args:
            connection (Connection): The switch session.
            cdp_port (str): The port the neighbor is on.
            vlan (str): VLAN to search for.

        returns:
            Trunked_status: a bool of whether or not it is trunked
        """
        port_config = connection.send_command("show run int " + cdp_port)
        # will run if there is a port channel
        if 'channel-group' in port_config:
            port_config = self.clean_list(port_config)
            for port_index, item in enumerate(port_config):
                if 'channel' in item:
                    port_channel = 'po' + port_config[port_index + 1]
                    trunked_status = self.config_analyzer(vlan,
                                                          connection.send_command('show run int ' +
                                                                                  port_channel))
        # will run if there is no port channel
        else:
            trunked_status = self.config_analyzer(vlan, port_config)

        return trunked_status

    def get_cdp_port(self, connection):
        """
        This function retrieves the trunk port information of the current
        switches neighbor both on this switch and the neighbor, and determines
        if the neighbor is a router or not.

        Args:
            connection (Connection): The current session with the switch.

        Returns:
            cdp_port (str): Contains the cdp port on this switch.
            cdp_port_on_neighbor (str): Contains the cdp port on the neighbor.
            is_router (bool): Determines if the neighbor is a router or not
        """
        cdp_port = None
        cdp_port_on_neighbor = None
        is_router = False
        neighbors = connection.send_command('show cdp ne')

        # This clean up the strings and shorten the list
        # so that there is not as much to search
        neighbors = self.clean_list(neighbors)
        # loops through the neighbors list, and pulls the port information if
        # there is a router as a neighbor
        for item_index, item in enumerate(neighbors):
            # This checks to determine if the array math done below can be
            # done or not, and forces it to check for a demarc instead
            if (item_index + 3) > len(neighbors):
                break
            # This runs if the program finds a neighbor
            if ('r1' in item or 'r2' in item):
                cdp_port = neighbors[item_index + 1] + neighbors[item_index + 2]
                print(cdp_port)
                is_router = True
            # this searches for the cdp port for the current switch on its
            # neighbor
            if cdp_port is not None and ('Eth' in neighbors[item_index + 3] or
                                         'Gig' in neighbors[item_index + 3] or 'Ten' in
                                         neighbors[item_index + 3]):
                cdp_port_on_neighbor = (neighbors[item_index + 3] +
                                        neighbors[item_index + 4])
                return cdp_port, cdp_port_on_neighbor, is_router
        # loops through the neighbors list, and pulls the port information if
        # there is not a router as a neighbor
        for item_index, item in enumerate(neighbors):
            # This checks to determine if the array math done below can be
            # done or not
            if (item_index + 3) > len(neighbors):
                raise IndexError
            # This runs if the program finds a neighbor
            if ('dx' in item):
                cdp_port = neighbors[item_index + 1] + neighbors[item_index + 2]
            # this searches for the cdp port for the current switch on its
            # neighbor
            if cdp_port is not None and ('Eth' in neighbors[item_index + 3] or
                                         'Gig' in neighbors[item_index + 3] or 'Ten' in
                                         neighbors[item_index + 3]):
                cdp_port_on_neighbor = (neighbors[item_index + 3] +
                                        neighbors[item_index + 4])
                break

        return cdp_port, cdp_port_on_neighbor, is_router

    def check_trunk_down(self, next_hop, cdp_port_on_neighbor, vlan):
        """
        This function checks the trunk on the neighbor to the current switch

        Args:
            next_hop (str): Contains the IP of the neighbor.
            cdp_port_on_neighbor (str): Contains the cdp port on the neighbor
                vlan

        Returns:
            bool: Determines whether or not it is trunked.
        """
        # This is necessary so that the finally statement does not throw an error
        # if this function runs into an error before connection is instantiated
        connection = None
        try:
            connection = self.connect(next_hop)
            is_trunked = self.check_config(connection, cdp_port_on_neighbor,
                                           vlan)
            return is_trunked
        except Exception as e:
            raise e
        finally:
            self.switchaccess.logout(connection)

    def check_vlan_list(self, switch, vlan):
        """
        This is the main function of the class. This function takes the switch
        and the vlan and determines if it correctly trunked to the router.

        Args:
            switch (str): The switch name.
            vlan (str): VLAN to be checked.

        Returns:
            TrunkChecked or str: a named Tuple if the function is done; if the
            program is not finished, it will return a string containing the
            neighbors IP.

        Raises:
            InvalidVlanError: When the VLAN is invalid
            NoInputError: when the parameters are not given
            InvalidSwitchError: When the switch IP or name is invalid
        """
        # This is necessary so that the finally statement does not throw an error
        # if this function runs into an error before connection is instantiated
        connection = None
        try:
            # This verifies that the user-inputed VLAN is only numbers between
            # 2-4095
            if not switch or not vlan:
                raise NoInputError("Please fill out both the Switch Name/IP " +
                                   "and VLAN fields.")
            vlan_user_check = re.search('[\D]', vlan)
            if vlan_user_check or int(vlan) > 4095 or int(vlan) < 2:
                raise InvalidVlanError("VLANS can only contain numbers " +
                                       "between 2 - 4095.")

            # this Tests to see if what is given as 'switch' is a valid switch
            # name/IP
            switch = socket.gethostbyaddr(switch)[0]
            connection = self.connect(switch)
            vlan_list = connection.send_command('show vlan br')
            # this is for foundry switches, which do not respond to cdp
            if 'nvalid' in vlan_list:
                raise FoundryError('Found a foundry')
            # runs if the vlan is in the vlan list
            if vlan in vlan_list:
                cdp_port, cdp_port_on_neighbor, is_router = self.get_cdp_port(
                    connection)
                # This will run if we can find a neighbor
                if cdp_port:
                    trunked_status = self.check_config(connection, cdp_port,
                                                       vlan)
                    # find the ip of the next hop
                    next_hop = self.find_next_hop(connection, cdp_port)
                    # this Tests to see if what is given as 'next_hop' is a valid
                    # switch name/IP
                    next_hop = socket.gethostbyaddr(next_hop)[0]
                    # this will run if the trunk is configured correctly
                    if trunked_status:
                        # check the trunked down status on the neighbor
                        is_trunked_down = self.check_trunk_down(next_hop,
                                                                cdp_port_on_neighbor, vlan)
                        if is_trunked_down:
                            if is_router:
                                return TrunkChecked(switch, vlan,
                                                    "VLAN " + vlan + " is trunked " +
                                                    " correctly to the router " + next_hop +
                                                    ".")
                            else:
                                return next_hop
                        else:
                            return TrunkChecked(switch, vlan,
                                                "The VLAN is not trunked down from " +
                                                next_hop + " to " + switch)

                    # This will run if the trunk is not configured correctly on
                    # the port
                    else:
                        return TrunkChecked(switch, vlan,
                                            "The trunk is not configured correctly from " +
                                            switch + " to its neighbor " + next_hop)

                # This will run if there is no demarc or router above this switch
                else:
                    # self.Network.logout(connection)
                    return TrunkChecked(switch, vlan,
                                        "Could not locate the switch above " + switch)

            # This will run if the VLAN is not built on the switch
            else:
                # self.Network.logout(connection)
                return TrunkChecked(switch, vlan,
                                    "The vlan does not exist on the switch " + switch)
        except FoundryError:
            return TrunkChecked(switch, vlan,
                                'Trunk Checker can not traverse Foundry Devices.')
        except socket.herror:
            return TrunkChecked(switch, vlan,
                                "IP found as the neighbor for " + switch +
                                " cannot be found in the DNS table.")
        except socket.gaierror:
            raise InvalidSwitchError(switch + " is not a valid switch name/IP.")
        except IOError:
            traceback.print_exc()
            return TrunkChecked(switch, vlan,
                                "Error: Could not log into " + switch + ".")
        except IndexError:
            return TrunkChecked(switch, vlan, "Could not find the neighbor for "
                                + switch + ".")
        finally:
            self.switchaccess.logout(connection)

class PortConfigCommon(object):
    """
    Common functions and utilities for Ports classes.
    """
    def verify_switchport(self, mt_result, connection=None, verify_vlan=None):
        """
        Verify switch port status/configuration for possible config changes. It
        will remain silent if the port is okay to change. It will throw an error
        if the port cannot be validated.

        Args:
            mt_result (tuple): Output from a MACFinder.search_switch() call.
            connection (Connection): Optional - SwitchAccess Connection object.
                    If given, this will run another command to check MAC
                    addresses on the port.
            verify_vlan (int): Optional - VLAN ID as an integer. If given, also
                    check VLAN status for that port.

        Raises:
            ValueError: If the port cannot be validated.
        """
        # convert mt_result, if needed
        if isinstance(mt_result, dict) and mt_result.get('maclocation'):
            mt_result = mt_result['maclocation']
        # instance test
        if (not hasattr(mt_result, 'port') or not hasattr(mt_result, 'message')
                or not hasattr(mt_result, 'simple_config')):
            raise ValueError("MACTracker result is not a MacLocation object")

        if not mt_result.port:
            raise ValueError("MACTracker could not discover the port on " +
                    str(mt_result.switchname))

        # check for a message from MACFinder
        if mt_result.message:
            if ('device is not reporting its mac' in mt_result.message.lower()
                    and not mt_result.port):
                raise ValueError("MAC Address not found on switch")
            else: # generic message
                raise ValueError("Error looking up switch port: " +
                        mt_result.message)


        # check for port channels
        if (mt_result.port.lower().startswith('po') or 'channel-group' in
                mt_result.simple_config.lower()):
            raise ValueError("Port " + mt_result.port + " is a port channel" +
                    " or is a part of a port channel")

        # check to make sure the port isn't already on that vlan, if ID is given
        if verify_vlan is not None:
            if ('switchport access vlan ' + str(verify_vlan)
                    ) in mt_result.simple_config:
                raise ValueError("Port " + mt_result.port +
                        " already configured on VLAN " + str(verify_vlan))
            if connection is not None:
                vlanlist = connection.send_command(
                        'show vlan brief | begin 1')
                vlanlist = [int(v.split()[0]) for v in vlanlist.splitlines()
                        if len(v.split()) > 1 and v.split()[0].isdigit()]
                if int(verify_vlan) not in vlanlist:
                    raise ValueError("VLAN ID " + str(verify_vlan) +
                            " is not configured on the switch")

        # check for Packetfence/802.1x configuration
        if ('authentication port-control auto' in mt_result.simple_config or
                'authentication order mab' in mt_result.simple_config):
            raise ValueError("Discovered port " + mt_result.port +
                    " is managed by PacketFence/802.1x")

        # check for trunked ports and key interfaces
        if 'switchport mode trunk' in mt_result.simple_config:
            # Trunked port on a cisco device
            raise ValueError("Discovered port " + mt_result.port +
                    " is a trunk port")
        if 'description key:' in mt_result.simple_config:
            raise ValueError("Discovered port " + mt_result.port +
                    " is a key interface")

        # also check Foundry ports, just in case
        foundry_config = mt_result.simple_config.splitlines()
        foundry_config = [line for line in foundry_config if 'Tagg' in line]
        if str(mt_result.port) in foundry_config:
            raise ValueError("Discovered port " + mt_result.port +
                    " is a tagged port (Foundry switch)")

        # check for multiple MAC addresses - if there's a bunch, there could
        # be an unmanaged switch, and changing the VLAN can break stuff
        if connection:
            maclist = connection.send_command(
                    'show mac address-table interface ' + mt_result.port +
                    ' | include ' + mt_result.port)
            if len(maclist.splitlines()) > 3:
                # 3 devices should be okay: phone VOIP + phone data + comp data
                raise ValueError("More than three MAC addresses discovered on "+
                        mt_result.port)

class PortInfo(object):
    """
    This class is designed to hold all of the information about
    a port that is needed for PortConfig. A simple class is used
    instead of a named Tuple so that the members are still mutable.

    Args:
        switch (str): Optional - the name or IP of the switch
        port (str): Optional - The port number 
        simple_config (str): Optional - The config of the port
        mac (str): Optional - the mac of the device on the port
        ip (str): Optional - the ip of the device
        enabled (bool): Optional - if the port is in shutdown or enabled
        description (str): Optional - short description tied to the port
        protected (bool): Optional - whether or not the port is protected
        message (str): Optional - a message that goes with the port
        connected (bool): Optional - whether or not the device is connected
    """
    def __init__(self, switch=None, port=None, simple_config=None, mac=None,
        ip=None, enabled=True, description='', protected=True, message=None,
        connected=False):
        self.switch = switch
        self.port = port
        self.simple_config = simple_config
        self.mac = mac
        self.ip = ip
        self.enabled = enabled
        self.description = description
        self.protected = protected
        self.message = message
        self.connected = connected

    def asdict(self):
        """
        this returns the members of the object as a dictionary

        Returns:
            dict: a dictionary containing the members of the object
        """
        return {'switch': self.switch, 'port': self.port,
                'simple_config': self.simple_config, 'mac': self.mac,
                'ip': self.ip, 'enabled': self.enabled,
                'description': self.description,
                'protected': self.protected, 'message': self.message,
                'connected': self.connected}

class PortConfig(PortConfigCommon):
    """
    This class is designed to enable the retrieval of information about a
    specific port based off of an IP, MAC, or switch information. It also
    enables the ability to enable/disable a port and change the ports
    description, given that it is not a protedcted port. The port protection
    status is determined by a method from the parent clsss PortConfigCommon,
    verify_switchport

    Args: 
        sa (SwitchAccess): A SwitchAccess object for logging into switches
        mc (MacFinder): A MacFinder object
        rf (RouteFinder): A RouteFinder object
    """

    def __init__(self, sa, mc, rf):
        self.switchaccess = sa
        self.mactracker = mc
        self.routefinder = rf
        self.threads = {}
        self.threadlock = threading.Lock()
        self.mac_pattern = re.compile("(\\b([\d]|[a-f]){4}\.([\d]|[a-f]){4}\." +
                "([\d]|[a-f]){4}\\b)")

    def get_port_info(self, port, thread_id=None, switch=None, connection=None,
             ip=None, keep_alive=False):
        """
        This method connects to a switch and gathers all information
        regarding a certain port on that switch

        Args:
            port (str): The port on the switch
            thread_id (int): Optional - the ID of the thread
            switch (str): Optional - the name of the switch
            connection (Connection): Optional - A SwitchAccess connection to the
                    switch
            ip (str): Optional - IP of the device connected to the port
            keep_alive (bool): Optional - whether or not to keep the connection 
                    alive

        Returns:
            PortInfo: A PortInfo object that contains the details of the port

        Raises:
            ValueError: When a connection to the switch cannot be established
        """
        try:
            if thread_id:
                self.update(thread_id, "Searching the switch...", None, False)
            verified = False
            if switch:
                host = socket.gethostbyaddr(switch)[0]
                connection = self.switchaccess.login(switch)
            elif connection:
                host, host_ip = self.mactracker.get_switch_name(connection)
                host = socket.gethostbyaddr(host_ip)[0]
            else:
                raise ValueError("No Switch or Connection given")

            port_output = connection.send_command("show run int " + str(port))
            if "nvalid" in port_output:
                raise ValueError("Invalid port number: " + str(port))

            port_info = PortInfo(host, port, port_output, 'unknown', 'unknown',
                    True, '', True, None)
            if ip:
                port_info.ip = ip
                verified = True

            port_output = port_output.split("\r\n")
            for line in port_output:
                if 'description' in line:
                    # remove the word description
                    port_info.description = line[13:]
                if 'shutdown' in line:
                    port_info.enabled = False

            mac_output = connection.send_command("show mac address-table " +
                    "interface " + port).split("Multicast")[0]
            if self.mac_pattern.search(mac_output):
                mac_list = self.mac_pattern.findall(mac_output)
                port_info.mac = mac_list.pop()[0]
                for mac in mac_list:
                    if mac[0] not in port_info.mac:
                        port_info.mac += "\n" + mac[0]

            if (not ip and "\n" not in port_info.mac and
                    'unknown' not in port_info.mac):
                port_info.ip = self.get_device_ip(port_info.mac,
                        thread_id=thread_id)

            if not verified:
                self.verify(port_info, connection, thread_id=thread_id,
                        info=port_info)

            port_info.connected = self.check_connection(connection, port,
                    thread_id=thread_id)

            return port_info
        except socket.gaierror:
            raise ValueError("Incorrect Switch name or IP: " + switch)
        except socket.herror:
            raise ValueError("Incorrect Switch name or IP: " + switch)
        finally:
            if connection is not None and keep_alive is False:
                self.switchaccess.logout(connection)

    def check_connection(self, connection, port, thread_id=None):
        """
        This helper method searchs the status of the port, to see if it is
        connected or not connected. The state of 'trunk' counts as connected

        Args:
            connection (Connection): A Network connection object
            port (str): the port to check the connection on
            thread_id (int): Optional - the id of the thread to send the update 
                    message to

        Returns:
            bool: True if the port has a connected device, false if the port 
            does not
        """
        if thread_id:
            self.update(thread_id, "Checking connectivity...", None, False)
        index = 0
        # strip the letters, because the user won't add them like the
        # switch will represent them
        for character in str(port):
            if str.isdigit(character):
                break
            index += 1
        connectivity = connection.send_command("show int status | include " +
                port[index:])
        if 'connected' in connectivity or 'trunk' in connectivity:
            return True
        return False

    def update_description(self, switch, port, description):
        """
        This method will replace the description of a port with the description
        given in the arguments

        Args:
            switch (str): switch name
            port (str): port number on switch
            description (str): description to be tagged to that port

        Returns:
            Portinfo: The info about the port
        """
        try:
            self.threadlock.acquire()
            connection = self.switchaccess.login(switch)
            connection.send_command('configure terminal')
            connection.send_command('interface ' + port)
            if description == '':
                connection.send_command("no description")
            else:
                connection.send_command('description ' + description)
            connection.send_command('end')
            connection.send_command('wri')
            data = self.get_port_info(port, connection=connection)
            return data
        finally:
            self.threadlock.release()


    def toggle_port(self, switch, port):
        """
        This method logs into a switch and will either disable or enable
        it, based on what state it is currently in

        Args:
            switch (str): switch name
            port (str): port on switch

        Returns:
            PortInfo: Info about the port 
        """
        try:
            self.threadlock.acquire()
            connection = self.switchaccess.login(switch)
            connection.send_command("configure terminal")
            connection.send_command("interface " + port)
            config = connection.send_command("do show run int " + port)
            if 'shutdown' in config:
                connection.send_command("no shutdown")
            else:
                connection.send_command("shutdown")
            connection.send_command("end")
            connection.send_command("wri")
            return self.get_port_info(port, connection=connection)
        finally:
            self.threadlock.release()

    def search_mac(self, mac_address, thread_id=None):
        """
        This method uses the mactrcker object to find where a mac
        address is located on the network, and gather the relavent
        information.

        Args:
            mac_address (str): a mac address to search
            thread_id (int): Optional - the ID of the thread to update

        Returns:
            PortInfo: The info about the port found

        Raises:
            ValueError: When the connection is broken or the direct port could 
                    not be found
        """
        if thread_id:
            self.update(thread_id, "Searching for MAC on the network...", None,
                   False)
        mac = self.mactracker.parse_mac(mac_address)

        mt_thread = self.mactracker.start_mactrack_thread(mac,
                keep_connection=True)

        while True:
            time.sleep(2)
            mt_result = self.mactracker.get_thread(mt_thread)
            if not mt_result:
                raise ValueError("MACTracker thread dissapeared")
            if mt_result['message'] is None:
                break
            if 'Not found' in mt_result['message']:
                raise ValueError("MAC Address not found on the Network")
            if mt_result['error'] is True:
                raise ValueError("MACTracker has run into an error: \n" +
                        mt_result['message'])
        mt_result, connection = self.mactracker.get_thread_and_connection(
                mt_thread, autodelete=True)

        mt_result = mt_result['maclocation']
        if connection is None:
            raise ValueError(
                    "Unable to keep a connection to the destination switch " +
                    mt_result.switchname)

        if not mt_result.port:
            raise ValueError("Could not find the direct port the MAC Address" +
                    " is currently on")

        try:
            # verify with MACTracker results
            result = self.verify(mt_result, thread_id=thread_id,
                    connection=connection)
            return result
        finally:
            if connection is not None:
                self.switchaccess.logout(connection)

    def get_device_ip(self, mac, thread_id=None):
        """
        This method uses the Tracker object to find the IP that is attached
        to and returns it

        Args:
            mac (str): A mac address
            thread_id (int): Optional - The ID of the thread

        Returns:
            str: An IP address if there is one tied to the mac, otherwise 
            returns unknown

        Raises:
            ValueError: When the thread is lost or the ID is incorrect
        """
        if thread_id:
            self.update(thread_id, "Searching for device IP...", None, False)
        mac = self.mactracker.parse_mac(mac)
        mt_thread = self.mactracker.start_mactrack_thread(mac)
        ip = 'unknown'
        while True:
            time.sleep(2)
            mt_result = self.mactracker.get_thread(mt_thread)
            if not mt_result:
                raise ValueError("MACTracker thread lost")
            # found the matching IP
            if (mt_result['maclocation'] and
                    mt_result['maclocation'].current_ip != ""):
                ip = mt_result['maclocation'].current_ip
                break
            if (mt_result['message'] is None or
                    'Not found' in mt_result['message']):
                break
        # terminate the thread
        self.mactracker.get_thread(mt_thread, autodelete=True)
        return ip

    def search_ip(self, ip, thread_id=None):
        """
        This method uses routefinder to get the mac address tied to an IP,
        then send that mac to search_mac

        Args:
            ip (str): the ip address to search for
            thread_id (int): Optional - The ID of the thread
        
        Returns:
            PortInfo: the info about the port

        Raises:
            ValueError: When the IP is not currently in use
        """
        if thread_id:
            self.update(thread_id, "Searching for MAC tied to the IP...", None,
                    False)
        ip_results = self.routefinder.findroute(ip)

        # passes through errors from routefinder
        if isinstance(ip_results['route'], str):
            raise ValueError(ip_results['route'])

        mac = ip_results['route']['mac']
        if not mac:
            raise ValueError("IP address is not currently in use")

        return self.search_mac(mac, thread_id=thread_id)

    def verify(self, maclocation, connection, thread_id=None, info=None):
        """
        This helper method uses the inherited method verify_switchport
        To ensure that a switchport is able to be changed or not, and return
        a dict of the relevant information

        Args:
            maclocation (Maclocation): a named tuple or object that has the 
                    required members
            connection (Connection): a Switchaccess connection to a switch
            thread_id (int): Optional - The ID of the thread
            info (PortInfo): a PortInfo object

        Returns:
            PortInfo: A PortInfo object with an accurate 'protected' field 
        """
        if thread_id:
            self.update(thread_id, "Checking if port is protected...", None,
                    False)
        if not info:
            info = self.get_port_info(maclocation.port,
                    thread_id=None, connection=connection,
                    ip=maclocation.current_ip, keep_alive=True)
        try:

            self.verify_switchport(maclocation, connection=connection)
            info.protected = False
            return info
        except ValueError as e:
            # This section would allow APs to be edited. It is
            # commented out in this iteration of the tool
            # if "AP" in str(e):
            #     info.protected = False
            #     return info

            # trim the message if need be
            error = str(e)
            if "AP" in error:
                error = error.split(".", 1)[0].split(": ")[1]
            info.message = (error + ".\n Contact a NOC Engineer to make any " +
                    "changes")
            return info

    def start_search(self, switch, port, mac, ip, get_thread=False):
        """
        This method should be the only one called by other programs
        to start searching for port datails. It starts the thread for searching
        for the port information, and can either return the thread id to
        check for updates, or a dictionary that contains a message and a
        PortInfo object after the thread has completed. It requires either an 
        IP, a MAC address, or a switch/port pair to function. 

        Args:
            switch (str): a switch name, or None
            port (str): a port number, or None
            mac (str): a mac address, or None
            ip (str): an IP address, or None
            get_thread (bool): Optional - True to get thread id, False to get 
                    dictionary of results
                    
        Returns:
            int or dict: the thread ID if get_thread is True; A dictionary 
            containing the keys message, data, and error if False
        """
        thread_id = int(round(time.time() * 1000))
        ssthread = SSThread(thread_id, switch, port, mac, ip, self)
        ssthread.start()
        self.update(thread_id, "Starting search...", None, False)
        if not get_thread:
            ssthread.join()
            return self.threads[thread_id]
        return thread_id

    def update(self, threadID, message, data, error):
        """
        Internal method only. This method updates the thread dictionary with any 
        information given, namely a message, data, or an error

        Args:
            threadID (int): the ID of the thread to be updated
            message (str): the message to store with the thread
            data (PortInfo): A PortInfo object
            error (bool): a boolean of whether there is an error or not
        """
        self.threadlock.acquire()
        self.threads[threadID] = {'message': message, 'data': data,
                'error': error, }
        self.threadlock.release()

    def status(self, thread_id):
        """
        This method checks the threads dictionary to see if a thread is alive
        and active, completed, or errored out. It deletes the thread if it is
        done.

        Arguments:
            thread_id (int): the id that is stored as a key in self.threads

        Returns:
            dict: Either a result dictionary with a dict of the PortObject, or 
            an error dictionary with a message
        """
        self.threadlock.acquire()
        thread_current = self.threads.get(int(thread_id), None)
        self.threadlock.release()
        if not thread_current:
            logging.error('warning: thread_id ' + str(thread_id) +' is invalid')
            return {'error': 'Invalid thread ID'}
        if thread_current and (not thread_current['message'] or
                thread_current['error']):
            self.threadlock.acquire()
            del self.threads[int(thread_id)]
            self.threadlock.release()
        if thread_current['error']:
            return {'error': thread_current['message']}
        else:
            if thread_current['data'] is not None:
                data_dict = thread_current['data'].asdict()
            else:
                data_dict = None
            if (data_dict and 'trunk' in str(data_dict.get('message')).lower()):
                data_dict['mac'] = 'N/A (trunk port)'
            return {'result': {'message': thread_current['message'],
                    'data': data_dict}}

class SSThread(threading.Thread):
    """
    This class contains the work that will be done to create a
    PortInfo Object. It is designated as a thread so that multiple
    instances can be called at a time. It requires either an IP, a MAC address, 
    or a switch/port pair to function. The other fields can be initialized as 
    None

    Args:
        threadID (int): the ID of the thread
        switch (str): the name or IP of the switch
        port (str): the port number on the switch
        mac (str): the mac address of the device on the port
        ip (str): the IP of the device on the port
        portconfig (PortConfig): a PortConfig object 
    """
    def __init__(self, threadID, switch, port, mac, ip, portconfig):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.switch = switch
        self.port = port
        self.ip = ip
        self.mac = mac
        self.portconfig = portconfig
        self.name = "Ports.GetPortInfo"

    def run(self):
        """
        Determines which set of data was given, and searches for the port info 
        based off of that. Looks for mac first, then switch/port, then IP. 
        """
        try:
            if self.mac:
                self.portconfig.update(self.threadID, "Searching for " +
                        self.mac + "...", None, False)
                result = self.portconfig.search_mac(self.mac,
                        thread_id=self.threadID)
            elif self.switch:
                self.portconfig.update(self.threadID, "Searching on " +
                        self.switch + "...", None,  False)
                result = self.portconfig.get_port_info(self.port,
                        thread_id=self.threadID, switch=self.switch)
            elif self.ip:
                self.portconfig.update(self.threadID, "Searching for " +
                        self.ip + "...", None, None)
                result = self.portconfig.search_ip(self.ip,
                        thread_id=self.threadID)
            self.portconfig.update(self.threadID, None, result, False)
        except Exception as e:
            self.portconfig.update(self.threadID, str(e), None, True)


