from __future__ import absolute_import
import logging
import re
import time
from builtins import object
from builtins import str
from past.builtins import basestring


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
        self.arp = []

    def __eq__(self, other):
        if not isinstance(other, vlan):
            return NotImplemented
        return self.number == other.number
    def __hash__(self):
        return hash(self._number)
    def assing_confg_attributes(self):
        pass

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
