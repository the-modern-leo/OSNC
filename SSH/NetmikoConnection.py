from netmiko import SSHDetect, ConnectHandler
from auth import SSH
import logging
logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")

def _exception(e):
    logging.error(e)
    return

class connection():
    def __init__(self,host,device_type=None):
        self.host = host
        self.device_type = device_type
        self.device = {
                'device_type':device_type,
                'host':host,
                'username':SSH.username,
                'password':SSH.password}

    def connnect(self):
        try:
            if self.device_type == None:
                self._auto_connect()
            net_connect = ConnectHandler(**self.device)
            return net_connect
        except Exception as e:
            _exception(e)

    def _auto_connect(self):
        try:
            device = {
                "device_type": "autodetect",
                "host": self.host,
                'username':SSH.username,
                'password':SSH.password}

            guesser = SSHDetect(**device)
            best_match = guesser.autodetect()
            print(best_match)  # Name of the best device_type to use further
            print(guesser.potential_matches)  # Dictionary of the whole matching result
            # Update the 'device' dictionary with the device_type
            self.device["device_type"] = best_match
        except Exception as e:
            _exception(e)



