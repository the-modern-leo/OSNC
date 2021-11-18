#testing Frameworks
import unittest
from unittest.mock import patch


#Script functions
from Network.Switch import Stack, Neighbor
from Network.AccessList import ACL, ACL_Entry
from SNMP.Objects import SNMP, SNMP_community
from Network.Port import Interface
from Tacacs.Objects import TACACS

##packacges
from ipaddress import IPv4Address
from netaddr import EUI

from Tests.TestNetwork.device_list.Switches_syntax_compatability.cisco.catalyst import ws_c3560cx_8pc_s,\
    c29xx,c36xx,c38xx,c9407r,c4510r_e_,c94010r,c3560cg_8pc_s,c3560x_24_poe,c3650_48pq_e,c9300_series
from Tests.TestNetwork.device_list.Switches_syntax_compatability.cisco.nexus import c9332pq,c93180yc_fx

def mocked_creation_SSH_Netmiko(*args, **kwargs):
    """
    This should be for mocking responses from a Cisco 9300
    :return:
    """
    class MockResponse_Cisco_Catalyst_9300:
        pass

# def mocked_creation_SSH_paramiko(*args, **kwargs):
#     """
#     This should be for mocking responses
#     :return:
#     """
#     class MockResponse_SSH_paramiko_login:
#         pass
#     return MockResponse_SSH_paramiko_login

def mocked_creation_SSH_paramiko_channel(*args, **kwargs):
    """
    This should be for mocking responses
    :return:
    """
    class MockResponse_ssh_paramiko_channel:
        def __init__(self):
            pass
        def settimeout(self,timeoutlimit):
            self.timeoutlimit = timeoutlimit
        def recv(self,recv_number):
            self.recv_number = recv_number

    return MockResponse_ssh_paramiko_channel
