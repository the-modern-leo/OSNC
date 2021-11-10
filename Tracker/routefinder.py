from future import standard_library
standard_library.install_aliases()
from builtins import str
from builtins import range
from past.builtins import basestring
from builtins import object
from netaddr import IPNetwork, IPAddress
from collections import namedtuple
import time, re, logging, threading, traceback, copy, socket
from common import database
from routefinder.db import DBRouter, DBUnmanagedRouter

from routefinder import settings

Route = namedtuple('Route', ['ip', 'vrf', 'interface', 'nodename', 'config',
        'ip2', 'config2', 'mac', 'current_ip'])
Route.__new__.__defaults__ = (None, None, None, None, None, None, None, None,
        None)

class RouteFinder(object):
    """
    Routefinder script ported to python. This takes an IP/subnet, and
    traverses core routers to find the L3 VLAN (or firewall) the subnet is
    routed from.

    Args:
        switchaccess (SwitchAccess): SwitchAccess object used to log in to
                switches.
        acitools (ACITools): ACITools object to look up ACI routes. May be None
                if ACI is not available.
        default_router (str): Default (core) router to start searches from.
    """
    def __init__(self, switchaccess, default_router, acitools=None):
        self.switchaccess = switchaccess # SwitchAccess object to call
        self.acitools = acitools # optional ACITools object
        self._default_router = default_router
        self.threads = {}
        self.lock = threading.Lock()

    class RouteFinderParseException(Exception):
        """
        This exception is raised when the RouteFinder class encounters another
        error parsing data from the routers.
        """
        pass

    class RouteFinderIPException(Exception):
        """
        This exception is raised when the IP or subnet given is invalid.
        """
        pass

    class RouteFinderTimeoutException(Exception):
        """
        This exception is raised when a connection timeout to a router or hop
        occurs.
        """
        pass

    class RouteFinderNotRoutedException(Exception):
        """
        This exception is raised when a route points nowhere (0.0.0.0/0).
        """
        pass

    def _parse_cisco_route(self, output):
        """
        Parse Cisco IOS/IOS-XE 'show ip route' outputs, for the next hop
        (if indirect) or VLAN/Firewall (if direct).

        Args:
            output (str): Output of a Cisco router

        Returns:
            Route: A named tuple describing the next hop IP or local VLAN ID.

        Raises:
            RouteFinderNotRoutedException: When the line cannot be found
        """
        def _get_line_c6500(output):
            for index, line in enumerate(output):
                if "Routing Descriptor" in line:
                    return output[index + 1].replace('*', '')

        data = _get_line_c6500(output.replace(',', '').splitlines())

        if not data:
            raise self.RouteFinderNotRoutedException('Route not found on router')

        nexthop = re.sub('\s+', ' ', data).split(' ')
        if "directly" in nexthop:
            return Route(interface=nexthop[-1])
        else:
            return Route(nexthop[1])

    def _parse_nexus_route(self, output):
        """
        Parse Cisco N7K 'show ip route' outputs, for the next hop (if
        indirect) or VLAN/Firewall (if direct).

        Args:
            output (str): Output of a Cisco router

        Returns:
            Route: A named tuple describing the next hop IP or local VLAN ID.

        Raises:
            RouteFinderNotRoutedException: When the subnet is not routed
        """
        try:
            try:
                zr = [s for s in
                    output.replace(',','').splitlines() if "ubest" in s]
                if "0.0.0.0/0" in zr[0].split(' ')[0]:
                    raise self.RouteFinderNotRoutedException("points to 0.0.0.0/0")
            except IndexError:
                pass

            data=[s for s in output.replace(',','').splitlines() if "*via" in s]

            if not data: #older router, try parsing a different way
                return self._parse_cisco_route(output)

            nexthop = re.sub('\s+', ' ', data[0]).split(' ')

            if any(s in nexthop[-1] for s in ['direct', 'am', 'local', 'hsrp']):
                ip_index = 2
                if '[' in nexthop[3]: # this is the metric, not the interface!
                    ip_index = 1
                return Route(nexthop[ip_index].split('%', 1)[0],
                        interface=nexthop[ip_index + 1])
            else:
                return Route(nexthop[2].split('%', 1)[0])
        except (ValueError, IndexError) as e:
            traceback.print_exc()
            logging.info("data: " + str(output))
            #raise RouteFinderParseException(str(e))
            raise # debug only TODO

    def _check_vrf(self, ip):
        """
        Check a router/firewall IP, and change the VRF instance if needed.

        Args:
            ip (str): IP address of the firewall/next hop

        Returns:
            str or None: A new VRF string; None if no change is needed.
        """
        return (settings.IP_VRF[ip] if ip in settings.IP_VRF else None)

    def check_unmanaged(self, ip):
        """
        Check a router/firewall IP for an unmanaged device.

        Args:
            ip (str): IP address of the firewall/next hop

        Returns:
            str or None: A message string if the IP is in the unmanaged devices
            list in cisco.py; otherwise None
        """
        with database.db_session() as dbsession:
            result = dbsession.query(DBUnmanagedRouter).filter(
                    DBUnmanagedRouter.ipaddress == ip).first()
            if result:
                return result.message

    def get_dev_info(self):
        """
        Returns the status of the module

        Returns:
            str: the status of the module
        """
        return "Production"

    def get_routers(self):
        """
        Get a list of routers known by the module.

        Returns:
            dict: A dictionary of tuples with the router IP as a key, name, and
            backup name as the tuple value
        """
        with database.db_session() as dbsession:
            routerlist = dbsession.query(DBRouter).all()
            return {r.ipaddress: (r.routername, r.secondaryname)
                    for r in routerlist}

    def get_unmanaged(self):
        """
        Get a list of unmanaged devices known by the module.

        Returns:
            dict: A dictionary of unmanaged router IPs and descriptions.
        """
        with database.db_session() as dbsession:
            umlist = dbsession.query(DBUnmanagedRouter).all()
            return {u.ipaddress: u.message for u in umlist}

    def add_or_modify_router(self, ip, name, backup=None):
        """
        Modify a router entry if it exists, or add a new router entry.

        Args:
            ip (str): IP address of the router
            name (str): Name of the router
            backup (str): Optional - backup router name

        Raises:
            ValueError: if there was a problem inserting the new entry.
        """
        if not ip or not name:
            raise ValueError("IP or router name was not given")

        with database.db_session() as dbsession:
            existingum = dbsession.query(DBUnmanagedRouter).filter(
                    DBUnmanagedRouter.ipaddress == ip).one_or_none()
            if existingum:
                # can't add a router if it is also an unmanaged device
                raise ValueError(str(ip) + " is already an umanaged device")

            existingrouter = dbsession.query(DBRouter).filter(
                    DBRouter.ipaddress == ip)

            if existingrouter.one_or_none():
                updatedict = {'routername': name}
                if backup:
                    updatedict['secondaryname'] = backup

                existingrouter.update(updatedict)
            else:
                dbsession.add((DBRouter(ipaddress=ip, routername=name,
                        secondaryname=backup) if backup
                        else DBRouter(ipaddress=ip, routername=name)))

    def delete_router(self, ip):
        """
        Delete a router entry from the database.

        Args:
            ip (str): IP address of the router to delete.

        Raises:
            ValueError: When the router does not exist
        """
        if not ip:
            raise ValueError("IP was not given")

        with database.db_session() as dbsession:
            existing = dbsession.query(DBRouter).filter(
                    DBRouter.ipaddress == ip).one_or_none()
            if not existing:
                raise ValueError("Router does not exist")
            dbsession.delete(existing)

    def add_or_modify_unmanaged(self, ip, message):
        """
        Modify an unmanaged device entry, or add a new entry if it doesn't
        exist.

        Args:
            ip (str): IP address of the device
            message (str): Message or description of the device

        Raises:
            ValueError: if there was a problem inserting the new entry.
        """
        if not ip or not message:
            raise ValueError("IP or message was not given")

        with database.db_session() as dbsession:
            existingrouter = dbsession.query(DBRouter).filter(
                    DBRouter.ipaddress == ip).one_or_none()
            if existingrouter:
                # can't add an unmanaged device if it is also a router
                raise ValueError(str(ip) + " is already a router")

            existingum = dbsession.query(DBUnmanagedRouter).filter(
                    DBUnmanagedRouter.ipaddress == ip)
            if existingum.one_or_none():
                existingum.update({'message': message})
            else:
                dbsession.add(DBUnmanagedRouter(ipaddress=ip, message=message))

    def delete_unmanaged(self, ip):
        """
        Delete an unmanaged device entry from the database.

        Args:
            ip (str): IP address of the device to delete.

        Raises:
            ValueError: When the requested IP is not in the list
        """
        if not ip:
            raise ValueError("IP was not given")

        with database.db_session() as dbsession:
            existing = dbsession.query(DBUnmanagedRouter).filter(
                    DBUnmanagedRouter.ipaddress == ip).one_or_none()
            if not existing:
                raise ValueError("Unmanaged device does not exist")
            dbsession.delete(existing)

    def get_defaults(self):
        """
        Get default router and VRF.

        Returns:
            list: A list of the default router and default VRF as strings.
        """
        return [self._default_router, settings.DEFAULT_VRF]

    def get_routername(self, router):
        """
        Look up a router name.

        Args:
            router (str): Router as an IP

        Returns:
            str: A router name if available, otherwise an empty string.
        """
        with database.db_session() as dbsession:
            result = dbsession.query(DBRouter).filter(
                    DBRouter.ipaddress == router).one_or_none()
            return result.routername if result else ""

    def get_backuprouter(self, router):
        """
        Look up the backup router IP for the given router

        Args:
            router (str): Router as an IP

        Returns:
            str: The backup router as an IP string if available
        """
        with database.db_session() as dbsession:
            result = dbsession.query(DBRouter).filter(
                    DBRouter.ipaddress == router).one_or_none()
            if result:
                result = dbsession.query(DBRouter).filter(
                        DBRouter.routername==result.secondaryname).first()
                return result.ipaddress if result else ""
            return ""

    def get_secondary_config(self, router, interface, result):
        """
        Get the interface config from the secondary/backup router.

        Note that this does not return a value - it instead modifies the
        result parameter as an array so this can be used in a thread.

        Args:
            router (str): Primary router IP
            interface (str): SVI ID to retrieve the config for
            result (str): String that is modified with the config result.

        Raises:
            RouteFinderTimeoutException: When the connection times out
        """
        connection = None
        router = self.get_backuprouter(router)
        if not router:
            result[0] = None
            return

        try:
            connection, output = self.switchaccess.login_and_run(router,
                    ("show runn interface " + interface))

            result[0] = output
            result[1] = router
        except Exception as e:
            if "timed out" in str(e):
                raise self.RouteFinderTimeoutException(router + " timed out")
            traceback.print_exc()
            result[0] = None
        finally:
            if connection: # close SSH connection
                self.switchaccess.logout(connection)

    def get_junos_route(self, ip, junos_router, vrf, config=False):
        """
        Attempt to read a route from JunOS firewalls or routers.

        Args:
            ip (str): IP/subnet to search for
            junos_router (str): JunOS router as an FQDN or IP.
            vrf (str): VRF name
            config (bool): Optional - if True also retrieve the config.

        Returns:
            str: An error message if unsuccessful, a Route namedtuple otherwise.
        """
        connection = None
        try:
            connection, output = self.switchaccess.login_and_run(junos_router,
                    "show route " + str(ip) + ' | match "(Direct|reth)"')
            if "Direct" not in output:
                logging.warn(output)
                return ("Route points to JunOS firewall " + str(junos_router) +
                        " but was not found in config")

            output = output.splitlines()
            iface = output[1].split()[-1]
            name =connection.send_command('show version brief | match Hostname')
            name = name.splitlines()[0].split(': ')[-1]
            junos_config = None
            if config:
                junos_config = connection.send_command('show configuration ' +
                        'interfaces ' + iface)
            mac = connection.send_command('show arp hostname ' + ip +
                    ' | match reth')
            mac = mac.splitlines()
            if mac[0]:
                mac = mac[0].split()[0]
            else:
                mac = "No Associated MAC"
            return Route(junos_router, vrf, iface, name, junos_config, None,
                    None, mac)
        except Exception as e:
            traceback.print_exc()
            return "JunOS error reading " + str(junos_router) + ": " + str(e)
        finally:
            if connection:
                self.switchaccess.logout(connection)

    def getnexthop(self, ip, router, vrf=None, config=False):
        """
        Discover the next route hop for the IP from the given router.

        This is a generator, which means this should be called repeatedly until
        an error or end result (actual router) is reached.

        Args:
            ip (str): IP address or CIDR subnet of the route destination to
            check
            router (str): Router to check the route for.
            vrf (str): Optional - string describing the VRF to check.
            config (bool): Optional - if True, retrieve the SVI config as well.

        Returns:
            str or Route: retruns a message if not able to find results; returns
            the found results in a Route named tuple

        Raises:
            RouteFinderIPException: When the router/ IP is invalid
            RouteFinderNotRoutedException: When the subnet route is not found
            RouteFinderTimeoutException: When the connection times out
        """
        if not vrf:
            vrf=settings.DEFAULT_VRF
        connection = None
        newvrf = None

        # strip whitespace from IP
        ip = ip.replace(' ', '')

        try: # test IPs
            ip = str(IPNetwork(ip).ip)
        except Exception:
            raise self.RouteFinderIPException("invalid host/router IP")

        unmanaged = self.check_unmanaged(router)
        if unmanaged: # Unmanaged device, give up and don't log in
            return "Unreachable router " + router + ": " + unmanaged
        elif router in settings.DDC_ACI_NEXTHOPS:
            # ACI-routed subnet, return with the correct response
            return "DDC ACI Subnet"
        elif not self.get_routername(router) and router != self._default_router:
            return "Router " + router + " not in router table/whitelist"

        try:
            connection, output = self.switchaccess.login_and_run(router,
                    ("show ip route" + ((" vrf "+vrf) if vrf else "") +" "+ ip))

            parsed = self._parse_nexus_route(output)

            if not parsed.ip: # parse_cisco does not provide an ip
                parsed = Route(router, parsed.vrf, parsed.interface)

            newvrf = self._check_vrf(parsed.ip)
            unmanaged = self.check_unmanaged(parsed.ip)
            if vrf == 'all' or (parsed.ip and parsed.ip in settings.VRF_UNTRUST):
                # VRFs routed behind firewalls
                output = connection.send_command("show vrf | exclude VRF-ID")
                vrflist = [v.split()[0] for v in output.splitlines()
                        if v.split()[0] not in ['default', 'management',
                        'keepalive']]
                oldvrf = vrf
                for v in vrflist:
                    if v == vrf:
                        continue # skip the vrf we are already in
                    try:
                        output = connection.send_command("show ip route vrf " +
                                v + " " + ip)
                        if 'intra' in output: # special fix for CSBS VRFs - keep
                            continue          # checking other VRFs since some
                                              # external routes != default route

                        parsed = self._parse_nexus_route(output)
                        vrf = v
                        break    # non-default route was found - stop checking
                    except self.RouteFinderNotRoutedException:
                        continue # route not found in vrf - check the next one
                if vrf == oldvrf and parsed.ip in settings.VRF_UNTRUST:
                    # points back to the default route - must be on firewall
                    if unmanaged: # check unmanaged devices just in case
                        return ("Unreachable router " + parsed.ip + ": " +
                                unmanaged)
                    # TODO: Enable this tool to search palo-alto firwalls for
                    # Layer 3 configurations anddisplay them in Cisco style.
                    # Then this chck can be removed
                    if parsed.ip == "10.64.32.229":
                        return ("Requested IP/subnet routed on fw-ddc-colo_" +
                                "untrust.net.utah.edu (10.64.32.229).")
                    return Route(parsed.ip, vrf, None, 'junos')
            elif unmanaged: # Unmanaged device, give up and don't log in
                return "Unreachable router " + parsed.ip + ": " + unmanaged
            elif newvrf: # VRF check
                # check VRF'd route before logging out
                output = connection.send_command("show ip route vrf " + newvrf +
                        " " + ip)
                vrf = newvrf
                parsed = self._parse_nexus_route(output)

            if vrf:
                parsed = parsed._replace(vrf=vrf)
            parsed = parsed._replace(mac=self.find_mac(connection,
                                        ip, parsed.vrf))
            # check for static route, and change if needed
            if parsed.ip in settings.STATIC_ROUTES:
                return Route(settings.STATIC_ROUTES[parsed.ip], parsed.vrf,
                             parsed.interface, None, mac=parsed.mac)

            # also print config, if direct route
            if config and parsed.interface:
                res = [None, None]
                # threading: run both config grabbers in parallel to avoid wait
                backup = threading.Thread(target=self.get_secondary_config,
                        args=(router, parsed.interface, res),
                        name="routefinder.GetSecondaryConfig")
                backup.start()

                output = connection.send_command("show runn interface " +
                        parsed.interface)
                backup.join() # get data from backup config thread
                return Route(parsed.ip, parsed.vrf, interface=parsed.interface,
                        nodename=parsed.nodename, config=output,
                        ip2=(res[1] if res[0] else None), config2=res[0],
                        mac=parsed.mac)
            else:
                return parsed
        except self.RouteFinderNotRoutedException as e:
            if newvrf and "CLINICAL" in newvrf: #pylint: disable=unsupported-membership-test
                # check the CLINICAL-PCI-1 vrf instead
                return self.getnexthop(ip, router, vrf="CLINICAL-PCI-1",
                        config=config)
            else:
                raise
        except Exception as e:
            # raise some errors - add as appropriate
            if "timed out" in str(e) or "timeout" in str(e):
                try: # do the nslookup
                    router = socket.gethostbyaddr(router)[0]
                except:
                    pass
                raise self.RouteFinderTimeoutException(router + " timed out")
            traceback.print_exc()
            raise
        finally:
            if connection: # close SSH connection
                self.switchaccess.logout(connection)

    def find_mac(self, connection, ip, vrf=None):
        """
        This function uses the ARP table from the router to find what
        MAC address is tied to the IP, if any

        Args:
            connection (Connection): Network connection to the router
            ip (str): the IP of the device to get the mac of
            vrf (str): Optional - the vrf of the vlan, if any
        Returns:
            str: the mac associated to the IP, or 'No Associated MAC'
        """
        try:
            if vrf is None:
                output = connection.send_command("show ip arp " + ip +
                        " | include " + ip)
            else:
                output = connection.send_command("show ip arp " + ip + " vrf " +
                        vrf + " | include " + ip)
                if 'invalid input' in output.lower():
                    output = connection.send_command("show ip arp vrf " + vrf +
                            " " + ip + " | include " + ip)
            mac_ad = "No Associated MAC"
            mac_pattern = re.compile(
                    "([a-f]|\d){4}\.([a-f]|\d){4}\.([a-f]|\d){4}")
            if len(output) > 1:
                mac_ad = mac_pattern.search(output).group(0)
            return mac_ad
        except:         # errors should not be fatal
            return "No Associated MAC"

    def findroute(self, ip, config=False, synchronous=True):
        """
        Find route of a given IP or subnet.

        This is a blocking function that will produce a routing result, but
        will give no progress.

        Args:
            ip (str): IP address or subnet to check.
            config (bool): Optional - if True, retrieve the config as well.
            synchronous (bool): Optional - If True, run synchronously (wait for
                    thread to finish).

        Returns:
            Route or int: A named tuple with relevant information added if
            synchronous=True; otherwise this will return a thread ID to
            reference with get_thread().

        Raises:
            ValueError: When the IP address is invalid
        """
        try:
            IPNetwork(ip)
        except:
            raise ValueError("Invalid IP address")

        thread_id = int(round(time.time() * 1000))
        time.sleep(0.001); # guarantee thread_id won't be reused
        thread = FindRouteThread(thread_id, self, ip, config)
        thread.start()
        if synchronous:
            thread.join()
            return self.get_thread(thread_id)
        else:
            return thread_id

    def get_thread(self, thread_id, autodelete=True):
        """
        Get information/output for a running or recently-completed
        routefinding thread.

        Args:
            thread_id (int): Thread ID
            autodelete (bool): Optional - If True, this will delete thread
                    information if the thread/route finding has been completed.

        Returns:
            dict: containing the route message and a Route namedtuple.

        Raises:
            ValueError: When the threadID is invalid
        """
        self.lock.acquire()
        try:
            if thread_id not in list(self.threads.keys()):
                raise ValueError("Invalid Thread ID " + str(thread_id))
            thread_dict = self.threads[thread_id]
            if autodelete and thread_dict['message'] is None:
                # thread is done, delete
                del self.threads[thread_id]
            return thread_dict
        finally:
            self.lock.release()

    def _update(self, thread_id, message, route):
        """
        Internal function - update a routefinding thread with information
        from the thread.

        Args:
            thread_id (int): the ID of the thread
            message (str): message to store
            route (Route): the named tuple to store
        """
        self.lock.acquire()
        self.threads[thread_id] = {"message": message, "route": route}
        self.lock.release()

    def get_firewall_path(self, src_vrf, src_name, dst_vrf, dst_name,
            dst_config):
        """
        Determine firewalls or ACLs in between a source and destination VRF.

        Args:
            src_vrf (str): Source VRF
            src_name (str): Source Router name
            dst_vrf (str): Destination VRF
            dst_name (str): Destination Router name
            dst_config (str): Destination VLAN configuration

        Returns:
            tuple: A tuple containing a list of firewalls (in order from source
            to destination) and a boolean for the destination ACL.
        """
        firewalls = [] # in order, from source to destination
        # FIXME make this more accurate
        has_acl = ('access-group' in dst_config and 'out' in dst_config)

        if src_vrf == dst_vrf:
            if (src_name is not None and src_name == dst_name
                    and src_name.startswith('fw')):
                return ([str(src_name) + ' (Trust to Trust)'], has_acl)
            else:
                return ([], has_acl)

        if src_vrf:
            src_vrf = src_vrf.lower().replace('_', '-')
            if src_vrf in list(settings.VRF_FIREWALL.keys()):
                # exact VRF found in VRF_FIREWALL
                if settings.VRF_FIREWALL[src_vrf]:
                    # don't add a blank VRF - this means there's no firewall
                    firewalls.extend(list(reversed(
                            settings.VRF_FIREWALL[src_vrf])))
            elif any(v in src_vrf for v in list(settings.VRF_FIREWALL.keys())):
                # there is a VRF in VRF_FIREWALL that is in this VRF name
                key = [v for v in settings.VRF_FIREWALL if v in src_vrf][0]
                firewalls.extend(list(reversed(settings.VRF_FIREWALL[key])))
            else:
                raise ValueError("Unknown firewall for source VRF " +
                        str(src_vrf))
            if src_name is not None and src_name.startswith('fw'):
                # routed directly on the firewall, add it to the firewall list
                firewalls.insert(0, src_name)

        if dst_vrf:
            dst_vrf = dst_vrf.lower().replace('_', '-')
            if dst_vrf in list(settings.VRF_FIREWALL.keys()):
                firewalls.extend(settings.VRF_FIREWALL[dst_vrf])
            elif any(v in dst_vrf for v in list(settings.VRF_FIREWALL.keys())):
                key = [v for v in settings.VRF_FIREWALL if v in dst_vrf][0]
                firewalls.extend(settings.VRF_FIREWALL[key])
            else:
                raise ValueError("Unknown firewall for destination VRF " +
                        str(dst_vrf))
            if dst_name is not None and dst_name.startswith('fw'):
                # routed directly on the firewall, add it to the firewall list
                firewalls.append(dst_name)

        # remove duplicate/common firewalls
        old_firewalls = copy.copy(firewalls)
        for fw in firewalls:
            if firewalls.count(fw) > 1:
                for i in range(0, firewalls.count(fw)):
                    firewalls.remove(fw)

        if old_firewalls and not firewalls:
            # if VRFs are different but there's no different FWs, there are
            # multiple VRFs terminated on the closest firewall to the src/dest
            firewalls = [old_firewalls[0]]
        return (firewalls, has_acl)

