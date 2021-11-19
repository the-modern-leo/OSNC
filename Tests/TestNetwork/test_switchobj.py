### Local Imports ###
from Network.Switch import Stack, Neighbor
from Network.AccessList import ACL,ACL_Entry
from Network.Port import Interface
from SNMP.Objects import SNMP,SNMP_community, SNMP_contact,SNMP_view, SNMP_Group
from Tacacs.Objects import TACACS


### Test Imports ###
from Tests.TestNetwork.device_list.Switches_syntax_compatability.cisco.catalyst import ws_c3560cx_8pc_s,\
    c29xx,c36xx,c38xx,c9407r,c4510r_e_,c94010r,c3560cg_8pc_s,c3560x_24_poe,c3650_48pq_e,c9300_series
from Tests.TestNetwork.device_list.Switches_syntax_compatability.cisco.nexus import c9332pq,c93180yc_fx

### global imports ###
import unittest
from unittest.mock import patch
from ipaddress import IPv4Address
from netaddr import EUI



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
    This is for Testing compatibility of Stack Devices accross multiple platforms
    """
    def test_Catalyst_2960(self):
        """
        scx1-ddc-d11.med.utah.edu
        Model: WS-C2960G-24TC-L
        Software Version: 12.2(44)SE6
        """
        s = Stack(ipaddress="172.20.71.105")
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
        self.assertEqual(s.description, 'Datacenter Sub Access Layer Stack')
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
        self.assertIsInstance(s.cdpneighbors[0].ip, IPv4Address)
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
            self.assertIsInstance(log[1],IPv4Address)

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
        self.assertIsInstance(s.tacacs[0].server, IPv4Address)
        self.assertEqual(str(s.tacacs[0].server),'172.31.17.180')
        self.assertIsInstance(s.tacacs[1].server, IPv4Address)
        self.assertEqual(str(s.tacacs[1].server), '10.64.32.5')

    def test_Nexus_3064T(self):
        """
        Model:WS-C3560X-48P
        Software Version: 12.2(53)SE2
        """
        s = Stack('172.31.7.151')
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
        self.assertEqual(s.description, 'Sub Access Layer Stack')
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
            self.assertIsInstance(neighbor.ip, IPv4Address)
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
            self.assertIsInstance(log[1], IPv4Address)

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
        self.assertIsInstance(s.tacacs[0].server, IPv4Address)
        self.assertEqual(str(s.tacacs[0].server), '172.31.17.180')
        self.assertIsInstance(s.tacacs[1].server, IPv4Address)
        self.assertEqual(str(s.tacacs[1].server), '10.64.32.5')

    def test_Catalyst_3560X_24_PoE(self):
        """
        dx1-619honors
        Model: WS-C3560X-24P
        Software Version: 12.2(55)SE3
        """
        s = Stack("155.97.253.188")
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
        self.assertEqual(s.description, 'Demarc (Access Layer Stack)')
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
            self.assertIsInstance(neighbor.ip, IPv4Address)
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
            self.assertIsInstance(log[1], IPv4Address)

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
        self.assertIsInstance(s.tacacs[0].server, IPv4Address)
        self.assertEqual(str(s.tacacs[0].server), '172.31.17.180')
        self.assertIsInstance(s.tacacs[1].server, IPv4Address)
        self.assertEqual(str(s.tacacs[1].server), '10.64.32.5')

    def test_Catalyst_3560X_48_PoE(self):
        """
        Model:WS-C3560X-48P
        Software Version: 12.2(53)SE2
        """
        s = Stack("172.20.66.109")
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
        self.assertEqual(s.description, 'Sub Access Layer Stack')
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
            self.assertIsInstance(neighbor.ip, IPv4Address)
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
            self.assertIsInstance(log[1], IPv4Address)

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
        self.assertIsInstance(s.tacacs[0].server, IPv4Address)
        self.assertEqual(str(s.tacacs[0].server), '172.31.17.180')
        self.assertIsInstance(s.tacacs[1].server, IPv4Address)
        self.assertEqual(str(s.tacacs[1].server), '10.64.32.5')

    def Cisco_Catalyst_3650_24TD(self):
        pass
        s = Stack("172.20.66.109")
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
        self.assertEqual(s.description, 'Sub Access Layer Stack')
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
            self.assertIsInstance(neighbor.ip, IPv4Address)
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
            self.assertIsInstance(log[1], IPv4Address)

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
        self.assertIsInstance(s.tacacs[0].server, IPv4Address)
        self.assertEqual(str(s.tacacs[0].server), '172.31.17.180')
        self.assertIsInstance(s.tacacs[1].server, IPv4Address)
        self.assertEqual(str(s.tacacs[1].server), '10.64.32.5')

    def Cisco_Catalyst_3650_48PD(self):
        pass
        # s = Stack("")
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
        s = Stack("172.31.7.159")
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
        # self.assertEqual(s.description, 'Sub Access Layer Stack')
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
        #     self.assertIsInstance(neighbor.ip, IPv4Address)
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
        #     self.assertIsInstance(log[1], IPv4Address)
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
        # self.assertIsInstance(s.tacacs[0].server, IPv4Address)
        # self.assertEqual(str(s.tacacs[0].server), '172.31.17.180')
        # self.assertIsInstance(s.tacacs[1].server, IPv4Address)
        # self.assertEqual(str(s.tacacs[1].server), '10.64.32.5')

    def Catalyst_37xx_Stack(self):
        pass
        # s = Stack(ipaddress="")
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
        # s = Stack(ipaddress="")
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
        # s = Stack(ipaddress="")
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
        s = Stack(ipaddress="172.30.133.197")
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
        self.assertEqual(s.description, 'Demarc (Access Layer Stack)')
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
            self.assertIsInstance(neighbor.ip, IPv4Address)
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
            self.assertIsInstance(log[1], IPv4Address)

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
        self.assertIsInstance(s.tacacs[0].server, IPv4Address)
        self.assertEqual(str(s.tacacs[0].server), '172.31.17.180')
        self.assertEqual(str(s.tacacs[0].name), 'TAC-EBC')
        self.assertIsInstance(s.tacacs[1].server, IPv4Address)
        self.assertEqual(str(s.tacacs[1].server), '10.64.32.5')
        self.assertEqual(str(s.tacacs[1].name), 'TAC-SECONDARY')

    def Catalyst_C4507R(self):
        pass
        # s = Stack("")
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
        # s = Stack("")
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
        s = Stack("172.31.16.7")
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
        self.assertEqual(s.description, 'Sub Access Layer Stack')
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
            self.assertIsInstance(neighbor.ip, IPv4Address)
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
            self.assertIsInstance(log[1], IPv4Address)

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
        self.assertIsInstance(s.tacacs[0].server, IPv4Address)
        self.assertEqual(str(s.tacacs[0].server), '172.31.17.180')
        self.assertEqual(str(s.tacacs[0].name), 'TAC-EBC')
        self.assertIsInstance(s.tacacs[1].server, IPv4Address)
        self.assertEqual(str(s.tacacs[1].server), '10.64.32.5')
        self.assertEqual(str(s.tacacs[1].name), 'TAC-SECONDARY')

    def Catalyst_4948(self):
        pass
        # s = Stack(ipaddress="")
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
        # s = Stack(ipaddress="")
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
        # s = Stack(ipaddress="")
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
        # s = Stack(ipaddress="")
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
        # s = Stack(ipaddress="")
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

if __name__ == '__main__':
    unittest.main()