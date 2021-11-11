from __future__ import absolute_import
from builtins import next
from builtins import str
from builtins import range
from past.builtins import basestring
from builtins import object
import traceback, re, os, jinja2, logging
from netaddr import IPAddress, IPNetwork


class vlan:
    """
    This object is for gathering information about multiple vlans that are attached to a device
    """
    def __init__(self, number):
        self._number = number
        self.number = number
        self.name = ''
        self.voice = False
        self.interfaces = []
        self.description = None
        self.rawdata = None
        self.network = None
        self.ipaddress = None
        self.interface = None
        self.helperip = []
        self.subnets = []
        self.vrf = None
        self.shutdown = True
        self.mac_addresses = []

    def __eq__(self, other):
        if not isinstance(other, vlan):
            return NotImplemented
        return self.number == other.number
    def __hash__(self):
        return hash(self._number)

class VLANConfig(object):
    """
    VLAN configuration module. This generates VLAN configs and Wireless VLAN
    configs, as well as provides tools to find information about reserving
    subnets.

    Args:
        routefinder_checker (func): Finds route.
        infoblox_checker (func): Gets subnet info.
        infoblox_servers (func): Gets Infoblox servers
        orion_vlan (func): Gets vlans.
        orion_poll (func): Forces a poll.
        building_getter (func): Gets building.
        poc_checker (func): Searches POC.
    """
    def __init__(self, routefinder_checker, infoblox_checker, infoblox_servers,
            orion_vlan, orion_poll, building_getter, poc_checker):
        self.routefinder_checker = routefinder_checker
        self.check_infoblox = infoblox_checker
        self.get_infoblox_servers = infoblox_servers
        self.get_orion_vlan = orion_vlan
        self.force_orion_poll = orion_poll
        self.get_building = building_getter
        self.poc_checker = poc_checker

    class VLANConfigError(Exception):
        """
        A VLANConfigError is a generic error for this object.
        """
        pass

    def get_dev_info(self):
        """
        Gets development information.

        Returns:
            str: Returns "Production".
        """
        return "Production"

    def check_free_subnet(self, subnet):
        """
        Check a particular subnet and make sure it isn't routed or used in
        Infoblox.

        Args:
            subnet (str): Subnet to be checked.

        Returns:
            bool or str: Returns true if subnet is free; Otherwise returns
            errors.
        """
        error = []
        # first: check Infoblox (split subnet/cidr anyway)
        ipinfo = self.check_infoblox(subnet.split('/')[0])
        if ipinfo:
            error.append('exists in Infoblox')

        # next: check POC if available
        if self.poc_checker:
            result = self.poc_checker(subnet, inclusive=True)
            if len(result):
                for poc in result: # dictionary of POC entries
                    # cover both potential status cases
                    if ('available' not in result[poc].status.lower()
                            or 'not available' in result[poc].status.lower()):
                        error.append("Used or reserved in POC database (" +
                                str(poc) + ")")
                        break

        # finally: check routers
        result = self.routefinder_checker(subnet)
        if ((isinstance(result, basestring) and '0.0.0.0' in result)
                or (result.get('route') and '0.0.0.0' in result['route'])):
            if len(error) == 0:
                return True
        else:
            error.append('routed subnet')

        if len(error) > 0:
            return ', '.join(error)

    def get_wlc_vlan_names(self):
        """
        Get available VLAN Names from the wireless node. This is really a
        wrapper for the Orion module VLAN grabber.

        Returns:
            list: Returns list of vlan names

        """
        # hardcoded node ID - may need to be changed in the future
        self.force_orion_poll(settings.R1_WIFI_NODEID) # update Orion first

        vlan_list = self.get_orion_vlan(settings.R1_WIFI_NODEID)
        name_list = []
        for vlan in vlan_list:
            name_list.append(vlan_list[vlan][0])

        return name_list

    def _build_wlc_config(self, vlan_id, vlan_name, subnet, hsrpgroup,
            infoblox_servers, packetfence_server, extra_helpers, vrf, bgpconfig,
            wism_trunks, wism_config):
        """
        Build the WLC VLAN config using a Jinja2 template.

        Args:
            vlan_id (int): Argument for jinja2 template
            vlan_name (str): Argument for jinja2 template
            subnet (IPNetwork): Argument for jinja2 template
            hsrpgroup (str): Argument for jinja2 template
            infoblox_servers (list): Argument for jinja2 template
            packetfence_server (str): Argument for jinja2 template
            extra_helpers (str): Argument for jinja2 template
            vrf (str): Argument for jinja2 template
            bgpconfig (str): Argument for jinja2 template
            wism_trunks (str): Argument for jinja2 template
            wism_config (str): Argument for jinja2 template

        Returns:
            str: Rendered template
        """
        jenv = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()),
                trim_blocks=True, lstrip_blocks=True)

        template = jenv.get_template(settings.WLC_TEMPLATE)

        config = template.render(
                vlanid = vlan_id,
                vlanname = vlan_name,
                gateway = str(subnet[1]),
                subnetmask = str(subnet.netmask),
                r1_ipaddress = str(subnet[2]),
                r2_ipaddress = str(subnet[3]),
                hsrpgroup = hsrpgroup,
                infoblox1 = infoblox_servers[0],
                infoblox2 = infoblox_servers[1],
                packetfence = packetfence_server,
                extrahelpers = (("ip helper-address " + extra_helpers + '\n')
                        if extra_helpers else ''),
                vrf = (vrf if vrf else ''),
                bgpconfig = (bgpconfig if bgpconfig else ''),
                wism_trunks = wism_trunks,
                wism_config = wism_config)
        logging.debug(vlan_name + " generated ok")
        return config

    def generate_wlc_vlan(self, vlanid, subnet, is_department=False,
            department_name=None, is_clinical=False, wlc_set=1, hsrp_group=254,
            is_uguest=False, extra_helpers=None):
        """
        Generate a VLAN config for the wifi routers and WLCs.

        Args:
            vlanid (int): VLAN ID.
            subnet (IPNetwork): Subnet IPNetwork object.
            is_department (bool): Optional - Defines whether subnet is
                departmental.
            department_name (str): Optional - Department name.
            is_clinical (bool): Optional - Defines whether subnet is clincal.
            wlc_set (int): Optional - WLC number.
            hsrp_group (int): Optional - hsrp Group.
            is_uguest (bool): Optional - Defines whether subnet is UGuest.
            extra_helpers (str): Optional - Extra helper addresses.

        Returns:
            str: Rendered jinja2 template.

        Raises:
            ValueError: Caused if argument values are incorrect.
        """
        # check parameters
        if not is_department and (wlc_set < 1 or wlc_set > 5):
            raise ValueError("WLC set number incorrect")
        elif not isinstance(vlanid, (int, int)) or vlanid < 1:
            raise ValueError("invalid VLAN ID")
        elif is_department and not department_name:
            raise ValueError("missing department name/description")
        elif is_department and is_uguest:
            raise ValueError("departmental UGuest subnet not supported")
        elif '/' not in subnet:
            raise ValueError("CIDR block information missing in subnet")
        elif not is_department and is_clinical:
            raise ValueError("Non-departmental subnets cannot be Clinical")
        elif hsrp_group > 255 or hsrp_group < 0:
            raise ValueError("HSRP Group must be between 0 and 255")
        try:
            subnet = IPNetwork(subnet)
            if is_department and len(subnet) <= 15:
                raise ValueError("given subnet is too small for departments")
            if extra_helpers:
                IPAddress(extra_helpers)
        except:
            raise ValueError("invalid subnet")

        # generate VLAN name
        if is_department:
            vlan_name = ("wifi-" + str(department_name) +
                    ("-UGuest" if is_uguest else "-UConnect"))
        else:
            vlan_list = self.get_wlc_vlan_names()
            net_numbers = []
            for vlan in vlan_list:
                if ((not is_uguest and 'UConnect' in vlan) or
                        (is_uguest and 'UGuest' in vlan)):
                    try:
                        net_numbers.append(int(re.findall(r'^\d+',
                                vlan.split('net')[1])[0]))
                    except IndexError:
                        continue # no problem, just don't add the name
                    except:
                        traceback.print_exc()
                        continue

            try:
                next_net = max(net_numbers) + 1
            except ValueError:
                traceback.print_exc()
                raise self.VLANConfigError('net VLAN ID sequence not found')

            vlan_name = ("wifi-set" + str(wlc_set) + "net" + str(next_net) +
                    ("-UGuest" if is_uguest else "-UConnect"))

        # get DHCP helper addresses
        infoblox_servers = self.get_infoblox_servers(is_clinical)

        # generate WISM IPs
        if is_department:
            # departmental UConnect: span across all controllers
            wlc_ips = subnet[5:15]
        else:
            # non-departmental subnet: span across the WLC set
            wlc_ips = subnet[5:7]

        # generate trunk and interface configs for each WISM
        wism_template1 = ("config interface create " + vlan_name + " " +
                str(vlanid) + "\n" +
                "config interface vlan " + vlan_name + " " + str(vlanid) +"\n")
        wism_template2 = ("config interface dhcp dynamic-interface " +
                vlan_name + " primary " + infoblox_servers[0] + " secondary " +
                infoblox_servers[1] + "\n" +
                "save config\n" + "y\n" + "exit\n")

        vrf = None
        bgp_config = None
        # departmental UConnect WISM trunk and interface configs
        if is_department:
            if is_clinical:
                vrf = "ip vrf forwarding CLINICAL\n"
                bgp_config = ("###Step 2a: Add the subnet to the Clinical VRF" +
                "\n\nconf t\n" +
                "router bgp 17055\n" +
                "address-family ipv4 vrf CLINICAL\n" +
                "network " + str(subnet[0]) + " mask " + str(subnet.netmask) +
                "\n" + "end")

            wism_trunks = 'conf t\n'
            for wlc in range(1,6):
                wism_trunks += ("wism module " + str(wlc) +
                        " controller 1 allowed-vlan " + str(vlanid) + "\n")
            wism_trunks += ("end\n" + "write mem\n")

            wism_config = ''
            for router in [1,2]:
                for wlc in range(1,6):
                    wism_config += ("r" + str(router) + "-wlc" + str(wlc) +
                            "\n\n" + wism_template1 +
                            "config interface address dynamic-interface " +
                            vlan_name + " " + str(next(wlc_ips)) + " " +
                            str(subnet.netmask) + " " + str(subnet[1]) + "\n" +
                            wism_template2 + "\n")
        # General VLAN trunk and interface configs
        else:
            wism_trunks = ("conf t\n" +
                    "wism module " + str(wlc_set) +
                    " controller 1 allowed-vlan " + str(vlanid) + "\n" +
                    "end\n" + "write mem\n")

            wism_config = ("r1-wlc" + str(wlc_set) + "\n\n" + wism_template1 +
                    "config interface address dynamic-interface " + vlan_name+
                    " " + str(next(wlc_ips)) + " " + str(subnet.netmask) + " "+
                    str(subnet[1]) + "\n" + wism_template2 + "\n" +

                    "r2-wlc" + str(wlc_set) + "\n\n" + wism_template1 +
                    "config interface address dynamic-interface " + vlan_name+
                    " " + str(next(wlc_ips)) + " " + str(subnet.netmask) + " "+
                    str(subnet[1]) + "\n" + wism_template2 + "\n" )

        config_text = self._build_wlc_config(vlanid, vlan_name, subnet,
                hsrp_group, infoblox_servers, settings.PACKETFENCE_SERVER,
                extra_helpers, vrf, bgp_config, wism_trunks, wism_config)
        return config_text

    def _build_vlan_config(self, vlanid, vlan_name, subnet, vrf,
            infoblox_servers, bldg_number, is_nexus=False):
        """
        Generate an r1 and r2 VLAN config using a Jinja2 template.

        Args:
            vlanid (int): VLAN ID.
            vlan_name (str): VLAN name.
            subnet (IPNetwork): IPNetwork Object that defines subnet.
            vrf (str): VRF for vlan.
            infoblox_servers (list): List of Infoblox servers.
            bldg_number (int): Building number.
            is_nexus (bool): Optional - Indicates whether switch is a nexus.

        Return:
            str: Rendered jinja2 template.
        """
        jenv = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()),
                trim_blocks=True, lstrip_blocks=True)

        if is_nexus:
            template = jenv.get_template(settings.NEXUS_TEMPLATE)
            config = template.render(
                    vlanid = vlanid,
                    vlanname = vlan_name,
                    vrf = (("vrf member " + vrf + "\n") if vrf else ''),
                    gateway = str(subnet[1]),
                    r1_ipcidr = str(subnet[2]) + '/' + str(subnet.prefixlen),
                    r2_ipcidr = str(subnet[3]) + '/' + str(subnet.prefixlen),
                    infoblox1 = infoblox_servers[0],
                    infoblox2 = infoblox_servers[1],
                    bldgnum = bldg_number)
            logging.debug(vlan_name + " generated ok")
            return config
        else:
            standby_id = vlanid % 100
            template = jenv.get_template(settings.VLAN_TEMPLATE)
            config = template.render(
                    vlanid = vlanid,
                    vlanname = vlan_name,
                    vrf = (("ip vrf forwarding " + vrf + "\n") if vrf else ''),
                    gateway = str(subnet[1]),
                    r1_ipcidr = str(subnet[2]) + ' ' + str(subnet.netmask),
                    r2_ipcidr = str(subnet[3]) + ' ' + str(subnet.netmask),
                    infoblox1 = infoblox_servers[0],
                    infoblox2 = infoblox_servers[1],
                    standbyid = standby_id,
                    bldgnum = bldg_number)
            logging.debug(vlan_name + " generated ok")
            return config

    def get_vrfs(self):
        """
        Get the list of VRF names.

        Returns:
            list: VRF names.
        """
        return settings.VRFS

    def generate_vlan(self, vlanid, name, bldg_number, subnet, vrf=None,
            is_nexus=False):
        """
        Generate a regular VLAN for use on the distribution nodes.
        Note that the is_nexus parameter is only used if bldg_number is not
        defined.

        Args:
            vlanid (int): VLAN ID.
            name (str): VLAN name.
            bldg_number (int): Building number.
            subnet (IPNetwork): IPNetwork Object that defines subnet.
            vrf (str): Optional - VRF for VLAN.
            is_nexus (bool): Optional - Indicates whether switch is a nexus.

        Returns:
            str: Rendered jinja2 template.

        Raises:
            ValueError: Caused by invalid vlan, vrf, or name.
        """
        try:
            # error checking
            if vlanid < 2 or vlanid > 4095:
                raise ValueError("Invalid value for VLAN ID")

            if vrf and vrf not in settings.VRFS:
                raise ValueError("Invalid VRF")

            if not name:
                raise ValueError("VLAN Name/description is missing")

            subnet = IPNetwork(subnet)

            # generate data
            infoblox_servers = self.get_infoblox_servers("CLINICAL" in vrf)
            if bldg_number and bldg_number > 0:
                bldg = self.get_building(bldg_number)
                if not bldg or not bldg.number:
                    raise ValueError("Invalid building number")

                node = ((bldg.node.lower() + '-') if bldg.node else '')
                vlan_name = (node + bldg.abbrev + '-' + name)
                is_nexus = ((bldg.node.lower() in settings.NEXUS_NODES)
                        if bldg.node else False)
            else:
                vlan_name = name

            return self._build_vlan_config(vlanid, vlan_name, subnet.cidr, vrf,
                    infoblox_servers, bldg_number, is_nexus)
        except:
            traceback.print_exc()
            raise

