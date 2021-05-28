from future import standard_library
standard_library.install_aliases()
from builtins import next
from builtins import str
from builtins import range
from builtins import object
import sys, threading, socket, time, traceback, logging, subprocess, queue
from netaddr import IPAddress, IPNetwork
from netaddr.core import AddrFormatError
from collections import namedtuple

INTERVAL = 1.0 # ping interval, in seconds
TIMEOUT = 3600 # ping timeout, in seconds (3600 = 1 hour)

# pick the correct ping timeout option depending on OS
PING_TIMEOUTCMD = ("-t" if 'darwin' in sys.platform else
        ('-W' if 'linux' in sys.platform else ''))
PINGOPTS = ('-O' if 'linux' in sys.platform else '')

Endpoint = namedtuple('Endpoint', ['ip', 'fqdn'])

class PingWall(object):
    """
    Utilities for pinging multiple endpoints and displaying results, as well
    as pinging from certain routers.
    """
    def __init__(self):
        self.threads = {}
        self.threadlock = threading.Lock()

    def _get_endpoint(self, epstring):
        """
        Get endpoint data (FQDN and IP) from an endpoint string, which may
        contain either the FQDN or IP.

        Args:
            epstring (str): Endpoint data (IP or FQDN)

        Returns:
            Endpoint: An Endpoint namedtuple.

        Raises:
            ValueError: When there is no IP for the endpoint
        """
        ip = None
        dns = None
        try:
            ip = IPAddress(epstring)
            # no exceptions raised, so an IP was passed in - look up DNS
            try:
                dns = socket.gethostbyaddr(epstring)[0]
            except:
                pass # no hostname found
        except AddrFormatError:
            # DNS FQDN was passed in, so grab IP
            try:
                dns = epstring
                ip = socket.gethostbyname(epstring)
                ip = IPAddress(ip)
            except socket.gaierror:
                raise ValueError("Invalid endpoint " + str(epstring))

        if not ip:
            raise ValueError("No IP found for endpoint " + str(epstring))
        return Endpoint(str(ip), dns)

    def _scan_subnets(self, pinglist):
        """
        Convert a pinglist containing subnets/CIDR blocks to individual IPs.

        Args:
            pinglist (list): List of IPs, FQDNs or subnets as strings.

        Returns:
            list: A list of IPs or FQDNs as strings.
        """
        new_pinglist = []
        for item in pinglist:
            try:
                ipn = IPNetwork(item)
                if ipn.prefixlen == 32:
                    # copy IP as-is
                    new_pinglist.append(item)
                else:
                    # otherwise get host IPs from the subnet (skip network and
                    # broadcast IP)
                    new_pinglist.extend([str(ip) for ip in list(ipn[1:-1])])
            except AddrFormatError:
                new_pinglist.append(item) # must be an FQDN, continue

        return new_pinglist

    def scan_endpoints(self, eplist):
        """
        Ping scan a list of endpoints and returns the list of hosts that reply.
        Args:
            eplist (list): list of Endpoint named tuples.

        Returns:
            list: A list of Endpoint named tuples that have replied.
        """
        NUM_THREADS = 8
        epqueue = queue.Queue()
        for ep in eplist:
            epqueue.put(ep)
        # start up some scan threads
        threadlist = []
        for thr in range(NUM_THREADS):
            threadlist.append(ScanPingThread(epqueue))
            threadlist[thr].daemon = True
            threadlist[thr].start()
        # wait until all threads are complete, then collect results
        epqueue.join()
        new_eplist = []
        for thr in range(NUM_THREADS):
            new_eplist.extend(threadlist[thr].get_results())
        return new_eplist

    def start_scan(self, pinglist):
        """
        Start a ping scan thread.

        Args:
            pinglist (list): List of endpoints (IP addresses or hostnames) as 
                strings.

        Returns:
            list: List of reachable IPs as strings.

        Raises:
            ValueError: When there are too many endpoints
        """
        pinglist = self._scan_subnets(pinglist)

        # check list length
        if len(pinglist) > 256:
            raise ValueError("Too many endpoints")

        # change pinglist into a list of Endpoints
        eplist = [self._get_endpoint(ep) for ep in pinglist]
        return [ep.ip for ep in self.scan_endpoints(eplist)]

    def start_pings(self, pinglist, unid=None):
        """
        Start a continuous ping thread.

        Args:
            pinglist (list): List of endpoints (IP addresses or hostnames) as 
                strings.
            unid (str): Optional - starting uNID

        Returns:
            int: Thread ID

        Raises:
            ValueError: When there are too many endpoints
        """
        thread_id = int(round(time.time() * 1000))
        pinglist = self._scan_subnets(pinglist) # scan pinglist for subnets

        # check list length
        if len(pinglist) > 256:
            raise ValueError("Too many endpoints")

        # change pinglist into a list of Endpoints
        eplist = [self._get_endpoint(ep) for ep in pinglist]
        try:
            self.threadlock.acquire()
            self.threads[thread_id] = ContinuousPingThread(thread_id, unid,
                    eplist, self.stop_pings)
            self.threads[thread_id].start()
            return thread_id
        finally:
            self.threadlock.release()

    def stop_pings(self, threadid):
        """
        Stop a ping thread.

        Args:
            threadid (int): Thread ID to stop

        Raises:
            ValueError: When the thread can't be found
        """
        if threadid not in list(self.threads.keys()):
            raise ValueError(str(threadid) + ' invalid or already stopped')

        try:
            self.threadlock.acquire()
            self.threads[threadid].cancel()
        finally:
            self.threadlock.release()

    def get_threads(self):
        """
        Gets list of threads.

        Returns:
            list: List of Thread ID integers.
        """
        return list(self.threads.keys())

    def get_status(self, threadid):
        """
        Get the current status/state of a ping thread.

        Args:
            threadid (int): Thread ID

        Returns:
            dict or None: with endpoints and DNS and statuses if running; None
            otherwise
        """
        if threadid not in list(self.threads.keys()):
            return # no results

        try:
            self.threadlock.acquire()
            results = self.threads[threadid].get_results()
            if self.threads[threadid].stop:
                # this thread is stopped, return one last time and delete thread
                del self.threads[threadid]
            return results
        finally:
            self.threadlock.release()

    def ping_from_router(self, switchaccess, router, endpoint, vrf=None):
        """
        Ping an endpoint directly from a particular router.

        Args:
            switchaccess (SwitchAccess): SwitchAccess object to use for router 
                logins.
            router (str): Router name as a string, must be a member of the
                Network.get_routerlist() list.
            endpoint: Endpoint to ping
            vrf (str): Optional - VRF name

        Raises:
            ValueError: When the router name is invalid
        """
        if not switchaccess:
            return # Network is not available

        routerlist = switchaccess.get_routerlist()
        if (router not in routerlist['nexus']
                and router not in routerlist['ios']):
            raise ValueError("Invalid Router name, must be in router whitelist")

        endpoint = self._get_endpoint(endpoint)
        if vrf is not None:
            vrf = ''.join([c for c in vrf if c.isalnum() or c in ['-','_']])

        is_nxos = (router in routerlist['nexus'])
        if is_nxos:
            command = ('ping ' + endpoint.ip + (' vrf '+vrf if vrf else ''))
        else:
            command = ('ping ' + (' vrf ' + vrf if vrf else '') +
                    ' ' + endpoint.ip)
        connection = None
        try:
            connection, output = switchaccess.login_and_run(router, command)
            output = output.replace('\r\n', '\n')
            if is_nxos and '---' in output:
                output = output[output.find('---'):]
            elif 'Sending' in output:
                output = output[output.find('Sending'):]
            return output
        finally:
            switchaccess.logout(connection)

