ip_address = '155.97.126.101'
software = 'software'
hardware = 'hardware'
read_results = {
 'show version':"""Cisco IOS Software, C3560E Software (C3560E-UNIVERSALK9-M), Version 12.2(55)SE3, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2011 by Cisco Systems, Inc.
Compiled Thu 05-May-11 15:57 by prod_rel_team
Image text-base: 0x00003000, data-base: 0x02800000

ROM: Bootstrap program is C3560E boot loader
BOOTLDR: C3560E Boot Loader (C3560X-HBOOT-M) Version 12.2(53r)SE2, RELEASE SOFTWARE (fc1)

sx1-029fieldhouse-hightemp uptime is 3 years, 6 weeks, 5 days, 7 hours, 6 minutes
System returned to ROM by power-on
System restarted at 10:23:15 MDT Thu May 10 2018
System image file is "flash:/c3560e-universalk9-mz.122-55.SE3/c3560e-universalk9-mz.122-55.SE3.bin"


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

License Level: lanbase
License Type: Permanent
Next reload license Level: lanbase

cisco WS-C3560X-24P (PowerPC405) processor (revision A0) with 262144K bytes of memory.
Processor board ID FDO1522P0KU
Last reset from power-on
3 Virtual Ethernet interfaces
1 FastEthernet interface
28 Gigabit Ethernet interfaces
2 Ten Gigabit Ethernet interfaces
The password-recovery mechanism is enabled.

512K bytes of flash-simulated non-volatile configuration memory.
Base ethernet MAC Address       : 00:07:7D:EE:88:80
Motherboard assembly number     : 73-12555-05
Motherboard serial number       : FDO15221MMP
Model revision number           : A0
Motherboard revision number     : C0
Model number                    : WS-C3560X-24P-L
Daughterboard assembly number   : 800-32786-01
Daughterboard serial number     : FDO15221QDE
System serial number            : FDO1522P0KU
Top Assembly Part Number        : 800-31329-02
Top Assembly Revision Number    : C0
Version ID                      : V02
CLEI Code Number                : COMJS00ARB
Hardware Board Revision Number  : 0x03

          
Switch Ports Model              SW Version            SW Image                 
------ ----- -----              ----------            ----------               
*    1 30    WS-C3560X-24P      12.2(55)SE3           C3560E-UNIVERSALK9-M     


Configuration register is 0xF
""",
 'show run':"""Building configuration...

Current configuration : 14064 bytes
!
! Last configuration change at 11:44:01 MDT Mon Apr 26 2021 by noc-orionncm
! NVRAM config last updated at 21:26:18 MDT Sun Jun 20 2021 by noc-orionncm
!
version 12.2
no service pad
service timestamps debug datetime msec localtime
service timestamps log datetime msec localtime
service password-encryption
!
hostname sx1-029fieldhouse-hightemp
!
boot-start-marker
boot-end-marker
!
vrf definition Mgmt-vrf
 !
 address-family ipv4
 exit-address-family
!
logging buffered notifications
logging console critical
enable secret 5 $1$LZ1X$/t7/MbpwgfMwd/YxLCAtQ1
!
!
!
aaa new-model
!
!
aaa authentication login default group tacacs+ enable
aaa authentication login console line enable
aaa authentication enable default group tacacs+ enable
aaa authorization exec default group tacacs+ 
aaa authorization commands 0 default group tacacs+ 
aaa authorization commands 1 default group tacacs+ 
aaa authorization commands 15 default group tacacs+ 
aaa accounting exec default start-stop group tacacs+
aaa accounting commands 1 default stop-only group tacacs+
aaa accounting commands 15 default stop-only group tacacs+
aaa accounting connection default start-stop group tacacs+
aaa accounting system default start-stop group tacacs+
!
!
!
aaa session-id common
clock timezone MST -7
clock summer-time MDT recurring
system mtu routing 1500
authentication mac-move permit
no ip source-route
!
!
ip dhcp snooping
ip domain-name net.utah.edu
ip name-server 172.20.120.20
ip device tracking
vtp domain vtp-029fldh
          vtp mode transparent
udld aggressive

!
!
crypto pki trustpoint TP-self-signed-2112784512
 enrollment selfsigned
 subject-name cn=IOS-Self-Signed-Certificate-2112784512
 revocation-check none
 rsakeypair TP-self-signed-2112784512
!
!
crypto pki certificate chain TP-self-signed-2112784512
 certificate self-signed 01
  30820257 308201C0 A0030201 02020101 300D0609 2A864886 F70D0101 04050030 
  31312F30 2D060355 04031326 494F532D 53656C66 2D536967 6E65642D 43657274 
  69666963 6174652D 32313132 37383435 3132301E 170D3933 30333031 30303031 
  31345A17 0D323030 31303130 30303030 305A3031 312F302D 06035504 03132649 
  4F532D53 656C662D 5369676E 65642D43 65727469 66696361 74652D32 31313237 
  38343531 3230819F 300D0609 2A864886 F70D0101 01050003 818D0030 81890281 
  8100D314 F3F286E7 E32BAFAE 98EB26D9 FC933745 F4DD6CE7 5FCA77BA A4F81174 
  F137A9BD 0071B1D8 BBE82429 D18B4688 5C95BF86 A429377E 42FA925E FE234E72 
  8DCE9609 CAAECA69 1F30FADC D4775ACB D12CAC4A 78C37136 565A3097 4C116553 
  1BABA12F E2C01439 6926A54C 02C6EF7B 28E09421 FEFEBDA0 2B676F15 D2054FD1 
  17630203 010001A3 7F307D30 0F060355 1D130101 FF040530 030101FF 302A0603 
  551D1104 23302182 1F647831 2D363338 50582D31 30642D66 6F72742E 6E65742E 
  75746168 2E656475 301F0603 551D2304 18301680 1497F5B7 6A5614F3 8692184B 
  919C3A99 44DEA792 13301D06 03551D0E 04160414 97F5B76A 5614F386 92184B91 
  9C3A9944 DEA79213 300D0609 2A864886 F70D0101 04050003 8181005C 3A034F1A 
  06048E57 AAA82C5F 5AB37510 B85E27F7 A59659FA 24CA0F39 E4C01464 7630725A 
  2647416F B3397101 FB181150 94B0393A FE3B735B 89FF5EAA 080A2887 FB895522 
  9C93B348 833F5FC5 FE8D40A6 2EB6991F CDC2FA09 83BA6786 7D2FF9AB FF951412 
  C5625C64 86E1041C 6955BBCF C09FECFC F56BCD47 4BEA4E66 D60DB5
  quit
!
spanning-tree mode rapid-pvst
no spanning-tree optimize bpdu transmission
spanning-tree extend system-id
!
!
!
!
vlan internal allocation policy ascending
!
vlan 419
 name lib-029fhouse-wireless
!
vlan 636
 name lib-029fieldhouse303-fm
!
vlan 656
 name lib-029fieldhouse-fm
!
vlan 694
 name lib-029field-utility-metering-fm
!
vlan 751
 name lib-029fieldhouse-ehs
!
          vlan 802
 name lib-029fldh-m
!
vlan 1208
 name lib-029fldh-fm-scada
!
vlan 2100
 name Vendor-0029FieldH-DigitalSign
!
ip ssh version 2
lldp run
!
!
interface FastEthernet0
 no ip address
 shutdown
!
interface GigabitEthernet0/1
 description #AP
 switchport access vlan 419
 switchport mode access
!
interface GigabitEthernet0/2
 switchport access vlan 694
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet0/3
 switchport access vlan 636
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet0/4
 switchport access vlan 694
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet0/5
 switchport access vlan 694
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet0/6
 switchport access vlan 694
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet0/7
 switchport access vlan 694
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet0/8
 switchport access vlan 694
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet0/9
 switchport access vlan 694
           switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet0/10
 switchport access vlan 694
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet0/11
 switchport access vlan 751
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet0/12
 switchport access vlan 751
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet0/13
 switchport access vlan 751
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet0/14
 switchport access vlan 751
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet0/15
 switchport mode access
 switchport voice vlan 201
 spanning-tree portfast
!
interface GigabitEthernet0/16
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet0/17
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet0/18
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet0/19
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet0/20
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet0/21
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet0/22
 switchport mode access
           switchport voice vlan 201
 spanning-tree portfast
!
interface GigabitEthernet0/23
 description fm-scada
 switchport access vlan 1208
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet0/24
 description fm-scada
 switchport access vlan 1208
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/1
 description key:G1/1:dx1-029field-lib:Te1/1/3
 switchport trunk encapsulation dot1q
 switchport mode trunk
 ip dhcp snooping trust
!
interface GigabitEthernet1/2
 description key:sx1-029field-sign-lib:g0/12
 switchport trunk encapsulation dot1q
 switchport trunk allowed vlan 419,802,2100
 switchport mode trunk
!
interface GigabitEthernet1/3
 switchport trunk encapsulation dot1q
 switchport trunk allowed vlan 162,163,210,620,802
 switchport mode trunk
!
interface GigabitEthernet1/4
 switchport trunk encapsulation dot1q
 switchport trunk allowed vlan 162,163,210,620,877
 switchport mode trunk
!
interface TenGigabitEthernet1/1
!
interface TenGigabitEthernet1/2
!
interface Vlan1
 no ip address
 no ip route-cache
 shutdown
!
interface Vlan802
 ip address 155.97.126.101 255.255.255.248
!
interface Vlan837
 no ip address
!
ip default-gateway 155.97.126.97
no ip http server
no ip http secure-server
ip sla enable reaction-alerts
logging facility local6
logging source-interface Vlan802
logging 155.98.253.244
          logging 155.98.204.52
logging host 172.24.29.65 transport udp port 5140
logging 172.24.29.14
logging 10.70.24.10
access-list 70 remark == Update 4-26-2021
access-list 70 remark ======= NOC SNMP RO =======
access-list 70 permit 10.64.2.70
access-list 70 permit 10.71.25.65
access-list 70 permit 155.100.126.163
access-list 70 permit 155.100.126.162
access-list 70 permit 10.71.24.21
access-list 70 permit 10.71.24.20
access-list 70 permit 10.71.24.23
access-list 70 permit 10.71.24.22
access-list 70 permit 10.71.24.17
access-list 70 permit 10.71.24.16
access-list 70 permit 10.71.24.19
access-list 70 permit 10.71.24.18
access-list 70 permit 172.20.150.100
access-list 70 permit 10.71.24.25
access-list 70 permit 10.71.24.13
access-list 70 permit 10.71.24.12
access-list 70 permit 10.71.24.15
access-list 70 permit 10.71.24.14
access-list 70 permit 10.71.24.11
access-list 70 permit 155.100.123.72
access-list 70 permit 10.71.25.164
access-list 70 permit 155.98.164.192 0.0.0.31
access-list 70 permit 155.99.254.128 0.0.0.127
access-list 70 permit 155.98.253.0 0.0.0.255
access-list 70 deny   any log
access-list 71 remark == Update 4-26-2021
access-list 71 remark ======= NOC SNMP RW =======
access-list 71 permit 10.64.2.70
access-list 71 permit 10.71.25.65
access-list 71 permit 155.100.126.163
access-list 71 permit 155.100.126.162
access-list 71 permit 10.71.24.21
access-list 71 permit 10.71.24.20
access-list 71 permit 10.71.24.23
access-list 71 permit 10.71.24.22
access-list 71 permit 10.71.24.17
access-list 71 permit 10.71.24.16
access-list 71 permit 10.71.24.19
access-list 71 permit 10.71.24.18
access-list 71 permit 172.20.150.100
access-list 71 permit 10.71.24.25
access-list 71 permit 10.71.24.13
access-list 71 permit 10.71.24.12
access-list 71 permit 10.71.24.15
access-list 71 permit 10.71.24.14
access-list 71 permit 10.71.24.11
access-list 71 permit 155.100.123.72
access-list 71 permit 10.71.25.164
access-list 71 permit 155.98.164.192 0.0.0.31
access-list 71 permit 155.99.254.128 0.0.0.127
access-list 71 permit 155.98.253.0 0.0.0.255
access-list 71 deny   any log
access-list 101 deny   udp any any eq 135
          access-list 101 deny   udp any any eq 136
access-list 101 deny   udp any any eq netbios-ns
access-list 101 deny   udp any any eq netbios-dgm
access-list 101 deny   tcp any any eq 139
access-list 101 deny   tcp any any eq 445
access-list 101 deny   udp any any eq 445
access-list 101 deny   udp any any eq bootpc
access-list 101 permit ip any any
access-list 199 remark == Update 4-26-2021 ==
access-list 199 remark ====== line VTY 0-15 inbound =====
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
access-list 199 permit tcp 155.98.164.192 0.0.0.31 any eq 22
access-list 199 remark -----New Orion Address-----------
access-list 199 permit tcp host 10.71.24.11 any eq 22
access-list 199 permit tcp host 10.71.24.12 any eq 22
access-list 199 permit tcp host 10.71.24.13 any eq 22
access-list 199 permit tcp host 10.71.24.14 any eq 22
access-list 199 permit tcp host 10.71.24.15 any eq 22
access-list 199 permit tcp host 10.71.24.16 any eq 22
access-list 199 permit tcp host 10.71.24.17 any eq 22
access-list 199 permit tcp host 10.71.24.18 any eq 22
access-list 199 permit tcp host 10.71.24.19 any eq 22
access-list 199 permit tcp host 10.71.24.20 any eq 22
access-list 199 permit tcp host 10.71.24.21 any eq 22
access-list 199 permit tcp host 10.71.24.22 any eq 22
access-list 199 permit tcp host 10.71.24.23 any eq 22
access-list 199 permit tcp host 10.71.24.25 any eq 22
access-list 199 permit tcp host 10.71.25.65 any eq 22
access-list 199 permit tcp host 10.71.25.164 any eq 22
access-list 199 deny   ip any any log
snmp-server engineID local 000000090200000628362780
snmp-server group NOCGrv3RO v3 priv read NOCViewRO access 70
snmp-server group NOCGrv3RO v3 auth context vlan- match prefix 
snmp-server group NOCGrv3RW v3 priv write NOCViewRW access 71
snmp-server view NOCViewRO internet included
snmp-server view NOCViewRW internet included
snmp-server community We5U=#9vahev RW 71
snmp-server community fortNs!$q~5r9 RW 71
snmp-server community fort$NmP! RO 70
snmp-server community 99U#u#U!x RO 70
snmp-server community 1xR$bluE RO 73
snmp-server community cl3an RW 71
snmp-server community Yx5XdagKRsmD3Oi RO 70
snmp-server location Bldg. 029 Room hightemp
snmp-server contact BC-503691 Y-040806
snmp-server enable traps snmp authentication linkdown linkup coldstart warmstart
          snmp-server enable traps tty
snmp-server enable traps config
snmp-server enable traps stpx root-inconsistency loop-inconsistency
snmp-server enable traps vlancreate
snmp-server enable traps vlandelete
snmp-server enable traps envmon fan shutdown supply temperature status
snmp-server host 155.98.253.152 version 2c 99U#u#U!x 
snmp-server host 155.98.253.148 v2c 
snmp-server host 155.98.253.149 v2c 
snmp ifmib ifindex persist
tacacs-server host 172.31.17.180
tacacs-server host 10.64.32.5
tacacs-server directed-request
tacacs-server key 7 032D1F0E2F4B246E6E0B0044
!
no vstack
banner login ^C
sx1-029fldh-hightemp-lib
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
privilege exec level 1 show
!
line con 0
 exec-timeout 15 0
 password 7 046E1F0707230D1D5D
 login authentication console
 stopbits 1
line vty 0 4
 access-class 199 in
 exec-timeout 30 0
 password 7 09795A08110756415F
 transport input ssh
line vty 5 15
 access-class 199 in
 exec-timeout 30 0
 password 7 09795A08110756415F
 transport input ssh
!
ntp clock-period 36027456
ntp server 155.97.159.10
end
""",
 'show int status':"""Port      Name               Status       Vlan       Duplex  Speed Type
Gi0/1     #AP                connected    419        a-full a-1000 10/100/1000BaseTX
Gi0/2                        connected    694        a-full  a-100 10/100/1000BaseTX
Gi0/3                        connected    636        a-half   a-10 10/100/1000BaseTX
Gi0/4                        notconnect   694          auto   auto 10/100/1000BaseTX
Gi0/5                        notconnect   694          auto   auto 10/100/1000BaseTX
Gi0/6                        notconnect   694          auto   auto 10/100/1000BaseTX
Gi0/7                        notconnect   694          auto   auto 10/100/1000BaseTX
Gi0/8                        notconnect   694          auto   auto 10/100/1000BaseTX
Gi0/9                        notconnect   694          auto   auto 10/100/1000BaseTX
Gi0/10                       notconnect   694          auto   auto 10/100/1000BaseTX
Gi0/11                       notconnect   751          auto   auto 10/100/1000BaseTX
Gi0/12                       connected    751        a-full  a-100 10/100/1000BaseTX
Gi0/13                       connected    751        a-full  a-100 10/100/1000BaseTX
Gi0/14                       connected    751        a-full  a-100 10/100/1000BaseTX
Gi0/15                       notconnect   1            auto   auto 10/100/1000BaseTX
Gi0/16                       notconnect   1            auto   auto 10/100/1000BaseTX
Gi0/17                       notconnect   1            auto   auto 10/100/1000BaseTX
Gi0/18                       notconnect   1            auto   auto 10/100/1000BaseTX
Gi0/19                       notconnect   1            auto   auto 10/100/1000BaseTX
Gi0/20                       notconnect   1            auto   auto 10/100/1000BaseTX
Gi0/21                       notconnect   1            auto   auto 10/100/1000BaseTX
Gi0/22                       notconnect   1            auto   auto 10/100/1000BaseTX
Gi0/23    fm-scada           notconnect   1208         auto   auto 10/100/1000BaseTX
Gi0/24    fm-scada           notconnect   1208         auto   auto 10/100/1000BaseTX
Gi1/1     key:G1/1:dx1-029fi connected    trunk      a-full a-1000 1000BaseLX SFP
Gi1/2     key:sx1-029field-s connected    trunk      a-full a-1000 1000BaseLX SFP
Gi1/3                        notconnect   1            auto   auto 1000BaseLX SFP
Gi1/4                        notconnect   1            auto   auto Not Present
Fa0                          disabled     routed       auto   auto 10/100BaseTX""",
 'show run | section interface':"""^
% Invalid input detected at '^' marker.
""",
 'show run | in interface':"""interface FastEthernet0
interface GigabitEthernet0/1
interface GigabitEthernet0/2
interface GigabitEthernet0/3
interface GigabitEthernet0/4
interface GigabitEthernet0/5
interface GigabitEthernet0/6
interface GigabitEthernet0/7
interface GigabitEthernet0/8
interface GigabitEthernet0/9
interface GigabitEthernet0/10
interface GigabitEthernet0/11
interface GigabitEthernet0/12
interface GigabitEthernet0/13
interface GigabitEthernet0/14
interface GigabitEthernet0/15
interface GigabitEthernet0/16
interface GigabitEthernet0/17
interface GigabitEthernet0/18
interface GigabitEthernet0/19
interface GigabitEthernet0/20
interface GigabitEthernet0/21
interface GigabitEthernet0/22
interface GigabitEthernet0/23
interface GigabitEthernet0/24
interface GigabitEthernet1/1
interface GigabitEthernet1/2
interface GigabitEthernet1/3
interface GigabitEthernet1/4
interface TenGigabitEthernet1/1
interface TenGigabitEthernet1/2
interface Vlan1
interface Vlan802
interface Vlan837
logging source-interface Vlan802""",
 'show interface link':"""^
% Invalid input detected at '^' marker.
""",
 'show interface':"""Vlan1 is administratively down, line protocol is down 
  Hardware is EtherSVI, address is 0007.7dee.88c0 (bia 0007.7dee.88c0)
  MTU 1500 bytes, BW 1000000 Kbit, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     51919579 packets input, 3115174740 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 1 interface resets
     0 output buffer failures, 0 output buffers swapped out
Vlan802 is up, line protocol is up 
  Hardware is EtherSVI, address is 0007.7dee.88c1 (bia 0007.7dee.88c1)
  Internet address is 155.97.126.101/29
  MTU 1500 bytes, BW 1000000 Kbit, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output 00:00:00, output hang never
  Last clearing of "" counters never
  Input queue: 1/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 2000 bits/sec, 2 packets/sec
  5 minute output rate 2000 bits/sec, 1 packets/sec
     119248377 packets input, 15851004833 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     51196774 packets output, 14051637755 bytes, 0 underruns
     0 output errors, 2 interface resets
     0 output buffer failures, 0 output buffers swapped out
Vlan837 is down, line protocol is down 
  Hardware is EtherSVI, address is 0007.7dee.88c2 (bia 0007.7dee.88c2)
  MTU 1500 bytes, BW 1000000 Kbit, DLY 10 usec, 
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
     0 output errors, 0 interface resets
     0 output buffer failures, 0 output buffers swapped out
FastEthernet0 is administratively down, line protocol is down 
  Hardware is PowerPC405 FastEthernet, address is 0007.7dee.88b7 (bia 0007.7dee.88b7)
  MTU 1500 bytes, BW 100000 Kbit, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not set
  Unknown duplex, Unknown Speed, MII
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/0 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet0/1 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 0007.7dee.8881 (bia 0007.7dee.8881)
  Description: #AP
  MTU 1500 bytes, BW 1000000 Kbit, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:19, output 00:00:00, output hang never
  Last clearing of "" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 6000 bits/sec, 5 packets/sec
  5 minute output rate 9000 bits/sec, 5 packets/sec
     978136785 packets input, 275994064832 bytes, 0 no buffer
     Received 5764922 broadcasts (5708853 multicasts)
     0 runts, 0 giants, 0 throttles
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 5708853 multicast, 0 pause input
     0 input packets with dribble condition detected
     1358997825 packets output, 1244017191836 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 PAUSE output
     0 output buffer failures, 0 output buffers swapped out
          GigabitEthernet0/2 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 0007.7dee.8882 (bia 0007.7dee.8882)
  MTU 1500 bytes, BW 100000 Kbit, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 00:00:00, output hang never
  Last clearing of "" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 16000 bits/sec, 6 packets/sec
  5 minute output rate 4000 bits/sec, 7 packets/sec
     560628146 packets input, 135574148168 bytes, 0 no buffer
     Received 111886 broadcasts (197 multicasts)
     0 runts, 0 giants, 0 throttles
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 197 multicast, 0 pause input
     0 input packets with dribble condition detected
     729942745 packets output, 74295998109 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 PAUSE output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet0/3 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 0007.7dee.8883 (bia 0007.7dee.8883)
  MTU 1500 bytes, BW 10000 Kbit, DLY 1000 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Half-duplex, 10Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 00:00:00, output hang never
  Last clearing of "" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 7000 bits/sec, 11 packets/sec
     3649418 packets input, 597362203 bytes, 0 no buffer
     Received 474603 broadcasts (0 multicasts)
     0 runts, 1 giants, 0 throttles
     1 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     778729577 packets output, 61532963699 bytes, 0 underruns
     0 output errors, 9049 collisions, 2 interface resets
     0 babbles, 27841 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 PAUSE output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet0/4 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 0007.7dee.8884 (bia 0007.7dee.8884)
  MTU 1500 bytes, BW 10000 Kbit, DLY 1000 usec, 
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
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 PAUSE output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet0/5 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 0007.7dee.8885 (bia 0007.7dee.8885)
  MTU 1500 bytes, BW 10000 Kbit, DLY 1000 usec, 
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
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 PAUSE output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet0/6 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 0007.7dee.8886 (bia 0007.7dee.8886)
  MTU 1500 bytes, BW 10000 Kbit, DLY 1000 usec, 
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
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 PAUSE output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet0/7 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 0007.7dee.8887 (bia 0007.7dee.8887)
  MTU 1500 bytes, BW 10000 Kbit, DLY 1000 usec, 
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
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 PAUSE output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet0/8 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 0007.7dee.8888 (bia 0007.7dee.8888)
  MTU 1500 bytes, BW 10000 Kbit, DLY 1000 usec, 
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
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 PAUSE output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet0/9 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 0007.7dee.8889 (bia 0007.7dee.8889)
  MTU 1500 bytes, BW 10000 Kbit, DLY 1000 usec, 
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
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 PAUSE output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet0/10 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 0007.7dee.888a (bia 0007.7dee.888a)
  MTU 1500 bytes, BW 10000 Kbit, DLY 1000 usec, 
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
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 PAUSE output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet0/11 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 0007.7dee.888b (bia 0007.7dee.888b)
  MTU 1500 bytes, BW 10000 Kbit, DLY 1000 usec, 
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
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 PAUSE output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet0/12 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 0007.7dee.888c (bia 0007.7dee.888c)
  MTU 1500 bytes, BW 100000 Kbit, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 00:00:00, output hang never
  Last clearing of "" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 1000 bits/sec, 1 packets/sec
     9931863 packets input, 3696298005 bytes, 0 no buffer
     Received 9931863 broadcasts (313934 multicasts)
     0 runts, 1 giants, 0 throttles
     4 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 313934 multicast, 0 pause input
     0 input packets with dribble condition detected
     149458244 packets output, 14979468109 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 babbles, 0 late collision, 0 deferred
               0 lost carrier, 0 no carrier, 0 PAUSE output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet0/13 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 0007.7dee.888d (bia 0007.7dee.888d)
  MTU 1500 bytes, BW 100000 Kbit, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 00:00:00, output hang never
  Last clearing of "" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 1000 bits/sec, 1 packets/sec
     176232357 packets input, 16857817481 bytes, 0 no buffer
     Received 343220 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     340921355 packets output, 34686547050 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 PAUSE output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet0/14 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 0007.7dee.888e (bia 0007.7dee.888e)
  MTU 1500 bytes, BW 100000 Kbit, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 00:00:00, output hang never
  Last clearing of "" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 1000 bits/sec, 1 packets/sec
     37232270 packets input, 2621478120 bytes, 0 no buffer
     Received 1 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     207145748 packets output, 22239969469 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 PAUSE output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet0/15 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 0007.7dee.888f (bia 0007.7dee.888f)
  MTU 1500 bytes, BW 10000 Kbit, DLY 1000 usec, 
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
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 PAUSE output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet0/16 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 0007.7dee.8890 (bia 0007.7dee.8890)
  MTU 1500 bytes, BW 10000 Kbit, DLY 1000 usec, 
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
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 PAUSE output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet0/17 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 0007.7dee.8891 (bia 0007.7dee.8891)
  MTU 1500 bytes, BW 10000 Kbit, DLY 1000 usec, 
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
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 PAUSE output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet0/18 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 0007.7dee.8892 (bia 0007.7dee.8892)
  MTU 1500 bytes, BW 10000 Kbit, DLY 1000 usec, 
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
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 PAUSE output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet0/19 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 0007.7dee.8893 (bia 0007.7dee.8893)
  MTU 1500 bytes, BW 10000 Kbit, DLY 1000 usec, 
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
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 PAUSE output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet0/20 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 0007.7dee.8894 (bia 0007.7dee.8894)
  MTU 1500 bytes, BW 10000 Kbit, DLY 1000 usec, 
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
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 PAUSE output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet0/21 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 0007.7dee.8895 (bia 0007.7dee.8895)
  MTU 1500 bytes, BW 10000 Kbit, DLY 1000 usec, 
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
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 PAUSE output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet0/22 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 0007.7dee.8896 (bia 0007.7dee.8896)
  MTU 1500 bytes, BW 10000 Kbit, DLY 1000 usec, 
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
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 PAUSE output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet0/23 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 0007.7dee.8897 (bia 0007.7dee.8897)
  Description: fm-scada
  MTU 1500 bytes, BW 10000 Kbit, DLY 1000 usec, 
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
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 PAUSE output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet0/24 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 0007.7dee.8898 (bia 0007.7dee.8898)
  Description: fm-scada
  MTU 1500 bytes, BW 10000 Kbit, DLY 1000 usec, 
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
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 PAUSE output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/1 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 0007.7dee.8899 (bia 0007.7dee.8899)
  Description: key:G1/1:dx1-029field-lib:Te1/1/3
  MTU 1500 bytes, BW 1000000 Kbit, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not set
  Full-duplex, 1000Mb/s, link type is auto, media type is 1000BaseLX SFP
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output 00:00:01, output hang never
  Last clearing of "" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 44000 bits/sec, 42 packets/sec
  5 minute output rate 39000 bits/sec, 17 packets/sec
     4568774100 packets input, 1624969594194 bytes, 0 no buffer
     Received 2454608184 broadcasts (1669464971 multicasts)
     0 runts, 0 giants, 0 throttles
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 1669464971 multicast, 0 pause input
     0 input packets with dribble condition detected
     1916663559 packets output, 499332598941 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 babbles, 0 late collision, 0 deferred
               0 lost carrier, 0 no carrier, 0 PAUSE output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/2 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 0007.7dee.889a (bia 0007.7dee.889a)
  Description: key:sx1-029field-sign-lib:g0/12
  MTU 1500 bytes, BW 1000000 Kbit, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not set
  Full-duplex, 1000Mb/s, link type is auto, media type is 1000BaseLX SFP
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output 00:00:00, output hang never
  Last clearing of "" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 13000 bits/sec, 6 packets/sec
  5 minute output rate 13000 bits/sec, 8 packets/sec
     191971714 packets input, 49100312123 bytes, 0 no buffer
     Received 44459849 broadcasts (39378910 multicasts)
     0 runts, 0 giants, 0 throttles
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 39378910 multicast, 0 pause input
     0 input packets with dribble condition detected
     284916963 packets output, 97311480874 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 PAUSE output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/3 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 0007.7dee.889b (bia 0007.7dee.889b)
  MTU 1500 bytes, BW 10000 Kbit, DLY 1000 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not set
  Auto-duplex, Auto-speed, link type is auto, media type is 1000BaseLX SFP
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
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 PAUSE output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/4 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 0007.7dee.889c (bia 0007.7dee.889c)
            MTU 1500 bytes, BW 10000 Kbit, DLY 1000 usec, 
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
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 PAUSE output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/1 is down, line protocol is down (notconnect) 
  Hardware is not present
  Hardware is Ten Gigabit Ethernet, address is 0007.7dee.889d (bia 0007.7dee.889d)
  MTU 1500 bytes, BW 10000 Kbit, DLY 1000 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not set
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
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 PAUSE output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/2 is down, line protocol is down (notconnect) 
  Hardware is not present
  Hardware is Ten Gigabit Ethernet, address is 0007.7dee.889e (bia 0007.7dee.889e)
  MTU 1500 bytes, BW 10000 Kbit, DLY 1000 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not set
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
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 PAUSE output
     0 output buffer failures, 0 output buffers swapped out""",
 'show inventory':"""NAME: "1", DESCR: "WS-C3560X-24P"
PID: WS-C3560X-24P-L   , VID: V02  , SN: FDO1522P0KU

NAME: "Power Supply 0", DESCR: "FRU Power Supply"
PID: C3KX-PWR-715WAC   , VID: V01  , SN: LIT151303ZG

NAME: "FRULink Slot 1 - FRULink Module", DESCR: "FRULink 1G Module"
PID: C3KX-NM-1G        , VID: V01  , SN: FDO15200U16

NAME: "GigabitEthernet1/1", DESCR: "1000BaseLX SFP"
PID: Unspecified       , VID:      , SN: FNS1006R02J     

NAME: "GigabitEthernet1/2", DESCR: "1000BaseLX SFP"
PID: Unspecified       , VID:      , SN: AGS1007A0TG     

NAME: "GigabitEthernet1/3", DESCR: "1000BaseLX SFP"
PID: Unspecified       , VID:      , SN: F34233570070    

""",
 'show interface counters':"""Port            InOctets    InUcastPkts    InMcastPkts    InBcastPkts 
Gi0/1       275994066681      972371868        5708853          56069 
Gi0/2       135574152989      560516272            197         111689 
Gi0/3          597362203        3174815              0         474603 
Gi0/4                  0              0              0              0 
Gi0/5                  0              0              0              0 
Gi0/6                  0              0              0              0 
Gi0/7                  0              0              0              0 
Gi0/8                  0              0              0              0 
Gi0/9                  0              0              0              0 
Gi0/10                 0              0              0              0 
Gi0/11                 0              0              0              0 
Gi0/12        3696298373              0         313934        9617930 
Gi0/13       16857817545      175889138              0         343220 
Gi0/14        2621478120       37232269              0              1 
Gi0/15                 0              0              0              0 
Gi0/16                 0              0              0              0 
Gi0/17                 0              0              0              0 
Gi0/18                 0              0              0              0 
Gi0/19                 0              0              0              0 
Gi0/20                 0              0              0              0 
Gi0/21                 0              0              0              0 
Gi0/22                 0              0              0              0 
Gi0/23                 0              0              0              0 
Gi0/24                 0              0              0              0 
Gi1/1      1624969602869     2114165977     1669464995      785143224 
Gi1/2        49100313577      147511868       39378910        5080939 
Gi1/3                  0              0              0              0 
Gi1/4                  0              0              0              0 

Port           OutOctets   OutUcastPkts   OutMcastPkts   OutBcastPkts 
Gi0/1      1244017192018     1205433779      152850112         713936 
Gi0/2        74295998933      581981928      147910651          50177 
Gi0/3        61532965295       12134151      133201879      633366634 
Gi0/4                  0              0              0              0 
Gi0/5                  0              0              0              0 
Gi0/6                  0              0              0              0 
Gi0/7                  0              0              0              0 
Gi0/8                  0              0              0              0 
Gi0/9                  0              0              0              0 
Gi0/10                 0              0              0              0 
Gi0/11                 0              0              0              0 
Gi0/12       14979468409        9226170      139209907        1022170 
Gi0/13       34686547788      181385340      149188857       10347163 
Gi0/14       22239970137       47266503      149188859       10690390 
Gi0/15                 0              0              0              0 
Gi0/16                 0              0              0              0 
Gi0/17                 0              0              0              0 
Gi0/18                 0              0              0              0 
Gi0/19                 0              0              0              0 
Gi0/20                 0              0              0              0 
Gi0/21                 0              0              0              0 
Gi0/22                 0              0              0              0 
Gi0/23                 0              0              0              0 
Gi0/24                 0              0              0              0 
Gi1/1       499332624060     1873638109       27631271       15394249 
Gi1/2        97311482514      157646057      127161472         109442 
Gi1/3                  0              0              0              0 
          
Port           OutOctets   OutUcastPkts   OutMcastPkts   OutBcastPkts 
Gi1/4                  0              0              0              0 """,
 'show cdp nei detail':"""-------------------------
Device ID: sx1-029field-sign-lib.net.utah.edu
Entry address(es): 
  IP address: 155.97.126.102
Platform: cisco IE-4000-4GC4GP4G-E,  Capabilities: Switch IGMP 
Interface: GigabitEthernet1/2,  Port ID (outgoing port): GigabitEthernet1/1
Holdtime : 142 sec

Version :
Cisco IOS Software, IE4000  Software (IE4000-UNIVERSALK9-M), Version 15.2(4)EA9, RELEASE SOFTWARE (fc2)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2019 by Cisco Systems, Inc.
Compiled Wed 26-Jun-19 03:37 by prod_rel_team

advertisement version: 2
VTP Management Domain: 'vtp-029field'
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 155.97.126.102

-------------------------
Device ID: dx1-029field-lib.net.utah.edu
Entry address(es): 
  IP address: 155.97.126.100
Platform: cisco WS-C3650-48PQ,  Capabilities: Switch IGMP 
Interface: GigabitEthernet1/1,  Port ID (outgoing port): TenGigabitEthernet1/1/3
Holdtime : 137 sec

Version :
Cisco IOS Software [Everest], Catalyst L3 Switch Software (CAT3K_CAA-UNIVERSALK9-M), Version 16.6.8, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2020 by Cisco Systems, Inc.
Compiled Thu 23-Apr-20 17:22 by mcpre

advertisement version: 2
VTP Management Domain: 'vtp-029field'
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 155.97.126.100

-------------------------
Device ID: ap-0029-1-x
Entry address(es): 
  IP address: 172.30.4.22
  IPv6 address: FE80::26B:F1FF:FE25:D38E  (link-local)
Platform: cisco AIR-AP3802I-B-K9,  Capabilities: Router Trans-Bridge 
Interface: GigabitEthernet0/1,  Port ID (outgoing port): GigabitEthernet0
Holdtime : 121 sec

Version :
Cisco AP Software, ap3g3-k9w8 Version: 8.10.151.0
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 2014-2015 by Cisco Systems, Inc.

advertisement version: 2
Duplex: full
          Power drawn: 29.900 Watts
Power request id: 2175, Power management id: 13
Power request levels are:29900 15400 0 0 0 
Management address(es): 
  IP address: 172.30.4.22
""",
 'show module all':"""^
% Invalid input detected at '^' marker.
""",
 'show module':"""^
% Invalid input detected at '^' marker.
""",
 'show run | section snmp':"""^
% Invalid input detected at '^' marker.
""",
 'show run | in snmp':"""snmp-server engineID local 000000090200000628362780
snmp-server group NOCGrv3RO v3 priv read NOCViewRO access 70
snmp-server group NOCGrv3RO v3 auth context vlan- match prefix 
snmp-server group NOCGrv3RW v3 priv write NOCViewRW access 71
snmp-server view NOCViewRO internet included
snmp-server view NOCViewRW internet included
snmp-server community We5U=#9vahev RW 71
snmp-server community fortNs!$q~5r9 RW 71
snmp-server community fort$NmP! RO 70
snmp-server community 99U#u#U!x RO 70
snmp-server community 1xR$bluE RO 73
snmp-server community cl3an RW 71
snmp-server community Yx5XdagKRsmD3Oi RO 70
snmp-server location Bldg. 029 Room hightemp
snmp-server contact BC-503691 Y-040806
snmp-server enable traps snmp authentication linkdown linkup coldstart warmstart
snmp-server enable traps tty
snmp-server enable traps config
snmp-server enable traps stpx root-inconsistency loop-inconsistency
snmp-server enable traps vlancreate
snmp-server enable traps vlandelete
snmp-server enable traps envmon fan shutdown supply temperature status
snmp-server host 155.98.253.152 version 2c 99U#u#U!x 
snmp-server host 155.98.253.148 v2c 
snmp-server host 155.98.253.149 v2c 
snmp ifmib ifindex persist""",
 'show snmp user':"""User name: NONUserv3RO
Engine ID: 000000090200000628362780
storage-type: nonvolatile	 active
Authentication Protocol: MD5
Privacy Protocol: DES
Group-name: NOCGrv3RO

User name: NONUserv3Rw
Engine ID: 000000090200000628362780
storage-type: nonvolatile	 active
Authentication Protocol: MD5
Privacy Protocol: DES
Group-name: NOCGrv3RW
""",
 'show access-list':"""Standard IP access list 70
    10 permit 10.64.2.70
    230 permit 10.71.25.65
    50 permit 155.100.126.163
    40 permit 155.100.126.162
    190 permit 10.71.24.21
    180 permit 10.71.24.20
    210 permit 10.71.24.23
    200 permit 10.71.24.22
    150 permit 10.71.24.17
    140 permit 10.71.24.16
    170 permit 10.71.24.19
    160 permit 10.71.24.18
    20 permit 172.20.150.100
    220 permit 10.71.24.25
    110 permit 10.71.24.13
    100 permit 10.71.24.12
    130 permit 10.71.24.15
    120 permit 10.71.24.14
    90 permit 10.71.24.11
    30 permit 155.100.123.72
    240 permit 10.71.25.164
    60 permit 155.98.164.192, wildcard bits 0.0.0.31
    70 permit 155.99.254.128, wildcard bits 0.0.0.127
    80 permit 155.98.253.0, wildcard bits 0.0.0.255
    250 deny   any log
Standard IP access list 71
    10 permit 10.64.2.70
    230 permit 10.71.25.65
    50 permit 155.100.126.163
    40 permit 155.100.126.162
    190 permit 10.71.24.21
    180 permit 10.71.24.20
    210 permit 10.71.24.23
    200 permit 10.71.24.22
    150 permit 10.71.24.17
    140 permit 10.71.24.16 (1610264 matches)
    170 permit 10.71.24.19
    160 permit 10.71.24.18
    20 permit 172.20.150.100
    220 permit 10.71.24.25
    110 permit 10.71.24.13
    100 permit 10.71.24.12
    130 permit 10.71.24.15
    120 permit 10.71.24.14
    90 permit 10.71.24.11
    30 permit 155.100.123.72
    240 permit 10.71.25.164
    60 permit 155.98.164.192, wildcard bits 0.0.0.31
    70 permit 155.99.254.128, wildcard bits 0.0.0.127
    80 permit 155.98.253.0, wildcard bits 0.0.0.255
    250 deny   any log
Extended IP access list 101
    10 deny udp any any eq 135
    20 deny udp any any eq 136
    30 deny udp any any eq netbios-ns
    40 deny udp any any eq netbios-dgm
    50 deny tcp any any eq 139
    60 deny tcp any any eq 445
              70 deny udp any any eq 445
    80 deny udp any any eq bootpc
    90 permit ip any any
Extended IP access list 199
    10 permit tcp 155.98.253.0 0.0.0.255 any eq 22 (66 matches)
    20 permit tcp host 172.20.150.100 any eq 22
    30 permit tcp host 155.100.126.162 any eq 22
    40 permit tcp host 155.100.126.163 any eq 22
    50 permit tcp host 10.64.2.70 any eq 22
    60 permit tcp host 155.99.239.130 any eq 22
    70 permit tcp host 155.97.152.244 any eq 22
    80 permit tcp host 155.100.123.72 any eq 22
    90 permit tcp 155.99.254.128 0.0.0.127 any eq 22 (2 matches)
    100 permit tcp 155.98.164.192 0.0.0.31 any eq 22 (12 matches)
    110 permit tcp host 10.71.24.11 any eq 22
    120 permit tcp host 10.71.24.12 any eq 22
    130 permit tcp host 10.71.24.13 any eq 22
    140 permit tcp host 10.71.24.14 any eq 22
    150 permit tcp host 10.71.24.15 any eq 22
    160 permit tcp host 10.71.24.16 any eq 22 (88 matches)
    170 permit tcp host 10.71.24.17 any eq 22
    180 permit tcp host 10.71.24.18 any eq 22
    190 permit tcp host 10.71.24.19 any eq 22
    200 permit tcp host 10.71.24.20 any eq 22
    210 permit tcp host 10.71.24.21 any eq 22
    220 permit tcp host 10.71.24.22 any eq 22
    230 permit tcp host 10.71.24.23 any eq 22
    240 permit tcp host 10.71.24.25 any eq 22
    250 permit tcp host 10.71.25.65 any eq 22
    260 permit tcp host 10.71.25.164 any eq 22
    270 deny ip any any log (20 matches)""",
 'show run | section logging':"""^
% Invalid input detected at '^' marker.
""",
 'show run | in logging':"""logging buffered notifications
logging console critical
logging facility local6
logging source-interface Vlan802
logging 155.98.253.244
logging 155.98.204.52
logging host 172.24.29.65 transport udp port 5140
logging 172.24.29.14
logging 10.70.24.10""",
 'show mac address-table':"""Mac Address Table
-------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
 All    0100.0ccc.cccc    STATIC      CPU
 All    0100.0ccc.cccd    STATIC      CPU
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
 751    0000.0c9f.f2ef    DYNAMIC     Gi1/1
 751    0018.8520.281d    DYNAMIC     Gi0/12
 751    001e.1e24.4a3c    DYNAMIC     Gi0/13
 751    a89d.21e5.b9b3    DYNAMIC     Gi1/1
 751    ecce.1389.7802    DYNAMIC     Gi1/1
 751    ecce.1389.8582    DYNAMIC     Gi1/1
 694    0000.0c9f.f2b6    DYNAMIC     Gi1/1
 694    5065.83c7.31b9    DYNAMIC     Gi0/2
 694    a89d.21e5.b9b3    DYNAMIC     Gi1/1
 694    ecce.1389.7802    DYNAMIC     Gi1/1
 694    ecce.1389.8582    DYNAMIC     Gi1/1
 419    0000.0c9f.f1a3    DYNAMIC     Gi1/1
 419    006b.f125.d38e    DYNAMIC     Gi0/1
 419    2c5a.0f22.8696    DYNAMIC     Gi1/1
 419    a89d.21e5.b9b3    DYNAMIC     Gi1/1
 419    ac7a.5695.237a    DYNAMIC     Gi1/2
 419    ecce.1389.7802    DYNAMIC     Gi1/1
 419    ecce.1389.8582    DYNAMIC     Gi1/1
   1    a89d.21e5.b9b3    DYNAMIC     Gi1/1
   1    f45e.ab3b.684f    DYNAMIC     Gi1/1
 636    0000.0c9f.f27c    DYNAMIC     Gi1/1
 636    0010.8d04.5c08    DYNAMIC     Gi1/1
 636    0090.c2f7.ed4e    DYNAMIC     Gi0/3
 636    a89d.21e5.b9b3    DYNAMIC     Gi1/1
 636    ecce.1389.8582    DYNAMIC     Gi1/1
 656    0000.0c9f.f290    DYNAMIC     Gi1/1
 656    001e.c600.1a77    DYNAMIC     Gi1/1
 656    a89d.21e5.b9b3    DYNAMIC     Gi1/1
 656    ecce.1389.7802    DYNAMIC     Gi1/1
 656    ecce.1389.8582    DYNAMIC     Gi1/1
 802    0000.0c9f.f322    DYNAMIC     Gi1/1
 802    a89d.21e5.b9b3    DYNAMIC     Gi1/1
 802    ecce.1389.7802    DYNAMIC     Gi1/1
 802    ecce.1389.8582    DYNAMIC     Gi1/1
          1208    0000.0c9f.f4b8    DYNAMIC     Gi1/1
1208    a89d.21e5.b9b3    DYNAMIC     Gi1/1
1208    ecce.1389.7802    DYNAMIC     Gi1/1
1208    ecce.1389.8582    DYNAMIC     Gi1/1
2100    0000.0c9f.f834    DYNAMIC     Gi1/1
2100    0003.2d45.8cec    DYNAMIC     Gi1/2
2100    0003.2d46.a644    DYNAMIC     Gi1/2
2100    0003.2d46.a664    DYNAMIC     Gi1/2
2100    0003.2d46.b508    DYNAMIC     Gi1/2
2100    a89d.21e5.b9b3    DYNAMIC     Gi1/1
2100    ecce.1389.7802    DYNAMIC     Gi1/1
2100    ecce.1389.8582    DYNAMIC     Gi1/1
Total Mac Addresses for this criterion: 66""",
 'show run | section tacacs':"""^
% Invalid input detected at '^' marker.
""",
 'show run | in tacacs':"""aaa authentication login default group tacacs+ enable
aaa authentication enable default group tacacs+ enable
aaa authorization exec default group tacacs+ 
aaa authorization commands 0 default group tacacs+ 
aaa authorization commands 1 default group tacacs+ 
aaa authorization commands 15 default group tacacs+ 
aaa accounting exec default start-stop group tacacs+
aaa accounting commands 1 default stop-only group tacacs+
aaa accounting commands 15 default stop-only group tacacs+
aaa accounting connection default start-stop group tacacs+
aaa accounting system default start-stop group tacacs+
tacacs-server host 172.31.17.180
tacacs-server host 10.64.32.5
tacacs-server directed-request
tacacs-server key 7 032D1F0E2F4B246E6E0B0044""",
 'show power inline':"""Available:495.0(w)  Used:45.3(w)  Remaining:449.7(w)

Interface Admin  Oper       Power   Device              Class Max
                            (Watts)                            
--------- ------ ---------- ------- ------------------- ----- ----
Gi0/1     auto   on         29.9    AIR-AP3802I-B-K9    4     30.0 
Gi0/2     auto   off        0.0     n/a                 n/a   30.0 
Gi0/3     auto   off        0.0     n/a                 n/a   30.0 
Gi0/4     auto   off        0.0     n/a                 n/a   30.0 
Gi0/5     auto   off        0.0     n/a                 n/a   30.0 
Gi0/6     auto   off        0.0     n/a                 n/a   30.0 
Gi0/7     auto   off        0.0     n/a                 n/a   30.0 
Gi0/8     auto   off        0.0     n/a                 n/a   30.0 
Gi0/9     auto   off        0.0     n/a                 n/a   30.0 
Gi0/10    auto   off        0.0     n/a                 n/a   30.0 
Gi0/11    auto   off        0.0     n/a                 n/a   30.0 
Gi0/12    auto   on         15.4    Ieee PD             3     30.0 
Gi0/13    auto   off        0.0     n/a                 n/a   30.0 
Gi0/14    auto   off        0.0     n/a                 n/a   30.0 
Gi0/15    auto   off        0.0     n/a                 n/a   30.0 
Gi0/16    auto   off        0.0     n/a                 n/a   30.0 
Gi0/17    auto   off        0.0     n/a                 n/a   30.0 
Gi0/18    auto   off        0.0     n/a                 n/a   30.0 
Gi0/19    auto   off        0.0     n/a                 n/a   30.0 
Gi0/20    auto   off        0.0     n/a                 n/a   30.0 
Gi0/21    auto   off        0.0     n/a                 n/a   30.0 
Gi0/22    auto   off        0.0     n/a                 n/a   30.0 
Gi0/23    auto   off        0.0     n/a                 n/a   30.0 
Gi0/24    auto   off        0.0     n/a                 n/a   30.0 """,
 'show environment all':"""^
% Invalid input detected at '^' marker.
""",
}
