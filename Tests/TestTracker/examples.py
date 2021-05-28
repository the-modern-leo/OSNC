show_vlan_409 = """Building configuration...\r\n
\r\n
Current configuration : 310 bytes\r\n
!\r\n
interface Vlan409\r\n
 description remote-3712laytonortho-lan\r\n
 ip vrf forwarding CLINICAL\r\n
 ip address 155.100.44.65 255.255.255.192\r\n
 ip helper-address 155.100.144.200\r\n
 ip helper-address 155.100.69.200\r\n
 no ip redirects\r\n
 no ip unreachables\r\n
 no ip proxy-arp\r\n
 ip pim sparse-mode\r\n
 ip flow monitor NETFLOW output\r\n
end\r\n
"""

show_vlan_805 = """Building configuration...\r\n
\r\n
Current configuration : 272 bytes\r\n
!\r\n
interface Vlan805\r\n
 description remote-915davis-m\r\n
 ip address 172.20.97.17 255.255.255.240\r\n
 ip helper-address 155.97.136.200\r\n
 ip helper-address 155.101.246.200\r\n
 no ip redirects\r\n
 no ip unreachables\r\n
 no ip proxy-arp\r\n
 ip pim sparse-mode\r\n
 ip flow monitor NETFLOW output\r\n
end\r\n
"""

invalid = """Translating "vlan"\r\n
^\r\n
% Invalid input detected at '^' marker.\r\n
"""

arp = "Internet  155.100.44.74          17   0007.4d8b.6216  ARPA   Vlan409\r\n"

mac_router = '*      409 0007.4d8b.6216  dynamic  Yes      130     Te2/5'

mac_switch = " 409    0007.4d8b.6216    DYNAMIC     Gi1/0/24"

name = "\r\nr1-remote#"

not_enabled = "% LLDP is not enabled\r\n"

cdp_router = """-------------------------
Device ID: dx1-3712layton-remote.net.utah.edu\r\n
Entry address(es):\r\n
  IP address: 172.20.97.5\r\n
Platform: cisco C9300-48U,  Capabilities: Switch IGMP\r\n
Interface: TenGigabitEthernet2/5,  Port ID (outgoing port): TenGigabitEthernet1/1/1\r\n
Holdtime : 158 sec\r\n
\r\n
Version :\r\n
Cisco IOS Software [Fuji], Catalyst L3 Switch Software (CAT9K_IOSXE), Version 16.8.1a, RELEASE SOFTWARE (fc1)\r\n
Technical Support: http://www.cisco.com/techsupport\r\n
Copyright (c) 1986-2018 by Cisco Systems, Inc.\r\n
Compiled Tue 03-Apr-18 18:49 by mcpre\r\n
\r\n
advertisement version: 2\r\n
VTP Management Domain: 'vtp-3712layton'\r\n
Native VLAN: 1\r\n
Duplex: full\r\n
Management address(es):\r\n
  IP address: 172.20.97.5\r\n
\r\n
\r\n
Total cdp entries displayed : 1\r\ns
"""

switch_port = """Building configuration...\r\n
\r\n
Current configuration : 115 bytes\r\n
!\r\n
interface GigabitEthernet1/0/24\r\n
 switchport access vlan 409\r\n
 switchport mode access\r\n
 spanning-tree portfast\r\n
end\r\n
"""

switch_cdp = """Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge\r\n
\r\n
                  S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone,\r\n
                  D - Remote, C - CVTA, M - Two-port Mac Relay\r\n
\r\n
Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID\r\n
\r\n
Total cdp entries displayed : 0\r\n"""

interface = """Name: Gi1/0/24\r\n
Switchport: Enabled\r\n
Administrative Mode: static access\r\n
Operational Mode: static access\r\n
Administrative Trunking Encapsulation: dot1q\r\n
Operational Trunking Encapsulation: native\r\n
Negotiation of Trunking: Off\r\n
Access Mode VLAN: 409 (remote-3712laytonortho-lan)\r\n
Trunking Native Mode VLAN: 1 (default)\r\n
Administrative Native VLAN tagging: disabled\r\n
Voice VLAN: none\r\n
Operational private-vlan: none\r\n
Trunking VLANs Enabled: ALL\r\n
Pruning VLANs Enabled: 2-1001\r\n
Capture Mode Disabled\r\n
Capture VLANs Allowed: ALL\r\n
\r\n
Protected: false\r\n
Unknown unicast blocked: disabled\r\n
Unknown multicast blocked: disabled\r\n
Vepa Enabled: false\r\n
Appliance trust: none"""