class FindRouteThread(threading.Thread):
    """
    Route finding thread. This manages next hop finding while the RouteFinder
    object traverses the network.

    Args:
        thread_id (int): the ID of the thread
        rf (RouteFinder): The RouteFinder object
        ip (str): the IP to search
        get_config (bool): Optional - Whether or not to get the advanced config
    """

    def __init__(self, thread_id, rf, ip, get_config=False):
        super(FindRouteThread, self).__init__()
        self._kill = threading.Event()
        self.ID = thread_id
        self.rf = rf
        self.ip = ip
        self.config = get_config
        self.name = "routefinder.FindRoute"

    def run(self):
        """
        Search for the routed path of this subnet on the network using the
        RouteFinder object in a separate thread
        """
        old_router = None
        router = self.rf.get_defaults()[0]
        vrf = self.rf.get_defaults()[1]
        nexthop_junos = False
        while True:
            message = "Checking " + router + ", vrf " + str(vrf) + "..."
            self.rf._update(self.ID, message, None)

            try:
                if nexthop_junos:
                    route = self.rf.get_junos_route(self.ip, router, vrf,
                            self.config)
                else:
                    route = self.rf.getnexthop(self.ip, router, vrf,self.config)
            except self.rf.RouteFinderNotRoutedException as e:
                # no traceback messages for default routes
                self.rf._update(self.ID, None, str(e))
                break
            except Exception as e: # Error
                traceback.print_exc() # debug
                self.rf._update(self.ID, None, str(e))
                break

            if isinstance(route, basestring): # error or message
                if 'DDC ACI' in route and self.rf.acitools is not None:
                    # if the ACI is available, check that system first
                    self.rf._update(self.ID, "Checking ACI...", None)
                    apic = self.rf.acitools.create_connection("DDC")
                    aci_result = self.rf.acitools.find_subnet(
                            IPNetwork(self.ip), apic, True)
                    if not aci_result: # Traced to ACI, but not routed here
                        # Check non-routed stuff first (shutdown BDs)
                        aci_result = self.rf.acitools.find_subnet(
                                IPNetwork(self.ip), apic)
                        if not aci_result:
                            logging.error("Traced to ACI, but not found: " +
                                    str(self.ip))
                            self.rf._update(self.ID, None,
                                    "Routed in ACI, unknown interface (L3Out?)")
                            break
                        # routed on the Nexus 7K, but behind the DDC firewall
                        router = old_router
                        vrf = 'all'
                        continue
                    aci_result = aci_result[0] # TODO only first result for now

                    # get more information about the BD if config is requested
                    aci_config = None
                    if self.config:
                        if type(aci_result).__name__ == 'SubnetInfo':
                            # get BD information from any (the first) epg
                            epginfo = self.rf.acitools.get_epg_info(apic,
                                    aci_result.epgs[0].dn.split("/")[1][3:],
                                    aci_result.epgs[0].dn.split("/")[2][3:],
                                    aci_result.epgs[0].dn.split("/")[3][4:])
                            subnetlist = epginfo['subnets']
                            aci_config = ('BD: ' + epginfo['bd']['name'] +
                                    '\n\nContext/VRF: ' +
                                    epginfo['context']['name']+
                                    '\n\nEPGs:\n' +
                                    '\n'.join(epg.dn for epg in aci_result.epgs)
                                    + '\n\nSubnets:\n' +
                                    '\n'.join(sub['ip'] for sub in subnetlist)+
                                    '\n\nDHCP Relays: ' +
                                    ', '.join(epginfo['bd']['relays']))
                        elif type(aci_result).__name__ == 'L3OutInfo':
                            aci_config = ('Context/VRF: ' + aci_result.context +
                                    '\n\nName: ' + aci_result.name)

                    interface = 'unknown'
                    if_name = 'unknown'
                    if type(aci_result).__name__ == 'SubnetInfo':
                        interface = aci_result.bd.dn
                        if_name = f"{aci_result.bd.dn.split('/')[1][3:]} Tenant"
                    elif type(aci_result).__name__ == 'L3OutInfo':
                        interface = aci_result.name
                        if_name = aci_result.dn.split('/')[1][3:] + " Tenant"

                    self.rf._update(self.ID, None, {
                            "ip": "ACI",
                            "vrf": aci_result.context,
                            "interface": interface,
                            "name": if_name,
                            "config": aci_config,
                            "ip2": None, "name2": None, "config2": None,
                            "current_ip": self.ip})
                elif "whitelist" in route:
                    logging.error('non-whitelisted ip ' + str(router) +
                            ': for ' + str(self.ip))
                    self.rf._update(self.ID, None, route)
                elif "hosts" in route:
                    logging.error('missing entry in known_hosts ' + str(router)+
                            ': for ' + str(self.ip))
                    self.rf._update(self.ID, None, route)
                else:
                    self.rf._update(self.ID, None, route)
                break
            elif not route.interface: # indirect route, keep checking
                old_router = router
                router = route.ip
                vrf = route.vrf
                # check for JunOS firewall
                if route.nodename and 'junos' in route.nodename:
                    nexthop_junos = True
            else:  # success!
                self.rf._update(self.ID, None, {
                        "ip": route.ip, "vrf": route.vrf,
                        "interface": route.interface,
                        "name": self.rf.get_routername(router),
                        "config": route.config,
                        "ip2": route.ip2,
                        "name2": self.rf.get_routername(route.ip2),
                        "config2": route.config2,
                        "mac": route.mac,
                        "current_ip": self.ip})
                break
