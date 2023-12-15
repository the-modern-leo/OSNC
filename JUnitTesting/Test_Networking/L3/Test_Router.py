import unittest

import netaddr

from Network.L3.Router import Router, VRF
from Network.L2.Vlan import vlan
import re
from netaddr import mac_cisco,IPNetwork


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
        vlans = [(1600,"CRN-tvm","10.23.0.2", "/26","10.23.0.1"),
(1601,"CRS-tvm","10.23.0.66", "/26","10.23.0.65"),
(1602,"SHSC-tvm","10.23.0.130", "/26","10.23.0.129"),
(1603,"TRXAirport-tvm","10.23.0.194", "/26","10.23.0.193"),
(1604,"TRXMJ-tvm","10.23.1.2", "/26","10.23.1.1"),
(1605,"TRXN-tvm","10.23.1.66", "/26","10.23.1.65"),
(1606,"TRXS-tvm","10.23.1.130", "/26","10.23.1.129"),
(1607,"TRXU-tvm","10.23.1.194", "/26","10.23.1.193"),
(1608,"TRXWV-tvm","10.23.2.2", "/26","10.23.2.1"),
(1609,"JRSC-TVM-Test","10.23.2.66", "/29","10.23.2.65"),
(1610,"P2P-FW-Edge","10.23.2.74", "/29","10.23.2.73")]
        vlanobjs = []
        for vl in vlans:
            v.network = IPNetwork(vl[2]+vl[3])
            v = vlan(vl[0])
            v.name = vl[1]
            v.helperip = ["10.2.5.150","10.2.7.150"]
            v.vrf = ["fuelmaster"]
            vlanobjs.append(v)
        routers = []
        flhqrouter = Router("192.168.100.201")
        flhqrouter.bgpnei = ["10.7.2.1",
                             "10.7.2.2",
                             "10.7.2.3",
                             "10.7.2.4",
                             "10.7.2.5",
                             "10.7.2.6",
                             "10.7.2.7",
                             "10.7.2.8",
                             "10.7.1.9"]
        flhqrouter.bgpInstanceNumb = 3
        routers.append(flhqrouter)

        mb3router = Router("192.168.100.201")
        mb3router.bgpnei = ["10.7.2.0",
                             "10.7.2.2",
                             "10.7.2.3",
                             "10.7.2.4",
                             "10.7.2.5",
                             "10.7.2.6",
                             "10.7.2.7",
                             "10.7.2.8",
                             "10.7.1.9"]
        flhqrouter.bgpInstanceNumb = 3
        routers.append(mb3router)
        ips = ["10.10.2.1","10.22.2.1","10.29.2.1","10.103.2.1","10.113.2.1","10.20.2.1","10.12.2.1"]
        for ip in ips:
            r = Router(ip)
            r.bgpnei = ["10.7.2.0","10.7.2.1"]
            r.bgpInstanceNumb = 3
            routers.append(r)

        v = VRF("fuelmaster","20")
        v.generate_all_vrf_configurations(routers,vlanobjs)



