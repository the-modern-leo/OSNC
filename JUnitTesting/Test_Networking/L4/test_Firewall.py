import unittest
from Network.L4.firewall import PaloAlto,adddressobj,GroupObj

class TestRouter(unittest.TestCase):
    def test_CreateAddressObj(self):
        addr = adddressobj("addr_10.5.0.1","10.5.0.1/32",True)
        result = addr.Create()
        with PaloAlto(ip="10.7.17.132",pano=True) as p:
            p.SendConfigCommands(result)

        pass

    def test_CreateGroupObj(self):
        group = GroupObj("test",True)
        result = group.Create()
        with PaloAlto(ip="10.7.17.132",pano=True) as p:
            p.SendConfigCommands(result)
        pass

    def test_AssocateAddressToGroupObj(self):
        group = GroupObj("test",True)
        result = group.AddAddressObj("addr_10.5.0.1")
        with PaloAlto(ip="10.7.17.132",pano=True) as p:
            p.SendConfigCommands(result)
        pass

    def test_DeleteAddressObj(self):
        group = GroupObj("test",True)
        result = group.Delete()
        with PaloAlto(ip="10.7.17.132",pano=True) as p:
            p.SendConfigCommands(result)
        pass

---------------------Platforms-------------------------------
f"""
vrf definition {vrf_name}
 rd 65000:{vrf number}0
 route-target export 65000:{vrf number}0
 route-target import 65000:{vrf number}0
 !
 address-family ipv4
 exit-address-family
!
interface Loopback{vrf number}
 description PTP-OSPF-{vrf number}-{router_name}
 vrf forwarding {vrf_name}
 ip address 10.{Device Cidr}.24.4 255.255.255.0
!
vlan110{vrf number}
name PTP-OSPF-{vrf number}-{router_name}
!
interface Vlan110{vrf number}
 description PTP-OSPF-{vrf number}-{router_name}
 mtu {Match Physical Interface}
 vrf forwarding {vrf_name}
 ip address 10.{Device Cidr}.25.4 255.255.255.0
!
Vlan2855
name CRS-{vrf_name}
!
interface Vlan2855
 description CRS-{vrf_name}
 vrf forwarding {vrf_name}
 ip address 10.{Device Cidr}.18.130 255.255.255.128
 ip helper-address 10.2.5.150
 ip helper-address 10.2.7.150
 standby version 2
 standby 2855 ip 10.{Device Cidr}.18.129
 standby 2855 priority 1
 standby 2855 preempt
!
interface Vlan2856
 description CRS-{vrf_name}
 vrf forwarding {vrf_name}
 ip address 10.{Device Cidr}.18.130 255.255.255.128
 ip helper-address 10.2.5.150
 ip helper-address 10.2.7.150
 standby version 2
 standby 2856 ip 10.{Device Cidr}.18.129
 standby 2856 priority 1
 standby 2856 preempt
!
router ospf {vrf number} vrf {vrf_name}
 router-id 10.{Device Cidr}.24.4
 passive-interface default
 no passive-interface Vlan110{vrf number}
 network 10.{Device Cidr}.18.0 0.0.15.255 area 0.0.0.0
 network 10.{Device Cidr}.19.0 0.0.15.255 area 0.0.0.0
!
interface [To router interface]
 switchport trunk allowed vlan add 110{vrf number}
end
!
interface [To Switch interface]
 switchport trunk allowed vlan add 2855
end
"""




---------------------buildings-------------------------------
f"""
vrf definition {vrf_name}
 rd 65000:{vrf number}0
 route-target export 65000:{vrf number}0
 route-target import 65000:{vrf number}0
 !
 address-family ipv4
 exit-address-family
!
interface Loopback{vrf number}
 description PTP-OSPF-{vrf number}-{router_name}
 vrf forwarding {vrf_name}
 ip address 10.{Device Cidr}.24.4 255.255.255.0
!
vlan110{vrf number}
name PTP-OSPF-{vrf number}-{router_name}
!
interface Vlan110{vrf number}
 description PTP-OSPF-{vrf number}-{router_name}
 mtu {Match Physical Interface}
 vrf forwarding {vrf_name}
 ip address 10.{Device Cidr}.25.4 255.255.255.0
!
Vlan{switchVlan}
name CRS-{vrf_name}
!
interface Vlan{switchVlan}
 description CRS-{vrf_name}
 vrf forwarding {vrf_name}
 ip address 10.{Device Cidr}.{DeviceType}.{secondIP} 255.255.255.0
 ip helper-address 10.2.5.150
 ip helper-address 10.2.7.150
 standby version 2
 standby {switchVlan} ip 10.{Device Cidr}.{DeviceType}.{firstIP}
 standby {switchVlan} priority 1
 standby {switchVlan} preempt
!
router ospf {vrf number} vrf {vrf_name}
 router-id 10.{Device Cidr}.24.4
 passive-interface default
 no passive-interface Vlan110{vrf number}
 network 10.{Device Cidr}.{DeviceType}.0 0.0.0.255 area 0.0.0.0
!
interface [To router interface]
 switchport trunk allowed vlan add 110{vrf number}
end
!
interface [To Switch interface]
 switchport trunk allowed vlan add {switchVlan}
end
"""
