import unittest
from Network.L2.Switch import Stack
from Network.L3.Router import Router
from Services.SQL.Mysql import DB
import re
from netaddr import mac_cisco


class TestStack(unittest.TestCase):

    def test_stack(self):
        s = Stack("10.45.150.129")
        s.login()
        s.conn.enable_cisco()
        s.getSwitchInfo()
        s.assignattributes()

    def test_get_endpointInformation(self):
        switchestoCollectEndpoints = set()
        switcheswithendpoints = set()
        allswitches = set()
        with DB() as conn:
            results = conn.GetallSwitches()
            inteserstring = f"endpoints (switchport,macaddress,NetID) VALUES (%s, %s,%s)"
            endpoints = conn._select_record(f"* FROM endpoints")
        for endpoint in endpoints:
            switcheswithendpoints.add(endpoint[5])
        for sw in results:
            allswitches.add(sw[0])
        SwitchIDSwithnoendpoints = allswitches - switcheswithendpoints
        SwitchTupleSwithnoendpoints = set()
        for swTuple in results:
            if swTuple[0] in SwitchIDSwithnoendpoints:
                SwitchTupleSwithnoendpoints.add(swTuple)
        for switch in results:
            for endpoint in endpoints:
                if not endpoint[5] == switch[0]:
                    switchestoCollectEndpoints.add(switch)
                    continue
        for switchtuple in SwitchTupleSwithnoendpoints:
            try:
                s = Stack(switchtuple[1])
                s.login()
                s.conn.enable_cisco()
                s.getSwitchInfo()
                s.assignattributes()
                all_ports = s.allinterfaces()
                if not switchtuple[5]:
                    with DB() as conn:
                        if s.defaultgateway:
                            results = conn._update_record(f"networkdevice SET deafultgateway = '{str(s.defaultgateway)}' WHERE NetID = {switchtuple[0]}")
                for port in all_ports:
                    if not port.trunk:
                        for macaddress in port.mac_addresses:
                            macaddress.dialect = mac_cisco
                            try:
                                with DB() as conn:
                                    conn.addendpoint(inteserstring, (str(port),str(macaddress),switchtuple[0]))
                            except Exception as t:
                                print (t)
                                pass
            except Exception as e:
                print(e)
                continue
            s.logout()
        for switchtuple in SwitchTupleSwithnoendpoints:
            try:
                s = Stack(switchtuple[1])
                s.login()
                s.conn.enable_cisco()
                s.getSwitchInfo()
                s.assignattributes()
                pass
            except:
                continue
            s.logout()

    def test_ip_DHCP_snooping(self):
        with DB() as conn:
            results = conn.GetallSwitches()
        pass
        for switchtuple in results:
            try:
                s = Stack(switchtuple[1])
                s.login()
                s.conn.enable_cisco()
                s.getSwitchInfo()
                s.assignattributes()
                interface_list = []
                for neighbor in s.cdpneighbors:
                    if "bilbo" in neighbor.deviceid.lower() or "frodo" in neighbor.deviceid.lower():
                        interface_list.append(str(neighbor.interface))
                    if "pcc" in neighbor.deviceid.lower():
                        interface_list.append(str(neighbor.interface))
                if interface_list:
                    s.push_ipdhcpsnooping("1-4094", interface_list)
            except:
                continue
            s.logout()

            

