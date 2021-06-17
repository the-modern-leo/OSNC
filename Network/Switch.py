
class Neighbor():
    def __int__(self,deviceid):
        self.deviceid = deviceid
        self.ip = None
        self.platform = None
        self.interface = None
        self.remote_interface = None
        self.VTPDomain = None
        self.duplex = None

    def __eq__(self, other):
        if not isinstance(other, Neighbor):
            return NotImplemented
        return self.deviceid == other.deviceid and self.ip == other.ip

    def __hash__(self):
        return hash(self.deviceid)

class Checker():
    """
    A module that checks current, deployed switches against generated data
    to determine if their config, Infoblox naming, and Orion entries follow
    standards and best practices.

    Naming Policy for Access Layer:
    <function descriptor><number>-<building number><building code>-<room number>-<node>.net.utah.edu

    For those that have an address for the building code:
    <function descriptor><number>-<building number><building code>-<room number>-<node>.net.utah.edu


    Args:
        building_getter (function): Retrieves building information.
        host_getter (function): Retrieves host information.
        dns_getter (function): Retrieves dns record information.
        host_generator (function): Generates host name.
        orion_getter (function): Retrieves switch information.
    """
    def __init__(self, building_getter, host_getter, dns_getter, host_generator,
            orion_getter):
        self.building_getter = building_getter
        self.host_getter = host_getter
        self.dns_getter = dns_getter
        self.host_generator = host_generator
        self.orion_getter = orion_getter

    class HostnameFormatError(Exception):
        """
        This is when the hostname format for the switch is incorrect.
        """
        pass

    class OrionEntryError(Exception):
        """
        This is when the switch entry in Orion is incorrect
        (missing data, etc.).
        """
        pass

    CheckStatus = namedtuple('CheckStatus', ['error', 'actual', 'expected',
        'data'])

    dist_nodes = ['ebc', 'park', 'lib', 'remote', 'fort', 'ddc', 'som',
            'clinical']

    def get_dev_info(self):
        """
        Retrieves development information.

        Returns:
            str: Returns "Production" if all getters are set, otherwise returns
            "Development".
        """
        if (self.building_getter and self.host_getter and self.dns_getter and
                self.host_generator and self.orion_getter):
            return "Production"
        else:
            return "Development"

    def check_hostname(self, ip):
        """
        Checks a switch hostname from Infoblox. This searches for a host record
        or A record by IP, and checks against the building list and hostname
        format standard (outlined in hostname-format.md) for compatibility.

        Args:
            ip (str): IP address of the switch.

        Returns:
            CheckStatus: Named tuple describing the validity of the hostname. If
            CheckStatus.error is blank or None, the hostname is correct.

        Example:
        dx1-892_585komas-101-ebc.net.utah.edu
            """
        # get host data from Infoblox
        host_data = self.host_getter(ip)
        if "UNUSED" in host_data['status']:
            return self.CheckStatus("switch IP not found", None, None, None)
        host_data = host_data['names'][0]
        error = None
        switch_prefix = ""
        bldg_number = 0
        room_number = ""
        expected_host = None
        extra_data = None
        try:
            # split the hostname data up
            host_split = host_data.partition('.')[0].split('-')
            switch_prefix = host_split[0]
            bldg_short = host_split[1]
            if bldg_short.isdigit(): # research park building
                offset = 1
                bldg_number = bldg_short
            else:
                offset = 0
                bldg_number = re.findall(r'\d+', bldg_short)[0]
            room_number = '-'.join(host_split[2 + offset:-1])

            # check prefix (sx, dx etc)
            if not any(s in switch_prefix for s in ['sx', 'dx']):
                raise self.HostnameFormatError('wrong prefix')

            # check building number (and short name, if not research park)
            if bldg_number == 0:
                raise self.HostnameFormatError("building number is incorrect")
            shortname = (self.building_getter(bldg_number).shortname.
                    replace(' ', '').lower())
            if offset == 1:
                if shortname != host_split[2]:
                    raise self.HostnameFormatError("short name is incorrect")
            else:
                # split building number from short name and check
                if (shortname != re.sub(bldg_number, '', bldg_short)):
                    raise self.HostnameFormatError("short name is incorrect")

            # check room number and make sure it's not a distribution node
            if room_number in self.dist_nodes:
                raise self.HostnameFormatError("room number is missing")

            # check distribution node
            dist = host_split[-1]
            if "poe" in dist: # PoE is not part of the naming standard
                raise self.HostnameFormatError("POE suffix in hostname")
            elif dist not in self.dist_nodes:
                # last split is probably part of the room number
                room_number = '-'.join(host_split[2 + offset:])
                # ignore buildings that have their own routers (no dist. node)
                if self.building_getter(bldg_number).node.lower() != "self":
                    raise self.HostnameFormatError("invalid distribution node")

            # check DNS zone and make sure it isn't med.utah.edu
            if "med.utah.edu" in host_data.partition('.')[2]:
                raise self.HostnameFormatError("DNS zone is incorrect")

            # check demarc alias
            if 'dx1' in switch_prefix:
                demarc_alias = 'dx1-'+str(bldg_number).zfill(3)+'.net.utah.edu'
                recd = self.dns_getter(demarc_alias)
                if not recd:
                    expected_host = demarc_alias
                    raise self.HostnameFormatError("demarc alias is missing")
                elif 'canonical' in recd and recd['canonical'] != host_data:
                    extra_data = demarc_alias
                    host_data = recd['canonical']
                    raise self.HostnameFormatError("demarc CNAME does not " +
                            "point to full hostname correctly")
                elif 'ipv4addr' in recd and recd['ipv4addr'] != ip:
                    extra_data = demarc_alias
                    raise self.HostnameFormatError("demarc alias does not " +
                            "point to full hostname/IP")

        except IndexError as e:
            if len(host_split) + offset == 5: # everything except last element
                error = "missing distribution node"
            else:
                error = ("missing information in hostname (requires switch " +
                        "prefix, building number, short name, room number, " +
                        "and distribution node)")
        except self.HostnameFormatError as e:
            error = str(e)
        finally:
            if bldg_number != 0 and room_number and not expected_host:
                expected_host = self.host_generator(switch_prefix,
                        bldg_number, room_number) + ".net.utah.edu"
            elif not expected_host:
                expected_host = "insufficient_data"
            return self.CheckStatus(error, host_data, expected_host, extra_data)

    def check_orion(self, ip):
        """
        Checks a switch's entry in Orion. This checks for the correct switch
        name format, custom properties, and notification tier.

        Args:
            ip (str): IP address of the switch.

        Returns:
            CheckStatus: Named tuple describing the validity of the Orion Node.
            If CheckStatus.error is blank or None, the switch entry is correct.
        """
        error = None
        actual_entry = None
        expected_entry = None
        try:
            orion_info = self.orion_getter(ip=ip)

            expected_entry = orion_info.dns_name
            if orion_info.name != orion_info.dns_name:
                actual_entry = orion_info.name
                raise self.OrionEntryError("Orion name and DNS name differ")

            if not orion_info.dns_name:
                raise self.OrionEntryError("DNS name is missing")
            if not orion_info.barcode:
                raise self.OrionEntryError("barcode is missing")
            if not orion_info.proptag:
                raise self.OrionEntryError("property tag is missing")
            if not orion_info.location:
                raise self.OrionEntryError("location information is missing")
            if orion_info.snmp_version == 2:
                raise self.OrionEntryError("SNMP version is v2")

        except self.OrionEntryError as e:
            error = str(e)
        except Exception as e:
            # because OrionObjectException not available
            if "Node does not exist" in str(e):
                error = "does not exist"
            else:
                traceback.print_exc()
        finally:
            return self.CheckStatus(error, actual_entry, expected_entry, None)

    def check_switch(self, ip):
        """
        Check a switch by logging in and grabbing the hostname, domain name,
        and other config items. Not implemented

        Args:
            ip (str): IP address of the switch.

        Returns:
            CheckStatus: Named tuple describing the validity of the switch
            config. If CheckStatus.error is blank or None, the switch config is
            valid and correct.
        """
        pass
        #TODO Create this function

