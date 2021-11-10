import re
import logging
import datetime
from .settings import cisco
from datetime import datetime
from collections import defaultdict
import concurrent
from concurrent.futures import ThreadPoolExecutor

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def remove_spaces(s):
    s = re.sub(" ", "", s)
    return s

def remove_byte_strings(result):
    new_result = []
    for l in result.split("\r\n"):
        l = bytes(l,'utf-8')
        if b'\x1b' in l:
            l=l.replace(b'\x1b',b'')
        new_result.append(l.decode('utf-8'))
    return '\r\n'.join(new_result)

def _exception(e):
    logger.error(e,exc_info=True)
    raise

class Network_Object:
    def __init__(self):
        self.name = None
        self.subnet = []

class Building:

    def __init__(self, dx1=None, dx2=None):
        """
        This Object handles controlling different aspects about a building's switch infrastructure.

        Args:
            demarkhostname (Switch): A Switch Object with the ipaddress of the Demark
            SecondDemark (Switch): A Switch Object with the ipaddress of the second Demark in the building
        """
        # assert isinstance(dx1, Switch), f'demark should be Switch object got {type(dx1)}'
        self.dx1 = dx1
        self.switches = []
        self.dx2 = dx2

    def _get_all_switch_info(self, ipad):
        """

        Returns:

        """
        try:
            s = Switch(str(ipad))
            s.login()
            s.getSwitchInfo()
            s.assignattributes()
            s.logout(s.conn)
        except Exception as e:
            return s
        else:
            return s

    def _discover_demark_from_switches(self):
        """
        Will assign any demarks from neighbors of any switches assigned.
        Returns:
        """
        try:
            dx1 = None
            dx2 = None
            for switch in self.switches:
                for neigbhor in switch.cdpneighbors:
                    if 'dx1' in neigbhor.deviceid.lower():
                        s = Switch(str(neigbhor.ip))
                        dx1 = s
                    if 'dx2' in neigbhor.deviceid.lower():
                        s = Switch(str(neigbhor.ip))
                        dx2 = s

            if not dx1 and not dx2:
                switches = set()
                for switch in self.switches:
                    for neigbhor in switch.cdpneighbors:
                        if 'sx' in neigbhor.deviceid.lower():
                            s = Switch(str(neigbhor.ip))
                            s.getSwitchInfo()
                            s.assignattributes()
                            switches.add(s)
                self.switches.union(set(switches))
                self._discover_demark_from_switches()

            if dx1:
                dx1.getSwitchInfo()
                dx1.assignattributes()
                self.dx1 = dx1
            if dx2:
                dx2.getSwitchInfo()
                dx2.assignattributes()
                self.dx2 = dx2

        except Exception as e:
            logging.error(e, exc_info=True)
            print(e)
            _exception(e)
            raise

    def collect_all_switches(self):
        """
        This function collects all the devices connected to both demarks creates a switch object for them all and stores
        them in a list
        """
        try:
            ipaddresses = set()
            if self.dx2:
                for neigbhor in self.dx2.cdpneighbors:
                    if "sx" in neigbhor.deviceid or "SX" in neigbhor.deviceid:
                        if str(neigbhor.ip) == str(self.dx1.ip):
                            continue
                        ipaddresses.add(neigbhor.ip)

            for neigbhor in self.dx1.cdpneighbors:
                if "sx" in neigbhor.deviceid or "SX" in neigbhor.deviceid:
                    if self.dx2:
                        if str(neigbhor.ip) == str(self.dx2.ip):
                            continue
                    ipaddresses.add(neigbhor.ip)

            ipaddresses_2 = set()
            # log into devices attached to the dx devices, and gather their attached devices
            with ThreadPoolExecutor(max_workers=20) as executor:
                future_to_ip = {executor.submit(self._get_all_switch_info, ipad): ipad for ipad in ipaddresses}

                for future in concurrent.futures.as_completed(future_to_ip):
                    ip = future_to_ip[future]
                    try:
                        s = future.result()
                        for neigbhor in s.cdpneighbors:
                            if hasattr(neigbhor, 'ip'):
                                if str(neigbhor.ip) == str(self.dx1.ip) or str(neigbhor.ip) == str(
                                        self.dx2.ip):
                                    continue
                                if "sx" in neigbhor.deviceid or "SX" in neigbhor.deviceid:
                                    if neigbhor.ip not in ipaddresses:
                                        ipaddresses_2.add(neigbhor.ip)
                    except Exception as exc:
                        continue

            ipaddresses_3 = set()
            if ipaddresses_2:
                with ThreadPoolExecutor(max_workers=20) as executor:
                    future_to_ip = {executor.submit(self._get_all_switch_info, ipad): ipad for ipad in ipaddresses_2}

                    for future in concurrent.futures.as_completed(future_to_ip):
                        ip = future_to_ip[future]
                        try:
                            s = future.result()
                            self.sx_switches.append(s)
                            for neigbhor in s.cdpneighbors:
                                if hasattr(neigbhor, 'ip'):
                                    if str(neigbhor.ip) == str(self.dx1.ip) or str(neigbhor.ip) == str(
                                            self.dx2.ip):
                                        continue
                                    if "sx" in neigbhor.deviceid or "SX" in neigbhor.deviceid:
                                        if neigbhor.ip not in ipaddresses or neigbhor.ip not in ipaddresses_2:
                                            ipaddresses_3.add(neigbhor.ip)
                        except Exception as exc:
                            continue

            if ipaddresses_3:
                with ThreadPoolExecutor(max_workers=20) as executor:
                    future_to_ip = {executor.submit(self._get_all_switch_info, ipad): ipad for ipad in
                                    ipaddresses_2}

                    for future in concurrent.futures.as_completed(future_to_ip):
                        ip = future_to_ip[future]
                        try:
                            s = future.result()
                            self.sx_switches.append(s)
                        except Exception as exc:
                            continue

            final_ipaddresses = set().union(ipaddresses, ipaddresses_2, ipaddresses_3)

            for ipad in final_ipaddresses:
                self.switches.append(Switch(str(ipad)))

            self.switches = []
            with ThreadPoolExecutor(max_workers=20) as executor:
                future_to_ip = {executor.submit(self._get_all_switch_info, ipad): ipad for ipad in
                                final_ipaddresses}

                for future in concurrent.futures.as_completed(future_to_ip):
                    ip = future_to_ip[future]
                    try:
                        s = future.result()
                        self.switches.append(s)
                    except Exception as exc:
                        continue
        except Exception as e:
            logging.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            pass

    def changedescription(self, remote, local, ipaddress, hostname):
        """
        Handles logging into the switch, testing the interface, and altering the interface in response
        Args:
            ipaddress (str): The Ip address of the device to be logged into
            remote (str): The interface for the far, or remote end of the connection.
            local: (str): The interface for the close, or local end of the connection on this device.

        Returns:
        """
        assert isinstance(remote, str), f"remote must be str, but got {type(remote)}"
        assert isinstance(local, str), f"local must be str, but got {type(local)}"
        assert isinstance(ipaddress, str), f"ipaddress must be str, but got {type(ipaddress)}"
        assert isinstance(hostname, str), f"hostname must be str, but got {type(hostname)}"
        if remote == '' or local == '' or ipaddress == '' or hostname == '':
            _exception(e)
            raise ValueError
        logger.info(f'Correcting {remote} on {ipaddress} - Starting')
        try:
            pass
            # # c = SwitchAccess(Switch_access.username, Switch_access.password)
            # # c = c.login(ipaddress)
            # # result = c.send_command(f'show run Interface {remote}')
            # # full_result = result
            # # logger.debug(result)
            #
            # if remote in result:
            #     result = result.split('\r\n')
            #     result = [x for x in result if 'Command' not in x]
            #     result = [x for x in result if 'Time' not in x]
            #     result = [x for x in result if 'version' not in x]
            #     result = [x for x in result if x != '']
            #     result = [x for x in result if x != '\r']
            #     response = ['config t']
            #     corret = True
            #     # create the short names for the description
            #     remote = re.sub("nGigabitEthernet", "", remote)
            #     remote = re.sub("igabitEthernet", "", remote)
            #     remote = re.sub("ernet", "", remote)
            #     local = re.sub("nGigabitEthernet", "", local)
            #     local = re.sub("igabitEthernet", "", local)
            #     local = re.sub("ernet", "", local)
            #     descriptionchallenge = f'key:{remote}:{hostname}:{local}'
            #     # loop over the inferface configuration
            #     for line in result:
            #         if 'description' in line:
            #             newdescrip = None
            #             # only get the interface portion of description
            #             description = re.sub("description", "", line)
            #             description = re.sub(" ", "", description)
            #             # Tests the description currently on the demark uplink interface
            #
            #             if descriptionchallenge == description:
            #                 logger.info(f'Description:{description} on {remote} - Correct')
            #                 metrics_logger.info(f'Device:{ipaddress} Description:{description} on {remote} - Correct')
            #             else:
            #                 logger.info(f'Description:{description} on {remote} - Incorrect')
            #                 metrics_logger.info(f'Device:{ipaddress} Description:{description} on {remote} - Incorrect')
            #                 newdescrip = f'description {descriptionchallenge}'
            #                 corret = False
            #                 response.append(newdescrip)
            #         # appends the interface into response.
            #         elif 'interface' in line:
            #             response.append(line)
            #
            #     # handle for missing Description line
            #     if 'description' not in full_result:
            #         logger.info(f'Description on {remote} - missing')
            #         metrics_logger.info(f'Device:{ipaddress} Description on {remote} - missing')
            #         corret = False
            #         newdescrip = f'description {descriptionchallenge}'
            #         response.append(newdescrip)
            #
            #     response.append('end')
            #     response.append('wri')
            #     # only send the commands to the interface is not correct
            #     if not corret:
            #         for command in response:
            #             result = c.send_command(command)
            #             logger.debug(f'response from device: {result}')

        except Exception as e:
            logger.info(f'Correcting {remote} on {ipaddress} - Failed')
            logger.error(e, exc_info=True)
        else:
            logger.info(f'Correcting {remote} on {ipaddress} - Success')

    def correctlinkinterfaces(self):
        """
        This function starts with the routers that are connected to the demarks in the building. It looks at their CDP
        Neigbhors, and sets the interface descriptions to the correct key format. Than Alters the interface descriptions
        on the demark leading to the routers, and the interface descriptions leading to the Switches_syntax_compatability. It repeats this
        one last time with the remaining switches altering their interface descriptions.
        """
        logger.info(f'Correcting Interfaces to Network Devices - Starting')
        # TODO Handle for remote sites that start with routers instead of DX
        # TODO Handle for Switch hanging off other switches
        try:
            # perform description update on dx2
            if self.dx2:
                # perform description update on R devices
                for switch in self.dx2.cdpneighbors:
                    if 'r1' in switch.hostname or 'r2' in switch.hostname:
                        logger.debug(f'testing interfaces on {switch.hostname}')
                        self.changedescription(switch.link["remote"], switch.link["local"],
                                               switch.ip, hostname=self.dx2.hostname)

                # perform description update on dx2
                logger.debug(f'testing interfaces on {self.dx2.hostname}')
                for switch in self.dx2.cdpneighbors:
                    self.changedescription(switch.link["local"], switch.link["remote"], self.dx2.ip,
                                           hostname=switch.hostname)

                # perform description update on Sx devices
                for switch in self.dx2.cdpneighbors:
                    if 'sx' in switch.hostname:
                        logger.debug(f'testing interfaces on {switch.hostname}')
                        self.changedescription(switch.link["remote"], switch.link["local"],
                                               switch.ip, hostname=self.dx2.hostname)

            # perform Description update for only one router
            for switch in self.dx1.cdpneighbors:
                # perform description update on R devices
                if 'r1' in switch.hostname or 'r2' in switch.hostname:
                    self.changedescription(switch.link["remote"], switch.link["local"],
                                           switch.ip, hostname=self.dx1.hostname)

            # perform description update on dx1
            for switch in self.dx1.cdpneighbors:
                self.changedescription(switch.link["local"], switch.link["remote"], self.dx1.ip,
                                       hostname=switch.hostname)

            # perform description update on Sx devices
            for switch in self.dx1.cdpneighbors:
                if 'sx' in switch.hostname:
                    self.changedescription(switch.link["remote"], switch.link["local"], switch.ip
                                           , hostname=self.dx1.hostname)
        except Exception as e:
            logger.error(e, exc_info=True)
        else:
            logger.info(f'Correcting Interfaces to Network Devices - Sucess')

    def migratetonewhardware(self, oldswitch: Switch, newswitch: Switch):
        """
        This function takes in two devices and old switch currently active, and a switch that will replace it on
        the network also currently live on the network. It will handle sorting through the ports,
        deleting unused ones, and grouping them by vlan. Those grouped ports, and vlans will than be
        applied to the new switch applying the largest vlan to the smallest vlan to the first blade, first port working
        it's way to the last blade, and last port.
        """
        # TODO add an options for padding Vlans with Extra ports for future projects.
        assert hasattr(oldswitch, 'ip'), "new an ip address to log into oldswitch"
        assert hasattr(newswitch, 'ip'), "new an ip address to log into newswitch"
        logger.info("Migration to new hardware - Starting")
        try:
            # clean away all the unused interfaces for the oldswitch
            activeports = []
            for blade in oldswitch.blades:
                blade.delunconfiguredports()
                blade.delunusedportsoverperiodoftime()
                blade.delportswithouttraffic()
                for key, interface in blade.interfaces.items():
                    activeports.append(interface)
            activeports.sort(key=lambda x: x.vlan, reverse=True)

            groups = defaultdict(list)

            for obj in activeports:
                groups[obj.vlan].append(obj)

            validvlans = []
            vlanlist = []
            for key, vlangroup in groups.items():
                if key == 0:
                    continue
                vlanlist.append(vlangroup)
                validvlans.append(key)

            # transfer the new vlans to the new switch
            for vlan in oldswitch.vlans:
                if vlan.number in validvlans:
                    newswitch.vlans.append(vlan)

            # check the names of the vlans
            newswitch.check_vlan_name()
            # write the vlans to the new device
            newswitch.write_vlans()

            vlanlist.sort(key=len, reverse=True)

            # create a que of interfaces that will be transfered
            # l = queue.Queue(maxsize=500)
            for value in vlanlist:
                for Interface in value:
                    newswitch.add_interface(Interface,Next_availabe=True)
                    # l.put(Interface)

            # add the ports to the new device starating with first blade, and moving to next

            # for blade in newswitch.blades:
            #     while not l.empty():
            #         result = blade.transferinterface(interfaceobj=l.get(), nextavailable=True)
            #         if result == "Blade is full":
            #             break
            # create the new running configuration
            newswitch.generateportconfiguration()

            # write the port configurations to the device
            newswitch.write_portconfig()

        except Exception as e:
            logger.info("Migration to new hardware - Failed")
            logger.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            logger.info("Migration to new hardware - Success")

    def migrate_multiple_old_to_new_hardware(self, oldswitchs: list, newswitch: Switch):
        """
        This function takes in two devices and old switch currently active, and a switch that will replace it on
        the network also currently live on the network. It will handle sorting through the ports,
        deleting unused ones, and grouping them by vlan. Those grouped ports, and vlans will than be
        applied to the new switch applying the largest vlan to the smallest vlan to the first blade, first port working
        it's way to the last blade, and last port.
        """
        try:
            # collect all the inforamtion for each switch
            for switch in oldswitchs:
                switch.getSwitchInfo()

            # clean away all the unused interfaces for the oldswitch
            # activeports = []
            # for blade in oldswitch.blades:
            #     blade.delunconfiguredports()
            #     blade.delunusedportsoverperiodoftime()
            #     blade.delportswithouttraffic()
            #     for key, interface in blade.interfaces.items():
            #         activeports.append(interface)
            # activeports.sort(key=lambda x: x.vlan, reverse=True)
            #
            # groups = defaultdict(list)
            #
            # for obj in activeports:
            #     groups[obj.vlan].append(obj)
            #
            # validvlans = []
            # vlanlist = []
            # for key, vlangroup in groups.items():
            #     if key == 0:
            #         continue
            #     vlanlist.append(vlangroup)
            #     validvlans.append(key)
            #
            # # transfer the new vlans to the new switch
            # for vlan in oldswitch.vlans:
            #     if vlan.number in validvlans:
            #         newswitch.vlans.append(vlan)
            #
            # # check the names of the vlans
            # newswitch.check_vlan_name()
            # # write the vlans to the new device
            # newswitch.write_vlans()
            #
            # vlanlist.sort(key=len, reverse=True)
            #
            # # create a que of interfaces that will be transfered
            # l = queue.Queue(maxsize=500)
            # for value in vlanlist:
            #     for Interface in value:
            #         l.put(Interface)
            #
            # # add the ports to the new device starating with first blade, and moving to next
            # for blade in newswitch.blades:
            #     while not l.empty():
            #         result = blade.transferinterface(interfaceobj=l.get(), nextavailable=True)
            #         if result == "Blade is full":
            #             break
            # # create the new running configuration
            # newswitch.generateportconfiguration()
            #
            # # write the port configurations to the device
            # newswitch.write_portconfig()

        except Exception as e:
            logger.info("Migration to new hardware - Failed")
            logger.error(e, exc_info=True)
        else:
            logger.info("Migration to new hardware - Success")
            end_time = datetime.now()
            metrics_logger.info(f'Finished moving vlans, and ports in: {end_time - start_time}')

    def portcountreport(self):
        """
        Running this function will calculate the active number of ports per switch in a building. Present a total per stack
        and persentage per stack as well as a building total and percentage.
        Returns:
        """
        try:
            Totalportcount = 0
            Totalactivecount = 0
            devices = []
            for s in self.sx_switches:
                try:
                    singleportcount = s.lifeCycleUpdate_interface_report()
                    Totalactivecount = Totalactivecount + singleportcount
                    Totalportcount = Totalportcount + s.portcount
                    print(f"----------------{s.hostname}----------------")
                    print(f"Total Ports: {s.portcount}")
                    print(f"Active Ports: {singleportcount}")
                    print(f"Port Percent Utilization: {(singleportcount / s.portcount) * 100}")
                except Exception as e:
                    logging.error(e, exc_info=True)
                    print(e)
                    _exception(e)
                    raise
            print(f"Building Total Ports: {Totalportcount}")
            print(f"Building Active Ports: {Totalactivecount}")
            print(f"Building Port Percent Utilization: {(Totalactivecount / Totalportcount) * 100}")

        except Exception as e:
            logging.error(e, exc_info=True)
            print(e)
            _exception(e)
            raise

