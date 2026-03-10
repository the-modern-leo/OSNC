import unittest

import netaddr

from Network.L3.Router import Router, VRF, bgp, ospf
from Network.L2.Vlan import vlan
from vendors.infoblox import restapi
import re
from netaddr import mac_cisco,IPNetwork,EUI
import os


class TestRouter(unittest.TestCase):

    def test_upper(self):
        r = Router('10.59.150.173')
        r.get_started()
        self.assertEqual()

    def test_find_port_quick(self):
        r = Router("")
        r.get_started()
        mac = EUI('')
        mac.dialect = mac_cisco
        result = r.find_port_quick(mac=mac)
        print(result)

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

    def test_vrf_creation(self):
        r = restapi()
        containers = r.get_Network_containers_all("10.24.0.0/24")
        routers = []
        Hubrouters = []
        for network in containers:
            matches = re.findall(r"Vlan: ([\d]{0,5})[\s\S]Location: (.*)[\s\S]Router: (.*)[\s\S]{0,2}",network["comment"],re.MULTILINE)[0]
            v = vlan(matches[0])
            v.name = matches[1] + "-fuelmaster"
            v.network = IPNetwork(network['network'])
            v.helper_addr = [IPNetwork("10.2.5.150/32"),IPNetwork("10.2.7.150/32")]
            if "/" in matches[2]:
                name_ip = re.findall(r"([a-zA-z\d]{0,20}).*<([\d]{0,3}.[\d]{0,3}.[\d]{0,3}.[\d]{0,3}.)>.*/ ([a-zA-z\d]{0,20}).*<([\d]{0,3}.[\d]{0,3}.[\d]{0,3}.[\d]{0,3}.)>",
                                     matches[2], re.MULTILINE)[0]
                r1 = Router(name_ip[1])
                r1.vlans.append(v)
                r1.hostname = name_ip[0]
                r2 = Router(name_ip[3])
                r2.vlans.append(v)
                r2.hostname = name_ip[2]
                if "FLHQ" in r2.hostname:
                    b = bgp()
                    b.routerid = netaddr.IPNetwork("10.7.1.0/32")
                    b.loopback = "3"
                    b.ASNumber = "65000"
                    b.neighbors = [netaddr.IPNetwork("10.7.1.1/32"),
                                   netaddr.IPNetwork("10.7.1.2/32"),
                                   netaddr.IPNetwork("10.7.1.3/32"),
                                   netaddr.IPNetwork("10.7.1.4/32"),
                                   netaddr.IPNetwork("10.7.1.5/32"),
                                   netaddr.IPNetwork("10.7.1.6/32"),
                                   netaddr.IPNetwork("10.7.1.7/32"),
                                   netaddr.IPNetwork("10.7.1.8/32"),
                                   netaddr.IPNetwork("10.7.1.9/32")]
                    r2.route_protocols = b
                    o = ospf()
                    o.routerid = netaddr.IPNetwork("10.7.3.1/32")
                    o.loopback = "20"
                    o.neighbors = [netaddr.IPNetwork("10.7.3.0/32"),
                                   netaddr.IPNetwork("10.7.3.2/32"),
                                   netaddr.IPNetwork("10.7.3.3/32"),
                                   netaddr.IPNetwork("10.7.3.4/32"),
                                   netaddr.IPNetwork("10.7.3.5/32"),
                                   netaddr.IPNetwork("10.7.3.6/32"),
                                   netaddr.IPNetwork("10.7.3.7/32"),
                                   netaddr.IPNetwork("10.7.3.8/32"),
                                   netaddr.IPNetwork("10.7.3.9/32")]
                    o.networks = [netaddr.IPNetwork("10.7.0.0/16"), netaddr.IPNetwork("10.24.0.0/24")]
                    r2.ospf = o
                if "MB3" in r1.hostname:
                    b = bgp()
                    b.routerid = netaddr.IPNetwork("10.7.1.1/32")
                    b.loopback = "3"
                    b.ASNumber = "65000"
                    b.neighbors = [netaddr.IPNetwork("10.7.1.2/32"),
                                   netaddr.IPNetwork("10.7.1.3/32"),
                                   netaddr.IPNetwork("10.7.1.4/32"),
                                   netaddr.IPNetwork("10.7.1.5/32"),
                                   netaddr.IPNetwork("10.7.1.6/32"),
                                   netaddr.IPNetwork("10.7.1.7/32"),
                                   netaddr.IPNetwork("10.7.1.8/32"),
                                   netaddr.IPNetwork("10.7.1.9/32")]
                    o = ospf()
                    o.routerid = netaddr.IPNetwork("10.7.3.2/32")
                    o.loopback = "20"
                    o.neighbors = [netaddr.IPNetwork("10.7.3.0/32"),
                                   netaddr.IPNetwork("10.7.3.1/32"),
                                   netaddr.IPNetwork("10.7.3.3/32"),
                                   netaddr.IPNetwork("10.7.3.4/32"),
                                   netaddr.IPNetwork("10.7.3.5/32"),
                                   netaddr.IPNetwork("10.7.3.6/32"),
                                   netaddr.IPNetwork("10.7.3.7/32"),
                                   netaddr.IPNetwork("10.7.3.8/32"),
                                   netaddr.IPNetwork("10.7.3.9/32")]
                    o.networks = [netaddr.IPNetwork("10.7.0.0/16"),netaddr.IPNetwork("10.24.0.0/24")]
                    r1.route_protocols = b
                    r1.ospf = o
                Hubrouters.append(r1)
                Hubrouters.append(r2)
            else:
                name_ip = re.findall(
                    r"([a-zA-z\d]{0,20}).*<([\d]{0,3}.[\d]{0,3}.[\d]{0,3}.[\d]{0,3}.)>",
                    matches[2], re.MULTILINE)[0]
                b = bgp()
                b.loopback = "3"
                b.ASNumber = "65000"
                b.networks = [netaddr.IPNetwork("192.168.100.0/24"),netaddr.IPNetwork("10.7.1.0/24")]
                o = ospf()
                o.neighbors = [netaddr.IPNetwork("10.7.3.1/32"),netaddr.IPNetwork("10.7.3.2/32")]
                o.loopback = "20"
                r1 = Router(name_ip[1])
                r1.hostname = name_ip[0]
                r1.vlans.append(v)
                if "OG1" in r1.hostname:
                    b.routerid = netaddr.IPNetwork("10.7.1.2/32")
                    o.routerid = netaddr.IPNetwork("10.7.3.3/32")
                    b.neighbors = [netaddr.IPNetwork("192.168.100.241/30")]
                elif "WSA" in r1.hostname:
                    b.routerid = netaddr.IPNetwork("10.7.1.3/32")
                    o.routerid = netaddr.IPNetwork("10.7.3.4/32")
                    b.neighbors = [netaddr.IPNetwork("192.168.100.129/30"),netaddr.IPNetwork("192.168.100.29/30")]
                elif "DDTC" in r1.hostname:
                    b.routerid = netaddr.IPNetwork("10.7.1.4/32")
                    o.routerid = netaddr.IPNetwork("10.7.3.5/32")
                    b.neighbors = [netaddr.IPNetwork("192.168.100.42/30")]
                elif "RS" in r1.hostname:
                    b.routerid = netaddr.IPNetwork("10.7.1.5/32")
                    o.routerid = netaddr.IPNetwork("10.7.3.6/32")
                    b.neighbors = [netaddr.IPNetwork("192.168.100.6/30")]
                elif "MB3CI3" in r1.hostname:
                    b.routerid = netaddr.IPNetwork("10.7.1.6/32")
                    o.routerid = netaddr.IPNetwork("10.7.3.7/32")
                    b.neighbors = [netaddr.IPNetwork("192.168.100.78/30")]
                elif "MC1" in r1.hostname:
                    b.routerid = netaddr.IPNetwork("10.7.1.7/32")
                    o.routerid = netaddr.IPNetwork("10.7.3.8/32")
                    b.neighbors = [netaddr.IPNetwork("192.168.100.225/30")]
                elif "Timp" in r1.hostname:
                    b.routerid = netaddr.IPNetwork("10.7.1.8/32")
                    o.routerid = netaddr.IPNetwork("10.7.3.9/32")
                    b.neighbors = [netaddr.IPNetwork("192.168.100.149/30")]
                elif "JRSC" in r1.hostname:
                    b.routerid = netaddr.IPNetwork("10.7.1.9/32")
                    o.routerid = netaddr.IPNetwork("")
                    b.neighbors = [netaddr.IPNetwork("10.7.32.5/31"),netaddr.IPNetwork("192.168.100.101/30")]
                r1.route_protocols = b
                o.networks = [netaddr.IPNetwork("10.7.0.0/16"), netaddr.IPNetwork("10.24.0.0/24")]
                r1.ospf = o
                routers.append(r1)
        v = VRF("fuelmaster",20)
        configs = v.generate_all_vrf_configurations(routers)
        save_path = ""
        for con,r in zip(configs,routers):
            name_of_file = f"{r.hostname}-change.txt"
            completeName = os.path.join(save_path, name_of_file + ".txt")
            with open(completeName,"w") as f:
                f.write(con)

    def test_eigrp_config(self):
        info = restapi()
        networks = info.get_Network_container(netadd="10.7.34.0/24")
        flhqrouter = Router("10.10.10.10")
        flhqrouter.hostname = 'FLHQ9605'
        mb3router = Router("10.10.10.10")
        mb3router.hostname = 'MB39605'
        r2s = [flhqrouter, mb3router]
        Hubrouters = []
        for n in networks:
            matches = re.findall(r"Vlan: ([\d]{0,5})[\s\S]Location: (.*)[\s\S]Router: (.*)[\s\S]{0,2}", n["comment"],
                       re.MULTILINE)[0]
            v = vlan(matches[0])
            v.network = IPNetwork(n['network'])
            if "/" in matches[2]:
                name_ip = re.findall(r"([a-zA-z\d]{0,20}) \/ ([a-zA-z\d]{0,20}).*",
                                     matches[2], re.MULTILINE)[0]
                v.name = f"{name_ip[0]}<>{name_ip[1]}-PTP"
                for router in Hubrouters:
                    if name_ip[0] == router.hostname:
                        router.vlans.append(v)
                        break
                r1 = Router(netaddr.IPNetwork(n["network"])[0])
                r1.vlans.append(v)
                r1.hostname = name_ip[0]
                Hubrouters.append(r1)
                for router in r2s:
                    if name_ip[1] == router.hostname:
                        router.vlans.append(v)

        zrouters_configs = ""
        for router in Hubrouters:
            zrouters_configs = zrouters_configs + f"--------------------{router.hostname}----------------\n" + router.generate_vlan_config()
        FLHQ_config = r2s[0].generate_vlan_config()
        mb3_config = r2s[1].generate_vlan_config()
        pass

    def test_port_finder_ipaddress(self):
            iplist = ["10.43.14.5",
"10.43.14.6",
"10.43.14.10",
"10.43.14.11",
"10.43.14.15",
"10.43.14.16",
"10.43.14.20",
"10.43.14.21",
"10.43.14.25",
"10.43.14.26",
"10.43.14.30",
"10.43.14.31",
"10.43.14.35",
"10.43.14.36",
"10.43.14.40",
"10.43.14.41",
"10.43.14.45",
"10.43.14.46",
"10.43.14.75",
"10.43.14.76",
"10.43.14.50",
"10.43.14.51",
"10.43.14.55",
"10.43.14.56",
"10.43.14.60",
"10.43.14.61",
"10.43.14.65",
"10.43.14.66",
"10.43.14.70",
"10.43.14.71",
"10.49.14.5",
"10.49.14.6",
"10.49.14.10",
"10.49.14.11",
"10.49.14.15",
"10.49.14.16",
"10.53.14.5",
"10.53.14.6",
"10.49.14.20",
"10.49.14.21",
"10.49.14.25",
"10.49.14.26",
"10.49.14.30",
"10.49.14.31",
"10.49.14.35",
"10.49.14.41",
"10.49.14.45",
"10.49.14.46",
"10.49.14.50",
"10.49.14.51",
"10.49.14.55",
"10.49.14.56",
"10.49.14.60",
"10.49.14.61",
"10.47.14.40",
"10.47.14.41",
"10.47.14.45",
"10.47.14.46",
"10.47.14.35",
"10.47.14.36",
"10.47.14.30",
"10.47.14.31",
"10.47.14.20",
"10.47.14.21",
"10.47.14.25",
"10.47.14.26",
"10.47.14.15",
"10.47.14.16",
"10.47.14.10",
"10.47.14.11",
"10.47.14.5",
"10.47.14.6",
"10.53.14.15",
"10.53.14.16",
"10.53.14.20",
"10.53.14.21",
"10.53.14.25",
"10.53.14.26",
"10.53.14.30",
"10.53.14.31",
"10.53.14.35",
"10.53.14.36",
"10.53.14.40",
"10.53.14.41",
"10.53.14.45",
"10.53.14.46",
"10.53.14.50",
"10.53.14.51",
"10.53.14.55",
"10.53.14.56",
"10.53.14.60",
"10.53.14.61",
"10.57.14.35",
"10.57.14.36",
"10.57.14.30",
"10.57.14.31",
"10.57.14.25",
"10.57.14.26",
"10.57.14.20",
"10.57.14.21",
"10.57.14.15",
"10.57.14.16",
"10.57.14.10",
"10.57.14.11",
"10.57.14.5",
"10.57.14.6",
"10.45.14.47",
"10.45.14.48",
"10.55.14.5",
"10.55.14.6",
"10.55.14.10",
"10.55.14.11",
"10.55.14.15",
"10.55.14.16",
"10.55.14.20",
"10.55.14.21",
"10.55.14.25",
"10.55.14.26",
"10.67.14.5",
"10.67.14.10",
"10.67.14.16",
"10.67.14.18",
"10.67.14.20",
"10.67.14.22",
"10.67.14.24",
"10.67.14.26",
"10.67.14.30",
"10.67.14.32",
"10.45.14.40",
"10.45.14.41",
"10.45.14.35",
"10.45.14.36",
"10.45.14.30",
"10.45.14.31",
"10.45.14.25",
"10.45.14.26",
"10.45.14.20",
"10.45.14.21",
"10.45.14.15",
"10.45.14.16",
"10.45.14.17",
"10.45.14.18",
"10.45.14.19",
"10.45.14.10",
"10.45.14.11",
"10.45.14.45",
"10.45.14.46",
"10.59.14.45",
"10.59.14.46",
"10.59.14.47",
"10.59.14.48",
"10.59.14.5",
"10.59.14.6",
"10.59.14.10",
"10.59.14.11",
"10.59.14.15",
"10.59.14.16",
"10.59.14.20",
"10.59.14.21",
"10.59.14.25",
"10.59.14.26",
"10.59.14.30",
"10.59.14.31",
"10.59.14.35",
"10.59.14.36",
"10.59.14.40",
"10.59.14.41"]
            results = []
            r = Router("192.168.100.202")
            r.get_started()
            for ip in iplist:
                result = r.find_port(ip)
                if result:
                    results.append(f"IP address:{result[0]},interface:{str(result[1])} Mac Address: {str(result)}")
            for res in results:
                print (res)
