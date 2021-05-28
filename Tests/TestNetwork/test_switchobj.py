import ipaddress
import re
import unittest

import datetime
from dateutil.relativedelta import relativedelta
from Network.Network import Switch, Interface, Blade, Building, Console_server, SwitchAccess
from Network.Network import Router, SFP, vlan, Neighbor, ACL, SNMP, SNMP_community
from Network.Network import ACL_Entry, TACACS, Provision_Switch_from_old_switch
from Network.Network import SNMP_contact, Building, SNMP_Group, SNMP_view, ASA
from ipaddress import IPv4Address
from netaddr import EUI
import random
from auth import Switch_access, OrionAPI
import csv
from paramiko import ssh_exception
from concurrent.futures import ThreadPoolExecutor, as_completed
import concurrent.futures
from orion.orion import Orion
import random
import time

class TestCommandResults(unittest.TestCase):

    def test_responses_WS_C4507R_E(self):
        oldswitch = Switch('172.31.5.5')
        oldswitch.login()
        oldswitch.getSwitchInfo()
        #version Tests
        self.assertIsNotNone(oldswitch.version_result)
        self.assertIn('Cisco IOS Software',oldswitch.version_result)
        self.assertIn('Technical Support: http://www.cisco.com/techsupport', oldswitch.version_result)
        self.assertNotIn('Current configuration', oldswitch.version_result)
        self.assertNotIn('Last configuration change at', oldswitch.version_result)
        self.assertNotIn('NVRAM config last updated at', oldswitch.version_result)
        #Run Tests
        self.assertIn('Current configuration', oldswitch.run_result)
        self.assertIn('configuration change', oldswitch.run_result)
        self.assertIn('!', oldswitch.run_result)
        self.assertIn('interface', oldswitch.run_result)
        # Show interface link Tests
        self.assertIn('Port    Name               Down Time        Down Since', oldswitch.portdowntime_result)
        self.assertIn('secs', oldswitch.portdowntime_result)
        self.assertIn('minutes', oldswitch.portdowntime_result)
        self.assertNotIn("% Invalid input detected at '^' marker.", oldswitch.portdowntime_result)
        #inventory Tests
        self.assertIn('PID:',oldswitch.inv_result)
        self.assertIn('VID:', oldswitch.inv_result)
        self.assertIn('SN:', oldswitch.inv_result)
        #Portcount Tests
        self.assertIn('Port             InBytes   InUcastPkts   InMcastPkts   InBcastPkts', oldswitch.portcount_result)
        self.assertNotIn("% Invalid input detected at '^' marker.", oldswitch.portcount_result)
        #CDP NEI Test
        self.assertIn('Device ID:', oldswitch.cdpnei_result)
        self.assertIn('-------------------------', oldswitch.cdpnei_result)
        self.assertIn('Entry address(es):', oldswitch.cdpnei_result)
        self.assertIn('Platform:', oldswitch.cdpnei_result)
        self.assertNotIn("% Invalid input detected at '^' marker.", oldswitch.cdpnei_result)
        #moduleresults
        self.assertIn('Mod Ports Card Type                              Model              Serial No.', oldswitch.module_result)
        self.assertIn('Power consumed by backplane :', oldswitch.module_result)
        self.assertIn('Chassis Type :', oldswitch.module_result)
        self.assertIn(' M MAC addresses                    Hw  Fw           Sw               Status', oldswitch.module_result)
        self.assertNotIn("% Invalid input detected at '^' marker.", oldswitch.module_result)
        self.assertNotIn("Device ID:", oldswitch.module_result)
        self.assertNotIn("Entry address(es):", oldswitch.module_result)
        self.assertNotIn("Platform:", oldswitch.module_result)

    def test_responses_C9300_48U(self):
        c = DeviceAccess(Switch_access.username, Switch_access.password)
        oldswitch_con = c.login('172.31.5.16')
        oldswitch = Switch()
        oldswitch.getSwitchInfo(oldswitch_con)
        self.assertIsNotNone(oldswitch.version_result)
        self.assertNotIn("% Invalid input detected at '^' marker.", oldswitch.version_result)
        self.assertIn('Cisco IOS Software',oldswitch.version_result)
        self.assertIn('Technical Support: http://www.cisco.com/techsupport', oldswitch.version_result)
        self.assertNotIn('Current configuration', oldswitch.version_result)
        self.assertNotIn('Last configuration change at', oldswitch.version_result)
        self.assertNotIn('NVRAM config last updated at', oldswitch.version_result)
        self.assertIn('Current configuration', oldswitch.run_result)
        self.assertNotIn("% Invalid input detected at '^' marker.", oldswitch.run_result)
        self.assertIn('configuration change', oldswitch.run_result)
        self.assertIn('!', oldswitch.run_result)
        self.assertIn('interface', oldswitch.run_result)
        self.assertIn("% Invalid input detected at '^' marker.", oldswitch.portdowntime_result)

    def test_assign_version_C9300_48U(self):
        c = DeviceAccess(Switch_access.username, Switch_access.password)
        oldswitch_con = c.login('172.31.5.16')
        oldswitch = Switch()
        oldswitch.getSwitchInfo(oldswitch_con)
        oldswitch.sortVersion(versionresult=oldswitch.version_result)
        self.assertTrue(hasattr(oldswitch,'modelnumber'))
        self.assertTrue(hasattr(oldswitch, 'uptime'))
        self.assertTrue(hasattr(oldswitch, 'version'))
        self.assertTrue(hasattr(oldswitch, 'serial'))
        self.assertTrue(hasattr(oldswitch, 'blades'))
        self.assertTrue(hasattr(oldswitch, 'stack'))
        self.assertFalse(oldswitch.version == "16.6.5")
        self.assertTrue(oldswitch.stack)
        self.assertTrue(oldswitch.serial == ['FOC2245Q0BX','FCW2303DHC7'])
        self.assertTrue(len(oldswitch.serial) == 2)
        self.assertTrue(len(oldswitch.blades) == 2)
        for blade in oldswitch.blades:
            self.assertTrue(hasattr(blade, 'portcount'))
            self.assertTrue(hasattr(blade, 'modelnumber'))
            self.assertTrue(hasattr(blade, 'ISOversion'))
            self.assertTrue(hasattr(blade, 'stacknumber'))
            self.assertTrue(blade.ISOversion == "16.6.5")
            self.assertTrue(blade.modelnumber == "C9300-48U")
            self.assertTrue(blade.portcount == 62)
        self.assertTrue(any(x.stacknumber == 1 for x in oldswitch.blades))
        self.assertTrue(any(x.stacknumber == 2 for x in oldswitch.blades))
        self.assertFalse(any(x.stacknumber == 3 for x in oldswitch.blades))
        self.assertFalse(any(x.stacknumber == 4 for x in oldswitch.blades))
        self.assertFalse(oldswitch.modelnumber == "C9300-48U")
        #TODO write a test for oldswitch.time

    def test_assign_version_WS_C4507R_E(self):
        c = DeviceAccess(Switch_access.username, Switch_access.password)
        oldswitch_con = c.login('172.31.5.5')
        oldswitch = Switch()
        oldswitch.getSwitchInfo(oldswitch_con)
        oldswitch.sortVersion(versionresult=oldswitch.version_result)
        self.assertTrue(hasattr(oldswitch,'modelnumber'))
        self.assertTrue(hasattr(oldswitch, 'uptime'))
        self.assertTrue(hasattr(oldswitch, 'version'))
        self.assertTrue(hasattr(oldswitch, 'serial'))
        self.assertTrue(hasattr(oldswitch, 'blades'))
        self.assertTrue(hasattr(oldswitch, 'stack'))
        self.assertFalse(oldswitch.version == "12.2(44r)SG5")
        self.assertTrue(oldswitch.chassis)
        self.assertFalse(oldswitch.stack)
        self.assertTrue(oldswitch.modelnumber == "WS-C4507R-E")

    def test_assign_run_c9300_48U(self):
        """
        Tests that the function for assigning the switch attribues to run are working properly on
        93000 switches.
        Returns:

        """
        c = DeviceAccess(Switch_access.username, Switch_access.password)
        oldswitch_con = c.login('172.31.5.16')
        oldswitch = Switch()
        oldswitch.getSwitchInfo(oldswitch_con)
        oldswitch.sortVersion(versionresult=oldswitch.version_result)

    def test_delportswithouttraffic_WS_C4507R_E(self):
        """

        Tests the the function 'delportswithouttraffic'. Checks to see if the interfaces that are removed
        are accurate

        """
        c = DeviceAccess(Switch_access.username, Switch_access.password)
        oldswitch_con = c.login('172.31.5.5')
        oldswitch = Switch()
        oldswitch.getSwitchInfo(oldswitch_con)
        oldswitch.assignattributes()

        #before removing interfaces
        portswithtraffic = 0
        portswithtrafficlist = []
        totalports = 0
        for blade in oldswitch.blades:
            totalports += blade.portcount
            blade.trafficedportscount = 0
            blade.trafficedports = []
            for interface in blade.interfaces:
                if (interface.InOctets > 0 or
                    interface.InUcastPkts > 0 or
                    interface.InMcastPkts > 0 or
                    interface.InBcastPkts > 0 or
                    interface.outOctets > 0 or
                    interface.outUcastPkts > 0 or
                    interface.outMcastPkts > 0 or
                    interface.outBcastPkts > 0):
                    portswithtraffic += 1
                    portswithtrafficlist.append(interface)
                    blade.trafficedportscount += 1
                    blade.trafficedports.append(interface)

        # Tests per blade
        portswithouttrafficcount = 0
        portswithtrafficaftertest = []
        for blade in oldswitch.blades:
            unusedports = blade.portcount - blade.trafficedportscount
            blade.inuseports = blade.portcount
            blade.delportswithouttraffic()
            self.assertEqual(unusedports,blade.portcount-blade.inuseports)
            self.assertEqual(blade.trafficedports,blade.interfaces)
            portswithouttrafficcount += blade.portcount - blade.inuseports
            portswithtrafficaftertest += blade.interfaces

        #device total Tests
        self.assertEqual(portswithtrafficlist,portswithtrafficaftertest)
        self.assertEqual(portswithouttrafficcount,totalports-portswithtraffic)

    def test_delunconfiguredports_WS_C4507R_E(self):
        """

        Tests the the function 'delunconfiguredports'. Checks to see if the interfaces that are removed
        are accurate

        """
        c = DeviceAccess(Switch_access.username, Switch_access.password)
        oldswitch_con = c.login('172.31.5.5')
        oldswitch = Switch()
        oldswitch.getSwitchInfo(oldswitch_con)
        oldswitch.assignattributes()

        configuredports = []
        configuredportscount = 0
        for blade in oldswitch.blades:
            blade.configuredports = []
            blade.configuredportcount = 0
            for interface in blade.interfaces:
                if (interface.description or
                        interface.vlan or
                        interface.trunk or
                        interface.trunkvlan or
                        interface.voicevlan or
                        interface.dualmode or
                        interface.stpf):
                    configuredports.append(interface)
                    configuredportscount += 1
                    blade.configuredports.append(interface)
                    blade.configuredportcount += 1

        #per blade Tests
        for blade in oldswitch.blades:
            blade.inuseports = blade.portcount
            blade.delunconfiguredports()
            self.assertEqual(blade.portcount - blade.inuseports, blade.portcount - blade.configuredportcount)
            self.assertEqual(blade.configuredports,blade.interfaces)

    def test_delunusedportsoverperiodoftime_WS_C4507R_E(self):
        """

        Tests the the function 'delunusedportsoverperiodoftime'. Checks to see if the interfaces that are removed
        are accurate

        """
        c = DeviceAccess(Switch_access.username, Switch_access.password)
        oldswitch_con = c.login('172.31.5.5')
        oldswitch = Switch()
        oldswitch.getSwitchInfo(oldswitch_con)
        oldswitch.assignattributes()

        #calcuations to Tests against
        connectedports = []
        connectedportscount = 0
        past = datetime.datetime.now() - datetime.timedelta(days=180)
        for blade in oldswitch.blades:
            blade.connectedports = []
            blade.connectedportscount = 0
            for interface in blade.interfaces:
                if interface.downtime:
                    if interface.downtime > past:
                        connectedports.append(interface)
                        connectedportscount += 1
                        blade.connectedports.append(interface)
                        blade.connectedportscount += 1
                else:
                    #gathers ports on active connections
                    connectedports.append(interface)
                    connectedportscount += 1
                    blade.connectedports.append(interface)
                    blade.connectedportscount += 1

        for blade in oldswitch.blades:
            blade.inuseports = blade.portcount
            blade.delunusedportsoverperiodoftime()
            self.assertEqual(blade.portcount - blade.inuseports, blade.portcount - blade.connectedportscount)
            self.assertEqual(blade.connectedports,blade.interfaces)

    def test_groupbyvlans_WS_C4507R_E(self):
        """

        Tests the the function 'groupbyvlans'. checks the accuratcely of the function by comparing the total interfaces
        before, and after. Also checks the ordering of the vlans from least to greatest.

        """
        c = DeviceAccess(Switch_access.username, Switch_access.password)
        oldswitch_con = c.login('172.31.5.5')
        oldswitch = Switch()
        oldswitch.getSwitchInfo(oldswitch_con)
        oldswitch.assignattributes()
        oldswitch.vlans()

        portsize = []
        #Tests that the ports are orginized largest to smallest.
        for vlan,ports in oldswitch.groupedvlans.items():
            portsize.append(len(ports))
        for counter, port in enumerate(portsize):
            if counter == 0:
                pass
            else:
                self.assertLessEqual(portsize[counter],portsize[counter-1])

        #Tests there are no links to other network devices in this list
        for inter in oldswitch.cdpneighbors:
            for vlan, ports in oldswitch.groupedvlans.items():
                #Tests 0 or 1 are not in the list of vlans
                self.assertNotEqual(int(vlan),0)
                self.assertNotEqual(int(vlan), 1)
                for interface in ports:
                    self.assertNotEqual(inter.link['local'],interface.fullname)

    def test_transferinterface_WS_C4507R_E(self):
        """

        Tests the the function 'transferinterface'. checks that the interface is added to the next open interface
        Checks that the interface is applied to the given interface name.

        """
        c = DeviceAccess(Switch_access.username, Switch_access.password)
        oldswitch_con = c.login('172.31.5.5')
        oldswitch = Switch()
        oldswitch.getSwitchInfo(oldswitch_con)
        oldswitch.assignattributes()

        interface = Interface()
        interface.fullname = 'GigabitEthernet0/1'
        interface.type = 'copper'
        interface.vlan = 125
        interface.dualmode = True
        interface.voicevlan = 360
        interface.stpf = True

        #test error response that the port name is not on device
        with self.assertRaises(ValueError):
            oldswitch.blades[0].transferinterface(interfaceobj=interface,portname=interface.fullname)


        interface.fullname = 'GigabitEthernet1/8'
        for blade in oldswitch.blades:
            for inter in blade.interfaces:
                if inter.fullname == f'interface {interface.fullname}':
                    inter.vlan = 456
                    inter.dualmode = False
                    inter.voicevlan = 678
                    inter.stpf = False
                    break

        interface.fullname = 'GigabitEthernet1/7'
        # test assignment to specific port
        oldswitch.blades[0].transferinterface(interfaceobj=interface, portname='GigabitEthernet1/8')
        interface.fullname = 'GigabitEthernet1/8'
        for inter in oldswitch.allinterfaces():
            if inter.fullname == f'interface {interface.fullname}':
                self.assertEqual(inter.type, interface.type)
                self.assertEqual(inter.vlan, interface.vlan)
                self.assertEqual(inter.dualmode, interface.dualmode)
                self.assertEqual(inter.voicevlan, interface.voicevlan)
                self.assertEqual(inter.stpf, interface.stpf)


        # test assignmnet to next available port should be 1/7
        interface.fullname = f'GigabitEthernet1/{random.randint(7, 18)}'
        oldswitch.blades[0].transferinterface(interfaceobj=interface, nextavailable=True)
        self.assertGreater(len(oldswitch.allinterfaces()),1)
        for inter in oldswitch.allinterfaces():
            if inter.fullname == f'interface GigabitEthernet1/7':
                self.assertEqual(inter.type, interface.type)
                self.assertEqual(inter.vlan, interface.vlan)
                self.assertEqual(inter.dualmode, interface.dualmode)
                self.assertEqual(inter.voicevlan, interface.voicevlan)
                self.assertEqual(inter.stpf, interface.stpf)

    def test_migratetonewhardware_WS_C2960S_48FPD_L_to_WS_C3650_48PQ(self):
        #create the oldswitch object
        c = DeviceAccess(Switch_access.username, Switch_access.password)
        oldswitch_con = c.login('172.31.5.11')
        oldswitch = Switch()
        oldswitch.getSwitchInfo(oldswitch_con)
        oldswitch.assignattributes()

        #collect all the interfaces active switches
        activeports = []
        for blade in oldswitch.blades:
            blade.delunconfiguredports()
            blade.delunusedportsoverperiodoftime()
            blade.delportswithouttraffic()
            for interface in blade.interfaces:
                activeports.append(interface)

        #collect the vlans thosw switches are on
        oldvlans = oldswitch.vlans()


        c = DeviceAccess(Switch_access.username, Switch_access.password)
        newswitch_con = c.login('172.31.5.11')
        newswitch = Switch()
        newswitch.getSwitchInfo(newswitch_con)
        newswitch.assignattributes()

        unconfigports = []
        for blade in newswitch.blades:
            for interface in blade.interfaces:
                unconfigports.append(interface)

        #run the function
        b = Building(dx1='172.31.5.13', dx2='172.31.5.12')
        b.migratetonewhardware(oldswitch,newswitch)

        #pull the data from that switch again
        c = DeviceAccess(Switch_access.username, Switch_access.password)
        newswitch_con_2 = c.login('172.31.5.11')
        newswitch_2 = Switch()
        newswitch_2.getSwitchInfo(newswitch_con_2)
        newswitch_2.assignattributes()

        #remove the unconfigured ports from the list of ports
        appliedports = []
        for blade in newswitch_2.blades:
            for interface in blade.interfaces:
                blade.delunconfiguredports()
                appliedports.append(interface)
        #pull the new vlans
        newvlans = newswitch_2.vlans()

        #checks to see if the correct ports were transfered to the new device
        self.assertEqual(len(activeports),len(appliedports))

        #checks to see that all the Vlans are on the new switch, and the correct amount of ports were assigned
        for key,value in oldvlans.items():
            self.assertIn(key,newvlans.keys())
            self.assertEqual(len(value),newvlans[key])

    def test_correctlinkinterfaces(self):
        """
        Checks to see if the checks put in place for the interface are followed properly.
        """
        test_batch = [
            '172.30.132.4',
            '172.30.134.132']

        for ip in test_batch:
            c = DeviceAccess(Switch_access.username, Switch_access.password)
            dx_con = c.login(ip)
            dx = Switch()
            dx.getSwitchInfo(dx_con)
            dx.assignattributes()

            switches = []
            dx_list = []

            #sort out the devices connected to DX, and create the correct interface descriptions
            for switch in dx.cdpneighbors:
                switches.append(switch)
                remote = switch.link["remote"]
                remote = re.sub("nGigabitEthernet", "", remote)
                remote = re.sub("igabitEthernet", "", remote)
                remote = re.sub("ernet", "", remote)
                local = switch.link["local"]
                local = re.sub("nGigabitEthernet", "", local)
                local = re.sub("igabitEthernet", "", local)
                local = re.sub("ernet", "", local)
                dxint = (local,f'description key:{local}:{switch.hostname}:{remote}')
                dx_list.append(dxint)
                if 'r1' in switch.hostname or 'r2' in switch.hostname:
                    descrip = (switch.IPAddress, remote, f'description key:{remote}:{dx.hostname}:{local}')
                    switches.append(descrip)
                elif 'sx' in switch.hostname:
                    descrip = (switch.IPAddress, remote, f'description key:{remote}:{dx.hostname}:{local}')
                    switches.append(descrip)

            #run the function
            b = Building(dx1=dx)
            b.correctlinkinterfaces()


            #test the results of running the function on the dx
            c = DeviceAccess(Switch_access.username, Switch_access.password)
            dx_con = c.login('172.31.5.12')
            for descrip in dx_list:
                result = dx_con.send_command(f'show run int {descrip[0]}')
                result = result.split('\r\n')
                #test that there is a description on the interface
                self.assertIn('description',result)
                for line in result:
                    if 'description' in line:
                        description = re.sub('description','',line)
                        description = re.sub(' ', '', description)
                        #test that the description on the interface is correctly applied
                        self.assertEqual(description,descrip[1])

            #test the results of the function on all the devices connected to dx
            for switch in switches:
                c = DeviceAccess(Switch_access.username, Switch_access.password)
                dx_con = c.login(switch[0])
                result = dx_con.send_command(f'show run int {switch[1]}')
                result = result.split('\r\n')
                self.assertIn('description', result)
                for line in result:
                    if 'description' in line:
                        description = re.sub('description','',line)
                        description = re.sub(' ', '', description)
                        #test that the description on the interface is correctly applied
                        self.assertEqual(description,switch[2])

    def test_correctlinkinterfaces_logging(self):
        """
        the logging for this switch update is very important. It collects the data for buisness processing.
        This Tests to ensure that the logging is being done properly, and is actually happening
        """

        test_batch = [
            '172.30.132.4',
            '172.30.134.132']

        #collect the information about the switches
        for ip in test_batch:
            c = DeviceAccess(Switch_access.username, Switch_access.password)
            dx_con = c.login(ip)
            dx = Switch()
            dx.getSwitchInfo(dx_con)
            dx.assignattributes()



        with open(file='switchupdate_metrics.log',mode='r') as f:
            logfile = f.read()

            for switch in dx.cdpneighbors:
                remote = switch.link["remote"]
                remote = re.sub("nGigabitEthernet", "", remote)
                remote = re.sub("igabitEthernet", "", remote)
                remote = re.sub("ernet", "", remote)
                local = switch.link["local"]
                local = re.sub("nGigabitEthernet", "", local)
                local = re.sub("igabitEthernet", "", local)
                local = re.sub("ernet", "", local)
                if 'r1' in switch.hostname or 'r2' in switch.hostname:
                    logmessage = f'Device:{switch.IPAddress} Description:description key:{remote}:{dx.hostname}:{local} on {remote} - Correct'
                    logmessagewrong = f'Device:{switch.IPAddress} Description:description key:{remote}:{dx.hostname}:{local} on {remote}  - Incorrect'
                    logmessagemssing = f'Device:{switch.IPAddress} Description on {remote} - missing'
                elif 'sx' in switch.hostname:
                    logmessage = f'Device:{switch.IPAddress} Description:description key:{remote}:{dx.hostname}:{local} on {remote} - Correct'
                    logmessagewrong = f'Device:{switch.IPAddress} Description:description key:{remote}:{dx.hostname}:{local} on {remote}  - Incorrect'
                    logmessagemssing = f'Device:{switch.IPAddress} Description on {remote} - missing'
                if logmessage in logfile:
                    self.assertIn(logmessage, logfile)
                elif logmessagemssing in logfile:
                    self.assertIn(logmessagemssing,logfile)
                elif logmessagewrong in logfile:
                    self.assertIn(logmessagewrong,logfile)
                else:
                    self.assertTrue(False)

