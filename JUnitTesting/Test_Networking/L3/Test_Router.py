import unittest
from Network.L3.Router import Router, VRF
import re
from netaddr import mac_cisco


class TestRouter(unittest.TestCase):

    def test_upper(self):
        r = Router('10.59.150.173')
        r.get_started()
        self.assertEqual()

    def test_find_port_quick(self):
        r = Router("192.168.100.178")
        r.get_started()
        aprs = []
        all_ports = []
        for arp in r.arps:
            third_octet = re.findall(r"[\d]{0,3}.[\d]{0,3}.([\d]{0,3}).[\d]{0,3}", arp.ip)
            for octet in third_octet:
                if "14" in octet:
                    aprs.append(arp)
                    break
        for arp in aprs:
            port = r.find_port_quick(mac=arp.mac)
            all_ports.append(port)
        for ports in all_ports:
            mac = ports[2]
            mac.dialect = mac_cisco
            print(f"IP address:{ports[0]},interface:{str(ports[1])}, Mac Address: {str(mac)}")

    def test_port_finder(self):
        r = Router("192.168.100.202")
        r.get_started()
        aprs = []
        all_ports = []
        for arp in r.arps:
            third_octet = re.findall(r"[\d]{0,3}.[\d]{0,3}.([\d]{0,3}).[\d]{0,3}",arp.ip)
            for octet in third_octet:
                if "14" in octet:
                    aprs.append(arp)
                    break
        for arp in aprs:
            port = r.find_port(mac=arp.mac)
            all_ports.append(port)
        for ports in all_ports:
            mac = ports[1].interface.mac_addresses[0]
            mac.dialect = mac_cisco
            print(f"IP address:{ports[0]},interface:{str(ports[1])} Mac Address: {str(mac)}")

    def test_generate_vrf_configuration(self):
        v = VRF()
        v.generate_Vrf_configuration()

