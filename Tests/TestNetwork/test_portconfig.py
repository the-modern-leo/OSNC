import unittest, re

from Tracker.mactracker import MacLocation
from portconfig import portconfig_common, vlanchanger

class FakeMacTracker(object):
    pass

class FakeConnection(object):
    def send_command(self, cmd):
        if 'show vlan brief' in cmd:
            return "10  test data net            active \n20  test-voice-vlan        active "
        elif 'configure terminal' in cmd:
            return "Enter configuration commands, one per line.  End with CNTL/Z."

class FakeSwitchAccess(object):
    def login(switch):
        return FakeConnection()

    def login_and_run(self, switch, cmd):
        fc = FakeConnection()
        return fc, fc.send_command(cmd)

    def logout(self, conn):
        pass

good_config = """Building configuration...
Current configuration : 173 bytes
!
interface GigabitEthernet1/2
 description Example edge port config
 switchport access vlan 10
 switchport mode access
 switchport voice vlan 20
 spanning-tree portfast
end"""

bad_config = """Building configuration...
Current configuration : 173 bytes
!
interface GigabitEthernet1/2
 description Example trunk interface
 switchport access vlan 10
 switchport mode trunk
 switchport trunk allowed vlan 10,11,12
 switchport voice vlan 20
 spanning-tree portfast
end"""

mab_config = """Building configuration...
Current configuration : 173 bytes
!
interface GigabitEthernet1/2
 switchport mode access
 switchport voice vlan 20
 authentication host-mode multi-domain
 authentication order mab
 authentication port-control auto
 authentication periodic
 mab
 spanning-tree portfast
end
"""

class TestPortConfigCommon(unittest.TestCase):
    def test_verify(self):
        mtr1 = {"message": None, "maclocation":
                MacLocation("switch1", "10.10.10.10", "GigabitEthernet1/2",
                None, good_config, None, None), "error": False}
        mtr2 = {"message": None, "maclocation":
                MacLocation("switch1", "10.10.10.10", None,
                'Device is not reporting its MAC to this neighbor, although it was reporting to the router. Here is the neighbor.',
                None, None, None), "error": False}
        mtr3 = {"message": None, "maclocation":
                MacLocation("switch1", "10.10.10.10", "GigabitEthernet1/2",
                'Could not find where the device is directly connected, here is the last known switch and port.',
                None, None, None), "error": False}
        mtr4 = {'message': 'logging into 10.10.10.11...', 'error': False, 'maclocation': None}
        mtr5 = {"message": None, "maclocation":
                MacLocation("switch1", "10.10.10.10", "GigabitEthernet1/2",
                None, bad_config, None, None), "error": False}
        mtr6 = {"message": None, "maclocation":
                MacLocation("switch1", "10.10.10.10", "GigabitEthernet1/2",
                None, mab_config, None, None), "error": False}
        pc = portconfig_common.PortConfigCommon()
        pc.verify_switchport(mtr1)

        with self.assertRaises(ValueError):
            # test device partially tracked, but not found
            pc.verify_switchport(mtr2)
        with self.assertRaises(ValueError):
            # generic MACTracker error message
            pc.verify_switchport(mtr3)
        with self.assertRaises(ValueError):
            # in progress message
            pc.verify_switchport(mtr4)
        with self.assertRaises(ValueError):
            # bad config, trunk port
            pc.verify_switchport(mtr5)
        # verify VLANs
        pc.verify_switchport(mtr1, verify_vlan=11)
        with self.assertRaises(ValueError):
            pc.verify_switchport(mtr1, verify_vlan=10)

        with self.assertRaises(ValueError):
            # verify 802.1x
            pc.verify_switchport(mtr6)

class TestVLANChanger(unittest.TestCase):
    def test_vlangetter(self):
        sa = FakeSwitchAccess()
        mt = FakeMacTracker()
        vc = vlanchanger.VLANChanger(sa, mt)

        with self.assertRaises(ValueError):
            vc.get_vlan_list()

        self.assertEqual(vc.get_vlan_list(switch='switch1'),
                [(10, 'test data net'), (20, 'test-voice-vlan')])
        fc = FakeConnection()
        self.assertEqual(vc.get_vlan_list(connection=fc),
                [(10, 'test data net'), (20, 'test-voice-vlan')])

    def test_vlansetter(self):
        sa = FakeSwitchAccess()
        mt = FakeMacTracker()
        vc = vlanchanger.VLANChanger(sa, mt)
        fc = FakeConnection()
        vc.configure_port_vlan('switch1', 'GigabitEthernet1/2', 11, fc)