class TestRouterCommandResults(unittest.TestCase):
    """
    This class of Tests are for the Router Class
    """

    def test_getSwitchInfo_Cisco_C6880X(self):
        """
        This function Tests the gathering of information from a Cisco Router Model C6880x
        Also currently used as the R1-remote Routers
        """

        c = DeviceAccess(Switch_access.username, Switch_access.password)
        r_con = c.login("172.29.4.1")
        rx = Router()
        rx.getSwitchInfo(r_con)

        #Tests that the hostname was assigned
        self.assertTrue(rx.hostname)
        self.assertEqual("r1-remote",rx.hostname)


        #test Version results
        #ensures the sent command didn't error out
        self.assertNotIn('% Incomplete command.',rx.version_result)
        self.assertNotIn('% Unrecognized command',rx.version_result)
        self.assertNotIn('% Unrecognized command', rx.version_result)
        self.assertNotIn("% Invalid input detected at '^' marker.", rx.version_result)
        # checks this is the correct Command was sent, and the correct response was sent
        # and checks for the line that Version function looks for
        self.assertIn("Cisco IOS Software", rx.version_result)
        # checks to make sure this is not a Nexus Device
        self.assertNotIn("Nexus", rx.version_result)
        self.assertNotIn("Device name:", rx.version_result)
        self.assertNotIn("Kernel uptime", rx.version_result)
        self.assertNotIn("system:", rx.version_result)

        #checks model number is present
        self.assertIn("C6880-X",rx.version_result)
        #checks for to see if the Up time is present
        self.assertIn("uptime is",rx.version_result)
        #checks that the trigger for the Serial Number is present
        self.assertIn("Processor board ID", rx.version_result)

        #test physical interface Results
        self.assertNotIn('% Incomplete command.', rx.interface_result)
        self.assertNotIn('% Unrecognized command', rx.interface_result)
        self.assertNotIn('% Unrecognized command', rx.interface_result)
        self.assertNotIn("% Invalid input detected at '^' marker.", rx.interface_result)

        #make sure the results don't include the Vlan interfaces
        self.assertNotIn("vrf", rx.interface_result)
        self.assertNotIn("interface Vlan", rx.interface_result)

        #test Portdowntime_result
        self.assertFalse(rx.portdowntime_result)

        #test Inv_results
        self.assertNotIn('% Incomplete command.', rx.inv_result)
        self.assertNotIn('% Unrecognized command', rx.inv_result)
        self.assertNotIn('% Unrecognized command', rx.inv_result)
        self.assertNotIn("% Invalid input detected at '^' marker.", rx.inv_result)

        self.assertIn("NAME:", rx.inv_result)
        self.assertIn("PID:", rx.inv_result)
        self.assertIn("VID:", rx.inv_result)
        self.assertIn("SN:", rx.inv_result)
        self.assertIn("DESCR:", rx.inv_result)

        #test Portcount
        self.assertNotIn('% Incomplete command.', rx.portcount_result)
        self.assertNotIn('% Unrecognized command', rx.portcount_result)
        self.assertNotIn('% Unrecognized command', rx.portcount_result)
        self.assertNotIn("% Invalid input detected at '^' marker.", rx.portcount_result)

        self.assertIn("Port", rx.portcount_result)
        self.assertIn("InOctets", rx.portcount_result)
        self.assertIn("InUcastPkts", rx.portcount_result)
        self.assertIn("InMcastPkts", rx.portcount_result)
        self.assertIn("InBcastPkts", rx.portcount_result)
        self.assertIn("OutOctets", rx.portcount_result)
        self.assertIn("OutUcastPkts", rx.portcount_result)
        self.assertIn("OutMcastPkts", rx.portcount_result)
        self.assertIn("OutBcastPkts", rx.portcount_result)


        #test cdpnei
        self.assertNotIn('% Incomplete command.', rx.cdpnei_result)
        self.assertNotIn('% Unrecognized command', rx.cdpnei_result)
        self.assertNotIn('% Unrecognized command', rx.cdpnei_result)
        self.assertNotIn("% Invalid input detected at '^' marker.", rx.cdpnei_result)

        self.assertIn("-------------------------", rx.cdpnei_result)
        self.assertIn("Device ID:", rx.cdpnei_result)
        self.assertIn("Entry address(es):", rx.cdpnei_result)
        self.assertIn("Platform:", rx.cdpnei_result)
        self.assertIn("Interface:", rx.cdpnei_result)
        self.assertIn("Port ID", rx.cdpnei_result)
        self.assertIn("Holdtime :", rx.cdpnei_result)
        self.assertIn("Version :", rx.cdpnei_result)
        self.assertIn("Duplex:", rx.cdpnei_result)

        #test Module
        self.assertNotIn('% Incomplete command.', rx.module_result)
        self.assertNotIn('% Unrecognized command', rx.module_result)
        self.assertNotIn('% Unrecognized command', rx.module_result)
        self.assertNotIn("% Invalid input detected at '^' marker.", rx.module_result)

        self.assertIn("Mod", rx.module_result)
        self.assertIn("Ports", rx.module_result)
        self.assertIn("Card", rx.module_result)
        self.assertIn("Model", rx.module_result)
        self.assertIn("Serial No.", rx.module_result)
        self.assertIn("MAC addresses", rx.module_result)
        self.assertIn("Sub-Module", rx.module_result)
        self.assertIn("Online Diag Status", rx.module_result)

        #test vlan interface
        self.assertNotIn('% Incomplete command.', rx.vlan_interface_result)
        self.assertNotIn('% Unrecognized command', rx.vlan_interface_result)
        self.assertNotIn('% Unrecognized command', rx.vlan_interface_result)
        self.assertNotIn("% Invalid input detected at '^' marker.", rx.vlan_interface_result)

        #make sure the results don't include the Vlan interfaces
        self.assertNotIn("Ethernet", rx.vlan_interface_result)
        self.assertNotIn("switchport mode trunk", rx.vlan_interface_result)

    def test_getSwitchInfo_Cisco_Nexus7700(self):
        """
        This function Tests the gathering of information from a Cisco Router Model C6880x
        Also currently used as the EBC Routers
        """

        c = DeviceAccess(Switch_access.username, Switch_access.password)
        r_con = c.login("172.29.1.10")
        rx = Router()
        rx.getSwitchInfo(r_con)

        #Tests that the hostname was assigned
        self.assertTrue(rx.hostname)
        self.assertEqual("r1-ebc-ebc",rx.hostname)


        #test Version results
        #ensures the sent command didn't error out
        self.assertNotIn('% Incomplete command.',rx.version_result)
        self.assertNotIn('% Unrecognized command',rx.version_result)
        self.assertNotIn('% Unrecognized command', rx.version_result)
        self.assertNotIn("% Invalid input detected at '^' marker.", rx.version_result)
        # checks this is the correct Command was sent, and the correct response was sent
        # and checks for the line that Version function looks for
        self.assertIn("Cisco Nexus Operating System", rx.version_result)
        # checks to make sure this is not a Nexus Device
        self.assertIn("Nexus", rx.version_result)
        self.assertIn("Software", rx.version_result)
        self.assertIn("Hardware", rx.version_result)
        self.assertIn("Kernel uptime", rx.version_result)
        self.assertIn("Processor Board ID", rx.version_result)

        #checks model number is present
        self.assertIn("Nexus7700",rx.version_result)

        #test physical interface Results
        self.assertNotIn('% Incomplete command.', rx.interface_result)
        self.assertNotIn('% Unrecognized command', rx.interface_result)
        self.assertNotIn('% Unrecognized command', rx.interface_result)
        self.assertNotIn("% Invalid input detected at '^' marker.", rx.interface_result)

        #make sure the results don't include the Vlan interfaces
        self.assertNotIn("interface Vlan", rx.interface_result)

        #test Portdowntime_result
        self.assertFalse(rx.portdowntime_result)

        #test Inv_results
        self.assertNotIn('% Incomplete command.', rx.inv_result)
        self.assertNotIn('% Unrecognized command', rx.inv_result)
        self.assertNotIn('% Unrecognized command', rx.inv_result)
        self.assertNotIn("% Invalid input detected at '^' marker.", rx.inv_result)

        self.assertIn("NAME:", rx.inv_result)
        self.assertIn("PID:", rx.inv_result)
        self.assertIn("VID:", rx.inv_result)
        self.assertIn("SN:", rx.inv_result)
        self.assertIn("DESCR:", rx.inv_result)

        #test Portcount
        self.assertNotIn('% Incomplete command.', rx.portcount_result)
        self.assertNotIn('% Unrecognized command', rx.portcount_result)
        self.assertNotIn('% Unrecognized command', rx.portcount_result)
        self.assertNotIn("% Invalid input detected at '^' marker.", rx.portcount_result)

        self.assertIn("Port", rx.portcount_result)
        self.assertIn("--------------------------------------------------------------------------------", rx.portcount_result)
        self.assertIn("InOctets", rx.portcount_result)
        self.assertIn("InUcastPkts", rx.portcount_result)
        self.assertIn("InMcastPkts", rx.portcount_result)
        self.assertIn("InBcastPkts", rx.portcount_result)
        self.assertIn("OutOctets", rx.portcount_result)
        self.assertIn("OutUcastPkts", rx.portcount_result)
        self.assertIn("OutMcastPkts", rx.portcount_result)
        self.assertIn("OutBcastPkts", rx.portcount_result)


        #test cdpnei
        self.assertNotIn('% Incomplete command.', rx.cdpnei_result)
        self.assertNotIn('% Unrecognized command', rx.cdpnei_result)
        self.assertNotIn('% Unrecognized command', rx.cdpnei_result)
        self.assertNotIn("% Invalid input detected at '^' marker.", rx.cdpnei_result)

        self.assertIn("-------------------------", rx.cdpnei_result)
        self.assertIn("Device ID:", rx.cdpnei_result)
        self.assertIn("Device ID:", rx.cdpnei_result)
        self.assertIn("Platform:", rx.cdpnei_result)
        self.assertIn("Interface:", rx.cdpnei_result)
        self.assertIn("Port ID", rx.cdpnei_result)
        self.assertIn("Holdtime:", rx.cdpnei_result)
        self.assertIn("Version:", rx.cdpnei_result)
        self.assertIn("Duplex:", rx.cdpnei_result)

        #test Module
        self.assertNotIn('% Incomplete command.', rx.module_result)
        self.assertNotIn('% Unrecognized command', rx.module_result)
        self.assertNotIn('% Unrecognized command', rx.module_result)
        self.assertNotIn("% Invalid input detected at '^' marker.", rx.module_result)

        self.assertIn("Mod", rx.module_result)
        self.assertIn("Ports", rx.module_result)
        self.assertIn("Model", rx.module_result)
        self.assertIn("Serial-Num", rx.module_result)
        self.assertIn("MAC-Address(es)", rx.module_result)
        self.assertIn("Module-Type", rx.module_result)
        self.assertIn("Online Diag Status", rx.module_result)
        self.assertIn("Xbar", rx.module_result)
        self.assertIn("Sw", rx.module_result)

        #test vlan interface
        self.assertNotIn('% Incomplete command.', rx.vlan_interface_result)
        self.assertNotIn('% Unrecognized command', rx.vlan_interface_result)
        self.assertNotIn('% Unrecognized command', rx.vlan_interface_result)
        self.assertNotIn("% Invalid input detected at '^' marker.", rx.vlan_interface_result)

        #make sure the results don't include the Vlan interfaces
        self.assertNotIn("Ethernet", rx.vlan_interface_result)
        self.assertNotIn("switchport mode trunk", rx.vlan_interface_result)

    def test_getSwitchInfo_Cisco_Nexus7000(self):
        """
        This function Tests the gathering of information from a Cisco Router Model C6880x
        Also currently used as the park,lib Routers
        """

        c = DeviceAccess(Switch_access.username, Switch_access.password)
        r_con = c.login("172.29.1.12")
        rx = Router()
        rx.getSwitchInfo(r_con)

        #Tests that the hostname was assigned
        self.assertTrue(rx.hostname)
        self.assertEqual("r1-park-ebc",rx.hostname)


        #test Version results
        #ensures the sent command didn't error out
        self.assertNotIn('% Incomplete command.',rx.version_result)
        self.assertNotIn('% Unrecognized command',rx.version_result)
        self.assertNotIn('% Unrecognized command', rx.version_result)
        self.assertNotIn("% Invalid input detected at '^' marker.", rx.version_result)
        # checks this is the correct Command was sent, and the correct response was sent
        # and checks for the line that Version function looks for
        self.assertIn("Cisco Nexus Operating System", rx.version_result)
        # checks to make sure this is not a Nexus Device
        self.assertIn("Nexus", rx.version_result)
        self.assertIn("Software", rx.version_result)
        self.assertIn("Hardware", rx.version_result)
        self.assertIn("Kernel uptime", rx.version_result)
        self.assertIn("Processor Board ID", rx.version_result)

        #checks model number is present
        self.assertIn("Nexus7000",rx.version_result)
        self.assertIn("C7010", rx.version_result)

        #test physical interface Results
        self.assertNotIn('% Incomplete command.', rx.interface_result)
        self.assertNotIn('% Unrecognized command', rx.interface_result)
        self.assertNotIn('% Unrecognized command', rx.interface_result)
        self.assertNotIn("% Invalid input detected at '^' marker.", rx.interface_result)

        #make sure the results don't include the Vlan interfaces
        self.assertNotIn("interface Vlan", rx.interface_result)

        #test Portdowntime_result
        self.assertFalse(rx.portdowntime_result)

        #test Inv_results
        self.assertNotIn('% Incomplete command.', rx.inv_result)
        self.assertNotIn('% Unrecognized command', rx.inv_result)
        self.assertNotIn('% Unrecognized command', rx.inv_result)
        self.assertNotIn("% Invalid input detected at '^' marker.", rx.inv_result)

        self.assertIn("NAME:", rx.inv_result)
        self.assertIn("PID:", rx.inv_result)
        self.assertIn("VID:", rx.inv_result)
        self.assertIn("SN:", rx.inv_result)
        self.assertIn("DESCR:", rx.inv_result)

        #test Portcount
        self.assertNotIn('% Incomplete command.', rx.portcount_result)
        self.assertNotIn('% Unrecognized command', rx.portcount_result)
        self.assertNotIn('% Unrecognized command', rx.portcount_result)
        self.assertNotIn("% Invalid input detected at '^' marker.", rx.portcount_result)

        self.assertIn("Port", rx.portcount_result)
        self.assertIn("--------------------------------------------------------------------------------", rx.portcount_result)
        self.assertIn("InOctets", rx.portcount_result)
        self.assertIn("InUcastPkts", rx.portcount_result)
        self.assertIn("InMcastPkts", rx.portcount_result)
        self.assertIn("InBcastPkts", rx.portcount_result)
        self.assertIn("OutOctets", rx.portcount_result)
        self.assertIn("OutUcastPkts", rx.portcount_result)
        self.assertIn("OutMcastPkts", rx.portcount_result)
        self.assertIn("OutBcastPkts", rx.portcount_result)


        #test cdpnei
        self.assertNotIn('% Incomplete command.', rx.cdpnei_result)
        self.assertNotIn('% Unrecognized command', rx.cdpnei_result)
        self.assertNotIn('% Unrecognized command', rx.cdpnei_result)
        self.assertNotIn("% Invalid input detected at '^' marker.", rx.cdpnei_result)

        self.assertIn("-------------------------", rx.cdpnei_result)
        self.assertIn("Device ID:", rx.cdpnei_result)
        self.assertIn("Device ID:", rx.cdpnei_result)
        self.assertIn("Platform:", rx.cdpnei_result)
        self.assertIn("Interface:", rx.cdpnei_result)
        self.assertIn("Port ID", rx.cdpnei_result)
        self.assertIn("Holdtime:", rx.cdpnei_result)
        self.assertIn("Version:", rx.cdpnei_result)
        self.assertIn("Duplex:", rx.cdpnei_result)

        #test Module
        self.assertNotIn('% Incomplete command.', rx.module_result)
        self.assertNotIn('% Unrecognized command', rx.module_result)
        self.assertNotIn('% Unrecognized command', rx.module_result)
        self.assertNotIn("% Invalid input detected at '^' marker.", rx.module_result)

        self.assertIn("Mod", rx.module_result)
        self.assertIn("Ports", rx.module_result)
        self.assertIn("Model", rx.module_result)
        self.assertIn("Serial-Num", rx.module_result)
        self.assertIn("MAC-Address(es)", rx.module_result)
        self.assertIn("Module-Type", rx.module_result)
        self.assertIn("Online Diag Status", rx.module_result)
        self.assertIn("Xbar", rx.module_result)
        self.assertIn("Sw", rx.module_result)

        #test vlan interface
        self.assertNotIn('% Incomplete command.', rx.vlan_interface_result)
        self.assertNotIn('% Unrecognized command', rx.vlan_interface_result)
        self.assertNotIn('% Unrecognized command', rx.vlan_interface_result)
        self.assertNotIn("% Invalid input detected at '^' marker.", rx.vlan_interface_result)

        #make sure the results don't include the Vlan interfaces
        self.assertNotIn("Ethernet", rx.vlan_interface_result)
        self.assertNotIn("switchport mode trunk", rx.vlan_interface_result)

    def test_getSwitchInfo_Cisco_WSC6509E(self):
        """
        This function Tests the gathering of information from a Cisco Router Model C6880x
        Also currently used as the fort Routers
        """

        c = DeviceAccess(Switch_access.username, Switch_access.password)
        r_con = c.login("172.29.1.18")
        rx = Router()
        rx.getSwitchInfo(r_con)

        #Tests that the hostname was assigned
        self.assertTrue(rx.hostname)
        self.assertEqual("r1-fort", rx.hostname)

        #test Version results
        #ensures the sent command didn't error out
        self.assertNotIn('% Incomplete command.',rx.version_result)
        self.assertNotIn('% Unrecognized command',rx.version_result)
        self.assertNotIn('% Unrecognized command', rx.version_result)
        self.assertNotIn("% Invalid input detected at '^' marker.", rx.version_result)
        # checks this is the correct Command was sent, and the correct response was sent
        # and checks for the line that Version function looks for
        self.assertIn("Cisco IOS Software", rx.version_result)
        # checks to make sure this is not a Nexus Device
        self.assertNotIn("Nexus", rx.version_result)
        self.assertNotIn("Device name:", rx.version_result)
        self.assertNotIn("Kernel uptime", rx.version_result)
        self.assertNotIn("system:", rx.version_result)

        #checks model number is present
        self.assertIn("WS-C6509-E",rx.version_result)
        #checks for to see if the Up time is present
        self.assertIn("uptime is",rx.version_result)
        #checks that the trigger for the Serial Number is present
        self.assertIn("Processor board ID", rx.version_result)

        #test physical interface Results
        self.assertNotIn('% Incomplete command.', rx.interface_result)
        self.assertNotIn('% Unrecognized command', rx.interface_result)
        self.assertNotIn('% Unrecognized command', rx.interface_result)
        self.assertNotIn("% Invalid input detected at '^' marker.", rx.interface_result)

        #make sure the results don't include the Vlan interfaces
        self.assertNotIn("vrf", rx.interface_result)
        self.assertNotIn("interface Vlan", rx.interface_result)

        #test Portdowntime_result
        self.assertFalse(rx.portdowntime_result)

        #test Inv_results
        self.assertNotIn('% Incomplete command.', rx.inv_result)
        self.assertNotIn('% Unrecognized command', rx.inv_result)
        self.assertNotIn('% Unrecognized command', rx.inv_result)
        self.assertNotIn("% Invalid input detected at '^' marker.", rx.inv_result)

        self.assertIn("NAME:", rx.inv_result)
        self.assertIn("PID:", rx.inv_result)
        self.assertIn("VID:", rx.inv_result)
        self.assertIn("SN:", rx.inv_result)
        self.assertIn("DESCR:", rx.inv_result)

        #test Portcount
        self.assertNotIn('% Incomplete command.', rx.portcount_result)
        self.assertNotIn('% Unrecognized command', rx.portcount_result)
        self.assertNotIn('% Unrecognized command', rx.portcount_result)
        self.assertNotIn("% Invalid input detected at '^' marker.", rx.portcount_result)

        self.assertIn("Port", rx.portcount_result)
        self.assertIn("InOctets", rx.portcount_result)
        self.assertIn("InUcastPkts", rx.portcount_result)
        self.assertIn("InMcastPkts", rx.portcount_result)
        self.assertIn("InBcastPkts", rx.portcount_result)
        self.assertIn("OutOctets", rx.portcount_result)
        self.assertIn("OutUcastPkts", rx.portcount_result)
        self.assertIn("OutMcastPkts", rx.portcount_result)
        self.assertIn("OutBcastPkts", rx.portcount_result)


        #test cdpnei
        self.assertNotIn('% Incomplete command.', rx.cdpnei_result)
        self.assertNotIn('% Unrecognized command', rx.cdpnei_result)
        self.assertNotIn('% Unrecognized command', rx.cdpnei_result)
        self.assertNotIn("% Invalid input detected at '^' marker.", rx.cdpnei_result)

        self.assertIn("-------------------------", rx.cdpnei_result)
        self.assertIn("Device ID:", rx.cdpnei_result)
        self.assertIn("Entry address(es):", rx.cdpnei_result)
        self.assertIn("Platform:", rx.cdpnei_result)
        self.assertIn("Interface:", rx.cdpnei_result)
        self.assertIn("Port ID", rx.cdpnei_result)
        self.assertIn("Holdtime :", rx.cdpnei_result)
        self.assertIn("Version :", rx.cdpnei_result)
        self.assertIn("Duplex:", rx.cdpnei_result)

        #test Module
        self.assertNotIn('% Incomplete command.', rx.module_result)
        self.assertNotIn('% Unrecognized command', rx.module_result)
        self.assertNotIn('% Unrecognized command', rx.module_result)
        self.assertNotIn("% Invalid input detected at '^' marker.", rx.module_result)

        self.assertIn("Mod", rx.module_result)
        self.assertIn("Ports", rx.module_result)
        self.assertIn("Card", rx.module_result)
        self.assertIn("Model", rx.module_result)
        self.assertIn("Serial No.", rx.module_result)
        self.assertIn("MAC addresses", rx.module_result)
        self.assertIn("Sub-Module", rx.module_result)
        self.assertIn("Online Diag Status", rx.module_result)

        #test vlan interface
        self.assertNotIn('% Incomplete command.', rx.vlan_interface_result)
        self.assertNotIn('% Unrecognized command', rx.vlan_interface_result)
        self.assertNotIn('% Unrecognized command', rx.vlan_interface_result)
        self.assertNotIn("% Invalid input detected at '^' marker.", rx.vlan_interface_result)

        #make sure the results don't include the Vlan interfaces
        self.assertNotIn("Ethernet", rx.vlan_interface_result)
        self.assertNotIn("switchport mode trunk", rx.vlan_interface_result)

    def test_getSwitchInfo_Cisco_C6816XLE(self):
        """
        This function Tests the gathering of information from a Cisco Router Model C6880x
        Also currently used as the farmington Routers
        """

        c = DeviceAccess(Switch_access.username, Switch_access.password)
        r_con = c.login("172.29.4.13")
        rx = Router()
        rx.getSwitchInfo(r_con)

        #Tests that the hostname was assigned
        self.assertTrue(rx.hostname)
        self.assertEqual("r1-3716Farmington", rx.hostname)

        #test Version results
        #ensures the sent command didn't error out
        self.assertNotIn('% Incomplete command.',rx.version_result)
        self.assertNotIn('% Unrecognized command',rx.version_result)
        self.assertNotIn('% Unrecognized command', rx.version_result)
        self.assertNotIn("% Invalid input detected at '^' marker.", rx.version_result)
        # checks this is the correct Command was sent, and the correct response was sent
        # and checks for the line that Version function looks for
        self.assertIn("Cisco IOS Software", rx.version_result)
        # checks to make sure this is not a Nexus Device
        self.assertNotIn("Nexus", rx.version_result)
        self.assertNotIn("Device name:", rx.version_result)
        self.assertNotIn("Kernel uptime", rx.version_result)
        self.assertNotIn("system:", rx.version_result)

        #checks model number is present
        self.assertIn("C6816-X-LE",rx.version_result)
        #checks for to see if the Up time is present
        self.assertIn("uptime is",rx.version_result)
        #checks that the trigger for the Serial Number is present
        self.assertIn("Processor board ID", rx.version_result)

        #test physical interface Results
        self.assertNotIn('% Incomplete command.', rx.interface_result)
        self.assertNotIn('% Unrecognized command', rx.interface_result)
        self.assertNotIn('% Unrecognized command', rx.interface_result)
        self.assertNotIn("% Invalid input detected at '^' marker.", rx.interface_result)

        #make sure the results don't include the Vlan interfaces
        self.assertNotIn("vrf", rx.interface_result)
        self.assertNotIn("interface Vlan", rx.interface_result)

        #test Portdowntime_result
        self.assertFalse(rx.portdowntime_result)

        #test Inv_results
        self.assertNotIn('% Incomplete command.', rx.inv_result)
        self.assertNotIn('% Unrecognized command', rx.inv_result)
        self.assertNotIn('% Unrecognized command', rx.inv_result)
        self.assertNotIn("% Invalid input detected at '^' marker.", rx.inv_result)

        self.assertIn("NAME:", rx.inv_result)
        self.assertIn("PID:", rx.inv_result)
        self.assertIn("VID:", rx.inv_result)
        self.assertIn("SN:", rx.inv_result)
        self.assertIn("DESCR:", rx.inv_result)

        #test Portcount
        self.assertNotIn('% Incomplete command.', rx.portcount_result)
        self.assertNotIn('% Unrecognized command', rx.portcount_result)
        self.assertNotIn('% Unrecognized command', rx.portcount_result)
        self.assertNotIn("% Invalid input detected at '^' marker.", rx.portcount_result)

        self.assertIn("Port", rx.portcount_result)
        self.assertIn("InOctets", rx.portcount_result)
        self.assertIn("InUcastPkts", rx.portcount_result)
        self.assertIn("InMcastPkts", rx.portcount_result)
        self.assertIn("InBcastPkts", rx.portcount_result)
        self.assertIn("OutOctets", rx.portcount_result)
        self.assertIn("OutUcastPkts", rx.portcount_result)
        self.assertIn("OutMcastPkts", rx.portcount_result)
        self.assertIn("OutBcastPkts", rx.portcount_result)


        #test cdpnei
        self.assertNotIn('% Incomplete command.', rx.cdpnei_result)
        self.assertNotIn('% Unrecognized command', rx.cdpnei_result)
        self.assertNotIn('% Unrecognized command', rx.cdpnei_result)
        self.assertNotIn("% Invalid input detected at '^' marker.", rx.cdpnei_result)

        self.assertIn("-------------------------", rx.cdpnei_result)
        self.assertIn("Device ID:", rx.cdpnei_result)
        self.assertIn("Entry address(es):", rx.cdpnei_result)
        self.assertIn("Platform:", rx.cdpnei_result)
        self.assertIn("Interface:", rx.cdpnei_result)
        self.assertIn("Port ID", rx.cdpnei_result)
        self.assertIn("Holdtime :", rx.cdpnei_result)
        self.assertIn("Version :", rx.cdpnei_result)
        self.assertIn("Duplex:", rx.cdpnei_result)

        #test Module
        self.assertNotIn('% Incomplete command.', rx.module_result)
        self.assertNotIn('% Unrecognized command', rx.module_result)
        self.assertNotIn('% Unrecognized command', rx.module_result)
        self.assertNotIn("% Invalid input detected at '^' marker.", rx.module_result)

        self.assertIn("Mod", rx.module_result)
        self.assertIn("Ports", rx.module_result)
        self.assertIn("Card", rx.module_result)
        self.assertIn("Model", rx.module_result)
        self.assertIn("Serial No.", rx.module_result)
        self.assertIn("MAC addresses", rx.module_result)
        self.assertIn("Sub-Module", rx.module_result)
        self.assertIn("Online Diag Status", rx.module_result)

        #test vlan interface
        self.assertNotIn('% Incomplete command.', rx.vlan_interface_result)
        self.assertNotIn('% Unrecognized command', rx.vlan_interface_result)
        self.assertNotIn('% Unrecognized command', rx.vlan_interface_result)
        self.assertNotIn("% Invalid input detected at '^' marker.", rx.vlan_interface_result)

        #make sure the results don't include the Vlan interfaces
        self.assertNotIn("Ethernet", rx.vlan_interface_result)
        self.assertNotIn("switchport mode trunk", rx.vlan_interface_result)

    def test_assignattributes_Cisco_C6880X(self):
        """
        Tests the process of transferring the Data collected from router, and moving it into python objects
        """
        c = DeviceAccess(Switch_access.username, Switch_access.password)
        r_con = c.login("172.29.4.1")
        rx = Router()
        rx.getSwitchInfo(r_con)


        #Tests the sortVersion
        rx.sortVersion(rx.version_result)
        self.assertEqual(rx.nexus, None)
        self.assertEqual(rx.version,"15.5(1)SY1")
        self.assertEqual(rx.modelnumber, "C6880-X")
        self.assertEqual(rx.serial, ["SAL1948U5JF"])
        self.assertFalse(rx.blades)
        self.assertIsInstance(rx.uptime, relativedelta)
        self.assertIsInstance(rx.lastrestart, datetime.datetime)

        # Tests the sortInventory
        rx.sortInventory(rx.inv_result)
        self.assertTrue(rx.serial)
        self.assertTrue(rx.SFPs)
        self.assertTrue(rx.blades)
        self.assertTrue(rx.serial,["SAL1948U5JF"])
        self.assertEqual(45,len(rx.SFPs))
        for Trans in rx.SFPs:
            self.assertIsInstance(Trans,SFP)
            self.assertTrue(Trans.speed)
            self.assertTrue(Trans.SN)
            self.assertTrue(Trans.port)
        self.assertEqual(3, len(rx.blades))
        for b in rx.blades:
            self.assertIsInstance(b,Blade)
            self.assertTrue(b.serialnumber)
            self.assertTrue(b.stacknumber)

        # Tests the sortmodule
        rx.sortmodule(rx.module_result)
        self.assertTrue(rx.serial)
        self.assertTrue(rx.SFPs)
        self.assertTrue(rx.blades)
        self.assertEqual(3, len(rx.blades))
        for b in rx.blades:
            self.assertIsInstance(b, Blade)
            self.assertTrue(b.status)
            self.assertTrue(b.modelnumber)
            self.assertTrue(b.serialnumber)
            self.assertTrue(b.portcount)
            self.assertTrue(b.stacknumber)
            self.assertTrue(b.fwversion)
            self.assertTrue(b.ISOversion)
            self.assertTrue(b.hwversion)
            self.assertTrue(b.macaddresses)

        # Tests the sortinterfaces
        rx.sortinterfaces(rx.interface_result)
        #test eacch blade for ports
        for b in rx.blades:
            self.assertIsInstance(b, Blade)
            self.assertTrue(b.interfaces)
            # for interface in b.interfaces:
            self.assertEqual(len(b.interfaces),16)
            portrange = range(1,17)
            for port,interface in b.interfaces.items():
                self.assertIn(int(port),portrange)
                self.assertTrue(interface.portnumber)
                self.assertTrue(interface.blade)

        # Tests the sort_vlan_interfaces
        rx.sort_vlan_interfaces(rx.vlan_interface_result)
        self.assertEqual(184,len(rx.vlansints))
        for vl in rx.vlansints:
            self.assertIsInstance(vl,vlan)
            self.assertTrue(vl.number)
            self.assertTrue(vl.rawdata)

        # Tests the sortCdpNeiDetail
        rx.sortCdpNeiDetail(rx.cdpnei_result)
        self.assertEqual(39,len(rx.cdpneighbors))
        for n in rx.cdpneighbors:
            self.assertIsInstance(n,Neighbor)
            self.assertTrue(n.deviceid)
            self.assertTrue(n.platform)
            self.assertTrue(n.duplex)
            self.assertTrue(n.ip)
            self.assertTrue(n.interface)
            self.assertTrue(n.remote_interface)
            self.assertIsInstance(n.interface,Interface)
            self.assertIsInstance(n.remote_interface, Interface)

        # Tests the sortportcounters
        rx.sortportcounters(rx.portcount_result)
        for blade in rx.blades:
            for count, port in blade.interfaces.items():
                self.assertIsNotNone(port.InOctets)
                self.assertIsNotNone(port.InUcastPkts)
                self.assertIsNotNone(port.InBcastPkts)
                self.assertIsNotNone(port.outOctets)
                self.assertIsNotNone(port.outUcastPkts)
                self.assertIsNotNone(port.outBcastPkts)
                self.assertIsNotNone(port.outMcastPkts)
                self.assertIsNotNone(port.outBcastPkts)
                self.assertIsNotNone(port.InMcastPkts)

    def test_assignattributes_Cisco_Nexus7700(self):
        """
        """
        c = DeviceAccess(Switch_access.username, Switch_access.password)
        r_con = c.login("172.29.1.10")
        rx = Router()
        rx.getSwitchInfo(r_con)
        rx.assignattributes(r_con)

        # Tests the sortVersion
        rx.sortVersion(rx.version_result)
        self.assertTrue(rx.nexus)
        self.assertEqual(rx.version, "8.2(2)")
        self.assertEqual(rx.modelnumber, "Nexus7700 C7710")
        self.assertEqual(rx.serial, ["JAE23022TX1"])
        self.assertFalse(rx.blades)
        self.assertIsInstance(rx.uptime, relativedelta)
        self.assertIsInstance(rx.lastrestart, datetime.datetime)

        # Tests the sortInventory
        rx.sortInventory(rx.inv_result)
        self.assertTrue(rx.serial)
        self.assertTrue(rx.SFPs)
        self.assertTrue(rx.blades)
        self.assertTrue(rx.serial, ["JAE23022TX1"])
        self.assertEqual(42, len(rx.SFPs))
        for Trans in rx.SFPs:
            self.assertIsInstance(Trans, SFP)
            self.assertTrue(Trans.speed)
            self.assertTrue(Trans.SN)
            self.assertTrue(Trans.port)
        self.assertEqual(3, len(rx.blades))
        for b in rx.blades:
            self.assertIsInstance(b, Blade)
            self.assertTrue(b.serialnumber)
            self.assertTrue(b.stacknumber)

        # Tests the sortmodule
        rx.sortmodule(rx.module_result)
        self.assertTrue(rx.serial)
        self.assertTrue(rx.SFPs)
        self.assertTrue(rx.blades)
        self.assertEqual(3, len(rx.blades))
        for b in rx.blades:
            self.assertIsInstance(b, Blade)
            self.assertTrue(b.status)
            self.assertTrue(b.modelnumber)
            self.assertTrue(b.serialnumber)
            self.assertTrue(b.portcount)
            self.assertTrue(b.stacknumber)
            self.assertTrue(b.fwversion)
            self.assertTrue(b.ISOversion)
            self.assertTrue(b.hwversion)
            self.assertTrue(b.macaddresses)

        # Tests the sortinterfaces
        rx.sortinterfaces(rx.interface_result)
        # test eacch blade for ports
        for b in rx.blades:
            self.assertIsInstance(b, Blade)
            self.assertTrue(b.interfaces)
            # for interface in b.interfaces:
            self.assertEqual(len(b.interfaces), 16)
            portrange = range(1, 17)
            for port, interface in b.interfaces.items():
                self.assertIn(int(port), portrange)
                self.assertTrue(interface.portnumber)
                self.assertTrue(interface.blade)

        # Tests the sort_vlan_interfaces
        rx.sort_vlan_interfaces(rx.vlan_interface_result)
        self.assertEqual(184, len(rx.vlansints))
        for vl in rx.vlansints:
            self.assertIsInstance(vl, vlan)
            self.assertTrue(vl.number)
            self.assertTrue(vl.rawdata)

        # Tests the sortCdpNeiDetail
        rx.sortCdpNeiDetail(rx.cdpnei_result)
        self.assertEqual(39, len(rx.cdpneighbors))
        for n in rx.cdpneighbors:
            self.assertIsInstance(n, Neighbor)
            self.assertTrue(n.deviceid)
            self.assertTrue(n.platform)
            self.assertTrue(n.duplex)
            self.assertTrue(n.ip)
            self.assertTrue(n.interface)
            self.assertTrue(n.remote_interface)
            self.assertIsInstance(n.interface, Interface)
            self.assertIsInstance(n.remote_interface, Interface)

        # Tests the sortportcounters
        rx.sortportcounters(rx.portcount_result)
        for blade in rx.blades:
            for count, port in blade.interfaces.items():
                self.assertIsNotNone(port.InOctets)
                self.assertIsNotNone(port.InUcastPkts)
                self.assertIsNotNone(port.InBcastPkts)
                self.assertIsNotNone(port.outOctets)
                self.assertIsNotNone(port.outUcastPkts)
                self.assertIsNotNone(port.outBcastPkts)
                self.assertIsNotNone(port.outMcastPkts)
                self.assertIsNotNone(port.outBcastPkts)
                self.assertIsNotNone(port.InMcastPkts)

    def test_assignattributes_Cisco_Nexus7000(self):
        """
        """
        c = DeviceAccess(Switch_access.username, Switch_access.password)
        r_con = c.login("172.29.4.1")
        rx = Router()
        rx.getSwitchInfo(r_con)
        rx.assignattributes(r_con)
        # Tests the sortVersion
        # Tests the sortVersion
        # Tests the sortInventory
        # Tests the sortmodule
        # Tests the sortinterfaces
        # Tests the sort_vlan_interfaces
        # Tests the sortCdpNeiDetail
        # Tests the sortportcounters

    def test_assignattributes_Cisco_WSC6509E(self):
        """
        """
        c = DeviceAccess(Switch_access.username, Switch_access.password)
        r_con = c.login("172.29.4.1")
        rx = Router()
        rx.getSwitchInfo(r_con)
        rx.assignattributes(r_con)

        # Tests the sortVersion
        # Tests the sortVersion
        # Tests the sortInventory
        # Tests the sortmodule
        # Tests the sortinterfaces
        # Tests the sort_vlan_interfaces
        # Tests the sortCdpNeiDetail
        # Tests the sortportcounters

    def test_assignattributes_Cisco_C6816XLE(self):
        """
        """
        c = DeviceAccess(Switch_access.username, Switch_access.password)
        r_con = c.login("172.29.4.1")
        rx = Router()
        rx.getSwitchInfo(r_con)
        rx.assignattributes(r_con)

        # Tests the sortVersion
        # Tests the sortVersion
        # Tests the sortInventory
        # Tests the sortmodule
        # Tests the sortinterfaces
        # Tests the sort_vlan_interfaces
        # Tests the sortCdpNeiDetail
        # Tests the sortportcounters

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

