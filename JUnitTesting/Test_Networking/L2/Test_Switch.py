import unittest
from Network.L2.Switch import Stack
import re
from netaddr import mac_cisco


class TestStack(unittest.TestCase):

    def test_stack(self):
        s = Stack("10.45.150.129")
        s.login()
        s.conn.enable_cisco()
        s.getSwitchInfo()
        s.assignattributes()

    def test_ip_DHCP_snooping(self):
        devicelist = []
        for ip in devicelist:
            s = Stack(ip)
            s.login()
            s.conn.enable_cisco()
            s.getSwitchInfo()
            s.assignattributes()
            result1 = s.conn.send_command("config t")
            result2 = s.conn.send_command("ip dhcp snooping")
            result3 = s.conn.send_command("ip dhcp snooping vlan 1-4094")
            for neighbor in s.cdpneighbors:
                int = "int " + str(neighbor.interface)
                result4 = s.conn.send_command(int)
                result5 = s.conn.send_command("ip dhcp snooping trust")
            result6 = s.conn.send_command("end")
            result7 = s.conn.send_command("wri")
            result8 = s.conn.send_command("show run | sec dhcp")
            if "ip dhcp snooping vlan 1-4094" in result8 and "ip dhcp snooping trust" in result8:
                pass
            else:
                pass
            s.logout()
            