class Node():
    """
    This object incompases everything from a distribution node down to the edge devices
    """

    def __init__(self, r1_ipaddress=None, r2_ipaddress=None):
        self.r1_ipaddress = r1_ipaddress
        self.r2_ipaddress = r2_ipaddress
        self.r1 = None
        self.r2 = None
        self.edgedevices = []
        self.touchingdevices = []

    def assign_routers(self):
        """
        Takes the ip addresses from self.r1_ipaddress, self.r2_ipaddress and creates Router Objects for each than
        assigns them to self.R1, and self.R2
        Returns:
        """
        logger.info(f'Contacting Both Routers in Node, and Assigning attributes - Starting')
        try:
            r1 = Router(self.r1_ipaddress)
            r1.login()
            r1.getSwitchInfo()
            r1.assignattributes()
            self.r1 = r1
            r1.logout(r1.conn)

            r2 = Router(self.r2_ipaddress)
            r2.login()
            r2.getSwitchInfo()
            r2.assignattributes()
            self.r2 = r2
            r2.logout(r2.conn)
        except Exception as e:
            logger.info(f'Contacting Both Routers in Node, and Assigning attributes - Failed')
            logger.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            logger.info(f'Contacting Both Routers in Node, and Assigning attributes - Success')

    def get_all_vlans(self):
        """

        Returns (set): A list of all the vlans from both routers

        """
        try:
            logger.info(f'Getting Vlans on: {self.r1.hostname} - Starting')
            vlans = set()
            for v1 in self.r1.vlansints:
                vlans.add(v1)
            logger.info(f'Getting Vlans on: {self.r2.hostname} - Starting')
            for v2 in self.r2.vlansints:
                vlans.add(v2)
            return vlans
        except Exception as e:
            logger.info(f'Getting Vlans on: {self.r2.hostname} - Failed')
            logger.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            logger.info(f'Getting Vlans on: {self.r2.hostname} - Success')
            return neighbors

    def get_all_downstream(self):
        logger.info(f'Collecting Router information for R1:{self.r1_ipaddress} R2:{self.r2_ipaddress} - STARTING')
        try:
            self.r1 = Router(self.r1_ipaddress)
            self.r1.login()
            self.r1.getSwitchInfo()
            self.r1.assignattributes()

            if self.r2_ipaddress:
                self.r2 = Router(self.r2_ipaddress)
                self.r2.login()
                self.r2.getSwitchInfo()
                self.r2.assignattributes()

            hostnamelist = set()
            # filter, and compile the devices downstream from the router
            for switch in self.r1.cdpneighbors:
                # Don't include the distro routers in this list
                test = any(x in switch.deviceid for x in cisco.distrobution_layer_list)
                if any(x in switch.deviceid for x in cisco.distrobution_layer_list):
                    continue
                # ignore the partner nodes
                if self.r1_ipaddress in switch.ip or self.r1.hostname in switch.deviceid:
                    continue
                if self.r2_ipaddress:
                    if self.r2_ipaddress in switch.ip or self.r2.hostname in switch.deviceid:
                        continue
                # special filter rules if this is the remote router
                if "r1-remote" in self.r1.hostname:
                    for funcdiscr in cisco.core_layer_function_descriptors:
                        if funcdiscr not in switch.deviceid.lower():
                            hostnamelist.add(switch.deviceid)
                else:
                    for funcdiscr in cisco.core_layer_function_descriptors:
                        if (funcdiscr not in switch.deviceid.lower()
                                or 'r1' not in switch.deviceid.lower() or 'r2' not in switch.deviceid.lower()):
                            hostnamelist.add(switch.deviceid)

            if self.r2_ipaddress:
                # filter through all the devices in r2
                for switch in self.r2.cdpneighbors:
                    # Don't include the distro routers in this list
                    if any(x in switch.deviceid for x in cisco.distrobution_layer_list):
                        continue
                    # ignore the partner nodes
                    if self.r1_ipaddress in switch.ip or self.r1.hostname in switch.deviceid:
                        continue
                    if self.r2_ipaddress:
                        if self.r2_ipaddress in switch.ip or self.r2.hostname in switch.deviceid:
                            continue
                    # special filter rules if this is the remote routers
                    if self.r2_ipaddress:
                        if "r2-remote" in self.r2.hostname:
                            for funcdiscr in cisco.core_layer_function_descriptors:
                                if funcdiscr not in switch.deviceid.lower():
                                    hostnamelist.add(switch.deviceid)
                        else:
                            for funcdiscr in cisco.core_layer_function_descriptors:
                                if (funcdiscr not in switch.deviceid.lower()
                                        or 'r1' not in switch.deviceid.lower() or 'r2' not in switch.deviceid.lower()):
                                    hostnamelist.add(switch.deviceid)
            set_list = set()
            # handles all
            if self.r2_ipaddress:
                if "r2-remote" in self.r2.hostname or 'r1-remote' in self.r1.hostname:
                    # pair the routers for the remote sites.
                    r1_list = []
                    r2_list = []
                    for deviceid in hostnamelist:
                        if 'r1' in deviceid.lower():
                            r1_list.append(deviceid)
                        elif 'r2' in deviceid.lower():
                            r2_list.append(deviceid)

                    paired_routers = []
                    for deviceid in r1_list:
                        r1_hostname = re.sub("r1-", "", deviceid)
                        for hostname_2 in r2_list:
                            r2_hostname = re.sub("r2-", "", hostname_2)
                            if r2_hostname == r1_hostname:
                                hostnamelist.remove(deviceid)
                                hostnamelist.remove(hostname_2)
                                paired_routers.append((deviceid, hostname_2))

                    # collect all the ip addresses for paired routers in remote locations
                    for hostnames in paired_routers:
                        pair = {}
                        r1_list.remove(hostnames[0])
                        r2_list.remove(hostnames[1])
                        for switch in self.r1.cdpneighbors:
                            if hostnames[0] == switch.deviceid:
                                pair['r1'] = switch
                            elif hostnames[1] == switch.deviceid:
                                pair['r2'] = switch
                        for switch in self.r2.cdpneighbors:
                            if hostnames[0] == switch.deviceid:
                                pair['r1'] = switch
                            elif hostnames[1] == switch.deviceid:
                                pair['r2'] = switch
                        node = Node(r1_ipaddress=pair['r1'].ip, r2_ipaddress=pair['r2'].ip)
                        node.get_all_downstream()
                        router_iplist = node.switchipaddresslist
                        set_list.update(router_iplist)

                    # collect all the single router ip's for r1
                    for deviceid in r1_list:
                        router = None
                        for switch in self.r1.cdpneighbors:
                            if deviceid == switch.deviceid:
                                router = switch
                        if self.r2_ipaddress:
                            for switch in self.r2.cdpneighbors:
                                if deviceid == switch.deviceid:
                                    router = switch
                        node = Node(r1_ipaddress=router.ip)
                        node.get_all_downstream()
                        router_iplist = node.switchipaddresslist
                        set_list.update(router_iplist)

            for switch in self.r1.cdpneighbors:
                if switch.deviceid in hostnamelist:
                    self.touchingdevices.append(switch)
                    hostnamelist.remove(switch.deviceid)

            if self.r2_ipaddress:
                for switch in self.r2.cdpneighbors:
                    if switch.deviceid in hostnamelist:
                        self.touchingdevices.append(switch)

            third_draft = set()
            for list in self.touchingdevices:
                third_draft.add(list.ip)

            switchipaddresslist = set()
            with ThreadPoolExecutor(max_workers=40) as executor:
                future_to_ip = {executor.submit(self.get_neibhors, switch.ip): switch for switch
                                in self.touchingdevices}

                for future in concurrent.futures.as_completed(future_to_ip):
                    ip = future_to_ip[future]
                    try:
                        # recieve iplist from self.get_neibhors thread
                        iplist = future.result()
                        filteriplist = set()
                        # filter through all the ips addresses and hostnames in response, and remove the routers
                        for ips in iplist:
                            if self.r1_ipaddress in ips[0] or self.r1.hostname in ips[1]:
                                continue
                            if self.r2_ipaddress:
                                if self.r2_ipaddress in ips[0] or self.r2.hostname in ips[1]:
                                    continue
                            filteriplist.add(ips[0])
                    except Exception as exc:
                        continue
                    else:
                        # remotes the distrobution layer from the ipaddresses pulled
                        new_set = switchipaddresslist.union(filteriplist)
                        switchipaddresslist = new_set

            extralist = set()
            if switchipaddresslist:
                # log into all the sx switches, and add any daisy chained devices to the list
                with ThreadPoolExecutor(max_workers=40) as executor:
                    future_to_ip = {executor.submit(self.get_neibhors, switch): switch for switch
                                    in switchipaddresslist}

                    for future in concurrent.futures.as_completed(future_to_ip):
                        ip = future_to_ip[future]
                        try:
                            iplist = future.result()
                            filteredips = set()
                            # don't add any previously discovered devices
                            for ips in iplist:
                                if ips[0] in switchipaddresslist:
                                    continue
                                if ips[0] in third_draft:
                                    continue
                                if self.r1_ipaddress in ips[0] or self.r1.hostname in ips[1]:
                                    continue
                                if self.r2_ipaddress:
                                    if self.r2_ipaddress in ips[0] or self.r2.hostname in ips[1]:
                                        continue
                                filteredips.add(ips[0])
                        except Exception as exc:
                            continue
                        else:
                            new_set = extralist.union(filteredips)
                            extralist = new_set

            extralist_2 = set()
            # log into all the sx switches, and add any daisy chained devices to the list
            if extralist:
                with ThreadPoolExecutor(max_workers=40) as executor:
                    future_to_ip = {executor.submit(self.get_neibhors, switch): switch for
                                    switch
                                    in extralist}

                    for future in concurrent.futures.as_completed(future_to_ip):
                        ip = future_to_ip[future]
                        try:
                            iplist = future.result()

                            # don't add any previously discovered devices
                            filteredips = set()
                            for ips in iplist:
                                if ips[0] in switchipaddresslist:
                                    continue
                                if ips[0] in third_draft:
                                    continue
                                if ips[0] in extralist:
                                    continue
                                filteredips.add(ips[0])
                        except Exception as exc:
                            continue
                        else:
                            new_set = extralist_2.union(filteredips)
                            extralist = new_set

            # combine all the lists of ips into one master list.
            draft_list = switchipaddresslist.union(extralist)
            second_draft = draft_list.union(extralist_2)
            final = second_draft.union(third_draft)
            acutal_final = final.union(set_list)
        except Exception as e:
            logger.info(f'Collecting Router information for R1:{self.r1_ipaddress} R2:{self.r2_ipaddress} - FAILED')
            logger.error(e, exc_info=True)
        else:
            logger.info(f'Collecting Router information for R1:{self.r1_ipaddress} R2:{self.r2_ipaddress} - Success')
            self.switchipaddresslist = acutal_final

    def _Get_ipaddress_list_thread(self):
        switchipaddresslist = set()
        # log into devices attached to the dx devices, and gather their attached devices
        with ThreadPoolExecutor(max_workers=40) as executor:
            future_to_ip = {executor.submit(self.get_neibhors, switch.ip): switch for switch
                            in self.touchingdevices}

            for future in concurrent.futures.as_completed(future_to_ip):
                ip = future_to_ip[future]
                try:
                    # recieve iplist from self.get_neibhors thread
                    iplist = future.result()
                    filteriplist = set()
                    # filter through all the ips addresses and hostnames in response, and remove the routers
                    for ips in iplist:
                        if self.r1_ipaddress in ips[0] or self.r1.deviceid in ips[1]:
                            continue
                        if self.r2_ipaddress:
                            if self.r2_ipaddress in ips[0] or self.r2.deviceid in ips[1]:
                                continue
                        filteriplist.add(ips[0])
                except Exception as exc:
                    continue
                else:
                    # remotes the distrobution layer from the ipaddresses pulled
                    new_set = switchipaddresslist.union(filteriplist)
                    switchipaddresslist = new_set
        pass

    def check_egde_acl(self):
        """
        Takes all the IP addresses in self.switchipaddresslist, logs into the device, creates a switch object for them
        gathers the ACL lists, creates an object for them, and checks the list of ACL against the standards
        """
        logger.info(f'Collecting Edge ACL - Starting')
        try:
            for ip in self.switchipaddresslist:
                logger.debug(f'Gettting Edge Device: {ip} - Starting')
                try:
                    s = Switch(ip)
                    s.login()
                    s.getSwitchInfo()
                    s.assignattributes()
                    s.sort_acl()
                except Exception as e:
                    logger.info(f'Gettting Edge Device: {ip} - Failed')
                    logger.error(e, exc_info=True)
                else:
                    logger.debug(f'Gettting Edge Device: {ip} - Starting')

        except Exception as e:
            logger.info(f'Collecting Edge ACL - FAILED')
            logger.error(e, exc_info=True)
        else:
            logger.info(f'Collecting Edge ACL - Success')

    def get_switch_adjecent_negibhors(self):
        """
        This function is for threading the gathering of devices on the network.
        :return (set): A List of neighbor objects
        """

        try:
            logger.info(f'Getting All Switches_syntax_compatability Touching: {self.r1.hostname} - Starting')
            neighbors = set()
            for neighbor in self.r1.cdpneighbors:
                neighbors.add(neighbor)
            logger.info(f'Getting All Switches_syntax_compatability Touching: {self.r2.hostname} - Starting')
            for neighbor in self.r2.cdpneighbors:
                neighbors.add(neighbor)

        except Exception as e:
            logger.info(f'Getting All Switches_syntax_compatability Touching: {self.r1.hostname} - Failed')
            logger.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            logger.info(f'Getting All Switches_syntax_compatability Touching: {self.r1.hostname} - Success')
            return neighbors

    def get_neibhors(self, ip):
        """
        This function is for threading the gathering of devices on the network.
        :return (set): A List of IP addresses
        """
        logger.info(f'Getting Edge Device: {ip} - Starting')
        try:
            switchipaddresslist = set()
            ip = re.sub('\r', '', ip)
            ip = re.sub(' ', '', ip)
            s = Switch(ip)
            s.login()
            s.cdpnei_result = s.send_command('show cdp nei detail')
            s.sortCdpNeiDetail(s.cdpnei_result)
            # filter through the attached devices
            for switch2 in s.cdpneighbors:
                # remove the node types if present
                if 'r1-remote' in switch2.hostname or 'r2-remote' in switch2.hostname:
                    continue
                # filter out any distrobution routers
                if any(x in switch2.hostname for x in cisco.distrobution_layer_list):
                    continue
                if 'ap' in switch2.hostname:
                    continue
                if any(x in switch2.hostname for x in cisco.access_layer_function_descriptors):
                    switchipaddresslist.add((switch2.ip, switch2.hostname))
                if any(x in switch2.hostname for x in cisco.distrobution_layer_descriptors):
                    switchipaddresslist.add((switch2.ip, switch2.hostname))
        except Exception as e:
            logger.info(f'Getting Edge Device: {ip} - Failed')
            logger.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            logger.debug(f'Getting Edge Device: {ip} - Starting')
            return switchipaddresslist

    def get_mgmt_vlans(self):
        try:
            r = Router(self.r1_ipaddress)
            r.login()
            output = r.conn.send_command("show cdp neighbors detail")
            parsed_output = []
            index = -1
            for line in output.split('\r\n'):
                strip_line = line.strip()
                if strip_line == "":
                    print("empty")
                elif "------------" in line:
                    index += 1
                    parsed_output.append([])
                else:
                    parsed_output[index].append(strip_line)
            for section in parsed_output:
                bldg_num = 0
                for i in range(len(section)):
                    if "Device ID:" in section[i]:
                        pass
                    if "Mgmt address(es):" in section[i]:
                        pass


        except Exception as e:
            pass
        else:
            pass

    def _update_single_switch_acl(self,ip):
        """
        logs into a single edge device to update the acl to reflect what is in settings
        Args:
            ip (str): An ip of the edge device
        Returns:
        """
        s = Switch(ip)
        s.getSwitchInfo()
        s.assignattributes()
        s.check_ACL()
        s.update_ACL()

    def Update_all_edge_ACLS(self):
        """
        Will select onl the Edge devices under this routing node, and update the ACLS to what is listed in settings
        Returns:
        """
        for ip in self.switchipaddresslist:
            self._update_single_switch_acl(ip)

class Network():
    def __init__(self):
        pass

    def Get_All_devices(self):
        for distnode in cisco.distrobution_layer_ip:
            n = Node(r1_ipaddress=distnode[0], r2_ipaddress=distnode[1])
            n.get_all_downstream()
            from concurrent.futures import ThreadPoolExecutor
            import concurrent.futures
            try:
                batch = []
                logger.debug(f"new Thread Pool - Starting")
                with ThreadPoolExecutor(max_workers=8) as executor:
                    for ipaddress in n.switchipaddresslist:
                        logger.debug(f"New Thread - Starting")
                        future_to_ipaddress = {executor.submit(interfaceupdatetask, ipaddress): ipaddress}
                    for future in concurrent.futures.as_completed(future_to_ipaddress):
                        ipaddress = future_to_ipaddress[future]
                        try:
                            data = future.result()
                            if data:
                                batch.append(data)
                        except Exception as e:
                            logger.error(e, exc_info=True)

                logger.debug(f"new Thread Pool - closed")
            except Exception as e:
                logger.error(e, exc_info=True)
            else:
                pass
