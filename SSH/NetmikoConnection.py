from netmiko import ConnectHandler
from auth import SSH
import logging
logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")

def _exception(e):
    logging.error(e)
    return

class connection():
    def __init__(self,host,device_type):
        self.device = {
                'device_type':device_type,
                'host':host,
                'username':SSH.username,
                'password':SSH.password}

    def connnect(self):
        try:
            with ConnectHandler(**self.device) as net_connect:
                yield net_connect
                net_connect.disconnect()
        except Exception as e:
            _exception(e)