class TestSwitchTransfer(unittest.TestCase):
    def test_2960_to_9300(self):
        """
        sx2-3574ddc-battery.net.utah.edu
        Model: WS-C2960-24LT-L
        Software Version:
        to
        sx2-3574ddc-battery-ebc.net.utah.edu
        Model: 9300
        Software Version: 16.6.8
        """
        Provision_Switch_from_old_switch("172.31.7.144")

class TestBuildingNetwork(unittest.TestCase):
    """
    Tests the functions in building network object
    """

    def test_collect_all_switches(self):
        """
        Logs the collection of all the correct switchs and their assignment using building 582
        """
        dx1 = Switch("172.31.7.133")
        dx1.login()
        dx1.getSwitchInfo()
        dx1.assignattributes()
        dx2 = Switch("172.31.7.134")
        dx2.login()
        dx2.getSwitchInfo()
        dx2.assignattributes()


        b582 = Building(dx1=dx1, dx2=dx2)
        b582.collect_all_switches()

        test_switches = ["172.31.7.151","172.31.7.153","172.31.7.145",
                         "172.31.7.155","172.31.7.141","172.31.7.137",
                         "172.31.7.156","172.31.7.135","172.31.7.149",
                         "172.31.7.154", "172.31.7.157", "172.31.7.150",
                         "172.31.7.159", "172.31.7.158", "172.31.7.146",
                         "172.31.7.142", "172.31.7.138", "172.31.7.136",
                         "172.31.7.147", "172.31.7.143", "172.31.7.139",
                         "172.31.7.148", "172.31.7.144", "172.31.7.140"
                         ]
        realips = []
        for switch in b582.switches:
            realips.append(str(switch.ip))
        test_switches.sort()
        realips.sort()
        self.assertEqual(test_switches,realips)

    def test_Portcountreport(self):
        dx1 = Switch("172.31.7.133")
        dx1.login()
        dx1.getSwitchInfo()
        dx1.assignattributes()
        dx1.logout(dx1.conn)
        dx2 = Switch("172.31.7.134")
        dx2.login()
        dx2.getSwitchInfo()
        dx2.assignattributes()
        dx2.logout(dx2.conn)

        b582 = Building(dx1=dx1, dx2=dx2)
        b582.collect_all_switches()
        b582.portcountreport()

        for sx in b582.sx_switches:
            singleportcount = sx.lifeCycleUpdate_interface_report()
            if sx.hostname == 'dx1-582pharm':
                self.assertEqual(40,sx.portcount)
            elif sx.hostname == 'dx1-582pharm':
                self.assertEqual(40, sx.portcount)

