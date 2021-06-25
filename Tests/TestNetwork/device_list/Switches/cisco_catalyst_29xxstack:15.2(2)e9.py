ip_address = '172.20.66.203'
software = 'software'
hardware = 'hardware'
read_results = {
 'show version':"""Cisco IOS Software, C2960S Software (C2960S-UNIVERSALK9-M), Version 15.2(2)E9, RELEASE SOFTWARE (fc4)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2018 by Cisco Systems, Inc.
Compiled Sat 08-Sep-18 14:56 by prod_rel_team

ROM: Bootstrap program is C2960S board boot loader
BOOTLDR: C2960S Boot Loader (C2960S-HBOOT-M) Version 12.2(55r)SE, RELEASE SOFTWARE (fc1)

sx2-521som-2r189-som uptime is 1 year, 38 weeks, 2 days, 1 hour, 48 minutes
System returned to ROM by power-on
System restarted at 13:42:05 MDT Tue Oct 1 2019
System image file is "flash:/c2960s-universalk9-mz.152-2.E9.bin"
Last reload reason: power-on



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

cisco WS-C2960S-24PS-L (PowerPC) processor (revision G0) with 131072K bytes of memory.
Processor board ID FOC1721X3S9
Last reset from power-on
2 Virtual Ethernet interfaces
1 FastEthernet interface
28 Gigabit Ethernet interfaces
The password-recovery mechanism is enabled.

512K bytes of flash-simulated non-volatile configuration memory.
Base ethernet MAC Address       : 0C:68:03:42:CB:80
Motherboard assembly number     : 73-11908-09
Power supply part number        : 341-0393-02
Motherboard serial number       : FOC17202CZB
Power supply serial number      : DCA1717U0JY
Model revision number           : G0
Motherboard revision number     : A0
Model number                    : WS-C2960S-24PS-L
Daughterboard assembly number   : 73-11933-04
Daughterboard serial number     : FOC17210JY9
System serial number            : FOC1721X3S9
Top Assembly Part Number        : 800-30945-04
Top Assembly Revision Number    : A0
Version ID                      : V04
CLEI Code Number                : COMGE00ARD
Daughterboard revision number   : A0
Hardware Board Revision Number  : 0x01


          Switch Ports Model                     SW Version            SW Image                 
------ ----- -----                     ----------            ----------               
*    1 28    WS-C2960S-24PS-L          15.2(2)E9             C2960S-UNIVERSALK9-M     


Configuration register is 0xF
""",
 'show run':"""Building configuration...

Current configuration : 10853 bytes
!
! Last configuration change at 16:10:12 MDT Fri Jun 11 2021 by u0800148
! NVRAM config last updated at 21:26:44 MDT Sun Jun 20 2021 by noc-orionncm
!
version 15.2
no service pad
service timestamps debug datetime msec localtime
service timestamps log datetime msec localtime
service password-encryption
!
hostname sx2-521som-2r189-som
!
boot-start-marker
boot-end-marker
!
logging buffered notifications
logging console critical
enable secret 5 $1$4t.F$L9qshsCYyLDWvFWFGoBKW1
!
aaa new-model
!
!
aaa group server tacacs+ NOC-TAC
 server name TAC-EBC
 server name TAC-SECONDARY
!
aaa authentication login default group NOC-TAC line enable
aaa authentication login console enable
aaa authentication enable default group NOC-TAC enable
aaa authorization exec default group NOC-TAC 
aaa authorization commands 0 default group NOC-TAC 
aaa authorization commands 1 default group NOC-TAC 
aaa authorization commands 15 default group NOC-TAC 
aaa accounting exec default start-stop group NOC-TAC
aaa accounting commands 1 default stop-only group NOC-TAC
aaa accounting commands 15 default stop-only group NOC-TAC
aaa accounting connection default start-stop group NOC-TAC
aaa accounting system default start-stop group NOC-TAC
!
!
!
!
!
!
aaa session-id common
clock timezone MST -7 0
clock summer-time MDT recurring
switch 1 provision ws-c2960s-24ps-l
no ip source-route
!
!
ip domain-name net.utah.edu
ip name-server 172.20.120.20
vtp domain vtp-5100acc
vtp mode transparent
!
!
          !
!
!
udld aggressive

authentication mac-move permit
!
!
!
!
spanning-tree mode rapid-pvst
spanning-tree extend system-id
no errdisable detect cause gbic-invalid
errdisable recovery cause udld
errdisable recovery cause storm-control
!
!
!
!
vlan internal allocation policy ascending
!
vlan 111
 name som-zeroclients-2
!
vlan 333
 name som-521som-m
!
vlan 382
 name clin-521-som
!
vlan 702
 name som-521som-voip
!
vlan 1040
 name som-521som-ap-mgmt
!
lldp run
!
! 
!
!
!
!
!
!
!
!
interface FastEthernet0
 no ip address
 shutdown
!
interface GigabitEthernet1/0/1
 switchport access vlan 382
 switchport mode access
 switchport voice vlan 702
 spanning-tree portfast
!
interface GigabitEthernet1/0/2
 description ACCESS POINT
           switchport access vlan 1040
 switchport mode access
!
interface GigabitEthernet1/0/3
 description ACCESS POINT
 switchport access vlan 1040
 switchport mode access
!
interface GigabitEthernet1/0/4
 description ACCESS POINT
 switchport access vlan 1040
 switchport mode access
!
interface GigabitEthernet1/0/5
 description ACCESS POINT
 switchport access vlan 1040
 switchport mode access
!
interface GigabitEthernet1/0/6
 description ACCESS POINT
 switchport access vlan 1040
 switchport mode access
!
interface GigabitEthernet1/0/7
 description ACCESS POINT
 switchport access vlan 1040
 switchport mode access
!
interface GigabitEthernet1/0/8
 switchport access vlan 1040
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/9
 switchport access vlan 111
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/10
 switchport access vlan 1040
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/11
 switchport access vlan 382
 switchport mode access
 switchport voice vlan 702
 spanning-tree portfast
!
interface GigabitEthernet1/0/12
 switchport access vlan 1040
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/13
 switchport access vlan 382
 switchport mode access
 switchport voice vlan 702
 spanning-tree portfast
          !
interface GigabitEthernet1/0/14
 switchport access vlan 382
 switchport mode access
 switchport voice vlan 702
 spanning-tree portfast
!
interface GigabitEthernet1/0/15
 switchport access vlan 382
 switchport mode access
 switchport voice vlan 702
 spanning-tree portfast
!
interface GigabitEthernet1/0/16
 switchport access vlan 382
 switchport mode access
 switchport voice vlan 702
 spanning-tree portfast
!
interface GigabitEthernet1/0/17
 switchport access vlan 382
 switchport mode access
 switchport voice vlan 702
 spanning-tree portfast
!
interface GigabitEthernet1/0/18
 switchport access vlan 1040
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/19
 switchport access vlan 1040
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/20
 switchport access vlan 1040
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/21
 switchport access vlan 1040
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/22
 switchport access vlan 1040
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/23
 switchport access vlan 1040
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/24
 switchport mode trunk
!
interface GigabitEthernet1/0/25
           switchport mode trunk
!
interface GigabitEthernet1/0/26
!
interface GigabitEthernet1/0/27
!
interface GigabitEthernet1/0/28
!
interface Vlan1
 no ip address
 no ip route-cache
 shutdown
!
interface Vlan333
 ip address 172.20.66.203 255.255.255.0
!
ip default-gateway 172.20.66.1
no ip http server
no ip http secure-server
!
ip tftp blocksize 8192
ip ssh version 2
!
logging facility local6
logging source-interface Vlan333
logging host 155.98.204.52
logging host 155.98.253.244
logging host 172.24.29.14
logging host 10.70.24.10
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
          !
snmp-server group NOCGrv3RO v3 priv read NOCViewRO access 70
snmp-server group NOCGrv3RO v3 auth context vlan- match prefix 
snmp-server group NOCGrv3RW v3 priv write NOCViewRW access 71
snmp-server view NOCViewRO internet included
snmp-server view NOCViewRW internet included
snmp-server location Bldg. 3701 Room 2w
snmp-server contact BC-1 Y-336099
snmp ifmib ifindex persist
tacacs server TAC-EBC
 address ipv4 172.31.17.180
 key 7 0522420A08084B2B39070E53
tacacs server TAC-SECONDARY
 address ipv4 10.64.32.5
 key 7 022F405E22420A036C4C1058
!
!
privilege exec level 1 show configuration
privilege exec level 1 show
banner login ^C
sx2-521som-2r189-som

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
!
line con 0
 exec-timeout 15 0
 password 7 0814584F011B444446
 login authentication console
 stopbits 1
line vty 0 4
 access-class 199 in
 exec-timeout 30 0
 password 7 046E1F0707230D1D5D
 transport input ssh
line vty 5 15
 access-class 199 in
 exec-timeout 30 0
 password 7 046E1F0707230D1D5D
 transport input ssh
!
ntp server time.utah.edu
end
""",
 'show int status':"""Port      Name               Status       Vlan       Duplex  Speed Type 
Gi1/0/1                      connected    382        a-full  a-100 10/100/1000BaseTX
Gi1/0/2   ACCESS POINT       connected    1040       a-full a-1000 10/100/1000BaseTX
Gi1/0/3   ACCESS POINT       connected    1040       a-full a-1000 10/100/1000BaseTX
Gi1/0/4   ACCESS POINT       connected    1040       a-full a-1000 10/100/1000BaseTX
Gi1/0/5   ACCESS POINT       connected    1040       a-full a-1000 10/100/1000BaseTX
Gi1/0/6   ACCESS POINT       connected    1040       a-full a-1000 10/100/1000BaseTX
Gi1/0/7   ACCESS POINT       connected    1040       a-full a-1000 10/100/1000BaseTX
Gi1/0/8                      notconnect   1040         auto   auto 10/100/1000BaseTX
Gi1/0/9                      connected    111        a-full a-1000 10/100/1000BaseTX
Gi1/0/10                     notconnect   1040         auto   auto 10/100/1000BaseTX
Gi1/0/11                     connected    382        a-full a-1000 10/100/1000BaseTX
Gi1/0/12                     connected    1040       a-full  a-100 10/100/1000BaseTX
Gi1/0/13                     connected    382        a-full a-1000 10/100/1000BaseTX
Gi1/0/14                     connected    382        a-full a-1000 10/100/1000BaseTX
Gi1/0/15                     connected    382        a-full a-1000 10/100/1000BaseTX
Gi1/0/16                     connected    382        a-full a-1000 10/100/1000BaseTX
Gi1/0/17                     connected    382        a-full  a-100 10/100/1000BaseTX
Gi1/0/18                     notconnect   1040         auto   auto 10/100/1000BaseTX
Gi1/0/19                     connected    1040       a-full a-1000 10/100/1000BaseTX
Gi1/0/20                     connected    1040       a-full a-1000 10/100/1000BaseTX
Gi1/0/21                     connected    1040       a-full a-1000 10/100/1000BaseTX
Gi1/0/22                     connected    1040       a-full a-1000 10/100/1000BaseTX
Gi1/0/23                     connected    1040       a-full a-1000 10/100/1000BaseTX
Gi1/0/24                     connected    trunk      a-full a-1000 10/100/1000BaseTX
Gi1/0/25                     notconnect   1            auto   auto Not Present
Gi1/0/26                     notconnect   1            auto   auto Not Present
Gi1/0/27                     notconnect   1            auto   auto Not Present
Gi1/0/28                     notconnect   1            auto   auto Not Present
Fa0                          disabled     routed       auto   auto 10/100BaseTX""",
 'show run | section interface':"""interface FastEthernet0
 no ip address
 shutdown
interface GigabitEthernet1/0/1
 switchport access vlan 382
 switchport mode access
 switchport voice vlan 702
 spanning-tree portfast
interface GigabitEthernet1/0/2
 description ACCESS POINT
 switchport access vlan 1040
 switchport mode access
interface GigabitEthernet1/0/3
 description ACCESS POINT
 switchport access vlan 1040
 switchport mode access
interface GigabitEthernet1/0/4
 description ACCESS POINT
 switchport access vlan 1040
 switchport mode access
interface GigabitEthernet1/0/5
 description ACCESS POINT
 switchport access vlan 1040
 switchport mode access
interface GigabitEthernet1/0/6
 description ACCESS POINT
 switchport access vlan 1040
 switchport mode access
interface GigabitEthernet1/0/7
 description ACCESS POINT
 switchport access vlan 1040
 switchport mode access
interface GigabitEthernet1/0/8
 switchport access vlan 1040
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/9
 switchport access vlan 111
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/10
 switchport access vlan 1040
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/11
 switchport access vlan 382
 switchport mode access
 switchport voice vlan 702
 spanning-tree portfast
interface GigabitEthernet1/0/12
 switchport access vlan 1040
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/13
 switchport access vlan 382
 switchport mode access
 switchport voice vlan 702
 spanning-tree portfast
interface GigabitEthernet1/0/14
           switchport access vlan 382
 switchport mode access
 switchport voice vlan 702
 spanning-tree portfast
interface GigabitEthernet1/0/15
 switchport access vlan 382
 switchport mode access
 switchport voice vlan 702
 spanning-tree portfast
interface GigabitEthernet1/0/16
 switchport access vlan 382
 switchport mode access
 switchport voice vlan 702
 spanning-tree portfast
interface GigabitEthernet1/0/17
 switchport access vlan 382
 switchport mode access
 switchport voice vlan 702
 spanning-tree portfast
interface GigabitEthernet1/0/18
 switchport access vlan 1040
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/19
 switchport access vlan 1040
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/20
 switchport access vlan 1040
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/21
 switchport access vlan 1040
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/22
 switchport access vlan 1040
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/23
 switchport access vlan 1040
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/24
 switchport mode trunk
interface GigabitEthernet1/0/25
 switchport mode trunk
interface GigabitEthernet1/0/26
interface GigabitEthernet1/0/27
interface GigabitEthernet1/0/28
interface Vlan1
 no ip address
 no ip route-cache
 shutdown
interface Vlan333
 ip address 172.20.66.203 255.255.255.0
logging source-interface Vlan333""",
 'show run | in interface':"""interface FastEthernet0
interface GigabitEthernet1/0/1
interface GigabitEthernet1/0/2
interface GigabitEthernet1/0/3
interface GigabitEthernet1/0/4
interface GigabitEthernet1/0/5
interface GigabitEthernet1/0/6
interface GigabitEthernet1/0/7
interface GigabitEthernet1/0/8
interface GigabitEthernet1/0/9
interface GigabitEthernet1/0/10
interface GigabitEthernet1/0/11
interface GigabitEthernet1/0/12
interface GigabitEthernet1/0/13
interface GigabitEthernet1/0/14
interface GigabitEthernet1/0/15
interface GigabitEthernet1/0/16
interface GigabitEthernet1/0/17
interface GigabitEthernet1/0/18
interface GigabitEthernet1/0/19
interface GigabitEthernet1/0/20
interface GigabitEthernet1/0/21
interface GigabitEthernet1/0/22
interface GigabitEthernet1/0/23
interface GigabitEthernet1/0/24
interface GigabitEthernet1/0/25
interface GigabitEthernet1/0/26
interface GigabitEthernet1/0/27
interface GigabitEthernet1/0/28
interface Vlan1
interface Vlan333
logging source-interface Vlan333""",
 'show interface link':"""^
% Invalid input detected at '^' marker.
""",
 'show interface':"""Vlan1 is administratively down, line protocol is down 
  Hardware is EtherSVI, address is 0c68.0342.cbc0 (bia 0c68.0342.cbc0)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 32w3d, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     2 packets input, 684 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 1 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Vlan333 is up, line protocol is up 
  Hardware is EtherSVI, address is 0c68.0342.cbc2 (bia 0c68.0342.cbc2)
  Internet address is 172.20.66.203/24
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
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
  5 minute output rate 2000 bits/sec, 2 packets/sec
     63801971 packets input, 9146899304 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     58153166 packets output, 12987230951 bytes, 0 underruns
     0 output errors, 1 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
FastEthernet0 is administratively down, line protocol is down 
  Hardware is PowerPC FastEthernet, address is 0c68.0342.cbb9 (bia 0c68.0342.cbb9)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
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
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/1 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 0c68.0342.cb81 (bia 0c68.0342.cb81)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:24, output 00:00:01, output hang never
  Last clearing of "" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 509950
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 86000 bits/sec, 61 packets/sec
     3278734 packets input, 765787108 bytes, 0 no buffer
     Received 654296 broadcasts (654245 multicasts)
     1437 runts, 0 giants, 0 throttles 
     8243 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 654245 multicast, 0 pause input
     0 input packets with dribble condition detected
     2076194754 packets output, 292992426238 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/2 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 0c68.0342.cb82 (bia 0c68.0342.cb82)
  Description: ACCESS POINT
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:08, output 00:00:00, output hang never
  Last clearing of "" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 4000 bits/sec, 2 packets/sec
  5 minute output rate 9000 bits/sec, 13 packets/sec
     1441918606 packets input, 462513508768 bytes, 0 no buffer
               Received 6190816 broadcasts (3203012 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 3203012 multicast, 0 pause input
     0 input packets with dribble condition detected
     3350586397 packets output, 3291811736531 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/3 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 0c68.0342.cb83 (bia 0c68.0342.cb83)
  Description: ACCESS POINT
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:20, output 00:00:00, output hang never
  Last clearing of "" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 8000 bits/sec, 12 packets/sec
     404351499 packets input, 139192436099 bytes, 0 no buffer
     Received 6255896 broadcasts (3203916 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 3203916 multicast, 0 pause input
     0 input packets with dribble condition detected
     1199916745 packets output, 711280503575 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/4 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 0c68.0342.cb84 (bia 0c68.0342.cb84)
  Description: ACCESS POINT
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:05, output 00:00:00, output hang never
  Last clearing of "" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 2000 bits/sec, 1 packets/sec
  5 minute output rate 8000 bits/sec, 13 packets/sec
     414642123 packets input, 162861522258 bytes, 0 no buffer
     Received 6273116 broadcasts (3203637 multicasts)
               0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 3203637 multicast, 0 pause input
     0 input packets with dribble condition detected
     1068965315 packets output, 615082121664 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/5 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 0c68.0342.cb85 (bia 0c68.0342.cb85)
  Description: ACCESS POINT
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:07, output 00:00:00, output hang never
  Last clearing of "" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 1000 bits/sec, 1 packets/sec
  5 minute output rate 8000 bits/sec, 12 packets/sec
     366611865 packets input, 154571699528 bytes, 0 no buffer
     Received 6270285 broadcasts (3203902 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 3203902 multicast, 0 pause input
     0 input packets with dribble condition detected
     1051967726 packets output, 588982388532 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/6 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 0c68.0342.cb86 (bia 0c68.0342.cb86)
  Description: ACCESS POINT
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:28, output 00:00:00, output hang never
  Last clearing of "" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 79000 bits/sec, 6 packets/sec
  5 minute output rate 784000 bits/sec, 71 packets/sec
     384334632 packets input, 226971159405 bytes, 0 no buffer
     Received 6253860 broadcasts (3203891 multicasts)
     0 runts, 0 giants, 0 throttles 
               0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 3203891 multicast, 0 pause input
     0 input packets with dribble condition detected
     1087448084 packets output, 673651012217 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/7 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 0c68.0342.cb87 (bia 0c68.0342.cb87)
  Description: ACCESS POINT
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 34w3d, output 00:00:00, output hang never
  Last clearing of "" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 8000 bits/sec, 12 packets/sec
     279234731 packets input, 195827632013 bytes, 0 no buffer
     Received 3575674 broadcasts (1984680 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 1984680 multicast, 0 pause input
     0 input packets with dribble condition detected
     762970368 packets output, 257545741661 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/8 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 0c68.0342.cb88 (bia 0c68.0342.cb88)
  MTU 1500 bytes, BW 10000 Kbit/sec, DLY 1000 usec, 
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
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/9 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 0c68.0342.cb89 (bia 0c68.0342.cb89)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:09, output 00:00:01, output hang never
  Last clearing of "" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 2
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     14187988 packets input, 1314199860 bytes, 0 no buffer
     Received 1112134 broadcasts (550987 multicasts)
     0 runts, 0 giants, 0 throttles 
     6 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 550987 multicast, 0 pause input
     0 input packets with dribble condition detected
     1538510259 packets output, 220574004481 bytes, 0 underruns
     0 output errors, 0 collisions, 4 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/10 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 0c68.0342.cb8a (bia 0c68.0342.cb8a)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 252/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 32w3d, output hang never
  Last clearing of "" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     15 packets input, 3522 bytes, 0 no buffer
     Received 9 broadcasts (0 multicasts)
     1 runts, 0 giants, 0 throttles 
     4 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     186 packets output, 21485 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
               0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/11 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 0c68.0342.cb8b (bia 0c68.0342.cb8b)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:29, output 00:00:01, output hang never
  Last clearing of "" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 5
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 86000 bits/sec, 60 packets/sec
     104316841 packets input, 61740560545 bytes, 0 no buffer
     Received 1894345 broadcasts (1623461 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 1623461 multicast, 0 pause input
     0 input packets with dribble condition detected
     2240221067 packets output, 409296491377 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/12 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 0c68.0342.cb8c (bia 0c68.0342.cb8c)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 00:00:00, output hang never
  Last clearing of "" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 32674
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 7000 bits/sec, 12 packets/sec
     13164444 packets input, 900512906 bytes, 0 no buffer
     Received 13164444 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     1262 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     354753047 packets output, 32491085428 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
               0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/13 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 0c68.0342.cb8d (bia 0c68.0342.cb8d)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:19, output 00:00:00, output hang never
  Last clearing of "" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 3
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 86000 bits/sec, 61 packets/sec
     66472481 packets input, 23106574520 bytes, 0 no buffer
     Received 796594 broadcasts (744328 multicasts)
     0 runts, 1 giants, 0 throttles 
     1 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 744328 multicast, 0 pause input
     0 input packets with dribble condition detected
     2180012152 packets output, 386422706997 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/14 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 0c68.0342.cb8e (bia 0c68.0342.cb8e)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:13, output 00:00:00, output hang never
  Last clearing of "" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 3
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 85000 bits/sec, 60 packets/sec
     66243233 packets input, 32482740074 bytes, 0 no buffer
     Received 750602 broadcasts (708104 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 708104 multicast, 0 pause input
     0 input packets with dribble condition detected
     2180447195 packets output, 393893711904 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/15 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 0c68.0342.cb8f (bia 0c68.0342.cb8f)
            MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:04, output 00:00:00, output hang never
  Last clearing of "" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 3
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 86000 bits/sec, 61 packets/sec
     170484311 packets input, 74134804617 bytes, 0 no buffer
     Received 1031043 broadcasts (924939 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 924939 multicast, 0 pause input
     0 input packets with dribble condition detected
     2274468861 packets output, 408894647244 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/16 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 0c68.0342.cb90 (bia 0c68.0342.cb90)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:25, output 00:00:00, output hang never
  Last clearing of "" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 3
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 86000 bits/sec, 61 packets/sec
     6097211 packets input, 2147119100 bytes, 0 no buffer
     Received 654359 broadcasts (654239 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 654239 multicast, 0 pause input
     0 input packets with dribble condition detected
     2079481322 packets output, 294781988792 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/17 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 0c68.0342.cb91 (bia 0c68.0342.cb91)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
            Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:23, output 00:00:00, output hang never
  Last clearing of "" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 386329
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 86000 bits/sec, 61 packets/sec
     1775775 packets input, 244126057 bytes, 0 no buffer
     Received 553257 broadcasts (553167 multicasts)
     2 runts, 0 giants, 0 throttles 
     5 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 553167 multicast, 0 pause input
     0 input packets with dribble condition detected
     1803309195 packets output, 260122515283 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/18 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 0c68.0342.cb92 (bia 0c68.0342.cb92)
  MTU 1500 bytes, BW 10000 Kbit/sec, DLY 1000 usec, 
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
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/19 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 0c68.0342.cb93 (bia 0c68.0342.cb93)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
            ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:05, output 00:00:01, output hang never
  Last clearing of "" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 30000 bits/sec, 3 packets/sec
  5 minute output rate 465000 bits/sec, 46 packets/sec
     465749433 packets input, 155734989587 bytes, 0 no buffer
     Received 4227956 broadcasts (3303055 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 3303055 multicast, 0 pause input
     0 input packets with dribble condition detected
     979889929 packets output, 492758018593 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/20 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 0c68.0342.cb94 (bia 0c68.0342.cb94)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:19, output 00:00:01, output hang never
  Last clearing of "" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 5000 bits/sec, 3 packets/sec
  5 minute output rate 8000 bits/sec, 13 packets/sec
     690281195 packets input, 298184018678 bytes, 0 no buffer
     Received 4228145 broadcasts (3303046 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 3303046 multicast, 0 pause input
     0 input packets with dribble condition detected
     1289784538 packets output, 810109126316 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/21 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 0c68.0342.cb95 (bia 0c68.0342.cb95)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:08, output 00:00:01, output hang never
  Last clearing of "" counters never
            Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 3000 bits/sec, 2 packets/sec
  5 minute output rate 9000 bits/sec, 12 packets/sec
     1853749068 packets input, 650513591800 bytes, 0 no buffer
     Received 4228155 broadcasts (3303007 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 3303007 multicast, 0 pause input
     0 input packets with dribble condition detected
     4182180671 packets output, 4093163852341 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/22 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 0c68.0342.cb96 (bia 0c68.0342.cb96)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:10, output 00:00:01, output hang never
  Last clearing of "" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 2000 bits/sec, 2 packets/sec
  5 minute output rate 8000 bits/sec, 12 packets/sec
     511038864 packets input, 172499340179 bytes, 0 no buffer
     Received 4228107 broadcasts (3303061 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 3303061 multicast, 0 pause input
     0 input packets with dribble condition detected
     1158445956 packets output, 723926021858 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/23 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 0c68.0342.cb97 (bia 0c68.0342.cb97)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:04, output 00:00:00, output hang never
  Last clearing of "" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
            5 minute input rate 3000 bits/sec, 2 packets/sec
  5 minute output rate 8000 bits/sec, 12 packets/sec
     1001612464 packets input, 304974901295 bytes, 0 no buffer
     Received 4227991 broadcasts (3303048 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 3303048 multicast, 0 pause input
     0 input packets with dribble condition detected
     2162772447 packets output, 1751152930535 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/24 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 0c68.0342.cb98 (bia 0c68.0342.cb98)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output 00:00:00, output hang never
  Last clearing of "" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 28
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 1397000 bits/sec, 246 packets/sec
  5 minute output rate 146000 bits/sec, 56 packets/sec
     20772519912 packets input, 14849785985114 bytes, 0 no buffer
     Received 6621998267 broadcasts (1089792854 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 1089792854 multicast, 586 pause input
     0 input packets with dribble condition detected
     8319332477 packets output, 3157487356591 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/25 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 0c68.0342.cb99 (bia 0c68.0342.cb99)
  MTU 1500 bytes, BW 10000 Kbit/sec, DLY 1000 usec, 
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
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/26 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 0c68.0342.cb9a (bia 0c68.0342.cb9a)
  MTU 1500 bytes, BW 10000 Kbit/sec, DLY 1000 usec, 
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
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/27 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 0c68.0342.cb9b (bia 0c68.0342.cb9b)
  MTU 1500 bytes, BW 10000 Kbit/sec, DLY 1000 usec, 
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
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/28 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 0c68.0342.cb9c (bia 0c68.0342.cb9c)
  MTU 1500 bytes, BW 10000 Kbit/sec, DLY 1000 usec, 
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
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out""",
 'show inventory':"""NAME: "1", DESCR: "WS-C2960S-24PS-L"
PID: WS-C2960S-24PS-L  , VID: V04  , SN: FOC1721X3S9

""",
 'show interface counters':"""Port            InOctets    InUcastPkts    InMcastPkts    InBcastPkts 
Gi1/0/1        765787108        2624438         654245             51 
Gi1/0/2     462513512055     1435727794        3203012        2987804 
Gi1/0/3     139192436786      398095604        3203916        3051980 
Gi1/0/4     162861522740      408369008        3203638        3069480 
Gi1/0/5     154571700019      360341583        3203902        3066383 
Gi1/0/6     226971251212      378080864        3203892        3049969 
Gi1/0/7     195827632013      275659057        1984680        1590994 
Gi1/0/8                0              0              0              0 
Gi1/0/9       1314199860       13075854         550987         561147 
Gi1/0/10            3522              6              0              9 
Gi1/0/11     61740560877      102422496        1623462         270884 
Gi1/0/12       900512978              0              0       13164445 
Gi1/0/13     23106574520       65675887         744328          52266 
Gi1/0/14     32482740210       65492633         708104          42498 
Gi1/0/15     74134804617      169453268         924939         106104 
Gi1/0/16      2147119100        5442852         654239            120 
Gi1/0/17       244126057        1222518         553167             90 
Gi1/0/18               0              0              0              0 
Gi1/0/19    155734990853      461521484        3303055         924901 
Gi1/0/20    298184018848      686053051        3303046         925099 
Gi1/0/21    650513591926     1849520914        3303007         925148 
Gi1/0/22    172499340489      506810759        3303061         925046 
Gi1/0/23    304974901485      997384474        3303048         924944 
Gi1/0/24  14849786027854    14150521749     1089792888     5532205488 
Gi1/0/25               0              0              0              0 
Gi1/0/26               0              0              0              0 
Gi1/0/27               0              0              0              0 
Gi1/0/28               0              0              0              0 

Port           OutOctets   OutUcastPkts   OutMcastPkts   OutBcastPkts 
Gi1/0/1     292992462733      692997696      350434362     1032762826 
Gi1/0/2    3291811738728     2845088807      131414103      374083513 
Gi1/0/3     711280506275      694472777      131420263      374023732 
Gi1/0/4     615082123735      563537588      131421028      374006724 
Gi1/0/5     588982390746      546536665      131421138      374009949 
Gi1/0/6     673651032180      582001661      131420142      374026353 
Gi1/0/7     257545743732      255886672      131597409      375486312 
Gi1/0/8                0              0              0              0 
Gi1/0/9     220574004545      670368118      223695692      644446450 
Gi1/0/10           21485             12             55            119 
Gi1/0/11    409296527872      857676507      349898149     1032646541 
Gi1/0/12     32491087427        5387905       83389740      265975426 
Gi1/0/13    386422743492      796619495      350727386     1032665401 
Gi1/0/14    393893748535      797013416      350754005     1032679906 
Gi1/0/15    408894683739      891518518      350488989     1032461484 
Gi1/0/16    294782025287      696153525      350758048     1032569879 
Gi1/0/17    260122532511      676656094      285761988      840891185 
Gi1/0/18               0              0              0              0 
Gi1/0/19    492758020409      472308537      131419842      376161567 
Gi1/0/20    810109127711      782203200      131419951      376161401 
Gi1/0/21   4093163853574     3674599193      131420070      376161421 
Gi1/0/22    723926023091      650864465      131419981      376161523 
Gi1/0/23   1751152931704     1655190876      131419995      376161588 
Gi1/0/24   3157487473117     8218536733       65710986       35084927 
Gi1/0/25               0              0              0              0 
Gi1/0/26               0              0              0              0 
Gi1/0/27               0              0              0              0 
          
Port           OutOctets   OutUcastPkts   OutMcastPkts   OutBcastPkts 
Gi1/0/28               0              0              0              0 """,
 'show cdp nei detail':"""-------------------------
Device ID: ap-0521-2-R110E
Entry address(es): 
  IP address: 172.20.105.53
  IPv6 address: FE80::86B2:61FF:FEC1:D6B0  (link-local)
Platform: cisco AIR-CAP3702I-A-K9,  Capabilities: Trans-Bridge Source-Route-Bridge IGMP 
Interface: GigabitEthernet1/0/21,  Port ID (outgoing port): GigabitEthernet0
Holdtime : 170 sec

Version :
Cisco IOS Software, C3700 Software (AP3G2-K9W8-M), Version 15.3(3)JF10, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2019 by Cisco Systems, Inc.
Compiled Thu 13-Jun-19 18:51 by prod_rel_team

advertisement version: 2
Duplex: full
Power drawn: 16.800 Watts
Power request id: 1165, Power management id: 45
Power request levels are:16800 15400 13000 0 0 
Management address(es): 
  IP address: 172.20.105.53

-------------------------
Device ID: ap-0521-2-R149
Entry address(es): 
  IP address: 172.20.105.9
  IPv6 address: FE80::86B2:61FF:FE9B:D504  (link-local)
Platform: cisco AIR-CAP3702I-A-K9,  Capabilities: Trans-Bridge Source-Route-Bridge IGMP 
Interface: GigabitEthernet1/0/20,  Port ID (outgoing port): GigabitEthernet0
Holdtime : 131 sec

Version :
Cisco IOS Software, C3700 Software (AP3G2-K9W8-M), Version 15.3(3)JF10, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2019 by Cisco Systems, Inc.
Compiled Thu 13-Jun-19 18:51 by prod_rel_team

advertisement version: 2
Duplex: full
Power drawn: 16.800 Watts
Power request id: 1924, Power management id: 45
Power request levels are:16800 15400 13000 0 0 
Management address(es): 
  IP address: 172.20.105.9

-------------------------
Device ID: ap-0521-2-R130
Entry address(es): 
  IP address: 172.20.104.185
  IPv6 address: FE80::2E4F:52FF:FE1A:A590  (link-local)
Platform: cisco AIR-AP1815W-B-K9,  Capabilities: Router Trans-Bridge 
Interface: GigabitEthernet1/0/3,  Port ID (outgoing port): GigabitEthernet0
Holdtime : 135 sec

Version :
Cisco AP Software, ap1g5-k9w8 Version: 8.5.151.0
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 2014-2015 by Cisco Systems, Inc.
          
advertisement version: 2
Duplex: full
Power drawn: 8.600 Watts
Power request id: 56920, Power management id: 44
Power request levels are:8600 0 0 0 0 
Management address(es): 
  IP address: 172.20.104.185

-------------------------
Device ID: ap-0521-2-R200
Entry address(es): 
  IP address: 172.20.105.142
  IPv6 address: FE80::6EAB:5FF:FEED:1628  (link-local)
Platform: cisco AIR-AP1815W-B-K9,  Capabilities: Router Trans-Bridge 
Interface: GigabitEthernet1/0/5,  Port ID (outgoing port): GigabitEthernet0
Holdtime : 139 sec

Version :
Cisco AP Software, ap1g5-k9w8 Version: 8.5.151.0
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 2014-2015 by Cisco Systems, Inc.

advertisement version: 2
Duplex: full
Power drawn: 8.600 Watts
Power request id: 10981, Power management id: 43
Power request levels are:8600 0 0 0 0 
Management address(es): 
  IP address: 172.20.105.142

-------------------------
Device ID: ap-0521-2-R189
Entry address(es): 
  IP address: 172.20.105.146
  IPv6 address: FE80::86B2:61FF:FEC0:BEB0  (link-local)
Platform: cisco AIR-CAP3702I-A-K9,  Capabilities: Trans-Bridge Source-Route-Bridge IGMP 
Interface: GigabitEthernet1/0/19,  Port ID (outgoing port): GigabitEthernet0
Holdtime : 159 sec

Version :
Cisco IOS Software, C3700 Software (AP3G2-K9W8-M), Version 15.3(3)JF10, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2019 by Cisco Systems, Inc.
Compiled Thu 13-Jun-19 18:51 by prod_rel_team

advertisement version: 2
Duplex: full
Power drawn: 16.800 Watts
Power request id: 442, Power management id: 45
Power request levels are:16800 15400 13000 0 0 
Management address(es): 
  IP address: 172.20.105.146

-------------------------
Device ID: ap-0521-2-R177
Entry address(es): 
  IP address: 172.20.105.131
  IPv6 address: FE80::6E8B:D3FF:FE29:FA  (link-local)
          Platform: cisco AIR-AP3802I-B-K9,  Capabilities: Router Trans-Bridge 
Interface: GigabitEthernet1/0/2,  Port ID (outgoing port): GigabitEthernet0
Holdtime : 138 sec

Version :
Cisco AP Software, ap3g3-k9w8 Version: 8.5.151.0
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 2014-2015 by Cisco Systems, Inc.

advertisement version: 2
Duplex: full
Power drawn: 30.000 Watts
Power request id: 62736, Power management id: 39
Power request levels are:30000 15400 0 0 0 
Management address(es): 
  IP address: 172.20.105.131

-------------------------
Device ID: ap-0521-2-R161
Entry address(es): 
  IP address: 172.20.104.164
  IPv6 address: FE80::86B2:61FF:FEB9:8074  (link-local)
Platform: cisco AIR-CAP3702I-A-K9,  Capabilities: Trans-Bridge Source-Route-Bridge IGMP 
Interface: GigabitEthernet1/0/22,  Port ID (outgoing port): GigabitEthernet0
Holdtime : 167 sec

Version :
Cisco IOS Software, C3700 Software (AP3G2-K9W8-M), Version 15.3(3)JF10, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2019 by Cisco Systems, Inc.
Compiled Thu 13-Jun-19 18:51 by prod_rel_team

advertisement version: 2
Duplex: full
Power drawn: 16.800 Watts
Power request id: 38408, Power management id: 45
Power request levels are:16800 15400 13000 0 0 
Management address(es): 
  IP address: 172.20.104.164

-------------------------
Device ID: ap-0521-2-R143
Entry address(es): 
  IP address: 172.20.105.158
  IPv6 address: FE80::2E4F:52FF:FEB9:7128  (link-local)
Platform: cisco AIR-AP1815W-B-K9,  Capabilities: Router Trans-Bridge 
Interface: GigabitEthernet1/0/4,  Port ID (outgoing port): GigabitEthernet0
Holdtime : 178 sec

Version :
Cisco AP Software, ap1g5-k9w8 Version: 8.5.151.0
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 2014-2015 by Cisco Systems, Inc.

advertisement version: 2
Duplex: full
Power drawn: 8.600 Watts
Power request id: 9262, Power management id: 43
Power request levels are:8600 0 0 0 0 
          Management address(es): 
  IP address: 172.20.105.158

-------------------------
Device ID: ap-0521-2-R163
Entry address(es): 
  IP address: 172.20.104.187
  IPv6 address: FE80::C6F7:D5FF:FE14:2220  (link-local)
Platform: cisco AIR-AP1815W-B-K9,  Capabilities: Router Trans-Bridge 
Interface: GigabitEthernet1/0/6,  Port ID (outgoing port): GigabitEthernet0
Holdtime : 148 sec

Version :
Cisco AP Software, ap1g5-k9w8 Version: 8.5.151.0
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 2014-2015 by Cisco Systems, Inc.

advertisement version: 2
Duplex: full
Power drawn: 8.600 Watts
Power request id: 35692, Power management id: 43
Power request levels are:8600 0 0 0 0 
Management address(es): 
  IP address: 172.20.104.187

-------------------------
Device ID: ap-0521-2-R140
Entry address(es): 
  IP address: 172.20.105.249
  IPv6 address: FE80::86B2:61FF:FEC1:D7C4  (link-local)
Platform: cisco AIR-CAP3702I-A-K9,  Capabilities: Trans-Bridge Source-Route-Bridge IGMP 
Interface: GigabitEthernet1/0/23,  Port ID (outgoing port): GigabitEthernet0
Holdtime : 142 sec

Version :
Cisco IOS Software, C3700 Software (AP3G2-K9W8-M), Version 15.3(3)JF10, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2019 by Cisco Systems, Inc.
Compiled Thu 13-Jun-19 18:51 by prod_rel_team

advertisement version: 2
Duplex: full
Power drawn: 16.800 Watts
Power request id: 11649, Power management id: 45
Power request levels are:16800 15400 13000 0 0 
Management address(es): 
  IP address: 172.20.105.249


Total cdp entries displayed : 10""",
 'show module all':"""^
% Invalid input detected at '^' marker.
""",
 'show module':"""^
% Invalid input detected at '^' marker.
""",
 'show run | section snmp':"""snmp-server group NOCGrv3RO v3 priv read NOCViewRO access 70
snmp-server group NOCGrv3RO v3 auth context vlan- match prefix 
snmp-server group NOCGrv3RW v3 priv write NOCViewRW access 71
snmp-server view NOCViewRO internet included
snmp-server view NOCViewRW internet included
snmp-server location Bldg. 3701 Room 2w
snmp-server contact BC-1 Y-336099
snmp ifmib ifindex persist""",
 'show run | in snmp':"""snmp-server group NOCGrv3RO v3 priv read NOCViewRO access 70
snmp-server group NOCGrv3RO v3 auth context vlan- match prefix 
snmp-server group NOCGrv3RW v3 priv write NOCViewRW access 71
snmp-server view NOCViewRO internet included
snmp-server view NOCViewRW internet included
snmp-server location Bldg. 3701 Room 2w
snmp-server contact BC-1 Y-336099
snmp ifmib ifindex persist""",
 'show snmp user':"""User name: NONUserv3RO
Engine ID: 8000000903000C680342CB81
storage-type: nonvolatile	 active
Authentication Protocol: MD5
Privacy Protocol: DES
Group-name: NOCGrv3RW

User name: NONUserv3Rw
Engine ID: 8000000903000C680342CB81
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
    140 permit 10.71.24.16
    170 permit 10.71.24.19
    160 permit 10.71.24.18
    20 permit 172.20.150.100
    220 permit 10.71.24.25
    110 permit 10.71.24.13 (2417215 matches)
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
Extended IP access list 199
    10 permit tcp 155.98.253.0 0.0.0.255 any eq 22 (70 matches)
    20 permit tcp host 172.20.150.100 any eq 22
    30 permit tcp host 155.100.126.162 any eq 22
    40 permit tcp host 155.100.126.163 any eq 22
    50 permit tcp host 10.64.2.70 any eq 22
    60 permit tcp host 155.99.239.130 any eq 22
              70 permit tcp host 155.97.152.244 any eq 22
    80 permit tcp host 155.100.123.72 any eq 22
    90 permit tcp 155.99.254.128 0.0.0.127 any eq 22 (8 matches)
    100 permit tcp 155.98.164.192 0.0.0.31 any eq 22 (12 matches)
    110 permit tcp host 10.71.24.11 any eq 22
    120 permit tcp host 10.71.24.12 any eq 22
    130 permit tcp host 10.71.24.13 any eq 22 (94 matches)
    140 permit tcp host 10.71.24.14 any eq 22
    150 permit tcp host 10.71.24.15 any eq 22
    160 permit tcp host 10.71.24.16 any eq 22
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
    270 deny ip any any log
Extended IP access list CISCO-CWA-URL-REDIRECT-ACL
    100 deny udp any any eq domain
    101 deny tcp any any eq domain
    102 deny udp any eq bootps any
    103 deny udp any any eq bootpc
    104 deny udp any eq bootpc any
    105 permit tcp any any eq www
Extended IP access list preauth_ipv4_acl (per-user)
    10 permit udp any any eq domain
    20 permit tcp any any eq domain
    30 permit udp any eq bootps any
    40 permit udp any any eq bootpc
    50 permit udp any eq bootpc any
    60 deny ip any any
IPv6 access list preauth_ipv6_acl (per-user)
    permit udp any any eq domain sequence 10
    permit tcp any any eq domain sequence 20
    permit icmp any any nd-ns sequence 30
    permit icmp any any nd-na sequence 40
    permit icmp any any router-solicitation sequence 50
    permit icmp any any router-advertisement sequence 60
    permit icmp any any redirect sequence 70
    permit udp any eq 547 any eq 546 sequence 80
    permit udp any eq 546 any eq 547 sequence 90
    deny ipv6 any any sequence 100""",
 'show run | section logging':"""logging buffered notifications
logging console critical
logging facility local6
logging source-interface Vlan333
logging host 155.98.204.52
logging host 155.98.253.244
logging host 172.24.29.14
logging host 10.70.24.10""",
 'show run | in logging':"""logging buffered notifications
logging console critical
logging facility local6
logging source-interface Vlan333
logging host 155.98.204.52
logging host 155.98.253.244
logging host 172.24.29.14
logging host 10.70.24.10""",
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
   1    000c.db19.701b    DYNAMIC     Gi1/0/24
 333    0004.80eb.a884    DYNAMIC     Gi1/0/24
 333    0004.80eb.d8f4    DYNAMIC     Gi1/0/24
 333    0004.80ee.3be4    DYNAMIC     Gi1/0/24
 333    0004.80ee.6fd8    DYNAMIC     Gi1/0/24
 333    000c.db19.6fb8    DYNAMIC     Gi1/0/24
 333    000c.db19.701b    DYNAMIC     Gi1/0/24
 333    00c0.b755.d6a5    DYNAMIC     Gi1/0/24
 333    00c0.b763.0da6    DYNAMIC     Gi1/0/24
 333    00c0.b798.611c    DYNAMIC     Gi1/0/24
 333    00c0.b79b.9589    DYNAMIC     Gi1/0/24
 333    00c0.b7b3.28a3    DYNAMIC     Gi1/0/24
 333    00c0.b7b6.d0df    DYNAMIC     Gi1/0/24
 333    00c0.b7c8.5851    DYNAMIC     Gi1/0/24
 333    00c0.b7e2.281a    DYNAMIC     Gi1/0/24
 333    00c0.b7eb.479a    DYNAMIC     Gi1/0/24
 333    00c0.b7eb.47b0    DYNAMIC     Gi1/0/24
 333    00c0.b7ec.e6f1    DYNAMIC     Gi1/0/24
 333    00c0.b7ef.a89a    DYNAMIC     Gi1/0/24
 333    00c0.b7f0.c928    DYNAMIC     Gi1/0/24
 333    00c0.b7f0.caab    DYNAMIC     Gi1/0/24
 333    00c0.b7f1.17e6    DYNAMIC     Gi1/0/24
 333    00c0.b7f1.2128    DYNAMIC     Gi1/0/24
 333    00c0.b7f1.2136    DYNAMIC     Gi1/0/24
 333    00c0.b7f1.213f    DYNAMIC     Gi1/0/24
 333    00c0.b7f1.2142    DYNAMIC     Gi1/0/24
 333    00c0.b7f1.2149    DYNAMIC     Gi1/0/24
 333    00c0.b7f1.2151    DYNAMIC     Gi1/0/24
 333    00c0.b7f1.2158    DYNAMIC     Gi1/0/24
 333    00c0.b7f1.2166    DYNAMIC     Gi1/0/24
 333    00c0.b7f1.21b2    DYNAMIC     Gi1/0/24
 333    00c0.b7f4.96dd    DYNAMIC     Gi1/0/24
 333    bcf1.f260.79b3    DYNAMIC     Gi1/0/24
1040    0004.80eb.a884    DYNAMIC     Gi1/0/24
          1040    0004.80eb.d8f4    DYNAMIC     Gi1/0/24
1040    0004.80ee.3be4    DYNAMIC     Gi1/0/24
1040    0004.80ee.6fd8    DYNAMIC     Gi1/0/24
1040    000c.db19.6fb8    DYNAMIC     Gi1/0/24
1040    000c.db19.701b    DYNAMIC     Gi1/0/24
1040    0024.dd01.4334    DYNAMIC     Gi1/0/12
1040    0027.9048.1430    DYNAMIC     Gi1/0/24
1040    0035.1abf.e91c    DYNAMIC     Gi1/0/24
1040    0035.1ae5.b38c    DYNAMIC     Gi1/0/24
1040    00c8.8b28.d5a0    DYNAMIC     Gi1/0/24
1040    00eb.d510.4da0    DYNAMIC     Gi1/0/24
1040    00eb.d510.52f0    DYNAMIC     Gi1/0/24
1040    00ee.ab3f.5ab0    DYNAMIC     Gi1/0/24
1040    0462.7384.77dc    DYNAMIC     Gi1/0/24
1040    0462.73bd.9890    DYNAMIC     Gi1/0/24
1040    0462.73bd.b878    DYNAMIC     Gi1/0/24
1040    0462.73c0.54dc    DYNAMIC     Gi1/0/24
1040    0462.73c2.e3e8    DYNAMIC     Gi1/0/24
1040    0462.73c2.e8a0    DYNAMIC     Gi1/0/24
1040    0462.73c7.dccc    DYNAMIC     Gi1/0/24
1040    0462.73cb.c4a0    DYNAMIC     Gi1/0/24
1040    0462.73cb.c5bc    DYNAMIC     Gi1/0/24
1040    0462.73cb.c624    DYNAMIC     Gi1/0/24
1040    0462.73e1.ea70    DYNAMIC     Gi1/0/24
1040    0462.73e1.eaa0    DYNAMIC     Gi1/0/24
1040    0462.73e1.f040    DYNAMIC     Gi1/0/24
1040    0462.73e1.f0fc    DYNAMIC     Gi1/0/24
1040    0462.73e1.f108    DYNAMIC     Gi1/0/24
1040    0462.73e1.f224    DYNAMIC     Gi1/0/24
1040    0462.73e1.f4fc    DYNAMIC     Gi1/0/24
1040    0462.73e2.fe4c    DYNAMIC     Gi1/0/24
1040    0462.73e3.035c    DYNAMIC     Gi1/0/24
1040    0462.73e3.03d4    DYNAMIC     Gi1/0/24
1040    0462.73e3.0438    DYNAMIC     Gi1/0/24
1040    0462.73e3.0440    DYNAMIC     Gi1/0/24
1040    0462.73e3.049c    DYNAMIC     Gi1/0/24
1040    0462.73e3.0660    DYNAMIC     Gi1/0/24
1040    0462.73e8.09dc    DYNAMIC     Gi1/0/24
1040    0462.73e8.0dac    DYNAMIC     Gi1/0/24
1040    0462.73e8.0db4    DYNAMIC     Gi1/0/24
1040    0462.73e8.0ecc    DYNAMIC     Gi1/0/24
1040    0462.73e8.10b4    DYNAMIC     Gi1/0/24
1040    0462.73e8.1344    DYNAMIC     Gi1/0/24
1040    0462.73e8.140c    DYNAMIC     Gi1/0/24
1040    0462.73e8.df58    DYNAMIC     Gi1/0/24
1040    0462.73e8.e23c    DYNAMIC     Gi1/0/24
1040    0462.73e8.e610    DYNAMIC     Gi1/0/24
1040    0462.73f0.c9f4    DYNAMIC     Gi1/0/24
1040    0462.73f0.cd14    DYNAMIC     Gi1/0/24
1040    0462.73f0.d1d0    DYNAMIC     Gi1/0/24
1040    0462.73f0.d2a8    DYNAMIC     Gi1/0/24
1040    1c6a.7a39.9c14    DYNAMIC     Gi1/0/24
1040    2c4f.521a.83a0    DYNAMIC     Gi1/0/24
1040    2c4f.521a.8908    DYNAMIC     Gi1/0/24
1040    2c4f.521a.9180    DYNAMIC     Gi1/0/24
1040    2c4f.521a.94d8    DYNAMIC     Gi1/0/24
1040    2c4f.521a.9a98    DYNAMIC     Gi1/0/24
1040    2c4f.521a.9f08    DYNAMIC     Gi1/0/24
1040    2c4f.521a.a218    DYNAMIC     Gi1/0/24
          1040    2c4f.521a.a468    DYNAMIC     Gi1/0/24
1040    2c4f.521a.a590    DYNAMIC     Gi1/0/3
1040    2c4f.5249.32b8    DYNAMIC     Gi1/0/24
1040    2c4f.5249.36a8    DYNAMIC     Gi1/0/24
1040    2c4f.5249.37c0    DYNAMIC     Gi1/0/24
1040    2c4f.5249.3948    DYNAMIC     Gi1/0/24
1040    2c4f.5263.9a70    DYNAMIC     Gi1/0/24
1040    2c4f.5263.9aa0    DYNAMIC     Gi1/0/24
1040    2c4f.5263.a4a0    DYNAMIC     Gi1/0/24
1040    2c4f.52b9.7128    DYNAMIC     Gi1/0/4
1040    2c4f.52bb.2e38    DYNAMIC     Gi1/0/24
1040    2c4f.52bb.2f80    DYNAMIC     Gi1/0/24
1040    2c4f.52bb.3008    DYNAMIC     Gi1/0/24
1040    2c4f.52bb.30a8    DYNAMIC     Gi1/0/24
1040    3c51.0e3d.efea    DYNAMIC     Gi1/0/24
1040    3c51.0e40.cbce    DYNAMIC     Gi1/0/24
1040    3c51.0e60.4fe6    DYNAMIC     Gi1/0/24
1040    3c51.0e60.5550    DYNAMIC     Gi1/0/24
1040    3c51.0efa.6874    DYNAMIC     Gi1/0/24
1040    3c51.0efa.6878    DYNAMIC     Gi1/0/24
1040    3c51.0efa.68b4    DYNAMIC     Gi1/0/24
1040    5c5a.c715.524a    DYNAMIC     Gi1/0/24
1040    5c5a.c72c.5a22    DYNAMIC     Gi1/0/24
1040    5c5a.c72c.6a02    DYNAMIC     Gi1/0/24
1040    5c5a.c72c.6a0e    DYNAMIC     Gi1/0/24
1040    5c5a.c72c.6a38    DYNAMIC     Gi1/0/24
1040    5c5a.c7f0.74b0    DYNAMIC     Gi1/0/24
1040    6c8b.d328.fc18    DYNAMIC     Gi1/0/24
1040    6c8b.d328.fe3a    DYNAMIC     Gi1/0/24
1040    6c8b.d329.00fa    DYNAMIC     Gi1/0/2
1040    6c8b.d3aa.5622    DYNAMIC     Gi1/0/24
1040    6c8b.d3aa.72fa    DYNAMIC     Gi1/0/24
1040    6c8b.d3f1.6376    DYNAMIC     Gi1/0/24
1040    6c8b.d3fe.4714    DYNAMIC     Gi1/0/24
1040    6c8b.d3ff.b1e0    DYNAMIC     Gi1/0/24
1040    6cab.0580.e9b8    DYNAMIC     Gi1/0/24
1040    6cab.05ed.0c50    DYNAMIC     Gi1/0/24
1040    6cab.05ed.1628    DYNAMIC     Gi1/0/5
1040    6cab.05ed.1cc0    DYNAMIC     Gi1/0/24
1040    6cab.05ed.1ec8    DYNAMIC     Gi1/0/24
1040    7079.b317.697a    DYNAMIC     Gi1/0/24
1040    78ba.f989.dd2c    DYNAMIC     Gi1/0/24
1040    78bc.1ab3.b25a    DYNAMIC     Gi1/0/24
1040    78bc.1ab3.b960    DYNAMIC     Gi1/0/24
1040    78bc.1ab3.c19e    DYNAMIC     Gi1/0/24
1040    78bc.1ab3.c1ec    DYNAMIC     Gi1/0/24
1040    78bc.1adb.c15a    DYNAMIC     Gi1/0/24
1040    78bc.1adb.c3f2    DYNAMIC     Gi1/0/24
1040    84b2.616b.9510    DYNAMIC     Gi1/0/24
1040    84b2.6196.fbe0    DYNAMIC     Gi1/0/24
1040    84b2.619b.d504    DYNAMIC     Gi1/0/20
1040    84b2.61b0.4ecc    DYNAMIC     Gi1/0/24
1040    84b2.61b9.8074    DYNAMIC     Gi1/0/22
1040    84b2.61bf.a750    DYNAMIC     Gi1/0/24
1040    84b2.61c0.bb3c    DYNAMIC     Gi1/0/24
1040    84b2.61c0.bb48    DYNAMIC     Gi1/0/24
1040    84b2.61c0.beb0    DYNAMIC     Gi1/0/19
1040    84b2.61c1.d668    DYNAMIC     Gi1/0/24
1040    84b2.61c1.d6b0    DYNAMIC     Gi1/0/21
          1040    84b2.61c1.d7c4    DYNAMIC     Gi1/0/23
1040    84b2.61c1.d7e8    DYNAMIC     Gi1/0/24
1040    84b8.02af.d000    DYNAMIC     Gi1/0/24
1040    a0b4.395d.8596    DYNAMIC     Gi1/0/24
1040    a0b4.3978.d8b0    DYNAMIC     Gi1/0/24
1040    a0b4.3987.b0e4    DYNAMIC     Gi1/0/24
1040    a0b4.3987.ca8e    DYNAMIC     Gi1/0/24
1040    a0b4.398d.7244    DYNAMIC     Gi1/0/24
1040    a0b4.398d.7258    DYNAMIC     Gi1/0/24
1040    a0b4.398d.7260    DYNAMIC     Gi1/0/24
1040    a0b4.398d.7870    DYNAMIC     Gi1/0/24
1040    a0b4.398d.7a2a    DYNAMIC     Gi1/0/24
1040    a89d.2140.602c    DYNAMIC     Gi1/0/24
1040    a89d.216f.bb18    DYNAMIC     Gi1/0/24
1040    b00c.d13f.4019    DYNAMIC     Gi1/0/24
1040    bcf1.f260.79b3    DYNAMIC     Gi1/0/24
1040    c4f7.d514.0d58    DYNAMIC     Gi1/0/24
1040    c4f7.d514.0ee8    DYNAMIC     Gi1/0/24
1040    c4f7.d514.0f40    DYNAMIC     Gi1/0/24
1040    c4f7.d514.1be0    DYNAMIC     Gi1/0/24
1040    c4f7.d514.1c60    DYNAMIC     Gi1/0/24
1040    c4f7.d514.1d60    DYNAMIC     Gi1/0/24
1040    c4f7.d514.1e60    DYNAMIC     Gi1/0/24
1040    c4f7.d514.1eb8    DYNAMIC     Gi1/0/24
1040    c4f7.d514.2108    DYNAMIC     Gi1/0/24
1040    c4f7.d514.2168    DYNAMIC     Gi1/0/24
1040    c4f7.d514.2200    DYNAMIC     Gi1/0/24
1040    c4f7.d514.2208    DYNAMIC     Gi1/0/24
1040    c4f7.d514.2220    DYNAMIC     Gi1/0/6
1040    c4f7.d514.2308    DYNAMIC     Gi1/0/24
1040    c4f7.d514.23f8    DYNAMIC     Gi1/0/24
1040    c4f7.d514.2460    DYNAMIC     Gi1/0/24
1040    c4f7.d521.1db0    DYNAMIC     Gi1/0/24
1040    c4f7.d521.20a0    DYNAMIC     Gi1/0/24
1040    c4f7.d521.20f0    DYNAMIC     Gi1/0/24
1040    c4f7.d521.2290    DYNAMIC     Gi1/0/24
1040    c4f7.d521.2300    DYNAMIC     Gi1/0/24
1040    c4f7.d521.2658    DYNAMIC     Gi1/0/24
1040    dc8c.376e.32ba    DYNAMIC     Gi1/0/24
1040    dc8c.3778.f1a4    DYNAMIC     Gi1/0/24
1040    dc8c.3785.638a    DYNAMIC     Gi1/0/24
1040    dc8c.378e.2384    DYNAMIC     Gi1/0/24
1040    dc8c.37df.34e8    DYNAMIC     Gi1/0/24
1040    e4aa.5d00.0034    DYNAMIC     Gi1/0/24
1040    e4aa.5d00.0768    DYNAMIC     Gi1/0/24
1040    e4aa.5d00.0810    DYNAMIC     Gi1/0/24
1040    e4aa.5d00.092c    DYNAMIC     Gi1/0/24
1040    e4aa.5d00.0f34    DYNAMIC     Gi1/0/24
1040    e4aa.5d00.1070    DYNAMIC     Gi1/0/24
1040    e4aa.5d00.108c    DYNAMIC     Gi1/0/24
1040    e4aa.5d00.114c    DYNAMIC     Gi1/0/24
1040    e4aa.5d00.1428    DYNAMIC     Gi1/0/24
1040    e4aa.5d00.14d0    DYNAMIC     Gi1/0/24
1040    e4aa.5d00.155c    DYNAMIC     Gi1/0/24
1040    e4aa.5d00.165c    DYNAMIC     Gi1/0/24
1040    e4aa.5d00.16ac    DYNAMIC     Gi1/0/24
1040    e4aa.5d00.16b4    DYNAMIC     Gi1/0/24
1040    e4aa.5d00.188c    DYNAMIC     Gi1/0/24
1040    e4aa.5d00.1cb8    DYNAMIC     Gi1/0/24
          1040    e4aa.5d06.7954    DYNAMIC     Gi1/0/24
1040    e4aa.5d06.7a08    DYNAMIC     Gi1/0/24
1040    e4aa.5d06.7a44    DYNAMIC     Gi1/0/24
1040    e4aa.5d06.8b2c    DYNAMIC     Gi1/0/24
1040    e4aa.5d08.263c    DYNAMIC     Gi1/0/24
1040    e4aa.5d08.27f4    DYNAMIC     Gi1/0/24
1040    e4aa.5d09.07dc    DYNAMIC     Gi1/0/24
1040    e4aa.5d13.2950    DYNAMIC     Gi1/0/24
1040    e4aa.5d13.295c    DYNAMIC     Gi1/0/24
1040    e4aa.5d13.29c4    DYNAMIC     Gi1/0/24
1040    e4aa.5d13.29dc    DYNAMIC     Gi1/0/24
1040    e4aa.5d13.2ad8    DYNAMIC     Gi1/0/24
1040    e4aa.5d13.2b00    DYNAMIC     Gi1/0/24
1040    e4aa.5d13.315c    DYNAMIC     Gi1/0/24
1040    e4aa.5d13.357c    DYNAMIC     Gi1/0/24
1040    e4aa.5d6c.b0d8    DYNAMIC     Gi1/0/24
1040    e4aa.5d6d.f67c    DYNAMIC     Gi1/0/24
1040    e4aa.5d77.adf4    DYNAMIC     Gi1/0/24
1040    e4aa.5d81.5f24    DYNAMIC     Gi1/0/24
1040    e4aa.5db2.e0a4    DYNAMIC     Gi1/0/24
1040    e4aa.5dcd.2ca0    DYNAMIC     Gi1/0/24
1040    e4aa.5dcd.2f0c    DYNAMIC     Gi1/0/24
1040    e4aa.5dcd.3070    DYNAMIC     Gi1/0/24
1040    e4aa.5dd2.b5b4    DYNAMIC     Gi1/0/24
1040    e4aa.5dd7.c1d4    DYNAMIC     Gi1/0/24
1040    e4aa.5dd7.cc54    DYNAMIC     Gi1/0/24
1040    e4aa.5dd7.e82c    DYNAMIC     Gi1/0/24
1040    e4aa.5dd7.ea98    DYNAMIC     Gi1/0/24
1040    e4aa.5dd7.ed64    DYNAMIC     Gi1/0/24
1040    e4aa.5dd9.595c    DYNAMIC     Gi1/0/24
1040    e4aa.5df3.f6dc    DYNAMIC     Gi1/0/24
1040    fc5b.3991.238e    DYNAMIC     Gi1/0/24
1040    fc5b.3991.52fa    DYNAMIC     Gi1/0/24
 702    0004.80eb.a884    DYNAMIC     Gi1/0/24
 702    0004.f2fd.d594    DYNAMIC     Gi1/0/24
 702    0004.f2ff.7889    DYNAMIC     Gi1/0/24
 702    000c.db19.6fb8    DYNAMIC     Gi1/0/24
 702    000c.db19.701b    DYNAMIC     Gi1/0/24
 702    24d9.2148.ea32    DYNAMIC     Gi1/0/14
 702    50cd.22b3.929c    DYNAMIC     Gi1/0/13
 702    6416.7f3e.a823    DYNAMIC     Gi1/0/24
 702    6416.7f82.d88b    DYNAMIC     Gi1/0/24
 702    a009.ed0a.6b04    DYNAMIC     Gi1/0/11
 702    b447.5eb4.b024    DYNAMIC     Gi1/0/24
 702    bcf1.f260.79b3    DYNAMIC     Gi1/0/24
 702    c057.bc28.b4df    DYNAMIC     Gi1/0/16
 702    c81f.ea9a.757d    DYNAMIC     Gi1/0/15
 702    c81f.ea9a.75cb    DYNAMIC     Gi1/0/1
 702    c81f.ea9b.0d71    DYNAMIC     Gi1/0/17
 382    0000.ba30.110c    DYNAMIC     Gi1/0/24
 382    0004.80eb.a884    DYNAMIC     Gi1/0/24
 382    0004.80eb.d8f4    DYNAMIC     Gi1/0/24
 382    0004.80ee.3be4    DYNAMIC     Gi1/0/24
 382    0004.80ee.6fd8    DYNAMIC     Gi1/0/24
 382    0005.1baa.6902    DYNAMIC     Gi1/0/24
 382    0007.327d.18ed    DYNAMIC     Gi1/0/24
 382    0007.327f.a220    DYNAMIC     Gi1/0/24
 382    000c.c601.ae4c    DYNAMIC     Gi1/0/24
 382    000c.c601.b81e    DYNAMIC     Gi1/0/24
           382    000c.c601.b8fc    DYNAMIC     Gi1/0/24
 382    000c.db19.6fb8    DYNAMIC     Gi1/0/24
 382    000c.db19.701b    DYNAMIC     Gi1/0/24
 382    0011.0a1d.cd00    DYNAMIC     Gi1/0/24
 382    0014.388a.fb71    DYNAMIC     Gi1/0/24
 382    0015.5d0f.6600    DYNAMIC     Gi1/0/24
 382    0015.5d0f.6601    DYNAMIC     Gi1/0/24
 382    0017.0887.5776    DYNAMIC     Gi1/0/24
 382    0018.7da9.fb9a    DYNAMIC     Gi1/0/24
 382    001b.7816.bf9b    DYNAMIC     Gi1/0/24
 382    001d.9722.01d6    DYNAMIC     Gi1/0/24
 382    001d.9722.01d9    DYNAMIC     Gi1/0/24
 382    001d.9722.01da    DYNAMIC     Gi1/0/24
 382    001d.9722.01ea    DYNAMIC     Gi1/0/24
 382    001d.9722.01f0    DYNAMIC     Gi1/0/24
 382    001d.9722.01f2    DYNAMIC     Gi1/0/24
 382    001d.9722.01f4    DYNAMIC     Gi1/0/24
 382    001e.8fd3.2162    DYNAMIC     Gi1/0/24
 382    001f.c69c.ac8b    DYNAMIC     Gi1/0/24
 382    0021.5a7d.9890    DYNAMIC     Gi1/0/24
 382    0025.9099.184a    DYNAMIC     Gi1/0/24
 382    0050.b61b.fd68    DYNAMIC     Gi1/0/24
 382    0050.b627.83d5    DYNAMIC     Gi1/0/24
 382    0060.e065.1506    DYNAMIC     Gi1/0/24
 382    00bb.c1cb.c9f9    DYNAMIC     Gi1/0/24
 382    00e0.4c78.1369    DYNAMIC     Gi1/0/24
 382    0462.7322.7504    DYNAMIC     Gi1/0/24
 382    0462.733a.0008    DYNAMIC     Gi1/0/24
 382    0462.738d.d530    DYNAMIC     Gi1/0/24
 382    0462.73bd.ca50    DYNAMIC     Gi1/0/24
 382    0462.73c2.e884    DYNAMIC     Gi1/0/24
 382    0462.73e1.d664    DYNAMIC     Gi1/0/24
 382    0462.73e8.111c    DYNAMIC     Gi1/0/24
 382    0462.73f0.cf98    DYNAMIC     Gi1/0/24
 382    0492.264c.422a    DYNAMIC     Gi1/0/24
 382    04d4.c4aa.f03a    DYNAMIC     Gi1/0/24
 382    04d9.f51f.13e2    DYNAMIC     Gi1/0/24
 382    04d9.f51f.db32    DYNAMIC     Gi1/0/24
 382    0862.662e.8c72    DYNAMIC     Gi1/0/24
 382    0862.6634.1052    DYNAMIC     Gi1/0/24
 382    0862.6635.a675    DYNAMIC     Gi1/0/24
 382    0862.6635.a687    DYNAMIC     Gi1/0/24
 382    0862.6635.a8f8    DYNAMIC     Gi1/0/24
 382    0862.6637.212d    DYNAMIC     Gi1/0/24
 382    0862.6637.2841    DYNAMIC     Gi1/0/24
 382    0862.66c5.8cbc    DYNAMIC     Gi1/0/24
 382    0866.98f0.4d12    DYNAMIC     Gi1/0/24
 382    0c4d.e9c6.7572    DYNAMIC     Gi1/0/24
 382    0c9d.92c8.6631    DYNAMIC     Gi1/0/24
 382    0cc4.7a72.8ee4    DYNAMIC     Gi1/0/24
 382    0cc4.7a72.a0dc    DYNAMIC     Gi1/0/24
 382    1060.4b15.c255    DYNAMIC     Gi1/0/24
 382    1062.e517.eef6    DYNAMIC     Gi1/0/24
 382    107b.4445.8f74    DYNAMIC     Gi1/0/24
 382    107b.444e.ece2    DYNAMIC     Gi1/0/24
 382    107b.444e.ed5e    DYNAMIC     Gi1/0/24
 382    107b.444e.ed60    DYNAMIC     Gi1/0/24
 382    107b.444e.ef0b    DYNAMIC     Gi1/0/24
 382    107b.44a3.668c    DYNAMIC     Gi1/0/24
           382    107b.44a3.697e    DYNAMIC     Gi1/0/24
 382    107b.44a3.69ff    DYNAMIC     Gi1/0/24
 382    107b.44a3.6a97    DYNAMIC     Gi1/0/24
 382    10bf.484e.52ea    DYNAMIC     Gi1/0/24
 382    10dd.b1db.8c8c    DYNAMIC     Gi1/0/24
 382    10e7.c600.d38e    DYNAMIC     Gi1/0/24
 382    10e7.c606.12d2    DYNAMIC     Gi1/0/24
 382    10e7.c606.1619    DYNAMIC     Gi1/0/24
 382    10e7.c60c.38a7    DYNAMIC     Gi1/0/24
 382    10e7.c60c.38bd    DYNAMIC     Gi1/0/24
 382    10e7.c60c.38e0    DYNAMIC     Gi1/0/24
 382    10e7.c60c.3a85    DYNAMIC     Gi1/0/24
 382    10e7.c610.c5d0    DYNAMIC     Gi1/0/24
 382    10e7.c610.c676    DYNAMIC     Gi1/0/24
 382    10e7.c661.c5b9    DYNAMIC     Gi1/0/24
 382    1458.d040.c61f    DYNAMIC     Gi1/0/24
 382    14dd.a97c.5e22    DYNAMIC     Gi1/0/24
 382    14dd.a97e.6e2f    DYNAMIC     Gi1/0/24
 382    1831.bf6b.caee    DYNAMIC     Gi1/0/24
 382    1831.bfb0.d01b    DYNAMIC     Gi1/0/24
 382    1831.bfb4.c98e    DYNAMIC     Gi1/0/24
 382    1831.bfde.3f22    DYNAMIC     Gi1/0/24
 382    1831.bfde.3f7d    DYNAMIC     Gi1/0/24
 382    1831.bfde.402b    DYNAMIC     Gi1/0/24
 382    1831.bfe0.6708    DYNAMIC     Gi1/0/24
 382    1860.2405.2628    DYNAMIC     Gi1/0/24
 382    1860.2421.a026    DYNAMIC     Gi1/0/24
 382    1860.2421.a056    DYNAMIC     Gi1/0/24
 382    1860.2424.16db    DYNAMIC     Gi1/0/24
 382    1860.2426.c4e3    DYNAMIC     Gi1/0/24
 382    1860.246d.9fa6    DYNAMIC     Gi1/0/24
 382    1860.247e.cb84    DYNAMIC     Gi1/0/24
 382    1860.2488.04bd    DYNAMIC     Gi1/0/24
 382    1860.24cb.61b1    DYNAMIC     Gi1/0/24
 382    1c1a.dfb2.2305    DYNAMIC     Gi1/0/24
 382    1c1b.0d66.a5ec    DYNAMIC     Gi1/0/24
 382    1c1b.0de7.7e64    DYNAMIC     Gi1/0/24
 382    1c1b.0dea.106b    DYNAMIC     Gi1/0/24
 382    1c1b.0deb.03b0    DYNAMIC     Gi1/0/24
 382    1c87.2c70.f8f7    DYNAMIC     Gi1/0/24
 382    1cb7.2caf.2c48    DYNAMIC     Gi1/0/24
 382    1cb7.2cb1.693e    DYNAMIC     Gi1/0/24
 382    1cc1.de84.c366    DYNAMIC     Gi1/0/24
 382    2426.4249.e27f    DYNAMIC     Gi1/0/24
 382    244b.fe59.6933    DYNAMIC     Gi1/0/24
 382    24be.05e7.492c    DYNAMIC     Gi1/0/24
 382    24d9.2148.ea32    DYNAMIC     Gi1/0/14
 382    2880.230e.74cf    DYNAMIC     Gi1/0/24
 382    2884.fafd.87e4    DYNAMIC     Gi1/0/24
 382    2c44.fd04.5e14    DYNAMIC     Gi1/0/24
 382    2c4d.5453.4a82    DYNAMIC     Gi1/0/24
 382    2c4d.5457.a4e7    DYNAMIC     Gi1/0/24
 382    2c4d.5457.a62c    DYNAMIC     Gi1/0/24
 382    2c4d.5458.3898    DYNAMIC     Gi1/0/24
 382    2c4f.5263.a468    DYNAMIC     Gi1/0/24
 382    2c56.dcd5.1881    DYNAMIC     Gi1/0/24
 382    2c56.dcfc.2641    DYNAMIC     Gi1/0/24
 382    2cea.7f38.333f    DYNAMIC     Gi1/0/24
 382    2cfd.a171.43b0    DYNAMIC     Gi1/0/24
           382    2cfd.a171.4440    DYNAMIC     Gi1/0/24
 382    2cfd.a1bc.a286    DYNAMIC     Gi1/0/24
 382    2cfd.a1e3.da3c    DYNAMIC     Gi1/0/24
 382    305a.3a45.58d3    DYNAMIC     Gi1/0/24
 382    305a.3a7b.99ba    DYNAMIC     Gi1/0/24
 382    305a.3a7d.abeb    DYNAMIC     Gi1/0/24
 382    305a.3a7f.1f6e    DYNAMIC     Gi1/0/24
 382    305a.3a82.17f2    DYNAMIC     Gi1/0/24
 382    305a.3a82.19c1    DYNAMIC     Gi1/0/24
 382    305a.3a82.21e4    DYNAMIC     Gi1/0/24
 382    308d.99a9.ab13    DYNAMIC     Gi1/0/24
 382    3448.ed97.1397    DYNAMIC     Gi1/0/24
 382    3464.a96f.bb28    DYNAMIC     Gi1/0/24
 382    38c9.863d.8eda    DYNAMIC     Gi1/0/24
 382    38c9.8641.9a29    DYNAMIC     Gi1/0/24
 382    38d5.4718.e972    DYNAMIC     Gi1/0/24
 382    38d5.4718.e975    DYNAMIC     Gi1/0/24
 382    38d5.4718.eaf4    DYNAMIC     Gi1/0/24
 382    38f9.d314.a4d3    DYNAMIC     Gi1/0/24
 382    3c51.0efa.6896    DYNAMIC     Gi1/0/24
 382    3c52.82be.8744    DYNAMIC     Gi1/0/24
 382    3c7d.0a01.8fd9    DYNAMIC     Gi1/0/24
 382    3ca8.2af5.5b09    DYNAMIC     Gi1/0/24
 382    3ca8.2afb.a6d6    DYNAMIC     Gi1/0/24
 382    4016.7ea8.e8ab    DYNAMIC     Gi1/0/24
 382    4016.7eac.c625    DYNAMIC     Gi1/0/24
 382    40b0.3418.098c    DYNAMIC     Gi1/0/24
 382    40b0.341a.4fb8    DYNAMIC     Gi1/0/24
 382    40b0.341a.541a    DYNAMIC     Gi1/0/24
 382    40b0.343e.4d4a    DYNAMIC     Gi1/0/24
 382    40b0.349e.6c75    DYNAMIC     Gi1/0/24
 382    480f.cf38.715d    DYNAMIC     Gi1/0/24
 382    480f.cf3a.aad4    DYNAMIC     Gi1/0/24
 382    480f.cf3a.ab16    DYNAMIC     Gi1/0/24
 382    480f.cf3b.93e7    DYNAMIC     Gi1/0/24
 382    480f.cf3d.ebb4    DYNAMIC     Gi1/0/24
 382    480f.cf45.29f8    DYNAMIC     Gi1/0/24
 382    480f.cf5f.17a9    DYNAMIC     Gi1/0/24
 382    480f.cfc7.fa8a    DYNAMIC     Gi1/0/24
 382    484d.7edb.46ab    DYNAMIC     Gi1/0/24
 382    484d.7ef9.97d8    DYNAMIC     Gi1/0/24
 382    48ba.4edc.adbb    DYNAMIC     Gi1/0/24
 382    48ba.4edc.f8ff    DYNAMIC     Gi1/0/24
 382    4ced.fb45.1dab    DYNAMIC     Gi1/0/24
 382    4ced.fb94.3c85    DYNAMIC     Gi1/0/24
 382    4ced.fbbf.63c5    DYNAMIC     Gi1/0/24
 382    4ced.fbc2.3067    DYNAMIC     Gi1/0/24
 382    4ced.fbc8.1b4f    DYNAMIC     Gi1/0/24
 382    4ced.fbc8.1bf6    DYNAMIC     Gi1/0/24
 382    4ced.fbc8.1c19    DYNAMIC     Gi1/0/24
 382    500f.f53c.8cd9    DYNAMIC     Gi1/0/24
 382    5046.5d73.08ef    DYNAMIC     Gi1/0/24
 382    5065.f350.3004    DYNAMIC     Gi1/0/24
 382    50cd.22b3.929c    DYNAMIC     Gi1/0/13
 382    54bf.6485.d6c3    DYNAMIC     Gi1/0/24
 382    5820.b14d.45a4    DYNAMIC     Gi1/0/24
 382    5838.790d.40b7    DYNAMIC     Gi1/0/24
 382    6045.cb84.1fd2    DYNAMIC     Gi1/0/24
 382    6045.cb84.2281    DYNAMIC     Gi1/0/24
           382    6045.cb85.699d    DYNAMIC     Gi1/0/24
 382    6400.6a88.eca3    DYNAMIC     Gi1/0/24
 382    6416.7fba.00d5    DYNAMIC     Gi1/0/24
 382    6451.0626.9883    DYNAMIC     Gi1/0/24
 382    6451.065e.da6e    DYNAMIC     Gi1/0/24
 382    645a.edf5.5d04    DYNAMIC     Gi1/0/24
 382    6470.0211.ad8c    DYNAMIC     Gi1/0/24
 382    68ab.8a82.65dc    DYNAMIC     Gi1/0/24
 382    68ab.8a82.661e    DYNAMIC     Gi1/0/24
 382    6c02.e0f2.939c    DYNAMIC     Gi1/0/24
 382    6c2b.59c9.2fb5    DYNAMIC     Gi1/0/24
 382    6c2b.59c9.78dd    DYNAMIC     Gi1/0/24
 382    6c2b.59c9.880f    DYNAMIC     Gi1/0/24
 382    6c2b.59c9.8b77    DYNAMIC     Gi1/0/24
 382    6c2b.59c9.8f4c    DYNAMIC     Gi1/0/24
 382    6c2b.59c9.921d    DYNAMIC     Gi1/0/24
 382    6c2b.59c9.b3c3    DYNAMIC     Gi1/0/24
 382    6c2b.59c9.b4f8    DYNAMIC     Gi1/0/24
 382    6c2b.59c9.bd9c    DYNAMIC     Gi1/0/24
 382    6c2b.59cc.a39b    DYNAMIC     Gi1/0/24
 382    6c2b.59d3.e39b    DYNAMIC     Gi1/0/24
 382    6c2b.59d5.3f23    DYNAMIC     Gi1/0/24
 382    6c2b.59d5.40f0    DYNAMIC     Gi1/0/24
 382    6c2b.59ea.fa84    DYNAMIC     Gi1/0/24
 382    6c2b.59f8.cbf9    DYNAMIC     Gi1/0/24
 382    6c3b.e507.bed6    DYNAMIC     Gi1/0/24
 382    6c8b.d3a0.3322    DYNAMIC     Gi1/0/24
 382    6cab.05ed.0c58    DYNAMIC     Gi1/0/24
 382    6cc2.1711.6c17    DYNAMIC     Gi1/0/24
 382    6cc2.1726.22f2    DYNAMIC     Gi1/0/24
 382    6cc2.1726.42c0    DYNAMIC     Gi1/0/24
 382    6cc2.1729.2043    DYNAMIC     Gi1/0/24
 382    704d.7b6a.d0ff    DYNAMIC     Gi1/0/24
 382    704d.7b6a.d1c8    DYNAMIC     Gi1/0/24
 382    704d.7b71.d448    DYNAMIC     Gi1/0/24
 382    704d.7b71.d69a    DYNAMIC     Gi1/0/24
 382    705a.0f13.434a    DYNAMIC     Gi1/0/24
 382    705a.0f37.a554    DYNAMIC     Gi1/0/24
 382    705a.0fa5.cb29    DYNAMIC     Gi1/0/24
 382    705a.0fa7.f136    DYNAMIC     Gi1/0/24
 382    708b.cd9d.b2bd    DYNAMIC     Gi1/0/24
 382    708b.cd9d.b2ec    DYNAMIC     Gi1/0/24
 382    708b.cda6.ca62    DYNAMIC     Gi1/0/24
 382    708b.cda6.ca65    DYNAMIC     Gi1/0/24
 382    708b.cda6.d78b    DYNAMIC     Gi1/0/24
 382    7478.27be.1e59    DYNAMIC     Gi1/0/24
 382    7488.bbb8.167a    DYNAMIC     Gi1/0/24
 382    74d0.2b25.e2bb    DYNAMIC     Gi1/0/24
 382    74d0.2b25.e309    DYNAMIC     Gi1/0/24
 382    74d0.2b26.5f27    DYNAMIC     Gi1/0/24
 382    74d0.2b29.349b    DYNAMIC     Gi1/0/24
 382    781c.5acc.4d49    DYNAMIC     Gi1/0/24
 382    787b.8aaf.0a7b    DYNAMIC     Gi1/0/24
 382    787b.8ab3.ff9b    DYNAMIC     Gi1/0/24
 382    787b.8ae2.ab3c    DYNAMIC     Gi1/0/24
 382    788c.7714.c77a    DYNAMIC     Gi1/0/24
 382    80c1.6e97.92ec    DYNAMIC     Gi1/0/24
 382    80e8.2c06.e303    DYNAMIC     Gi1/0/24
 382    84a9.3e4f.6c1a    DYNAMIC     Gi1/0/24
           382    8cdc.d420.457e    DYNAMIC     Gi1/0/24
 382    8cdc.d42e.0695    DYNAMIC     Gi1/0/24
 382    8cdc.d43c.8e3c    DYNAMIC     Gi1/0/24
 382    8cdc.d446.9534    DYNAMIC     Gi1/0/24
 382    8cdc.d446.9729    DYNAMIC     Gi1/0/24
 382    8cdc.d44d.84a5    DYNAMIC     Gi1/0/24
 382    8cdc.d461.a3d2    DYNAMIC     Gi1/0/24
 382    8cec.4bb0.eb28    DYNAMIC     Gi1/0/24
 382    8cec.4bd7.f540    DYNAMIC     Gi1/0/24
 382    906c.ac82.d486    DYNAMIC     Gi1/0/24
 382    9457.a517.0f15    DYNAMIC     Gi1/0/24
 382    9457.a5d1.ab4b    DYNAMIC     Gi1/0/24
 382    94c6.9111.1e6c    DYNAMIC     Gi1/0/24
 382    94c6.9113.d93c    DYNAMIC     Gi1/0/24
 382    985a.ebdd.8448    DYNAMIC     Gi1/0/24
 382    98e7.43bd.d95c    DYNAMIC     Gi1/0/24
 382    9c5c.8e6e.42f4    DYNAMIC     Gi1/0/24
 382    9c5c.8e6e.435e    DYNAMIC     Gi1/0/24
 382    9c5c.8e6e.4586    DYNAMIC     Gi1/0/24
 382    9cb6.5415.9ed5    DYNAMIC     Gi1/0/24
 382    9ceb.e8a1.5396    DYNAMIC     Gi1/0/24
 382    a009.ed0a.6b04    DYNAMIC     Gi1/0/11
 382    a048.1c68.118a    DYNAMIC     Gi1/0/24
 382    a08c.fddc.7607    DYNAMIC     Gi1/0/24
 382    a08c.fdeb.fec0    DYNAMIC     Gi1/0/24
 382    a0b4.398d.78b0    DYNAMIC     Gi1/0/24
 382    a0dd.e539.5718    DYNAMIC     Gi1/0/24
 382    a0dd.e539.b4ec    DYNAMIC     Gi1/0/24
 382    a0dd.e5fc.9478    DYNAMIC     Gi1/0/24
 382    a4bb.6d4d.3bdb    DYNAMIC     Gi1/0/24
 382    a4bb.6d4d.4a77    DYNAMIC     Gi1/0/24
 382    a4bb.6d4e.dba6    DYNAMIC     Gi1/0/24
 382    a4bb.6d77.9cdf    DYNAMIC     Gi1/0/24
 382    a4bb.6d7a.2081    DYNAMIC     Gi1/0/24
 382    a4bb.6d80.82ee    DYNAMIC     Gi1/0/24
 382    a4bb.6dab.e912    DYNAMIC     Gi1/0/24
 382    a4bb.6daf.3a30    DYNAMIC     Gi1/0/24
 382    a4bb.6db6.2521    DYNAMIC     Gi1/0/24
 382    a4bb.6dc8.fdfd    DYNAMIC     Gi1/0/24
 382    a4bb.6dda.b50d    DYNAMIC     Gi1/0/24
 382    a85e.4557.e9ef    DYNAMIC     Gi1/0/24
 382    a85e.4557.ea7d    DYNAMIC     Gi1/0/24
 382    a85e.4557.ea92    DYNAMIC     Gi1/0/24
 382    a860.b602.d191    DYNAMIC     Gi1/0/24
 382    a860.b61d.e47a    DYNAMIC     Gi1/0/24
 382    a860.b633.65d5    DYNAMIC     Gi1/0/24
 382    a860.b635.5683    DYNAMIC     Gi1/0/24
 382    a860.b635.57d5    DYNAMIC     Gi1/0/24
 382    a8a1.5960.4ec6    DYNAMIC     Gi1/0/24
 382    ac22.0bc2.5eb2    DYNAMIC     Gi1/0/24
 382    ac87.a314.6562    DYNAMIC     Gi1/0/24
 382    ac87.a33b.0ff2    DYNAMIC     Gi1/0/24
 382    ace2.d301.0ffd    DYNAMIC     Gi1/0/24
 382    ace2.d301.6a38    DYNAMIC     Gi1/0/24
 382    ace2.d304.5102    DYNAMIC     Gi1/0/24
 382    ace2.d306.cc81    DYNAMIC     Gi1/0/24
 382    ace2.d308.5074    DYNAMIC     Gi1/0/24
 382    ace2.d30d.9238    DYNAMIC     Gi1/0/24
 382    ace2.d310.fd12    DYNAMIC     Gi1/0/24
           382    ace2.d311.198c    DYNAMIC     Gi1/0/24
 382    b05a.dac2.bd18    DYNAMIC     Gi1/0/24
 382    b05c.da66.53e3    DYNAMIC     Gi1/0/24
 382    b06e.bf2e.e2a9    DYNAMIC     Gi1/0/24
 382    b06e.bf34.aa58    DYNAMIC     Gi1/0/24
 382    b06e.bf7f.8375    DYNAMIC     Gi1/0/24
 382    b06e.bf7f.838d    DYNAMIC     Gi1/0/24
 382    b06e.bfcd.43a6    DYNAMIC     Gi1/0/24
 382    b07b.2506.b4f8    DYNAMIC     Gi1/0/24
 382    b42e.99ad.c9d9    DYNAMIC     Gi1/0/24
 382    b4b6.86c7.d64a    DYNAMIC     Gi1/0/24
 382    bcb1.81a5.97cf    DYNAMIC     Gi1/0/24
 382    bcf1.f260.79b3    DYNAMIC     Gi1/0/24
 382    c03e.ba8f.9ce0    DYNAMIC     Gi1/0/24
 382    c057.bc28.b4df    DYNAMIC     Gi1/0/16
 382    c49d.edea.5047    DYNAMIC     Gi1/0/24
 382    c4f7.d514.17c8    DYNAMIC     Gi1/0/24
 382    c4f7.d514.1970    DYNAMIC     Gi1/0/24
 382    c81f.ea9a.757d    DYNAMIC     Gi1/0/15
 382    c81f.ea9a.75cb    DYNAMIC     Gi1/0/1
 382    c81f.ea9b.0d71    DYNAMIC     Gi1/0/17
 382    c82a.1455.b557    DYNAMIC     Gi1/0/24
 382    c860.00c7.9d61    DYNAMIC     Gi1/0/24
 382    c860.00c7.a097    DYNAMIC     Gi1/0/24
 382    c8d3.ffa1.de40    DYNAMIC     Gi1/0/24
 382    c8d3.ffa4.1bcd    DYNAMIC     Gi1/0/24
 382    c8d3.ffa4.1c85    DYNAMIC     Gi1/0/24
 382    c8d3.ffa4.1cd5    DYNAMIC     Gi1/0/24
 382    c8d3.ffae.e549    DYNAMIC     Gi1/0/24
 382    c8d3.ffb3.edab    DYNAMIC     Gi1/0/24
 382    c8d3.ffb3.ee08    DYNAMIC     Gi1/0/24
 382    c8d3.ffb5.429b    DYNAMIC     Gi1/0/24
 382    c8d3.ffb5.6608    DYNAMIC     Gi1/0/24
 382    c8d3.ffb7.f583    DYNAMIC     Gi1/0/24
 382    c8d3.ffb7.f6e8    DYNAMIC     Gi1/0/24
 382    c8d3.ffb8.bd29    DYNAMIC     Gi1/0/24
 382    c8d3.ffba.2327    DYNAMIC     Gi1/0/24
 382    c8d3.ffba.23e0    DYNAMIC     Gi1/0/24
 382    c8d3.ffba.36bc    DYNAMIC     Gi1/0/24
 382    c8d3.ffbc.4332    DYNAMIC     Gi1/0/24
 382    d017.c2d1.9b7f    DYNAMIC     Gi1/0/24
 382    d017.c2d1.a2bc    DYNAMIC     Gi1/0/24
 382    d45d.6455.245a    DYNAMIC     Gi1/0/24
 382    d478.9bbe.bb70    DYNAMIC     Gi1/0/24
 382    d4c9.efff.3c34    DYNAMIC     Gi1/0/24
 382    d89e.f334.4be8    DYNAMIC     Gi1/0/24
 382    d89e.f334.4ef8    DYNAMIC     Gi1/0/24
 382    dc4a.3e6b.85c9    DYNAMIC     Gi1/0/24
 382    dc4a.3e6b.85fb    DYNAMIC     Gi1/0/24
 382    dc4a.3e82.21a7    DYNAMIC     Gi1/0/24
 382    dc4a.3e86.a58e    DYNAMIC     Gi1/0/24
 382    dc4a.3e9b.0c89    DYNAMIC     Gi1/0/24
 382    e03f.4948.2866    DYNAMIC     Gi1/0/24
 382    e03f.4948.2884    DYNAMIC     Gi1/0/24
 382    e03f.4948.2970    DYNAMIC     Gi1/0/24
 382    e03f.4985.0717    DYNAMIC     Gi1/0/24
 382    e0d5.5eb0.b469    DYNAMIC     Gi1/0/24
 382    e0d5.5eb5.e8f0    DYNAMIC     Gi1/0/24
 382    e0d5.5ed9.e7e6    DYNAMIC     Gi1/0/24
           382    e454.e85c.43b4    DYNAMIC     Gi1/0/24
 382    e454.e85c.e4ac    DYNAMIC     Gi1/0/24
 382    e454.e85d.64cd    DYNAMIC     Gi1/0/24
 382    e454.e863.cb7c    DYNAMIC     Gi1/0/24
 382    e454.e876.f58c    DYNAMIC     Gi1/0/24
 382    e454.e876.f64a    DYNAMIC     Gi1/0/24
 382    e454.e88c.5e63    DYNAMIC     Gi1/0/24
 382    e454.e895.97b8    DYNAMIC     Gi1/0/24
 382    e454.e8b5.23f1    DYNAMIC     Gi1/0/24
 382    e454.e8da.6db2    DYNAMIC     Gi1/0/24
 382    e454.e8da.9e6a    DYNAMIC     Gi1/0/24
 382    e454.e8db.3ceb    DYNAMIC     Gi1/0/24
 382    e454.e8db.6a5b    DYNAMIC     Gi1/0/24
 382    e454.e8db.6afd    DYNAMIC     Gi1/0/24
 382    e4aa.5d00.07bc    DYNAMIC     Gi1/0/24
 382    e4aa.5d00.0ba4    DYNAMIC     Gi1/0/24
 382    e4aa.5d00.0e04    DYNAMIC     Gi1/0/24
 382    e4aa.5d09.0a48    DYNAMIC     Gi1/0/24
 382    e4aa.5d73.d28c    DYNAMIC     Gi1/0/24
 382    e4aa.5dac.5a0c    DYNAMIC     Gi1/0/24
 382    e4b9.7af9.c6c9    DYNAMIC     Gi1/0/24
 382    e4b9.7af9.c9b6    DYNAMIC     Gi1/0/24
 382    e4e7.49a4.dc6a    DYNAMIC     Gi1/0/24
 382    ec8e.b56e.799f    DYNAMIC     Gi1/0/24
 382    ec8e.b579.8e3c    DYNAMIC     Gi1/0/24
 382    ec8e.b59b.b428    DYNAMIC     Gi1/0/24
 382    ecb1.d75c.608f    DYNAMIC     Gi1/0/24
 382    ecb1.d76e.efaa    DYNAMIC     Gi1/0/24
 382    f02f.74dd.cac7    DYNAMIC     Gi1/0/24
 382    f079.5939.4891    DYNAMIC     Gi1/0/24
 382    f079.5939.4892    DYNAMIC     Gi1/0/24
 382    f430.b92b.5ed1    DYNAMIC     Gi1/0/24
 382    f430.b974.1c6a    DYNAMIC     Gi1/0/24
 382    f430.b9ef.1c39    DYNAMIC     Gi1/0/24
 382    f44d.3067.da05    DYNAMIC     Gi1/0/24
 382    f44d.306a.6f33    DYNAMIC     Gi1/0/24
 382    f44d.306b.d796    DYNAMIC     Gi1/0/24
 382    f481.39e6.875b    DYNAMIC     Gi1/0/24
 382    f4db.e6b2.5114    DYNAMIC     Gi1/0/24
 382    f4db.e6bf.d91c    DYNAMIC     Gi1/0/24
 382    f4db.e6f4.c200    DYNAMIC     Gi1/0/24
 382    f4db.e6fd.46e8    DYNAMIC     Gi1/0/24
 382    f4db.e6ff.4244    DYNAMIC     Gi1/0/24
 382    f4db.e6ff.552c    DYNAMIC     Gi1/0/24
 382    f832.e49b.b9b7    DYNAMIC     Gi1/0/24
 382    f832.e49e.9d63    DYNAMIC     Gi1/0/24
 382    f832.e49e.9d64    DYNAMIC     Gi1/0/24
 382    f832.e49f.097a    DYNAMIC     Gi1/0/24
 382    f832.e4a2.1f49    DYNAMIC     Gi1/0/24
 382    fc15.b476.bb32    DYNAMIC     Gi1/0/24
 382    fc3f.db02.948b    DYNAMIC     Gi1/0/24
 382    fc3f.db02.94a8    DYNAMIC     Gi1/0/24
 382    fc3f.db06.7cfa    DYNAMIC     Gi1/0/24
 382    fc3f.db0d.7fb4    DYNAMIC     Gi1/0/24
 382    fc3f.db0f.7fa0    DYNAMIC     Gi1/0/24
 382    fc3f.db11.5b08    DYNAMIC     Gi1/0/24
 382    fc3f.db53.3305    DYNAMIC     Gi1/0/24
 111    0004.80eb.a884    DYNAMIC     Gi1/0/24
 111    000c.db19.6fb8    DYNAMIC     Gi1/0/24
           111    000c.db19.701b    DYNAMIC     Gi1/0/24
 111    bcf1.f260.79b3    DYNAMIC     Gi1/0/24
 111    c81f.ea9a.7610    DYNAMIC     Gi1/0/9
Total Mac Addresses for this criterion: 706""",
 'show run | section tacacs':"""aaa group server tacacs+ NOC-TAC
 server name TAC-EBC
 server name TAC-SECONDARY
tacacs server TAC-EBC
 address ipv4 172.31.17.180
 key 7 0522420A08084B2B39070E53
tacacs server TAC-SECONDARY
 address ipv4 10.64.32.5
 key 7 022F405E22420A036C4C1058""",
 'show run | in tacacs':"""aaa group server tacacs+ NOC-TAC
tacacs server TAC-EBC
tacacs server TAC-SECONDARY""",
 'show power inline':"""Module   Available     Used     Remaining
          (Watts)     (Watts)    (Watts) 
------   ---------   --------   ---------
1           370.0      193.0       177.0
Interface Admin  Oper       Power   Device              Class Max
                            (Watts)                            
--------- ------ ---------- ------- ------------------- ----- ----
Gi1/0/1   auto   on         4.0     Ieee PD             1     30.0 
Gi1/0/2   auto   on         30.0    AIR-AP3802I-B-K9    4     30.0 
Gi1/0/3   auto   on         8.6     AIR-AP1815W-B-K9    4     30.0 
Gi1/0/4   auto   on         8.6     AIR-AP1815W-B-K9    4     30.0 
Gi1/0/5   auto   on         8.6     AIR-AP1815W-B-K9    4     30.0 
Gi1/0/6   auto   on         8.6     AIR-AP1815W-B-K9    4     30.0 
Gi1/0/7   auto   on         8.6     Ieee PD             4     30.0 
Gi1/0/8   auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/9   auto   on         4.0     Ieee PD             1     30.0 
Gi1/0/10  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/11  auto   on         4.0     Ieee PD             1     30.0 
Gi1/0/12  auto   on         4.0     Ieee PD             1     30.0 
Gi1/0/13  auto   on         4.0     Ieee PD             1     30.0 
Gi1/0/14  auto   on         4.0     Ieee PD             1     30.0 
Gi1/0/15  auto   on         4.0     Ieee PD             1     30.0 
Gi1/0/16  auto   on         4.0     Ieee PD             1     30.0 
Gi1/0/17  auto   on         4.0     Ieee PD             1     30.0 
Gi1/0/18  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/19  auto   on         16.8    AIR-CAP3702I-A-K9   4     30.0 
Gi1/0/20  auto   on         16.8    AIR-CAP3702I-A-K9   4     30.0 
Gi1/0/21  auto   on         16.8    AIR-CAP3702I-A-K9   4     30.0 
Gi1/0/22  auto   on         16.8    AIR-CAP3702I-A-K9   4     30.0 
Gi1/0/23  auto   on         16.8    AIR-CAP3702I-A-K9   4     30.0 
Gi1/0/24  auto   off        0.0     n/a                 n/a   30.0 """,
 'show environment all':"""^
% Invalid input detected at '^' marker.
""",
}