class Stack():

    def __init__(self,ip):
        # query result variables
        super().__init__(ip)
        self.version_result = None
        self.run_result = None
        self.portdowntime_result = None
        self.portcount_result = None
        self.inv_result = None
        self.cdpnei_result = None
        self.module_result = None
        self.mac_address_result = None
        self.interface_result = None
        self.logging_data_result = None
        self.status_result = None
        self.acl_result = None

        self.device = None
        self.modelnumber = None
        self.IPAddress = None
        self.uplink = None
        self.version = None
        self.serial = None
        self.stack = None
        self.uptime = None
        self.lastrestart = None
        self.subnetmask = None
        self.defaultgateway = None
        self.bannername = None
        self.portcount = 0
        self.blades = set()
        self.groupedvlans = None
        self.chassis = None
        self.hostname = None
        self.cdpneighbors = None
        self.SNMP = None
        self.access_lists = []
        self.nexus = None
        self.SFPs = None
        self.vlansints = None
        self.conn = None
        self.node = None
        self.tacacs = []
        self.port_channels = []

        # Location variables
        self.roomnumber = None
        self.buildingname = None
        self.buildnumber = None
        self.racknumber = None
        self.description = None
        self.address = None
        self.function_descriptor = None
        self.function_descriptor_number = None
        self.node = None

        # Logging variables
        self.logging_data = None
        self.should_overwrite_logging = None

        self.mgmt_vlan = None

        #policy checkes
            #SNMP
                #groups
        self.snmp_group_RW_wrong = False
        self.snmp_group_RW_missing = False
        self.snmp_group_remove = []
        self.SNMP_context_wrong = False
        self.SNMP_context_missing = False
                #views
        self.snmp_view_rw_wrong = False
        self.snmp_view_rw_missing = False
        self.snmp_view_remove = []
                #users
        self.snmp_user_RW_wrong = False
        self.snmp_user_RW_missing = False
        self.snmp_user_remove = []

        self.snmp_version_mismatch = False
        self.remove_SNMP_version_2 = False

            #Monitoring
        self.orion_encript_meth_wrong = False
        self.orion_auth_meth_wrong = False
        self.orion_version_wrong = False
        self.orion_username_wrong = False
            #access Lists
        self.acl_71_missing = False
        self.acl_199_missing = False
        self.old_orion_ips_71 = False
        self.new_orion_ips_71 = False
        self.remove_acl = []

    def __repr__(self):
        return str(self.ip)

    def __hash__(self):
        return hash((self.version_result,
        self.run_result,
        self.portdowntime_result,
        self.portcount_result,
        self.inv_result,
        self.cdpnei_result,
        self.module_result,
        self.mac_address_result,
        self.interface_result,
        self.logging_data_result,
        self.status_result,
        self.acl_result))

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.ip == other.ip

    def login_and_run_logout(self, command):
        """Log in to a device and immediately run a command.

        Args:
            router: Device IP address or DNS host name as a string.
            command: Command to run on the device if login is successful.
            quick: Optional boolean - if True, shorten timeouts for logging in.

        Returns:
            A tuple containing the Connection object as well as a multiline
            output string.
        """
        with Connection_manager(self.ip) as conn:
            output = conn.send_command(command)
        return command, output
    def check_for_errors_in_send_command(self,results):
        """
        This functions checks for all the common issues in responses on switches
        Args:
            results(str): the results of running 'send_command'

        Returns:
            (tuple): (bool,results)

        """
        pass
    def getSwitchInfo_vlan(self):
        """
        Gathers all the essential information from the switch, and creates a switch object based off the
        results for better use in python coding projects
        Args:
            con (Connection): an active Parimko Connection to a switch

        Returns (Switch, Connection):
        """
        logger.info(f"Gathering Switch data - Starting")
        try:
            self.version_result = self.conn.send_command('show version', manypages=True)
            self.run_result = self.conn.send_command('show run', manypages=True)
            self.status_result = self.conn.send_command('show int status', manypages=True)
            self.interface_result = self.conn.send_command('show run | section interface', manypages=True)
            if 'Invalid input detected at' in self.interface_result:
                self.interface_name_r = self.conn.send_command('show run | in interface', manypages=True)
            self.cdpnei_result = self.conn.send_command('show cdp nei detail', manypages=True)
            self.inv_result = self.conn.send_command('show inventory', manypages=True)
            self.module_result = self.conn.send_command('show module all', manypages=True)
            if 'Invalid input detected at' in self.module_result:
                self.module_result = self.conn.send_command('show module', manypages=True)
        except Exception as e:
            logger.info(f"Gathering Switch data - Failed")
            logger.error(e, exc_info=True)
            self.logout(self.conn)
        else:
            logger.info(f"Gathering Switch data - Success")
            self.logout(self.conn)

    def getSwitchInfo(self):
        """
        Gathers all the essential information from the switch, and creates a switch object based off the
        results for better use in python coding projects
        Args:
            con (Connection): an active Parimko Connection to a switch

        Returns (Switch, Connection):
        """
        logger.info(f"Gathering Switch data - Starting")
        try:
            self.login()
            teststring = self.conn.send_command('enable', manypages=True)
            if not teststring:
                pass
            elif '% Invalid command at' in teststring:
                pass
            else:
                self.conn.enable_cisco(password=Switch_access.password)
            self.version_result = self.conn.send_command('show version', manypages=True)
            self.run_result = self.conn.send_command('show run', manypages=True)
            self.status_result = self.conn.send_command('show int status', manypages=True)
            self.interface_result = self.conn.send_command('show run | section interface', manypages=True)
            if 'Invalid input detected at' in self.interface_result:
                self.interface_name_r = self.conn.send_command('show run | in interface', manypages=True)
            self.portdowntime_result = self.conn.send_command('show interface link', manypages=True)
            if 'Invalid input detected at' in self.portdowntime_result:
                self.portdowntime_result_in = self.conn.send_command('show interface', manypages=True)
            self.inv_result = self.conn.send_command('show inventory', manypages=True)
            self.portcount_result = self.conn.send_command('show interface counters', manypages=True)
            self.cdpnei_result = self.conn.send_command('show cdp nei detail', manypages=True)
            self.module_result = self.conn.send_command('show module all', manypages=True)
            if 'Invalid input detected at' in self.module_result:
                self.module_result = self.conn.send_command('show module', manypages=True)
            self.snmp_result = self.conn.send_command('show run | section snmp', manypages=True)
            if 'Invalid input detected at' in self.snmp_result:
                self.snmp_result_in = self.conn.send_command('show run | in snmp', manypages=True)
            self.snmp_user_result = self.conn.send_command('show snmp user', manypages=True)
            self.acl_result = self.conn.send_command('show access-list', manypages=True)
            self.logging_data_result = self.conn.send_command('show run | section logging', manypages=True)
            if 'Invalid input detected at' in self.logging_data_result:
                self.logging_data_result = self.conn.send_command('show run | in logging', manypages=True)
            self.mac_address_result = self.conn.send_command('show mac address-table', manypages=True)
            self.tacacs_result = self.conn.send_command('show run | section tacacs', manypages=True)
            if 'Invalid input detected at' in self.tacacs_result:
                self.tacacs_result_in = self.conn.send_command('show run | in tacacs', manypages=True)
            self.inline_power_result = self.conn.send_command('show power inline', manypages=True)
            self.environment_result = self.conn.send_command('show environment all', manypages=True)
        except Exception as e:
            logger.info(f"Gathering Switch data - Failed")
            logger.error(e, exc_info=True)
            self.logout(self.conn)
        else:
            logger.info(f"Gathering Switch data - Success")
            self.logout(self.conn)

    def getSwitchInfo_thread(self):
        """
        Gathers all the essential information from the switch, and creates a switch object based off the
        results for better use in python coding projects
        Args:
            con (Connection): an active Parimko Connection to a switch

        Returns (Switch, Connection):
        """
        logger.info(f"Gathering Switch data - Starting")
        try:
            command_list = ['show version','show run','show int status','show run | section interface',
                              'show run | in interface','show interface link','show interface','show inventory',
                              'show interface counters','show cdp nei detail','show module all', 'show module',
                              'show run | section snmp','show run | in snmp','show snmp user','show access-list',
                              'show run | section logging','show run | in logging','show mac address-table',
                                'show run | section tacacs',
                              'show run | in tacacs','show power inline','show environment all']
            # log into devices attached to the dx devices, and gather their attached devices
            with ThreadPoolExecutor(max_workers=9) as executor:
                results = executor.map(self.login_and_run_logout,command_list)

            results = list(results)
            self.version_result = results[0][1]
            self.run_result = results[1][1]
            self.status_result = results[2][1]
            self.interface_result = results[3][1]
            if 'Invalid input detected at' in self.interface_result:
                self.interface_name_r = results[4][1]
            self.portdowntime_result = results[5][1]
            if 'Invalid input detected at' in self.portdowntime_result:
                self.portdowntime_result_in = results[6][1]
            self.inv_result = results[7][1]
            self.portcount_result = results[8][1]
            self.cdpnei_result = results[9][1]
            self.module_result = results[10][1]
            if 'Invalid input detected at' in self.module_result:
                self.module_result = results[11][1]
            self.snmp_result = results[12][1]
            if 'Invalid input detected at' in self.snmp_result:
                self.snmp_result_in = results[13][1]
            self.snmp_user_result = results[14][1]
            self.acl_result = results[15][1]
            self.logging_data_result = results[16][1]
            if 'Invalid input detected at' in self.logging_data_result:
                self.logging_data_result = results[17][1]
            self.mac_address_result = results[18][1]
            self.tacacs_result = results[19][1]
            if 'Invalid input detected at' in self.tacacs_result:
                self.tacacs_result_in = results[20][1]
            self.inline_power_result = results[21][1]
            self.environment_result = results[22][1]
        except Exception as e:
            logger.info(f"Gathering Switch data - Failed")
            logger.error(e, exc_info=True)
            _exception(e)
        else:
            logger.info(f"Gathering Switch data - Success")

    def get_run_data(self):
        """
        gets the fun information for this device and assignes it to the self.run_results
        :return:
        """
        logger.info(f"Gathering Switch Run data - Started")
        try:
            self.run_result = self.conn.send_command('show run', manypages=True)
            if '% Invalid command at' in self.run_result:
                raise ValueError
            if self.run_result is None:
                raise ValueError
        except Exception as e:
            logger.info(f"Gathering Switch Run data - Failed")
            logger.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            logger.info(f"Gathering Switch Run data - Success")

    ############################################## Sort Functions ###########################################
    def assignattributes_vlan(self):
        """
        takes the responses from get switch info, and applies those responses to the object attributes

        """
        try:
            # gatjers the model numbers for device
            self.sortVersion(versionresult=self.version_result)
            self.sortInventory(self.inv_result)
            if self.modelnumber in settings.modularaccess:
                # gathers blades for chassis
                self.sortmodule(self.module_result)
            # applies interfaces to blades, applies vlans
            self.sortRun(self.run_result)
            # sort through interface results
            self.sortinterfaces(self.interface_result)
            # applies the uplinks
            self.sortCdpNeiDetail(self.cdpnei_result)
            # runs extra commands to gather the need information for modularaccess switches.
            if self.modelnumber in settings.modularaccess:
                self.chassis = True
            self.sort_hostname()
            if not self.portcount:
                for blade in self.blades:
                    if blade.interfaces:
                        self.portcount += len(blade.interfaces)
                    if blade.moduleinterfaces:
                        self.portcount += len(blade.moduleinterfaces)
        except Exception as e:
            logger.error(e, exc_info=True)
            raise
    def assignattributes(self):
        """
        takes the responses from get switch info, and applies those responses to the object attributes

        """
        try:
            #TODO Add a function to sort the output of show 'hw-module all attribute'
            # gatjers the model numbers for device
            self.sortVersion(versionresult=self.version_result)
            self.sortInventory(self.inv_result)
            if self.modelnumber in settings.modularaccess:
                # gathers blades for chassis
                self.sortmodule(self.module_result)
            # applies interfaces to blades, applies vlans
            self.sortRun(self.run_result)
            # sort through interface results
            self.sortinterfaces(self.interface_result)
            # applies the uplinks
            self.sortCdpNeiDetail(self.cdpnei_result)
            # get, and apply the ACL information
            self.sort_acl()
            # sort through interface results
            self.sortlogging(self.logging_data_result)
            # sort through interface results
            self.sortsnmp()
            # sort through interface results
            self._sort_snmp_user()
            # applies the port counters to the interfaces
            self.sortportcounters(self.portcount_result)
            # runs extra commands to gather the need information for modularaccess switches.
            if self.modelnumber in settings.modularaccess:
                self.chassis = True
                # self.sortportdowntime(self.portdowntime_result)
            self.sort_hostname()
            self.sort_mac_address(self.mac_address_result)
            self.sort_tacacs()
            self.sort_status()
            self.sort_power_inline()
            self.sort_enviroment()
            if not self.portcount:
                for blade in self.blades:
                    if blade.interfaces:
                        self.portcount += len(blade.interfaces)
                    if blade.moduleinterfaces:
                        self.portcount += len(blade.moduleinterfaces)
        except Exception as e:
            logger.error(e, exc_info=True)
            _exception(e)
            raise

    def assignattributes_thread(self):
        """
        takes the responses from get switch info, and applies those responses to the object attributes

        """
        try:
            # gatjers the model numbers for device
            self.sortVersion(versionresult=self.version_result)
            self.sortInventory(self.inv_result)
            if self.modelnumber in settings.modularaccess:
                # gathers blades for chassis
                self.sortmodule(self.module_result)
            # applies interfaces to blades, applies vlans
            self.sortRun(self.run_result)

            future_results = {}
            # log into devices attached to the dx devices, and gather their attached devices
            with ThreadPoolExecutor(max_workers=20) as executor:
                future_results[executor.submit(self.sortinterfaces)] = self.interface_result
                future_results[executor.submit(self.sortCdpNeiDetail, self.cdpnei_result)] = self.cdpnei_result
                future_results[executor.submit(self.sort_acl, None)] = None
                future_results[executor.submit(self.sortlogging, self.logging_data_result)] = self.logging_data_result
                future_results[executor.submit(self.sortsnmp, None)] = None
                future_results[executor.submit(self._sort_snmp_user, None)] = None
                future_results[executor.submit(self.sortportcounters, self.portcount_result)] = self.portcount_result
                # runs extra commands to gather the need information for modularaccess switches.
                if self.modelnumber in settings.modularaccess:
                    future_results[executor.submit(self.sortportdowntime, self.portdowntime_result)] = self.portdowntime_result
                future_results[executor.submit(self.sort_hostname, None)] = None
                future_results[executor.submit(self.sort_mac_address, self.mac_address_result)] = self.mac_address_result
                future_results[
                    executor.submit(self.sort_tacacs, None)] = None
                future_results[
                    executor.submit(self.sort_status, None)] = None
                future_results[
                    executor.submit(self.sort_power_inline, None)] = None
                future_results[
                    executor.submit(self.sort_enviroment, None)] = None
                future_results[
                    executor.submit(self.sort_power_inline, None)] = None

                for future in concurrent.futures.as_completed(future_results):
                    ip = future_results[future]
                    try:
                        s = future.result()
                    except Exception as e:
                        logger.error(e, exc_info=True)
                        _exception(e)
                        raise
            if not self.portcount:
                for blade in self.blades:
                    if blade.interfaces:
                        self.portcount += len(blade.interfaces)
                    if blade.moduleinterfaces:
                        self.portcount += len(blade.moduleinterfaces)
        except Exception as e:
            logger.error(e, exc_info=True)
            _exception(e)
            _exception(e)
            raise

    def sort_status(self):
        """
        Returns:
        """
        # TODO Finish building this method to get Copper/fiber types per port
        status_response = self.status_result.split("\r\n")

    def sort_tacacs(self):
        """
        applies the tacas command to the tacas object, and than to the switch object.
        """
        logger.info("Sorting 'show run | section tacacs' - Starting")
        try:
            if 'Invalid input detected at' in self.tacacs_result:
                tacacslines = self.tacacs_result_in
                tacacslines = tacacslines.split("\r\n")
                tacacslines = [x for x in tacacslines if x]
                newtaclines = []
                for line in tacacslines:
                    if "aaa" in line:  # skip Accounting, Authorization, and Authentication entries
                        continue
                    else:
                        newtaclines.append(line)
                for line in newtaclines:
                    if "tacacs-server host" in line:
                        t = TACACS()
                        ip = re.sub("tacacs-server host ", "", line)
                        ip = re.sub("tacacs-server ", "", ip)
                        ip = re.sub("timeout 5", "", ip)
                        ip = [x for x in ip if x]
                        ip = ''.join([x for x in ip if x != ' '])
                        t.server = ipaddress.IPv4Address(ip)
                        self.tacacs.append(t)
            else:
                tacacslines = self.tacacs_result
                tacacslines = tacacslines.split("\r\n")
                tacacslines = [x for x in tacacslines if x]
                newtaclines = []
                v1tacacs = []
                for line in tacacslines:
                    if "aaa" in line:  # skip Accounting, Authorization, and Authentication entries
                        continue
                    if "feature tacacs+" in line:
                        continue
                    if "ip access-list copp-system-acl-tacacsradius" in line:
                        continue
                    if "permit tcp any" in line:
                        continue
                    if "source-interface" in line:
                        continue
                    if "match access-group name" in line:
                        continue
                    if "class copp-tacacsradius" in line:
                        continue
                    if "police pps 400" in line:
                        continue
                    if "tacacs-server" in line:  # Gather lines for v1 of tacacs
                        v1tacacs.append(line)
                    else:
                        newtaclines.append(line)
                newtaclines = "\r\n".join(newtaclines)
                tacacservers = newtaclines.split("tacacs server ")
                for line in v1tacacs:
                    if "server name " in line:
                        continue
                    if " server " in line:
                        continue
                    if line == '':
                        continue
                    if "tacacs-server host " in line:
                        t = TACACS()
                        ip = re.sub("tacacs-server host ", "", line)
                        ip = re.sub("timeout ", "", ip)
                        ip = ip.split(" ")
                        ip = [x for x in ip if x][0]
                        ip = ''.join([x for x in ip if x != ' '])
                        t.server = ipaddress.IPv4Address(ip)
                        self.tacacs.append(t)
                for tac in tacacservers:
                    if "server name " in tac:
                        continue
                    if " server " in tac:
                        continue
                    if tac == '':
                        continue
                    t = TACACS()
                    taclines = tac.split("\r\n")
                    t.name = taclines[0]
                    for line in tacacslines:
                        if line == '':
                            continue
                        elif "key 7 " in line:
                            t.key = re.sub("key 7 ", "", line)
                        elif "address ipv4 " in line:
                            ip = re.sub("address ipv4 ", "", line).rstrip()
                            ip = ''.join([x for x in ip if x != ' '])
                            t.server = ipaddress.IPv4Address(ip)
                        else:
                            pass
                    self.tacacs.append(t)

        except Exception as e:
            logger.info("Sorting 'show run | section tacacs' - failed")
            logger.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            pass

    def sortinterfaces(self, interface_result=None):
        """
        This function sorts through every single interface on the device, and applies those interfaces to the blade object
        :param interface_result (str) a response from the command "show run | section interface":
        """
        logger.info("Sorting 'show run | section interface' - Starting")
        assert hasattr(self, 'blades'), f'the blades have not been set on this object'
        assert self.blades is not None, f'the blades have not been set on this object'
        try:
            if not interface_result:
            #ssh into switch, and get information:
                self.login()
                self.interface_result = self.conn.send_command('show run | section interface', manypages=True)
                interface_result = self.interface_result
                if 'Invalid input detected at' in self.interface_result:
                    self.interface_name_r = self.conn.send_command('show run | in interface', manypages=True)
                    interface_result = self.interface_name_r
                self.logout(self.conn)
            # Checks if this command is not runnable on this machine
            if '% Invalid input detected at' in interface_result:
                if not '\r\n' in self.run_result:
                    interface_result = self.run_result.split('\n')
                else:
                    interface_result = self.run_result.split('\r\n')
                endupdate = True
            elif not interface_result:
                if not '\r\n' in self.run_result:
                    interface_result = self.run_result.split('\n')
                else:
                    interface_result = self.run_result.split('\r\n')
                endupdate = True
            else:
                if not '\r\n' in self.interface_result:
                    interface_result = self.interface_result.split('\n')
                else:
                    interface_result = self.interface_result.split('\r\n')
                endupdate = False
            # located the index values of the interfaces

            interfaceindex = []
            endofinterfaces = None

            # removes any --More-- that were randomly added.
            interface_result = [re.sub('--More--', '', x) for x in interface_result]
            # collect switch information
            for line in interface_result:
                if 'interface FastEthernet1' in line and "/" not in line:
                    pass
                elif 'interface FastEthernet0' in line and "/" not in line:
                    pass
                elif 'GigabitEthernet0/0' in line:
                    pass
                elif 'no passive-' in line and 'TenGigabitEthernet' in line:
                    pass
                elif 'interface HundredGigE' in line:
                    interfaceindex.append(interface_result.index(line))
                elif 'interface TwentyFiveGigE' in line:
                    interfaceindex.append(interface_result.index(line))
                elif 'interface TenGigabitEthernet' in line:
                    interfaceindex.append(interface_result.index(line))
                elif 'interface GigabitEthernet' in line:
                    interfaceindex.append(interface_result.index(line))
                elif 'interface TwoGigabitEthernet' in line:
                    interfaceindex.append(interface_result.index(line))
                elif 'interface FiveGigabitEthernet' in line:
                    interfaceindex.append(interface_result.index(line))
                elif 'interface FastEthernet' in line:
                    interfaceindex.append(interface_result.index(line))
                elif 'interface Ethernet' in line:
                    interfaceindex.append(interface_result.index(line))
                elif 'interface Ethernet100' in line:
                    interfaceindex.append(interface_result.index(line))
                elif 'interface Port-channel' in line:
                    interfaceindex.append(interface_result.index(line))
                elif 'interface Vlan1' in line or 'interface mgmt0' in line:
                    endofinterfaces = interface_result.index(line)

            if endupdate:
                end = endofinterfaces
            else:
                end = len(interface_result)
            # sepereate the interfaces
            sortedinterfaces = []
            for inter in sorted(interfaceindex):
                next_interface_index = interfaceindex.index(inter) + 1
                if next_interface_index < len(interfaceindex):
                    next_interface = interfaceindex[next_interface_index]
                    interfacedetails = interface_result[inter:next_interface]
                    sortedinterfaces.append(interfacedetails)
                else:
                    interfacedetails = interface_result[inter:end]
                    sortedinterfaces.append(interfacedetails)

            newsortedinterfaces = []
            for interf in sortedinterfaces:
                if "Port-channel" in interf[0]:
                    p = PortChannel()
                    p.fullname = interf[0]
                    p.ponumber = int(re.sub("interface Port-channel", "", p.fullname))
                    p.fullname = re.sub("interface", "", p.fullname)
                    # handle adding port channels
                    for line in interf:
                        if 'switchport mode trunk' in line:
                            p.trunk = True
                        elif 'switchport mode trunk allowed vlan' in line:
                            p.trunkvlan.append(re.sub('switchport mode trunk allowed vlan', '', line))
                        elif 'switchport mode trunk allowed vlan add' in line:
                            p.trunkvlan.append(re.sub('switchport mode trunk allowed vlan add', '', line))
                        elif 'description' in line:
                            p.description = re.sub('description', '', line)
                        elif 'switchport access vlan' in line:
                            line2 = re.sub('--More--', '', line)
                            line2 = re.sub('\\x1b\\r', '', line2)
                            p.vlan = int(re.sub('switchport access vlan', '', line2))
                        elif 'spanning-tree portfast' in line:
                            p.stpf = True
                        elif 'switchport voice vlan' in line:
                            p.voicevlan = re.sub('switchport voice vlan', '', line)
                    self.port_channels.append(p)
                else:
                    newsortedinterfaces.append(interf)

            interfaces = []
            # assign the interfaces attributes to the Interface object
            for interf in newsortedinterfaces:
                i = Interface()
                i.fullname = interf[0]
                i.fullname = re.sub("interface", "", i.fullname)
                namesplit = i.fullname.split(" ")
                namesplit = [x for x in namesplit if x]  # remove spaces
                i.fullname = " ".join(namesplit).rstrip()
                blandport = self._get_interface_numbers(i.fullname)
                blandport = blandport.split("/")
                if len(blandport) > 2:  # handle 3 long
                    i.blade = int(blandport[0])
                    i.module = int(blandport[1])
                    i.portnumber = int(blandport[2])
                else:
                    i.blade = int(blandport[0])
                    i.portnumber = int(blandport[1])
                for line in interf:
                    if 'switchport mode trunk' in line:
                        i.trunk = True
                    elif 'switchport mode trunk allowed vlan' in line:
                        i.trunkvlan.append(re.sub('switchport mode trunk allowed vlan', '', line))
                    elif 'switchport mode trunk allowed vlan add' in line:
                        i.trunkvlan.append(re.sub('switchport mode trunk allowed vlan add', '', line))
                    elif 'description' in line:
                        i.description = re.sub('description', '', line)
                    elif 'switchport access vlan' in line:
                        line2 = re.sub('--More--', '', line)
                        line2 = re.sub('\\x1b\\r', '', line2)
                        i.vlan = int(re.sub('switchport access vlan', '', line2))
                    elif 'spanning-tree portfast' in line:
                        i.stpf = True
                    elif 'switchport voice vlan' in line:
                        i.voicevlan = re.sub('switchport voice vlan', '', line)
                    elif 'TenGigabitEthernet' in line:
                        i.type = 'copper'
                    elif 'GigabitEthernet' in line and 'Ten' not in line:
                        i.type = 'copper'
                    elif 'GigabitEthernet' in line and 'Ten' not in line:
                        i.type = 'copper'
                    elif 'FastEthernet' in line and 'Ten' not in line:
                        i.type = 'copper'
                    elif 'channel-group' in line:  # handle adding port-channel info
                        port_split = line.split(" ")
                        port_split = [x for x in port_split if x]
                        portnumber = int(port_split[1])
                        for port_channel in self.port_channels:
                            if port_channel.ponumber == portnumber:
                                i.portchannel = port_channel
                interfaces.append(i)
            # assign module interfaces to Module

            # assign the interface to the blade it is on.
            blades = set()
            testblades = set()
            testblades.add(0)
            testblades.add(1)
            for interface in interfaces:
                blades.add(interface.blade)

            for i in interfaces:
                if i.blade == 5:
                    pass
                if i.portchannel:  # add interface to port channels
                    for port_channel in self.port_channels:
                        if port_channel.ponumber == i.portchannel.ponumber:
                            port_channel.interfaces.append(i)
                if blades == testblades:  # handle module information for single blade
                    for blade in self.blades:
                        if blade.stacknumber == 1:
                            if i.blade == 0:  # assign to blade 1
                                blade.interfaces[f"{i.portnumber}"] = i
                            if i.blade == 1:
                                blade.moduleinterfaces[f"{i.portnumber}"] = i
                else:  # handle standard formating of 0/1 and 1/0/1 formats
                    for blade in self.blades:
                        if i.blade == 0:
                            if blade.stacknumber == 1:
                                blade.interfaces[f"{i.portnumber}"] = i
                        elif hasattr(i, "module"):
                            if i.module != 0:
                                if i.blade == blade.stacknumber:
                                    blade.moduleinterfaces[f"{i.portnumber}"] = i
                            else:
                                if i.blade == blade.stacknumber:
                                    if i.portnumber == 49 or i.portnumber == 50 or i.portnumber == 51 or i.portnumber == 52:
                                        blade.moduleinterfaces[f"{i.portnumber}"] = i
                                    else:
                                        blade.interfaces[f"{i.portnumber}"] = i
                        elif i.blade == blade.stacknumber:
                            if i.portnumber == 49 or i.portnumber == 50 or i.portnumber == 51 or i.portnumber == 52:
                                blade.moduleinterfaces[f"{i.portnumber}"] = i
                            else:
                                blade.interfaces[f"{i.portnumber}"] = i

            for blade in self.blades:
                if blade.interfaces == {} and blade.moduleinterfaces == {}:
                    raise AttributeError ("was not able to assign Interfaces to blades")

        except Exception as e:
            logger.info("Sorting 'show run | section interface' - failed")
            logger.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            logger.info("Sorting 'show run | section interface' - Success")

    def sort_acl(self,acl_lines=None):
        """
        Gets all the ACL information in self.aclnumbers, creates an acl object for each number
        and gets the full acl information for that list.
        """
        logger.info(f"Sorting 'show run | section access-list' - Success")
        try:
            ACCESS = Access_Lists()
            if not acl_lines:
                # Grabs and stores each line of the switch's ACLs
                acl_lines = self.acl_result.split("\r\n")

            standard_ip_list = []
            extended_ip_lists = []
            ipv6_lists = []
            extended_mac_lists = []
            splitpoints = []

            for counter, list in enumerate(acl_lines):
                if list == '':
                    continue
                if "Standard IP" in list:
                    splitpoints.append(counter)
                if "Extended IP" in list:
                    splitpoints.append(counter)
                if "IPv6 access list" in list:
                    splitpoints.append(counter)
                if "Extended MAC" in list:
                    splitpoints.append(counter)

            sections = []
            for counter, point in enumerate(splitpoints):
                if counter == len(splitpoints) - 1:
                    sections.append('\r\n'.join(acl_lines[point:]))
                else:
                    sections.append('\r\n'.join(acl_lines[point:splitpoints[counter + 1]]))

            for list in sections:
                if "Standard IP" in list:
                    standard_ip_list.append(list)
                if "Extended IP" in list:
                    extended_ip_lists.append(list)
                if "IPv6 access list" in list:
                    ipv6_lists.append(list)
                if "Extended MAC" in list:
                    extended_mac_lists.append(list)

            for accesslist in standard_ip_list:
                accesslist = re.sub("Standard IP ", "", accesslist)
                a = self._sort_access_lists_2(accesslist, type="standard")
                a.type = 'Standard IP'
                ACCESS.standard_ip_lists.append(a)
                if a.number:
                    ACCESS.numbers.add(a.number)
                if a.name:
                    ACCESS.names.add(a.name)
            for accesslist in extended_ip_lists:
                accesslist = re.sub("Extended IP ", "", accesslist)
                if "preauth_" in accesslist:  # skip access lists for switch internal use
                    continue
                if "system-cpp" in accesslist:  # skip access lists for switch internal use
                    continue
                a = self._sort_access_lists_2(accesslist, type="extended")
                a.type = 'Extended IP'
                ACCESS.extended_ip_lists.append(a)
                if a.number:
                    ACCESS.numbers.add(a.number)
                if a.name:
                    ACCESS.names.add(a.name)
            for accesslist in ipv6_lists:
                accesslist = re.sub("IPv6 ", "", accesslist)
                a = self._sort_access_lists_2(accesslist, type="ipv6")
                a.type = 'IPv6'
                ACCESS.ipv6_lists.append(a)
                if a.number:
                    ACCESS.numbers.add(a.number)
                if a.name:
                    ACCESS.names.add(a.name)
            for accesslist in extended_mac_lists:
                accesslist = re.sub("Extended MAC ", "", accesslist)
                a = self._sort_access_lists_2(accesslist, type="mac")
                a.type = 'Extended MAC'
                ACCESS.extended_mac_lists.append(a)
                if a.number:
                    ACCESS.numbers.add(a.number)
                if a.name:
                    ACCESS.names.add(a.name)

        except Exception as e:
            logger.info(f"Sorting 'show run | section access-list' - FAILED")
            logger.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            logger.info(f"Sorting 'show run | section access-list' - Success")
            self.access_lists = ACCESS

    def _sort_access_lists_2(self, accesslist, type):
        """

        Args:
            accesslist (str): A String containing all only 1 access list output

        Returns :
            (ACL): an ACL object with

        """
        # TODO adjust this function to work with mac addresses
        try:
            a = ACL()
            a.raw_data = accesslist
            try:
                a.number = int(re.sub("access list ", "", accesslist.split("\r\n")[0]))
            except ValueError:  # string name not number
                a.name = re.sub("access list ", "", accesslist.split("\r\n")[0])

            if type == "ipv6":
                pass
            if type == "standard":
                for line in accesslist.split("\r\n"):
                    e = ACL_Entry()
                    if "access list " in line:
                        continue
                    e.raw_data = line
                    if '(' in line and ')' in line:
                        per = re.search('\(([^)]+)', line).group(1)
                        e.matches = [int(s) for s in per.split() if s.isdigit()][0]
                        line = re.sub(per, '', line)
                        line = re.sub('\)', '', line)
                        line = re.sub('\(', '', line)
                    if "wildcard" in line:  # process subnets on old devices
                        e.wildcard = line.split(', wildcard bits ')[1:][0]
                        line = line.split(', wildcard bits ')[:1][0]
                    if "log" in line:  # process subnets on old devices
                        e.log = True
                        line = re.sub("log", "", line)
                    options = line.split(" ")
                    options = [x for x in options if x]  # remove spaces
                    e.number = int(options[0])
                    if options[1] == 'permit':
                        e.permit = True
                    if options[1] == 'deny':
                        e.permit = False
                    try:
                        e.source = ipaddress.ip_address(options[2])
                    except ValueError as g:
                        if options[2] == 'any':
                            e.source = 'any'
                    finally:
                        a.Entries.append(e)
            if type == "extended":
                for line in accesslist.split("\r\n"):
                    e = ACL_Entry()
                    if "access list " in line:
                        continue
                    e.raw_data = line
                    if '(' in line and ')' in line:
                        per = re.search('\(([^)]+)', line).group(1)
                        e.matches = [int(s) for s in per.split() if s.isdigit()][0]
                        line = re.sub(per, '', line)
                        line = re.sub('\)', '', line)
                        line = re.sub('\(', '', line)
                    if "wildcard" in line:  # process subnets on old devices
                        e.wildcard = line.split(', wildcard bits ')[1:][0]
                        line = line.split(', wildcard bits ')[:1][0]
                    if "log" in line:  # process subnets on old devices
                        e.log = True
                        line = re.sub("log", "", line)
                    options = line.split(" ")
                    options = [x for x in options if x]  # remove spaces
                    e.number = int(options[0])
                    if options[1] == 'permit':
                        e.permit = True
                    elif options[1] == 'deny':
                        e.permit = False
                    if options[2] == 'tcp':
                        e.protocol = 'tcp'
                    elif options[2] == 'udp':
                        e.protocol = 'udp'
                    elif options[2] == 'ip':
                        e.protocol = 'any'
                    if options[3] == 'host':  # only a single ip address
                        try:
                            e.source = ipaddress.ip_address(options[4])
                        except ValueError as g:
                            print(g)
                            logging.error(g, exc_info=True)
                            if options[2] == 'any':
                                e.source = 'any'
                        if options[5] == 'any':  # handling destinations
                            e.destination = 'any'
                        if len(options) > 6:
                            if options[6] == 'eq':
                                try:
                                    e.destination_port = int(options[7])
                                except ValueError:
                                    e.destination_port = options[7]
                    elif options[3] == 'any':
                        e.source = 'any'
                    elif "." in options[3]:  # handle an wildcard
                        e.source = ipaddress.ip_address(options[3])
                        e.source_wildcard = options[4]
                        if options[5] == 'any':  # handling destinations
                            e.destination = 'any'
                        elif "." in options[5]:
                            e.destination = ipaddress.ip_address(options[5])
                            e.destination = options[6]
                            if len(options) > 8:
                                if options[8] == 'eq':
                                    e.destination_port = options[9]
                        elif len(options) > 6:
                            if len(options) > 7:
                                if options[7] == 'eq':
                                    e.destination_port = int(options[8])
                    if options[4] == 'any':
                        e.destination = 'any'
                    if len(options) > 5:
                        if options[5] == 'log':
                            e.destination_port = 'any'
                            e.log = True
                    a.Entries.append(e)
            if type == "mac":
                pass
        except Exception as e:
            logger.error(e, exc_info=True)
            print(e)
            _exception(e)
            raise
        else:
            return a

    def _sort_access_lists(self, accesslist, extended=False):
        """

        Args:
            accesslist (str): A String containing all only 1 access list output

        Returns :
            (ACL): an ACL object with

        """
        # TODO adjust this function to work with mac addresses
        try:
            a = ACL()
            try:
                a.number = int(re.sub("access list ", "", accesslist.split("\r\n")[0]))
            except ValueError:  # string name not number
                a.name = re.sub("access list ", "", accesslist.split("\r\n")[0])
            if extended:
                a.raw_data = f"Extended IP {accesslist}"
            else:
                a.raw_data = f"Standard IP {accesslist}"
            for line in accesslist.split("\r\n")[1:]:
                if line == '':
                    continue
                entry = ACL_Entry()
                entry.raw_data = line
                matches = 0
                wildcard = None
                if '(' in line and ')' in line:
                    per = re.search('\(([^)]+)', line).group(1)
                    matches = [int(s) for s in per.split() if s.isdigit()][0]
                    line = re.sub(per, '', line)
                    line = re.sub('\)', '', line)
                    line = re.sub('\(', '', line)
                if "deny" in line:
                    entry.type = "deny"
                    number = [int(s) for s in line if s.isdigit()]
                    number = int(''.join([str(x) for x in number]))
                    entry.number = number
                    entry.protocol = 'Any'
                    entry.matche_count = matches
                    continue
                if "any eq" in line:
                    line = re.sub("any eq", "", line)
                    protocol = line.split(" ")
                    protocol = [x for x in protocol if x]
                    protocol = protocol[len(protocol) - 1]
                    entry.match = 'eq'
                    entry.destination = 'any'
                    line = re.sub(f" {str(protocol)}", "", line)
                if "permit" in line:
                    entry.type = 'permit'
                    line = re.sub(f"permit ", "", line)
                if "udp" in line:
                    entry.type = 'udp'
                    line = re.sub(f"udp ", "", line)
                if "wildcard" in line:  # process subnets on old devices
                    wildcard = line.split(', wildcard bits ')[1:][0]
                    line = line.split(', wildcard bits ')[:1][0]
                if "host" in line:
                    line = re.sub(f"host ", "", line)
                count_check = line.split(" ")
                count_check = [x for x in count_check if x]
                if extended and len(count_check) > 4:
                    wildcard = line.split(" ")
                    wildcard = [x for x in wildcard if x]
                    wildcard = wildcard[len(wildcard) - 1]
                    line = re.sub(f" {str(wildcard)}", "", line)
                line = line.split(' ')
                line = [x for x in line if x]
                line = [x.rstrip() for x in line]
                entry.ipaddress = ipaddress.ip_address(line[len(line) - 1])
                if extended:
                    entry.typeofprotocol = line[len(line) - 2]
                    entry.type = line[len(line) - 3]
                    entry.number = line[len(line) - 4]
                else:
                    entry.type = line[len(line) - 2]
                    entry.number = line[len(line) - 3]
                entry.wildcard = wildcard
                entry.number = int(line[0])
                entry.matche_count = matches
                a.Entries.append(entry)
        except Exception as e:
            logger.error(e, exc_info=True)
            print(e)
            return a
        else:
            return a

    def sort_mac_address(self, mac_address_result):
        """
        assigns the variables from the mac address table to both the Vlans, and the ports from this command
        Args:
            mac_address_result (str): the output from command "show mac address-table"
        """
        logger.info("Sorting 'show mac address-table' - Starting")
        try:
            maclines = mac_address_result.split("\r\n")
            maclines = [x for x in maclines if x]
            macentries = []
            for line in maclines:
                if "Mac Address Table" in line:
                    continue
                elif "-------------------------------------------" in line:
                    continue
                elif "Vlan    Mac Address       Type        Ports" in line:
                    continue
                elif "----    -----------       --------    -----" in line:
                    continue
                elif "---------+-----------------+--------+---------+------+----+------------------" in line:
                    continue
                elif "Total Mac Addresses for this criterion:" in line:
                    continue
                elif "Legend:" in line:
                    continue
                elif "age - seconds since last seen,+ - primary entry using vPC Peer-Link" in line:
                    continue
                elif "                                                          Eth1/49/1" in line:
                    continue
                elif "* - primary entry, G - Gateway MAC, (R) - Routed MAC, O - Overlay MAC" in line:
                    continue
                elif "age - seconds since first seen,+ - primary entry using vPC Peer-Link" in line:
                    continue
                elif "VLAN     MAC Address      Type      age     Secure NTFY    Ports" in line:
                    continue
                else:
                    macentries.append(line)

            for macline in macentries:
                if not macline:
                    continue
                if "All" in macline:
                    continue
                if "Unicast" in macline:
                    continue
                if "---------" in macline:
                    continue

                if "vlan" in macline and 'mac' in macline and 'type' in macline:
                    continue
                if "Multicast" in macline and "Entries" in macline:
                    break
                macline = macline.split(" ")
                macline = [x for x in macline if x]
                if len(macline) == 8:
                    if '*' in macline or '*' in macline[0]:
                        shortport = macline[7]
                        vlan = int(macline[1])
                        macaddress = EUI(macline[2])
                    else:
                        shortport = macline[7]
                        vlan = int(macline[0])
                        macaddress = EUI(macline[1])
                else:
                    if not macline:
                        continue
                    if "Eth" in macline[0]:
                        continue
                    vlan = int(macline[0])
                    macaddress = EUI(macline[1])
                    shortport = macline[3]
                if len(macline) == 4:
                    shortport = macline[3]
                elif len(macline) == 5:
                    shortport = macline[4]
                if 'Port-channel' in shortport:  # handle port-channels
                    number = int(re.sub("Port-channel", "", shortport))
                    for po in self.port_channels:
                        if number == po.number:
                            po.mac_addresses.append(macaddress)
                    continue
                if shortport == 'Switch':
                    continue
                if "/" not in shortport:
                    continue
                port = shortport.split("/")
                if len(port) == 3:
                    port = shortport.split("/")[2]
                elif len(port) == 2:
                    port = shortport.split("/")[1]
                bl = int(self._get_interface_numbers(shortport.split("/")[0]))
                if bl == 0:
                    bl = 1
                for blade in self.blades:
                    if bl == blade.stacknumber:
                        if int(port) in [49,50,51,52]:
                            blade.moduleinterfaces[port].mac_addresses.append(macaddress)
                        else:
                            blade.interfaces[port].mac_addresses.append(macaddress)
                        break
                for vl in self.vlans:
                    if vlan == vl.number:
                        vl.mac_addresses.append(macaddress)
                        break

        except Exception as e:
            logger.info("Sorting 'show mac address-table' - failed")
            logger.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            pass

    def sortmodule(self, module):
        """
        Used to collect the blade information for chassis units.
        Args:
            module (str): A response from the command 'show module all'
            switchobj (Switch): A Switch Object

        Returns (Switch): a switch object with the blade objects
                            having been added
        """
        logger.info("Sorting 'show module all' - Starting")
        try:
            # create blade list if not already done
            if not self.blades:
                self.blades = set()
            # splits the response by line, and creates a generator
            if not '\r\n' in module:
                module = (module.split('\n'))
            else:
                module = (module.split('\r\n'))

            # removes random --More-- from the response
            module = [re.sub('--More--', '', x) for x in module]

            # sort through the response to locate the section listing all the modules
            headerline = None
            endofheader = None
            for line in module:
                if 'Mod Ports Card Type                              Model              Serial No.' in line:
                    headerline = module.index(line)
                elif 'Mod Ports Card Type                                   Model          Serial No.' in line:
                    headerline = module.index(line)
                elif 'Mod' in line and 'Ports' in line and 'Card' in line and 'Type' in line and 'Model' in line and 'Serial No.' in line:
                    headerline = module.index(line)
                elif 'M MAC addresses                    Hw  Fw           Sw               Status' in line:
                    endofheader = module.index(line)
                elif 'Mod MAC addresses                       Hw    Fw           Sw           Status' in line:
                    endofheader = module.index(line)
                elif 'Mod' in line and 'MAC addresses' in line and 'Hw'in line and 'Fw'in line and 'Sw' in line and 'Status' in line:
                    endofheader = module.index(line)

            allmodules = module[headerline + 2:endofheader - 1]
            for line in allmodules:
                line = line.split(' ')
                line = [x for x in line if x != '']
                b = Blade(line[len(line) - 1])
                b.stacknumber = int(line[0])
                b.modelnumber = line[len(line) - 2]
                if "SUP" in b.modelnumber:
                    b.SUP = True
                b.portcount = int(line[1])
                self.blades.add(b)

            if self.blades == set():
                raise AttributeError("unable to assign blades to Switch")

        except Exception as e:
            logger.info("Sorting 'show module all' - failed")
            logger.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            return self

    def sortportdowntime(self, portdowntime):
        """

        Args:
            portdowntime (str): A response from the command 'show interfaces link'

        Returns: a switch object with the Interface objects having the Downtime added to them

        """
        assert isinstance(portdowntime, str), f'portdowntime: must be str, but got {type(portdowntime)}'
        for blade in self.blades:
            assert blade.interfaces != [], f'Blade{blade.stacknumber} is missing interfaces'
        logger.info("Sorting 'show interfaces link' - Starting")
        try:
            # creates a list, and removes the empty strings in the list
            port = portdowntime.split('\r\n')
            port = [x for x in port if x != '']
            port = [x for x in port if x]
            for blade in self.blades:
                for key, interface in blade.interfaces.items():
                    for p in port:
                        if 'Port' in p and 'Name' in p and 'Down Time' in p and "Down Since" in p:  # skip titles
                            continue
                        if p == '          ':
                            continue
                        c = p[9:27]
                        p = re.sub(f'{c}', '', p)
                        p = p.split(' ')

                        # removes all None type objects from list
                        p = [x for x in p if x]
                        p = [x for x in p if x != '']
                        p = [x.rstrip() for x in p]

                        if p[0] == interface.shortname():
                            if p[1] == '00':
                                pass
                            else:
                                if self.modelnumber == 'C9410R':
                                    if '00:00:00' in p:
                                        continue
                                    if 'Gi' in p[0] or 'Te' in p[0]:
                                        p.remove(p[0])
                                    date_obj = datetime.strptime(''.join(p), "%H:%M:%S")
                                    interface.downtime = date_obj
                                else:
                                    downsince = p[len(p) - 5:]
                                    date_obj = datetime.strptime(' '.join(downsince), "%H:%M:%S %a %b %d %Y")
                                    interface.downtime = date_obj
        except Exception as e:
            logger.info("Sorting 'show interfaces link' - Failed")
            logger.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            logger.info("Sorting 'show interfaces link' - Success")

    def sortportcounters(self, portcounters):
        """
        This function applies all the port counters to all the ports in the switch object.
        Args:
            portcounters (str): A response from the command 'show interfaces counters'
            switchobj (Switch): A switch object with interfaces already pulled

        Returns: a switch object with the ports counters applied to all the interfaces
        """
        try:
            assert isinstance(portcounters, str), f'portcounters: must be str, but got {type(portcounters)}'
            assert self.blades != set(), f'Swithobj is missing blades'
            for blade in self.blades:
                assert blade.interfaces != [], f'Blade{blade.stacknumber} is missing interfaces'
            logger.info("Sorting 'show interfaces counters' - Starting")
            port = portcounters.split('\r\n')
            port = [x for x in port if x != '']
            for blade in self.blades:
                for key, interface in blade.interfaces.items():
                    out = False
                    for p in port:
                        p = p.split(' ')
                        p = [x for x in p if x != '']
                        if p:
                            if p[0] == interface.shortname():
                                if out:
                                    if self.modelnumber == 'Nexus5010':
                                        interface.outOctets = int(p[1])
                                        interface.outUcastPkts = int(p[2])
                                    else:
                                        interface.outOctets = int(p[1])
                                        interface.outUcastPkts = int(p[2])
                                        interface.outMcastPkts = int(p[3])
                                        interface.outBcastPkts = int(p[4])
                                else:
                                    if self.modelnumber == 'Nexus5010':
                                        interface.InOctets = int(p[1])
                                        interface.InUcastPkts = int(p[2])
                                    else:
                                        interface.InOctets = int(p[1])
                                        interface.InUcastPkts = int(p[2])
                                        interface.InMcastPkts = int(p[3])
                                        interface.InBcastPkts = int(p[4])
                                    out = True
                for key, interface in blade.moduleinterfaces.items():
                    out = False
                    for p in port:
                        p = p.split(' ')
                        p = [x for x in p if x != '']
                        if p:
                            if p[0] == interface.shortname():
                                if out:
                                    if self.modelnumber == 'Nexus5010':
                                        interface.outOctets = int(p[1])
                                        interface.outUcastPkts = int(p[2])
                                    else:
                                        interface.outOctets = int(p[1])
                                        interface.outUcastPkts = int(p[2])
                                        interface.outMcastPkts = int(p[3])
                                        interface.outBcastPkts = int(p[4])
                                else:
                                    if self.modelnumber == 'Nexus5010':
                                        interface.InOctets = int(p[1])
                                        interface.InUcastPkts = int(p[2])
                                    else:
                                        interface.InOctets = int(p[1])
                                        interface.InUcastPkts = int(p[2])
                                        interface.InMcastPkts = int(p[3])
                                        interface.InBcastPkts = int(p[4])
                                    out = True
        except Exception as e:
            logger.info("Sorting 'show interfaces counters' - Failed")
            logger.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            logger.info("Sorting 'show interfaces counters' - Success")

    def sortInventory(self, invresult):
        """
        takes the string for Invresults, and grabs the serial numbers for the system out of it.
        Args:
            invresult (str): a result for 'show inventory'
            switchobj (Switch): A switch object

        Returns (Switch):

        """
        assert isinstance(invresult, str), f'invresult: must be str, but got {type(invresult)}'
        logger.info("Sorting 'show Inventory' - Starting")
        try:
            inv = invresult.split('NAME:')

            if self.blades == None or self.blades == set():
                for hdevice in inv:
                    if hdevice == '':
                        continue
                    self.sort_inventory_hardware(hdevice)
            # get the serial number for the whole system
            for hdevice in inv:
                if hdevice == '':
                    continue
                hdeviceparts = hdevice.split(',')
                if 'Switch System' in hdevice:
                    for line in hdeviceparts:
                        if 'SN:' in line:
                            switchserial = line.split(':')[1].rstrip()
                            switchserial = re.sub(" ", "", switchserial)
                            self.serial = [switchserial]
                            logger.info("Sorting 'show Inventory' - Success")
                            return self

        except Exception as e:
            logger.info("Sorting 'show Inventory' - Failed")
            logger.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            logger.info("Sorting 'show Inventory' - Success")
            return self

    def sort_inventory_hardware(self,linelist):
        """
        I.e.
        NAME: "Power Supply Module 0", DESCR: "Cisco Catalyst 9500 Series 650W AC Power Supply"
        PID: C9K-PWR-650WAC-R  , VID: V01  , SN: ART2422F1CU
        Returns:
        """
        try:
            hdeviceparts = linelist.split(',')
            stacknumber = None
            supervisor = None
            if 'Slot' in hdeviceparts[0] and 'Linecard' in hdeviceparts[0]:
                stacknumber = re.sub('Slot','',hdeviceparts[0])
                stacknumber = re.sub('Linecard', '', stacknumber)
                stacknumber = re.sub('"','',stacknumber).strip()
            if 'Slot' in hdeviceparts[0] and 'Supervisor' in hdeviceparts[0]:
                supervisor = re.sub('Slot', '', hdeviceparts[0])
                supervisor = re.sub('Supervisor', '', supervisor)
                supervisor = re.sub('"', '', supervisor).strip()
            name = re.sub('','',hdeviceparts[0])
            name = re.sub('"','',name).strip()
            description = re.sub('DESCR:','',hdeviceparts[1])
            description = re.sub('"', '', description)
            description = re.sub('PID:', '', description)
            description = description.split('\r\n')
            if len(description) == 1:
                description = description[0].strip()
                pid = None
            else:
                pid = description[1].strip()
                description = description[0].strip()
            vid = re.sub('VID:','',hdeviceparts[2])
            vid = re.sub('"', '', vid).strip()
            sn = re.sub('SN:','',hdeviceparts[3]).strip('"')
            sn = re.sub('"', '', sn).strip()


            # if "Chassis" in name and self.modelnumber in pid: #use this entry as a blade in the switch
            #     bl = Blade()
            #     if stacknumber:
            #         bl.stacknumber = int(stacknumbner)
            #     bl.modelnumber = pid
            #     bl.serialnumber = sn
            #     if '48' in pid:
            #         bl.portcount = 48
            #     elif '24' in pid:
            #         bl.portcount = 24
            #     self.blades.add(bl)
            if pid in settings.line_card_pids:
                bl = Blade(sn)
                if stacknumber:
                    stacknumber = re.sub('-','',stacknumber)
                    bl.stacknumber = int(stacknumber)
                bl.modelnumber = pid
                if '48' in pid:
                    bl.portcount = 48
                elif '24' in pid:
                    bl.portcount = 24
                if supervisor:
                    bl.SUP = True
                    bl.stacknumber = int(supervisor)
                self.blades.add(bl)
            if description in settings.sfp_descriptions: #add SFP to list
                s = SFP()
                s.port = name
                s.SN = sn
                if '40G' in description:
                    s.speed = '40G'
                elif '10G' in description:
                    s.speed = '10G'
                elif '1000' in description:
                    s.speed = '1G'

                if 'SR' in pid:
                    s.type = 'SR'
                elif 'LR' in pid:
                    s.type = 'LR'
                elif 'LH' in pid:
                    s.type = 'LH'
                    s.speed = '1GB'

        except Exception as e:
            logger.info("Sorting 'show Inventory' - Failed")
            logger.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            pass

    def sortVersion(self, versionresult):
        """
        This functions pulls out the Stack information, Version number, Model Number, Serial number,
        and switch uptime for the 'show version' response
        Args:
            versionresult (str): A response from running 'show version' on a switch
            :param chassislist (list): A List of models that are switch chassis

        assignes values to the following:
        self.nexus (bool): Weather the device is nexus of not
        self.version (str): The IOS Version of the device
        self.hostname (str): The Configured hostname locally on the device
        self.uptime (datetime): a length of time the switch has been running for
        self.modelnumber (str): The Hardware Model of the device
        self.blades (list): [Blade,Blade,] The amount of blades in this switch, their serial number, and version number
        self.portcount (int): The total number of ports on this device

        """
        assert isinstance(versionresult, str), f'versionresult: must be str, but got {type(versionresult)}'
        logger.info("Sorting 'show Version' - Starting")
        try:
            stackline = None
            # run code here
            # search through response to gather the indivigual info
            if "Cisco IOS Software" in versionresult:
                self.nexus = False
            elif "Cisco Nexus Operating System" in versionresult:
                self.nexus = True
            else:
                self.nexus = False
            if not '\r\n' in versionresult:
                ver = versionresult.split('\n')
            else:
                ver = versionresult.split('\r\n')
            serialnumber = set()

            # sort version using nexus sort methods
            if self.nexus:
                for count, line2 in enumerate(ver):
                    if 'system:' in line2:
                        self.version = re.sub('version', '', line2)
                        self.version = re.sub('system:', '', self.version)
                        self.version = re.sub(' ', '', self.version)
                    elif 'Device name:' in line2:
                        self.hostname = re.sub('Device name:', '', line2)
                        self.hostname = re.sub(' ', '', self.hostname)
                    elif 'Kernel uptime' in line2:
                        self.uptime = re.sub('Kernel uptime is', '', line2)
                        self.uptime = re.sub(' ', '', self.uptime)
                    elif 'Hardware' in line2:
                        self.modelnumber = re.sub('cisco', '', ver[count + 1])
                        self.modelnumber = re.sub('"20x10GE/Supervisor"', '', self.modelnumber)
                        self.modelnumber = re.sub('Chassis', '', self.modelnumber)
                        self.modelnumber = re.sub(' ', '', self.modelnumber)
                        self.modelnumber = self.modelnumber.rstrip('()')
                        self.modelnumber = self.modelnumber.strip()
                        # self.blades = set()
                        # b = Blade()
                        # b.stacknumber = 1
                        # self.blades.add(b)
                logger.info("Sorting 'show Version' - Success")
                return self

            for count, line in enumerate(ver):
                # discover if there is more than one blade in this stack by counting serial numbers
                if 'System Serial Number' in line or 'System serial number' in line or 'Processor board ID' in line:
                    line = re.sub('System Serial Number', '', line)
                    line = re.sub('System serial number', '', line)
                    line = re.sub('Processor board ID', '', line)
                    line = re.sub(':', '', line)
                    line = re.sub(' ', '', line)
                    serialnumber.add(line)
                if 'Hardware: ' in line:
                    self.modelnumber = re.sub('Hardware: ','',line)
                    self.modelnumber = self.modelnumber.split(',')[0]
                    self.modelnumber = self.modelnumber.strip()
                    pass
                if 'Model Number ' in line:
                    self.modelnumber = re.sub("Model Number ", "", line)
                    self.modelnumber = re.sub(":", "", self.modelnumber)
                    self.modelnumber = [x for x in self.modelnumber if x]
                    self.modelnumber = ''.join([x for x in self.modelnumber if x != ' '])
                    self.modelnumber = self.modelnumber.strip()
                if "------ ----- -----              ----------        ----------            ----" in line:
                    stackline = count + 1
                # discover if device is a nexus device
                if 'uptime is' in line:
                    time = self._get_uptime(line)
                    self.uptime = self._get_uptime(line)
                # discovers if the switch is a chassis
                for model in settings.modularaccess:
                    if model in line:
                        self.modelnumber = model
                        # gets the all possible data points from Version
                        for line in ver:
                            # gets restart time
                            if 'System restarted at' in line:
                                self.uptime = line.split('at')[1]
                            if "Cisco IOS Software, IOS-XE Software," in line:
                                match = re.findall('[\d]{0,2}\.[\d]{0,2}\.[\da-zA-z]{0,3}\.[a-zA-Z]{0,3}|[\d]{0,2}\.[\d]{0,2}\.[\da-zA-z]{0,4}',line)
                                if match:
                                    self.version = match[0]


                        logger.info("Sorting 'show Version' - Success")
                        return self

            if self.modelnumber not in settings.modularaccess:  # handle working on a Stack of Switches
                if len(serialnumber) > 1:
                    self.__setattr__('stack', True)
                    if not stackline or stackline == None:
                        self.serial = []
                        # collects everything for all blades in stack
                        for line in ver:
                            if ('Switch' in line and
                                    'Ports' in line and
                                    'Model' in line and
                                    'SW Version' in line):
                                stackline = ver.index(line) + 2
                            # finds Serial Number
                            elif 'System Serial Number' in line or 'System serial number' in line:
                                line = line.split(':')[1]
                                line = re.sub(' ', '', line)
                                self.serial.append(line)
                                pass
                            # finds Switch uptime
                            elif 'uptime is' in line:
                                uptime = line.split('is')[1]
                                self.uptime = uptime
                    stackinfo = ver[stackline:stackline + 8]

                    endofstackline = None
                    for line in stackinfo:
                        if line == '' or line.strip() == '':
                            endofstackline = stackinfo.index(line)
                            break
                    stackinfo = stackinfo[:endofstackline]
                    tports = 0
                    self.blades = set()
                    bl = [x for x in stackinfo if x != '']
                    for bl in stackinfo:
                        bl = bl.split(' ')
                        bl = [x for x in bl if x != '']
                        bl = [x for x in bl if x != '*']
                        # get ports
                        b = Blade(None)
                        b.portcount = int(bl[1])
                        tports += int(bl[1])
                        b.modelnumber = bl[2]
                        b.ISOversion = bl[3]
                        b.stacknumber = int(bl[0])
                        self.blades.add(b)
                    self.portcount = tports

                else:
                    # collects information as just one switch
                    for line in ver:
                        if 'System Serial Number' in line or 'System serial number' in line:
                            line = line.split(':')[1]
                            line = re.sub(' ', '', line)
                            self.serial = line
                        # finds hardware type
                        elif 'Model Number' in line:
                            self.modelnumber = line.split(':')[1]
                            self.modelnumber = self.modelnumber.strip()
                        # finds Switch uptime
                        elif 'System restarted at' in line:
                            self.uptime = line.split('at')[1]
                        # finds up time on older switches
                        elif 'uptime is' in line:
                            uptime = line.split('is')[1]
                            self.uptime = uptime
                        # gets the index number of the titles for the stacks
                        elif ('Switch' in line and
                              'Ports' in line and
                              'Model' in line and
                              'SW Version' in line):
                            stackline = ver.index(line)
                    # gets the first stack line
                    if stackline: #create blades if there is information to do so else skip creation.
                        self.blades = set()
                        b = Blade(serialnumber.pop())
                        firststack = ver[int(stackline) + 2]
                        firststack = firststack.split(' ')
                        firststack = list(filter(None, firststack))
                        b.stacknumber = int(firststack[1])
                        b.portcount = firststack[2]
                        b.modelnumber = firststack[3]
                        b.ISOversion = firststack[4]
                        self.modelnumber = firststack[3]
                        self.modelnumber = self.modelnumber.strip()
                        self.version = firststack[4]
                        self.blades.add(b)
                    if self.blades == set():
                        bl = Blade(serialnumber.pop())
                        bl.modelnumber = self.modelnumber
                        bl.stacknumber = 1
                        for line in ver:
                            if 'TwentyFive Gigabit Ethernet interfaces' in line: # get mac address for blade
                                bl.portcount = int(re.sub('TwentyFive Gigabit Ethernet interfaces','',line).strip())
                            elif 'Cisco IOS XE Software, Version' in line:
                                bl.ISOversion = re.sub("Cisco IOS XE Software, Version","",line).strip()
                        self.blades.add(bl)
        except Exception as e:
            logger.info("Sorting 'show Version' - failed")
            logger.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            logger.info("Sorting 'show Version' - Success")
    def sortRun(self, runresult=''):
        """
        This functions pulls out the hostname, Vlans, Port-channel Interface, Port interfaces, Ip address,
        Network Mask, Default gateway, Uplink interfaces, SNMP Location, SNMP Contact, and Banner name
        for the 'show run'
        Args:
            switchobj (Switch): A switch object to have attributes applied to
            runresult (str): A response from running 'show run' on a switch

        Returns (Switch): A switch object with Attributes applied.
        """
        assert isinstance(runresult, str), f'runresult: must be str, but got {type(runresult)}'
        # assert hasattr(self, 'blades'), f'the blades have not been set on this object'
        # assert self.blades is not None, f'the blades have not been set on this object'
        logger.info("Sorting 'show run' - Starting")
        try:
            if not '\r\n' in runresult:
                run = runresult.split('\n')
            else:
                run = runresult.split('\r\n')
            vlanindex = set()
            interfaceindex = []
            endofinterfaces = None
            aclnumberlist = []
            # removes any --More-- that were randomly added.
            run = [re.sub('--More--', '', x) for x in run]

            # collect switch information
            for line in run:
                # put the system level name for the switch
                if 'Hostname' in line or 'hostname' in line:
                    self.hostname = re.sub('hostname', '', line).rstrip()
                    self.hostname = re.sub(' ', '', self.hostname)
                # get the ip address and subnetmask for this switch
                elif 'ip address' in line and 'no' not in line and 'remark' not in line:
                    if 'dhcp' in line:
                        continue
                    line = re.sub('ip address ', '', line)
                    self.IPAddress = line.split(' ')[1]
                    self.subnetmask = line.split(' ')[2]
                # get the default gateway for this switch
                elif 'ip default-gateway' in line:
                    self.defaultgateway = line.split(' ')[2]
                # grab the banner name for this switch
                elif 'banner login' in line:
                    self.bannername = run[run.index(line) + 1].rstrip()
                    if not self.bannername:  # handle a space right after banner login
                        self.bannername = run[run.index(line) + 2].rstrip()
                elif 'banner motd Z' in line:
                    self.bannername = run[run.index(line) + 1].rstrip()
                    if not self.bannername:  # handle a space right after banner login
                        self.bannername = run[run.index(line) + 2].rstrip()

                # seperate vlans
                elif 'switchport access vlan' in line:
                    pass
                elif 'vlan internal allocation policy ascending' in line:
                    pass
                elif 'snmp-server enable traps vlan' in line:
                    pass
                elif 'monitor session' in line and 'vlan' in line:
                    pass
                elif 'switchport voice vlan' in line:
                    pass
                elif 'ip dhcp snooping vlan 1-4094' in line:
                    pass
                elif 'snmp-server group NOCGrv3RO v3 auth context vlan-' in line:
                    pass
                elif 'switchport trunk allowed' in line:
                    pass
                elif 'switchport trunk native vlan' in line:
                    pass
                elif 'logging source-Interface Vlan' in line:
                    pass
                elif 'spanning-tree vlan' in line:
                    pass
                elif 'vlan configuration 1-4094' in line:
                    pass
                elif 'vlan configuration' in line:
                    pass
                elif 'pnp startup-vlan 850' in line:
                    pass
                elif 'interface-vlan' in line:
                    pass
                elif 'vlan 213,241,410-412' in line:
                    pass
                elif 'vlan 841,844-845' in line:
                    pass
                elif 'vlan 500,509-510' in line:
                    pass
                elif 'vlan 1 ' in line:
                    pass
                elif '\rvlan 1[K' in line:
                    pass
                elif 'limit-resource vlan' in line:
                    pass
                elif 'feature interface-vlan' in line:
                    pass
                elif 'vlan dot1q tag native' in line:
                    pass
                elif 'vlan' in line and ',' in line:
                    pass
                elif ' vlan ' in line and '#' in line:
                    pass
                elif 'vlan' in line and '-' in line:
                    pass
                elif 'vlan' in line and '====laundry' in line:
                    pass
                elif 'vlan' in line and 'configuration' in line:
                    pass
                elif 'vlan' in line and 'ip igmp snooping' in line:
                    pass
                elif 'vlan' in line and 'description' in line:
                    pass
                elif 'vlan' in line and 'shutdown' in line:
                    pass
                elif 'vlan ' in line.strip():
                    vlanindex.add(run.index(line))
                # seperate Access lists
                elif 'ip access-list' in line:
                    continue
                elif 'access-list' in line:
                    aclnumberlist.append(line)

            vlans = []
            # create Vlan objects from the sorted run file
            # TODO create handling for Vlans that have multiples, and ranges
            # IE vlan 500,509-510 or vlan 841,844-845
            for v in vlanindex:
                name = re.sub('--More--', '', run[v + 1])
                name = re.sub(',', '', name)
                name = re.sub('name', '', name)
                name = re.sub(' ', '', name)
                number = re.sub('--More--', '', run[v]).split(' ')
                number = [x for x in number if x != '']
                vl = vlan(int(number[1]))
                vl.name = name
                vlans.append(vl)
            self.vlans = vlans
            if not self.vlans:
                logger.error(f"Run Results:{run}")
                logger.error(f"vlans list:{vlans}")
                logger.error(f"vlans index numbers:{vlanindex}")
                raise ValueError("Vlans were not assigned")

            # sepereate the interfaces
            sortedinterfaces = []
            for inter in sorted(interfaceindex):
                next_interface_index = interfaceindex.index(inter) + 1
                if next_interface_index < len(interfaceindex):
                    next_interface = interfaceindex[next_interface_index]
                    interfacedetails = run[inter:next_interface]
                    sortedinterfaces.append(interfacedetails)
                else:
                    interfacedetails = run[inter:endofinterfaces - 1]
                    sortedinterfaces.append(interfacedetails)

            self.aclnumbers = set()
            # sort thorugh the acl stuff
            for aclline in aclnumberlist:
                line = aclline.split(' ')
                line = [x for x in line if x]
                self.aclnumbers.add(line[1])
        except Exception as e:
            logger.info("Sorting 'show run' - Failed")
            logger.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            logger.info("Sorting 'show run' - Success")
            return self
    def sortCdpNeiDetail(self, cdpnei):
        """
        This function pulls the neiboring device information from the command 'show cdp nei' and assigns the uplink
        variable to the Switch object.

        Args:
            ip (str): ipaddress of uplink switch
            cdpneidetail (list): A list split by line of the response when running Show cdp nei detail


        :return (list): A list of the seperated Responses of only SX switch information
        """
        assert isinstance(cdpnei, str), f'cdpnei must be a str, got {type(cdpnei)}'
        assert cdpnei is not None, f'cdpnei is an empty string. please pass through response from "show cdp nei detail"'
        logger.info("Sorting 'show cdp nei detail' - Starting")
        try:
            cdpneidetail = cdpnei.split('-------------------------')
            switchs = [x for x in cdpneidetail if x]
            self.uplinklist = []
            self.cdpneighbors = []
            for switch in switchs:
                cdpneiobj = self._get_neighbor(switch)
                self.cdpneighbors.append(cdpneiobj)
                self.uplinklist.append(cdpneiobj.interface)
        except Exception as e:
            logger.info("Sorting 'show cdp nei detail' - Failed")
            logger.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            logger.info("Sorting 'show cdp nei detail' - Success")
    def sortlogging(self, logging_result):
        """

        :param logging_result:
        :return:
        """
        assert isinstance(logging_result, str), f'logging_result: must be str, but got {type(logging_result)}'
        logger.info("Sorting 'show run | section looging' - Starting")
        try:
            logginglines = []
            logg = logging_result.split('\r\n')
            for line in logg:
                line = line.split(' ')
                for part in line:
                    try:
                        ip = ipaddress.ip_address(re.sub('\r', '', part))
                    except:
                        continue
                    logginglines.append((line, ip))


        except Exception as e:
            logger.info("Sorting 'show run | section looging' - Failed")
            logger.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            logger.info("Sorting 'show run | section looging' - Success")
            self.logging_data = logginglines
    def sortsnmp(self):
        """

        :param snmp_result:
        :return:
        """
        logger.info("Sorting 'show run | section snmp' - Starting")
        try:
            if "Invalid input detected at" not in self.snmp_result:
                snmp_result = self.snmp_result
            else:
                snmp_result = self.snmp_result_in

            snmp = snmp_result.split('\r\n')
            s = SNMP()
            for line in snmp:
                if 'v3' in line:
                    s.version.add(3)
                elif 'v2' in line:
                    s.version.add(2)
                if 'snmp-server view' in line:
                    part = line.split(' ')
                    v = SNMP_view()
                    v.name = part[2]
                    v.mibfamily = part[3]
                    if 'included' in line:
                        v.included = True
                    elif 'excluded' in line:
                        v.excluded = True
                    s.views.append(v)
                if 'snmp-server community' in line:  # Collect SNMP V2 info
                    s.version.add(2)
                    c = SNMP_community()
                    c.raw_data = line
                    line = re.sub('snmp-server community ', '', line)
                    line = line.split(' ')
                    c.string = line[0]
                    if 'RW' in line[1]:
                        c.rw = True
                    elif 'RO' in line[1]:
                        c.ro = True
                    if len(line) > 2:  # if an access list is present
                        c.accesslist = int(line[2])
                        if int(line[2]) in self.access_lists.numbers:
                            for access_list in self.access_lists.standard_ip_lists:
                                if access_list.number == int(line[2]):
                                    c.accesslist = access_list
                    s.communities.append(c)
                if 'snmp-server enable traps' in line:  # Collet the Traps for this device
                    line = re.sub('snmp-server enable traps ', '', line)
                    line = line.split(' ')
                    for t in line:
                        s.traps.append(t)
                if 'snmp-server host ' in line:  # collect the SNMP Logging hosts
                    line = re.sub('snmp-server host ', '', line)
                    line = line.split(' ')
                    for l in line:
                        try:
                            ip = ipaddress.ip_address(re.sub('\r', '', l))
                            s.loggingips.append(ip)
                        except:
                            continue
                if 'snmp-server group' in line:  # create Group objects
                    line = re.sub('snmp-server group ', '', line)
                    if 'v3 auth context vlan- match prefix' in line:
                        if 'PFGrv3RO' in line:
                            s.contextPFG = True
                            s.contextPFG_line = line.strip()
                        elif 'NOCGrv3RO' in line:
                            s.context = True
                            s.context_line = line.strip()
                        elif 'CliNOCGrv3RO' in line:
                            s.contextClinical = True
                            s.contextClinical_line = line.strip()
                        continue
                    g = SNMP_Group()
                    g.line = line
                    if '71' in line or '70' in line or '76' in line:
                        part = line.split(' ')
                        # look up ACL
                        aclnumber = int(part[len(part) - 1])
                        for acl in self.access_lists.standard_ip_lists:
                            if int(acl.number) == aclnumber:
                                g.acl = acl
                        # assign Group Name
                        g.name = part[0]
                        # assign Version
                        g.version = part[1]
                        # Assign View name
                        g.viewname = part[4]
                        if 'read' in line:
                            g.RO = True
                        if 'write' in line:
                            g.RW = True
                        if 'auth' in line:
                            g.securitylevel = 'auth'
                        elif 'priv' in line:
                            g.securitylevel = 'priv'
                    s.groups.append(g)
                if 'snmp-server user' in line:  # create Group objects
                    line = re.sub('snmp-server user ', '', line)
                    name = line.split(" ")
                    name = [x for x in name if x!='']
                    g = SNMP_User()
                    g.name = name[0]
                    s.user.append(g)
                if 'snmp-server host-group' in line:  # create Group objects
                    h = SNMP_Host_Group()
                    line = re.sub('snmp-server host-group', '', line)
                    line = re.sub('version 3', '', line)
                    line = line.split(" ")
                    line = [x for x in line if x!='']
                    h.interface = line[0]
                    h.network_object = line[1]
                    h.user = line[len(line)-1]
                    for count,l in enumerate(line):
                        if "poll" in l:
                            g.polling = True
                    s.host_group = h
                if 'snmp-server location' in line:
                    part = line.split(' ')
                    for count, p in enumerate(part):
                        if 'Bldg.' in p:
                            s.location_bldg = part[count + 1]
                        if 'Rm.' in p:
                            s.location_rm = re.sub('Rm.', '', p)
                if 'snmp-server contact' in line:
                    line = re.sub('snmp-server contact ', '', line)
                    part = line.split(' ')
                    if ',' in line:  # more than one Barcode/Assest Tag
                        if "Y-" not in part[0] and "BC-" not in part[0]:  # handle tags without headers
                            for p in part:
                                c = SNMP_contact()
                                c.tag = p
                                s.contacts.append(c)
                        else:
                            bcs = part[0]
                            bcs = re.sub('BC-', '', bcs)
                            bcs = bcs.split(',')
                            tags = part[1]
                            tags = re.sub('Y-', '', tags)
                            tags = tags.split(',')
                            for bc, tag in zip(bcs, tags):
                                c = SNMP_contact()
                                c.bc = bc
                                c.tag = tag
                                s.contacts.append(c)
                    elif ',' not in line and 'BC-' not in line and 'Y-' not in line:
                        continue
                    else:
                        c = SNMP_contact()
                        c.bc = re.sub('BC-', '', part[0])
                        c.tag = re.sub('Y-', '', part[1])
                        s.contacts.append(c)

        except Exception as e:
            logger.info("Sorting 'show run | section snmp' - Failed")
            logger.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            logger.info("Sorting 'show run | section snmp' - Success")
            self.SNMP = s
    def _sort_snmp_user(self):
        """
        Sorts through the command "show run snmp"
        """
        try:
            results = self.snmp_user_result.split('User name:')
            for user in results:
                if user == '':
                    continue
                lines = user.split('\r\n')
                U = SNMP_User()
                U.name = lines[0].strip()
                for line in lines:
                    if line == '':
                        continue
                    if "Authentication Protocol:" in line:
                        U.Auth_proto = re.sub('Authentication Protocol: ','',line).strip()
                    elif "Privacy Protocol: " in line:
                        U.priv_proto = re.sub('Privacy Protocol: ','',line).strip()
                    elif "Group-name: " in line:
                        U.group = re.sub('Group-name: ','',line).strip()
                self.SNMP.user.append(U)
        except Exception as e:
            logger.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            pass
    def sort_hostname(self):
        """
        Gets room numbers, bldg numbers, rack numbers, and node information
        """
        try:
            pattern = re.compile("([0-9]{2,4}[A-Za-z]{2,10})")
            hostsplit = self.hostname.split("-")
            hostsplit = [x for x in hostsplit if x]
            if "_" in self.hostname:
                self._sort_research_park_names(hostsplit,pattern,underscore=True)
            else:
                if "ddc" in self.hostname and not "3574ddc" in self.hostname:  # process Dataceneter names
                    # <function descriptor><number>-<building name>-<rack location>
                    self.function_descriptor = ''.join([i for i in hostsplit[0] if not i.isdigit()])
                    self.function_descriptor_number = int(re.sub(self.function_descriptor,"",hostsplit[0]))
                    self.description = settings.function_descriptors[self.function_descriptor]
                    self.buildingname = hostsplit[1]
                    self.buildnumber = '3574'
                    self.racknumber = hostsplit[2]
                    for abv in settings.nodeabrlist:
                        if abv in hostsplit:
                            self.node = abv
                            hostsplit.remove(abv)
                            break
                elif "3574ddc" in self.hostname:
                    self.function_descriptor = ''.join([i for i in hostsplit[0] if not i.isdigit()])
                    self.function_descriptor_number = int(re.sub(self.function_descriptor, "", hostsplit[0]))
                    self.description = settings.function_descriptors[self.function_descriptor]
                    self.buildingname = hostsplit[1]
                    self.buildnumber = '3574'
                    self.racknumber = hostsplit[2]
                    for abv in settings.nodeabrlist:
                        if abv in hostsplit:
                            self.node = abv
                            hostsplit.remove(abv)
                            break
                elif "tdc" in self.hostname:
                    # <function descriptor><number>-<building name>-<rack location>
                    self.function_descriptor = ''.join([i for i in hostsplit[0] if not i.isdigit()])
                    self.function_descriptor_number = int(re.sub(self.function_descriptor, "", hostsplit[0]))
                    self.description = settings.function_descriptors[self.function_descriptor]
                    self.buildingname = hostsplit[1]
                    self.buildnumber = '3475'
                    self.racknumber = hostsplit[2]
                elif not pattern.match(hostsplit[1]) and RepresentsInt(hostsplit[1]): #process addresses locations in research park
                    self._sort_research_park_names(hostsplit,pattern)
                else:  # edge names
                    self._sort_edge_names(hostsplit,pattern)
        except Exception as e:
            logger.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            pass
    def _sort_research_park_names(self,hostsplit,pattern,underscore=False):
        if underscore == True:
            hostsplit_a = self.hostname.split("_")
            self.address = hostsplit_a[0].split("-")[1]
            self.hostname = re.sub(f"{self.address}_", "", self.hostname)
            hostsplit = self.hostname.split("-")
            hostsplit = [x for x in hostsplit if x]
            self.function_descriptor = None
        hostsplit = self._sort_key_words(hostsplit)
        hostsplit = self._sort_function_descriptor(hostsplit)
        hostsplit = self._sort_abv_node(hostsplit)
        hostsplit = self._sort_buildingname_number(hostsplit,pattern)
        hostsplit = self._sort_name_leftovers(hostsplit)
    def _sort_edge_names(self,hostsplit, pattern):
        try:
            self.function_descriptor = None
            hostsplit = self._sort_key_words(hostsplit)
            hostsplit = self._sort_function_descriptor(hostsplit)
            hostsplit = self._sort_abv_node(hostsplit)
            hostsplit = self._sort_buildingname_number(hostsplit,pattern)
            hostsplit = self._sort_name_leftovers(hostsplit)
        except Exception as e:
            logger.error(e, exc_info=True)
            _exception(e)
            raise
    def _sort_key_words(self,hostsplit):
        if "PoE" in hostsplit:
            hostsplit.remove("PoE")
        if "noc" in hostsplit:
            hostsplit.remove("noc")
        if 'poison' in hostsplit:
            hostsplit.remove('poison')
        if 'airmed' in hostsplit:
            hostsplit.remove('airmed')
        if 'parkcitycovid' in hostsplit:
            hostsplit.remove('parkcitycovid')
        if 'indoors' in hostsplit:
            hostsplit.remove('indoors')
        if 'meraki' in hostsplit:
            hostsplit.remove('meraki')
        if 'liberty' in hostsplit:
            hostsplit.remove('liberty')
        if 'dental' in hostsplit:
            hostsplit.remove('dental')
        return hostsplit
    def _sort_function_descriptor(self,hostsplit):
        for i in range(1, 10):
            if f"sx{i}" in hostsplit[0]:
                hostsplit.remove(f"sx{i}")
                self.function_descriptor_number = i
                self.function_descriptor = "sx"
            elif f"scx{i}" in hostsplit[0]:
                hostsplit.remove(f"scx{i}")
                self.function_descriptor_number = i
                self.function_descriptor = "scx"
            elif f"SCX{i}" in hostsplit[0]:
                hostsplit.remove(f"SCX{i}")
                self.function_descriptor_number = i
                self.function_descriptor = "scx"
            elif f"SX{i}" in hostsplit[0]:
                hostsplit.remove(f"SX{i}")
                self.function_descriptor_number = i
                self.function_descriptor = "sx"
        for i in range(1, 3):
            if f"dx{i}" in hostsplit[0]:
                hostsplit.remove(f"dx{i}")
                self.function_descriptor_number = i
                self.function_descriptor = "dx"
            elif f"DX{i}" in hostsplit[0]:
                hostsplit.remove(f"DX{i}")
                self.function_descriptor_number = i
                self.function_descriptor = "dx"
        for i in range(1, 3):
            if f"r{i}" in hostsplit[0]:
                hostsplit.remove(f"r{i}")
                self.function_descriptor_number = i
                self.function_descriptor = "r"
            elif f"R{i}" in hostsplit[0]:
                hostsplit.remove(f"R{i}")
                self.function_descriptor_number = i
                self.function_descriptor = "r"
        for i in range(1, 3):
            if f"gw{i}" in hostsplit[0]:
                hostsplit.remove(f"r{i}")
                self.function_descriptor_number = i
                self.function_descriptor = "r"
            elif f"R{i}" in hostsplit[0]:
                hostsplit.remove(f"R{i}")
                self.function_descriptor_number = i
                self.function_descriptor = "r"
        if self.function_descriptor:
            self.description = settings.function_descriptors[self.function_descriptor]
        return hostsplit
    def _sort_abv_node(self,hostsplit):
        for abv in settings.nodeabrlist:
            if abv in hostsplit:
                self.node = abv
                hostsplit.remove(abv)
                break
        return hostsplit
    def _sort_buildingname_number(self,hostsplit,pattern):
        for portion in hostsplit:
            if pattern.match(portion):
                hostsplit.remove(portion)
                bldgsplit = re.split('(\d+)', portion)
                bldgsplit = [x for x in bldgsplit if x]
                self.buildnumber = int(bldgsplit[0])
                self._pad_building_number()
                self.buildingname = bldgsplit[1]
        return hostsplit
    def _sort_name_leftovers(self,hostsplit):
        try:
            if len(hostsplit) > 0:
                new_hostsplit = []
                for portion in hostsplit:
                    if portion == self.address:
                        continue
                    elif portion == self.buildingname:
                        continue
                    elif portion == self.node:
                        continue
                    elif portion == self.racknumber:
                        continue
                    elif portion == self.roomnumber:
                        continue
                    elif RepresentsInt(portion):
                        if portion == self.address:
                            continue
                        elif portion == self.buildnumber:
                            continue
                        else:
                            new_hostsplit.append(portion)
                    else:
                        new_hostsplit.append(portion)
                if len(new_hostsplit) == 1:  # most likely the room
                    self.roomnumber = new_hostsplit[0]
                if len(new_hostsplit) == 2:
                    self.roomnumber = new_hostsplit[0]
                    self.racknumber = new_hostsplit[1]
                if len(new_hostsplit) == 3:
                    if 'va' in new_hostsplit:
                        new_hostsplit.remove('va')
                        if new_hostsplit[0] == '1':
                            new_hostsplit.remove('1')
                            self.buildnumber = '3460'
                        elif new_hostsplit[0] == '2':
                            new_hostsplit.remove('2')
                            self.buildnumber = '3464'
                        elif new_hostsplit[0] == '3':
                            new_hostsplit.remove('3')
                            self.buildnumber = '3466'
                        elif new_hostsplit[0] == '7':
                            new_hostsplit.remove('7')
                            self.buildnumber = '3467'
                        elif new_hostsplit[0] == '14':
                            new_hostsplit.remove('14')
                            self.buildnumber = '3465'
                        elif new_hostsplit[0] == '45':
                            new_hostsplit.remove('45')
                            self.buildnumber = '3486'
                        else:
                            pass
                        self.buildingname = 'va'
                        self.roomnumber = new_hostsplit[0]
                    self.buildnumber = int(new_hostsplit[0])
                    self._pad_building_number()
                    self.buildingname = new_hostsplit[1]
                    self.roomnumber = new_hostsplit[2]
        except Exception as e:
            logger.error(e, exc_info=True)
    def _pad_building_number(self):
        self.buildnumber = str(self.buildnumber)
        self.buildnumber = self.buildnumber.zfill(4)
    def sortinterface_name(self, interface_name_r):
        """
        Creates an interface_result out of the results of "show run | in interface"
        Args:
            interface_name_r (str): from show run | in interface
        """

        try:
            interface_configurations = ""
            interfaces = interface_name_r.split("\r\n")
            for interface in interfaces:
                if "Vlan" in interface:
                    continue
                result = self.conn.send_command(f"show run {interface}")
                result = re.sub("Building configuration...", "", result)
                result = re.sub("end", "", result)
                result = re.sub("!", "", result)
                newlist = result.split("\r\n")
                for line in result.split("\r\n"):
                    if "Current configuration" in line:
                        newlist.remove(line)
                newlist = [x for x in newlist if x]
                newlist = [x for x in newlist if x != "\r"]
                string = "\r\n".join(newlist)
                interface_configurations = interface_configurations + string + "\r\n"
        except Exception as e:
            logger.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            self.interface_result = interface_configurations
    def sort_memoory_Usage(self):
        """
        gets the Memory Usage from switch, and calcuate percentage
        Returns:
            (int): Percentage of memory used
        """
        logger.info("Sorting Memory: Starting")
        total_memory = None
        used_memory = None
        percent_memory = None
        try:
            try:
                self.login()
            except Exception as ssh:
                logger.info("Sorting Memory: Unable to Collect")
                _exception(e)
                raise
            self.system_results = self.conn.send_command('show system resources', manypages=True)
            self.memory_results = self.conn.send_command('show processes memory', manypages=True)
            if "Invalid input detected at" not in self.system_results:
                for line in self.system_results.split('\r\n'):
                    if 'Memory usage:' in line:
                        line = re.sub("Memory usage: ","",line)
                        line = line.split(",")
                        for l in line:
                            if "total" in l:
                                l = re.sub("K total","",l)
                                l.split(" ")
                                l = [x for x in l if x]
                                l = [x for x in l if x != ' ']
                                l = "".join(l)
                                total_memory = int(l)
                            elif "used" in l:
                                l = re.sub("K used", "", l)
                                l.split(" ")
                                l = [x for x in l if x]
                                l = [x for x in l if x != ' ']
                                l = "".join(l)
                                used_memory = int(l)
                        if total_memory and used_memory:
                            break
                if not total_memory and not used_memory:
                    print(f"Not Sure What to Do: {self.ip}")
            elif "Invalid input detected at" not in self.memory_results:
                for line in self.memory_results.split("\r\n"):
                    if "Processor Pool" in line:
                        line = re.sub("Processor Pool","",line)
                        line = line.split(":")
                        for l in line:
                            if "Used" in l:
                                l = re.sub("Used","",l)
                                l.split(" ")
                                l = [x for x in l if x]
                                l = [x for x in l if x != ' ']
                                l = "".join(l)
                                total_memory = int(l)
                            elif "Free" in l:
                                l = re.sub("Free", "", l)
                                l.split(" ")
                                l = [x for x in l if x]
                                l = [x for x in l if x != ' ']
                                l = "".join(l)
                                used_memory = int(l)
                        if total_memory and used_memory:
                            break
                    elif "System memory" in line:
                        line = re.sub("System memory ", "", line)
                        line = re.sub(":", "", line)
                        line = line.split(",")
                        for l in line:
                            if "total" in l:
                                l = re.sub("K total","",l)
                                l.split(" ")
                                l = [x for x in l if x]
                                l = [x for x in l if x != ' ']
                                l = "".join(l)
                                total_memory = int(l)
                            elif "used" in l:
                                l = re.sub("K used", "", l)
                                l.split(" ")
                                l = [x for x in l if x]
                                l = [x for x in l if x != ' ']
                                l = "".join(l)
                                used_memory = int(l)
                        if total_memory and used_memory:
                            break
                    elif "Total (all processes)" in line:
                        l = line.split(" ")
                        l = [x for x in l if x]
                        l = [x for x in l if x != ' ']
                        used_memory = int(l[1])
                        free_bytes = int(l[3])
                        total_memory = used_memory + free_bytes
                        break
                if not total_memory and not used_memory:
                    print(f"Not Sure What to Do: {self.ip}")
            else:
                print(f"Not Sure What to Do: {self.ip}")
        except Exception as e:
            self.logout(self.conn)
            _exception(e)
            raise
        else:
            self.logout(self.conn)
            percent_memory = round(100 * (used_memory / total_memory))
            logger.info("Sorting Memory: Succeess")
            return (used_memory, percent_memory)
    def sort_power_inline(self):
        try:
            if 'Invalid input detected at' in self.inline_power_result:
                pass
            else:
                port_power_modules = self.inline_power_result.split('Module   Available     Used     Remaining')
                for module in port_power_modules:
                    if '' == module:
                        continue
                    module = re.sub('Interface Admin  Oper       Power   Device              Class Max','',module)
                    module = re.sub('(Watts)', '', module)
                    module = re.sub('--------- ------ ---------- ------- ------------------- ----- ----', '', module)
                    module = re.sub('------   ---------   --------   ---------', '', module)
                    module = re.sub('(Watts)     (Watts)    (Watts)', '', module)
                    lines = module.split('\r\n')
                    lines = [x for x in lines if x.strip()]
                    lines = [x for x in lines if x !='']
                    lines = [x for x in lines if '()' not in x]
                    if self.chassis:
                        self.assign_power_inline_to_chassis(lines[0])
                    else:
                        self.assign_power_inline_to_blade(lines[0])
                    lines.pop(0)
                    for line in lines:
                        self.assign_power_inline_to_interface(line)
        except Exception as e:
            self.logout(self.conn)
            logger.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            pass
    def assign_power_inline_to_interface(self,line):
        try:
            line_segs = line.split(' ')
            line_segs = [x for x in line_segs if x != '']
            for b in self.blades:
                for port,i in b.interfaces.items():
                    if i.short == line_segs[0]:
                        i.power_admin = line_segs[1]
                        i.power_oper = line_segs[2]
                        i.power_power = line_segs[3]
                        i.power_device = line_segs[4]
                        i.Class = line_segs[5]
                        i.Max = line_segs[6]
                        return
        except Exception as e:
            logger.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            pass
    def _convert_power_info(self,b,line_segs):
        try:
            if line_segs[1] == 'n/a':
                b.available_watts = line_segs[1]
                b.used_watts = line_segs[2]
                b.remaining_watts = line_segs[3]
            else:
                if len(line_segs) == 3:
                    b.available_watts = float(self._get_just_power_int(line_segs[0]))
                    b.used_watts = float(self._get_just_power_int(line_segs[1]))
                    b.remaining_watts = float(self._get_just_power_int(line_segs[2]))
                else:
                    b.available_watts = float(self._get_just_power_int(line_segs[1]))
                    b.used_watts = float(self._get_just_power_int(line_segs[2]))
                    b.remaining_watts = float(self._get_just_power_int(line_segs[3]))
        except Exception as e:
            self.logout(self.conn)
            logger.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            return b

    def assign_power_inline_to_chassis(self,line):
        try:
            line_segs = line.split(' ')
            line_segs = [x for x in line_segs if x != '']
            self.available_watts = float(self._get_just_power_int(line_segs[0]))
            self.used_watts = float(self._get_just_power_int(line_segs[1]))
            self.remaining_watts = float(self._get_just_power_int(line_segs[2]))
        except Exception as e:
            self.logout(self.conn)
            logger.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            pass

    def assign_power_inline_to_blade(self,line):
        try:
            line_segs = line.split(' ')
            line_segs = [x for x in line_segs if x != '']
            for b in self.blades:
                if len(self.blades) == 1:
                    if len(line_segs) == 3:
                        b = self._convert_power_info(b,line_segs)
                        break
                    else:
                        b = self._convert_power_info(b,line_segs)
                        break
                if int(line_segs[0]) == b.stacknumber:
                    b = self._convert_power_info(b,line_segs)
        except Exception as e:
            self.logout(self.conn)
            logger.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            pass

    def _get_just_power_int(self,line_seg):
        """

        Args:
            line_seg:

        Returns:

        """
        line_seg = re.sub('\(w\)',"",line_seg)
        line_seg = re.sub('Available:', "", line_seg)
        line_seg = re.sub('Used:', "", line_seg)
        line_seg = re.sub('Remaining:', "", line_seg)
        return line_seg
    def sort_enviroment(self):
        try:
            if 'Invalid input detected at' in self.environment_result:
                pass
            else:
                lines = self.environment_result.split('\r\n')
                for count, line in enumerate(lines):
                    if '--  ------------------  ----------  ---------------  -------  -------  -----' in line:
                        power_supplies = lines[count+1:]
                        for line in power_supplies:
                            if '\r' == line:
                                continue
                            if line == '':
                                continue
                            if 'SW  Status          RPS Name          RPS Serial#  RPS Port#' in line:
                                continue
                            if '---------' in line:
                                continue
                            self.assign_environment_power_to_blade(line)
        except Exception as e:
            self.logout(self.conn)
            logger.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            pass
    def assign_environment_power_to_blade(self,line):
        try:
            line = line.split(' ')
            line = [x for x in line if x != '']
            if 'Not' in line[1]:
                sw = line[0]
                blade = sw[0]
                slot = sw[1]
            else:
                sw = line[0]
                blade = int(sw[0])
                slot = sw[1]
                for b in self.blades:
                    if b.stacknumber == blade:
                        if slot == 'A':
                            b.slot_a_PID = line[1]
                            b.slot_a_serial = line[2]
                            if len(line) > 6:
                                b.slot_a_status = ' '.join(line[3:6])
                                b.slot_a_system_power = line[6]
                                b.slot_a_watts = 0
                            else:
                                b.slot_a_status = line[3]
                                b.slot_a_system_power = line[4]
                                b.slot_a_poe_power = line[5]
                                b.slot_a_watts = int(line[6])
                        if slot == 'B':
                            b.slot_b_PID = line[1]
                            b.slot_b_serial = line[2]
                            b.slot_b_status = line[3]
                            if len(line) > 6:
                                b.slot_b_status = ' '.join(line[3:6])
                                b.slot_b_system_power = line[6]
                                b.slot_b_watts = 0
                            else:
                                b.slot_b_system_power = line[4]
                                b.slot_b_poe_power = line[5]
                                b.slot_b_watts = int(line[6])
        except Exception as e:
            self.logout(self.conn)
            logger.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            pass
    def L2_Interfaces(self):
        """
        This is a generator that yeilds the first Layer 2 interface on a switch (1/0/1 or 0/1) and increments up to the
        last interface. This will skip interfaces on supervisors, and modules (Ie. Te1/1/1).
        Returns (Interface): An the first interface object, and incrementing up
        """
        try:
            while True:
                try:
                    self.blades = sorted(self.blades,key=lambda x: x.stacknumber)
                    for blade in self.blades:
                        if blade.SUP:
                            continue
                        for portnumber,interface in blade.interfaces.items():
                            yield interface
                            blade.interfaces[portnumber] = interface
                except Exception as e:
                    break
        except Exception as e:
            _exception(e)

    def add_interface(self,interface,blade_and_port=None,Next_availabe=False):
        """
        This is used for migrating Layer 2 interfaces from one hardware to another.
        Args:
            interface (Interface): an interface object from another piece of hardware
        Returns:
        """

        ignore = ['downtime', 'portnumber', 'type',
                  'InOctets', 'InUcastPkts', 'InMcastPkts',
                  'InBcastPkts', 'outOctets', 'outUcastPkts',
                  'outMcastPkts', 'outBcastPkts', 'fullname', 'number', 'short']
        try:
            for new_interface in self.L2_Interfaces():
                if Next_availabe:
                    if (new_interface.description == '' and
                            new_interface.vlan == 0 and
                            new_interface.trunk == False and
                            new_interface.trunkvlan == [] and
                            new_interface.voicevlan == '' and
                            new_interface.dualmode == False and
                            new_interface.stpf == False):
                        # this port is available
                        if new_interface.type == interface.type:
                            for key, value in vars(interface).items():
                                if key not in ignore:
                                    setattr(new_interface, f'{key}', value)
                            logger.debug(f'Transferring {interface.fullname} to {new_interface.fullname}')
                            new_interface.empty = False
                            return
                elif int(new_interface.blade) == int(blade_and_port[0]) and int(new_interface.portnumber) == int(blade_and_port[1]):
                    for blade in self.blades:
                        if int(new_interface.blade) == int(blade.stacknumber):
                            for key, value in vars(interface).items():
                                if key not in ignore:
                                    setattr(new_interface, f'{key}', value)
                            new_interface.empty = False
                            self.write_single_portconfig(new_interface)
                            return
                else:
                    continue
        except Exception as e:
            _exception(e)

    ############################################# Update Functions #############################################
    def write_single_portconfig(self,interface):
        """
        Takes the configuration from a single interface, and writes the configuration out to the device
        Args:
            interface (Interface):

        Returns:
        """
        logger.info("Writing Port configs to device - Started")
        try:
            config_lines = interface.run_config()
            result = self.conn.send_command('config t', trim=False)
            for line in config_lines:
                try:
                    result = self.conn.send_command(line)
                except Exception as e:
                    _exception(e)
            result = self.conn.send_command('end')
            result = self.conn.send_command('wri')
        except Exception as e:
            logger.info("Writing Port configs to device - Failed")
            logger.error(e, exc_info=True)
            _exception(e)
        else:
            logger.info("Writing Port configs to device - Success")

    def write_portconfig(self):
        """
        Takes all the port configurations stored in self.Ports and writes them to the connection
        :param (Connection): A Parimiko Objecct
        """
        assert isinstance(self.conn, Connection), f'self.conn is not a connection object: {type(self.conn)}'
        assert isinstance(self.portconfig, list), f'self.Ports is not list'
        logger.info("Writing Port configs to device - Started")
        try:
            result = self.conn.send_command('config t', trim=False)
            if '(config)' not in result:
                raise ValueError(f'Did not enter Config mode')
            for line in self.portconfig:
                try:
                    result = self.conn.send_command(line)
                except Exception as e:
                    _exception(e)
            result = self.conn.send_command('end')
            result = self.conn.send_command('wri')
        except Exception as e:
            logger.info("Writing Port configs to device - Failed")
            logger.error(e, exc_info=True)
        else:
            logger.info("Writing Port configs to device - Success")
    def write_vlans(self):
        """
        This function writes out the configuration of the vlans stored in self.vlans
        :param self.conn (Connection): A Parmimiko connection to the device
        """
        assert isinstance(self.conn, Connection), f'self.conn is not a connection object: {type(self.conn)}'
        logger.info("Writing vlan configs to device - Started")
        try:
            result = self.conn.send_command('config t', trim=False)
            if '(config)' not in result:
                raise ValueError(f'Did not enter Config mode')
            for vlan in self.vlans:
                if vlan.number in range(800, 899):
                    continue
                result = self.conn.send_command(f'vlan {vlan.number}')
                result = self.conn.send_command(f'name {vlan.name}')
            result = self.conn.send_command('end')
            result = self.conn.send_command('wri')
        except Exception as e:
            logger.info("Writing vlan configs to device - Failed")
            logger.error(e, exc_info=True)
        else:
            logger.info("Writing vlan configs to device - Success")
    def update_ACL(self, switch_connection):
        """
        Updates the ACL list with our standards on the switch, if needed.

        Args:
            switch_connection (Connection): Used to send and update ACLs on switch.
        """
        logger.info(f"Updating switch ACLs - Starting ({self.IPAddress})")
        try:
            # Saving old config incase we need to roll back
            old_acl = switch_connection.send_command("show run | inc access-list")

            output = switch_connection.send_command("conf t")
            # Rewriting 70 ACL
            if not self.acl_correct_status[70]:
                logger.info(f"Removing 70 ACLs ({self.IPAddress})")
                switch_connection.send_command("no access-list 70")
                logger.info(f"Adding standard 70 ACLs ({self.IPAddress})")
                for line in settings.standard_acl_70:
                    switch_connection.send_command(line)
            # Rewriting 71 ACL
            if not self.acl_correct_status[71]:
                logger.info(f"Removing 71 ACLs ({self.IPAddress})")
                switch_connection.send_command("no access-list 71")
                logger.info(f"Adding standard 71 ACLs ({self.IPAddress})")
                if self.IPAddress in settings.packetfence_switches:
                    for line in settings.standard_acl_71_snmp2:
                        switch_connection.send_command(line)
                else:
                    for line in settings.standard_acl_71:
                        switch_connection.send_command(line)
            # Rewriting 76 ACL (SNMPv3)
            if not self.acl_correct_status[76]:
                logger.info(f"Removing 76 ACLs ({self.IPAddress})")
                switch_connection.send_command("no access-list 76")
                if self.IPAddress in settings.packetfence_switches:
                    logger.info(f"Adding standard 76 ACLs ({self.IPAddress})")
                    for line in settings.standard_acl_76:
                        switch_connection.send_command(line)
            # Rewriting 199 ACL
            if not self.acl_correct_status[199]:
                logger.info(f"Removing 199 ACLs ({self.IPAddress})")
                switch_connection.send_command("no access-list 199")
                logger.info(f"Adding standard 199 ACLs ({self.IPAddress})")
                if "-565eejmrb-" in self.hostname:
                    for line in settings.standard_acl_199_bldg565:
                        switch_connection.send_command(line)
                else:
                    for line in settings.standard_acl_199:
                        switch_connection.send_command(line)
            logger.info(f"Saving config ({self.IPAddress})")
            switch_connection.send_command("end")
            switch_connection.send_command("wr")

            # Metric Logging
            if (not self.acl_correct_status[70] or not self.acl_correct_status[71]
                    or not self.acl_correct_status[76] or not self.acl_correct_status[199]):
                pass

        except Exception as e:
            logger.info(f"Exception Occurred - Rewriting 199 ACL config ({self.IPAddress})")
            result = switch_connection.send_command("conf t")
            result = switch_connection.send_command("no access-list 199")
            for line in settings.standard_acl_199:
                result = switch_connection.send_command(line)
            result = switch_connection.send_command("end")
            result = switch_connection.send_command("wr")
            logger.info(f"Updating switch ACLs for {self.IPAddress} - Failed")
            logger.error(f"{self.IPAddress} Failed Update ACL")
            logger.error(e, exc_info=True)
        else:
            logger.info(f"Updating switch ACLs for {self.IPAddress} - Success")
    def update_logging(self, switch_connection):
        """
        Updates the logging host addresses with our standards on the switch, if needed.

        Args:
            switch_connection (Connection): Used to send and update logging addresses on switch.
        """
        logger.info(f"Updating switch logging configuration for {self.IPAddress} - Starting")
        if self.should_overwrite_logging == None:
            logger.info(f"check_logging() must be run before update_logging() ({self.IPAddress})")
            logger.info("Updating switch logging configuration - Failed")
            return
        if not self.should_overwrite_logging:
            logger.info(f"No update for logging is needed ({self.IPAddress})")
            logger.info(f"Updating switch logging configuration for {self.IPAddress} - Success")
            return
        try:
            # Saving old logging config
            old_logging_config = switch_connection.send_command("show run | inc logging host")
            output = switch_connection.send_command("conf t")
            # Removing old IP addresses
            logger.info(f"Removing old logging addresses ({self.IPAddress})")
            old_logging_lines = []
            for line_info in self.logging_data:
                line = " ".join(line_info[0])
                line = line.strip("\r\n")
                old_logging_lines.append(line)
                logger.info(f"Removing: {line} ({self.IPAddress})")
                switch_connection.send_command("no " + line)
            # Adding log IP addresses
            logger.info(f"Adding new logging IP addresses ({self.IPAddress})")
            for ip_addr in settings.standard_log_ips:
                logger.info(f"Adding: logging host {ip_addr} ({self.IPAddress})")
                # TODO Use different switch commands according to software version
                output = switch_connection.send_command("logging host " + ip_addr)
            logger.info(f"Saving config ({self.IPAddress})")
            switch_connection.send_command("end")
            switch_connection.send_command("wr")
            new_logging_config = switch_connection.send_command("show run | inc logging host")
            # Metric Logging

        except Exception as e:
            logger.info(f"Exception Occurred - Rolling back config ({self.IPAddress})")
            # Undoing any new changes
            new_changes = switch_connection.send_command("show run | inc logging host")
            new_changes = new_changes.split("\n\r")
            for i in range(len(new_changes)):
                new_changes[i] = new_changes[i].strip()
            switch_connection.send_command("conf t")
            for line in new_changes:
                switch_connection.send_command(f"no {line}")
            # Writing old config
            old_logging_config = old_logging_config.split("\n\r")
            for i in range(len(old_logging_config)):
                old_logging_config[i] = old_logging_config[i].strip()
            for line in old_logging_config:
                switch_connection.send_command(line)
            switch_connection.send_command("end")
            switch_connection.send_command("wr")
            logger.info("Updating switch logging configuration - Failed")
            logger.error(f"{self.IPAddress} Failed Update Logging")
            logger.error(e, exc_info=True)

        else:
            logger.info("Updating switch logging configuration - Success")
    def update_orion_migration(self):
        """
        Update logging, SNMP, and ACL for the Orion migration.
        """
        logger.info("Orion Migration: Updating - Starting ")
        try:
            if self.acl_71_missing:
                self._create_acl(71)
            if not self.new_orion_ips_71:
                self._correct_acl_to_standard(71)
            if self.old_orion_ips_71:
                self._correct_acl_to_standard(71)
            if self.snmp_view_rw_missing:
                self._create_snmp('RW-view')
            if self.snmp_view_rw_wrong:
                self._modify_snmp('RW-view')
            if self.snmp_group_RW_missing:
                self._create_snmp('RW-group')
            if self.snmp_group_RW_wrong:
                for group in self.SNMP.groups:
                    if group.name == settings.SNMP.RW.group.name:
                        self._modify_snmp('RW-group',group)
            if self.snmp_user_RW_missing:
                self._create_snmp('RW-User')
            if self.snmp_user_RW_wrong:
                self._modify_snmp('RW-User')
            if self.SNMP_context_wrong:
                self._modify_snmp("context", self.SNMP.context_line)
            if self.SNMP_context_missing:
                self._create_snmp("context")
            if self.remove_SNMP_version_2:
                for community in self.SNMP.communities:
                    self._remove_snmp(community)
            for user in self.snmp_user_remove:
                self._remove_snmp(user)
            for view in self.snmp_view_remove:
                self._remove_snmp(view)
            for group in self.snmp_group_remove:
                self._remove_snmp(group)
            for acl in self.remove_acl:
                self._remove_acl(acl)

        except Exception as e:
            logger.info("Orion Migration: Updating - Failed ")
            logger.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            logger.info("Orion Migration: Updating - Success ")
    def _create_acl(self,number):
        try:
            result = self.conn.send_command('config t')
            result = self.conn.send_command(f"no access-list {str(number)}")
            if number == 71:
                for line in settings.standard_acl_71:
                    try:
                        result = self.conn.send_command(line)
                    except ValueError as v:
                        pass
            result = self.conn.send_command(f"end")
            result = self.conn.send_command(f"wri")
        except Exception as e:
            logger.error(e, exc_info=True)
            _exception(e)
            raise
    def _modify_acl(self,aclnumber):
        pass
    def _remove_acl(self,acl):
        """

        Args:
            acl:

        Returns:
        """
        try:
            result = self.conn.send_command('config t')
            result = self.conn.send_command(f"no access-list {str(acl.number)}")
            result = self.conn.send_command(f"end")
            result = self.conn.send_command(f"wri")
        except Exception as e:
            logger.error(e, exc_info=True)
            _exception(e)
            raise
    def _remove_snmp(self,snmpobj):
        """

        Args:
            snmpobj:

        Returns:

        """
        try:
            if isinstance(snmpobj,SNMP_community):
                result = self.conn.send_command('config t')
                result = self.conn.send_command(f"no {snmpobj.raw_data}")
                result = self.conn.send_command(f"end")
                result = self.conn.send_command(f"wri")
            elif isinstance(snmpobj,SNMP_Group):
                result = self.conn.send_command('config t')
                result = self.conn.send_command(f"no snmp-server group {snmpobj.line}")
                result = self.conn.send_command(f"end")
                result = self.conn.send_command(f"wri")
            elif isinstance(snmpobj,SNMP_User):
                result = self.conn.send_command('config t')
                result = self.conn.send_command(f"no snmp-server user {snmpobj.name} {snmpobj.group} v3")
                result = self.conn.send_command(f"end")
                result = self.conn.send_command(f"wri")
            elif isinstance(snmpobj,SNMP_view):
                result = self.conn.send_command('config t')
                result = self.conn.send_command(f"no snmp-server view {snmpobj.name}")
                result = self.conn.send_command(f"end")
                result = self.conn.send_command(f"wri")
        except Exception as e:
            logger.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            pass
    def _add_entry_to_acl(self,acl,entries):
        pass
    def _correct_acl_to_standard(self, number):
        """

        Args:
            acl:
            entries:

        Returns:

        """
        try:
            result = self.conn.send_command('config t')
            result = self.conn.send_command(f"no access-list {str(number)}")
            if number == 71:
                for line in settings.standard_acl_71:
                    try:
                        result = self.conn.send_command(line)
                    except ValueError as v:
                        pass
            result = self.conn.send_command(f"end")
            result = self.conn.send_command(f"wri")
        except Exception as e:
            logger.error(e, exc_info=True)
            _exception(e)
            raise
    def _create_snmp(self,type):
        if type == 'RW-group':
            try:
                result = self.conn.send_command('config t')
                result = self.conn.send_command(f"snmp-server group {settings.SNMP.RW.group.name} v3 {settings.SNMP.RW.group.security} read {settings.SNMP.RW.group.view.name} write {settings.SNMP.RW.group.view.name} access {settings.SNMP.RW.group.access} ")
                result = self.conn.send_command(f"end")
                result = self.conn.send_command(f"wri")
            except Exception as e:
                logger.error(e, exc_info=True)
                _exception(e)
                raise
        elif type == 'RW-view':
            try:
                result = self.conn.send_command('config t')
                result = self.conn.send_command(f"snmp-server view {settings.SNMP.RW.group.view.name} "
                                                f"{settings.SNMP.RW.group.view.access} "
                                                f"{settings.SNMP.RW.group.view.mibfamily}")
                result = self.conn.send_command(f"end")
                result = self.conn.send_command(f"wri")
            except Exception as e:
                logger.error(e, exc_info=True)
                _exception(e)
                raise
        elif type == 'RW-User':
            try:
                result = self.conn.send_command('config t')
                result = self.conn.send_command(f"snmp-server user {settings.SNMP.RW.username} {settings.SNMP.RW.group.name} {settings.SNMP.RW.group.version} auth {settings.SNMP.RW.snmpv3_auth_meth} {settings.SNMP.RW.snmpv3_auth_pass} priv {settings.SNMP.RW.snmpv3_priv_meth} {settings.SNMP.RW.snmpv3_priv_pass}")
                result = self.conn.send_command(f"end")
                result = self.conn.send_command(f"wri")
            except Exception as e:
                logger.error(e, exc_info=True)
                _exception(e)
                raise
        elif type == "context":
            try:
                result = self.conn.send_command('config t')
                result = self.conn.send_command(f"snmp-server group {settings.SNMP.RW.context_line}")
                result = self.conn.send_command(f"end")
                result = self.conn.send_command(f"wri")
            except Exception as e:
                logger.error(e, exc_info=True)
                _exception(e)
                raise
    def _modify_snmp(self,type,objtype):
        try:
            if type == "context":
                result = self.conn.send_command('config t')
                result = self.conn.send_command(f"no snmp-server group {objtype}")
                result = self.conn.send_command(f"snmp-server group {settings.SNMP.RW.context_line}")
                result = self.conn.send_command(f"end")
                result = self.conn.send_command(f"wri")
            elif type == 'RW-User':
                pass
            elif type == 'RW-view':
                pass
            elif type == 'RW-group':
                result = self.conn.send_command('config t')
                result = self.conn.send_command(f"no snmp-server group {objtype}")
                result = self.conn.send_command(f"end")
                result = self.conn.send_command(f"wri")
                self._create_snmp('RW-group')
        except Exception as e:
            logger.error(e, exc_info=True)
            _exception(e)
            raise
    def update_SNMP(self, switch_con):
        """
        Updates the SNMP configuration lines on the switch
        """
        logger.info(f"Updating SNMP ({self.IPAddress})  - Starting ")
        try:
            result = switch_con.send_command('config t')
            if 3 in self.SNMP.version:
                # apply any Group Corrections to the Switch
                for snmp_group in self.SNMP.groups:
                    if snmp_group.remove:
                        logger.debug(f"SNMP Group: {snmp_group} - removed")
                        result = switch_con.send_command(f'no {snmp_group.line}')
                    if not snmp_group.correct:
                        logger.debug(f"SNMP Group: {snmp_group} - added")
                        if snmp_group.acl.number == '71':
                            result = switch_con.send_command(f'{settings.SNMP_group_71.auth}')
                            result = switch_con.send_command(f'{settings.SNMP_group_71.priv}')
                        if snmp_group.acl.number == '70':
                            result = switch_con.send_command(f'{settings.SNMP_group_70.auth}')
                            result = switch_con.send_command(f'{settings.SNMP_group_70.priv}')
                        if snmp_group.acl.number == '76':
                            result = switch_con.send_command(f'{settings.SNMP_group_76.priv}')

                # apply all corrections SNMP View to the switch
                for snmp_view in self.SNMP.views:
                    if not snmp_view.correct:
                        logger.debug(f"SNMP View: {snmp_view} - added")
                        if 'PFviewRO' in snmp_view.name:
                            result = switch_con.send_command(f'{settings.SNMP_View.PFG}')
                        if 'NOCViewRO' in snmp_view.name:
                            result = switch_con.send_command(f'{settings.SNMP_View.RO}')
                        if 'NOCViewRW' in snmp_view.name:
                            result = switch_con.send_command(f'{settings.SNMP_View.RW}')

            if 2 in self.SNMP.version:
                pass

        except Exception as e:
            logger.info(f"Updating SNMP ({self.IPAddress}) - Failed ")
            logger.error(e, exc_info=True)
        else:
            logger.info(f"Updating SNMP ({self.IPAddress}) - Success ")
    def generate_config(self):
        """
        Returns:
        """
        try:
            pass
            # Create Configuration for interfaces
            # create configurations for Vlans
            # create Logging configuration
        except Exception as e:
            logger.error(e, exc_info=True)

    ############################################# Other Functions #############################################

    def login(self, quick=False):
        """Log in to a SSH device.

        Args:
            self.IPAddress: Device IP address or DNS hostname.
            quick: Optional boolean - if True, shorten timeouts for logging in.

        Returns:
            A Connection object to continue sending and receiving data from
            the device.

        Raises:
            ValueErrors if there are problems logging in to the device.
        """
        logger.debug(f'SSH connection - {self.ip}')
        client = None
        try:
            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            auth_retry = 0
            # make two login attempts, in case something strange happens
            while auth_retry < 2:
                try:
                    client.connect(self.ip, username=self.username,
                                   password=self.password, look_for_keys=False,
                                   allow_agent=False, timeout=(30 if quick else 60))
                    break  # successful

                except socket.timeout:
                    raise IOError("Connection timed out")
                except paramiko.ssh_exception.NoValidConnectionsError as N:
                    logger.error(N, exc_info=True)
                    raise
                except paramiko.ssh_exception.AuthenticationException as a:
                    if auth_retry < 2:
                        auth_retry += 1
                        time.sleep(2)
                    else:
                        logger.error('Login exception: ' + str(a))
                        raise IOError("Cannot log in to device (" + str(a) + ")")
                except socket.gaierror as g:
                    logger.info(f'Router Value was not found on network: {self.ip}')
                    logger.error(g, exc_info=True)
                    _exception(g)
                    raise

                except Exception as e:
                    logger.error(e, exc_info=True)
                    _exception(e)
                    raise

            if auth_retry >= 2:
                raise IOError(f"Cannot log in to device: {self.ip} (TACACS user expired?)")

            channel = client.invoke_shell(height=60, width=120)
            channel.settimeout((30 if quick else 60))
            header = channel.recv(4096)  # clear channel
            header = header.decode("utf-8")
            if '#' not in header and '>' not in header and "User:" in header: #login for wireless controllers
                channel.send(f"{self.username}\n")
                loop_counter = 0
                while not channel.recv_ready():
                    time.sleep(0.1)
                    loop_counter += 1
                    if loop_counter > 1200:  # stuck for more than 60 seconds, give up
                        raise ValueError("Stuck in wait loop.")
                if channel.recv_ready():
                    header = channel.recv(4096).decode("utf-8")
                if "Password" in header:
                    channel.send(f"{self.username}\n")
                    loop_counter = 0
                    while not channel.recv_ready():
                        time.sleep(0.1)
                        loop_counter += 1
                        if loop_counter > 1200:  # stuck for more than 60 seconds, give up
                            raise ValueError("Stuck in wait loop.")
                    if channel.recv_ready():
                        header = channel.recv(4096).decode("utf-8")

            while ('#' not in header and '>' not in header and not channel.recv_ready()):
                time.sleep(0.1)  # wait for login to be successful
            if channel.recv_ready():
                header = channel.recv(4096).decode("utf-8")

            if '#' not in header and '>' not in header:  # invalid prompt
                time.sleep(2)  # prompt may have not loaded yet
                header += channel.recv(4096).decode("utf-8")
                if '#' not in header and '>' not in header:
                    logger.info(header)
                    if channel is not None:
                        channel.close()
                    if client is not None:
                        client.close()
                    raise ValueError("Cisco prompt not reached")

            prompt = header.splitlines()[-1].strip()
            self.conn = Connection(client, channel, prompt)
        except paramiko.ssh_exception.NoValidConnectionsError as N:
            raise
        except OSError as O:
            logger.error(O, exc_info=True)
            raise
        except:
            if client is not None:
                client.close()
            raise

    def check_orion_migration(self,orionobj):
        """
        A function that checks the logging. ACL, and SNMP for the switch against policy standards.
        """
        logger.info("Orion Migration: Checking - Starting ")
        try:
            self.check_ACL()
            self.check_SNMP(orionobj)
            self.check_orion_snmp(orionobj)

        except Exception as e:
            logger.info("Orion Migration: Checking - Failed ")
            logger.error(e, exc_info=True)
        else:
            logger.info("Orion Migration: Checking - Success ")

    def check_ACL(self):
        """
        Compares ACLs found on switch to standard ACLs for edge devices. If any need to be updated,
        the ACL status is updated in the self.acl_correct_status dictionary under the ACL number.
        """
        logger.info(f"Checking ACL for {self.ip} - Starting ")
        try:
            # Checking switch 70 ACLs
            if 71 not in self.access_lists.numbers:
                self.acl_71_missing = True

            if self.access_lists.standard_ip_lists:
                for standard_list in self.access_lists.standard_ip_lists:
                    if standard_list.number == 71:
                        for entries in standard_list.Entries:
                            if str(entries.source) in settings.new_orion_ips:
                                self.new_orion_ips_71 = True
                            if str(entries.source) in settings.old_orion_ips or str(entries.source) == '155.98.253.0':
                                self.old_orion_ips_71 = True
                    elif standard_list.number == 76:
                        pass
                    else:
                        self.remove_acl.append(standard_list)
        except Exception as e:
            logger.info(f"Checking ACL for {self.IPAddress} - Failed")
            logger.error(f"{self.IPAddress} Failed Check ACL")
            logger.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            logger.info(f"Checking ACL for {self.IPAddress} - Success")

    def check_orion_snmp(self,orionobj):
        """
        Args:
            orionobj:

        Returns:
        """
        try:
            if orionobj['SNMPLevel'] == 2:
                self.orion_version_wrong = True
            if not orionobj['SNMPAuthType'] == settings.SNMP.RW.snmpv3_auth_meth:
                self.orion_auth_meth_wrong = True
            if not orionobj['SNMPEncryptType'] == settings.SNMP.RW.snmpv3_priv_meth:
                self.orion_encript_meth_wrong = True
            if not orionobj['SNMPUsername'] == settings.SNMP.RW.username:
                self.orion_username_wrong = True

        except Exception as e:
            logger.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            pass

    def check_SNMP(self,orionobj):
        """
        Takes the SNMP Information stored in self.SNMP, and checks it against our standards
        """
        logger.info(f"Checking SNMP ({self.ip}) - Starting ")
        try:
            # look for all the SNMP properties to determing what is missing
            if 3 in self.SNMP.version:
                self.check_SNMP_v3()
                if not hasattr(self.SNMP,"context_line"):
                    self.SNMP_context_missing = True
                else:
                    if self.SNMP.context_line != settings.SNMP.RW.context_line:
                        self.SNMP_context_wrong = True
            else:
                self.snmp_group_RW_missing = True
                self.snmp_view_rw_missing = True
                self.snmp_user_RW_missing = True

            if 2 in self.SNMP.version:
                if self.modelnumber in settings.SNMPv3_versions_supported:
                    self.remove_SNMP_version_2 = True
                elif self.modelnumber == None:
                    for model in self.blades:
                        if model.modelnumber in settings.SNMPv3_versions_supported:
                            self.remove_SNMP_version_2 = True
                else:
                    self.check_SNMP_v2()

        except Exception as e:
            logger.info(f"Checking SNMP ({self.ip}) - Failed ")
            logger.error(e, exc_info=True)
        else:
            logger.info(f"Checking SNMP ({self.IPAddress}) - Success ")

    def check_Logging(self):
        """
        Compares logging IP addresses found on switch against standard edge device logging IP
        addresses. If the IPs need to be updated, self.should_overwrite_logging is set to true.
        """
        logger.info(f"Checking logging IP addresses for {self.IPAddress} - Starting")
        try:
            current_log_ips = []
            for line_info in self.logging_data:
                # Grabs IPv4 address object as 1st index in tuple.
                ip = line_info[1]
                if type(ip) is ipaddress.IPv4Address:
                    current_log_ips.append(str(ip))
                else:
                    log_str = " ".join(line_info[0])
                    logger.info(f"Could not locate IP address from {log_str} ({self.IPAddress})")
            logger.info(f"Logging IP addresses extacted: {str(current_log_ips)} ({self.IPAddress})")

            # Compares current logging IP addresses to standard addresses
            if set(settings.standard_log_ips) == set(current_log_ips):
                logger.info(f"Logging IPs correctly match our standards ({self.IPAddress})")
                self.should_overwrite_logging = False

            else:
                logger.info(f"Logging IPs do not match our standards ({self.IPAddress})")
                self.should_overwrite_logging = True

        except Exception as e:
            logger.info(f"Checking logging IP addresses - Failed ({self.IPAddress})")
            logger.error(f"{self.IPAddress} Failed Check Logging")
            logger.error(e, exc_info=True)

        else:
            logger.info(f"Checking logging IP addresses - Success ({self.IPAddress})")

    def check_SNMP_v2(self):
        """
        Checks the SNMP object for Version 2 standards
        """
        logger.info(f"Checking SNMP v2 ({self.IPAddress}) - Starting")
        try:
            standard_ro = False
            standard_rw = False
            snmp_communities = []
            for s in self.SNMP.communities:
                if hasattr(SNMP_community,'accesslist'):
                    if (s.string == settings.SNMP_V2.standard_ro and
                            SNMP_community.accesslist == '70'):  # Check for the Standard RO SNMP V2
                        standard_ro = True
                        snmp_communities.append(s)
                    elif (s.string == settings.SNMP_V2.standard_rw and
                          SNMP_community.accesslist == '71'):  # Check for the Standard RO SNMP V2
                        standard_rw = True
                        snmp_communities.append(s)

        except Exception as e:
            logger.info(f"Checking SNMP v2 ({self.IPAddress}) - Failed ")
            logger.error(e, exc_info=True)
        else:
            logger.info(f"Checking SNMP v2 ({self.IPAddress}) - Success ")
            self.SNMP.communities = snmp_communities

    def _check_snmpv3_groups(self):
        try:
            if any([ True for x in self.SNMP.groups if settings.SNMP.RW.group.name == x.name]):#check for RW View
                pass
            else:
                self.snmp_group_RW_missing = True

            logger.debug(f"SNMP Groups {self.SNMP.groups}")
            for snmp_group in self.SNMP.groups:
                if snmp_group.acl != None:
                    if snmp_group.acl.number not in settings.permitted_SNMP_Groups:
                        self.snmp_group_remove.append(snmp_group)
                    elif snmp_group.RW and snmp_group.name != settings.SNMP.RW.group.name:
                        self.snmp_group_remove.append(snmp_group)
                else:
                    self.snmp_group_remove.append(snmp_group)

            for group in self.SNMP.groups:
                if not group.remove and group.RW:
                    if group.acl.number != 71:
                        self.snmp_group_RW_wrong = False
                    if group.securitylevel != 'priv':
                        self.snmp_group_RW_wrong = False
                    if group.viewname != settings.SNMP.RW.group.view.name:
                        self.snmp_group_RW_wrong = False
                    if group.version != settings.SNMP.RW.group.version:
                        self.snmp_group_RW_wrong = False
                    if not group.RO:
                        self.snmp_group_RW_wrong = False

        except Exception as e:
            logger.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            pass

    def _check_snmpv3_views(self):
        try:
            if any([ True for x in self.SNMP.views if settings.SNMP.RW.group.view.name == x.name]):#check for RW View
                pass
            else:
                self.snmp_view_rw_missing = True

            logger.debug(f"SNMP Views {self.SNMP.views}")
            for view in self.SNMP.views:
                if view.name == settings.SNMP.RW.group.view.name:
                    continue
                if view.name != settings.SNMP.RW.group.view.name:
                    self.snmp_view_remove.append(view)

            for view in self.SNMP.views:
                if not view.remove and view.name == settings.SNMP.RW.group.view.name:
                    if not view.included:
                        self.snmp_view_rw_wrong = True
                    if view.excluded:
                        self.snmp_view_rw_wrong = True
                    if view.mibfamily != 'internet':
                        self.snmp_view_rw_wrong = True
        except Exception as e:
            logger.error(e, exc_info=True)
            _exception(e)
            raise

    def _check_snmpv3_users(self):
        if any([ True for x in self.SNMP.user if settings.SNMP.RW.username == x.name]):#check for RW View
            pass
        else:
            self.snmp_user_RW_missing = True

        for user in self.SNMP.user:
            if user.name == settings.SNMP.RW.username:
                continue
            if user.name != settings.SNMP.RW.username:
                self.snmp_user_remove.append(user)

        for User in self.SNMP.user:
            if not User.remove and User.name == settings.SNMP.RW.username:
                if User.Auth_proto != 'MD5':
                    self.snmp_user_RW_wrong = True
                if User.group != 'NOCGrv3RW':
                    self.snmp_user_RW_wrong = True
                if User.priv_proto != 'DES':
                    self.snmp_user_RW_wrong = True

    def check_SNMP_v3(self):
        """
        Checks the SNMP object for Version 3 standards
        """
        logger.info(f"Checking SNMP v3 ({self.ip}) - Starting")
        try:
            # remove SNMP Groups outside of accepted
            self._check_snmpv3_groups()
            # remove SNMP Views outside of what is needed
            self._check_snmpv3_views()
            # remove SNMP Groups outside of accepted
            self._check_snmpv3_users()
        except Exception as e:
            logger.info(f"Checking SNMP v3 ({self.ip}) - Failed ")
            logger.error(e, exc_info=True)
        else:
            logger.info(f"Checking SNMP v3 ({self.ip}) - Success ")

    def get_mgmt_vlan(self, switch_connection):
        # This function will be rewritten
        # Gets and formats output from switch
        output = switch_connection.send_command("show run | section interface Vlan8")
        print(f"VLAN output: {output}")
        output = output.split("\r\n")
        for i in range(len(output)):
            output[i] = output[i].strip()
        # Parses output
        self.mgmt_vlan = None
        for line in output:
            print(line)
            if "interface Vlan8" in line:
                vlan_num = re.match(r'8\d{2}', line).group(0)
                self.mgmt_vlan = vlan(vlan_num)
                print(vlan_num)
            elif "description" in line:
                pass
            elif "ip address" in line:
                pass
        # Verifies information parsed
        if (not self.mgmt_vlan.number == 0
                or not self.mgmt_vlan.number == None):
            pass
        if (not self.mgmt_vlan.name == ""
                or not self.mgmt_vlan.name == None):
            pass
        if not self.mgmt_vlan.subnet == None:
            pass

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
            n = Neighbor()
            if not "\r\n" in neighborstr:
                neighborlist = neighborstr.split("\n")
            else:
                neighborlist = neighborstr.split("\r\n")
            neighborlist = [x for x in neighborlist if x]
            neighborlist = [x for x in neighborlist if "---" not in x]
            n.deviceid = re.sub("Device ID: ", "", neighborlist[0])
            for line in neighborlist:
                if "IP address: " in line:
                    line = re.sub("IP address: ", "", line)
                    line = re.sub("IP address: ", "", line)
                    line = line.split(" ")
                    line = [x for x in line if x]
                    n.ip = ipaddress.ip_address(line[0])
                elif "IPv4 Address: " in line:
                    line = re.sub("IPv4 Address: ", "", line)
                    line = re.sub("IPv4 Address: ", "", line)
                    line = line.split(" ")
                    line = [x for x in line if x]
                    ip = line[0].rstrip()
                    n.ip = ipaddress.ip_address(ip)
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
                    n.interface = self._get_interface_obj(localport)
                    # remove brackets and containing info
                    remoteport = re.sub(f':', '', line[1])
                    remoteport = re.sub("PortID", "", remoteport)
                    remoteport = re.sub('\(outgoingport\)', "", remoteport)
                    remoteport = re.sub("PortID:", "", remoteport)
                    n.remote_interface = remoteport
                elif "VTP Management Domain:" in line:
                    n.VTPDomain = re.sub("VTP Management Domain: ", "", line)
                    n.VTPDomain = re.sub(" ", "", n.VTPDomain)
                elif "Duplex:" in line:
                    n.duplex = re.sub("Duplex: ", "", line)
                    n.duplex = re.sub(" ", "", n.duplex)

            # assign the neigbor object to the interface
            if localport:
                for blade in self.blades:
                    if blade.stacknumber == localport[0]:
                        blade.interfaces[localportnumber].neighbor = n
        except Exception as e:
            logger.error(e, exc_info=True)
            print(e)
            _exception(e)
            raise
        else:
            return n

    def _get_interface_obj(self, portinfo):
        """

        Args:
            portinfo (List): A list of 2 long or 3 long
        """
        try:
            Inter = None
            if len(portinfo) == 2:
                for blade in self.blades:
                    if int(portinfo[0]) == 0:
                        if blade.stacknumber == 1:
                            for portnumber, interface in blade.interfaces.items():
                                if portinfo[1] == portnumber:
                                    Inter = interface
                    elif int(portinfo[0]) == blade.stacknumber:
                        for portnumber, interface in blade.interfaces.items():
                            if portinfo[1] == portnumber:
                                Inter = interface

            elif len(portinfo) == 3:
                for blade in self.blades:
                    if int(portinfo[1]) != 0:
                        pass
                    elif int(portinfo[0]) == blade.stacknumber:
                        for portnumber, interface in blade.interfaces.items():
                            if int(portinfo[2]) == portnumber:
                                Inter = interface
        except Exception as e:
            logger.error(e, exc_info=True)
            print(e)
            _exception(e)
            raise
        else:
            return Inter

    def _get_interface_numbers(self, intstr):
        """
        This function will remove all the letters in an interface leaving just the numbers, and special characters
        Args:
            intstr (str): any interface title

        Returns (str): just stack/module/port numbers or vlan number
        """
        try:
            intstr = re.sub("HundredGigE", "", intstr)
            intstr = re.sub("FortyGigabitEthernet", "", intstr)
            intstr = re.sub("TwentyFiveGigE", "", intstr)
            intstr = re.sub("TwentyFiveGig", "", intstr)
            intstr = re.sub("TenGigabitEthernet", "", intstr)
            intstr = re.sub("FiveGigabitEthernet", "", intstr)
            intstr = re.sub("TwoGigabitEthernet", "", intstr)
            intstr = re.sub("GigabitEthernet", "", intstr)
            intstr = re.sub("FastEthernet", "", intstr)
            intstr = re.sub("Ethernet", "", intstr)
            intstr = re.sub("Hu", "", intstr)
            intstr = re.sub("Twe", "", intstr)
            intstr = re.sub("Tw", "", intstr)
            intstr = re.sub("Te", "", intstr)
            intstr = re.sub("Gi", "", intstr)
            intstr = re.sub("Fa", "", intstr)
            intstr = re.sub("Eth", "", intstr)
            intstr = re.sub("Fi", "", intstr)
            intstr = re.sub("Fo", "", intstr)
            intstr = re.sub(" ", "", intstr)
            intstr = re.sub("\x1b", "", intstr)
            intstr = intstr.replace('\r', '')
            intstr = intstr.rstrip()
        except Exception as e:
            logger.error(e, exc_info=True)
        else:
            return intstr

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
            if not self.hostname:
                self.get_hostname()
            line = re.sub(self.hostname.rstrip(), '', line)
            line = re.sub('uptime is', '', line)
            line = re.sub('Kernel', '', line)
            line = re.sub(' ', '', line)

            deltadic = self._create_time(line.split(","))
            # create a time object
            delta = None
            delta = relativedelta(years=-deltadic["years"],
                                  months=-deltadic["months"],
                                  weeks=-deltadic["days"],
                                  hours=-deltadic["hours"],
                                  minutes=-deltadic["minutes"])

            # create Datetime object
            lastrestart = datetime.now() - delta

        except Exception as e:
            logger.error(e, exc_info=True)
            return
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
            logger.error(e, exc_info=True)
        else:
            return deltadict

    def removeunusedinterfaces(self):
        for blade in self.blades:
            blade.delportswithouttraffic()
            blade.delunconfiguredports()
            blade.delunusedportsoverperiodoftime()

    def complie_interface_configs(self):
        assert self.groupedvlans, f'You must run vlans first'
        all_config = ''
        for interface in self.interfaces:
            config = interface.run_config()
            all_config += config
        return all_config

    def Vlans(self):
        """
        Returns: a dictionary of key vlan number, and list of interfaces in that vlan sorted by largest vlan
        """
        interfaces = []
        for blade in self.blades:
            for key, interface in blade.interfaces.items():
                interfaces.append(interface)
        newinterfaces = []

        # remove all trunk interfaces
        for interface in interfaces:
            if not interface.trunk:
                newinterfaces.append(interface)
        # remove links to other network devices
        interfaces = []
        for interface in newinterfaces:
            for inter in self.cdpneighbors:
                if f"{inter.link['local']}" == f'{interface.fullname}':
                    pass
                else:
                    interfaces.append(interface)
        # remove interfaces without vlans
        newinterfaces = []
        for interface in interfaces:
            if interface.vlan == 0 and interface.trunk == False:
                pass
            else:
                newinterfaces.append(interface)
        vlans = {}
        groups = []
        newinterfaces = sorted(newinterfaces, key=lambda x: x.vlan)
        # group all interfaces by vlan number
        for k, g in itertools.groupby(newinterfaces, key=lambda x: x.vlan):
            groups.append(g)
            vlans[k] = list(g)

        newvlan = {}
        # arrange Vlans into desending order starting with largest vlan group
        for k in sorted(vlans, key=lambda k: len(vlans[k]), reverse=True):
            newvlan[k] = vlans[k]

        self.groupedvlans = newvlan

        return newvlan

    def allinterfaces(self):
        interfaces = []
        for blade in self.blades:
            interfaces += blade.interfaces
        return interfaces

    def generateportconfiguration(self):
        """
        Creates the Configuration output to be sent to a device from this object
        :return: the configuration formated as a string
        """
        logger.info('Generating Port Configuration - Starting')
        try:
            allconfigs = []
            for blade in self.blades:
                for key, interface in blade.interfaces.items():
                    config = interface.run_config()
                    for line in config:
                        allconfigs.append(line)
        except Exception as e:
            logger.info('Generating Port Configuration - Failed')
            logger.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            logger.info('Generating Port Configuration - Success')
            self.portconfig = allconfigs

    def check_vlan_name(self):
        """
        This method checks the vlans stored in self.vlans by comparing the the name assigned on the router node for
        this device against against the current name. The current name is changed if the name is different.
        """
        logger.info("Checking Vlan names - Starting")
        try:
            vlans = None
            AuthNode = None
            # check hostname for router info
            namesplit = self.hostname.split('-')
            node = namesplit[len(namesplit) - 1]
            if "new" in node:
                node = namesplit[len(namesplit) - 2]
            if node in settings.nodeabrlist:
                AuthNode = f'{node}'
            else:  # get Node the hard way
                for switch in self.cdpneighbors:
                    switchname = re.sub('.net.utah.edu', '', switch.hostname)
                    switchname = switchname.split('-')
                    switchname = '-'.join(switchname[:len(switchname)])
                    if switchname in settings.nodeabrlist:
                        AuthNode = switchname
                    else:
                        if 'dx' in switch.hostname:
                            pass
            if AuthNode:
                n = settings.nodes[AuthNode]
                r = Router(n['r1'])
                r.login()

                vlans = set()
                for vlan in self.vlans:
                    result = r.conn.send_command(f'show run int vlan {vlan.number}')
                    if 'description' in result:
                        for line in result.split('\n'):
                            if 'description' in line:
                                vlanname = re.sub('description', '', line)
                                vlanname = re.sub(' ', '', vlanname)
                                vlanname = re.sub('#', '', vlanname)
                                vlanname = re.sub('vlan', '', vlanname)
                                vlanname = re.sub(f'{vlan.number}', '', vlanname)
                                vlanname = re.sub(':', '', vlanname)
                                vlanname = vlanname.rstrip()
                                if vlanname != vlan.name:  # Vlan name is wrong
                                    vlan.name = vlanname
                                vlans.add(vlan)

                    else:  # missing description
                        vlans.add(vlan)
                        pass

        except Exception as e:
            logger.info("Checking Vlan names - Failed")
            logger.error(e, exc_info=True)
        else:
            logger.info("Checking Vlan names - Success")
            self.vlans = vlans
    def _remove_domain_name(self,name):
        name = re.sub('.net.utah.edu','',name)
        name = re.sub('.med.utah.edu', '', name)
        return name
    def _get_node_from_name(self,hostname):
        """

        Returns:

        """
        try:
            # check hostname for router info
            hostname = self._remove_domain_name(hostname)
            namesplit = hostname.split('-')
            for name in namesplit:
                if name.lower() in settings.ROUTERS_NXOS:
                    return name.lower()
        except Exception as e:
            logger.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            pass

    def get_distro_Node(self):
        """
        Run this Function to assign self.distro_nodes with the correct Park, Lib, Remote, etc
        """
        assert self.hostname is not None, f'Hostname not assigned'
        assert self.cdpneighbors is not None, f'You need to assign CDP Neighbnors before running'
        logger.info("Assigning Distribution Node - starting")
        try:
            self.distrobution_node = None
            # check hostname for router info
            namesplit = self.hostname.split('-')
            for node in settings.ROUTERS_NXOS:
                if node.lower() in namesplit:
                    self.node = node
                    self.distrobution_node = node
                    return
            node = namesplit[len(namesplit) - 1]
            if f'{node}' in settings.ROUTERS_NXOS:
                self.distrobution_node = f'{node}'
            else:  # get Node the hard way
                for switch in self.cdpneighbors:
                    node = self._get_node_from_name(switch.deviceid)
                    if node != None:
                        self.distrobution_node = node
                        self.node = node
                        logger.info("Assigning Distribution Node' - Success")
                        return
                    else:
                        if 'dx' in switch.deviceid:
                            s = Switch(str(switch.ip))
                            s.login()
                            s.getSwitchInfo()
                            s.assignattributes()
                            for cdp in s.cdpneighbors:
                                node = self._get_node_from_name(cdp.deviceid)
                                if node:
                                    self.node = node
                                    self.distrobution_node = node
                                    break

                            # TODO create the function for getting the CDP neibor for this node
                        else:  # handle daisy chained devices
                            for switch in self.cdpneighbors:
                                if 'sx' in switch.deviceid:
                                    pass
        except Exception as e:
            logger.info("Assigning Distribution Node - Failed")
            logger.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            logger.info("Assigning Distribution Node' - Success")

    def get_hostname(self):
        """
        gets only the hostname, and assigns it to self.hostname
        """
        try:
            self.login()
            hostname = self.conn.send_command("show run | in hostname")
            self.hostname = re.sub("hostname ", "", hostname)
        except Exception as e:
            logger.error(e, exc_info=True)

    def lifeCycleUpdate_interface_report(self):
        """
        This function collects all the Interfaces, and Vlans from an older switch
        and prints out the Ports count still in use
        Returns: None

        """
        try:
            # 1: remove interfaces that haven't been used in the last 6 months
            self.removeunusedinterfaces()
            # 2:Take the ports that are left, and group them by their vlan
            # arranging them by largest vlan to smallest
            portcount = 0
            for blade in self.blades:
                portcount = portcount + len(blade.interfaces)

        except Exception as e:
            logger.error(e, exc_info=True)
        else:
            return portcount

    def lifeCycleUpdate_power_report(self):
        """
        This function collects all the informataion on the power being used on this switch.7

        """
        try:
            total_used_power = 0
            power_supplies = []
            for b in self.blades:
                total_used_power += b.used_watts
                if b.slot_a_PID != None:
                    power = {}
                    power['pid'] = b.slot_a_PID
                    power['watts'] = b.slot_a_watts
                    power_supplies.append(power)
                if b.slot_b_PID != None:
                    power = {}
                    power['pid'] = b.slot_b_PID
                    power['watts'] = b.slot_b_watts
                    power_supplies.append(power)
        except Exception as e:
            logger.error(e, exc_info=True)
        else:
            return total_used_power, power_supplies
    def check_hostname(self):
        """
        Checks the device hostname against our naming standards
        """
        try:
            newhostname = None
            if "_" in self.hostname:  # handle Research Park names
                pass
            elif "sx" in self.hostname or "dx" in self.hostname:  # handle standard edge devices
                room = None
                bldg = None
                bldg_abv = None
                Rack = None
                distro_node = None

                if not self.roomnumber:
                    room = input("Please Enter a Room Number: ")
                if not self.buildnumber:
                    bldg = input("Please Enter a building Number: ")
                if not self.buildingname:
                    bldg_abv = input("Please Enter a building Abbreviation: ")
                if not self.racknumber:
                    Rack = input("Please Enter a Rack Number: ")
                if not self.distrobution_node:
                    distro_node = input("Please Enter a Distrobution Node (i.e. Park): ")

                only_switch = None
                switch_count = None
                while only_switch not in ("yes", "no"):
                    only_switch = input("Is this the only UIT-NOC switch in this room/rack?: ")
                    if only_switch == 'yes':
                        break
                    elif only_switch == 'no':
                        while switch_count not in (1, 2, 3, 4, 5):
                            switch_count = input("How many UIT NOC Switch are in the Room/rack?: ")
                            if switch_count in (1, 2, 3, 4, 5):
                                break
                            else:
                                print("Please Enter a number between 1 - 5")
                    else:
                        print("Please Enter 'yes' or 'no' ")

                newhostname = f"{'sx' if 'sx' in self.hostname else 'dx'}{str(switch_count) if switch_count else 1}-" \
                              f"{bldg if bldg else self.buildnumber}" \
                              f"{bldg_abv if bldg_abv else self.buildingname}-" \
                              f"{room if room else self.roomnumber}-" \
                              f"{Rack if Rack else self.racknumber}-" \
                              f"{distro_node if distro_node else self.distrobution_node}"



        except Exception as e:
            logger.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            return newhostname

    def assign_pinterfaces_to_vlans(self):
        """
        takes all the interfaces on this switch, and addes them to the v.interfaces option on each Vlan object

        Returns:
        """
        try:
            vlans = []
            for blade in self.blades:
                for vlan in self.vlans:
                    for number, interface in blade.interfaces.items():
                        if int(interface.vlan) == int(vlan.number):
                            vlan.interfaces.append(interface)
                    vlans.append(vlan)
            self.vlans = vlans
        except Exception as e:
            logger.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            return

    def remove_unsued_vlans(self):
        """
        should only be run after attributes have been applied, and interfaces have been assigned to vlans
        Returns:
        """
        vlans = []
        for vlan in self.vlans:
            if vlan.interfaces == []:
                continue
            vlans.append(vlan)
        self.vlans = vlans

