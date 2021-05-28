from __future__ import print_function
from builtins import range
from builtins import object
import re, traceback, threading, time, logging, copy
import sys
from collections import namedtuple

MacLocation = namedtuple('MacLocation', ['switchname', 'switchip', 'port',
        'message', 'simple_config', 'config', 'current_ip'])

class WrongRouterException(Exception):
    pass

class MacFinder(object):
    """
    Searches for the switch and port location, along with the port's
    configuration for a MAC address.

    Args:
        switchaccess (SwitchAccess): Login and run iOS commands on a switch.
        acitools (ACITools): Application Centric Infastructure (cisco)
    """
    def __init__(self, switchaccess, acitools):
        self.switchaccess = switchaccess
        self.ip_pattern = re.compile("\\b((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]"
                "?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\b")
        self.routerlist = switchaccess.get_routerlist()['nexus']
        self.routerlist.extend(switchaccess.get_routerlist()['ios'])
        # remove secondary routers
        self.routerlist = [r for r in self.routerlist
                if r.startswith('r1-') or r.startswith('ddr1-') or
                'r2-remote' in r]
        self.acitools = acitools # leave this alone, needed to be a placeholder
        self.threads = {}
        self.thread_connections = {} # rarely used
        self.lock = threading.Lock()

    def get_dev_info(self):
        """
        Gets production information.

        Returns:
            str: Returns "Dev"
        """
        return "Dev"

    def parse_mac(self, mac):
        """
        Takes in a mac address and converts it to Cisco Style formatting.
        Throws a SyntaxError if the mac is not 12 characters without formatting.

        Args:
            mac (str): The MAC address to format.

        Returns:
            str: mac formatted Cisco style.
        """
        mac = mac.lower()
        # Strips everything but the hexadecimal characters.
        if mac == "no associated mac":
            raise SyntaxError("No associated MAC address found")
        mac = ''.join(char for char in mac if char in 'abcdef0123456789')
        if len(mac) != 12:
            raise SyntaxError('MAC Address needs to be 12 characters')
        # Places periods between every 4 characters.
        mac = '.'.join(mac[i:i+4] for i in range(0, len(mac), 4))
        return mac

    def search_switch(self, mac, switch, device_ip, keep_connection=None):
        """
        Search down switch links until it finds the edge configuration.

        Args:
            mac (str): The MAC address to search for.
            switch (str): The switch that we want to search.
            device_ip (str): the IP the device is pulling.
            keep_connection (Connection): Optional - if given, this will use
                this existing connection and keep it open when completed.

        Returns:
            tuple or bool: If successfully found, returns the switch name,
            switch port, and configuration in a 3-tuple of strings. If we get an
            error that we can handle, returns the name, switch port, and error
            in a 3-tuple of strings; Otherwise, if nothing is found, returns
            False.

        """
        try:
            if keep_connection is None:
                connection, output = self.switchaccess.login_and_run(switch,
                        'show mac address-table address '+ mac + ' | include ' +
                        mac)
            else:
                connection = keep_connection
                output = connection.send_command(
                        'show mac address-table address '+ mac + ' | include ' +
                        mac)

            switch_data = self.get_switch_name(connection)
            on_foundry = False
            if "Invalid input" in output:
                on_foundry = True
                output = connection.send_command("show mac-address " + mac +
                        " | include " + mac) # remove header
            if not output and ('r1' in switch or 'r2' in switch):
                raise WrongRouterException()
            elif output and ('r1' in switch or 'r2' in switch):
                device_ip = self.find_ip(connection, output, mac)
            elif not output:
                message = ('Device is not reporting its MAC to this neighbor,' +
                        ' although it was reporting to the router. Here is ' +
                        'the neighbor.')
                return MacLocation(switch_data[0], switch, None,
                        message, None, None, device_ip)

            # Parses the port from the MAC table.
            parsed = output.split(' ')
            cdp_port = None
            for s in parsed:
                if '/' in s or 'Po'in s:
                    cdp_port = s.replace('\r', '')
                # mac is found only on this devices peer, go to that peer
                elif 'Peer-Link' in s:
                    return (switch.replace('1', '2', 1), device_ip)
            #This will run if the switch is a foundry, and can't be run with the
            #above statement
            if cdp_port is None:
                for s in parsed:
                    if (s.isdigit() and len(s) < 3 and int(s) < 100):
                        cdp_port = s.replace('\r', '')

            if cdp_port is None:
                message = ('The CDP Port that this device is connected to ' +
                        'could not be found. Here is the last known ' +
                        'information.')
                return MacLocation(switch_data[0], switch, None,
                        message, None, None, device_ip)

            if on_foundry:
                cdp_detail = connection.send_command("show lldp neighbor "
                        + "detail ports ethernet " + cdp_port)
            else:
                #checks for cisco first
                cdp_detail = connection.send_command('show cdp neighbor int '
                                        + cdp_port + ' detail')

                if "Invalid" in cdp_detail: # or '^' in cdp_detail:
                    cdp_detail = connection.send_command('show cdp neighbor '
                                            + cdp_port + ' detail')

                #check foundry last
                if "Invalid" in cdp_detail:
                    cdp_detail = connection.send_command('show lldp neighbor '
                                         + cdp_port + ' detail')

            #Checks if its a cisco router or switch.
            if ('NX-OS' in cdp_detail or 'Cisco IOS' in cdp_detail
                    or ("Chassis id" in cdp_detail and 'sx' in
                    cdp_detail.lower())):
                # Finds the first match that fits the IP pattern.
                cdp_detail = cdp_detail.split('Management')
                return (self.ip_pattern.search(cdp_detail[-1]).group(0),
                        device_ip)
            # We're at an edge port
            elif ('Total cdp entries displayed : 0' in cdp_detail or
                    'Total entries displayed: 0' in cdp_detail or cdp_detail is
                    '' or 'MED Information' in cdp_detail):
                config = connection.send_command('show interface ' + cdp_port +
                        ' switchport')
                #This grabs a simple overview of the port, for readability
                simple_config = connection.send_command('show run int ' +
                        cdp_port)
                # remove "Admin private-vlan lines"
                config = '\n'.join([l for l in config.splitlines()
                        if not l.startswith("Administrative private-vlan")])
                return MacLocation(switch_data[0], switch, cdp_port,
                        None, simple_config, config, device_ip)
            #this is an edge port of the foundry swithes
            elif "No neighbors" in cdp_detail: # or 'Local port:' in cdp_detail:
                print("we got here")
                simple_config = connection.send_command("show vlan ethernet " +
                        cdp_port)
                return MacLocation(switch_data[0], switch, cdp_port,
                        None, simple_config, '', device_ip)
            elif 'Cisco AP' in cdp_detail:
                # If we're dealing with an AP, we don't want to bother searching
                message = ("The MAC address appears to be connected to an AP. "+
                        "The switch and port are the last known information.")
                return MacLocation(switch_data[0], switch, cdp_port,
                        message, None, None, device_ip)
            else:
                message = ('Could not find where the device is directly ' +
                        'connected, here is the last known switch and port.')
                return MacLocation(switch_data[0], switch, cdp_port,
                        message, None, None, device_ip)
        # ignore wrong router exceptions for logging purposes. It is an expected
        # behavior
        except WrongRouterException as e:
            raise e
        # Leave a more informative message for users that TOAST is unable to
        # log into this specific device
        except IOError as e:
            message = ('MacTracker is unable to log in to ' + str(switch) +
                    '. This could be a result of a TACACS error or the ' +
                    'switch being offline.')
            # connection was never assigned, so this is
            # required for the finally statement to work
            connection = None
            return MacLocation(switch, None, None, message, None,
                    None, device_ip)
        except Exception as e:
            traceback.print_exc()
            message = ('MacTracker has run into an unexpected error: ' + str(e))
            switch_data = self.get_switch_name(connection)
            return MacLocation(switch_data[0], switch, None,
                    message, None, None, device_ip)
        finally:
            if connection and not keep_connection:
                self.switchaccess.logout(connection)

    def get_switch_name(self, connection):
        """
        Helper function to get the name and IP address of the switch the
        connection is currently logged into.

        Args:
            connection (Connection): The current connection.

        Returns:
            tuple: 2-tuple of the switch name and IP address.
        """
        try:
            switch_name = connection.send_command('\n',
                    trim=False).splitlines()[-1].replace('#', '')
        except:
            switch_name = None
        try:
            switch_ip = connection.send_command(
                    'show ip interface brief | exclude unassigned')
            switch_ip = switch_ip.splitlines()[1].split()[1]
        except:
            switch_ip = None
        return (switch_name, switch_ip)

    def find_ip(self, connection, vlan_input, mac):
        """
        helper function used to retrieve the IP that is connected to a MAC
        address, if any

        Args:
            connection (Connection): the current connection
            vlan_input (str): a string containg the vlan and the MAC
            mac (str): the mac address formatted in cisco style

        Returns:
            str: the IP found tied to the MAC, or None if none is found
        """
        parsed = vlan_input.split(' ')
        parsed = [_f for _f in parsed if _f]
        vlan = parsed[1]
        ip = None
        vrf = None
        raw_ip = None
        vlan_config = connection.send_command("show run int vlan " + vlan)
        parsed = vlan_config.split(' ')
        for index, thing in enumerate(parsed):
            if ('vrf' in thing and ('member' in parsed[index+1] or 'forward' in
                    parsed[index+1])):
                vrf = parsed[index+2].replace('\r', '').replace('\n', '')

        if vrf:
            raw_ip = connection.send_command("show ip arp vlan " + vlan +
                    " vrf " + vrf + " | inc " + mac)
            if "Invalid" in raw_ip:
                raw_ip = connection.send_command("show ip arp vrf " + vrf +
                        " vlan " + vlan +  " | inc " + mac)
        else:
            raw_ip = connection.send_command("show ip arp vlan " + vlan +
                    " | inc " + mac)
        if self.ip_pattern.search(raw_ip):
            ip = self.ip_pattern.search(raw_ip).group(0)
        return ip

    def get_thread(self, thread_id, autodelete=False):
        """
        Get information/output for a running or recently-completed
        mactracking thread.

        Args:
            thread_id (int): Thread ID.
            autodelete (bool): Optional - If True, this will delete thread
                information if the thread/route finding has been completed.

        Returns:
            dict: Contains the tracking message and a MACLocation namedtuple.
        """
        self.lock.acquire()
        try:
            thread_id = int(thread_id)
            if thread_id not in self.threads.keys():
                return # nothing
            thread_dict = self.threads[thread_id]
            if autodelete and thread_dict['message'] is None:
                # thread is done, delete
                thread_dict = copy.copy(self.threads[thread_id])
                del self.threads[thread_id]
            return thread_dict
        finally:
            self.lock.release()

    def get_thread_and_connection(self, thread_id, autodelete=False):
        """
        Get the same information as get_thread(), but return an open
        connection in the dictionary as well. Note that this is not a
        repeatable function - once this is run the connection object is removed
        from MACTracker.

        Args:
            thread_id (int): Thread ID.
            autodelete (bool): Optional - If True, this will delete thread
                information if the thread/route finding has been completed.

        Returns:
            dict: A 2-tuple of a dictionary like get_thread() and a Connection
            object.
        """
        thread_dict = self.get_thread(thread_id, autodelete)
        if not thread_dict:
            return
        self.lock.acquire()
        try:
            if thread_id in self.thread_connections.keys():
                thread_conn = copy.copy(self.thread_connections[thread_id])
                del self.thread_connections[thread_id]
                return thread_dict, thread_conn
            else:
                raise ValueError("Thread ID " + str(thread_id) +
                        " connection not tracked")
        finally:
            self.lock.release()

    def start_mactrack_thread(self, mac, router=None, keep_connection=False):
        """
        Start a MACTracker thread.

        Args:
            mac (str): MAC address.
            router (str): Optional - router name.
            keep_connection (bool): Optional - if True, keep the Connection
                object open for the discovered switch and return it in a
                separate thread dictionary.

        Returns:
            int: A thread ID, to reference the running thread
        """
        thread_id = int(round(time.time() * 1000))
        try:
            self.lock.acquire(True)
            time.sleep(0.01) # make sure thread_id is unique
            self.threads[thread_id] = MTThread(thread_id, self, mac, router,
                    keep_connection)
            self.threads[thread_id].start()
            return thread_id
        finally:
            self.lock.release()

    def _update(self, thread_id, message, maclocation):
        """
        Internal function - update a routefinding thread with information
        from the thread.

        Args:
            thread_id (int): Thread ID
            message (str): Message for thread.
            maclocation (MacLocation): Named tuple
        """
        self.lock.acquire()
        self.threads[thread_id] = {"message": message,
                "maclocation": maclocation, "error": False}
        self.lock.release()

    def _update_error(self, thread_id, message):
        """
        Internal function - update a routefinding thread with information
        from the thread, with an error message.

        Args:
            thread_id (int): Thread ID
            message (str): Message for thread
        """
        self.lock.acquire()
        self.threads[thread_id] = {"message": message, "maclocation": None,
                "error": True}
        self.lock.release()

    def _update_connection(self, thread_id, connection):
        """
        Internal function - add a connection to the thread_connections dict.

        Args:
            thread_id (int): Thread ID.
            connection (Connection): Connection object.
        """
        self.lock.acquire()
        self.thread_connections[thread_id] = connection
        self.lock.release()