class VLANLookup(object):
    """
    This object is designed to enable the search for a vlan on a router.
    It has a list of all the routers registered with the Network tool
    and uses the Network object to log into the switches.

    Args:
        switchaccess (SwitchAccess): Object that lets you to login to switches.
    """

    def __init__(self, switchaccess):
        self.switchaccess = switchaccess
        self.router_list = self.switchaccess.get_routerlist()['ios']
        self.router_list.extend(self.switchaccess.get_routerlist()['nexus'])
        # get all routers not in a data center
        self.router_list = [r for r in self.router_list
                if r.startswith('r1-') or r.startswith('r2-')]

    def search_router(self, vlan_num, router):
        """
        This method logs into a router, checks to see if the layer two for
        a vlan is built out, and if it is, checks for the layer three config.
        It returns none if there is no layer two for that vlan id, and a
        dictionary with the router, layer two, and layer three information
        if it does exist.

        args:
            vlan_num (int): Vlan ID number
            router (str): Router IP address or hostname.

        returns:
            None or dict: None if no VLAN is found; Otherwise a dict if a vlan
            is found with keys 'router', 'name', and 'config'
        """
        result = None
        try:
            connection = self.switchaccess.login(router)
            vlan_list = connection.send_command("show vlan brief")
            vlan_list = vlan_list.split("\r\n")

            # this is the pattern for a vlan id
            vlan_pattern = re.compile("\\b\\d+\\b(?=\\s)")
            for entry in vlan_list:
                vlan = vlan_pattern.search(entry)
                if vlan is not None and int(vlan_num) == int(vlan.group(0)):
                    result = {'router': router}

                    # Add only the name to the 'name' entry
                    entry = entry.split(" ")
                    entry = [_f for _f in entry if _f]
                    result['name'] = entry[1]

                    # search for the layer 3
                    config = connection.send_command("show run int vlan "
                            + vlan.group(0))
                    if "Invalid" not in config:
                        result['config'] = config

            return result
        finally:
            self.switchaccess.logout(connection)

