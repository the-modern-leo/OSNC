from Network.L2.Switch import Stack
from Network.L3.Router import Router
from Services.SQL.Mysql import DB
import re
from netaddr import mac_cisco


class Endpoint():
    def __init__(self):
        self.ip = None
        self.mac = None
        self.switchport = None
        self.Switch = None
        self.NetID = None
        self.dnsname = None
        self.company = None
        self.defaultgateway = None
        self.Router = None
    def sqlValues(self):
        return (self.ip, self.dnsname,self.switchport,self.mac,self.NetID,self.company)