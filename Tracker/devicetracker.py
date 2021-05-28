import threading, time, logging, re

class DeviceTracker(object):
    """
    This class is designed to use both the Tracker and the
    routefinder objects to track devices on the network. If this is
    being used without multithreading, the thread_id parameter can be
    any int. The thread_id acts as a key for the results of this class,
    and those results are stored in a dictionary named threads that is 
    a part of the object.

    Args:
        mt_obj (MacFinder): a MacFinder object
        rf_obj (RouteFinder): a RouteFinder object
    """

    def __init__(self, mt_obj, rf_obj):
        self.mactracker = mt_obj
        self.rf = rf_obj
        self.threads = {}
        self.threadlock = threading.Lock()
        self.ip_pattern = re.compile("\\b((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]"
                "?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\b")

    def track(self, thread_id, search_item, mac_only=False, ip_only=False, 
            get_config=False, testing=False):
        """
        Tracks either a mac address or an IP address through the network. 
        There are options to retrieve only details for a mac, an IP, and to
        get the advanced config for these items

        Args:
            thread_id (int): the id of the thread stored in self.threads
            search_item (str): the IP or mac to search for
            mac_only (bool): whether or not to only search the mac
            ip_only (bool): whether or not to only search the IP
            get_config (bool): whether or not to get the advanced config
            testing (bool): check if running for Tests, skips the sleep calls
        """
        results = {'rf_result': {}, 'mt_result': {}}
        if ip_only:
            results['rf_result'] = self.ip_helper(thread_id, search_item, 
                    get_config=get_config, testing=testing)
            if results['rf_result']:
                self.update(thread_id, None, results, False)

        elif mac_only:
            results['mt_result'] = self.mac_helper(thread_id, search_item, 
                    get_config=get_config, testing=testing)
            if results['mt_result']:
                self.update(thread_id, None, results, False)
 
        else:
            if self.ip_pattern.search(search_item):
                results['rf_result'] = self.ip_helper(thread_id, search_item, 
                        get_config=get_config, testing=testing)
                if results['rf_result']:
                    self.update(thread_id, "Found IP details...", None, False)
                    if ( 'mac' in results['rf_result'] and
                            results['rf_result']['mac'] != 'No Associated MAC'):
                        results['mt_result'] = self.mac_helper(thread_id, 
                                results['rf_result']['mac'], 
                                get_config=get_config, testing=testing)
                        if results['mt_result']:
                            self.update(thread_id, None, results, False)
                    else:
                        self.update(thread_id, None, results, False)

            else:
                results['mt_result'] = self.mac_helper(thread_id, search_item, 
                        get_config=get_config, testing=testing)
                if results['mt_result']:
                    self.update(thread_id, "Found MAC details...", None, False)
                    if results['mt_result']['current_ip']:
                        results['rf_result'] = self.ip_helper(thread_id, 
                                results['mt_result']['current_ip'], 
                                get_config=get_config, testing=testing)
                        if results['mt_result']:
                            self.update(thread_id, None, results, False)
                    else:
                        self.update(thread_id, None, results, False)

    def ip_helper(self, thread_id, ip, get_config=False, testing=False):
        """
        Verifies the IP and gets the results from a helper method

        Args:
            thread_id (int): the id for the thread stored in self.threads
            ip (str): the IP to search for
            get_config (bool): whether or not to get the advanced config
            testing (bool): check if running for Tests, skips the sleep calls
        Returns:
            dict or None: if a result is found, returns the result in a dict;
            otherwise, it returns None.
            
        """
        if self.ip_pattern.search(ip):
            result = self.get_rf_results(thread_id, ip, get_config=get_config, 
                    testing=testing)
            if isinstance(result, str):
                self.update(thread_id, result, None, True)
                return None
            else:
                return result
        else:
            self.update(thread_id, "Invalid IP Address", None, True)
            return None

    def mac_helper(self, thread_id, search_item, get_config=False, 
            testing=False):
        """
        Verifies that the search_item is a mac address and searches
        for it on the network through a helper method

        Args:
            thread_id (int): the id for the thread stored in self.threads
            search_item (str): the item to parse as a mac address
            get_config (bool): whether or not to get the advanced config
            testing (bool): check if running for Tests, skips the sleep calls
        Returns:
            dict or None: if a result is found, returns the results; otherwise
            returns None
        """
        mac = None
        try:
            mac = self.mactracker.parse_mac(search_item)
        except Exception as e:
            self.update(thread_id, str(e), None, True)
            return None

        return self.get_mac_results(thread_id, mac, get_config=get_config, 
                testing=testing)
    
    def get_rf_results(self, thread_id, ip, get_config=False, testing=False):
        """
        Uses the routefinder object and manages its thread

        Args:
            thread_id (int): the id of the thread stored in self.threads
            ip (str): the ip to search for
            get_config (bool): whether or not to get the advanced config
            testing (bool): check if running for Tests, skips the sleep calls
        Returns:
            str or dict: string if there is an error on the thread, returns the 
            error message; If there is no error, returns the details in a 
            dict 
        """
        rf_thread = self.rf.findroute(ip, config=get_config, 
                        synchronous=False)
        while True:
            if not testing:
                time.sleep(2)
            rf_update = self.rf.get_thread(rf_thread)
            if not rf_update['message']:
                return rf_update['route']
            self.update(thread_id, rf_update['message'], None, False)

    def get_mac_results(self, thread_id, mac, get_config=False, testing=False):
        """
        Uses the Tracker object and manages its thread. Searches for
        port details based off of a mac

        Args:
            thread_id (int): id of the thread stored in self.threads
            mac (str): the mac to track
            get_config (bool): whether or not to get the advanced config
            testing (bool): check if running for Tests, skips the sleep calls
        Returns:
            dict or None: if a result is found, returns the results; None if 
            there is an error
        """
        mt_thread = self.mactracker.start_mactrack_thread(mac)

        while True:
            if not testing:
                time.sleep(2)
            mt_update = self.mactracker.get_thread(mt_thread, autodelete=True)
            if mt_update['error']:
                self.update(thread_id, mt_update['message'], None, True)
                return None
            elif not mt_update['message']:
                return mt_update['maclocation']._asdict()
            self.update(thread_id, mt_update['message'], None, False)

    def status(self, thread_id):
        """
        Access self.threads and get the information that is stored for 
        the specified thread_id

        Args:
            thread_id (int): the id of the thread stored in self.threads
        Returns:
            dict: contains either an error with a message or the 
                    status of the thread
        """
        self.threadlock.acquire()
        thread = self.threads.get(int(thread_id), None)   
        self.threadlock.release()

        if not thread:
            logging.error("thread " + str(thread_id) + " could not be found")
            return {'error': "Invalid Thread ID: Thread not found"}

        if not thread['message'] or thread['error']:
            self.threadlock.acquire()
            del self.threads[int(thread_id)]
            self.threadlock.release()

        if thread['error']:
            logging.error(thread['message'])
            return {'error': thread['message']}
        else:
            return {'result': {'message': thread['message'], 
                    'data': thread['data']}}

    def update(self, thread_id, message, data, error):
        """
        Update the data stored in the threads dictionary

        Args:
            thread_id (int): the id of the thread stored in self.threads
            message (str): the message to store
            data (dict): the result of the tracking
            error (bool): whether or not tere was an error
        """
        self.threadlock.acquire()
        self.threads[thread_id] = {'message': message, 'data': data, 
                'error': error}
        self.threadlock.release()

    def start_search(self, search_item, mac_only=False, ip_only=False, 
            get_config=False, get_thread=False, testing=False):
        """
        The main method of the class. Starts a threaded search for 
        details on the mac or IP given. Default is to run it in a non-threaded
        manner.

        Args:
            search_item (str): MAC or IP to search for
            mac_only (bool): whether or not to search for the mac only
            ip_only (bool): whether or not to search for the IP only
            get_config (bool): whether or not to get the advanced config
            get_thread (bool): True to get thread id and run on a new thread,
                    false to run in the same thread
            testing (bool): check if running for Tests, skips the sleep calls
        Returns:
            int or dict: the thread id if get_thread is True; the result if 
            get_thread is False
        """
        thread_id = int(round(time.time() * 1000))
        search = TrackingThread(thread_id, self, search_item, mac_only=mac_only,
                ip_only=ip_only, get_config=get_config, testing=testing)
        self.update(thread_id, "Starting search for search_item", None, False)
        search.start()

        if get_thread:
            return thread_id

        search.join()
        return self.threads[thread_id]


class TrackingThread(threading.Thread):
    """
    This class is designed to allow a TestTracker object to run in
    multiple threads

    Args:
        thread_id (int): the ID for this thread
        devicetracker (DeviceTracker): a DeviceTracker object
        search_item (str): the item to be searched for
        mac_only (bool): whether or not to only get mac info
        get_config (bool): whether or not to get the advanced configuration
        ip_only (bool): whether or not to only get the ip info
        testing (bool): whether or not this thread is for unit testing
    """
    def __init__(self, thread_id, devicetracker, search_item, mac_only=False, 
            get_config=False, ip_only=False, testing=False):
        threading.Thread.__init__(self)
        self.devicetracker = devicetracker
        self.thread_id = thread_id
        self.search_item = search_item
        self.mac_only = mac_only
        self.ip_only = ip_only
        self.get_config = get_config
        self.testing = testing

    def run(self):
        """
        Calls the track method of DeviceTracker in a separate thread
        """
        self.devicetracker.track(self.thread_id, self.search_item, 
                mac_only=self.mac_only, ip_only=self.ip_only, 
                get_config=self.get_config, testing=self.testing)