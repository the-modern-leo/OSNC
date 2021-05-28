import random
from collections import namedtuple

maclocation = namedtuple('maclocation', ['mac', 'current_ip'])

class TestMacTracker(object):
    """
    This class takes in and gives test input and output for 
    the purposes of testing TestTracker
    """

    def __init__(self):
        self.threads = {}

    def start_mactrack_thread(self, mac):
        thread = random.randint(0,1000)
        if mac == "error":
            self.set_thread(thread, "error", None, True)
        else:
            self.set_thread(thread, None, maclocation(mac=mac, current_ip='1.1.1.1'), False)
        return thread

    def get_thread(self, thread, autodelete=False):
        return self.threads[thread]

    def set_thread(self, thread, message, data, error):
        self.threads[thread] = {'message': message, 'maclocation': data, 
                'error': error}  

    def parse_mac(self, mac):
        if mac is not None:
            return mac
        else:
            raise ValueError("bad")

class TestRouteFinder(object):
    """
    This class represents the routefinder module for TestTracker testing
    """

    def __init__(self):
        self.threads = {}

    def findroute(self, ip, config=False, synchronous=False):
        thread_id = random.randint(0, 1000)
        if ip == '1.1.1.1':
            self.threads[thread_id] = {'message': None, 'route': 
                    {'mac': '0000.0000.0000'}}
        else:
            self.threads[thread_id] = {'message':None, 'route': {
                    'thing':"this works"}}

        return thread_id

    def get_thread(self, thread):
        return self.threads[thread]