class TestASA(unittest.TestCase):
    def test_get_crypto_maps(self):
        asa = ASA('155.100.9.2')
        asa.connect_to_ASA()

class TestSwitchCPUUsage(unittest.TestCase):

    def test_switch_CPUUsage(self):
        switch_row = []
        switch_row.append(["IP Address", "Orion_Memory Used (bytes)", "Orion_Percent Memory Used",
                           "Switch_Memory Used (bytes)", "Switch_Percent Memory Used"])
        device_dic = {}
        future_to_ipaddress = {}
        with ThreadPoolExecutor(max_workers=20) as executor:
            with open('Cisco_memory_used_orion.csv') as csvfile:
                reader = csv.reader(csvfile,delimiter=',')
                for row in reader:
                    if '\ufeffIP Address' in row:
                        continue
                    s = Switch(row[0])
                    device_dic[row[0]] = row
                    future_to_ipaddress[executor.submit(s.sort_memoory_Usage)] = row[0]
                for future in concurrent.futures.as_completed(future_to_ipaddress):
                    sw = future_to_ipaddress[future]
                    try:
                        Ram_Percentage = future.result()
                        if Ram_Percentage:
                            switch_row.append([device_dic[sw][0], device_dic[sw][1], device_dic[sw][2], Ram_Percentage[0],Ram_Percentage[1]])
                        else:
                            switch_row.append([device_dic[sw][0], device_dic[sw][1], device_dic[sw][2], "Not sure", "Not sure"])
                    except Exception as e:
                        switch_row.append([device_dic[sw][0], device_dic[sw][1], device_dic[sw][2], "Can't Log in", "Can't Log in"])

        with open('Cisco_memory_used_orion-2.csv','w+') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            for row in switch_row:
                writer.writerow(row)

    def test_switch_CPUUsage_static_list(self):

        orion = Orion(OrionAPI.url,OrionAPI.username,OrionAPI.password)
        results = orion.get_memory_usage_batch()
        future_to_ipaddress = {}
        with ThreadPoolExecutor(max_workers=20) as executor:
            for switch in results['results']:
                s = Switch(switch['IPAddress'])
                future_to_ipaddress[executor.submit(s.sort_memoory_Usage)] = switch['IPAddress']

            for future in concurrent.futures.as_completed(future_to_ipaddress):
                sw = future_to_ipaddress[future]
                try:
                    used_memory,percent_memory = future.result()
                except Exception as e:
                    continue
                else:
                    for switch in results['results']:
                        if sw == switch['IPAddress']:
                            if used_memory and percent_memory:
                                difference  = percent_memory - switch['PercentMemoryUsed']
                                if difference == -1 or difference == 1:
                                    continue
                                elif difference >= 2:
                                    print(f"Wrong - IP:{switch['IPAddress']} Switch Reporting Higher by {difference}%")
                                elif difference <= -2:
                                    print(f"Wrong - IP:{switch['IPAddress']} Orion Reporting Higher by {difference * -1}%")
                                else:
                                    if int(switch['PercentMemoryUsed']) != int(percent_memory):
                                        print(f"Wrong - IP:{switch['IPAddress']}")
                                    else:
                                        pass

    def test_compare(self):
        with open('Cisco_memory_used_orion-2.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            with open('Cisco_memory_used_orion-3.csv', 'w+') as csvfile_3:
                writer = csv.writer(csvfile_3, delimiter=',')
                for row in reader:
                    if 'IP Address' in row:
                        continue
                    if row[4] == 'Can\'t Log in':
                        continue
                    elif row[4] == "Not sure":
                        continue
                    elif row[2] != row[4]:
                        if row[2] > row[4]:
                            dif = int(row[2]) - int(row[4])
                            if dif == 1 or dif == -1:
                                continue
                            elif dif < 3 or dif > -3 and dif < 0:
                                continue
                            else:
                                writer.writerow(row)
    def test_single_switch_snmp_response(self):
        r = {'CoreNodeID': 2398, 'LastInventory': '2019-06-12T01:06:45.9970000', 'NodeID': 2398, 'Caption': 'sx1-369ambulparking-p5.net.utah.edu', 'IPAddress': '172.31.8.186', 'SNMPLevel': 2, 'SNMPUsername': None, 'SNMPAuthType': None, 'SNMPAuthPass': None, 'SNMPEncryptType': None, 'SNMPEncryptPass': None, 'Community': '99U#u#U!x', 'CommunityReadWrite': '', 'EncryptionAlgorithm': 0, 'Username': 'SWEN__pcvNtsW0MkKEOoG51fmCvyYPwUMVn2vTSNyUHF+42fDx+cjqmYzsJ537vzUfWgr7xB+tuvryPWJMnvCqAel/SGlIKa4SkItCEhfHeExFLHC5twNU6HPbb/7btRZuzOD7owOQdls9oYKJeUICjzCoz+Y0IWgb5yw7V0VlFxR4ZU0=', 'Password': 'SWEN__BTeZFK9xtacoK+cxiDBJVR67ofkVIHsoqDyZUGlrRApCZxqj2PbGS5OVFFQAjFgxGL4wFM+RqPWqpYW5EvgDsz3M7iUK9o9OncQaYrb/xL2CUz0+CIRXeQElvK6FSZtesWEELP/S5Mqui7poJx2goxBOH4zpzU7CE/GsQr+1wH4='}
        s = Switch(r['IPAddress'])
        try:
            s.login(quick=True)
        except OSError as O:
            s.logout(s.conn)
        except:
            pass
        s.getSwitchInfo()
        s.assignattributes()
        s.check_orion_migration(r)
        s.update_orion_migration()
        o = Orion(OrionAPI.url, OrionAPI.username, OrionAPI.password)
        if any([s.orion_auth_meth_wrong, s.orion_encript_meth_wrong, s.orion_username_wrong, s.orion_version_wrong]):
            results = input("Please check Orion Credentials. Continue (Y/N)")
            # o.update_snmp(r,tablename='NCM.Nodes',columnname='CoreNodeID',columnvalue=r['CoreNodeID']
    def test_switch_snmp_response(self):

        orion = Orion(OrionAPI.url,OrionAPI.username,OrionAPI.password)
        results = orion.get_no_snmp_Response()

        for count, r in enumerate(results):
            if count == 20:
                break
            if 'fw-' in r['Caption'].lower():
                a = ASA(r['IPAddress'])
                a.login()
                a.getSwitchInfo()
                a.assignattributes()
                a.check_orion_migration()
                a.update_orion_migration()
            elif 'pf-' in r['Caption'].lower():
                continue
            elif 'sx' in r['Caption'].lower():
                s = Switch(r['IPAddress'])
                try:
                    s.login(quick=True)
                except OSError as O:
                    s.logout(s.conn)
                    continue
                except:
                    pass
                s.getSwitchInfo()
                s.assignattributes()
                s.check_orion_migration(r)
                s.update_orion_migration()
                o = Orion(OrionAPI.url, OrionAPI.username, OrionAPI.password)
                if any([s.orion_auth_meth_wrong,s.orion_encript_meth_wrong,s.orion_username_wrong,s.orion_version_wrong]):
                    results = input("Please check Orion Credentials. Continue (Y/N)")
                    # o.update_snmp(r,tablename='NCM.Nodes',columnname='CoreNodeID',columnvalue=r['CoreNodeID'])
                s.logout(s.conn)
            else:
                continue
    def test_random_switch_snmp_response(self):

        orion = Orion(OrionAPI.url,OrionAPI.username,OrionAPI.password)
        results = orion.get_no_snmp_Response()
        switches = ['sx','dx','scx','sdx']
        randomtest = random.sample(results,40)
        for i,r in enumerate(randomtest):
            if 'fw-campus' in r['Caption'].lower():
                continue
            elif 'fw-' in r['Caption'].lower():
                a = ASA(r['IPAddress'])
                a.login()
                a.getSwitchInfo()
                a.assignattributes()
                a.check_orion_migration()
                a.update_orion_migration()
            elif any([True for x in switches if x in r['Caption'].lower()]):
                s = Switch(r['IPAddress'])
                try:
                    s.login(quick=True)
                except OSError as O:
                    s.logout(s.conn)
                    continue
                except:
                    pass
                s.getSwitchInfo()
                s.assignattributes()
                s.check_orion_migration(r)
                s.update_orion_migration()
                o = Orion(OrionAPI.url, OrionAPI.username, OrionAPI.password)
                if any([s.orion_auth_meth_wrong,s.orion_encript_meth_wrong,s.orion_username_wrong,s.orion_version_wrong]):
                    results = input("Please check Orion Credentials. Continue (Y/N)")
                    # o.update_snmp(r,tablename='NCM.Nodes',columnname='CoreNodeID',columnvalue=r['CoreNodeID'])
                s.logout(s.conn)
            else:
                continue
    def test_switch_ssh_response(self):
        orion = Orion(OrionAPI.url,OrionAPI.username,OrionAPI.password)
        results = orion.get_no_ssh_Response()
        for r in results:
            s = Switch(r['IPAddress'])
        future_to_ipaddress = {}

    def test_temp(self):
        for i in range(0,255):
            print(f"permit {i} any any")

class switch_QA(unittest.TestCase):
    def test_switch_hostname(self):
        with open('Cisco_memory_used_orion.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                if '\ufeffIP Address' in row:
                    continue
                s = Switch(row[0])
                s.get_hostname()
                s.sort_hostname()

class Testpower(unittest.TestCase):
    def test_get_power(self):
        switch = Switch(ipaddress='172.31.132.10')
        switch.login()
        switch.getSwitchInfo()
        switch.assignattributes()
        switch.sort_power_inline()
    def test_get_enviroment(self):
        switch = Switch(ipaddress='172.31.132.10')
        switch.login()
        switch.getSwitchInfo()
        switch.assignattributes()
        switch.sort_enviroment()

class Testbuildingnetwork(unittest.TestCase):
    def test_migratetonewhardware(self):
        oldswitch = Switch('172.31.14.37')
        oldswitch.login()
        oldswitch.getSwitchInfo()
        oldswitch.assignattributes()
        oldswitch.logout(oldswitch.conn)
        newswitch = Switch('172.31.14.41')
        newswitch.login()
        newswitch.getSwitchInfo()
        newswitch.assignattributes()
        b = Building(dx1=None)
        b.migratetonewhardware(oldswitch,newswitch)

    def test_migrate_multiple_to_one(self):
        oldswitch = Switch('172.30.64.69')
        newswitch = Switch('172.30.64.73')
        b = Building(dx1=oldswitch)
        b.migrate_multiple_old_to_new_hardware(oldswitch,newswitch)

class testswitchthreading(unittest.TestCase):
    def test_getswitchinfo(self):
        thread_time_start = time.perf_counter()
        oldswitch = Switch('172.31.132.9')
        oldswitch.getSwitchInfo_thread()

class testlabswitches(unittest.TestCase):
    def test_log_into_console_server(self):
        s = SwitchAccess('172.31.16.41')
        conn = s.login()
        result = conn.send_command('test')
        s.logout(conn)


if __name__ == '__main__':
    unittest.main()