import unittest, re
from Tests.TestTracker import examples
from Tracker import mactracker

class TestSwitchAccess(object):
    def __init__(self):
        self.routerlist = {'ios': ['r1-clinical', 'r2-clinical'], 'nexus': ['r1-remote', 'r2-remote']}

    def get_routerlist(self):
        return self.routerlist

    def login(self, switchname):
        connection = TestConnection()
        return TestConnection

    def login_and_run(self, switchname, command):
        connection = TestConnection()
        result = connection.send_command(command)
        return connection, result

    def logout(self, connection):
        return

class TestConnection(object):
    def send_command(self, command, trim=True):
        if command == '\n':
            return examples.name
        elif command == 'show run int vlan 409':
            return examples.show_vlan_409
        elif command == 'show ip arp vlan 409 vrf CLINICAL | inc 0007.4d8b.6216':
            return examples.invalid
        elif command == 'show ip arp vrf CLINICAL vlan 409 | inc 0007.4d8b.6216':
            return examples.arp
        elif command == 'show mac address-table address 0007.4d8b.6216 | include 0007.4d8b.6216':
            return examples.mac_router
        elif command == 'show mac address-table address 0007.4d8b.6216dx | include 0007.4d8b.6216dx':
            return examples.mac_switch
        elif command == 'show lldp neighbor Te2/5 detail':
            return examples.not_enabled
        elif command == 'show cdp neighbor int Te2/5 detail':
            return examples.cdp_router
        elif command == 'show lldp neighbor Gi1/0/24 detail':
            return examples.invalid
        elif command == 'show cdp neighbor int Gi1/0/24 detail':
            return examples.invalid
        elif command == 'show cdp neighbor Gi1/0/24 detail':
            return examples.switch_cdp
        elif 'switchport' in command:
            return examples.interface
        elif 'show run int Gi1/0/24' == command:
            return examples.switch_port



class TestMacTracker(unittest.TestCase):
    def test_constructor(self):
        sa = TestSwitchAccess()
        obj = mactracker.MacFinder(sa, None)
        self.assertTrue(isinstance(obj, mactracker.MacFinder))

    def test_regex_finds_ips(self):
        sa = TestSwitchAccess()
        obj = mactracker.MacFinder(sa, None)
        ip_string = "10.104.225.207"
        not_ip = "500.20.256.2"
        self.assertTrue(obj.ip_pattern.match(ip_string))
        self.assertIsNone(obj.ip_pattern.match(not_ip))

    def test_routerlist_only_grabs_r1(self):
        sa = TestSwitchAccess()
        obj = mactracker.MacFinder(sa, None)
        correct = ['r1-clinical', 'r1-remote']
        self.assertTrue(obj.routerlist, correct)

    def test_format_mac_correctly(self):
        sa = TestSwitchAccess()
        obj = mactracker.MacFinder(sa, None)
        test1 = "34:EF:A2:45:3A:4C"
        answer1 = "34ef.a245.3a4c"
        test2 = "3967ef3906ca"
        answer2 = "3967.ef39.06ca"
        test3 = "2892.aefd.ab28"
        self.assertEqual(obj.parse_mac(test1), answer1)
        self.assertEqual(obj.parse_mac(test2), answer2)
        self.assertEqual(obj.parse_mac(test3), test3)

    def test_mac_rejects_invalid_ones(self):
        sa = TestSwitchAccess()
        obj = mactracker.MacFinder(sa, None)
        test1 = "ov02.3jb3.2lk9"
        test2 = "no associated mac"
        self.assertRaises(SyntaxError, obj.parse_mac, test1)
        self.assertRaises(SyntaxError, obj.parse_mac, test2)

    def test_find_name(self):
        sa = TestSwitchAccess()
        obj = mactracker.MacFinder(sa, None)
        correct = "r1-remote"
        connection =TestConnection()
        self.assertEqual(obj.get_switch_name(connection)[0], correct)

    def test_find_ip(self):
        sa = TestSwitchAccess()
        obj = mactracker.MacFinder(sa, None)
        connection = TestConnection()
        ip_result = obj.find_ip(connection, examples.mac_router, '0007.4d8b.6216')
        self.assertEqual(ip_result, '155.100.44.74')

    def test_search_switch_for_router(self):
        sa = TestSwitchAccess()
        obj = mactracker.MacFinder(sa, None)
        result = obj.search_switch('0007.4d8b.6216', 'r1-remote', None)
        self.assertEqual(result[0], '172.20.97.5')
        self.assertEqual(result[1], '155.100.44.74')

    def test_search_switch_for_switch(self):
        """
        I added dx to the mac to differentiate it from the router searches
        in the TestConnection class
        """
        sa = TestSwitchAccess()
        obj = mactracker.MacFinder(sa, None)
        maclocation = obj.search_switch('0007.4d8b.6216dx', 'dx1-3712layton', '172.20.97.5')
        correct = mactracker.MacLocation('r1-remote', 'dx1-3712layton', 'Gi1/0/24', None, examples.switch_port,
                '\n'.join([l for l in examples.interface.splitlines() if not l.startswith("Administrative private-vlan")]),
                '172.20.97.5')
        self.assertEqual(maclocation, correct)

if __name__ == '__main__':
    unittest.main()