class MTThread(threading.Thread):
    """
    Tracks mac address in a thread.

    Args:
        threadID (int): Thread ID
        mt (MacFinder): MacFinder object
        macaddress (str): Mac address to track
        startrouter (str): Optional - Starting router dns name.
        keep_connection (bool): Whether to keep connection open.
    """
    def __init__(self, threadID, mt, macaddress, startrouter=None,
            keep_connection=False):
        super(MTThread, self).__init__()
        self._kill = threading.Event()
        self.threadID = int(threadID)
        self.mt = mt
        self.aci = mt.acitools
        self.macaddress = mt.parse_mac(macaddress)
        self.startrouter = startrouter
        self.keep_connection = keep_connection
        self.name = "Tracker.MACTrack"

    def run(self):
        """
        Runs the thread
        """
        try:
            if self.startrouter:
                routerlist = [self.startrouter]
                if self.startrouter not in self.mt.routerlist:
                    raise ValueError("Starting router name " +
                            str(self.startrouter) + " not in router list")
                message = "checking " + str(self.startrouter) + "..."
            else:
                routerlist = self.mt.routerlist
                message = "checking all routers..."
            self.mt._update(self.threadID, message, None)
            threadlist = []
            for router in routerlist:
                #This check explicitly ignores the DDC and TDC routers,
                #because those are checked by the ACI thread
                if "i11" in router or "tdc" in router:
                    continue
                thr = SwitchThread(self.threadID, self.mt, router,
                        self.macaddress, self.keep_connection)
                threadlist.append(thr)
                thr.start()

            if self.aci is not None:
                # start a thread to check for the mac in ACI, if enabled
                thr = SwitchThread(self.threadID, self.mt, 'aci',
                        self.macaddress, self.keep_connection)
                threadlist.append(thr)
                thr.start()

            for thr in threadlist:
                thr.join()

            if (self.mt.get_thread(self.threadID) and
                    self.mt.get_thread(self.threadID)['message'] == message):
                # last known message was "checking *...", no router found
                self.mt._update_error(self.threadID, "Not found on any routers")
        except Exception as e:
            traceback.print_exc()
            self.mt._update_error(self.threadID, "MACTracker error: " + str(e))

