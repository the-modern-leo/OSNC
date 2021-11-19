import dns.query
import dns.zone
import dns.resolver
import re, threading, time, logging

class DNSQuery(object):
    """
    This class is designed to query the DNS server, and return useful
    results for TOAST

    Args:
        dns_server (str): Optional - Defualts to . The given DNS
            Server is . The dns_server to query.
    """
    def __init__(self, dns_server=""):

        self.dns_server = dns_server
        self.threads = {}
        self.threadlock = threading.Lock()
        # set the DNS Server to the given DNS server
        dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
        dns.resolver.default_resolver.nameservers = [self.dns_server]
        # set the most popular zones at the top if using anycast
        if self.dns_server == "":
            self.zones = []
        else:
            self.zones = []
        # Update the Zones that are in the DNS Server
        UpdateThread(self).start()
        self.ip_pattern = re.compile("\\b((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]"
                "?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\b")

    def search_dns(self, thread_id, query, zone, hostnames):
        """
        This method performs a dig on the dns server in the given zone,
        and searches for the keyword in the zone entries. It returns
        a list of the hostnames and their related items, a CNAME or an IP.

        Arguments:
            thread_id (int): The id of the DQ thread to update.
            query (str): What to search for in the dig.
            zone (str): The specific zone to look in.
            hostnames (dict): Contains the results.
        """
        self.update(thread_id, 'Searching ' + zone + '...', None, False)
        dig = dns.zone.from_xfr(dns.query.xfr(self.dns_server, zone))
        dig_keys = list(dig.nodes.keys())
        dig_keys.sort()

        self.update(thread_id, 'Parsing ' + zone + '...', None, False)
        for key in dig_keys:
            line = str(dig[key].to_text(key))
            # exclude TXT entries and the inital entry for the search
            if query in line and '\"' not in line and "@" not in line:
                line = line.split()
                hostnames[self.format_data(line[0], zone)] = self.format_data(
                        line[-1], zone)

        self.update(thread_id, 'Finished Searching ' + zone + '...', None,
                False)

    def format_data(self, data, zone):
        """
        This method formats output from the dns query to look how
        the user would expect it to look.

        Arguments:
            data (str): The data from the query.
            zone (str): The zone the query was in.

        Returns:
            str: An IP address or a formatted host name.
        """
        # ignore IPv4, IPv6, and already formatted hostnames
        if re.match(self.ip_pattern, data) or ":" in data or ".edu" in data:
            return data
        else:
            return data + "." + zone

    def update_zones(self):
        """
        This method searches utah.edu and finds all of the unique
        name server entries and adds them to the assets text file,
        if the are not already in it.
        """
        dig = dns.zone.from_xfr(dns.query.xfr(self.dns_server, ''))
        dig_keys = list(dig.nodes.keys())
        dig_keys.sort()
        new_zones = []
        for key in dig_keys:
            line = str(dig[key].to_text(key))
            if 'NS' in line and '@' not in line:
                zone = line.split()[0] + ''
                if zone not in self.zones and zone not in new_zones:
                    new_zones.append(zone)

        for zone in new_zones:
            self.zones.append(zone)

    def update(self, thread_id, message, data, error):
        """
        This method updates the dictionary that is tied to a specific
        thread id that is a part of the threads dictionary. If it does
        not exist, it will add it to the threads dictionary.

        Arguments:
            thread_id (int): The thread_id key for the threads dictionary.
            message (str): the message to store.
            data (dict): data to return to the user.
            error (bool): True if there is an error, False otherwise.
        """
        self.threadlock.acquire()
        self.threads[thread_id] = {'message': message, 'data': data,
                'error': error, }
        self.threadlock.release()

    def status(self, thread_id):
        """
        This method queries the threads dictionary and retrieves what
        is currently stored as its value. It will delete threads and
        manage errors if there are any

        Arguments:
            thread_id (int): the key to search the threads dictionary.

        Returns:
            dict: Result under the key 'result' or error under the key 'error'.
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
            return {'result': {'message': thread_current['message'],
                    'data': thread_current['data']}}

    def dig(self, query, zone=None, get_thread=False):
        """
        This is the main method of external use. It starts a thread that
        will search the given zone or all zones if one is not given.

        Arguments:
            query (str): The string that you want to query the dns server with.
            zone (str): The zone to search in.
            get_thread (bool): True if you want the thread, false if you only
                want the result.
        Returns:
            int or dict: The thread id if get_thread is True; the result
            dictionary if thread_id is false.
        """
        thread_id = int(round(time.time() * 1000))
        hostnames = {}
        dqthread = DQThread(thread_id, query, self, hostnames, zone=zone)
        dqthread.start()
        if not get_thread:
            dqthread.join()
            return self.threads[thread_id]
        return thread_id

class DQThread(threading.Thread):
    """
    Used by other classes to start a DNS query.

    Args:
        threadID (int): The thread_id key for the threads dictionary.
        query (str): The string that you want to query the dns server with.
        dq (DNSQuery): DNS Query object to be updated.
        hostnames (dict): Contains the results.
        zone (str): This zone to search in.
    """

    def __init__(self, threadID, query, dq, hostnames, zone=None):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.query = query
        self.dq = dq
        self.hostnames = hostnames
        self.zone = zone

    def run(self):
        """
        Runs the thread.
        """
        # start a new thread for each zone
        if not self.zone:
            self.dq.update(self.threadID, 'Searching all zones...', None, False)
            threadlist = []
            for zone in self.dq.get_zones():
                thr = DigThread(self.threadID, self.query, self.dq,
                        self.hostnames, zone)
                threadlist.append(thr)
                thr.start()

            for thr in threadlist:
                thr.join()
            self.dq.update(self.threadID, None, self.hostnames, False)
        # start a thread with the given DNS zone
        else:
            self.dq.update(self.threadID, 'Searching ' + self.zone + '...',
                    None, False)
            thr = DigThread(self.threadID, self.query, self.dq, self.hostnames,
                    self.zone)
            thr.start()
            thr.join()
            self.dq.update(self.threadID, None, self.hostnames, False)

class DigThread(threading.Thread):
    """
    Class thread for performing a dig on the dns server.

    Args:
        threadID (int): The thread_id key for the threads dictionary.
        query (str): What to search for in the dig.
        dq (DNSQuery): DNS query object to be [blank]
        hostnames (dict): Contains the results.
        zone (str): This zone to search in.
    """
    def __init__(self, threadID, query, dq, hostnames, zone):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.query = query
        self.dq = dq
        self.hostnames = hostnames
        self.zone = zone

    def run(self):
        """
        Runs the dig.
        """
        self.dq.search_dns(self.threadID, self.query, self.zone, self.hostnames)

class UpdateThread(threading.Thread):
    """
    Class thread for updating the DNS Query.

    Args:
        dnsquery (DNSQuery): DNSQuery object to be updated.
    """
    def __init__(self, dnsquery):
        threading.Thread.__init__(self)
        self.dnsquery = dnsquery

    def run(self):
        """
        Runs update.
        """
        self.dnsquery.update_zones()