class ContinuousPingThread(threading.Thread):
    """
    Class used to represent a thread that continuously pings an endpoint.

    Args:
        threadid (int): The ID of the thread
        unid (str): unid of the user
        eplist (list): list of endpints
        stop_callback (instancemethod):method to be used as a callback
    """
    def __init__(self, threadid, unid, eplist, stop_callback):
        threading.Thread.__init__(self)
        self.threadID = threadid
        self.unid = unid
        # pingdict format: IP key: (DNS, latency, successful pings, total pings)
        self.pingdict = {ep.ip: (ep.fqdn, -1, 0, 0) for ep in eplist}
        self.procdict = {}
        self.generatordict = {}
        self.stop = False
        self.stop_callback = stop_callback
        self.name = "pingwall.ContinuousPing"

    def get_ping_status(self, ip):
        """
        Ping a particular IP in the background with subprocess. This returns
        a generator that can be used to asynchronously return IPs.

        Args:
            ip (str): The IP to ping

        Yields:
            str: A line containing an IP 

        """
        ip = str(ip)
        self.procdict[ip] = subprocess.Popen((['ping', PINGOPTS, ip]),
                stdout=subprocess.PIPE, universal_newlines=True)
        for line in iter(self.procdict[ip].stdout.readline, ""):
            yield line
        self.procdict[ip].stdout.close()
        del self.procdict[ip]

    def run(self):
        """
        Begin to ping all devices in local ping dictionary.
        """
        try:
            # start all ping processes first
            for ip, ep in list(self.pingdict.items()):
                self.generatordict[str(ip)] = self.get_ping_status(str(ip))
                next(self.generatordict[str(ip)]) # throw away header

            timeout_start = time.time()
            while not self.stop:
                t_start = time.time()
                for ip, ep in list(self.pingdict.items()):
                    fqdn, latency, p_success, p_total = ep
                    try:
                        output = next(self.generatordict[str(ip)])
                    except StopIteration:
                        continue # this host is done

                    if 'time=' not in output: # no ping was returned
                        result = -1
                    else:
                        # read milliseconds from time= field
                        output = next(field for field in output.split()
                                if 'time=' in field)
                        result = int(float(output[5:].strip()))
                        p_success += 1

                    # save latency results
                    self.pingdict[ip] = (fqdn, result, p_success, p_total+1)

                # check timeout - so indefinite pings won't keep going
                t_now = time.time()
                if t_now > timeout_start + TIMEOUT:
                    logging.info('pings timed out for ' + str(self.unid) +
                            ', autostopping thread')
                    self.stop_callback(self.threadID)
                    break

                # consistently ping around the time matching INTERVAL
                # this helps if there are many/latent endpoints that take more
                # than INTERVAL to run
                if t_now < t_start + INTERVAL:
                    time.sleep((t_start + INTERVAL) - t_now)
        except:
            traceback.print_exc()

    def cancel(self):
        """
        Stops all process in the local process dictionary
        """
        self.stop = True
        # terminate all processes
        for ip in list(self.procdict.keys()):
            self.procdict[ip].terminate()

    def get_results(self):
        """
        gets the results

        Returns:
            dict: The results of the ping
        """
        return self.pingdict

class ScanPingThread(threading.Thread):
    """
    Represent a single thread of a ping scan.

    Args:
        queue (Queue): queue of endpoints to scan
    """
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.reachablelist = []
        self.queue = queue
        self.name = "pingwall.ScanSubnet"

    def run(self):
        """
        Run the ScanPingThread. If an endpoint responds, it is added to reachablelist.
        """
        while True:
            next_ep = self.queue.get()
            proc = subprocess.Popen((['ping','-c','1'] +
                    PING_TIMEOUTCMD.split() + ['1', str(next_ep.ip)]),
                    stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            output, error = proc.communicate()
            output = output.decode()
            if error:
                logging.warn('Ping error: ' + str(error))
                continue
            if 'time=' in output: # got a response, add to reachable list
                self.reachablelist.append(next_ep)
            self.queue.task_done()

    def get_results(self):
        """
        Getter that returns reachable endpoints.
        
        Returns: 
            list: list of reachable endpoints
        """
        return self.reachablelist