class TestSwitchCommands(unittest.TestCase):
    """
    This is for Testing compatibility of Switch Devices accross multiple platforms
    """
    def test_Catalyst_2960(self):
        """
        scx1-ddc-d11.med.utah.edu
        Model: WS-C2960G-24TC-L
        Software Version: 12.2(44)SE6
        """
        s = Switch(ipaddress="172.20.71.105")
        s.login()
        s.getSwitchInfo()

        #test getting the information properly
        self.assertNotIn("Invalid input detected at",s.version_result)
        self.assertNotIn("Invalid input detected at",s.run_result)
        self.assertIn("Invalid input detected at",s.interface_result)
        self.assertNotIn("Invalid input detected at",s.interface_name_r)
        self.assertIn("Invalid input detected at",s.portdowntime_result)
        self.assertNotIn("Invalid input detected at", s.portdowntime_result_in)
        self.assertNotIn("Invalid input detected at",s.inv_result)
        self.assertNotIn("Invalid input detected at",s.portcount_result)
        self.assertNotIn("Invalid input detected at",s.cdpnei_result)
        self.assertIn("Invalid input detected at", s.module_result)
        self.assertIn("Invalid input detected at",s.snmp_result)
        self.assertNotIn("Invalid input detected at", s.snmp_result_in)
        self.assertNotIn("Invalid input detected at",s.logging_data_result)



        #Test the assigning of information to the correct objects
        s.assignattributes()

        #test global Variables
        self.assertEqual(s.bannername, 'scx1-ddc-d11.net.utah.edu')
        self.assertEqual(s.buildnumber, "3574")
        self.assertEqual(s.buildingname, 'ddc')
        self.assertEqual(s.racknumber, 'd11')
        self.assertEqual(s.description, 'Datacenter Sub Access Layer Switch')
        self.assertEqual(s.IPAddress, '172.20.71.105')
        self.assertEqual(s.portcount, 24)
        self.assertEqual(s.serial[0], 'FOC1427X55R')
        self.assertEqual(s.subnetmask, '255.255.255.192')
        self.assertNotEqual(s.uptime, None)

        #test the assignment of ACL object properties
        self.assertEqual(len(s.access_lists), 3)
        self.assertIn(199, s.access_lists.numbers)
        self.assertIn(70, s.access_lists.numbers)
        self.assertIn(71, s.access_lists.numbers)
        for aclobj in s.access_lists.standard_ip_lists:
            self.assertIsInstance(aclobj, ACL)
            self.assertIsInstance(aclobj.Entries,list)
            for entry in aclobj.Entries:
                self.assertIsInstance(entry, ACL_Entry)
                self.assertTrue(entry.type)
                self.assertTrue(entry.number)
            self.assertTrue(aclobj.Entries)
            self.assertTrue(aclobj.type)

        #test the assignment of the SNMP Value
        self.assertIsInstance(s.SNMP, SNMP)
        self.assertIsInstance(s.SNMP.communities,list)
        self.assertIsInstance(s.SNMP.traps,list)
        self.assertIsInstance(s.SNMP.traps,list)
        self.assertIsInstance(s.SNMP.version, set)
        self.assertTrue(s.SNMP.communities)
        self.assertEqual(len(s.SNMP.communities),5)
        for communities in s.SNMP.communities:
            self.assertIsInstance(communities,SNMP_community)
            self.assertTrue(communities.raw_data)
            self.assertTrue(communities.string)
        self.assertTrue(s.SNMP.traps)
        self.assertEqual(len(s.SNMP.traps),19)
        self.assertTrue(s.SNMP.version)
        self.assertTrue(s.SNMP.loggingips)
        self.assertIsInstance(s.SNMP.loggingips[0],IPv4Address)
        self.assertEqual(str(s.SNMP.loggingips[0]),'155.100.122.16')
        self.assertIn(2, s.SNMP.version)
        self.assertNotIn(3, s.SNMP.version)

        #check the blades configuration
        self.assertTrue(s.blades)
        self.assertEqual(len(s.blades),1)
        self.assertEqual(s.blades[0].ISOversion, '12.2(44)SE6')
        self.assertFalse(s.blades[0].SUP)
        self.assertEqual(s.blades[0].modelnumber,'WS-C2960G-24TC-L')
        self.assertEqual(s.blades[0].portcount, 24)
        self.assertTrue(s.blades[0].interfaces)
        self.assertEqual(len(s.blades[0].interfaces),24)
        portrange = range(1,25)
        for portnumber, interface in s.blades[0].interfaces.items():
            self.assertTrue(interface)
            self.assertIsInstance(interface.mac_addresses,list)
            if interface.mac_addresses:
                for macaddress in interface.mac_addresses:
                    self.assertIsInstance(macaddress,EUI)
            self.assertIsInstance(interface,Interface)
            self.assertEqual(interface.type, 'copper')
            self.assertIn(int(portnumber),portrange)
            self.assertTrue(interface.fullname)
            self.assertIn(interface.portnumber,portrange)
        self.assertTrue(s.blades[0].interfaces['3'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['5'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['6'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['17'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['18'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['19'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['21'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['22'].InBcastPkts)

        #test assignment of CDP Neighbor
        self.assertIsInstance(s.cdpneighbors, list)
        self.assertEqual(len(s.cdpneighbors), 1)
        self.assertIsInstance(s.cdpneighbors[0], Neighbor)
        self.assertEqual(s.cdpneighbors[0].deviceid, 'dcx1-ddc-d11.net.utah.edu(FOX1530G7M4)')
        self.assertEqual(str(s.cdpneighbors[0].ip), '172.28.65.64')
        self.assertIsInstance(s.cdpneighbors[0].ip, ipaddress.IPv4Address)
        self.assertEqual(s.cdpneighbors[0].platform, 'N5K-C5596UP')
        self.assertIsInstance(s.cdpneighbors[0].interface, Interface)
        self.assertEqual(s.cdpneighbors[0].interface.fullname, 'GigabitEthernet0/21')
        self.assertIsInstance(s.cdpneighbors[0].interface, Interface)
        self.assertEqual(s.cdpneighbors[0].interface.portnumber, 21)
        self.assertEqual(s.cdpneighbors[0].duplex, 'full')

        self.assertEqual(s.chassis, None)
        self.assertEqual(s.defaultgateway, '172.20.71.65')
        self.assertEqual(s.hostname, 'scx1-ddc-d11')
        self.assertEqual(s.ip, '172.20.71.105')
        self.assertEqual(s.lastrestart, None)

        #logging Info
        logging = ['155.100.122.16','155.98.253.244','155.98.204.52','172.24.29.14','10.70.24.10']
        for log in s.logging_data:
            self.assertIn(str(log[1]),logging)
            self.assertIsInstance(log[1],ipaddress.IPv4Address)

        #check vlans
        self.assertEqual(len(s.vlans),8)
        self.assertEqual(s.vlans[0].name, 'ACS-CSI-Mgmt')
        self.assertEqual(s.vlans[0].number, 418)
        self.assertEqual(s.vlans[1].name, 'ServerMgt')
        self.assertEqual(s.vlans[1].number, 423)
        self.assertEqual(s.vlans[2].name, 'dc-idsystems-security-inside')
        self.assertEqual(s.vlans[2].number, 501)
        for macaddress in s.vlans[2].mac_addresses:
            self.assertIsInstance(macaddress,EUI)
        self.assertEqual(s.vlans[3].name, 'dc-ucard-camera-sys')
        self.assertEqual(s.vlans[3].number, 564)
        self.assertEqual(s.vlans[4].name, 'dc-payforprint-sys')
        self.assertEqual(s.vlans[4].number, 592)
        self.assertEqual(s.vlans[5].name, 'komas-mgmt-2960')
        self.assertEqual(s.vlans[5].number, 672)
        self.assertEqual(s.vlans[6].name, 'uu-acs-679')
        self.assertEqual(s.vlans[6].number, 679)
        self.assertEqual(s.vlans[7].name, 'mframe')
        self.assertEqual(s.vlans[7].number, 682)

        #test tacacs configuration
        self.assertIsInstance(s.tacacs, list)
        self.assertEqual(len(s.tacacs),2)
        self.assertIsInstance(s.tacacs[0], TACACS)
        self.assertIsInstance(s.tacacs[0].server, ipaddress.IPv4Address)
        self.assertEqual(str(s.tacacs[0].server),'172.31.17.180')
        self.assertIsInstance(s.tacacs[1].server, ipaddress.IPv4Address)
        self.assertEqual(str(s.tacacs[1].server), '10.64.32.5')

    def test_Nexus_3064T(self):
        """
        Model:WS-C3560X-48P
        Software Version: 12.2(53)SE2
        """
        s = Switch(ipaddress='172.31.7.151')
        s.login()
        s.getSwitchInfo()

        # test getting the information properly
        self.assertNotIn("Invalid input detected at", s.version_result)
        self.assertNotIn("Invalid input detected at", s.run_result)
        self.assertNotIn("Invalid input detected at", s.interface_result)
        self.assertIn("Invalid command (interface name) at", s.portdowntime_result)
        self.assertNotIn("Invalid input detected at", s.inv_result)
        self.assertNotIn("Invalid input detected at", s.portcount_result)
        self.assertNotIn("Invalid input detected at", s.cdpnei_result)
        self.assertIn("Invalid number at", s.module_result)
        self.assertNotIn("Invalid input detected at", s.snmp_result)
        self.assertNotIn("Invalid input detected at", s.logging_data_result)
        self.assertNotIn("Invalid input detected at", s.tacacs_result)
        self.assertNotIn("Invalid input detected at", s.mac_address_result)
        self.assertNotIn("Invalid input detected at", s.acl_result)

        # Test the assigning of information to the correct objects
        s.assignattributes()

        # test global Variables
        self.assertEqual(s.bannername, 'sx1-521-ac141c')
        self.assertEqual(s.buildnumber, '0521')
        self.assertEqual(s.buildingname, 'SOM')
        self.assertEqual(s.roomnumber, 'AC141C')
        self.assertEqual(s.description, 'Sub Access Layer Switch')
        self.assertEqual(s.IPAddress, '172.20.66.109')
        self.assertEqual(s.portcount, 54)
        self.assertEqual(s.serial[0], 'FDO1424P1BT')
        self.assertEqual(s.subnetmask, '255.255.254.0')
        self.assertNotEqual(s.uptime, None)
        self.assertEqual(s.chassis, None)
        self.assertEqual(s.defaultgateway, '172.20.66.1')
        self.assertEqual(s.hostname, 'SX1-521SOM-AC141C')
        self.assertEqual(s.ip, '172.20.66.109')
        self.assertEqual(s.lastrestart, None)

        # test the assignment of ACL object properties
        self.assertEqual(len(s.access_lists), 3)
        self.assertIn(199, s.access_lists.numbers)
        self.assertIn(70, s.access_lists.numbers)
        self.assertIn(71, s.access_lists.numbers)
        for aclobj in s.access_lists.standard_ip_lists:
            self.assertIsInstance(aclobj, ACL)
            self.assertIsInstance(aclobj.Entries, list)
            for entry in aclobj.Entries:
                self.assertIsInstance(entry, ACL_Entry)
                self.assertTrue(entry.type)
                self.assertTrue(entry.number)
            self.assertTrue(aclobj.Entries)
            self.assertTrue(aclobj.type)

        # test the assignment of the SNMP Value
        self.assertIsInstance(s.SNMP, SNMP)
        self.assertIsInstance(s.SNMP.communities, list)
        self.assertIsInstance(s.SNMP.traps, list)
        self.assertIsInstance(s.SNMP.traps, list)
        self.assertIsInstance(s.SNMP.version, set)
        self.assertTrue(s.SNMP.communities)
        self.assertEqual(len(s.SNMP.communities), 8)
        for communities in s.SNMP.communities:
            self.assertIsInstance(communities, SNMP_community)
            self.assertTrue(communities.raw_data)
            self.assertTrue(communities.string)

        self.assertEqual(len(s.SNMP.contacts), 1)
        self.assertEqual(s.SNMP.contacts[0].bc, 'barcode:122256')
        self.assertEqual(s.SNMP.contacts[0].serial, None)
        self.assertEqual(s.SNMP.contacts[0].tag, 'RT:297828')
        for contact in s.SNMP.contacts:
            self.assertIsInstance(contact, SNMP_contact)
            self.assertIsInstance(contact.bc, str)
        self.assertTrue(s.SNMP.traps)
        self.assertEqual(len(s.SNMP.traps), 14)
        self.assertTrue(s.SNMP.version)
        self.assertTrue(s.SNMP.loggingips)
        test = ['155.100.122.152', '155.100.122.113','155.98.253.148','155.98.253.149']
        for log in s.SNMP.loggingips:
            self.assertIsInstance(log,IPv4Address)
            self.assertIn(str(log),test)
        self.assertIn(2, s.SNMP.version)
        self.assertNotIn(3, s.SNMP.version)

        # check the blades configuration
        self.assertTrue(s.blades)
        self.assertEqual(len(s.blades), 1)
        self.assertEqual(s.blades[0].ISOversion, '12.2(53)SE2')
        self.assertFalse(s.blades[0].SUP)
        self.assertEqual(s.blades[0].modelnumber, 'WS-C3560X-48P')
        self.assertEqual(s.blades[0].portcount, 54)
        self.assertTrue(s.blades[0].interfaces)
        self.assertEqual(len(s.blades[0].interfaces), 48)
        portrange = range(1, 49)
        for portnumber, interface in s.blades[0].interfaces.items():
            self.assertTrue(interface)
            self.assertIsInstance(interface.mac_addresses, list)
            if interface.mac_addresses:
                for macaddress in interface.mac_addresses:
                    self.assertIsInstance(macaddress, EUI)
            self.assertIsInstance(interface, Interface)
            self.assertEqual(interface.type, 'copper')
            self.assertIn(int(portnumber), portrange)
            self.assertTrue(interface.fullname)
            self.assertIn(interface.portnumber, portrange)
        for portnumber, interface in s.blades[0].moduleinterfaces.items():
            self.assertTrue(interface)
            self.assertIsInstance(interface.mac_addresses, list)
            if interface.mac_addresses:
                for macaddress in interface.mac_addresses:
                    self.assertIsInstance(macaddress, EUI)
            self.assertIsInstance(interface, Interface)
            self.assertTrue(interface.fullname)
            self.assertIn(interface.portnumber, portrange)
        self.assertTrue(s.blades[0].moduleinterfaces['GigabitEthernet1/1'].InBcastPkts)
        self.assertFalse(s.blades[0].moduleinterfaces['GigabitEthernet1/2'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['1'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['2'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['3'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['4'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['5'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['6'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['7'].InBcastPkts)
        self.assertFalse(s.blades[0].interfaces['8'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['9'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['10'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['11'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['12'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['13'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['14'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['15'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['16'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['17'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['18'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['19'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['20'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['21'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['22'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['23'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['24'].InBcastPkts)

        # test assignment of CDP Neighbor
        self.assertIsInstance(s.cdpneighbors, list)
        self.assertEqual(len(s.cdpneighbors), 4)
        for neighbor in s.cdpneighbors:
            self.assertIsInstance(neighbor, Neighbor)
            self.assertIsInstance(neighbor.ip, ipaddress.IPv4Address)
            self.assertIsInstance(neighbor.interface, Interface)
        self.assertEqual(s.cdpneighbors[0].deviceid, 'dx1-521-bc001.net.utah.edu')
        self.assertEqual(str(s.cdpneighbors[0].ip), '172.20.66.4')
        self.assertEqual(s.cdpneighbors[0].platform, 'ciscoWS-C4510R+E')
        self.assertEqual(s.cdpneighbors[0].interface.fullname, 'GigabitEthernet0/1')
        self.assertEqual(s.cdpneighbors[0].interface.portnumber, 1)
        self.assertEqual(s.cdpneighbors[0].duplex, 'full')

        # logging Info
        logging = ['155.98.253.244', '155.98.204.52', '172.24.29.14', '10.70.24.10']
        for log in s.logging_data:
            self.assertIn(str(log[1]), logging)
            self.assertIsInstance(log[1], ipaddress.IPv4Address)

        # check vlans
        self.assertEqual(len(s.vlans), 7)
        self.assertEqual(s.vlans[0].name, '521SOM-fl1-zeroclients')
        self.assertEqual(s.vlans[0].number, 110)
        self.assertEqual(s.vlans[1].name, '521-mgmt')
        self.assertEqual(s.vlans[1].number, 333)
        self.assertEqual(s.vlans[2].name, 'bldg-521-printer')
        self.assertEqual(s.vlans[2].number, 398)
        for macaddress in s.vlans[2].mac_addresses:
            self.assertIsInstance(macaddress, EUI)

        # test tacacs configuration
        self.assertIsInstance(s.tacacs, list)
        self.assertEqual(len(s.tacacs), 2)
        self.assertIsInstance(s.tacacs[0], TACACS)
        self.assertIsInstance(s.tacacs[0].server, ipaddress.IPv4Address)
        self.assertEqual(str(s.tacacs[0].server), '172.31.17.180')
        self.assertIsInstance(s.tacacs[1].server, ipaddress.IPv4Address)
        self.assertEqual(str(s.tacacs[1].server), '10.64.32.5')

    def test_Catalyst_3560X_24_PoE(self):
        """
        dx1-619honors
        Model: WS-C3560X-24P
        Software Version: 12.2(55)SE3
        """
        s = Switch(ipaddress="155.97.253.188")
        s.login()
        s.getSwitchInfo()

        # test getting the information properly
        self.assertNotIn("Invalid input detected at", s.version_result)
        self.assertNotIn("Invalid input detected at", s.run_result)
        self.assertIn("Invalid input detected at", s.interface_result)
        self.assertNotIn("Invalid input detected at", s.interface_name_r)
        self.assertIn("Invalid input detected at", s.portdowntime_result)
        self.assertNotIn("Invalid input detected at", s.portdowntime_result_in)
        self.assertNotIn("Invalid input detected at", s.inv_result)
        self.assertNotIn("Invalid input detected at", s.portcount_result)
        self.assertNotIn("Invalid input detected at", s.cdpnei_result)
        self.assertIn("Invalid input detected at", s.module_result)
        self.assertIn("Invalid input detected at", s.snmp_result)
        self.assertNotIn("Invalid input detected at", s.snmp_result_in)
        self.assertNotIn("Invalid input detected at", s.logging_data_result)
        self.assertIn("Invalid input detected at", s.tacacs_result)
        self.assertNotIn("Invalid input detected at", s.tacacs_result_in)
        self.assertNotIn("Invalid input detected at", s.mac_address_result)
        self.assertNotIn("Invalid input detected at", s.acl_result)


        # Test the assigning of information to the correct objects
        s.assignattributes()

        # test global Variables
        self.assertEqual(s.bannername, 'DX1-619honors')
        self.assertEqual(s.buildnumber, '0619')
        self.assertEqual(s.buildingname, 'honors')
        self.assertEqual(s.racknumber, None)
        self.assertEqual(s.description, 'Demarc (Access Layer Switch)')
        self.assertEqual(s.IPAddress, '155.97.253.188')
        self.assertEqual(s.portcount, 30)
        self.assertEqual(s.serial[0], 'FDO1522V0BF')
        self.assertEqual(s.subnetmask, '255.255.255.248')
        self.assertNotEqual(s.uptime, None)
        self.assertEqual(s.chassis, None)
        self.assertEqual(s.defaultgateway, '155.97.253.185')
        self.assertEqual(s.hostname, 'dx1-619honors')
        self.assertEqual(s.ip, '155.97.253.188')
        self.assertEqual(s.lastrestart, None)

        # test the assignment of ACL object properties
        self.assertEqual(len(s.access_lists), 4)
        self.assertIn(199, s.access_lists.numbers)
        self.assertIn(70, s.access_lists.numbers)
        self.assertIn(71, s.access_lists.numbers)
        self.assertIn(1, s.access_lists.numbers)
        for aclobj in s.access_lists.standard_ip_lists:
            self.assertIsInstance(aclobj, ACL)
            self.assertIsInstance(aclobj.Entries, list)
            for entry in aclobj.Entries:
                self.assertIsInstance(entry, ACL_Entry)
                self.assertTrue(entry.type)
                self.assertTrue(entry.number)
            self.assertTrue(aclobj.Entries)
            self.assertTrue(aclobj.type)

        # test the assignment of the SNMP Value
        self.assertIsInstance(s.SNMP, SNMP)
        self.assertIsInstance(s.SNMP.communities, list)
        self.assertIsInstance(s.SNMP.traps, list)
        self.assertIsInstance(s.SNMP.traps, list)
        self.assertIsInstance(s.SNMP.version, set)
        self.assertTrue(s.SNMP.communities)
        self.assertEqual(len(s.SNMP.communities), 6)
        for communities in s.SNMP.communities:
            self.assertIsInstance(communities, SNMP_community)
            self.assertTrue(communities.raw_data)
            self.assertTrue(communities.string)
        self.assertFalse(s.SNMP.traps)
        self.assertEqual(len(s.SNMP.traps), 0)
        self.assertTrue(s.SNMP.version)
        self.assertFalse(s.SNMP.loggingips)
        self.assertIn(2, s.SNMP.version)
        self.assertNotIn(3, s.SNMP.version)

        # check the blades configuration
        self.assertTrue(s.blades)
        self.assertEqual(len(s.blades), 1)
        self.assertEqual(s.blades[0].ISOversion, '12.2(55)SE3')
        self.assertFalse(s.blades[0].SUP)
        self.assertEqual(s.blades[0].modelnumber, 'WS-C3560X-24P')
        self.assertEqual(s.blades[0].portcount, 30)
        self.assertTrue(s.blades[0].interfaces)
        self.assertEqual(len(s.blades[0].interfaces), 24)
        portrange = range(1, 25)
        for portnumber, interface in s.blades[0].interfaces.items():
            self.assertTrue(interface)
            self.assertIsInstance(interface.mac_addresses, list)
            if interface.mac_addresses:
                for macaddress in interface.mac_addresses:
                    self.assertIsInstance(macaddress, EUI)
            self.assertIsInstance(interface, Interface)
            self.assertEqual(interface.type, 'copper')
            self.assertIn(int(portnumber), portrange)
            self.assertTrue(interface.fullname)
            self.assertIn(interface.portnumber, portrange)
        for portnumber, interface in s.blades[0].moduleinterfaces.items():
            self.assertTrue(interface)
            self.assertIsInstance(interface.mac_addresses, list)
            if interface.mac_addresses:
                for macaddress in interface.mac_addresses:
                    self.assertIsInstance(macaddress, EUI)
            self.assertIsInstance(interface, Interface)
            self.assertTrue(interface.fullname)
            self.assertIn(interface.portnumber, portrange)
        self.assertTrue(s.blades[0].moduleinterfaces['GigabitEthernet1/1'].InBcastPkts)
        self.assertTrue(s.blades[0].moduleinterfaces['GigabitEthernet1/2'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['1'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['2'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['3'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['4'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['5'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['6'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['7'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['8'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['9'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['10'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['11'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['12'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['13'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['14'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['15'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['16'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['17'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['18'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['19'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['20'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['21'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['22'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['23'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['24'].InBcastPkts)

        # test assignment of CDP Neighbor
        self.assertIsInstance(s.cdpneighbors, list)
        self.assertEqual(len(s.cdpneighbors), 7)
        for neighbor in s.cdpneighbors:
            self.assertIsInstance(neighbor, Neighbor)
            self.assertIsInstance(neighbor.ip, ipaddress.IPv4Address)
            self.assertIsInstance(neighbor.interface, Interface)
        self.assertEqual(s.cdpneighbors[0].deviceid, 'ap-0619-0-office')
        self.assertEqual(str(s.cdpneighbors[0].ip), '155.97.210.200')
        self.assertEqual(s.cdpneighbors[0].platform, 'ciscoAIR-CAP3702I-A-K9')
        self.assertEqual(s.cdpneighbors[0].interface.fullname, 'GigabitEthernet0/4')
        self.assertEqual(s.cdpneighbors[0].interface.portnumber, 4)
        self.assertEqual(s.cdpneighbors[0].duplex, 'full')

        # logging Info
        logging = ['155.98.253.244', '155.98.204.52', '172.24.29.14', '10.70.24.10']
        for log in s.logging_data:
            self.assertIn(str(log[1]), logging)
            self.assertIsInstance(log[1], ipaddress.IPv4Address)

        # check vlans
        self.assertEqual(len(s.vlans), 6)
        self.assertEqual(s.vlans[0].name, 'fort-619honors')
        self.assertEqual(s.vlans[0].number, 504)
        self.assertEqual(s.vlans[1].name, 'fort-619honors-ehs')
        self.assertEqual(s.vlans[1].number, 722)
        self.assertEqual(s.vlans[2].name, 'fort-619honors-m')
        self.assertEqual(s.vlans[2].number, 823)
        for macaddress in s.vlans[2].mac_addresses:
            self.assertIsInstance(macaddress, EUI)
        self.assertEqual(s.vlans[3].name, 'fort-650honors-fm-cam')
        self.assertEqual(s.vlans[3].number, 1627)
        self.assertEqual(s.vlans[4].name, 'fort-619honors-voip')
        self.assertEqual(s.vlans[4].number, 200)
        self.assertEqual(s.vlans[5].name, 'fort-619honors-wireless')
        self.assertEqual(s.vlans[5].number, 429)


        # test tacacs configuration
        self.assertIsInstance(s.tacacs, list)
        self.assertEqual(len(s.tacacs), 2)
        self.assertIsInstance(s.tacacs[0], TACACS)
        self.assertIsInstance(s.tacacs[0].server, ipaddress.IPv4Address)
        self.assertEqual(str(s.tacacs[0].server), '172.31.17.180')
        self.assertIsInstance(s.tacacs[1].server, ipaddress.IPv4Address)
        self.assertEqual(str(s.tacacs[1].server), '10.64.32.5')

    def test_Catalyst_3560X_48_PoE(self):
        """
        Model:WS-C3560X-48P
        Software Version: 12.2(53)SE2
        """
        s = Switch(ipaddress="172.20.66.109")
        s.login()
        s.getSwitchInfo()

        # test getting the information properly
        self.assertNotIn("Invalid input detected at", s.version_result)
        self.assertNotIn("Invalid input detected at", s.run_result)
        self.assertIn("Invalid input detected at", s.interface_result)
        self.assertNotIn("Invalid input detected at", s.interface_name_r)
        self.assertIn("Invalid input detected at", s.portdowntime_result)
        self.assertNotIn("Invalid input detected at", s.portdowntime_result_in)
        self.assertNotIn("Invalid input detected at", s.inv_result)
        self.assertNotIn("Invalid input detected at", s.portcount_result)
        self.assertNotIn("Invalid input detected at", s.cdpnei_result)
        self.assertIn("Invalid input detected at", s.module_result)
        self.assertIn("Invalid input detected at", s.snmp_result)
        self.assertNotIn("Invalid input detected at", s.snmp_result_in)
        self.assertNotIn("Invalid input detected at", s.logging_data_result)
        self.assertIn("Invalid input detected at", s.tacacs_result)
        self.assertNotIn("Invalid input detected at", s.tacacs_result_in)
        self.assertNotIn("Invalid input detected at", s.mac_address_result)
        self.assertNotIn("Invalid input detected at", s.acl_result)

        # Test the assigning of information to the correct objects
        s.assignattributes()

        # test global Variables
        self.assertEqual(s.bannername, 'sx1-521-ac141c')
        self.assertEqual(s.buildnumber, '0521')
        self.assertEqual(s.buildingname, 'SOM')
        self.assertEqual(s.roomnumber, 'AC141C')
        self.assertEqual(s.description, 'Sub Access Layer Switch')
        self.assertEqual(s.IPAddress, '172.20.66.109')
        self.assertEqual(s.portcount, 54)
        self.assertEqual(s.serial[0], 'FDO1424P1BT')
        self.assertEqual(s.subnetmask, '255.255.254.0')
        self.assertNotEqual(s.uptime, None)
        self.assertEqual(s.chassis, None)
        self.assertEqual(s.defaultgateway, '172.20.66.1')
        self.assertEqual(s.hostname, 'SX1-521SOM-AC141C')
        self.assertEqual(s.ip, '172.20.66.109')
        self.assertEqual(s.lastrestart, None)

        # test the assignment of ACL object properties
        self.assertEqual(len(s.access_lists), 3)
        self.assertIn(199, s.access_lists.numbers)
        self.assertIn(70, s.access_lists.numbers)
        self.assertIn(71, s.access_lists.numbers)
        for aclobj in s.access_lists.standard_ip_lists:
            self.assertIsInstance(aclobj, ACL)
            self.assertIsInstance(aclobj.Entries, list)
            for entry in aclobj.Entries:
                self.assertIsInstance(entry, ACL_Entry)
                self.assertTrue(entry.type)
                self.assertTrue(entry.number)
            self.assertTrue(aclobj.Entries)
            self.assertTrue(aclobj.type)

        # test the assignment of the SNMP Value
        self.assertIsInstance(s.SNMP, SNMP)
        self.assertIsInstance(s.SNMP.communities, list)
        self.assertIsInstance(s.SNMP.traps, list)
        self.assertIsInstance(s.SNMP.traps, list)
        self.assertIsInstance(s.SNMP.version, set)
        self.assertTrue(s.SNMP.communities)
        self.assertEqual(len(s.SNMP.communities), 8)
        for communities in s.SNMP.communities:
            self.assertIsInstance(communities, SNMP_community)
            self.assertTrue(communities.raw_data)
            self.assertTrue(communities.string)

        self.assertEqual(len(s.SNMP.contacts), 1)
        self.assertEqual(s.SNMP.contacts[0].bc, 'barcode:122256')
        self.assertEqual(s.SNMP.contacts[0].serial, None)
        self.assertEqual(s.SNMP.contacts[0].tag, 'RT:297828')
        for contact in s.SNMP.contacts:
            self.assertIsInstance(contact, SNMP_contact)
            self.assertIsInstance(contact.bc, str)
        self.assertTrue(s.SNMP.traps)
        self.assertEqual(len(s.SNMP.traps), 14)
        self.assertTrue(s.SNMP.version)
        self.assertTrue(s.SNMP.loggingips)
        test = ['155.100.122.152', '155.100.122.113','155.98.253.148','155.98.253.149']
        for log in s.SNMP.loggingips:
            self.assertIsInstance(log,IPv4Address)
            self.assertIn(str(log),test)
        self.assertIn(2, s.SNMP.version)
        self.assertNotIn(3, s.SNMP.version)

        # check the blades configuration
        self.assertTrue(s.blades)
        self.assertEqual(len(s.blades), 1)
        self.assertEqual(s.blades[0].ISOversion, '12.2(53)SE2')
        self.assertFalse(s.blades[0].SUP)
        self.assertEqual(s.blades[0].modelnumber, 'WS-C3560X-48P')
        self.assertEqual(s.blades[0].portcount, 54)
        self.assertTrue(s.blades[0].interfaces)
        self.assertEqual(len(s.blades[0].interfaces), 48)
        portrange = range(1, 49)
        for portnumber, interface in s.blades[0].interfaces.items():
            self.assertTrue(interface)
            self.assertIsInstance(interface.mac_addresses, list)
            if interface.mac_addresses:
                for macaddress in interface.mac_addresses:
                    self.assertIsInstance(macaddress, EUI)
            self.assertIsInstance(interface, Interface)
            self.assertEqual(interface.type, 'copper')
            self.assertIn(int(portnumber), portrange)
            self.assertTrue(interface.fullname)
            self.assertIn(interface.portnumber, portrange)
        for portnumber, interface in s.blades[0].moduleinterfaces.items():
            self.assertTrue(interface)
            self.assertIsInstance(interface.mac_addresses, list)
            if interface.mac_addresses:
                for macaddress in interface.mac_addresses:
                    self.assertIsInstance(macaddress, EUI)
            self.assertIsInstance(interface, Interface)
            self.assertTrue(interface.fullname)
            self.assertIn(interface.portnumber, portrange)
        self.assertTrue(s.blades[0].moduleinterfaces['GigabitEthernet1/1'].InBcastPkts)
        self.assertFalse(s.blades[0].moduleinterfaces['GigabitEthernet1/2'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['1'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['2'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['3'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['4'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['5'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['6'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['7'].InBcastPkts)
        self.assertFalse(s.blades[0].interfaces['8'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['9'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['10'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['11'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['12'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['13'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['14'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['15'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['16'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['17'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['18'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['19'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['20'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['21'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['22'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['23'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['24'].InBcastPkts)

        # test assignment of CDP Neighbor
        self.assertIsInstance(s.cdpneighbors, list)
        self.assertEqual(len(s.cdpneighbors), 4)
        for neighbor in s.cdpneighbors:
            self.assertIsInstance(neighbor, Neighbor)
            self.assertIsInstance(neighbor.ip, ipaddress.IPv4Address)
            self.assertIsInstance(neighbor.interface, Interface)
        self.assertEqual(s.cdpneighbors[0].deviceid, 'dx1-521-bc001.net.utah.edu')
        self.assertEqual(str(s.cdpneighbors[0].ip), '172.20.66.4')
        self.assertEqual(s.cdpneighbors[0].platform, 'ciscoWS-C4510R+E')
        self.assertEqual(s.cdpneighbors[0].interface.fullname, 'GigabitEthernet0/1')
        self.assertEqual(s.cdpneighbors[0].interface.portnumber, 1)
        self.assertEqual(s.cdpneighbors[0].duplex, 'full')

        # logging Info
        logging = ['155.98.253.244', '155.98.204.52', '172.24.29.14', '10.70.24.10']
        for log in s.logging_data:
            self.assertIn(str(log[1]), logging)
            self.assertIsInstance(log[1], ipaddress.IPv4Address)

        # check vlans
        self.assertEqual(len(s.vlans), 7)
        self.assertEqual(s.vlans[0].name, '521SOM-fl1-zeroclients')
        self.assertEqual(s.vlans[0].number, 110)
        self.assertEqual(s.vlans[1].name, '521-mgmt')
        self.assertEqual(s.vlans[1].number, 333)
        self.assertEqual(s.vlans[2].name, 'bldg-521-printer')
        self.assertEqual(s.vlans[2].number, 398)
        for macaddress in s.vlans[2].mac_addresses:
            self.assertIsInstance(macaddress, EUI)

        # test tacacs configuration
        self.assertIsInstance(s.tacacs, list)
        self.assertEqual(len(s.tacacs), 2)
        self.assertIsInstance(s.tacacs[0], TACACS)
        self.assertIsInstance(s.tacacs[0].server, ipaddress.IPv4Address)
        self.assertEqual(str(s.tacacs[0].server), '172.31.17.180')
        self.assertIsInstance(s.tacacs[1].server, ipaddress.IPv4Address)
        self.assertEqual(str(s.tacacs[1].server), '10.64.32.5')

    def Cisco_Catalyst_3650_24TD(self):
        pass
        s = Switch(ipaddress="172.20.66.109")
        s.login()
        s.getSwitchInfo()

        # test getting the information properly
        self.assertNotIn("Invalid input detected at", s.version_result)
        self.assertNotIn("Invalid input detected at", s.run_result)
        self.assertIn("Invalid input detected at", s.interface_result)
        self.assertNotIn("Invalid input detected at", s.interface_name_r)
        self.assertIn("Invalid input detected at", s.portdowntime_result)
        self.assertNotIn("Invalid input detected at", s.portdowntime_result_in)
        self.assertNotIn("Invalid input detected at", s.inv_result)
        self.assertNotIn("Invalid input detected at", s.portcount_result)
        self.assertNotIn("Invalid input detected at", s.cdpnei_result)
        self.assertIn("Invalid input detected at", s.module_result)
        self.assertIn("Invalid input detected at", s.snmp_result)
        self.assertNotIn("Invalid input detected at", s.snmp_result_in)
        self.assertNotIn("Invalid input detected at", s.logging_data_result)
        self.assertIn("Invalid input detected at", s.tacacs_result)
        self.assertNotIn("Invalid input detected at", s.tacacs_result_in)
        self.assertNotIn("Invalid input detected at", s.mac_address_result)
        self.assertNotIn("Invalid input detected at", s.acl_result)

        # Test the assigning of information to the correct objects
        s.assignattributes()

        # test global Variables
        self.assertEqual(s.bannername, 'sx1-521-ac141c')
        self.assertEqual(s.buildnumber, '0521')
        self.assertEqual(s.buildingname, 'SOM')
        self.assertEqual(s.roomnumber, 'AC141C')
        self.assertEqual(s.description, 'Sub Access Layer Switch')
        self.assertEqual(s.IPAddress, '172.20.66.109')
        self.assertEqual(s.portcount, 54)
        self.assertEqual(s.serial[0], 'FDO1424P1BT')
        self.assertEqual(s.subnetmask, '255.255.254.0')
        self.assertNotEqual(s.uptime, None)
        self.assertEqual(s.chassis, None)
        self.assertEqual(s.defaultgateway, '172.20.66.1')
        self.assertEqual(s.hostname, 'SX1-521SOM-AC141C')
        self.assertEqual(s.ip, '172.20.66.109')
        self.assertEqual(s.lastrestart, None)

        # test the assignment of ACL object properties
        self.assertEqual(len(s.access_lists), 3)
        self.assertIn(199, s.access_lists.numbers)
        self.assertIn(70, s.access_lists.numbers)
        self.assertIn(71, s.access_lists.numbers)
        for aclobj in s.access_lists.standard_lists:
            self.assertIsInstance(aclobj, ACL)
            self.assertIsInstance(aclobj.Entries, list)
            for entry in aclobj.Entries:
                self.assertIsInstance(entry, ACL_Entry)
                self.assertTrue(entry.type)
                self.assertTrue(entry.number)
            self.assertTrue(aclobj.Entries)
            self.assertTrue(aclobj.type)

        # test the assignment of the SNMP Value
        self.assertIsInstance(s.SNMP, SNMP)
        self.assertIsInstance(s.SNMP.communities, list)
        self.assertIsInstance(s.SNMP.traps, list)
        self.assertIsInstance(s.SNMP.traps, list)
        self.assertIsInstance(s.SNMP.version, set)
        self.assertTrue(s.SNMP.communities)
        self.assertEqual(len(s.SNMP.communities), 8)
        for communities in s.SNMP.communities:
            self.assertIsInstance(communities, SNMP_community)
            self.assertTrue(communities.raw_data)
            self.assertTrue(communities.string)

        self.assertEqual(len(s.SNMP.contacts), 1)
        self.assertEqual(s.SNMP.contacts[0].bc, 'barcode:122256')
        self.assertEqual(s.SNMP.contacts[0].serial, None)
        self.assertEqual(s.SNMP.contacts[0].tag, 'RT:297828')
        for contact in s.SNMP.contacts:
            self.assertIsInstance(contact, SNMP_contact)
            self.assertIsInstance(contact.bc, str)
        self.assertTrue(s.SNMP.traps)
        self.assertEqual(len(s.SNMP.traps), 14)
        self.assertTrue(s.SNMP.version)
        self.assertTrue(s.SNMP.loggingips)
        test = ['155.100.122.152', '155.100.122.113', '155.98.253.148', '155.98.253.149']
        for log in s.SNMP.loggingips:
            self.assertIsInstance(log, IPv4Address)
            self.assertIn(str(log), test)
        self.assertIn(2, s.SNMP.version)
        self.assertNotIn(3, s.SNMP.version)

        # check the blades configuration
        self.assertTrue(s.blades)
        self.assertEqual(len(s.blades), 1)
        self.assertEqual(s.blades[0].ISOversion, '12.2(53)SE2')
        self.assertFalse(s.blades[0].SUP)
        self.assertEqual(s.blades[0].modelnumber, 'WS-C3560X-48P')
        self.assertEqual(s.blades[0].portcount, 54)
        self.assertTrue(s.blades[0].interfaces)
        self.assertEqual(len(s.blades[0].interfaces), 48)
        portrange = range(1, 49)
        for portnumber, interface in s.blades[0].interfaces.items():
            self.assertTrue(interface)
            self.assertIsInstance(interface.mac_addresses, list)
            if interface.mac_addresses:
                for macaddress in interface.mac_addresses:
                    self.assertIsInstance(macaddress, EUI)
            self.assertIsInstance(interface, Interface)
            self.assertEqual(interface.type, 'copper')
            self.assertIn(int(portnumber), portrange)
            self.assertTrue(interface.fullname)
            self.assertIn(interface.portnumber, portrange)
        for portnumber, interface in s.blades[0].moduleinterfaces.items():
            self.assertTrue(interface)
            self.assertIsInstance(interface.mac_addresses, list)
            if interface.mac_addresses:
                for macaddress in interface.mac_addresses:
                    self.assertIsInstance(macaddress, EUI)
            self.assertIsInstance(interface, Interface)
            self.assertTrue(interface.fullname)
            self.assertIn(interface.portnumber, portrange)
        self.assertTrue(s.blades[0].moduleinterfaces['GigabitEthernet1/1'].InBcastPkts)
        self.assertFalse(s.blades[0].moduleinterfaces['GigabitEthernet1/2'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['1'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['2'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['3'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['4'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['5'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['6'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['7'].InBcastPkts)
        self.assertFalse(s.blades[0].interfaces['8'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['9'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['10'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['11'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['12'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['13'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['14'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['15'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['16'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['17'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['18'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['19'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['20'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['21'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['22'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['23'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['24'].InBcastPkts)

        # test assignment of CDP Neighbor
        self.assertIsInstance(s.cdpneighbors, list)
        self.assertEqual(len(s.cdpneighbors), 4)
        for neighbor in s.cdpneighbors:
            self.assertIsInstance(neighbor, Neighbor)
            self.assertIsInstance(neighbor.ip, ipaddress.IPv4Address)
            self.assertIsInstance(neighbor.interface, Interface)
        self.assertEqual(s.cdpneighbors[0].deviceid, 'dx1-521-bc001.net.utah.edu')
        self.assertEqual(str(s.cdpneighbors[0].ip), '172.20.66.4')
        self.assertEqual(s.cdpneighbors[0].platform, 'ciscoWS-C4510R+E')
        self.assertEqual(s.cdpneighbors[0].interface.fullname, 'GigabitEthernet0/1')
        self.assertEqual(s.cdpneighbors[0].interface.portnumber, 1)
        self.assertEqual(s.cdpneighbors[0].duplex, 'full')

        # logging Info
        logging = ['155.98.253.244', '155.98.204.52', '172.24.29.14', '10.70.24.10']
        for log in s.logging_data:
            self.assertIn(str(log[1]), logging)
            self.assertIsInstance(log[1], ipaddress.IPv4Address)

        # check vlans
        self.assertEqual(len(s.vlans), 7)
        self.assertEqual(s.vlans[0].name, '521SOM-fl1-zeroclients')
        self.assertEqual(s.vlans[0].number, 110)
        self.assertEqual(s.vlans[1].name, '521-mgmt')
        self.assertEqual(s.vlans[1].number, 333)
        self.assertEqual(s.vlans[2].name, 'bldg-521-printer')
        self.assertEqual(s.vlans[2].number, 398)
        for macaddress in s.vlans[2].mac_addresses:
            self.assertIsInstance(macaddress, EUI)

        # test tacacs configuration
        self.assertIsInstance(s.tacacs, list)
        self.assertEqual(len(s.tacacs), 2)
        self.assertIsInstance(s.tacacs[0], TACACS)
        self.assertIsInstance(s.tacacs[0].server, ipaddress.IPv4Address)
        self.assertEqual(str(s.tacacs[0].server), '172.31.17.180')
        self.assertIsInstance(s.tacacs[1].server, ipaddress.IPv4Address)
        self.assertEqual(str(s.tacacs[1].server), '10.64.32.5')

    def Cisco_Catalyst_3650_48PD(self):
        pass
        # s = Switch(ipaddress="")
        # s.login()
        # s.getSwitchInfo()
        #
        #
        # #test getting the information properly
        # self.assertEqual(s.version_result,)
        # self.assertEqual(s.run_result,)
        # self.assertEqual(s.interface_result,)
        # self.assertEqual(s.interface_name_r,)
        # self.assertEqual(s.portdowntime_result),
        # self.assertEqual(s.inv_result,)
        # self.assertEqual(s.portcount_result,)
        # self.assertEqual(s.cdpnei_result,)
        # self.assertEqual(s.module_result,)
        # self.assertEqual(s.snmp_result,)
        # self.assertEqual(s.logging_data_result,)
        #
        # #Test the assigning of information to the correct objects
        # s.assignattributes()
        #
        # self.assertEqual(s.switchdescription, )
        # self.assertEqual(s.demarkInterface, )
        # self.assertEqual(s.switchInterface, )
        # self.assertEqual(s.device, )
        # self.assertEqual(s.modelnumber, )
        # self.assertEqual(s.IPAddress, )
        # self.assertEqual(s.switchdescription, )
        # self.assertEqual(s.demarkdescription, )
        # self.assertEqual(s.uplink, )
        # self.assertEqual(s.systemName, )
        # self.assertEqual(s.version, )
        # self.assertEqual(s.serial, )
        # self.assertEqual(s.stack, )
        # self.assertEqual(s.uptime, )
        # self.assertEqual(s.lastrestart, )
        # self.assertEqual(s.subnetmask, )
        # self.assertEqual(s.defaultgateway, )
        # self.assertEqual(s.bannername, )
        # self.assertEqual(s.portcount, )
        # self.assertEqual(s.blades, )
        # self.assertEqual(s.groupedvlans, )
        # self.assertEqual(s.version_result, )
        # self.assertEqual(s.run_result, )
        # self.assertEqual(s.portdowntime_result, )
        # self.assertEqual(s.portcount_result, )
        # self.assertEqual(s.inv_result, )
        # self.assertEqual(s.cdpnei_result, )
        # self.assertEqual(s.module_result, )
        # self.assertEqual(s.chassis, )
        # self.assertEqual(s.hostname, )
        # self.assertEqual(s.link, )
        # self.assertEqual(s.cdpneighbors, )
        # self.assertEqual(s.SNMP, )
        # self.assertEqual(s.interface_result, )
        # self.assertEqual(s.ACL, )
        # self.assertEqual(s.nexus, )
        # self.assertEqual(s.SFPs, )
        # self.assertEqual(s.vlansints, )
        # self.assertEqual(s.conn, )
        # self.assertEqual(s.node, )
        # self.assertEqual(s.conn, )
        # self.assertEqual(s.node, )
        # # Location variables
        # self.assertEqual(s.roomnumber, )
        # self.assertEqual(s.buildingname, )
        # self.assertEqual(s.buildnumber, )
        # self.assertEqual(s.racknumber, )
        # # ACL variables
        # self.assertEqual(s.acl_correct_status, )
        # self.assertEqual(s.acl_data, )
        #
        # # Logging variables
        # self.assertEqual(s.logging_data_result, )
        # self.assertEqual(s.logging_data, )
        # self.assertEqual(s.should_overwrite_logging, )
        # self.assertEqual(s.mgmt_vlan, )

    def test_Cisco_Catalyst_3650_48PQ(self):
        """
        Returns:
        """
        s = Switch(ipaddress="172.31.7.159")
        s.login()
        s.getSwitchInfo()

        # test getting the information properly
        self.assertNotIn("Invalid input detected at", s.version_result)
        self.assertNotIn("Invalid input detected at", s.run_result)
        self.assertNotIn("Invalid input detected at", s.interface_result)
        self.assertIn("Invalid input detected at", s.portdowntime_result)
        self.assertNotIn("Invalid input detected at", s.inv_result)
        self.assertNotIn("Invalid input detected at", s.portcount_result)
        self.assertNotIn("Invalid input detected at", s.cdpnei_result)
        self.assertIn("Invalid input detected at", s.module_result)
        self.assertNotIn("Invalid input detected at", s.snmp_result)
        self.assertNotIn("Invalid input detected at", s.logging_data_result)
        self.assertNotIn("Invalid input detected at", s.tacacs_result)
        self.assertNotIn("Invalid input detected at", s.mac_address_result)
        self.assertNotIn("Invalid input detected at", s.acl_result)

        # # Test the assigning of information to the correct objects
        # s.assignattributes()

        # test global Variables
        # self.assertEqual(s.bannername, 'sx1-521-ac141c')
        # self.assertEqual(s.buildnumber, 521)
        # self.assertEqual(s.buildingname, 'SOM')
        # self.assertEqual(s.roomnumber, 'AC141C')
        # self.assertEqual(s.description, 'Sub Access Layer Switch')
        # self.assertEqual(s.IPAddress, '172.20.66.109')
        # self.assertEqual(s.portcount, 54)
        # self.assertEqual(s.serial[0], 'FDO1424P1BT')
        # self.assertEqual(s.subnetmask, '255.255.254.0')
        # self.assertNotEqual(s.uptime, None)
        # self.assertEqual(s.chassis, None)
        # self.assertEqual(s.defaultgateway, '172.20.66.1')
        # self.assertEqual(s.hostname, 'SX1-521SOM-AC141C')
        # self.assertEqual(s.ip, '172.20.66.109')
        # self.assertEqual(s.lastrestart, None)
        #
        # # test the assignment of ACL object properties
        # self.assertEqual(len(s.ACL), 3)
        # self.assertIn(199, s.ACL.numbers)
        # self.assertIn(70, s.ACL.numbers)
        # self.assertIn(71, s.ACL.numbers)
        # for aclobj in s.ACL.standard_ip_lists:
        #     self.assertIsInstance(aclobj, ACL)
        #     self.assertIsInstance(aclobj.Entries, list)
        #     for entry in aclobj.Entries:
        #         self.assertIsInstance(entry, ACL_Entry)
        #         self.assertTrue(entry.type)
        #         self.assertTrue(entry.number)
        #     self.assertTrue(aclobj.Entries)
        #     self.assertTrue(aclobj.type)
        #
        # # test the assignment of the SNMP Value
        # self.assertIsInstance(s.SNMP, SNMP)
        # self.assertIsInstance(s.SNMP.communities, list)
        # self.assertIsInstance(s.SNMP.traps, list)
        # self.assertIsInstance(s.SNMP.traps, list)
        # self.assertIsInstance(s.SNMP.version, set)
        # self.assertTrue(s.SNMP.communities)
        # self.assertEqual(len(s.SNMP.communities), 8)
        # for communities in s.SNMP.communities:
        #     self.assertIsInstance(communities, SNMP_community)
        #     self.assertTrue(communities.raw_data)
        #     self.assertTrue(communities.string)
        #
        # self.assertEqual(len(s.SNMP.contacts), 1)
        # self.assertEqual(s.SNMP.contacts[0].bc, 'barcode:122256')
        # self.assertEqual(s.SNMP.contacts[0].serial, None)
        # self.assertEqual(s.SNMP.contacts[0].tag, 'RT:297828')
        # for contact in s.SNMP.contacts:
        #     self.assertIsInstance(contact, SNMP_contact)
        #     self.assertIsInstance(contact.bc, str)
        # self.assertTrue(s.SNMP.traps)
        # self.assertEqual(len(s.SNMP.traps), 14)
        # self.assertTrue(s.SNMP.version)
        # self.assertTrue(s.SNMP.loggingips)
        # test = ['155.100.122.152', '155.100.122.113', '155.98.253.148', '155.98.253.149']
        # for log in s.SNMP.loggingips:
        #     self.assertIsInstance(log, IPv4Address)
        #     self.assertIn(str(log), test)
        # self.assertIn(2, s.SNMP.version)
        # self.assertNotIn(3, s.SNMP.version)
        #
        # # check the blades configuration
        # self.assertTrue(s.blades)
        # self.assertEqual(len(s.blades), 1)
        # self.assertEqual(s.blades[0].ISOversion, '12.2(53)SE2')
        # self.assertFalse(s.blades[0].SUP)
        # self.assertEqual(s.blades[0].modelnumber, 'WS-C3560X-48P')
        # self.assertEqual(s.blades[0].portcount, 54)
        # self.assertTrue(s.blades[0].interfaces)
        # self.assertEqual(len(s.blades[0].interfaces), 48)
        # portrange = range(1, 49)
        # for portnumber, interface in s.blades[0].interfaces.items():
        #     self.assertTrue(interface)
        #     self.assertIsInstance(interface.mac_addresses, list)
        #     if interface.mac_addresses:
        #         for macaddress in interface.mac_addresses:
        #             self.assertIsInstance(macaddress, EUI)
        #     self.assertIsInstance(interface, Interface)
        #     self.assertEqual(interface.type, 'copper')
        #     self.assertIn(int(portnumber), portrange)
        #     self.assertTrue(interface.fullname)
        #     self.assertIn(interface.portnumber, portrange)
        # for portnumber, interface in s.blades[0].moduleinterfaces.items():
        #     self.assertTrue(interface)
        #     self.assertIsInstance(interface.mac_addresses, list)
        #     if interface.mac_addresses:
        #         for macaddress in interface.mac_addresses:
        #             self.assertIsInstance(macaddress, EUI)
        #     self.assertIsInstance(interface, Interface)
        #     self.assertTrue(interface.fullname)
        #     self.assertIn(interface.portnumber, portrange)
        # self.assertTrue(s.blades[0].moduleinterfaces['GigabitEthernet1/1'].InBcastPkts)
        # self.assertFalse(s.blades[0].moduleinterfaces['GigabitEthernet1/2'].InBcastPkts)
        # self.assertTrue(s.blades[0].interfaces['1'].InBcastPkts)
        # self.assertTrue(s.blades[0].interfaces['2'].InBcastPkts)
        # self.assertTrue(s.blades[0].interfaces['3'].InBcastPkts)
        # self.assertTrue(s.blades[0].interfaces['4'].InBcastPkts)
        # self.assertTrue(s.blades[0].interfaces['5'].InBcastPkts)
        # self.assertTrue(s.blades[0].interfaces['6'].InBcastPkts)
        # self.assertTrue(s.blades[0].interfaces['7'].InBcastPkts)
        # self.assertFalse(s.blades[0].interfaces['8'].InBcastPkts)
        # self.assertTrue(s.blades[0].interfaces['9'].InBcastPkts)
        # self.assertTrue(s.blades[0].interfaces['10'].InBcastPkts)
        # self.assertTrue(s.blades[0].interfaces['11'].InBcastPkts)
        # self.assertTrue(s.blades[0].interfaces['12'].InBcastPkts)
        # self.assertTrue(s.blades[0].interfaces['13'].InBcastPkts)
        # self.assertTrue(s.blades[0].interfaces['14'].InBcastPkts)
        # self.assertTrue(s.blades[0].interfaces['15'].InBcastPkts)
        # self.assertTrue(s.blades[0].interfaces['16'].InBcastPkts)
        # self.assertTrue(s.blades[0].interfaces['17'].InBcastPkts)
        # self.assertTrue(s.blades[0].interfaces['18'].InBcastPkts)
        # self.assertTrue(s.blades[0].interfaces['19'].InBcastPkts)
        # self.assertTrue(s.blades[0].interfaces['20'].InBcastPkts)
        # self.assertTrue(s.blades[0].interfaces['21'].InBcastPkts)
        # self.assertTrue(s.blades[0].interfaces['22'].InBcastPkts)
        # self.assertTrue(s.blades[0].interfaces['23'].InBcastPkts)
        # self.assertTrue(s.blades[0].interfaces['24'].InBcastPkts)
        #
        # # test assignment of CDP Neighbor
        # self.assertIsInstance(s.cdpneighbors, list)
        # self.assertEqual(len(s.cdpneighbors), 4)
        # for neighbor in s.cdpneighbors:
        #     self.assertIsInstance(neighbor, Neighbor)
        #     self.assertIsInstance(neighbor.ip, ipaddress.IPv4Address)
        #     self.assertIsInstance(neighbor.interface, Interface)
        # self.assertEqual(s.cdpneighbors[0].deviceid, 'dx1-521-bc001.net.utah.edu')
        # self.assertEqual(str(s.cdpneighbors[0].ip), '172.20.66.4')
        # self.assertEqual(s.cdpneighbors[0].platform, 'ciscoWS-C4510R+E')
        # self.assertEqual(s.cdpneighbors[0].interface.fullname, 'GigabitEthernet0/1')
        # self.assertEqual(s.cdpneighbors[0].interface.portnumber, 1)
        # self.assertEqual(s.cdpneighbors[0].duplex, 'full')
        #
        # # logging Info
        # logging = ['155.98.253.244', '155.98.204.52', '172.24.29.14', '10.70.24.10']
        # for log in s.logging_data:
        #     self.assertIn(str(log[1]), logging)
        #     self.assertIsInstance(log[1], ipaddress.IPv4Address)
        #
        # # check vlans
        # self.assertEqual(len(s.vlans), 7)
        # self.assertEqual(s.vlans[0].name, '521SOM-fl1-zeroclients')
        # self.assertEqual(s.vlans[0].number, 110)
        # self.assertEqual(s.vlans[1].name, '521-mgmt')
        # self.assertEqual(s.vlans[1].number, 333)
        # self.assertEqual(s.vlans[2].name, 'bldg-521-printer')
        # self.assertEqual(s.vlans[2].number, 398)
        # for macaddress in s.vlans[2].mac_addresses:
        #     self.assertIsInstance(macaddress, EUI)
        #
        # # test tacacs configuration
        # self.assertIsInstance(s.tacacs, list)
        # self.assertEqual(len(s.tacacs), 2)
        # self.assertIsInstance(s.tacacs[0], TACACS)
        # self.assertIsInstance(s.tacacs[0].server, ipaddress.IPv4Address)
        # self.assertEqual(str(s.tacacs[0].server), '172.31.17.180')
        # self.assertIsInstance(s.tacacs[1].server, ipaddress.IPv4Address)
        # self.assertEqual(str(s.tacacs[1].server), '10.64.32.5')

    def Catalyst_37xx_Stack(self):
        pass
        # s = Switch(ipaddress="")
        # s.login()
        # s.getSwitchInfo()
        #
        #
        # #test getting the information properly
        # self.assertEqual(s.version_result,)
        # self.assertEqual(s.run_result,)
        # self.assertEqual(s.interface_result,)
        # self.assertEqual(s.interface_name_r,)
        # self.assertEqual(s.portdowntime_result),
        # self.assertEqual(s.inv_result,)
        # self.assertEqual(s.portcount_result,)
        # self.assertEqual(s.cdpnei_result,)
        # self.assertEqual(s.module_result,)
        # self.assertEqual(s.snmp_result,)
        # self.assertEqual(s.logging_data_result,)
        #
        # #Test the assigning of information to the correct objects
        # s.assignattributes()
        #
        # self.assertEqual(s.switchdescription, )
        # self.assertEqual(s.demarkInterface, )
        # self.assertEqual(s.switchInterface, )
        # self.assertEqual(s.device, )
        # self.assertEqual(s.modelnumber, )
        # self.assertEqual(s.IPAddress, )
        # self.assertEqual(s.switchdescription, )
        # self.assertEqual(s.demarkdescription, )
        # self.assertEqual(s.uplink, )
        # self.assertEqual(s.systemName, )
        # self.assertEqual(s.version, )
        # self.assertEqual(s.serial, )
        # self.assertEqual(s.stack, )
        # self.assertEqual(s.uptime, )
        # self.assertEqual(s.lastrestart, )
        # self.assertEqual(s.subnetmask, )
        # self.assertEqual(s.defaultgateway, )
        # self.assertEqual(s.bannername, )
        # self.assertEqual(s.portcount, )
        # self.assertEqual(s.blades, )
        # self.assertEqual(s.groupedvlans, )
        # self.assertEqual(s.version_result, )
        # self.assertEqual(s.run_result, )
        # self.assertEqual(s.portdowntime_result, )
        # self.assertEqual(s.portcount_result, )
        # self.assertEqual(s.inv_result, )
        # self.assertEqual(s.cdpnei_result, )
        # self.assertEqual(s.module_result, )
        # self.assertEqual(s.chassis, )
        # self.assertEqual(s.hostname, )
        # self.assertEqual(s.link, )
        # self.assertEqual(s.cdpneighbors, )
        # self.assertEqual(s.SNMP, )
        # self.assertEqual(s.interface_result, )
        # self.assertEqual(s.ACL, )
        # self.assertEqual(s.nexus, )
        # self.assertEqual(s.SFPs, )
        # self.assertEqual(s.vlansints, )
        # self.assertEqual(s.conn, )
        # self.assertEqual(s.node, )
        # self.assertEqual(s.conn, )
        # self.assertEqual(s.node, )
        # # Location variables
        # self.assertEqual(s.roomnumber, )
        # self.assertEqual(s.buildingname, )
        # self.assertEqual(s.buildnumber, )
        # self.assertEqual(s.racknumber, )
        # # ACL variables
        # self.assertEqual(s.acl_correct_status, )
        # self.assertEqual(s.acl_data, )
        #
        # # Logging variables
        # self.assertEqual(s.logging_data_result, )
        # self.assertEqual(s.logging_data, )
        # self.assertEqual(s.should_overwrite_logging, )
        # self.assertEqual(s.mgmt_vlan, )

    def Catalyst_3850(self):
        pass
        # s = Switch(ipaddress="")
        # s.login()
        # s.getSwitchInfo()
        #
        #
        # #test getting the information properly
        # self.assertEqual(s.version_result,)
        # self.assertEqual(s.run_result,)
        # self.assertEqual(s.interface_result,)
        # self.assertEqual(s.interface_name_r,)
        # self.assertEqual(s.portdowntime_result),
        # self.assertEqual(s.inv_result,)
        # self.assertEqual(s.portcount_result,)
        # self.assertEqual(s.cdpnei_result,)
        # self.assertEqual(s.module_result,)
        # self.assertEqual(s.snmp_result,)
        # self.assertEqual(s.logging_data_result,)
        #
        # #Test the assigning of information to the correct objects
        # s.assignattributes()
        #
        # self.assertEqual(s.switchdescription, )
        # self.assertEqual(s.demarkInterface, )
        # self.assertEqual(s.switchInterface, )
        # self.assertEqual(s.device, )
        # self.assertEqual(s.modelnumber, )
        # self.assertEqual(s.IPAddress, )
        # self.assertEqual(s.switchdescription, )
        # self.assertEqual(s.demarkdescription, )
        # self.assertEqual(s.uplink, )
        # self.assertEqual(s.systemName, )
        # self.assertEqual(s.version, )
        # self.assertEqual(s.serial, )
        # self.assertEqual(s.stack, )
        # self.assertEqual(s.uptime, )
        # self.assertEqual(s.lastrestart, )
        # self.assertEqual(s.subnetmask, )
        # self.assertEqual(s.defaultgateway, )
        # self.assertEqual(s.bannername, )
        # self.assertEqual(s.portcount, )
        # self.assertEqual(s.blades, )
        # self.assertEqual(s.groupedvlans, )
        # self.assertEqual(s.version_result, )
        # self.assertEqual(s.run_result, )
        # self.assertEqual(s.portdowntime_result, )
        # self.assertEqual(s.portcount_result, )
        # self.assertEqual(s.inv_result, )
        # self.assertEqual(s.cdpnei_result, )
        # self.assertEqual(s.module_result, )
        # self.assertEqual(s.chassis, )
        # self.assertEqual(s.hostname, )
        # self.assertEqual(s.link, )
        # self.assertEqual(s.cdpneighbors, )
        # self.assertEqual(s.SNMP, )
        # self.assertEqual(s.interface_result, )
        # self.assertEqual(s.ACL, )
        # self.assertEqual(s.nexus, )
        # self.assertEqual(s.SFPs, )
        # self.assertEqual(s.vlansints, )
        # self.assertEqual(s.conn, )
        # self.assertEqual(s.node, )
        # self.assertEqual(s.conn, )
        # self.assertEqual(s.node, )
        # # Location variables
        # self.assertEqual(s.roomnumber, )
        # self.assertEqual(s.buildingname, )
        # self.assertEqual(s.buildnumber, )
        # self.assertEqual(s.racknumber, )
        # # ACL variables
        # self.assertEqual(s.acl_correct_status, )
        # self.assertEqual(s.acl_data, )
        #
        # # Logging variables
        # self.assertEqual(s.logging_data_result, )
        # self.assertEqual(s.logging_data, )
        # self.assertEqual(s.should_overwrite_logging, )
        # self.assertEqual(s.mgmt_vlan, )

    def Catalyst_4500X(self):
        pass
        # s = Switch(ipaddress="")
        # s.login()
        # s.getSwitchInfo()
        #
        #
        # #test getting the information properly
        # self.assertEqual(s.version_result,)
        # self.assertEqual(s.run_result,)
        # self.assertEqual(s.interface_result,)
        # self.assertEqual(s.interface_name_r,)
        # self.assertEqual(s.portdowntime_result),
        # self.assertEqual(s.inv_result,)
        # self.assertEqual(s.portcount_result,)
        # self.assertEqual(s.cdpnei_result,)
        # self.assertEqual(s.module_result,)
        # self.assertEqual(s.snmp_result,)
        # self.assertEqual(s.logging_data_result,)
        #
        # #Test the assigning of information to the correct objects
        # s.assignattributes()
        #
        # self.assertEqual(s.switchdescription, )
        # self.assertEqual(s.demarkInterface, )
        # self.assertEqual(s.switchInterface, )
        # self.assertEqual(s.device, )
        # self.assertEqual(s.modelnumber, )
        # self.assertEqual(s.IPAddress, )
        # self.assertEqual(s.switchdescription, )
        # self.assertEqual(s.demarkdescription, )
        # self.assertEqual(s.uplink, )
        # self.assertEqual(s.systemName, )
        # self.assertEqual(s.version, )
        # self.assertEqual(s.serial, )
        # self.assertEqual(s.stack, )
        # self.assertEqual(s.uptime, )
        # self.assertEqual(s.lastrestart, )
        # self.assertEqual(s.subnetmask, )
        # self.assertEqual(s.defaultgateway, )
        # self.assertEqual(s.bannername, )
        # self.assertEqual(s.portcount, )
        # self.assertEqual(s.blades, )
        # self.assertEqual(s.groupedvlans, )
        # self.assertEqual(s.version_result, )
        # self.assertEqual(s.run_result, )
        # self.assertEqual(s.portdowntime_result, )
        # self.assertEqual(s.portcount_result, )
        # self.assertEqual(s.inv_result, )
        # self.assertEqual(s.cdpnei_result, )
        # self.assertEqual(s.module_result, )
        # self.assertEqual(s.chassis, )
        # self.assertEqual(s.hostname, )
        # self.assertEqual(s.link, )
        # self.assertEqual(s.cdpneighbors, )
        # self.assertEqual(s.SNMP, )
        # self.assertEqual(s.interface_result, )
        # self.assertEqual(s.ACL, )
        # self.assertEqual(s.nexus, )
        # self.assertEqual(s.SFPs, )
        # self.assertEqual(s.vlansints, )
        # self.assertEqual(s.conn, )
        # self.assertEqual(s.node, )
        # self.assertEqual(s.conn, )
        # self.assertEqual(s.node, )
        # # Location variables
        # self.assertEqual(s.roomnumber, )
        # self.assertEqual(s.buildingname, )
        # self.assertEqual(s.buildnumber, )
        # self.assertEqual(s.racknumber, )
        # # ACL variables
        # self.assertEqual(s.acl_correct_status, )
        # self.assertEqual(s.acl_data, )
        #
        # # Logging variables
        # self.assertEqual(s.logging_data_result, )
        # self.assertEqual(s.logging_data, )
        # self.assertEqual(s.should_overwrite_logging, )
        # self.assertEqual(s.mgmt_vlan, )

    def test_Catalyst_4500XP(self):
        s = Switch(ipaddress="172.30.133.197")
        s.login()
        s.getSwitchInfo()

        # test getting the information properly
        self.assertNotIn("Invalid input detected at", s.version_result)
        self.assertNotIn("Invalid input detected at", s.run_result)
        self.assertNotIn("Invalid input detected at", s.interface_result)
        self.assertNotIn("Invalid input detected at", s.portdowntime_result)
        self.assertNotIn("Invalid input detected at", s.inv_result)
        self.assertNotIn("Invalid input detected at", s.portcount_result)
        self.assertNotIn("Invalid input detected at", s.cdpnei_result)
        self.assertNotIn("Invalid input detected at", s.module_result)
        self.assertNotIn("Invalid input detected at", s.snmp_result)
        self.assertNotIn("Invalid input detected at", s.logging_data_result)
        self.assertNotIn("Invalid input detected at", s.tacacs_result)
        self.assertNotIn("Invalid input detected at", s.mac_address_result)
        self.assertNotIn("Invalid input detected at", s.acl_result)

        # Test the assigning of information to the correct objects
        s.assignattributes()

        # test global Variables
        self.assertEqual(s.bannername, 'dx1-012sutton-119-R1-park')
        self.assertEqual(s.buildnumber, '0012')
        self.assertEqual(s.buildingname, 'sutton')
        self.assertEqual(s.roomnumber, '119')
        self.assertEqual(s.description, 'Demarc (Access Layer Switch)')
        self.assertEqual(s.IPAddress, '172.30.133.197')
        self.assertEqual(s.portcount, 32)
        self.assertEqual(s.serial[0], 'JAE202003BF')
        self.assertEqual(s.subnetmask, '255.255.255.192')
        self.assertNotEqual(s.uptime, None)
        self.assertEqual(s.chassis, None)
        self.assertEqual(s.defaultgateway, '172.30.133.193')
        self.assertEqual(s.hostname, 'dx1-012sutton-119-R1')
        self.assertEqual(s.ip, '172.30.133.197')
        self.assertEqual(s.lastrestart, None)

        # test the assignment of ACL object properties
        self.assertEqual(len(s.access_lists), 31)
        self.assertIn(199, s.access_lists.numbers)
        self.assertIn(70, s.access_lists.numbers)
        self.assertIn(71, s.access_lists.numbers)
        for aclobj in s.access_lists.standard_ip_lists:
            self.assertIsInstance(aclobj, ACL)
            self.assertIsInstance(aclobj.Entries, list)
            for entry in aclobj.Entries:
                self.assertIsInstance(entry, ACL_Entry)
                self.assertTrue(entry.type)
                self.assertTrue(entry.number)
            self.assertTrue(aclobj.Entries)
            self.assertTrue(aclobj.type)

        # test the assignment of the SNMP Value
        self.assertIsInstance(s.SNMP, SNMP)
        self.assertIsInstance(s.SNMP.version, set)
        self.assertFalse(s.SNMP.communities)
        self.assertFalse(s.SNMP.contextPFG)
        self.assertFalse(s.SNMP.ifmib)
        self.assertFalse(s.SNMP.locationcorrect)
        self.assertFalse(s.SNMP.loggingcorrect)
        self.assertFalse(s.SNMP.loggingips)
        self.assertFalse(s.SNMP.traps)
        self.assertTrue(s.SNMP.contacts)
        self.assertTrue(s.SNMP.context_line)
        self.assertTrue(s.SNMP.location_bldg)
        self.assertTrue(s.SNMP.views)
        self.assertTrue(s.SNMP.version)
        # self.assertEqual(len(s.SNMP.communities), 8)
        # self.assertIsInstance(s.SNMP.communities, list)
        # for communities in s.SNMP.communities:
        #     self.assertIsInstance(communities, SNMP_community)
        #     self.assertTrue(communities.raw_data)
        #     self.assertTrue(communities.string)

        self.assertEqual(len(s.SNMP.contacts), 1)
        self.assertEqual(s.SNMP.contacts[0].bc, '1')
        self.assertEqual(s.SNMP.contacts[0].serial, None)
        self.assertEqual(s.SNMP.contacts[0].tag, '2')
        for contact in s.SNMP.contacts:
            self.assertIsInstance(contact, SNMP_contact)
            self.assertIsInstance(contact.bc, str)

        self.assertEqual(len(s.SNMP.groups),2)
        for group in s.SNMP.groups:
            self.assertIsInstance(group,SNMP_Group)
            self.assertIsInstance(group.acl,ACL)
        self.assertEqual(s.SNMP.groups[0].RO,True)
        self.assertEqual(s.SNMP.groups[0].RW, False)
        self.assertEqual(s.SNMP.groups[0].correct, False)
        self.assertEqual(s.SNMP.groups[0].line, 'NOCGrv3RO v3 priv read NOCViewRO access 70')
        self.assertEqual(s.SNMP.groups[0].name, 'NOCGrv3RO')
        self.assertEqual(s.SNMP.groups[0].remove, False)
        self.assertEqual(s.SNMP.groups[0].securitylevel, 'priv')
        self.assertEqual(s.SNMP.groups[0].version, 'v3')
        self.assertEqual(s.SNMP.groups[0].viewname, 'NOCViewRO')
        self.assertEqual(s.SNMP.groups[1].RO, False)
        self.assertEqual(s.SNMP.groups[1].RW, True)
        self.assertEqual(s.SNMP.groups[1].correct, False)
        self.assertEqual(s.SNMP.groups[1].line, 'NOCGrv3RW v3 priv write NOCViewRW access 71')
        self.assertEqual(s.SNMP.groups[1].name, 'NOCGrv3RW')
        self.assertEqual(s.SNMP.groups[1].remove, False)
        self.assertEqual(s.SNMP.groups[1].securitylevel, 'priv')
        self.assertEqual(s.SNMP.groups[1].version, 'v3')
        self.assertEqual(s.SNMP.groups[1].viewname, 'NOCViewRW')
        self.assertEqual(s.SNMP.location_bldg, '012')
        self.assertEqual(len(s.SNMP.views), 2)
        for group in s.SNMP.views:
            self.assertIsInstance(group, SNMP_view)
        self.assertEqual(s.SNMP.views[0].included, True)
        self.assertEqual(s.SNMP.views[0].excluded, False)
        self.assertEqual(s.SNMP.views[0].correct, False)
        self.assertEqual(s.SNMP.views[0].mibfamily, 'internet')
        self.assertEqual(s.SNMP.views[0].name, 'NOCViewRO')
        self.assertEqual(s.SNMP.views[1].included, True)
        self.assertEqual(s.SNMP.views[1].excluded, False)
        self.assertEqual(s.SNMP.views[1].correct, False)
        self.assertEqual(s.SNMP.views[1].mibfamily, 'internet')
        self.assertEqual(s.SNMP.views[1].name, 'NOCViewRW')
        # self.assertTrue(s.SNMP.traps)
        # self.assertEqual(len(s.SNMP.traps), 14)
        # self.assertTrue(s.SNMP.loggingips)
        # test = ['155.100.122.152', '155.100.122.113', '155.98.253.148', '155.98.253.149']
        # for log in s.SNMP.loggingips:
        #     self.assertIsInstance(log, IPv4Address)
        #     self.assertIn(str(log), test)
        self.assertIn(3, s.SNMP.version)
        self.assertNotIn(2, s.SNMP.version)

        # check the blades configuration
        self.assertTrue(s.blades)
        self.assertEqual(len(s.blades), 1)
        self.assertEqual(s.blades[0].ISOversion, '')
        self.assertFalse(s.blades[0].SUP)
        self.assertEqual(s.blades[0].modelnumber, 'WS-C4500X-32')
        self.assertEqual(s.blades[0].portcount, 32)
        self.assertTrue(s.blades[0].interfaces)
        self.assertEqual(len(s.blades[0].interfaces), 32)
        portrange = range(1, 33)
        for portnumber, interface in s.blades[0].interfaces.items():
            self.assertTrue(interface)
            self.assertIsInstance(interface.mac_addresses, list)
            if interface.mac_addresses:
                for macaddress in interface.mac_addresses:
                    self.assertIsInstance(macaddress, EUI)
            self.assertIsInstance(interface, Interface)
            self.assertEqual(interface.type, 'fiber')
            self.assertIn(int(portnumber), portrange)
            self.assertTrue(interface.fullname)
            self.assertIn(interface.portnumber, portrange)
        self.assertTrue(s.blades[0].interfaces['1'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['2'].InBcastPkts)
        self.assertFalse(s.blades[0].interfaces['3'].InBcastPkts)
        self.assertFalse(s.blades[0].interfaces['4'].InBcastPkts)
        self.assertFalse(s.blades[0].interfaces['5'].InBcastPkts)
        self.assertFalse(s.blades[0].interfaces['6'].InBcastPkts)
        self.assertFalse(s.blades[0].interfaces['7'].InBcastPkts)
        self.assertFalse(s.blades[0].interfaces['8'].InBcastPkts)
        self.assertFalse(s.blades[0].interfaces['9'].InBcastPkts)
        self.assertFalse(s.blades[0].interfaces['10'].InBcastPkts)
        self.assertFalse(s.blades[0].interfaces['11'].InBcastPkts)
        self.assertFalse(s.blades[0].interfaces['12'].InBcastPkts)
        self.assertFalse(s.blades[0].interfaces['13'].InBcastPkts)
        self.assertFalse(s.blades[0].interfaces['14'].InBcastPkts)
        self.assertFalse(s.blades[0].interfaces['15'].InBcastPkts)
        self.assertFalse(s.blades[0].interfaces['16'].InBcastPkts)
        self.assertFalse(s.blades[0].interfaces['17'].InBcastPkts)
        self.assertFalse(s.blades[0].interfaces['18'].InBcastPkts)
        self.assertFalse(s.blades[0].interfaces['19'].InBcastPkts)
        self.assertFalse(s.blades[0].interfaces['20'].InBcastPkts)
        self.assertFalse(s.blades[0].interfaces['21'].InBcastPkts)
        self.assertFalse(s.blades[0].interfaces['22'].InBcastPkts)
        self.assertFalse(s.blades[0].interfaces['23'].InBcastPkts)
        self.assertFalse(s.blades[0].interfaces['24'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['25'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['26'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['27'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['28'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['29'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['30'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['31'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['32'].InBcastPkts)

        # test assignment of CDP Neighbor
        self.assertIsInstance(s.cdpneighbors, list)
        self.assertEqual(len(s.cdpneighbors), 9)
        for neighbor in s.cdpneighbors:
            self.assertIsInstance(neighbor, Neighbor)
            self.assertIsInstance(neighbor.ip, ipaddress.IPv4Address)
            self.assertIsInstance(neighbor.interface, Interface)
        self.assertEqual(s.cdpneighbors[0].deviceid, 'r2-park-park(JAF1721ACLG)')
        self.assertEqual(str(s.cdpneighbors[0].ip), '172.29.1.13')
        self.assertEqual(s.cdpneighbors[0].platform, 'N7K-C7010')
        self.assertEqual(s.cdpneighbors[0].interface.fullname, 'TenGigabitEthernet1/2')
        self.assertEqual(s.cdpneighbors[0].interface.portnumber, 2)
        self.assertEqual(s.cdpneighbors[0].duplex, 'full')

        # logging Info
        logging = ['155.98.253.244', '155.98.204.52', '172.24.29.14', '10.70.24.10','10.71.24.11']
        for log in s.logging_data:
            self.assertIn(str(log[1]), logging)
            self.assertIsInstance(log[1], ipaddress.IPv4Address)

        # check vlans
        self.assertEqual(len(s.vlans), 36)
        self.assertEqual(s.vlans[0].name, 'park-011wbb-TLT-airmedia')
        self.assertEqual(s.vlans[0].number, 448)
        self.assertEqual(s.vlans[1].name, 'uu-012-FASB-redprint')
        self.assertEqual(s.vlans[1].number, 572)
        self.assertEqual(s.vlans[2].name, 'park-012suttongeo-ccure')
        self.assertEqual(s.vlans[2].number, 613)
        for macaddress in s.vlans[2].mac_addresses:
            self.assertIsInstance(macaddress, EUI)

        # test tacacs configuration
        self.assertIsInstance(s.tacacs, list)
        self.assertEqual(len(s.tacacs), 2)
        self.assertIsInstance(s.tacacs[0], TACACS)
        self.assertIsInstance(s.tacacs[0].server, ipaddress.IPv4Address)
        self.assertEqual(str(s.tacacs[0].server), '172.31.17.180')
        self.assertEqual(str(s.tacacs[0].name), 'TAC-EBC')
        self.assertIsInstance(s.tacacs[1].server, ipaddress.IPv4Address)
        self.assertEqual(str(s.tacacs[1].server), '10.64.32.5')
        self.assertEqual(str(s.tacacs[1].name), 'TAC-SECONDARY')

    def Catalyst_C4507R(self):
        pass
        # s = Switch(ipaddress="")
        # s.login()
        # s.getSwitchInfo()
        #
        #
        # #test getting the information properly
        # self.assertEqual(s.version_result,)
        # self.assertEqual(s.run_result,)
        # self.assertEqual(s.interface_result,)
        # self.assertEqual(s.interface_name_r,)
        # self.assertEqual(s.portdowntime_result),
        # self.assertEqual(s.inv_result,)
        # self.assertEqual(s.portcount_result,)
        # self.assertEqual(s.cdpnei_result,)
        # self.assertEqual(s.module_result,)
        # self.assertEqual(s.snmp_result,)
        # self.assertEqual(s.logging_data_result,)
        #
        # #Test the assigning of information to the correct objects
        # s.assignattributes()
        #
        # self.assertEqual(s.switchdescription, )
        # self.assertEqual(s.demarkInterface, )
        # self.assertEqual(s.switchInterface, )
        # self.assertEqual(s.device, )
        # self.assertEqual(s.modelnumber, )
        # self.assertEqual(s.IPAddress, )
        # self.assertEqual(s.switchdescription, )
        # self.assertEqual(s.demarkdescription, )
        # self.assertEqual(s.uplink, )
        # self.assertEqual(s.systemName, )
        # self.assertEqual(s.version, )
        # self.assertEqual(s.serial, )
        # self.assertEqual(s.stack, )
        # self.assertEqual(s.uptime, )
        # self.assertEqual(s.lastrestart, )
        # self.assertEqual(s.subnetmask, )
        # self.assertEqual(s.defaultgateway, )
        # self.assertEqual(s.bannername, )
        # self.assertEqual(s.portcount, )
        # self.assertEqual(s.blades, )
        # self.assertEqual(s.groupedvlans, )
        # self.assertEqual(s.version_result, )
        # self.assertEqual(s.run_result, )
        # self.assertEqual(s.portdowntime_result, )
        # self.assertEqual(s.portcount_result, )
        # self.assertEqual(s.inv_result, )
        # self.assertEqual(s.cdpnei_result, )
        # self.assertEqual(s.module_result, )
        # self.assertEqual(s.chassis, )
        # self.assertEqual(s.hostname, )
        # self.assertEqual(s.link, )
        # self.assertEqual(s.cdpneighbors, )
        # self.assertEqual(s.SNMP, )
        # self.assertEqual(s.interface_result, )
        # self.assertEqual(s.ACL, )
        # self.assertEqual(s.nexus, )
        # self.assertEqual(s.SFPs, )
        # self.assertEqual(s.vlansints, )
        # self.assertEqual(s.conn, )
        # self.assertEqual(s.node, )
        # self.assertEqual(s.conn, )
        # self.assertEqual(s.node, )
        # # Location variables
        # self.assertEqual(s.roomnumber, )
        # self.assertEqual(s.buildingname, )
        # self.assertEqual(s.buildnumber, )
        # self.assertEqual(s.racknumber, )
        # # ACL variables
        # self.assertEqual(s.acl_correct_status, )
        # self.assertEqual(s.acl_data, )
        #
        # # Logging variables
        # self.assertEqual(s.logging_data_result, )
        # self.assertEqual(s.logging_data, )
        # self.assertEqual(s.should_overwrite_logging, )
        # self.assertEqual(s.mgmt_vlan, )

    def Cisco_Catalyst_4506(self):
        pass
        # s = Switch(ipaddress="")
        # s.login()
        # s.getSwitchInfo()
        #
        #
        # #test getting the information properly
        # self.assertEqual(s.version_result,)
        # self.assertEqual(s.run_result,)
        # self.assertEqual(s.interface_result,)
        # self.assertEqual(s.interface_name_r,)
        # self.assertEqual(s.portdowntime_result),
        # self.assertEqual(s.inv_result,)
        # self.assertEqual(s.portcount_result,)
        # self.assertEqual(s.cdpnei_result,)
        # self.assertEqual(s.module_result,)
        # self.assertEqual(s.snmp_result,)
        # self.assertEqual(s.logging_data_result,)
        #
        # #Test the assigning of information to the correct objects
        # s.assignattributes()
        #
        # self.assertEqual(s.switchdescription, )
        # self.assertEqual(s.demarkInterface, )
        # self.assertEqual(s.switchInterface, )
        # self.assertEqual(s.device, )
        # self.assertEqual(s.modelnumber, )
        # self.assertEqual(s.IPAddress, )
        # self.assertEqual(s.switchdescription, )
        # self.assertEqual(s.demarkdescription, )
        # self.assertEqual(s.uplink, )
        # self.assertEqual(s.systemName, )
        # self.assertEqual(s.version, )
        # self.assertEqual(s.serial, )
        # self.assertEqual(s.stack, )
        # self.assertEqual(s.uptime, )
        # self.assertEqual(s.lastrestart, )
        # self.assertEqual(s.subnetmask, )
        # self.assertEqual(s.defaultgateway, )
        # self.assertEqual(s.bannername, )
        # self.assertEqual(s.portcount, )
        # self.assertEqual(s.blades, )
        # self.assertEqual(s.groupedvlans, )
        # self.assertEqual(s.version_result, )
        # self.assertEqual(s.run_result, )
        # self.assertEqual(s.portdowntime_result, )
        # self.assertEqual(s.portcount_result, )
        # self.assertEqual(s.inv_result, )
        # self.assertEqual(s.cdpnei_result, )
        # self.assertEqual(s.module_result, )
        # self.assertEqual(s.chassis, )
        # self.assertEqual(s.hostname, )
        # self.assertEqual(s.link, )
        # self.assertEqual(s.cdpneighbors, )
        # self.assertEqual(s.SNMP, )
        # self.assertEqual(s.interface_result, )
        # self.assertEqual(s.ACL, )
        # self.assertEqual(s.nexus, )
        # self.assertEqual(s.SFPs, )
        # self.assertEqual(s.vlansints, )
        # self.assertEqual(s.conn, )
        # self.assertEqual(s.node, )
        # self.assertEqual(s.conn, )
        # self.assertEqual(s.node, )
        # # Location variables
        # self.assertEqual(s.roomnumber, )
        # self.assertEqual(s.buildingname, )
        # self.assertEqual(s.buildnumber, )
        # self.assertEqual(s.racknumber, )
        # # ACL variables
        # self.assertEqual(s.acl_correct_status, )
        # self.assertEqual(s.acl_data, )
        #
        # # Logging variables
        # self.assertEqual(s.logging_data_result, )
        # self.assertEqual(s.logging_data, )
        # self.assertEqual(s.should_overwrite_logging, )
        # self.assertEqual(s.mgmt_vlan, )

    def test_Cisco_Catalyst_4510R(self):
        s = Switch(ipaddress="172.31.16.7")
        s.login()
        s.getSwitchInfo()

        # test getting the information properly
        self.assertNotIn("Invalid input detected at", s.version_result)
        self.assertNotIn("Invalid input detected at", s.run_result)
        self.assertNotIn("Invalid input detected at", s.interface_result)
        self.assertNotIn("Invalid input detected at", s.portdowntime_result)
        self.assertNotIn("Invalid input detected at", s.inv_result)
        self.assertNotIn("Invalid input detected at", s.portcount_result)
        self.assertNotIn("Invalid input detected at", s.cdpnei_result)
        self.assertNotIn("Invalid input detected at", s.module_result)
        self.assertNotIn("Invalid input detected at", s.snmp_result)
        self.assertNotIn("Invalid input detected at", s.logging_data_result)
        self.assertNotIn("Invalid input detected at", s.tacacs_result)
        self.assertNotIn("Invalid input detected at", s.mac_address_result)
        self.assertNotIn("Invalid input detected at", s.acl_result)

        # Test the assigning of information to the correct objects
        s.assignattributes()

        # test global Variables
        self.assertEqual(s.bannername, 'sx1-482-102tower-1w-2940b.net.utah.edu')
        self.assertEqual(s.buildnumber, '0102')
        self.assertEqual(s.buildingname, 'tower')
        self.assertEqual(s.roomnumber, None)
        self.assertEqual(s.description, 'Sub Access Layer Switch')
        self.assertEqual(s.IPAddress, '172.31.16.7')
        self.assertEqual(s.portcount, 392)
        self.assertEqual(s.serial[0], 'JAD204703HR')
        self.assertEqual(s.subnetmask, '255.255.255.0')
        self.assertNotEqual(s.uptime, None)
        self.assertEqual(s.chassis, None)
        self.assertEqual(s.defaultgateway, '172.31.16.1')
        self.assertEqual(s.hostname, 'sx1-482-102tower-1w-2940b')
        self.assertEqual(s.ip, '172.31.16.7')
        self.assertEqual(s.lastrestart, None)

        # test the assignment of ACL object properties
        self.assertEqual(len(s.access_lists), 19)
        self.assertIn(199, s.access_lists.numbers)
        self.assertIn(70, s.access_lists.numbers)
        self.assertIn(71, s.access_lists.numbers)
        self.assertIn(73, s.access_lists.numbers)
        for aclobj in s.access_lists.standard_ip_lists:
            self.assertIsInstance(aclobj, ACL)
            self.assertIsInstance(aclobj.Entries, list)
            for entry in aclobj.Entries:
                self.assertIsInstance(entry, ACL_Entry)
                self.assertTrue(entry.source)
                self.assertTrue(entry.number)
            self.assertTrue(aclobj.Entries)
            self.assertTrue(aclobj.type)
        for aclobj in s.access_lists.extended_ip_lists:
            self.assertIsInstance(aclobj, ACL)
            self.assertIsInstance(aclobj.Entries, list)
            for entry in aclobj.Entries:
                self.assertIsInstance(entry, ACL_Entry)
                self.assertTrue(entry.source)
                self.assertTrue(entry.number)
                self.assertTrue(entry.protocol)
            self.assertTrue(aclobj.Entries)
            self.assertTrue(aclobj.type)
        # test the assignment of the SNMP Value
        self.assertIsInstance(s.SNMP, SNMP)
        self.assertIsInstance(s.SNMP.version, set)
        self.assertFalse(s.SNMP.communities)
        self.assertFalse(s.SNMP.contextPFG)
        self.assertFalse(s.SNMP.ifmib)
        self.assertFalse(s.SNMP.locationcorrect)
        self.assertFalse(s.SNMP.loggingcorrect)
        self.assertFalse(s.SNMP.loggingips)
        self.assertFalse(s.SNMP.traps)
        self.assertTrue(s.SNMP.contacts)
        self.assertTrue(s.SNMP.context_line)
        self.assertTrue(s.SNMP.location_bldg)
        self.assertTrue(s.SNMP.location_rm)
        self.assertTrue(s.SNMP.views)
        self.assertTrue(s.SNMP.version)
        # self.assertEqual(len(s.SNMP.communities), 8)
        # self.assertIsInstance(s.SNMP.communities, list)
        # for communities in s.SNMP.communities:
        #     self.assertIsInstance(communities, SNMP_community)
        #     self.assertTrue(communities.raw_data)
        #     self.assertTrue(communities.string)

        self.assertEqual(len(s.SNMP.contacts), 1)
        self.assertEqual(s.SNMP.contacts[0].bc, '508007')
        self.assertEqual(s.SNMP.contacts[0].serial, None)
        self.assertEqual(s.SNMP.contacts[0].tag, 'R-***number***')
        for contact in s.SNMP.contacts:
            self.assertIsInstance(contact, SNMP_contact)
            self.assertIsInstance(contact.bc, str)
        self.assertEqual(len(s.SNMP.groups), 2)
        for group in s.SNMP.groups:
            self.assertIsInstance(group, SNMP_Group)
            self.assertIsInstance(group.acl, ACL)
        self.assertEqual(s.SNMP.groups[0].RO, True)
        self.assertEqual(s.SNMP.groups[0].RW, False)
        self.assertEqual(s.SNMP.groups[0].correct, False)
        self.assertEqual(s.SNMP.groups[0].line, 'NOCGrv3RO v3 priv read NOCViewRO access 70')
        self.assertEqual(s.SNMP.groups[0].name, 'NOCGrv3RO')
        self.assertEqual(s.SNMP.groups[0].remove, False)
        self.assertEqual(s.SNMP.groups[0].securitylevel, 'priv')
        self.assertEqual(s.SNMP.groups[0].version, 'v3')
        self.assertEqual(s.SNMP.groups[0].viewname, 'NOCViewRO')
        self.assertEqual(s.SNMP.groups[1].RO, False)
        self.assertEqual(s.SNMP.groups[1].RW, True)
        self.assertEqual(s.SNMP.groups[1].correct, False)
        self.assertEqual(s.SNMP.groups[1].line, 'NOCGrv3RW v3 priv write NOCViewRW access 71')
        self.assertEqual(s.SNMP.groups[1].name, 'NOCGrv3RW')
        self.assertEqual(s.SNMP.groups[1].remove, False)
        self.assertEqual(s.SNMP.groups[1].securitylevel, 'priv')
        self.assertEqual(s.SNMP.groups[1].version, 'v3')
        self.assertEqual(s.SNMP.groups[1].viewname, 'NOCViewRW')
        self.assertEqual(s.SNMP.location_bldg, '482')
        self.assertEqual(s.SNMP.location_rm, '2940b')
        self.assertEqual(len(s.SNMP.views), 3)
        for group in s.SNMP.views:
            self.assertIsInstance(group, SNMP_view)
        self.assertEqual(s.SNMP.views[0].included, True)
        self.assertEqual(s.SNMP.views[0].excluded, False)
        self.assertEqual(s.SNMP.views[0].correct, False)
        self.assertEqual(s.SNMP.views[0].mibfamily, 'internet')
        self.assertEqual(s.SNMP.views[0].name, 'NOCViewRO')
        self.assertEqual(s.SNMP.views[1].included, True)
        self.assertEqual(s.SNMP.views[1].excluded, False)
        self.assertEqual(s.SNMP.views[1].correct, False)
        self.assertEqual(s.SNMP.views[1].mibfamily, 'internet')
        self.assertEqual(s.SNMP.views[1].name, 'NOCViewRW')
        self.assertEqual(s.SNMP.views[2].included, True)
        self.assertEqual(s.SNMP.views[2].excluded, False)
        self.assertEqual(s.SNMP.views[2].correct, False)
        self.assertEqual(s.SNMP.views[2].mibfamily, 'internet')
        self.assertEqual(s.SNMP.views[2].name, 'VoicePhones')
        # self.assertTrue(s.SNMP.traps)
        # self.assertEqual(len(s.SNMP.traps), 14)
        # self.assertTrue(s.SNMP.loggingips)
        # test = ['155.100.122.152', '155.100.122.113', '155.98.253.148', '155.98.253.149']
        # for log in s.SNMP.loggingips:
        #     self.assertIsInstance(log, IPv4Address)
        #     self.assertIn(str(log), test)
        self.assertIn(3, s.SNMP.version)
        self.assertNotIn(2, s.SNMP.version)

        # check the blades configuration
        self.assertTrue(s.blades)
        self.assertEqual(len(s.blades), 9)
        self.assertEqual(s.blades[0].ISOversion, '')
        self.assertFalse(s.blades[0].SUP)
        self.assertEqual(s.blades[0].modelnumber, 'WS-X4748-12X48U+E')
        self.assertEqual(s.blades[0].portcount, 48)
        self.assertTrue(s.blades[0].interfaces)
        self.assertEqual(len(s.blades[0].interfaces), 48)
        self.assertEqual(s.blades[1].ISOversion, '')
        self.assertFalse(s.blades[1].SUP)
        self.assertEqual(s.blades[1].modelnumber, 'WS-X4748-UPOE+E')
        self.assertEqual(s.blades[1].portcount, 48)
        self.assertTrue(s.blades[1].interfaces)
        self.assertEqual(len(s.blades[1].interfaces), 48)
        self.assertEqual(s.blades[4].ISOversion, '')
        self.assertTrue(s.blades[4].SUP)
        self.assertEqual(s.blades[4].modelnumber, 'WS-X45-SUP8-E')
        self.assertEqual(s.blades[4].portcount, 8)
        self.assertTrue(s.blades[4].interfaces)
        self.assertEqual(len(s.blades[4].interfaces), 8)
        portrange = range(1, 49)
        for portnumber, interface in s.blades[0].interfaces.items():
            self.assertTrue(interface)
            self.assertIsInstance(interface.mac_addresses, list)
            if interface.mac_addresses:
                for macaddress in interface.mac_addresses:
                    self.assertIsInstance(macaddress, EUI)
            self.assertIsInstance(interface, Interface)
            self.assertIn(int(portnumber), portrange)
            self.assertTrue(interface.fullname)
            self.assertIn(interface.portnumber, portrange)
        self.assertTrue(s.blades[0].interfaces['1'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['2'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['3'].InBcastPkts)
        self.assertTrue(s.blades[1].interfaces['1'].InBcastPkts)
        self.assertFalse(s.blades[1].interfaces['2'].InBcastPkts)
        self.assertTrue(s.blades[1].interfaces['3'].InBcastPkts)
        self.assertTrue(s.blades[2].interfaces['1'].InBcastPkts)
        self.assertTrue(s.blades[2].interfaces['2'].InBcastPkts)
        self.assertTrue(s.blades[2].interfaces['3'].InBcastPkts)


        # test assignment of CDP Neighbor
        self.assertIsInstance(s.cdpneighbors, list)
        self.assertEqual(len(s.cdpneighbors), 10)
        for neighbor in s.cdpneighbors:
            self.assertIsInstance(neighbor, Neighbor)
            self.assertIsInstance(neighbor.ip, ipaddress.IPv4Address)
            self.assertIsInstance(neighbor.interface, Interface)
        self.assertEqual(s.cdpneighbors[0].deviceid, 'r1-102tower.net.utah.edu')
        self.assertEqual(str(s.cdpneighbors[0].ip), '10.104.97.1')
        self.assertEqual(s.cdpneighbors[0].platform, 'CiscoC6880-X')
        self.assertEqual(s.cdpneighbors[0].interface.fullname, 'TenGigabitEthernet5/1')
        self.assertEqual(s.cdpneighbors[0].interface.portnumber, 1)
        self.assertEqual(s.cdpneighbors[0].duplex, 'full')

        # logging Info
        logging = ['155.98.253.244', '172.24.29.14', '10.71.24.11']
        for log in s.logging_data:
            self.assertIn(str(log[1]), logging)
            self.assertIsInstance(log[1], ipaddress.IPv4Address)

        # check vlans
        self.assertEqual(len(s.vlans), 12)
        self.assertEqual(s.vlans[0].name, '102tower-floor1-voip')
        self.assertEqual(s.vlans[0].number, 113)
        self.assertEqual(s.vlans[1].name, '102tower-floor1-USS')
        self.assertEqual(s.vlans[1].number, 114)
        self.assertEqual(s.vlans[2].name, '102tower-BI_Data_Science')
        self.assertEqual(s.vlans[2].number, 115)
        for macaddress in s.vlans[2].mac_addresses:
            self.assertIsInstance(macaddress, EUI)

        # test tacacs configuration
        self.assertIsInstance(s.tacacs, list)
        self.assertEqual(len(s.tacacs), 2)
        self.assertIsInstance(s.tacacs[0], TACACS)
        self.assertIsInstance(s.tacacs[0].server, ipaddress.IPv4Address)
        self.assertEqual(str(s.tacacs[0].server), '172.31.17.180')
        self.assertEqual(str(s.tacacs[0].name), 'TAC-EBC')
        self.assertIsInstance(s.tacacs[1].server, ipaddress.IPv4Address)
        self.assertEqual(str(s.tacacs[1].server), '10.64.32.5')
        self.assertEqual(str(s.tacacs[1].name), 'TAC-SECONDARY')

    def Catalyst_4948(self):
        pass
        # s = Switch(ipaddress="")
        # s.login()
        # s.getSwitchInfo()
        #
        #
        # #test getting the information properly
        # self.assertEqual(s.version_result,)
        # self.assertEqual(s.run_result,)
        # self.assertEqual(s.interface_result,)
        # self.assertEqual(s.interface_name_r,)
        # self.assertEqual(s.portdowntime_result),
        # self.assertEqual(s.inv_result,)
        # self.assertEqual(s.portcount_result,)
        # self.assertEqual(s.cdpnei_result,)
        # self.assertEqual(s.module_result,)
        # self.assertEqual(s.snmp_result,)
        # self.assertEqual(s.logging_data_result,)
        #
        # #Test the assigning of information to the correct objects
        # s.assignattributes()
        #
        # self.assertEqual(s.switchdescription, )
        # self.assertEqual(s.demarkInterface, )
        # self.assertEqual(s.switchInterface, )
        # self.assertEqual(s.device, )
        # self.assertEqual(s.modelnumber, )
        # self.assertEqual(s.IPAddress, )
        # self.assertEqual(s.switchdescription, )
        # self.assertEqual(s.demarkdescription, )
        # self.assertEqual(s.uplink, )
        # self.assertEqual(s.systemName, )
        # self.assertEqual(s.version, )
        # self.assertEqual(s.serial, )
        # self.assertEqual(s.stack, )
        # self.assertEqual(s.uptime, )
        # self.assertEqual(s.lastrestart, )
        # self.assertEqual(s.subnetmask, )
        # self.assertEqual(s.defaultgateway, )
        # self.assertEqual(s.bannername, )
        # self.assertEqual(s.portcount, )
        # self.assertEqual(s.blades, )
        # self.assertEqual(s.groupedvlans, )
        # self.assertEqual(s.version_result, )
        # self.assertEqual(s.run_result, )
        # self.assertEqual(s.portdowntime_result, )
        # self.assertEqual(s.portcount_result, )
        # self.assertEqual(s.inv_result, )
        # self.assertEqual(s.cdpnei_result, )
        # self.assertEqual(s.module_result, )
        # self.assertEqual(s.chassis, )
        # self.assertEqual(s.hostname, )
        # self.assertEqual(s.link, )
        # self.assertEqual(s.cdpneighbors, )
        # self.assertEqual(s.SNMP, )
        # self.assertEqual(s.interface_result, )
        # self.assertEqual(s.ACL, )
        # self.assertEqual(s.nexus, )
        # self.assertEqual(s.SFPs, )
        # self.assertEqual(s.vlansints, )
        # self.assertEqual(s.conn, )
        # self.assertEqual(s.node, )
        # self.assertEqual(s.conn, )
        # self.assertEqual(s.node, )
        # # Location variables
        # self.assertEqual(s.roomnumber, )
        # self.assertEqual(s.buildingname, )
        # self.assertEqual(s.buildnumber, )
        # self.assertEqual(s.racknumber, )
        # # ACL variables
        # self.assertEqual(s.acl_correct_status, )
        # self.assertEqual(s.acl_data, )
        #
        # # Logging variables
        # self.assertEqual(s.logging_data_result, )
        # self.assertEqual(s.logging_data, )
        # self.assertEqual(s.should_overwrite_logging, )
        # self.assertEqual(s.mgmt_vlan, )

    def Catalyst_6880(self):
        pass
        # s = Switch(ipaddress="")
        # s.login()
        # s.getSwitchInfo()
        #
        #
        # #test getting the information properly
        # self.assertEqual(s.version_result,)
        # self.assertEqual(s.run_result,)
        # self.assertEqual(s.interface_result,)
        # self.assertEqual(s.interface_name_r,)
        # self.assertEqual(s.portdowntime_result),
        # self.assertEqual(s.inv_result,)
        # self.assertEqual(s.portcount_result,)
        # self.assertEqual(s.cdpnei_result,)
        # self.assertEqual(s.module_result,)
        # self.assertEqual(s.snmp_result,)
        # self.assertEqual(s.logging_data_result,)
        #
        # #Test the assigning of information to the correct objects
        # s.assignattributes()
        #
        # self.assertEqual(s.switchdescription, )
        # self.assertEqual(s.demarkInterface, )
        # self.assertEqual(s.switchInterface, )
        # self.assertEqual(s.device, )
        # self.assertEqual(s.modelnumber, )
        # self.assertEqual(s.IPAddress, )
        # self.assertEqual(s.switchdescription, )
        # self.assertEqual(s.demarkdescription, )
        # self.assertEqual(s.uplink, )
        # self.assertEqual(s.systemName, )
        # self.assertEqual(s.version, )
        # self.assertEqual(s.serial, )
        # self.assertEqual(s.stack, )
        # self.assertEqual(s.uptime, )
        # self.assertEqual(s.lastrestart, )
        # self.assertEqual(s.subnetmask, )
        # self.assertEqual(s.defaultgateway, )
        # self.assertEqual(s.bannername, )
        # self.assertEqual(s.portcount, )
        # self.assertEqual(s.blades, )
        # self.assertEqual(s.groupedvlans, )
        # self.assertEqual(s.version_result, )
        # self.assertEqual(s.run_result, )
        # self.assertEqual(s.portdowntime_result, )
        # self.assertEqual(s.portcount_result, )
        # self.assertEqual(s.inv_result, )
        # self.assertEqual(s.cdpnei_result, )
        # self.assertEqual(s.module_result, )
        # self.assertEqual(s.chassis, )
        # self.assertEqual(s.hostname, )
        # self.assertEqual(s.link, )
        # self.assertEqual(s.cdpneighbors, )
        # self.assertEqual(s.SNMP, )
        # self.assertEqual(s.interface_result, )
        # self.assertEqual(s.ACL, )
        # self.assertEqual(s.nexus, )
        # self.assertEqual(s.SFPs, )
        # self.assertEqual(s.vlansints, )
        # self.assertEqual(s.conn, )
        # self.assertEqual(s.node, )
        # self.assertEqual(s.conn, )
        # self.assertEqual(s.node, )
        # # Location variables
        # self.assertEqual(s.roomnumber, )
        # self.assertEqual(s.buildingname, )
        # self.assertEqual(s.buildnumber, )
        # self.assertEqual(s.racknumber, )
        # # ACL variables
        # self.assertEqual(s.acl_correct_status, )
        # self.assertEqual(s.acl_data, )
        #
        # # Logging variables
        # self.assertEqual(s.logging_data_result, )
        # self.assertEqual(s.logging_data, )
        # self.assertEqual(s.should_overwrite_logging, )
        # self.assertEqual(s.mgmt_vlan, )

    def Catalyst_9300(self):
        pass
        # s = Switch(ipaddress="")
        # s.login()
        # s.getSwitchInfo()
        #
        #
        # #test getting the information properly
        # self.assertEqual(s.version_result,)
        # self.assertEqual(s.run_result,)
        # self.assertEqual(s.interface_result,)
        # self.assertEqual(s.interface_name_r,)
        # self.assertEqual(s.portdowntime_result),
        # self.assertEqual(s.inv_result,)
        # self.assertEqual(s.portcount_result,)
        # self.assertEqual(s.cdpnei_result,)
        # self.assertEqual(s.module_result,)
        # self.assertEqual(s.snmp_result,)
        # self.assertEqual(s.logging_data_result,)
        #
        # #Test the assigning of information to the correct objects
        # s.assignattributes()
        #
        # self.assertEqual(s.switchdescription, )
        # self.assertEqual(s.demarkInterface, )
        # self.assertEqual(s.switchInterface, )
        # self.assertEqual(s.device, )
        # self.assertEqual(s.modelnumber, )
        # self.assertEqual(s.IPAddress, )
        # self.assertEqual(s.switchdescription, )
        # self.assertEqual(s.demarkdescription, )
        # self.assertEqual(s.uplink, )
        # self.assertEqual(s.systemName, )
        # self.assertEqual(s.version, )
        # self.assertEqual(s.serial, )
        # self.assertEqual(s.stack, )
        # self.assertEqual(s.uptime, )
        # self.assertEqual(s.lastrestart, )
        # self.assertEqual(s.subnetmask, )
        # self.assertEqual(s.defaultgateway, )
        # self.assertEqual(s.bannername, )
        # self.assertEqual(s.portcount, )
        # self.assertEqual(s.blades, )
        # self.assertEqual(s.groupedvlans, )
        # self.assertEqual(s.version_result, )
        # self.assertEqual(s.run_result, )
        # self.assertEqual(s.portdowntime_result, )
        # self.assertEqual(s.portcount_result, )
        # self.assertEqual(s.inv_result, )
        # self.assertEqual(s.cdpnei_result, )
        # self.assertEqual(s.module_result, )
        # self.assertEqual(s.chassis, )
        # self.assertEqual(s.hostname, )
        # self.assertEqual(s.link, )
        # self.assertEqual(s.cdpneighbors, )
        # self.assertEqual(s.SNMP, )
        # self.assertEqual(s.interface_result, )
        # self.assertEqual(s.ACL, )
        # self.assertEqual(s.nexus, )
        # self.assertEqual(s.SFPs, )
        # self.assertEqual(s.vlansints, )
        # self.assertEqual(s.conn, )
        # self.assertEqual(s.node, )
        # self.assertEqual(s.conn, )
        # self.assertEqual(s.node, )
        # # Location variables
        # self.assertEqual(s.roomnumber, )
        # self.assertEqual(s.buildingname, )
        # self.assertEqual(s.buildnumber, )
        # self.assertEqual(s.racknumber, )
        # # ACL variables
        # self.assertEqual(s.acl_correct_status, )
        # self.assertEqual(s.acl_data, )
        #
        # # Logging variables
        # self.assertEqual(s.logging_data_result, )
        # self.assertEqual(s.logging_data, )
        # self.assertEqual(s.should_overwrite_logging, )
        # self.assertEqual(s.mgmt_vlan, )

    def Catalyst_94010R(self):
        pass
        # s = Switch(ipaddress="")
        # s.login()
        # s.getSwitchInfo()
        #
        #
        # #test getting the information properly
        # self.assertEqual(s.version_result,)
        # self.assertEqual(s.run_result,)
        # self.assertEqual(s.interface_result,)
        # self.assertEqual(s.interface_name_r,)
        # self.assertEqual(s.portdowntime_result),
        # self.assertEqual(s.inv_result,)
        # self.assertEqual(s.portcount_result,)
        # self.assertEqual(s.cdpnei_result,)
        # self.assertEqual(s.module_result,)
        # self.assertEqual(s.snmp_result,)
        # self.assertEqual(s.logging_data_result,)
        #
        # #Test the assigning of information to the correct objects
        # s.assignattributes()
        #
        # self.assertEqual(s.switchdescription, )
        # self.assertEqual(s.demarkInterface, )
        # self.assertEqual(s.switchInterface, )
        # self.assertEqual(s.device, )
        # self.assertEqual(s.modelnumber, )
        # self.assertEqual(s.IPAddress, )
        # self.assertEqual(s.switchdescription, )
        # self.assertEqual(s.demarkdescription, )
        # self.assertEqual(s.uplink, )
        # self.assertEqual(s.systemName, )
        # self.assertEqual(s.version, )
        # self.assertEqual(s.serial, )
        # self.assertEqual(s.stack, )
        # self.assertEqual(s.uptime, )
        # self.assertEqual(s.lastrestart, )
        # self.assertEqual(s.subnetmask, )
        # self.assertEqual(s.defaultgateway, )
        # self.assertEqual(s.bannername, )
        # self.assertEqual(s.portcount, )
        # self.assertEqual(s.blades, )
        # self.assertEqual(s.groupedvlans, )
        # self.assertEqual(s.version_result, )
        # self.assertEqual(s.run_result, )
        # self.assertEqual(s.portdowntime_result, )
        # self.assertEqual(s.portcount_result, )
        # self.assertEqual(s.inv_result, )
        # self.assertEqual(s.cdpnei_result, )
        # self.assertEqual(s.module_result, )
        # self.assertEqual(s.chassis, )
        # self.assertEqual(s.hostname, )
        # self.assertEqual(s.link, )
        # self.assertEqual(s.cdpneighbors, )
        # self.assertEqual(s.SNMP, )
        # self.assertEqual(s.interface_result, )
        # self.assertEqual(s.ACL, )
        # self.assertEqual(s.nexus, )
        # self.assertEqual(s.SFPs, )
        # self.assertEqual(s.vlansints, )
        # self.assertEqual(s.conn, )
        # self.assertEqual(s.node, )
        # self.assertEqual(s.conn, )
        # self.assertEqual(s.node, )
        # # Location variables
        # self.assertEqual(s.roomnumber, )
        # self.assertEqual(s.buildingname, )
        # self.assertEqual(s.buildnumber, )
        # self.assertEqual(s.racknumber, )
        # # ACL variables
        # self.assertEqual(s.acl_correct_status, )
        # self.assertEqual(s.acl_data, )
        #
        # # Logging variables
        # self.assertEqual(s.logging_data_result, )
        # self.assertEqual(s.logging_data, )
        # self.assertEqual(s.should_overwrite_logging, )
        # self.assertEqual(s.mgmt_vlan, )

    def Catalyst_9407R(self):
        pass
        # s = Switch(ipaddress="")
        # s.login()
        # s.getSwitchInfo()
        #
        #
        # #test getting the information properly
        # self.assertEqual(s.version_result,)
        # self.assertEqual(s.run_result,)
        # self.assertEqual(s.interface_result,)
        # self.assertEqual(s.interface_name_r,)
        # self.assertEqual(s.portdowntime_result),
        # self.assertEqual(s.inv_result,)
        # self.assertEqual(s.portcount_result,)
        # self.assertEqual(s.cdpnei_result,)
        # self.assertEqual(s.module_result,)
        # self.assertEqual(s.snmp_result,)
        # self.assertEqual(s.logging_data_result,)
        #
        # #Test the assigning of information to the correct objects
        # s.assignattributes()
        #
        # self.assertEqual(s.switchdescription, )
        # self.assertEqual(s.demarkInterface, )
        # self.assertEqual(s.switchInterface, )
        # self.assertEqual(s.device, )
        # self.assertEqual(s.modelnumber, )
        # self.assertEqual(s.IPAddress, )
        # self.assertEqual(s.switchdescription, )
        # self.assertEqual(s.demarkdescription, )
        # self.assertEqual(s.uplink, )
        # self.assertEqual(s.systemName, )
        # self.assertEqual(s.version, )
        # self.assertEqual(s.serial, )
        # self.assertEqual(s.stack, )
        # self.assertEqual(s.uptime, )
        # self.assertEqual(s.lastrestart, )
        # self.assertEqual(s.subnetmask, )
        # self.assertEqual(s.defaultgateway, )
        # self.assertEqual(s.bannername, )
        # self.assertEqual(s.portcount, )
        # self.assertEqual(s.blades, )
        # self.assertEqual(s.groupedvlans, )
        # self.assertEqual(s.version_result, )
        # self.assertEqual(s.run_result, )
        # self.assertEqual(s.portdowntime_result, )
        # self.assertEqual(s.portcount_result, )
        # self.assertEqual(s.inv_result, )
        # self.assertEqual(s.cdpnei_result, )
        # self.assertEqual(s.module_result, )
        # self.assertEqual(s.chassis, )
        # self.assertEqual(s.hostname, )
        # self.assertEqual(s.link, )
        # self.assertEqual(s.cdpneighbors, )
        # self.assertEqual(s.SNMP, )
        # self.assertEqual(s.interface_result, )
        # self.assertEqual(s.ACL, )
        # self.assertEqual(s.nexus, )
        # self.assertEqual(s.SFPs, )
        # self.assertEqual(s.vlansints, )
        # self.assertEqual(s.conn, )
        # self.assertEqual(s.node, )
        # self.assertEqual(s.conn, )
        # self.assertEqual(s.node, )
        # # Location variables
        # self.assertEqual(s.roomnumber, )
        # self.assertEqual(s.buildingname, )
        # self.assertEqual(s.buildnumber, )
        # self.assertEqual(s.racknumber, )
        # # ACL variables
        # self.assertEqual(s.acl_correct_status, )
        # self.assertEqual(s.acl_data, )
        #
        # # Logging variables
        # self.assertEqual(s.logging_data_result, )
        # self.assertEqual(s.logging_data, )
        # self.assertEqual(s.should_overwrite_logging, )
        # self.assertEqual(s.mgmt_vlan, )

class TestSwitchObject(unittest.TestCase):
    # @patch('paramiko.SSHClient.connect', side_effect=mocked_creation_SSH_paramiko)
    @patch('paramiko.channel.Channel.recv', side_effect=mocked_creation_SSH_paramiko_channel)
    def test_read_to_write_config(self,test_send):
        """
        Tests that a switch object is able to read from all the approved switch types, and when writing it back out
        the syntax is the same
        :return:
        """
        switches_info = [ws_c3560cx_8pc_s,
                      c29xx,c36xx,
                      c38xx,
                      c9407r,
                      c4510r_e_,
                      c94010r,
                      c3560cg_8pc_s,
                      c3560x_24_poe,
                      c3650_48pq_e,
                      c9300_series,
                      c9332pq,
                      c93180yc_fx]
        #TODO work on Mocking the channel class
        for s in switches_info:
            switch = Stack(s.ip_address)
            switch.login()

class assign_attributes():
    def WS_C3560CX_8PC_S(self):
        s = Stack('172.31.16.52')
        s.version_results = """Cisco IOS Software, C3560CX Software (C3560CX-UNIVERSALK9-M), Version 15.2(3)E3, RELEASE SOFTWARE (fc3)
    Technical Support: http://www.cisco.com/techsupport
    Copyright (c) 1986-2016 by Cisco Systems, Inc.
    Compiled Wed 13-Jan-16 23:08 by prod_rel_team
    
    ROM: Bootstrap program is C3560CX boot loader
    BOOTLDR: C3560CX Boot Loader (C3560CX-HBOOT-M) Version 15.2(3r)E2, RELEASE SOFTWARE (fc2)
    
    sx1-482-102tower-5th-test uptime is 15 weeks, 2 hours, 28 minutes
    System returned to ROM by power-on
    System restarted at 08:06:30 MDT Thu Aug 5 2021
    System image file is "flash:/c3560cx-universalk9-mz.152-3.E3/c3560cx-universalk9-mz.152-3.E3.bin"
    Last reload reason: power-on
    
    
    
    This product contains cryptographic features and is subject to United
    States and local country laws governing import, export, transfer and
    use. Delivery of Cisco cryptographic products does not imply
    third-party authority to import, export, distribute or use encryption.
    Importers, exporters, distributors and users are responsible for
    compliance with U.S. and local country laws. By using this product you
    agree to comply with applicable laws and regulations. If you are unable
    to comply with U.S. and local laws, return this product immediately.
    
    A summary of U.S. laws governing Cisco cryptographic products may be found at:
    http://www.cisco.com/wwl/export/crypto/tool/stqrg.html
    
    If you require further assistance please contact us by sending email to
    export@cisco.com.
    
    License Level: ipbase
    License Type: Default. No valid license found.
    Next reload license Level: ipbase
    
    cisco WS-C3560CX-8PC-S (APM86XXX) processor (revision G0) with 524288K bytes of memory.
    Processor board ID FOC2011Z16A
    Last reset from power-on
    2 Virtual Ethernet interfaces
    12 Gigabit Ethernet interfaces
    The password-recovery mechanism is enabled.
    
    512K bytes of flash-simulated non-volatile configuration memory.
    Base ethernet MAC Address       : 04:2A:E2:61:91:00
    Motherboard assembly number     : 73-16471-04
    Power supply part number        : 341-0675-02
    Motherboard serial number       : FOC201034W8
    Power supply serial number      : LIT19510PHH
    Model revision number           : G0
    Motherboard revision number     : A0
    Model number                    : WS-C3560CX-8PC-S
    System serial number            : FOC2011Z16A
    Top Assembly Part Number        : 68-5359-02
    Top Assembly Revision Number    : D0
    Version ID                      : V02
    CLEI Code Number                : CMM1S10DRA
    Hardware Board Revision Number  : 0x02
    
    
              Switch Ports Model                     SW Version            SW Image                 
    ------ ----- -----                     ----------            ----------               
    *    1 12    WS-C3560CX-8PC-S          15.2(3)E3             C3560CX-UNIVERSALK9-M    
    
    
    Configuration register is 0xF"""
        s.run_resul = """Building configuration...

Current configuration : 13009 bytes
!
! Last configuration change at 09:59:19 MDT Fri Nov 5 2021 by u1377551
! NVRAM config last updated at 09:24:27 MDT Fri Nov 5 2021 by u1377551
!
version 15.2
no service pad
service timestamps debug datetime msec localtime
service timestamps log datetime msec localtime
service password-encryption
!
hostname sx1-482-102tower-5th-test
!
boot-start-marker
boot-end-marker
!
logging buffered notifications
logging console critical
enable secret 5 $1$UCvO$VE5h11OUQ26MvSNmvQmVK1
!
aaa new-model
!
!
aaa group server tacacs+ NOC-TAC
 server name TAC-EBC
 server name TAC-SECONDARY
!
aaa authentication login default group NOC-TAC line enable
aaa authentication login console enable
aaa authentication enable default group NOC-TAC enable
aaa authorization exec default group NOC-TAC 
aaa authorization commands 0 default group NOC-TAC 
aaa authorization commands 1 default group NOC-TAC 
aaa authorization commands 15 default group NOC-TAC 
aaa accounting exec default start-stop group NOC-TAC
aaa accounting commands 1 default stop-only group NOC-TAC
aaa accounting commands 15 default stop-only group NOC-TAC
aaa accounting connection default start-stop group NOC-TAC
aaa accounting system default start-stop group NOC-TAC
!
!
!
!
!
!
aaa session-id common
clock timezone MST -7 0
clock summer-time MDT recurring
system mtu routing 1500
no ip source-route
!
!
ip dhcp snooping
ip domain-name net.utah.edu
ip name-server 172.20.120.20
ip device tracking probe auto-source override
ip device tracking probe delay 60
vtp domain vtp-482-102tower
          vtp mode transparent
!
!
!
!
!
udld aggressive

authentication mac-move permit
!
!
crypto pki trustpoint DNAC-CA
 enrollment mode ra
 enrollment terminal
 usage ssl-client
 revocation-check crl none
!
!
crypto pki certificate chain DNAC-CA
 certificate ca 00C9F7D588881F3773
  30820397 3082027F A0030201 02020900 C9F7D588 881F3773 300D0609 2A864886 
  F70D0101 0B050030 62312D30 2B060355 04030C24 34363938 61633464 2D626465 
  632D6239 31332D62 3033622D 30303064 36313839 30313061 31163014 06035504 
  0A0C0D43 6973636F 20537973 74656D73 31193017 06035504 0B0C1043 6973636F 
  20444E41 2043656E 74657230 1E170D32 31303130 35323132 3434395A 170D3233 
  31303032 32313234 34395A30 62312D30 2B060355 04030C24 34363938 61633464 
  2D626465 632D6239 31332D62 3033622D 30303064 36313839 30313061 31163014 
  06035504 0A0C0D43 6973636F 20537973 74656D73 31193017 06035504 0B0C1043 
  6973636F 20444E41 2043656E 74657230 82012230 0D06092A 864886F7 0D010101 
  05000382 010F0030 82010A02 82010100 D5A4D1B7 16057688 A84C66BE E00F9A3C 
  520CA455 4DA315B1 9EFA46D9 59D2C083 22893419 C93AE0DC 1F15100A 47DAFD07 
  C009E465 09C914C7 E8826EAA 4FE77E2E 9B6BE141 D5A229DB C1FEF2DA C4D6ABBB 
  3A4E8F0C CDEB4454 20E50768 DCC92D8B B14EA3E7 330050A6 86820052 028BCD71 
  DD17D713 1BF77C6E 90395E7B C3A52E08 84521424 377FE6FC 67A86A22 A81798E1 
  2DFACB68 7A779DE9 147CF237 A9F7C164 07173B6A 704AC66B 9424C1CF B8634A15 
  B8940282 A0C7997F 3A93D52D EE2728A0 761FFE10 C5C5C299 544583BA 5595F226 
  FA2F9A37 A6E65572 36E2FB4D 72006D0B ABD99113 F8C04A34 CCF1B329 9F823AB1 
  6C3A750A 3D0423CD 4745E5CF 627CA183 02030100 01A35030 4E301D06 03551D0E 
  04160414 9EE306C8 49D7F68A C3016D4D 5FECF9EE B94C2D40 301F0603 551D2304 
  18301680 149EE306 C849D7F6 8AC3016D 4D5FECF9 EEB94C2D 40300C06 03551D13 
  04053003 0101FF30 0D06092A 864886F7 0D01010B 05000382 0101007D 7C5D8834 
  C74D1256 665F3C40 58B28995 6F58EA58 44377AD4 5400D68D 61700C60 9FDFF72C 
  143FAF3F 0B82C5B1 67A7C0FF 6E52E865 5F74D09D 4FBD7A2E 1D7CFF5D 0CE4FBA1 
  3CC73924 41D6DDDC 5958690E CF9017FA 295D95E7 EAE738C2 44F44567 53DBAA15 
  8B0C7133 D0CF2666 A3987614 9B378116 9712B4D2 1326F6F9 DED00762 7E9DE14C 
  1656A2B0 E3085FAF EF2311D6 2CD7A1FE 21627D26 329ADB4D F39A03D3 E68C1B9C 
  A96690E5 E8983340 98F7AAEE B791ACB9 B79B3553 077132E8 E6FC71CB 49F93FCE 
  C29F0797 F782469D 5F879951 65B20217 217E252D 767AAED1 4B9469B9 C1702178 
  40CF7015 3C2EB222 63697C09 013028DD AB8B9FD8 D87309B3 12C584
  	quit
spanning-tree mode rapid-pvst
spanning-tree extend system-id
!
!
!
!
vlan internal allocation policy ascending
!
vlan 10
           name test-private-vlan
!
vlan 151
 name floor5-campus
!
vlan 333
 name CCURE-FM
!
vlan 440
 name ebc-892komas-wireless
!
vlan 444
 name 482-VOIP
!
vlan 449
 name ebc-892komas-ITS
!
vlan 555
 name 482-lan
!
vlan 589
 name this-is-a-test
!
vlan 800
 name 482-102tower-m
!
vlan 986
 name noc-wrkstns-inside
!
vlan 994
 name ebc-NOC-AP-PRIMING
!
vlan 999
 name hello
!
lldp run
!
! 
!
!
!
!
!
!
!
!
interface GigabitEthernet0/1
 switchport access vlan 151
 switchport mode access
 switchport voice vlan 444
 ip device tracking maximum 65535
 spanning-tree portfast
!
interface GigabitEthernet0/2
 switchport access vlan 999
 switchport mode access
 switchport voice vlan 444
 ip device tracking maximum 65535
 shutdown
           spanning-tree portfast
!
interface GigabitEthernet0/3
 description Workstation/VOIP
 switchport access vlan 333
 switchport mode access
 ip device tracking maximum 65535
 shutdown
 spanning-tree portfast
!
interface GigabitEthernet0/4
 ip device tracking maximum 65535
 shutdown
!
interface GigabitEthernet0/5
 ip device tracking maximum 65535
 shutdown
!
interface GigabitEthernet0/6
 ip device tracking maximum 65535
 shutdown
!
interface GigabitEthernet0/7
 switchport access vlan 789
 switchport mode access
 ip device tracking maximum 65535
 shutdown
 spanning-tree portfast
!
interface GigabitEthernet0/8
 shutdown
!
interface GigabitEthernet0/9
 description Main Uplink
 switchport mode trunk
 no keepalive
!
interface GigabitEthernet0/10
 ip device tracking maximum 65535
 shutdown
 no keepalive
!
interface GigabitEthernet0/11
 ip device tracking maximum 65535
!
interface GigabitEthernet0/12
 ip device tracking maximum 65535
!
interface Vlan1
 no ip address
 no ip route-cache
 shutdown
!
interface Vlan800
 description 482-102tower-m
 ip address 172.31.16.52 255.255.255.0
 no ip route-cache
!
ip default-gateway 172.31.16.1
          ip forward-protocol nd
no ip http server
no ip http secure-server
ip http client source-interface Vlan800
!
ip ssh source-interface Vlan800
ip ssh version 2
!
!
ip sla enable reaction-alerts
logging facility local6
logging source-interface Vlan800
logging host 155.98.204.52
logging host 155.98.253.228
access-list 70 remark == Config generated 2019-04-24 ==
access-list 70 remark == Update 5-17-2018 RT and TS ==
access-list 70 remark ======= NOC SNMP RO =======
access-list 70 permit 10.64.2.70
access-list 70 permit 155.100.126.163
access-list 70 permit 155.100.126.162
access-list 70 permit 172.20.150.100
access-list 70 permit 155.98.164.192 0.0.0.31
access-list 70 permit 155.99.254.128 0.0.0.127
access-list 70 permit 155.98.253.0 0.0.0.255
access-list 70 deny   any log
access-list 71 remark ======= NOC SNMP RW =======
access-list 71 permit 10.64.2.70
access-list 71 permit 155.100.126.163
access-list 71 permit 155.100.126.162
access-list 71 permit 172.20.150.100
access-list 71 permit 155.99.254.128 0.0.0.127
access-list 71 permit 155.98.253.0 0.0.0.255
access-list 71 deny   any log
access-list 199 remark ====== line VTY 0-15 inbound =====
access-list 199 remark ====== Update 5-17-2018 RT and TS =====
access-list 199 remark ------ NetOpS Workstations-Servers-Pollers --------
access-list 199 permit tcp 155.98.253.0 0.0.0.255 any eq 22
access-list 199 permit tcp host 172.20.150.100 any eq 22
access-list 199 permit tcp host 155.100.126.162 any eq 22
access-list 199 permit tcp host 155.100.126.163 any eq 22
access-list 199 permit tcp host 10.64.2.70 any eq 22
access-list 199 remark ----- door1 & door2 ---------------------------
access-list 199 permit tcp host 155.99.239.130 any eq 22
access-list 199 permit tcp host 155.97.152.244 any eq 22
access-list 199 remark ----- NOC Citrix IP -------------------------
access-list 199 permit tcp host 155.100.123.72 any eq 22
access-list 199 remark ----- Wireless Subnet -------------------------
access-list 199 permit tcp 155.99.254.128 0.0.0.127 any eq 22
access-list 199 remark ------ VPN Connections ------------------------
access-list 199 permit tcp 155.101.243.0 0.0.0.31 any eq 22
access-list 199 permit tcp 155.98.164.192 0.0.0.31 any eq 22
access-list 199 deny   ip any any log
!
snmp-server group NOCGrv3RO v3 priv read NOCViewRO access 70
snmp-server group NOCGrv3RO v3 auth context vlan- match prefix 
snmp-server group NOCGrv3RW v3 priv write NOCViewRW access 71
snmp-server group NONUserv3Rw v3 priv 
snmp-server view NOCViewRO internet included
snmp-server view NOCViewRW internet included
          snmp-server trap-source Vlan800
snmp-server location Bldg. 482 Room 5363
snmp-server contact BC-none Y-none
snmp-server enable traps snmp authentication linkdown linkup coldstart warmstart
snmp-server enable traps flowmon
snmp-server enable traps transceiver all
snmp-server enable traps call-home message-send-fail server-fail
snmp-server enable traps tty
snmp-server enable traps eigrp
snmp-server enable traps ospf state-change
snmp-server enable traps ospf errors
snmp-server enable traps ospf retransmit
snmp-server enable traps ospf lsa
snmp-server enable traps ospf cisco-specific state-change nssa-trans-change
snmp-server enable traps ospf cisco-specific state-change shamlink interface
snmp-server enable traps ospf cisco-specific state-change shamlink neighbor
snmp-server enable traps ospf cisco-specific errors
snmp-server enable traps ospf cisco-specific retransmit
snmp-server enable traps ospf cisco-specific lsa
snmp-server enable traps license
snmp-server enable traps auth-framework sec-violation
snmp-server enable traps bfd
snmp-server enable traps cef resource-failure peer-state-change peer-fib-state-change inconsistency
snmp-server enable traps cluster
snmp-server enable traps config-copy
snmp-server enable traps config
snmp-server enable traps config-ctid
snmp-server enable traps trustsec-sxp conn-srcaddr-err msg-parse-err conn-config-err binding-err conn-up conn-down binding-expn-fail oper-nodeid-change binding-conflict
snmp-server enable traps energywise
snmp-server enable traps fru-ctrl
snmp-server enable traps entity
snmp-server enable traps event-manager
snmp-server enable traps hsrp
snmp-server enable traps ipmulticast
snmp-server enable traps ike policy add
snmp-server enable traps ike policy delete
snmp-server enable traps ike tunnel start
snmp-server enable traps ike tunnel stop
snmp-server enable traps ipsec cryptomap add
snmp-server enable traps ipsec cryptomap delete
snmp-server enable traps ipsec cryptomap attach
snmp-server enable traps ipsec cryptomap detach
snmp-server enable traps ipsec tunnel start
snmp-server enable traps ipsec tunnel stop
snmp-server enable traps ipsec too-many-sas
snmp-server enable traps ospfv3 state-change
snmp-server enable traps ospfv3 errors
snmp-server enable traps power-ethernet group 1
snmp-server enable traps power-ethernet police
snmp-server enable traps pim neighbor-change rp-mapping-change invalid-pim-message
snmp-server enable traps cpu threshold
snmp-server enable traps rep
snmp-server enable traps ipsla
snmp-server enable traps vstack
snmp-server enable traps bridge newroot topologychange
snmp-server enable traps stpx inconsistency root-inconsistency loop-inconsistency
snmp-server enable traps syslog
snmp-server enable traps vtp
          snmp-server enable traps vlancreate
snmp-server enable traps vlandelete
snmp-server enable traps flash insertion removal
snmp-server enable traps port-security
snmp-server enable traps envmon fan shutdown supply temperature status
snmp-server enable traps stackwise
snmp-server enable traps bulkstat collection transfer
snmp-server enable traps vrfmib vrf-up vrf-down vnet-trunk-up vnet-trunk-down
snmp-server enable traps errdisable
snmp-server enable traps mac-notification change move threshold
snmp-server enable traps vlan-membership
snmp-server host 155.98.253.228 version 3 priv NONUserv3Rw 
snmp ifmib ifindex persist
tacacs server TAC-EBC
 address ipv4 172.31.17.180
 key 7 143E560E25402F09042A2A74
tacacs server TAC-SECONDARY
 address ipv4 10.64.32.5
 key 7 013A4201724F032D014E5748
!
!
privilege exec level 1 show configuration
privilege exec level 1 show
banner login ^C
sx1-482-102tower-5th-test

University of Utah Network:  All use of this device must comply
with the University of Utah policies and procedures.  Any use of
this device, whether deliberate or not will be held legally
responsible.  See University of Utah Information Security
Policy (4-004) for details.

Problems within the University of Utah's network should be reported
by calling the Campus Helpdesk at 581-4000, or via e-mail at
helpdesk@utah.edu

DO NOT LOGIN
if you are not authorized by NetCom at the University of Utah.

^C
!
line con 0
 exec-timeout 15 0
 password 7 046E1F0707230D1D5D
 login authentication console
 stopbits 1
line vty 0 4
 access-class 199 in
 exec-timeout 30 0
 password 7 1422060A04066B7870
 transport input ssh
line vty 5 15
 access-class 199 in
 exec-timeout 30 0
 password 7 1422060A04066B7870
 transport input ssh
!
!
end"""
        s.status_result = """Port      Name               Status       Vlan       Duplex  Speed Type 
    Gi0/1                        notconnect   151          auto   auto 10/100/1000BaseTX
    Gi0/2                        disabled     999          auto   auto 10/100/1000BaseTX
    Gi0/3     Workstation/VOIP   disabled     333          auto   auto 10/100/1000BaseTX
    Gi0/4                        disabled     1            auto   auto 10/100/1000BaseTX
    Gi0/5                        disabled     1            auto   auto 10/100/1000BaseTX
    Gi0/6                        disabled     1            auto   auto 10/100/1000BaseTX
    Gi0/7                        disabled     789          auto   auto 10/100/1000BaseTX
    Gi0/8                        disabled     1            auto   auto 10/100/1000BaseTX
    Gi0/9     Main Uplink        connected    trunk      a-full a-1000 10/100/1000BaseTX
    Gi0/10                       disabled     1            auto   auto 10/100/1000BaseTX
    Gi0/11                       notconnect   1            auto   auto Not Present
    Gi0/12                       notconnect   1            auto   auto Not Present"""
        s.interface_result = """interface GigabitEthernet0/1
     switchport access vlan 151
     switchport mode access
     switchport voice vlan 444
     ip device tracking maximum 65535
     spanning-tree portfast
    interface GigabitEthernet0/2
     switchport access vlan 999
     switchport mode access
     switchport voice vlan 444
     ip device tracking maximum 65535
     shutdown
     spanning-tree portfast
    interface GigabitEthernet0/3
     description Workstation/VOIP
     switchport access vlan 333
     switchport mode access
     ip device tracking maximum 65535
     shutdown
     spanning-tree portfast
    interface GigabitEthernet0/4
     ip device tracking maximum 65535
     shutdown
    interface GigabitEthernet0/5
     ip device tracking maximum 65535
     shutdown
    interface GigabitEthernet0/6
     ip device tracking maximum 65535
     shutdown
    interface GigabitEthernet0/7
     switchport access vlan 789
     switchport mode access
     ip device tracking maximum 65535
     shutdown
     spanning-tree portfast
    interface GigabitEthernet0/8
     shutdown
    interface GigabitEthernet0/9
     description Main Uplink
     switchport mode trunk
     no keepalive
    interface GigabitEthernet0/10
     ip device tracking maximum 65535
     shutdown
     no keepalive
    interface GigabitEthernet0/11
     ip device tracking maximum 65535
    interface GigabitEthernet0/12
     ip device tracking maximum 65535
    interface Vlan1
     no ip address
     no ip route-cache
     shutdown
    interface Vlan800
     description 482-102tower-m
     ip address 172.31.16.52 255.255.255.0
     no ip route-cache
    ip http client source-interface Vlan800
    ip ssh source-interface Vlan800
              logging source-interface Vlan800
    snmp-server enable traps ospf cisco-specific state-change shamlink interface
    """
        s.interface_name_r = """^
    % Invalid input detected at '^' marker.
    
    """
        s.portdowntime_result = """Vlan1 is administratively down, line protocol is down 
      Hardware is EtherSVI, address is 042a.e261.9140 (bia 042a.e261.9140)
      MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
         reliability 255/255, txload 1/255, rxload 1/255
      Encapsulation ARPA, loopback not set
      Keepalive not supported 
      ARP type: ARPA, ARP Timeout 04:00:00
      Last input never, output never, output hang never
      Last clearing of "" counters never
      Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
      Queueing strategy: fifo
      Output queue: 0/40 (size/max)
      5 minute input rate 0 bits/sec, 0 packets/sec
      5 minute output rate 0 bits/sec, 0 packets/sec
         0 packets input, 0 bytes, 0 no buffer
         Received 0 broadcasts (0 IP multicasts)
         0 runts, 0 giants, 0 throttles 
         0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
         0 packets output, 0 bytes, 0 underruns
         0 output errors, 1 interface resets
         0 unknown protocol drops
         0 output buffer failures, 0 output buffers swapped out
    Vlan800 is up, line protocol is up 
      Hardware is EtherSVI, address is 042a.e261.9141 (bia 042a.e261.9141)
      Description: 482-102tower-m
      Internet address is 172.31.16.52/24
      MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
         reliability 255/255, txload 1/255, rxload 1/255
      Encapsulation ARPA, loopback not set
      Keepalive not supported 
      ARP type: ARPA, ARP Timeout 04:00:00
      Last input 00:00:00, output 00:00:00, output hang never
      Last clearing of "" counters never
      Input queue: 1/75/0/0 (size/max/drops/flushes); Total output drops: 0
      Queueing strategy: fifo
      Output queue: 0/40 (size/max)
      5 minute input rate 1000 bits/sec, 1 packets/sec
      5 minute output rate 1000 bits/sec, 1 packets/sec
         1419434 packets input, 110097206 bytes, 0 no buffer
         Received 0 broadcasts (0 IP multicasts)
         0 runts, 0 giants, 0 throttles 
         0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
         103991 packets output, 15282667 bytes, 0 underruns
         0 output errors, 2 interface resets
         0 unknown protocol drops
         0 output buffer failures, 0 output buffers swapped out
    GigabitEthernet0/1 is down, line protocol is down (notconnect) 
      Hardware is Gigabit Ethernet, address is 042a.e261.9101 (bia 042a.e261.9101)
      MTU 9198 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
         reliability 255/255, txload 1/255, rxload 1/255
      Encapsulation ARPA, loopback not set
      Keepalive set (10 sec)
      Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
      input flow-control is off, output flow-control is unsupported 
      ARP type: ARPA, ARP Timeout 04:00:00
      Last input 4w0d, output 4w0d, output hang never
      Last clearing of "" counters never
      Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
      Queueing strategy: fifo
                Output queue: 0/40 (size/max)
      5 minute input rate 0 bits/sec, 0 packets/sec
      5 minute output rate 0 bits/sec, 0 packets/sec
         154 packets input, 31846 bytes, 0 no buffer
         Received 61 broadcasts (6 multicasts)
         0 runts, 0 giants, 0 throttles 
         1 input errors, 1 CRC, 0 frame, 0 overrun, 0 ignored
         0 watchdog, 6 multicast, 0 pause input
         0 input packets with dribble condition detected
         1366 packets output, 294795 bytes, 0 underruns
         0 output errors, 0 collisions, 6 interface resets
         0 unknown protocol drops
         0 babbles, 0 late collision, 0 deferred
         0 lost carrier, 0 no carrier, 0 pause output
         0 output buffer failures, 0 output buffers swapped out
    GigabitEthernet0/2 is administratively down, line protocol is down (disabled) 
      Hardware is Gigabit Ethernet, address is 042a.e261.9102 (bia 042a.e261.9102)
      MTU 9198 bytes, BW 10000 Kbit/sec, DLY 1000 usec, 
         reliability 255/255, txload 1/255, rxload 1/255
      Encapsulation ARPA, loopback not set
      Keepalive set (10 sec)
      Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
      input flow-control is off, output flow-control is unsupported 
      ARP type: ARPA, ARP Timeout 04:00:00
      Last input never, output never, output hang never
      Last clearing of "" counters never
      Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
      Queueing strategy: fifo
      Output queue: 0/40 (size/max)
      5 minute input rate 0 bits/sec, 0 packets/sec
      5 minute output rate 0 bits/sec, 0 packets/sec
         0 packets input, 0 bytes, 0 no buffer
         Received 0 broadcasts (0 multicasts)
         0 runts, 0 giants, 0 throttles 
         0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
         0 watchdog, 0 multicast, 0 pause input
         0 input packets with dribble condition detected
         0 packets output, 0 bytes, 0 underruns
         0 output errors, 0 collisions, 0 interface resets
         0 unknown protocol drops
         0 babbles, 0 late collision, 0 deferred
         0 lost carrier, 0 no carrier, 0 pause output
         0 output buffer failures, 0 output buffers swapped out
    GigabitEthernet0/3 is administratively down, line protocol is down (disabled) 
      Hardware is Gigabit Ethernet, address is 042a.e261.9103 (bia 042a.e261.9103)
      Description: Workstation/VOIP
      MTU 9198 bytes, BW 10000 Kbit/sec, DLY 1000 usec, 
         reliability 255/255, txload 1/255, rxload 1/255
      Encapsulation ARPA, loopback not set
      Keepalive set (10 sec)
      Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
      input flow-control is off, output flow-control is unsupported 
      ARP type: ARPA, ARP Timeout 04:00:00
      Last input never, output never, output hang never
      Last clearing of "" counters never
      Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
      Queueing strategy: fifo
      Output queue: 0/40 (size/max)
      5 minute input rate 0 bits/sec, 0 packets/sec
                5 minute output rate 0 bits/sec, 0 packets/sec
         0 packets input, 0 bytes, 0 no buffer
         Received 0 broadcasts (0 multicasts)
         0 runts, 0 giants, 0 throttles 
         0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
         0 watchdog, 0 multicast, 0 pause input
         0 input packets with dribble condition detected
         0 packets output, 0 bytes, 0 underruns
         0 output errors, 0 collisions, 0 interface resets
         0 unknown protocol drops
         0 babbles, 0 late collision, 0 deferred
         0 lost carrier, 0 no carrier, 0 pause output
         0 output buffer failures, 0 output buffers swapped out
    GigabitEthernet0/4 is administratively down, line protocol is down (disabled) 
      Hardware is Gigabit Ethernet, address is 042a.e261.9104 (bia 042a.e261.9104)
      MTU 9198 bytes, BW 10000 Kbit/sec, DLY 1000 usec, 
         reliability 255/255, txload 1/255, rxload 1/255
      Encapsulation ARPA, loopback not set
      Keepalive set (10 sec)
      Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
      input flow-control is off, output flow-control is unsupported 
      ARP type: ARPA, ARP Timeout 04:00:00
      Last input never, output never, output hang never
      Last clearing of "" counters never
      Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
      Queueing strategy: fifo
      Output queue: 0/40 (size/max)
      5 minute input rate 0 bits/sec, 0 packets/sec
      5 minute output rate 0 bits/sec, 0 packets/sec
         0 packets input, 0 bytes, 0 no buffer
         Received 0 broadcasts (0 multicasts)
         0 runts, 0 giants, 0 throttles 
         0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
         0 watchdog, 0 multicast, 0 pause input
         0 input packets with dribble condition detected
         0 packets output, 0 bytes, 0 underruns
         0 output errors, 0 collisions, 0 interface resets
         0 unknown protocol drops
         0 babbles, 0 late collision, 0 deferred
         0 lost carrier, 0 no carrier, 0 pause output
         0 output buffer failures, 0 output buffers swapped out
    GigabitEthernet0/5 is administratively down, line protocol is down (disabled) 
      Hardware is Gigabit Ethernet, address is 042a.e261.9105 (bia 042a.e261.9105)
      MTU 9198 bytes, BW 10000 Kbit/sec, DLY 1000 usec, 
         reliability 255/255, txload 1/255, rxload 1/255
      Encapsulation ARPA, loopback not set
      Keepalive set (10 sec)
      Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
      input flow-control is off, output flow-control is unsupported 
      ARP type: ARPA, ARP Timeout 04:00:00
      Last input never, output never, output hang never
      Last clearing of "" counters never
      Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
      Queueing strategy: fifo
      Output queue: 0/40 (size/max)
      5 minute input rate 0 bits/sec, 0 packets/sec
      5 minute output rate 0 bits/sec, 0 packets/sec
         0 packets input, 0 bytes, 0 no buffer
         Received 0 broadcasts (0 multicasts)
                   0 runts, 0 giants, 0 throttles 
         0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
         0 watchdog, 0 multicast, 0 pause input
         0 input packets with dribble condition detected
         0 packets output, 0 bytes, 0 underruns
         0 output errors, 0 collisions, 1 interface resets
         0 unknown protocol drops
         0 babbles, 0 late collision, 0 deferred
         0 lost carrier, 0 no carrier, 0 pause output
         0 output buffer failures, 0 output buffers swapped out
    GigabitEthernet0/6 is administratively down, line protocol is down (disabled) 
      Hardware is Gigabit Ethernet, address is 042a.e261.9106 (bia 042a.e261.9106)
      MTU 9198 bytes, BW 10000 Kbit/sec, DLY 1000 usec, 
         reliability 255/255, txload 1/255, rxload 1/255
      Encapsulation ARPA, loopback not set
      Keepalive set (10 sec)
      Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
      input flow-control is off, output flow-control is unsupported 
      ARP type: ARPA, ARP Timeout 04:00:00
      Last input never, output never, output hang never
      Last clearing of "" counters never
      Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
      Queueing strategy: fifo
      Output queue: 0/40 (size/max)
      5 minute input rate 0 bits/sec, 0 packets/sec
      5 minute output rate 0 bits/sec, 0 packets/sec
         0 packets input, 0 bytes, 0 no buffer
         Received 0 broadcasts (0 multicasts)
         0 runts, 0 giants, 0 throttles 
         0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
         0 watchdog, 0 multicast, 0 pause input
         0 input packets with dribble condition detected
         0 packets output, 0 bytes, 0 underruns
         0 output errors, 0 collisions, 0 interface resets
         0 unknown protocol drops
         0 babbles, 0 late collision, 0 deferred
         0 lost carrier, 0 no carrier, 0 pause output
         0 output buffer failures, 0 output buffers swapped out
    GigabitEthernet0/7 is administratively down, line protocol is down (disabled) 
      Hardware is Gigabit Ethernet, address is 042a.e261.9107 (bia 042a.e261.9107)
      MTU 9198 bytes, BW 10000 Kbit/sec, DLY 1000 usec, 
         reliability 255/255, txload 1/255, rxload 1/255
      Encapsulation ARPA, loopback not set
      Keepalive set (10 sec)
      Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
      input flow-control is off, output flow-control is unsupported 
      ARP type: ARPA, ARP Timeout 04:00:00
      Last input never, output never, output hang never
      Last clearing of "" counters never
      Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
      Queueing strategy: fifo
      Output queue: 0/40 (size/max)
      5 minute input rate 0 bits/sec, 0 packets/sec
      5 minute output rate 0 bits/sec, 0 packets/sec
         0 packets input, 0 bytes, 0 no buffer
         Received 0 broadcasts (0 multicasts)
         0 runts, 0 giants, 0 throttles 
         0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
         0 watchdog, 0 multicast, 0 pause input
                   0 input packets with dribble condition detected
         0 packets output, 0 bytes, 0 underruns
         0 output errors, 0 collisions, 0 interface resets
         0 unknown protocol drops
         0 babbles, 0 late collision, 0 deferred
         0 lost carrier, 0 no carrier, 0 pause output
         0 output buffer failures, 0 output buffers swapped out
    GigabitEthernet0/8 is administratively down, line protocol is down (disabled) 
      Hardware is Gigabit Ethernet, address is 042a.e261.9108 (bia 042a.e261.9108)
      MTU 9198 bytes, BW 10000 Kbit/sec, DLY 1000 usec, 
         reliability 255/255, txload 1/255, rxload 1/255
      Encapsulation ARPA, loopback not set
      Keepalive set (10 sec)
      Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
      input flow-control is off, output flow-control is unsupported 
      ARP type: ARPA, ARP Timeout 04:00:00
      Last input 1w6d, output 1w6d, output hang never
      Last clearing of "" counters never
      Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
      Queueing strategy: fifo
      Output queue: 0/40 (size/max)
      5 minute input rate 0 bits/sec, 0 packets/sec
      5 minute output rate 0 bits/sec, 0 packets/sec
         240 packets input, 29082 bytes, 0 no buffer
         Received 159 broadcasts (111 multicasts)
         0 runts, 0 giants, 0 throttles 
         0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
         0 watchdog, 111 multicast, 0 pause input
         0 input packets with dribble condition detected
         1830 packets output, 223119 bytes, 0 underruns
         0 output errors, 0 collisions, 1 interface resets
         0 unknown protocol drops
         0 babbles, 0 late collision, 0 deferred
         0 lost carrier, 0 no carrier, 0 pause output
         0 output buffer failures, 0 output buffers swapped out
    GigabitEthernet0/9 is up, line protocol is up (connected) 
      Hardware is Gigabit Ethernet, address is 042a.e261.9109 (bia 042a.e261.9109)
      Description: Main Uplink
      MTU 9198 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
         reliability 255/255, txload 1/255, rxload 1/255
      Encapsulation ARPA, loopback not set
      Keepalive not set
      Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
      input flow-control is off, output flow-control is unsupported 
      ARP type: ARPA, ARP Timeout 04:00:00
      Last input 00:00:01, output 00:00:00, output hang never
      Last clearing of "" counters never
      Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
      Queueing strategy: fifo
      Output queue: 0/40 (size/max)
      5 minute input rate 8000 bits/sec, 8 packets/sec
      5 minute output rate 4000 bits/sec, 6 packets/sec
         81146258 packets input, 12406850632 bytes, 0 no buffer
         Received 79979375 broadcasts (67164951 multicasts)
         0 runts, 0 giants, 0 throttles 
         0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
         0 watchdog, 67164951 multicast, 0 pause input
         0 input packets with dribble condition detected
         50714881 packets output, 3776772371 bytes, 0 underruns
                   0 output errors, 0 collisions, 1 interface resets
         0 unknown protocol drops
         0 babbles, 0 late collision, 0 deferred
         0 lost carrier, 0 no carrier, 0 pause output
         0 output buffer failures, 0 output buffers swapped out
    GigabitEthernet0/10 is administratively down, line protocol is down (disabled) 
      Hardware is Gigabit Ethernet, address is 042a.e261.910a (bia 042a.e261.910a)
      MTU 9198 bytes, BW 10000 Kbit/sec, DLY 1000 usec, 
         reliability 255/255, txload 1/255, rxload 1/255
      Encapsulation ARPA, loopback not set
      Keepalive not set
      Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
      input flow-control is off, output flow-control is unsupported 
      ARP type: ARPA, ARP Timeout 04:00:00
      Last input never, output never, output hang never
      Last clearing of "" counters never
      Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
      Queueing strategy: fifo
      Output queue: 0/40 (size/max)
      5 minute input rate 0 bits/sec, 0 packets/sec
      5 minute output rate 0 bits/sec, 0 packets/sec
         0 packets input, 0 bytes, 0 no buffer
         Received 0 broadcasts (0 multicasts)
         0 runts, 0 giants, 0 throttles 
         0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
         0 watchdog, 0 multicast, 0 pause input
         0 input packets with dribble condition detected
         0 packets output, 0 bytes, 0 underruns
         0 output errors, 0 collisions, 0 interface resets
         0 unknown protocol drops
         0 babbles, 0 late collision, 0 deferred
         0 lost carrier, 0 no carrier, 0 pause output
         0 output buffer failures, 0 output buffers swapped out
    GigabitEthernet0/11 is down, line protocol is down (notconnect) 
      Hardware is Gigabit Ethernet, address is 042a.e261.910b (bia 042a.e261.910b)
      MTU 9198 bytes, BW 10000 Kbit/sec, DLY 1000 usec, 
         reliability 255/255, txload 1/255, rxload 1/255
      Encapsulation ARPA, loopback not set
      Keepalive not set
      Auto-duplex, Auto-speed, link type is auto, media type is Not Present
      input flow-control is off, output flow-control is unsupported 
      ARP type: ARPA, ARP Timeout 04:00:00
      Last input never, output never, output hang never
      Last clearing of "" counters never
      Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
      Queueing strategy: fifo
      Output queue: 0/40 (size/max)
      5 minute input rate 0 bits/sec, 0 packets/sec
      5 minute output rate 0 bits/sec, 0 packets/sec
         0 packets input, 0 bytes, 0 no buffer
         Received 0 broadcasts (0 multicasts)
         0 runts, 0 giants, 0 throttles 
         0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
         0 watchdog, 0 multicast, 0 pause input
         0 input packets with dribble condition detected
         0 packets output, 0 bytes, 0 underruns
         0 output errors, 0 collisions, 1 interface resets
         0 unknown protocol drops
         0 babbles, 0 late collision, 0 deferred
                   0 lost carrier, 0 no carrier, 0 pause output
         0 output buffer failures, 0 output buffers swapped out
    GigabitEthernet0/12 is down, line protocol is down (notconnect) 
      Hardware is Gigabit Ethernet, address is 042a.e261.910c (bia 042a.e261.910c)
      MTU 9198 bytes, BW 10000 Kbit/sec, DLY 1000 usec, 
         reliability 255/255, txload 1/255, rxload 1/255
      Encapsulation ARPA, loopback not set
      Keepalive not set
      Auto-duplex, Auto-speed, link type is auto, media type is Not Present
      input flow-control is off, output flow-control is unsupported 
      ARP type: ARPA, ARP Timeout 04:00:00
      Last input never, output never, output hang never
      Last clearing of "" counters never
      Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
      Queueing strategy: fifo
      Output queue: 0/40 (size/max)
      5 minute input rate 0 bits/sec, 0 packets/sec
      5 minute output rate 0 bits/sec, 0 packets/sec
         0 packets input, 0 bytes, 0 no buffer
         Received 0 broadcasts (0 multicasts)
         0 runts, 0 giants, 0 throttles 
         0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
         0 watchdog, 0 multicast, 0 pause input
         0 input packets with dribble condition detected
         0 packets output, 0 bytes, 0 underruns
         0 output errors, 0 collisions, 1 interface resets
         0 unknown protocol drops
         0 babbles, 0 late collision, 0 deferred
         0 lost carrier, 0 no carrier, 0 pause output
         0 output buffer failures, 0 output buffers swapped out
    """
        s.portdowntime_result_in = """"""
        s.inv_result = """NAME: "1", DESCR: "WS-C3560CX-8PC-S"
    PID: WS-C3560CX-8PC-S  , VID: V02  , SN: FOC2011Z16A
    
    
    portcount_result=Port            InOctets    InUcastPkts    InMcastPkts    InBcastPkts 
    Gi0/1              31846             93              6             55 
    Gi0/2                  0              0              0              0 
    Gi0/3                  0              0              0              0 
    Gi0/4                  0              0              0              0 
    Gi0/5                  0              0              0              0 
    Gi0/6                  0              0              0              0 
    Gi0/7                  0              0              0              0 
    Gi0/8              29082             81            111             48 
    Gi0/9        12406856435        1166954       67164957       12814424 
    Gi0/10                 0              0              0              0 
    Gi0/11                 0              0              0              0 
    Gi0/12                 0              0              0              0 
    
    Port           OutOctets   OutUcastPkts   OutMcastPkts   OutBcastPkts 
    Gi0/1             294795            167           1044            155 
    Gi0/2                  0              0              0              0 
    Gi0/3                  0              0              0              0 
    Gi0/4                  0              0              0              0 
    Gi0/5                  0              0              0              0 
    Gi0/6                  0              0              0              0 
    Gi0/7                  0              0              0              0 
    Gi0/8             223119            133           1578            119 
    Gi0/9         3776798684         104202       50610665            104 
    Gi0/10                 0              0              0              0 
    Gi0/11                 0              0              0              0 
    Gi0/12                 0              0              0              0 
    """
        s.portcount_result = """"""
        s.cdpnei_result = """-------------------------
    Device ID: sx1-482-102tower-5w-4401-102tower.net.ut
    Entry address(es): 
      IP address: 172.31.16.14
    Platform: cisco WS-C4510R+E,  Capabilities: Switch IGMP 
    Interface: GigabitEthernet0/9,  Port ID (outgoing port): GigabitEthernet3/2
    Holdtime : 156 sec
    
    Version :
    Cisco IOS Software, Catalyst 4500 L3 Switch  Software (cat4500es8-UNIVERSALK9-M), Version 15.2(3)E1, RELEASE SOFTWARE (fc3)
    Technical Support: http://www.cisco.com/techsupport
    Copyright (c) 1986-2015 by Cisco Systems, Inc.
    Compiled Tue 28-Apr-15 07:41 by prod_rel_team
    
    advertisement version: 2
    VTP Management Domain: 'vtp-102tower'
    Native VLAN: 1
    Duplex: full
    Management address(es): 
      IP address: 172.31.16.14
    Spare Pair PoE: Yes, Spare Pair Detection Required: No
    Spare Pair PD Config: Disable, Spare Pair PSE Operational: No
    
    
    Total cdp entries displayed : 1
    """
        s.module_result = """^
    % Invalid input detected at '^' marker.
    """
        s.module_result_in = """^
    % Invalid input detected at '^' marker.
    
    """
        s.snmp_result = """snmp-server group NOCGrv3RO v3 priv read NOCViewRO access 70
    snmp-server group NOCGrv3RO v3 auth context vlan- match prefix 
    snmp-server group NOCGrv3RW v3 priv write NOCViewRW access 71
    snmp-server group NONUserv3Rw v3 priv 
    snmp-server view NOCViewRO internet included
    snmp-server view NOCViewRW internet included
    snmp-server trap-source Vlan800
    snmp-server location Bldg. 482 Room 5363
    snmp-server contact BC-none Y-none
    snmp-server enable traps snmp authentication linkdown linkup coldstart warmstart
    snmp-server enable traps flowmon
    snmp-server enable traps transceiver all
    snmp-server enable traps call-home message-send-fail server-fail
    snmp-server enable traps tty
    snmp-server enable traps eigrp
    snmp-server enable traps ospf state-change
    snmp-server enable traps ospf errors
    snmp-server enable traps ospf retransmit
    snmp-server enable traps ospf lsa
    snmp-server enable traps ospf cisco-specific state-change nssa-trans-change
    snmp-server enable traps ospf cisco-specific state-change shamlink interface
    snmp-server enable traps ospf cisco-specific state-change shamlink neighbor
    snmp-server enable traps ospf cisco-specific errors
    snmp-server enable traps ospf cisco-specific retransmit
    snmp-server enable traps ospf cisco-specific lsa
    snmp-server enable traps license
    snmp-server enable traps auth-framework sec-violation
    snmp-server enable traps bfd
    snmp-server enable traps cef resource-failure peer-state-change peer-fib-state-change inconsistency
    snmp-server enable traps cluster
    snmp-server enable traps config-copy
    snmp-server enable traps config
    snmp-server enable traps config-ctid
    snmp-server enable traps trustsec-sxp conn-srcaddr-err msg-parse-err conn-config-err binding-err conn-up conn-down binding-expn-fail oper-nodeid-change binding-conflict
    snmp-server enable traps energywise
    snmp-server enable traps fru-ctrl
    snmp-server enable traps entity
    snmp-server enable traps event-manager
    snmp-server enable traps hsrp
    snmp-server enable traps ipmulticast
    snmp-server enable traps ike policy add
    snmp-server enable traps ike policy delete
    snmp-server enable traps ike tunnel start
    snmp-server enable traps ike tunnel stop
    snmp-server enable traps ipsec cryptomap add
    snmp-server enable traps ipsec cryptomap delete
    snmp-server enable traps ipsec cryptomap attach
    snmp-server enable traps ipsec cryptomap detach
    snmp-server enable traps ipsec tunnel start
    snmp-server enable traps ipsec tunnel stop
    snmp-server enable traps ipsec too-many-sas
    snmp-server enable traps ospfv3 state-change
    snmp-server enable traps ospfv3 errors
    snmp-server enable traps power-ethernet group 1
    snmp-server enable traps power-ethernet police
    snmp-server enable traps pim neighbor-change rp-mapping-change invalid-pim-message
    snmp-server enable traps cpu threshold
    snmp-server enable traps rep
              snmp-server enable traps ipsla
    snmp-server enable traps vstack
    snmp-server enable traps bridge newroot topologychange
    snmp-server enable traps stpx inconsistency root-inconsistency loop-inconsistency
    snmp-server enable traps syslog
    snmp-server enable traps vtp
    snmp-server enable traps vlancreate
    snmp-server enable traps vlandelete
    snmp-server enable traps flash insertion removal
    snmp-server enable traps port-security
    snmp-server enable traps envmon fan shutdown supply temperature status
    snmp-server enable traps stackwise
    snmp-server enable traps bulkstat collection transfer
    snmp-server enable traps vrfmib vrf-up vrf-down vnet-trunk-up vnet-trunk-down
    snmp-server enable traps errdisable
    snmp-server enable traps mac-notification change move threshold
    snmp-server enable traps vlan-membership
    snmp-server host 155.98.253.228 version 3 priv NONUserv3Rw 
    snmp ifmib ifindex persist
    """
        s.snmp_result_in = """ """
        s.snmp_user_result = """User name: NONUserv3RO
    Engine ID: 800000090300042AE2619101
    storage-type: nonvolatile	 active
    Authentication Protocol: MD5
    Privacy Protocol: DES
    Group-name: NOCGrv3RW
    
    User name: NONUserv3Rw
    Engine ID: 800000090300042AE2619101
    storage-type: nonvolatile	 active
    Authentication Protocol: MD5
    Privacy Protocol: AES128
    Group-name: NONUserv3Rw
    
    """
        s.acl_result = """Standard IP access list 70
        10 permit 10.64.2.70
        20 permit 155.100.126.163
        30 permit 155.100.126.162
        40 permit 172.20.150.100
        50 permit 155.98.164.192, wildcard bits 0.0.0.31
        60 permit 155.99.254.128, wildcard bits 0.0.0.127
        70 permit 155.98.253.0, wildcard bits 0.0.0.255
        80 deny   any log
    Standard IP access list 71
        10 permit 10.64.2.70
        20 permit 155.100.126.163
        30 permit 155.100.126.162
        40 permit 172.20.150.100
        50 permit 155.99.254.128, wildcard bits 0.0.0.127
        60 permit 155.98.253.0, wildcard bits 0.0.0.255
        70 deny   any log
    Extended IP access list 199
        10 permit tcp 155.98.253.0 0.0.0.255 any eq 22 (348 matches)
        20 permit tcp host 172.20.150.100 any eq 22
        30 permit tcp host 155.100.126.162 any eq 22
        40 permit tcp host 155.100.126.163 any eq 22
        50 permit tcp host 10.64.2.70 any eq 22
        60 permit tcp host 155.99.239.130 any eq 22 (2 matches)
        70 permit tcp host 155.97.152.244 any eq 22
        80 permit tcp host 155.100.123.72 any eq 22
        90 permit tcp 155.99.254.128 0.0.0.127 any eq 22 (126 matches)
        100 permit tcp 155.101.243.0 0.0.0.31 any eq 22
        110 permit tcp 155.98.164.192 0.0.0.31 any eq 22 (82 matches)
        120 deny ip any any log (50 matches)
    Extended IP access list CISCO-CWA-URL-REDIRECT-ACL
        100 deny udp any any eq domain
        101 deny tcp any any eq domain
        102 deny udp any eq bootps any
        103 deny udp any any eq bootpc
        104 deny udp any eq bootpc any
        105 permit tcp any any eq www
    Extended IP access list preauth_ipv4_acl (per-user)
        10 permit udp any any eq domain
        20 permit tcp any any eq domain
        30 permit udp any eq bootps any
        40 permit udp any any eq bootpc
        50 permit udp any eq bootpc any
        60 deny ip any any
    IPv6 access list preauth_ipv6_acl (per-user)
        permit udp any any eq domain sequence 10
        permit tcp any any eq domain sequence 20
        permit icmp any any nd-ns sequence 30
        permit icmp any any nd-na sequence 40
        permit icmp any any router-solicitation sequence 50
        permit icmp any any router-advertisement sequence 60
        permit icmp any any redirect sequence 70
        permit udp any eq 547 any eq 546 sequence 80
        permit udp any eq 546 any eq 547 sequence 90
        deny ipv6 any any sequence 100
    """
        s.logging_data_result = """logging buffered notifications
    logging console critical
    logging facility local6
    logging source-interface Vlan800
    logging host 155.98.204.52
    logging host 155.98.253.228"""
        s.logging_data_result_in = """"""
        s.mac_address_result = """Mac Address Table
    -------------------------------------------
    
    Vlan    Mac Address       Type        Ports
    ----    -----------       --------    -----
     All    0100.0ccc.cccc    STATIC      CPU
     All    0100.0ccc.cccd    STATIC      CPU
     All    0100.0ccd.cddc    STATIC      CPU
     All    0180.c200.0000    STATIC      CPU
     All    0180.c200.0001    STATIC      CPU
     All    0180.c200.0002    STATIC      CPU
     All    0180.c200.0003    STATIC      CPU
     All    0180.c200.0004    STATIC      CPU
     All    0180.c200.0005    STATIC      CPU
     All    0180.c200.0006    STATIC      CPU
     All    0180.c200.0007    STATIC      CPU
     All    0180.c200.0008    STATIC      CPU
     All    0180.c200.0009    STATIC      CPU
     All    0180.c200.000a    STATIC      CPU
     All    0180.c200.000b    STATIC      CPU
     All    0180.c200.000c    STATIC      CPU
     All    0180.c200.000d    STATIC      CPU
     All    0180.c200.000e    STATIC      CPU
     All    0180.c200.000f    STATIC      CPU
     All    0180.c200.0010    STATIC      CPU
     All    ffff.ffff.ffff    STATIC      CPU
       1    00a6.cad7.5181    DYNAMIC     Gi0/9
     151    0004.f2fe.3bf7    DYNAMIC     Gi0/9
     151    0004.f2ff.0218    DYNAMIC     Gi0/9
     151    0004.f2ff.02c6    DYNAMIC     Gi0/9
     151    0012.5f17.4a85    DYNAMIC     Gi0/9
     151    0012.5f17.4b15    DYNAMIC     Gi0/9
     151    0012.5f17.4b1d    DYNAMIC     Gi0/9
     151    0024.8120.e7b7    DYNAMIC     Gi0/9
     151    00a6.cad7.5181    DYNAMIC     Gi0/9
     151    00e0.db54.a528    DYNAMIC     Gi0/9
     151    00e0.db54.a52d    DYNAMIC     Gi0/9
     151    00e0.db56.076e    DYNAMIC     Gi0/9
     151    045d.4b00.b894    DYNAMIC     Gi0/9
     151    0830.6bcd.4110    DYNAMIC     Gi0/9
     151    0866.98b2.6aad    DYNAMIC     Gi0/9
     151    0866.98d4.405d    DYNAMIC     Gi0/9
     151    0c4d.e9a6.62d2    DYNAMIC     Gi0/9
     151    104f.a8e4.4291    DYNAMIC     Gi0/9
     151    104f.a8ef.419d    DYNAMIC     Gi0/9
     151    1cc1.de5c.2550    DYNAMIC     Gi0/9
     151    1cc1.de5c.2560    DYNAMIC     Gi0/9
     151    1cc1.de5e.45d8    DYNAMIC     Gi0/9
     151    28ff.3cac.19ff    DYNAMIC     Gi0/9
     151    38c9.8622.7463    DYNAMIC     Gi0/9
     151    644b.f01a.4f37    DYNAMIC     Gi0/9
     151    64f6.9d71.b7c0    DYNAMIC     Gi0/9
     151    7478.27f0.1a42    DYNAMIC     Gi0/9
     151    9c7b.ef77.b9ee    DYNAMIC     Gi0/9
     151    a4bb.6d80.8595    DYNAMIC     Gi0/9
     151    c81f.ea87.58f9    DYNAMIC     Gi0/9
     151    d003.4b59.daee    DYNAMIC     Gi0/9
     151    d485.649c.469b    DYNAMIC     Gi0/9
     151    ecb1.d76e.e899    DYNAMIC     Gi0/9
               800    002a.101e.b6ec    DYNAMIC     Gi0/9
     800    002a.101e.bfe4    DYNAMIC     Gi0/9
     800    002a.101e.c39e    DYNAMIC     Gi0/9
     800    002a.101e.c3f0    DYNAMIC     Gi0/9
     800    002a.101e.c416    DYNAMIC     Gi0/9
     800    002a.101e.c45e    DYNAMIC     Gi0/9
     800    002a.101e.c474    DYNAMIC     Gi0/9
     800    002a.101e.c5a8    DYNAMIC     Gi0/9
     800    002a.101e.d09e    DYNAMIC     Gi0/9
     800    002a.101e.d288    DYNAMIC     Gi0/9
     800    002a.101e.d34c    DYNAMIC     Gi0/9
     800    002a.101e.d358    DYNAMIC     Gi0/9
     800    002a.101e.d376    DYNAMIC     Gi0/9
     800    002a.101e.d496    DYNAMIC     Gi0/9
     800    002a.101e.d4a0    DYNAMIC     Gi0/9
     800    002a.101e.d4ae    DYNAMIC     Gi0/9
     800    002a.101e.d504    DYNAMIC     Gi0/9
     800    002a.101e.d730    DYNAMIC     Gi0/9
     800    002a.101e.dbf6    DYNAMIC     Gi0/9
     800    002a.101e.dddc    DYNAMIC     Gi0/9
     800    002a.1034.6b84    DYNAMIC     Gi0/9
     800    002a.1034.6c08    DYNAMIC     Gi0/9
     800    002a.1034.6c40    DYNAMIC     Gi0/9
     800    002a.1034.6c76    DYNAMIC     Gi0/9
     800    002a.1034.6c86    DYNAMIC     Gi0/9
     800    002a.1034.6c96    DYNAMIC     Gi0/9
     800    002a.1034.6cb4    DYNAMIC     Gi0/9
     800    002a.1034.6d0a    DYNAMIC     Gi0/9
     800    002a.1034.6d0c    DYNAMIC     Gi0/9
     800    002a.1034.731e    DYNAMIC     Gi0/9
     800    002a.1034.732c    DYNAMIC     Gi0/9
     800    002a.1034.737c    DYNAMIC     Gi0/9
     800    002a.1034.73b2    DYNAMIC     Gi0/9
     800    002a.1034.73cc    DYNAMIC     Gi0/9
     800    002a.1034.73da    DYNAMIC     Gi0/9
     800    002a.1034.7916    DYNAMIC     Gi0/9
     800    002a.1034.7b40    DYNAMIC     Gi0/9
     800    002a.1034.7b6e    DYNAMIC     Gi0/9
     800    002a.1034.7c64    DYNAMIC     Gi0/9
     800    002a.1034.7d0a    DYNAMIC     Gi0/9
     800    002a.1034.7d46    DYNAMIC     Gi0/9
     800    002a.1034.7d78    DYNAMIC     Gi0/9
     800    002a.1034.7fc8    DYNAMIC     Gi0/9
     800    002a.1034.826c    DYNAMIC     Gi0/9
     800    002a.1034.827c    DYNAMIC     Gi0/9
     800    002a.1034.828a    DYNAMIC     Gi0/9
     800    002a.1034.8294    DYNAMIC     Gi0/9
     800    002a.1034.82b0    DYNAMIC     Gi0/9
     800    002a.1034.82b6    DYNAMIC     Gi0/9
     800    002a.1034.82ba    DYNAMIC     Gi0/9
     800    002a.1034.82bc    DYNAMIC     Gi0/9
     800    002a.1034.82c4    DYNAMIC     Gi0/9
     800    002a.1034.838e    DYNAMIC     Gi0/9
     800    002a.1060.2f36    DYNAMIC     Gi0/9
     800    002a.1060.2f3c    DYNAMIC     Gi0/9
     800    002a.1060.2f5a    DYNAMIC     Gi0/9
     800    002a.1060.2fae    DYNAMIC     Gi0/9
     800    002a.1060.300e    DYNAMIC     Gi0/9
     800    002a.1060.30a6    DYNAMIC     Gi0/9
               800    002a.1060.3bfe    DYNAMIC     Gi0/9
     800    002a.1060.3c0c    DYNAMIC     Gi0/9
     800    002a.1060.3c5e    DYNAMIC     Gi0/9
     800    002a.1060.3c68    DYNAMIC     Gi0/9
     800    002a.1060.3c96    DYNAMIC     Gi0/9
     800    002a.1060.3c98    DYNAMIC     Gi0/9
     800    002a.1060.3cb8    DYNAMIC     Gi0/9
     800    002a.1060.3ffe    DYNAMIC     Gi0/9
     800    002a.1060.411e    DYNAMIC     Gi0/9
     800    002a.1060.447a    DYNAMIC     Gi0/9
     800    002a.1060.4696    DYNAMIC     Gi0/9
     800    0042.68a7.637e    DYNAMIC     Gi0/9
     800    00a6.cad7.5181    DYNAMIC     Gi0/9
     800    00a6.caff.849c    DYNAMIC     Gi0/9
     800    00a6.caff.8d18    DYNAMIC     Gi0/9
     800    00a6.caff.8d78    DYNAMIC     Gi0/9
     800    00a6.caff.8e0a    DYNAMIC     Gi0/9
     800    00a6.caff.8e0c    DYNAMIC     Gi0/9
     800    00d7.8f1e.a536    DYNAMIC     Gi0/9
     800    00d7.8f1e.a558    DYNAMIC     Gi0/9
     800    00d7.8fa6.d08c    DYNAMIC     Gi0/9
     800    00d7.8fa6.d2dc    DYNAMIC     Gi0/9
     800    00d7.8fa6.d32a    DYNAMIC     Gi0/9
     800    00d7.8fa6.d98c    DYNAMIC     Gi0/9
     800    00d7.8fa6.d98e    DYNAMIC     Gi0/9
     800    00f6.634a.4dd4    DYNAMIC     Gi0/9
     800    00f6.634a.53a8    DYNAMIC     Gi0/9
     800    00f6.634a.53d4    DYNAMIC     Gi0/9
     800    00f6.634a.5414    DYNAMIC     Gi0/9
     800    00f6.634a.541e    DYNAMIC     Gi0/9
     800    00f6.634a.5430    DYNAMIC     Gi0/9
     800    00f6.634a.543c    DYNAMIC     Gi0/9
     800    00f6.634a.543e    DYNAMIC     Gi0/9
     800    00f6.634a.5440    DYNAMIC     Gi0/9
     800    00f6.634a.5442    DYNAMIC     Gi0/9
     800    00f6.634a.544a    DYNAMIC     Gi0/9
     800    00f6.6373.8212    DYNAMIC     Gi0/9
     800    00f6.6373.8694    DYNAMIC     Gi0/9
     800    500f.8098.15da    DYNAMIC     Gi0/9
     800    58ac.78f8.5472    DYNAMIC     Gi0/9
     800    58ac.78f8.54b6    DYNAMIC     Gi0/9
     800    58ac.78f8.571a    DYNAMIC     Gi0/9
     800    64f6.9d71.b7c0    DYNAMIC     Gi0/9
     800    7079.b317.5896    DYNAMIC     Gi0/9
     800    b827.eb0f.7e37    DYNAMIC     Gi0/9
     986    0000.0c9f.f3da    DYNAMIC     Gi0/9
     986    0005.73a0.03da    DYNAMIC     Gi0/9
     986    003a.9c3f.ffc1    DYNAMIC     Gi0/9
     986    003a.9c40.5ec1    DYNAMIC     Gi0/9
     986    00a6.cad7.5181    DYNAMIC     Gi0/9
     986    3c07.5456.6bb3    DYNAMIC     Gi0/9
     986    8cdc.d434.9b0b    DYNAMIC     Gi0/9
     986    c8d3.ff73.e0b6    DYNAMIC     Gi0/9
    Total Mac Addresses for this criterion: 166
    """
        s.tacacs_result = """aaa group server tacacs+ NOC-TAC
     server name TAC-EBC
     server name TAC-SECONDARY
    tacacs server TAC-EBC
     address ipv4 172.31.17.180
     key 7 143E560E25402F09042A2A74
    tacacs server TAC-SECONDARY
     address ipv4 10.64.32.5
     key 7 013A4201724F032D014E5748"""
        s.tacacs_result_in = """"""
        s.inline_power_result = """Available:240.0(w)  Used:0.0(w)  Remaining:240.0(w)
    
    Interface Admin  Oper       Power   Device              Class Max
                                (Watts)                            
    --------- ------ ---------- ------- ------------------- ----- ----
    Gi0/1     auto   off        0.0     n/a                 n/a   30.0 
    Gi0/2     auto   off        0.0     n/a                 n/a   30.0 
    Gi0/3     auto   off        0.0     n/a                 n/a   30.0 
    Gi0/4     auto   off        0.0     n/a                 n/a   30.0 
    Gi0/5     auto   off        0.0     n/a                 n/a   30.0 
    Gi0/6     auto   off        0.0     n/a                 n/a   30.0 
    Gi0/7     auto   off        0.0     n/a                 n/a   30.0 
    Gi0/8     auto   off        0.0     n/a                 n/a   30.0 
    """
        s.environment_result = """^
    % Invalid input detected at '^' marker.
    """

        s.assignattributes()
        # test global Variables
        self.assertEqual(s.bannername, 'sx1-482-102tower-5th-test')
        self.assertEqual(s.buildnumber, "482")
        self.assertEqual(s.buildingname, '102tower')
        self.assertEqual(s.racknumber, None)
        self.assertEqual(s.description, 'Datacenter Sub Access Layer Switch')
        self.assertEqual(s.IPAddress, '172.31.16.52')
        self.assertEqual(s.portcount, 12)
        self.assertEqual(s.serial[0], 'FOC2011Z16A')
        self.assertEqual(s.subnetmask, '255.255.255.0')
        self.assertNotEqual(s.uptime, None)
        self.assertEqual(s.uplink,)

        # test the assignment of ACL object properties
        self.assertEqual(len(s.access_lists), 3)
        self.assertIn(199, s.access_lists.numbers)
        self.assertIn(70, s.access_lists.numbers)
        self.assertIn(71, s.access_lists.numbers)
        for aclobj in s.access_lists.standard_ip_lists:
            self.assertIsInstance(aclobj, ACL)
            self.assertIsInstance(aclobj.Entries, list)
            for entry in aclobj.Entries:
                self.assertIsInstance(entry, ACL_Entry)
                self.assertTrue(entry.type)
                self.assertTrue(entry.number)
            self.assertTrue(aclobj.Entries)
            self.assertTrue(aclobj.type)

        # test the assignment of the SNMP Value
        self.assertIsInstance(s.SNMP, SNMP)
        self.assertIsInstance(s.SNMP.communities, list)
        self.assertIsInstance(s.SNMP.traps, list)
        self.assertIsInstance(s.SNMP.traps, list)
        self.assertIsInstance(s.SNMP.version, set)
        self.assertTrue(s.SNMP.communities)
        self.assertEqual(len(s.SNMP.communities), 5)
        for communities in s.SNMP.communities:
            self.assertIsInstance(communities, SNMP_community)
            self.assertTrue(communities.raw_data)
            self.assertTrue(communities.string)
        self.assertTrue(s.SNMP.traps)
        self.assertEqual(len(s.SNMP.traps), 19)
        self.assertTrue(s.SNMP.version)
        self.assertTrue(s.SNMP.loggingips)
        self.assertIn(2, s.SNMP.version)
        self.assertNotIn(3, s.SNMP.version)

        # check the blades configuration
        self.assertTrue(s.blades)
        self.assertEqual(len(s.blades), 1)
        self.assertEqual(s.blades[0].ISOversion, '15.2(3)E3')
        self.assertFalse(s.blades[0].SUP)
        self.assertEqual(s.blades[0].modelnumber, 'WS-C3560CX-8PC-S')
        self.assertEqual(s.blades[0].portcount, 12)
        self.assertTrue(s.blades[0].interfaces)
        self.assertEqual(len(s.blades[0].interfaces), 12)
        portrange = range(1, 13)
        for portnumber, interface in s.blades[0].interfaces.items():
            self.assertTrue(interface)
            self.assertIsInstance(interface.mac_addresses, list)
            if interface.mac_addresses:
                for macaddress in interface.mac_addresses:
                    self.assertIsInstance(macaddress, EUI)
            self.assertIsInstance(interface, Interface)
            self.assertEqual(interface.type, 'copper')
            self.assertIn(int(portnumber), portrange)
            self.assertTrue(interface.fullname)
            self.assertIn(interface.portnumber, portrange)
        self.assertTrue(s.blades[0].interfaces['3'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['5'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['6'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['17'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['18'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['19'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['21'].InBcastPkts)
        self.assertTrue(s.blades[0].interfaces['22'].InBcastPkts)

        # test assignment of CDP Neighbor
        self.assertIsInstance(s.cdpneighbors, list)
        self.assertEqual(len(s.cdpneighbors), 1)
        self.assertIsInstance(s.cdpneighbors[0], Neighbor)
        self.assertEqual(s.cdpneighbors[0].deviceid, 'sx1-482-102tower-5w-4401-102tower.net.ut')
        self.assertEqual(str(s.cdpneighbors[0].ip), '172.31.16.14')
        self.assertIsInstance(s.cdpneighbors[0].ip, IPv4Address)
        self.assertEqual(s.cdpneighbors[0].platform, 'WS-C4510R+E')
        self.assertIsInstance(s.cdpneighbors[0].interface, Interface)
        self.assertEqual(s.cdpneighbors[0].interface.fullname, 'GigabitEthernet0/9')
        self.assertIsInstance(s.cdpneighbors[0].interface, Interface)
        self.assertEqual(s.cdpneighbors[0].interface.portnumber, 9)
        self.assertEqual(s.cdpneighbors[0].duplex, 'full')

        self.assertEqual(s.chassis, None)
        self.assertEqual(s.defaultgateway, '172.31.16.1')
        self.assertEqual(s.hostname, 'sx1-482-102tower-5th-test')
        self.assertEqual(s.ip, '172.31.16.52')
        self.assertEqual(s.lastrestart, None)

        # logging Info
        logging = ['155.98.204.52', '155.98.253.228']
        for log in s.logging_data:
            self.assertIn(str(log[1]), logging)
            self.assertIsInstance(log[1], IPv4Address)

        # check vlans
        self.assertEqual(len(s.vlans), 12)
        self.assertEqual(s.vlans[0].name, 'test-private-vlan')
        self.assertEqual(s.vlans[0].number, 10)
        self.assertEqual(s.vlans[1].name, 'floor5-campus')
        self.assertEqual(s.vlans[1].number, 151)
        self.assertEqual(s.vlans[2].name, 'CCURE-FM')
        self.assertEqual(s.vlans[2].number, 333)
        for macaddress in s.vlans[2].mac_addresses:
            self.assertIsInstance(macaddress, EUI)
        self.assertEqual(s.vlans[3].name, 'ebc-892komas-wireless')
        self.assertEqual(s.vlans[3].number, 440)
        self.assertEqual(s.vlans[4].name, '482-VOIP')
        self.assertEqual(s.vlans[4].number, 444)
        self.assertEqual(s.vlans[5].name, 'komas-mgmt-2960')
        self.assertEqual(s.vlans[5].number, 449)
        self.assertEqual(s.vlans[6].name, '482-lan')
        self.assertEqual(s.vlans[6].number, 555)
        self.assertEqual(s.vlans[7].name, 'this-is-a-test')
        self.assertEqual(s.vlans[7].number, 589)
        self.assertEqual(s.vlans[8].name, '482-102tower-m')
        self.assertEqual(s.vlans[8].number, 800)
        self.assertEqual(s.vlans[9].name, 'noc-wrkstns-inside')
        self.assertEqual(s.vlans[9].number, 986)
        self.assertEqual(s.vlans[10].name, 'ebc-NOC-AP-PRIMING')
        self.assertEqual(s.vlans[10].number, 994)
        self.assertEqual(s.vlans[11].name, 'hello')
        self.assertEqual(s.vlans[11].number, 999)

        # test tacacs configuration
        self.assertIsInstance(s.tacacs, list)
        self.assertEqual(len(s.tacacs), 2)
        self.assertIsInstance(s.tacacs[0], TACACS)
        self.assertIsInstance(s.tacacs[0].server, IPv4Address)
        self.assertEqual(str(s.tacacs[0].server), '172.31.17.180')
        self.assertIsInstance(s.tacacs[1].server, IPv4Address)
        self.assertEqual(str(s.tacacs[1].server), '10.64.32.5')


if __name__ == '__main__':
    unittest.main()