class Chassis(Stack):

class Blade:
    def __init__(self,serialnumber):
        self.serialnumber = serialnumber
        self.modelnumber = ''
        self.ISOversion = ''
        self.stacknumber = 0
        self.portcount = 0
        self.uptime = None
        self.interfaces = {}
        self.inuseports = 48
        self.moduleinterfaces = {}
        self.cardtype = None
        self.SUP = False
        self.status = None
        self.fwversion = None
        self.hwversion = None
        self.macaddresses = None
        self.configured_ports = set()

        #power variables
        self.available_watts = None
        self.used_watts = None
        self.remaining_watts = None
        self.slot_a_PID = None
        self.slot_a_serial = None
        self.slot_a_status = None
        self.slot_a_system_power = None
        self.slot_a_poe_power = None
        self.slot_a_watts = None
        self.slot_b_PID = None
        self.slot_b_serial = None
        self.slot_b_status = None
        self.slot_b_system_power = None
        self.slot_b_poe_power = None
        self.slot_b_watts = None

    def __hash__(self):
        return hash((self.serialnumber,
        self.cardtype,
        self.SUP,
        self.status,
        self.fwversion,
        self.hwversion,
        self.macaddresses))

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.serialnumber == other.serialnumber

    # TODO create a function that generates the configuration for this blade

    def delunconfiguredports(self):
        """
        This function loops through all the ports on this blade removing any ports that lack configurations
        """
        interfaces = {}
        for key, interface in self.interfaces.items():
            if (interface.description == '' and
                    interface.vlan == 0 and
                    interface.trunk == False and
                    interface.trunkvlan == set() and
                    interface.voicevlan == '' and
                    interface.dualmode == False and
                    interface.stpf == False):
                logger.info(f'{interface.fullname} nothing assigned to this port - removing config')
                self.inuseports -= 1
            else:
                logger.info(f'{interface.fullname} has configuration information')
                interfaces.update({key: interface})
        self.interfaces = interfaces

    def delunusedportsoverperiodoftime(self):
        """
        This function removes all the ports that haven't sent traffic in the last 6 months
        """
        past = datetime.now() - timedelta(days=180)
        interfaces = {}
        for key, interface in self.interfaces.items():
            if interface.downtime:
                if interface.downtime < past:
                    logger.info(f'{interface.fullname} has not been up in the last 6 months - removing config')
                    self.inuseports -= 1
                else:
                    logger.info(f'{interface.fullname} has been used recently')
                    interfaces.update({key: interface})
            else:
                logger.info(f'{interface.fullname} is actively connected')
                interfaces.update({key: interface})

        self.interfaces = interfaces

    def delportswithouttraffic(self):
        """
        This function removes all the ports from the interfaces list that has never seen any traffic.
        """
        interfaces = {}
        for key, interface in self.interfaces.items():
            if (interface.InOctets == 0 and
                    interface.InUcastPkts == 0 and
                    interface.InMcastPkts == 0 and
                    interface.InBcastPkts == 0 and
                    interface.outOctets == 0 and
                    interface.outUcastPkts == 0 and
                    interface.outMcastPkts == 0 and
                    interface.outBcastPkts == 0):
                logger.info(f'{interface.fullname} has not sent any traffic - removing config')
                self.inuseports -= 1
            else:
                logger.info(f'{interface.fullname} has been sending traffic')
                interfaces.update({key: interface})
        self.interfaces = interfaces

    def transferinterface(self, interfaceobj, portname=None, nextavailable=False):
        """
        This function is for adding Interface infomration to the ports on this blade. This function does not
        change the number of ports, or the names of those ports on this blade.
        Args:
            portname (str): ex - 'GigabitEthernet0/1'
            interfaceobj (Interface): An interface object that has the port configuration you are looking for
            nextavailable (bool): Set true if you just want the first available port configured

        Returns:

        """
        assert self.interfaces is not None, f'There are no interfaces generated for this blade'
        assert isinstance(interfaceobj, Interface), f'There are no interfaces generated for this blade'
        logger.info(
            f'Transferring {interfaceobj.fullname} to Port:{"Next available" if nextavailable else portname} - Starting')
        try:
            interfaces = {}
            ignore = ['downtime', 'portnumber', 'type',
                      'InOctets', 'InUcastPkts', 'InMcastPkts',
                      'InBcastPkts', 'outOctets', 'outUcastPkts',
                      'outMcastPkts', 'outBcastPkts', 'fullname', 'number', 'short']

            if nextavailable:
                for key, interface in self.interfaces.items():
                    # selects the first available port
                    if (interface.description == '' and
                            interface.vlan == 0 and
                            interface.trunk == False and
                            interface.trunkvlan == [] and
                            interface.voicevlan == '' and
                            interface.dualmode == False and
                            interface.stpf == False):
                        # this port is available
                        if interface.type == interfaceobj.type:
                            for key, value in vars(interfaceobj).items():
                                if key not in ignore:
                                    setattr(interface, f'{key}', value)
                            logger.debug(f'Transferring {interfaceobj.fullname} to {interface.fullname}')
                            interface.empty = False
                            self.interfaces.update({key: interface})
                            break
                    else:
                        self.configured_ports.add(interface.portnumber)
                        if interface.portnumber == 48:
                            return "Blade is full"
                    interfaces.update({key: interface})
                #if each port is configured on this switch go to next switch in stack
                if not any ([i for i in range(1,self.portcount) if i in self.configured_ports]):
                    return "Blade is full"

            elif portname:
                assert isinstance(portname, str), f'portname must be a str, but got {type(portname)}'
                portnamelist = []
                for interface in self.interfaces:
                    portnamelist.append(interface.fullname)
                    # assigns the first available port
                    if interface.fullname == f'interface {portname}':
                        for key, value in vars(interfaceobj).items():
                            if key not in ignore:
                                setattr(interface, f'{key}', value)
                        logger.debug(f'Transferring {interfaceobj.fullname} to {interface.fullname}')
                        interface.empty = False
                    interfaces.update({key: interface})

                if f'interface {portname}' not in portnamelist:
                    raise ValueError(f'{portname} Not on this blade')

        except:
            logger.info(
                f'Transferring {interfaceobj.fullname} to Port:{"Next available" if nextavailable else portname} - failed')
            raise
        else:
            logger.info(
                f'Transferring {interfaceobj.fullname} to Port:{"Next available" if nextavailable else portname} - success')

class Switch(Blade):