class SwitchThread(threading.Thread):
    """

    Args:
        threadID (int): Thread ID
        mt (MacFinder): MacFinder object
        router (str): Router name.
        macaddress (str): Mac address to track.
        keep_connection (bool): Optional - Whether to keep connection open.
    """
    def __init__(self, threadID, mt, router, macaddress, keep_connection=False):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.mt = mt
        self.macaddress = self.mt.parse_mac(macaddress)
        self.router = router
        self.keep_connection = keep_connection
        self.name = "Tracker.ReadSwitch"

    def run(self):
        """
        Runs the thread.
        """
        try:
            next_hop = self.router
            device_ip = ""
            if self.mt.acitools is not None and self.router == 'aci':
                result = self.mt.acitools.search_endpoint(self.macaddress)
                if result:
                    aci_info = [dict(r._asdict()) for r in result][0]
                    maclocation = MacLocation(aci_info['epg'], None,
                                aci_info['encap'], None, aci_info['path'],
                                aci_info['vcenter'], aci_info['ip'])
                    self.mt._update(self.threadID, None, maclocation)
                    # add a None to the connection dict if specified, so
                    # get_thread_and_connection() doesn't break with ACI
                    if self.keep_connection:
                        self.mt._update_connection(self.threadID, None)
                    return
                else:
                    raise WrongRouterException
            # main loop
            while True:
                if next_hop != self.router:
                    self.mt._update(self.threadID,
                            'logging into ' + next_hop + '...', None)

                try:
                    open_conn = None
                    if self.keep_connection:
                        open_conn = self.mt.switchaccess.login(next_hop)

                    result = self.mt.search_switch(self.macaddress,
                            next_hop, device_ip, keep_connection=(
                            open_conn if self.keep_connection else None))
                    if isinstance(result, MacLocation) or result is None:
                        self.mt._update(self.threadID, None, result)
                        # this is the place, don't close open_conn if specified
                        if self.keep_connection:
                            self.mt._update_connection(self.threadID, open_conn)
                        return
                    elif (not isinstance(result, MacLocation) and
                            isinstance(result[0], str)):
                        next_hop = result[0] # continue loop
                        device_ip = result[1]
                        if self.keep_connection:
                            self.mt.switchaccess.logout(open_conn)
                    else:
                        self.mt._update_error(self.threadID, "Unknown state")
                        if self.keep_connection:
                            self.mt.switchaccess.logout(open_conn)
                        return
                except:
                    if self.keep_connection:
                        # don't keep this connection open with an exception
                        self.mt.switchaccess.logout(open_conn)
                    raise
        except WrongRouterException:
            pass # pass this error to the MTThread
        except Exception as e:
            traceback.print_exc()
            self.mt._update_error(self.threadID, str(e))