class VLANChanger():
    """
    Object that handles changing VLAN configurations on edge ports.

    Args:
        switchaccess (SwitchAccess): SwitchAccess instance
        mactracker (MacFinder): a MacFinder object
    """

    def __init__(self, switchaccess, mactracker):
        self.switchaccess = switchaccess
        self.mactracker = mactracker

    def get_vlan_list(self, switch=None, connection=None):
        """
        Get the list of VLAN IDs and descriptions through a particular
        switch or connection. Note that this will exclude the default VLAN 1.

        Args:
            switch (str): Optional - Switch DNS name or IP address as a string.
                    Either this or connection must be supplied.
            connection (Connection): Optional - Open SwitchAccess Connection.

        Returns:
            list: A list of 2-tuples with IDs and descriptions

        Raises:
            ValueError: If none or both of the parameters are specified
        """
        if not switch and not connection:
            raise ValueError("switch or connection must be specified")
        elif switch and connection:
            raise ValueError("Both switch or connection cannot be given")
        opened_conn = False
        try:
            if not connection:
                opened_conn = True
                connection, result = self.switchaccess.login_and_run(switch,
                                                                     "show vlan brief | begin 1")
            else:
                result = connection.send_command(
                    "show vlan brief | begin 1")

            list_of_vlans = result.splitlines()
            result = []
            for index, line in enumerate(list_of_vlans):
                if 'active' in line:
                    # name is too long, so it is on the previous line
                    if line.split()[0] == 'active':
                        temp = list_of_vlans[index - 1] + line
                        logging.info(temp)
                        result.append(temp.split(' active ')[0])
                    else:
                        result.append(line.split(' active ')[0])

            result = [(int(line.split()[0]), ' '.join(line.split()[1:]))
                      for line in result if 'more' not in line.split()[0].lower()
                      and int(line.split()[0]) != 1]

            return sorted(result, key=lambda k: k[0])
        finally:
            if opened_conn:
                self.switchaccess.logout(connection)

    def search_and_verify_mac(self, mac, vlanid):
        """
        Search for a MAC address using MACTracker and verify configuration.
        Note that this is a blocking function for MAC address lookups.

        Args:
            mac (str): MAC Address for the device
            vlanid (int): VLAN ID

        Returns:
            tuple: A 2-tuple of a MacLocation object, and an existing Connection
            object to the discovered switch.

        Raises:
            ValueError: When the connection to the switch is interrupted
        """
        mac = self.mactracker.parse_mac(mac)

        # search for MAC address location using MACTracker's threads
        mt_thread = self.mactracker.start_mactrack_thread(mac,
                                                          keep_connection=True)
        while True:
            time.sleep(2)  # check every 2 seconds
            mt_result = self.mactracker.get_thread(mt_thread)
            if not mt_result:  # shouldn't happen
                raise ValueError("MACTracker thread disappeared")
            if mt_result['message'] is None:
                mt_result = mt_result['maclocation']  # get the found MacLocation
                break
        # clean up MACTracker objects and retrieve the connection
        mt_result, connection = self.mactracker.get_thread_and_connection(
            mt_thread, autodelete=True)
        mt_result = mt_result['maclocation']
        if connection is None:
            raise ValueError(
                "Unable to keep a connection to the destination switch " +
                mt_result.switchname)

        try:
            # verify with MACTracker results
            self.verify_switchport(mt_result, connection=connection,
                                   verify_vlan=vlanid)  # defined in portconfig_common
            return mt_result, connection
        except:
            if connection is not None:
                self.switchaccess.logout(connection)
            raise

    def configure_port_vlan(self, switch, port, vlanid, connection):
        """
        Configure an edge port on a particular switch to access a given VLAN
        ID. Note that this will only work on access ports, and only on ports
        where the searched MAC address is connected.

        Args:
            switch (str): Switch DNS name or IP address.
            port (str): Switch Interface as a string. Note that this must be the
                    full name, e.g. "GigabitEthernet1/0/1"
            vlanid (int): VLAN ID as a positive integer. This must exist on the
                    switch.
            connection (Connection): Existing Connection object to send commands
                    over.

        Raises:
            ValueError: When there is an issue interacting with the switch
        """
        try:
            logging.info("Changing VLAN on " + switch + " " + port +
                         " to VLAN " + str(vlanid))

            output = connection.send_command("configure terminal")
            if "nter configuration commands" not in output:
                raise ValueError("Unable to enter configure mode on switch " +
                                 switch + ": " + output)
            output = connection.send_command("interface " + port)
            if output:  # shouldn't have been any error message
                raise ValueError("Could not select port " + port +
                                 " on switch " + switch + ": " + output)
            output = connection.send_command("switchport access vlan " +
                                             str(vlanid))
            if output:
                raise ValueError("Could not set access VLAN on port " + port +
                                 ", " + switch + ": " + output)
            connection.send_command("end")
            # don't forget to save changes
            connection.send_command("write memory")
        finally:
            if connection is not None:
                self.switchaccess.logout(connection)

    def change_vlan(self, mac, vlanid):
        """
        Change the port a given MAC address is on to access the given VLAN
        ID. This also runs multiple checks and verifications before configuring
        the edge device, and minimizes the number of SSH sessions needed.

        Args:
            mac (str): MAC address
            vlanid (int): VLAN ID

        Returns:
            Maclocation: A MacLocation namedtuple of the discovered switch/port.

        Raises:
            ValueError: When the VLAN ID is outside of the usable range
        """
        vlanid = int(vlanid)
        if vlanid == 1 or vlanid > 4093:
            raise ValueError("Invalid VLAN ID")

        # look up switch and port information for the given MAC address
        mt_result, connection = self.search_and_verify_mac(mac, vlanid)

        # TODO save old config in a database somewhere
        logging.info("Old config: " + mt_result.simple_config)

        # all our Tests checked out, it's okay to swap to configure mode and
        # change the port VLAN
        self.configure_port_vlan(mt_result.switchip, mt_result.port, vlanid,
                                 connection)

        # return discovered MACLocation
        return mt_result
