import unittest
from Network.L2.Switch import Stack, Blade
from unittest.mock import Mock
from os import listdir
from os.path import isfile, join
import json

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
            
    def testAssignVersion(self):
        """testing Assigning Variables from several different Models, and Software Versions"""
        mypath = "C:/Users/nbradberry/Documents/Configurations"
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        for file in onlyfiles:
            try:
                with open(f'{mypath}/{file}') as json_data:
                        d = json.loads(json_data.read())
                        json_data.close()
                        s = Stack("10.45.150.129")
                        s.hostname = d["hostname"]
                        s.version_result = d["version_result"]
                        s.assignVersionVariables(d["version_result"])
                        self.assertTrue(s.blades)
                        for blade in s.blades:
                            self.assertIsInstance(blade,Blade)
                        self.assertTrue(s.uptime)
                        self.assertTrue(s.SystemSoftwareVersion)
            except Exception as e:
                print(e)

    def testAssigninventory(self):
        """testing Assigning Variables from several different Models, and Software Versions"""
        mypath = "C:/Users/nbradberry/Documents/Configurations"
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        for file in onlyfiles:
            try:
                with open(f'{mypath}/{file}') as json_data:
                    d = json.loads(json_data.read())
                    json_data.close()
                    s = Stack("10.45.150.129")
                    s.hostname = d["hostname"]
                    s.version_result = d["version_result"]
                    s.assignVersionVariables(d["version_result"])
                    s.sortInventory(d["inv_result"])
                    self.assertTrue(s.blades)
                    for blade in s.blades:
                        self.assertIsInstance(blade, Blade)
                    self.assertTrue(s.uptime)
                    self.assertTrue(s.SystemSoftwareVersion)
            except Exception as e:
                print(e)
