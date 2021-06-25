ip_address = '155.101.238.248'
software = 'software'
hardware = 'hardware'
read_results = {
 'show version':"""Cisco IOS Software, C3560CX Software (C3560CX-UNIVERSALK9-M), Version 15.2(3)E3, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2016 by Cisco Systems, Inc.
Compiled Wed 13-Jan-16 23:08 by prod_rel_team

ROM: Bootstrap program is C3560CX boot loader
BOOTLDR: C3560CX Boot Loader (C3560CX-HBOOT-M) Version 15.2(3r)E2, RELEASE SOFTWARE (fc2)

sx2-179ebc-227-ebc uptime is 2 years, 16 weeks, 1 day, 4 hours, 18 minutes
System returned to ROM by power-on
System restarted at 10:15:01 MST Tue Mar 5 2019
System image file is "flash:/c3560cx-universalk9-mz.152-3.E3/c3560cx-universalk9-mz.152-3.E3.bin"
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

License Level: ipbase
License Type: Default. No valid license found.
Next reload license Level: ipbase

cisco WS-C3560CX-8PC-S (APM86XXX) processor (revision G0) with 524288K bytes of memory.
Processor board ID FOC2011Z1DQ
Last reset from power-on
2 Virtual Ethernet interfaces
12 Gigabit Ethernet interfaces
The password-recovery mechanism is enabled.

512K bytes of flash-simulated non-volatile configuration memory.
Base ethernet MAC Address       : 00:CA:E5:1C:EA:00
Motherboard assembly number     : 73-16471-04
Power supply part number        : 341-0675-02
Motherboard serial number       : FOC20103515
Power supply serial number      : LIT19510NHN
Model revision number           : G0
Motherboard revision number     : A0
Model number                    : WS-C3560CX-8PC-S
System serial number            : FOC2011Z1DQ
Top Assembly Part Number        : 68-5359-02
Top Assembly Revision Number    : D0
Version ID                      : V02
CLEI Code Number                : CMM1S10DRA
Hardware Board Revision Number  : 0x02


          Switch Ports Model                     SW Version            SW Image                 
------ ----- -----                     ----------            ----------               
*    1 12    WS-C3560CX-8PC-S          15.2(3)E3             C3560CX-UNIVERSALK9-M    


Configuration register is 0xF
""",
 'show run':"""Building configuration...

Current configuration : 9180 bytes
!
! Last configuration change at 11:03:54 MDT Mon Apr 26 2021 by noc-orionncm
! NVRAM config last updated at 20:42:06 MDT Sun Jun 20 2021 by noc-orionncm
!
version 15.2
no service pad
service timestamps debug datetime msec localtime
service timestamps log datetime msec localtime
service password-encryption
!
hostname sx2-179ebc-227-ebc
!
boot-start-marker
boot-end-marker
!
logging buffered notifications
logging console critical
enable secret 5 $1$w1lV$.Q07O/ZQlTnK7CcDa8BPf1
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
system mtu routing 1500
no ip source-route
!
!
ip dhcp snooping
ip domain-name net.utah.edu
ip name-server 172.20.120.20
ip device tracking probe delay 10
vtp domain vtp-179ebc
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
spanning-tree mode rapid-pvst
spanning-tree extend system-id
!
!
!
!
vlan internal allocation policy ascending
!
vlan 201
 name ebc-179ebc-voip
!
vlan 466
 name ebc-179ebc-trapeze-wireless
!
vlan 627
 name ebc-179ebc-facil
!
vlan 650
 name ebc-302hightemp-hvac
!
vlan 699
 name 086mlib-hvac
!
vlan 820
 name lib-086mlib-m
!
vlan 829
 name ebc-179ebc-m
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
interface GigabitEthernet0/1
 description #AP
 switchport access vlan 466
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet0/2
 description #AP
           switchport access vlan 466
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet0/3
 description #AP
 switchport access vlan 466
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet0/4
 description #AP
 switchport access vlan 466
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet0/5
 description #AP
 switchport access vlan 466
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet0/6
 description #AP
 switchport access vlan 466
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet0/7
 description #AP
 switchport access vlan 466
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet0/8
 description #AP
 switchport access vlan 466
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet0/9
 no keepalive
!
interface GigabitEthernet0/10
 description g0/10:sx1-179-227:g1/1/1
 switchport mode trunk
 no keepalive
!
interface GigabitEthernet0/11
!
interface GigabitEthernet0/12
 description g0/12:sx1-179-227:t1/1/7
 switchport mode trunk
!
interface Vlan1
 no ip address
 no ip route-cache
 shutdown
!
          interface Vlan829
 description ebc-179ebc-m
 ip address 155.101.238.248 255.255.255.240
 no ip route-cache
!
ip default-gateway 155.101.238.241
ip forward-protocol nd
no ip http server
no ip http secure-server
!
ip ssh version 2
!
!
ip sla enable reaction-alerts
logging facility local6
logging source-interface Vlan829
logging host 172.24.29.14
logging host 10.71.24.11
logging host 155.98.253.244
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
snmp-server location Bldg. 179 Room 227
snmp-server contact BC-18004553 Y-
snmp ifmib ifindex persist
tacacs server TAC-EBC
           address ipv4 172.31.17.180
 key 7 0522420A08084B2B39070E53
tacacs server TAC-SECONDARY
 address ipv4 10.64.32.5
 key 7 09650A0C304112302B0E1D6B
!
!
privilege exec level 1 show configuration
privilege exec level 1 show
banner login ^C
sx2-179ebc-227-ebc

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
 password 7 13300313030E45797F
 login authentication console
 stopbits 1
line vty 0 4
 access-class 199 in
 exec-timeout 30 0
 password 7 073A354D460B585643
 transport input ssh
line vty 5 15
 access-class 199 in
 exec-timeout 30 0
 password 7 073A354D460B585643
 transport input ssh
!
ntp server time.utah.edu
!
end
""",
 'show int status':"""Port      Name               Status       Vlan       Duplex  Speed Type 
Gi0/1     #AP                connected    466        a-full a-1000 10/100/1000BaseTX
Gi0/2     #AP                connected    466        a-full a-1000 10/100/1000BaseTX
Gi0/3     #AP                connected    466        a-full a-1000 10/100/1000BaseTX
Gi0/4     #AP                connected    466        a-full a-1000 10/100/1000BaseTX
Gi0/5     #AP                notconnect   466          auto   auto 10/100/1000BaseTX
Gi0/6     #AP                notconnect   466          auto   auto 10/100/1000BaseTX
Gi0/7     #AP                notconnect   466          auto   auto 10/100/1000BaseTX
Gi0/8     #AP                notconnect   466          auto   auto 10/100/1000BaseTX
Gi0/9                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi0/10    g0/10:sx1-179-227: connected    trunk      a-full a-1000 10/100/1000BaseTX
Gi0/11                       notconnect   1            auto   auto Not Present
Gi0/12    g0/12:sx1-179-227: notconnect   1            auto   auto Not Present""",
 'show run | section interface':"""interface GigabitEthernet0/1
 description #AP
 switchport access vlan 466
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet0/2
 description #AP
 switchport access vlan 466
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet0/3
 description #AP
 switchport access vlan 466
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet0/4
 description #AP
 switchport access vlan 466
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet0/5
 description #AP
 switchport access vlan 466
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet0/6
 description #AP
 switchport access vlan 466
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet0/7
 description #AP
 switchport access vlan 466
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet0/8
 description #AP
 switchport access vlan 466
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet0/9
 no keepalive
interface GigabitEthernet0/10
 description g0/10:sx1-179-227:g1/1/1
 switchport mode trunk
 no keepalive
interface GigabitEthernet0/11
interface GigabitEthernet0/12
 description g0/12:sx1-179-227:t1/1/7
 switchport mode trunk
interface Vlan1
 no ip address
 no ip route-cache
 shutdown
interface Vlan829
 description ebc-179ebc-m
 ip address 155.101.238.248 255.255.255.240
 no ip route-cache
logging source-interface Vlan829""",
 'show run | in interface':"""interface GigabitEthernet0/1
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
interface Vlan1
interface Vlan829
logging source-interface Vlan829""",
 'show interface link':"""^
% Invalid input detected at '^' marker.
""",
 'show interface':"""Vlan1 is administratively down, line protocol is down 
  Hardware is EtherSVI, address is 00ca.e51c.ea40 (bia 00ca.e51c.ea40)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
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
     0 output errors, 1 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Vlan829 is up, line protocol is up 
  Hardware is EtherSVI, address is 00ca.e51c.ea41 (bia 00ca.e51c.ea41)
  Description: ebc-179ebc-m
  Internet address is 155.101.238.248/28
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
  5 minute input rate 1000 bits/sec, 1 packets/sec
  5 minute output rate 1000 bits/sec, 1 packets/sec
     90767503 packets input, 11612639822 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     38392847 packets output, 9877396457 bytes, 0 underruns
     0 output errors, 2 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet0/1 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 00ca.e51c.ea01 (bia 00ca.e51c.ea01)
  Description: #AP
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:17, output 00:00:00, output hang never
  Last clearing of "" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
            Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 151000 bits/sec, 92 packets/sec
     734470862 packets input, 409501714881 bytes, 0 no buffer
     Received 5694034 broadcasts (5478165 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 5478165 multicast, 0 pause input
     0 input packets with dribble condition detected
     42536999428 packets output, 12410904831665 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet0/2 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 00ca.e51c.ea02 (bia 00ca.e51c.ea02)
  Description: #AP
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:09, output 00:00:00, output hang never
  Last clearing of "" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 2000 bits/sec, 1 packets/sec
  5 minute output rate 157000 bits/sec, 93 packets/sec
     361926858 packets input, 212046871100 bytes, 0 no buffer
     Received 5694412 broadcasts (5478566 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 5478566 multicast, 0 pause input
     0 input packets with dribble condition detected
     42152105616 packets output, 11945821560548 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet0/3 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 00ca.e51c.ea03 (bia 00ca.e51c.ea03)
  Description: #AP
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:01, output 00:00:00, output hang never
  Last clearing of "" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
            Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 151000 bits/sec, 92 packets/sec
     96309608 packets input, 23581316470 bytes, 0 no buffer
     Received 5686229 broadcasts (5478397 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 5478397 multicast, 0 pause input
     0 input packets with dribble condition detected
     29149110982 packets output, 7974059123719 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet0/4 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 00ca.e51c.ea04 (bia 00ca.e51c.ea04)
  Description: #AP
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:13, output 00:00:00, output hang never
  Last clearing of "" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 151000 bits/sec, 92 packets/sec
     49107024 packets input, 12996974156 bytes, 0 no buffer
     Received 5697913 broadcasts (5479568 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 5479568 multicast, 0 pause input
     0 input packets with dribble condition detected
     41592061843 packets output, 11481607974100 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet0/5 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00ca.e51c.ea05 (bia 00ca.e51c.ea05)
  Description: #AP
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
GigabitEthernet0/6 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00ca.e51c.ea06 (bia 00ca.e51c.ea06)
  Description: #AP
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
GigabitEthernet0/7 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00ca.e51c.ea07 (bia 00ca.e51c.ea07)
  Description: #AP
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
GigabitEthernet0/8 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00ca.e51c.ea08 (bia 00ca.e51c.ea08)
  Description: #AP
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
GigabitEthernet0/9 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00ca.e51c.ea09 (bia 00ca.e51c.ea09)
  MTU 1500 bytes, BW 10000 Kbit/sec, DLY 1000 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not set
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
GigabitEthernet0/10 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 00ca.e51c.ea0a (bia 00ca.e51c.ea0a)
  Description: g0/10:sx1-179-227:g1/1/1
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not set
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output 00:00:00, output hang never
  Last clearing of "" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 177000 bits/sec, 118 packets/sec
  5 minute output rate 8000 bits/sec, 7 packets/sec
     55718783558 packets input, 16683902630085 bytes, 0 no buffer
     Received 2629797899 broadcasts (1826644564 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 1826644564 multicast, 0 pause input
     0 input packets with dribble condition detected
     1449531151 packets output, 682682814974 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet0/11 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00ca.e51c.ea0b (bia 00ca.e51c.ea0b)
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
GigabitEthernet0/12 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00ca.e51c.ea0c (bia 00ca.e51c.ea0c)
  Description: g0/12:sx1-179-227:t1/1/7
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
 'show inventory':"""NAME: "1", DESCR: "WS-C3560CX-8PC-S"
PID: WS-C3560CX-8PC-S  , VID: V02  , SN: FOC2011Z1DQ

""",
 'show interface counters':"""Port            InOctets    InUcastPkts    InMcastPkts    InBcastPkts 
Gi0/1       409501714881      728776828        5478165         215869 
Gi0/2       212046871316      356232447        5478566         215846 
Gi0/3        23581316628       90623381        5478397         207832 
Gi0/4        12996974220       43409111        5479569         218345 
Gi0/5                  0              0              0              0 
Gi0/6                  0              0              0              0 
Gi0/7                  0              0              0              0 
Gi0/8                  0              0              0              0 
Gi0/9                  0              0              0              0 
Gi0/10    16683902630085     1549378107    53366252116      803153335 
Gi0/11                 0              0              0              0 
Gi0/12                 0              0              0              0 

Port           OutOctets   OutUcastPkts   OutMcastPkts   OutBcastPkts 
Gi0/1     12410904848710      906585063    41582325514       48088936 
Gi0/2     11945821585705      518966086    41585051445       48088176 
Gi0/3      7974059140922       58847120    29042167930       48096019 
Gi0/4     11481607991145       45808046    41498168815       48085067 
Gi0/5                  0              0              0              0 
Gi0/6                  0              0              0              0 
Gi0/7                  0              0              0              0 
Gi0/8                  0              0              0              0 
Gi0/9                  0              0              0              0 
Gi0/10      682682814974     1257434258      191240720         856173 
Gi0/11                 0              0              0              0 
Gi0/12                 0              0              0              0 """,
 'show cdp nei detail':"""-------------------------
Device ID: ap-0179-1-112
Entry address(es): 
  IP address: 172.31.28.144
  IPv6 address: FE80::3A90:A5FF:FE78:1754  (link-local)
Platform: cisco AIR-AP3802I-B-K9,  Capabilities: Router Trans-Bridge 
Interface: GigabitEthernet0/1,  Port ID (outgoing port): GigabitEthernet0
Holdtime : 132 sec

Version :
Cisco AP Software, ap3g3-k9w8 Version: 8.10.151.0
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 2014-2015 by Cisco Systems, Inc.

advertisement version: 2
Duplex: full
Power drawn: 29.900 Watts
Power request id: 37046, Power management id: 18
Power request levels are:29900 15400 0 0 0 
Management address(es): 
  IP address: 172.31.28.144

-------------------------
Device ID: ap-0179-1-113
Entry address(es): 
  IP address: 172.31.28.113
  IPv6 address: FE80::72DF:2FFF:FE04:D960  (link-local)
Platform: cisco AIR-AP3802I-B-K9,  Capabilities: Router Trans-Bridge 
Interface: GigabitEthernet0/4,  Port ID (outgoing port): GigabitEthernet0
Holdtime : 128 sec

Version :
Cisco AP Software, ap3g3-k9w8 Version: 8.10.151.0
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 2014-2015 by Cisco Systems, Inc.

advertisement version: 2
Duplex: full
Power drawn: 29.900 Watts
Power request id: 37782, Power management id: 20
Power request levels are:29900 15400 0 0 0 
Management address(es): 
  IP address: 172.31.28.113

-------------------------
Device ID: sx1-179ebc-227-ebc.net.utah.edu
Entry address(es): 
  IP address: 155.101.238.247
Platform: cisco C9300-48U,  Capabilities: Switch IGMP 
Interface: GigabitEthernet0/10,  Port ID (outgoing port): TenGigabitEthernet1/1/7
Holdtime : 151 sec

Version :
Cisco IOS Software [Gibraltar], Catalyst L3 Switch Software (CAT9K_IOSXE), Version 16.12.4, RELEASE SOFTWARE (fc5)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2020 by Cisco Systems, Inc.
Compiled Thu 09-Jul-20 21:49 by mcpre

advertisement version: 2
          VTP Management Domain: 'vtp-179ebc'
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 155.101.238.247

-------------------------
Device ID: ap-0179-1-114b
Entry address(es): 
  IP address: 172.31.28.98
  IPv6 address: FE80::3A90:A5FF:FE78:1760  (link-local)
Platform: cisco AIR-AP3802I-B-K9,  Capabilities: Router Trans-Bridge 
Interface: GigabitEthernet0/2,  Port ID (outgoing port): GigabitEthernet0
Holdtime : 168 sec

Version :
Cisco AP Software, ap3g3-k9w8 Version: 8.10.151.0
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 2014-2015 by Cisco Systems, Inc.

advertisement version: 2
Duplex: full
Power drawn: 29.900 Watts
Power request id: 9735, Power management id: 15
Power request levels are:29900 15400 0 0 0 
Management address(es): 
  IP address: 172.31.28.98

-------------------------
Device ID: ap-0179-1-114a
Entry address(es): 
  IP address: 172.31.28.121
  IPv6 address: FE80::3A90:A5FF:FE5E:5BF2  (link-local)
Platform: cisco AIR-AP3802I-B-K9,  Capabilities: Router Trans-Bridge 
Interface: GigabitEthernet0/3,  Port ID (outgoing port): GigabitEthernet0
Holdtime : 137 sec

Version :
Cisco AP Software, ap3g3-k9w8 Version: 8.10.151.0
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 2014-2015 by Cisco Systems, Inc.

advertisement version: 2
Duplex: full
Power drawn: 29.900 Watts
Power request id: 19646, Power management id: 24
Power request levels are:29900 15400 0 0 0 
Management address(es): 
  IP address: 172.31.28.121


Total cdp entries displayed : 5""",
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
snmp-server location Bldg. 179 Room 227
snmp-server contact BC-18004553 Y-
snmp ifmib ifindex persist""",
 'show run | in snmp':"""snmp-server group NOCGrv3RO v3 priv read NOCViewRO access 70
snmp-server group NOCGrv3RO v3 auth context vlan- match prefix 
snmp-server group NOCGrv3RW v3 priv write NOCViewRW access 71
snmp-server view NOCViewRO internet included
snmp-server view NOCViewRW internet included
snmp-server location Bldg. 179 Room 227
snmp-server contact BC-18004553 Y-
snmp ifmib ifindex persist""",
 'show snmp user':"""User name: NONUserv3RO
Engine ID: 80000009030000CAE51CEA01
storage-type: nonvolatile	 active
Authentication Protocol: MD5
Privacy Protocol: DES
Group-name: NOCGrv3RW

User name: NONUserv3Rw
Engine ID: 80000009030000CAE51CEA01
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
    170 permit 10.71.24.19 (1658795 matches)
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
Extended IP access list 199
    10 permit tcp 155.98.253.0 0.0.0.255 any eq 22 (70 matches)
    20 permit tcp host 172.20.150.100 any eq 22
    30 permit tcp host 155.100.126.162 any eq 22
    40 permit tcp host 155.100.126.163 any eq 22
    50 permit tcp host 10.64.2.70 any eq 22
    60 permit tcp host 155.99.239.130 any eq 22
              70 permit tcp host 155.97.152.244 any eq 22
    80 permit tcp host 155.100.123.72 any eq 22
    90 permit tcp 155.99.254.128 0.0.0.127 any eq 22 (4 matches)
    100 permit tcp 155.98.164.192 0.0.0.31 any eq 22 (10 matches)
    110 permit tcp host 10.71.24.11 any eq 22
    120 permit tcp host 10.71.24.12 any eq 22
    130 permit tcp host 10.71.24.13 any eq 22
    140 permit tcp host 10.71.24.14 any eq 22
    150 permit tcp host 10.71.24.15 any eq 22
    160 permit tcp host 10.71.24.16 any eq 22
    170 permit tcp host 10.71.24.17 any eq 22
    180 permit tcp host 10.71.24.18 any eq 22
    190 permit tcp host 10.71.24.19 any eq 22 (84 matches)
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
logging source-interface Vlan829
logging host 172.24.29.14
logging host 10.71.24.11
logging host 155.98.253.244""",
 'show run | in logging':"""logging buffered notifications
logging console critical
logging facility local6
logging source-interface Vlan829
logging host 172.24.29.14
logging host 10.71.24.11
logging host 155.98.253.244""",
 'show mac address-table':"""Mac Address Table
-------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
 All    0100.0ccc.cccc    STATIC      CPU
 All    0100.0ccc.cccd    STATIC      CPU
 All    0100.0ccd.cddc    STATIC      CPU
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
   1    68ca.e436.11bb    DYNAMIC     Gi0/10
 466    0000.0c9f.f1d2    DYNAMIC     Gi0/10
 466    003a.9c3f.ffc1    DYNAMIC     Gi0/10
 466    003a.9c40.5ec1    DYNAMIC     Gi0/10
 466    00a7.4295.5bf4    DYNAMIC     Gi0/10
 466    0462.7366.0fb4    DYNAMIC     Gi0/10
 466    0462.7368.2bc8    DYNAMIC     Gi0/10
 466    0462.7375.8490    DYNAMIC     Gi0/10
 466    0462.73f0.cbc8    DYNAMIC     Gi0/10
 466    1880.902e.5854    DYNAMIC     Gi0/10
 466    1880.902e.5c72    DYNAMIC     Gi0/10
 466    1880.902e.5ee8    DYNAMIC     Gi0/10
 466    1880.902e.5eec    DYNAMIC     Gi0/10
 466    1880.902e.5f14    DYNAMIC     Gi0/10
 466    1880.902e.5f1c    DYNAMIC     Gi0/10
 466    1880.902e.5f34    DYNAMIC     Gi0/10
 466    1880.902e.5f52    DYNAMIC     Gi0/10
 466    1880.902e.5f60    DYNAMIC     Gi0/10
 466    1880.902e.5f6e    DYNAMIC     Gi0/10
 466    1880.902e.5f70    DYNAMIC     Gi0/10
 466    1880.902e.5f72    DYNAMIC     Gi0/10
 466    1880.902e.5f96    DYNAMIC     Gi0/10
 466    1880.9071.7144    DYNAMIC     Gi0/10
 466    3890.a55e.2ce2    DYNAMIC     Gi0/10
 466    3890.a55e.2cec    DYNAMIC     Gi0/10
 466    3890.a55e.4868    DYNAMIC     Gi0/10
 466    3890.a55e.48c4    DYNAMIC     Gi0/10
 466    3890.a55e.48f2    DYNAMIC     Gi0/10
 466    3890.a55e.48fc    DYNAMIC     Gi0/10
 466    3890.a55e.4926    DYNAMIC     Gi0/10
 466    3890.a55e.4952    DYNAMIC     Gi0/10
 466    3890.a55e.4964    DYNAMIC     Gi0/10
 466    3890.a55e.5bf2    DYNAMIC     Gi0/3
           466    3890.a55e.5c02    DYNAMIC     Gi0/10
 466    3890.a577.e0ec    DYNAMIC     Gi0/10
 466    3890.a577.f358    DYNAMIC     Gi0/10
 466    3890.a577.fdf6    DYNAMIC     Gi0/10
 466    3890.a577.fe12    DYNAMIC     Gi0/10
 466    3890.a577.fe26    DYNAMIC     Gi0/10
 466    3890.a577.fe6a    DYNAMIC     Gi0/10
 466    3890.a577.fe7c    DYNAMIC     Gi0/10
 466    3890.a577.ff2a    DYNAMIC     Gi0/10
 466    3890.a577.ff5e    DYNAMIC     Gi0/10
 466    3890.a578.0082    DYNAMIC     Gi0/10
 466    3890.a578.00cc    DYNAMIC     Gi0/10
 466    3890.a578.00d8    DYNAMIC     Gi0/10
 466    3890.a578.00da    DYNAMIC     Gi0/10
 466    3890.a578.0112    DYNAMIC     Gi0/10
 466    3890.a578.0114    DYNAMIC     Gi0/10
 466    3890.a578.0122    DYNAMIC     Gi0/10
 466    3890.a578.0154    DYNAMIC     Gi0/10
 466    3890.a578.015c    DYNAMIC     Gi0/10
 466    3890.a578.1754    DYNAMIC     Gi0/1
 466    3890.a578.1760    DYNAMIC     Gi0/2
 466    3890.a578.22c2    DYNAMIC     Gi0/10
 466    3c13.cce6.a48a    DYNAMIC     Gi0/10
 466    3c51.0e3d.f424    DYNAMIC     Gi0/10
 466    4001.7a91.2abe    DYNAMIC     Gi0/10
 466    4001.7ab2.b36e    DYNAMIC     Gi0/10
 466    4001.7ab2.b382    DYNAMIC     Gi0/10
 466    4001.7ab2.b3ba    DYNAMIC     Gi0/10
 466    4001.7ab2.b91c    DYNAMIC     Gi0/10
 466    4001.7ab2.bbce    DYNAMIC     Gi0/10
 466    40ce.2486.1d76    DYNAMIC     Gi0/10
 466    40ce.24ad.1ed6    DYNAMIC     Gi0/10
 466    40ce.24ad.1fd4    DYNAMIC     Gi0/10
 466    40ce.24ad.280c    DYNAMIC     Gi0/10
 466    40ce.24ad.4206    DYNAMIC     Gi0/10
 466    500f.8049.c6c8    DYNAMIC     Gi0/10
 466    500f.804a.01c6    DYNAMIC     Gi0/10
 466    500f.804a.0746    DYNAMIC     Gi0/10
 466    500f.8097.ef2a    DYNAMIC     Gi0/10
 466    500f.8097.f8d2    DYNAMIC     Gi0/10
 466    500f.8098.13d2    DYNAMIC     Gi0/10
 466    500f.8098.172e    DYNAMIC     Gi0/10
 466    500f.8098.173a    DYNAMIC     Gi0/10
 466    58ac.7815.9e90    DYNAMIC     Gi0/10
 466    58ac.7822.edec    DYNAMIC     Gi0/10
 466    58ac.7822.eec8    DYNAMIC     Gi0/10
 466    58ac.783f.50f0    DYNAMIC     Gi0/10
 466    58ac.783f.5180    DYNAMIC     Gi0/10
 466    58ac.783f.52a0    DYNAMIC     Gi0/10
 466    58ac.7842.e870    DYNAMIC     Gi0/10
 466    58ac.7842.e940    DYNAMIC     Gi0/10
 466    58ac.7842.e9cc    DYNAMIC     Gi0/10
 466    58ac.7842.eae8    DYNAMIC     Gi0/10
 466    58ac.7842.fb28    DYNAMIC     Gi0/10
 466    58ac.7842.fb78    DYNAMIC     Gi0/10
 466    58ac.7842.fb90    DYNAMIC     Gi0/10
 466    58ac.7842.fc0c    DYNAMIC     Gi0/10
 466    58ac.7842.fce0    DYNAMIC     Gi0/10
 466    58ac.7848.c9e0    DYNAMIC     Gi0/10
           466    58ac.786b.a1fc    DYNAMIC     Gi0/10
 466    58ac.786b.a270    DYNAMIC     Gi0/10
 466    58ac.786b.a274    DYNAMIC     Gi0/10
 466    58ac.786b.a3f4    DYNAMIC     Gi0/10
 466    68ca.e436.11bb    DYNAMIC     Gi0/10
 466    70db.981a.0e0c    DYNAMIC     Gi0/10
 466    70df.2f04.d960    DYNAMIC     Gi0/4
 466    70df.2f04.fa04    DYNAMIC     Gi0/10
 466    70df.2f04.fb86    DYNAMIC     Gi0/10
 466    70df.2f05.1df8    DYNAMIC     Gi0/10
 466    70df.2fa2.4f54    DYNAMIC     Gi0/10
 466    a023.9fd9.1de2    DYNAMIC     Gi0/10
 466    e4aa.5d00.1394    DYNAMIC     Gi0/10
 466    f4db.e651.0572    DYNAMIC     Gi0/10
 627    0000.0c9f.f273    DYNAMIC     Gi0/10
 627    003a.9c40.5ec1    DYNAMIC     Gi0/10
 627    00d0.c9ef.a233    DYNAMIC     Gi0/10
 627    68ca.e436.11bb    DYNAMIC     Gi0/10
 650    0000.0c9f.f28a    DYNAMIC     Gi0/10
 650    0003.b600.b203    DYNAMIC     Gi0/10
 650    003a.9c3f.ffc1    DYNAMIC     Gi0/10
 650    003a.9c40.5ec1    DYNAMIC     Gi0/10
 650    00a0.3d00.a443    DYNAMIC     Gi0/10
 650    00a0.3d00.a445    DYNAMIC     Gi0/10
 650    00a0.3d00.ae85    DYNAMIC     Gi0/10
 650    00a0.3d00.b3ed    DYNAMIC     Gi0/10
 650    00a0.3d00.c41f    DYNAMIC     Gi0/10
 650    68ca.e436.11bb    DYNAMIC     Gi0/10
 829    0000.0c9f.f33d    DYNAMIC     Gi0/10
 829    003a.9c3f.ffc1    DYNAMIC     Gi0/10
 829    003a.9c40.5ec1    DYNAMIC     Gi0/10
 829    68ca.e436.11bb    DYNAMIC     Gi0/10
 829    68ca.e436.11f1    DYNAMIC     Gi0/10
Total Mac Addresses for this criterion: 146""",
 'show run | section tacacs':"""aaa group server tacacs+ NOC-TAC
 server name TAC-EBC
 server name TAC-SECONDARY
tacacs server TAC-EBC
 address ipv4 172.31.17.180
 key 7 0522420A08084B2B39070E53
tacacs server TAC-SECONDARY
 address ipv4 10.64.32.5
 key 7 09650A0C304112302B0E1D6B""",
 'show run | in tacacs':"""aaa group server tacacs+ NOC-TAC
tacacs server TAC-EBC
tacacs server TAC-SECONDARY""",
 'show power inline':"""Available:240.0(w)  Used:119.6(w)  Remaining:120.4(w)

Interface Admin  Oper       Power   Device              Class Max
                            (Watts)                            
--------- ------ ---------- ------- ------------------- ----- ----
Gi0/1     auto   on         29.9    AIR-AP3802I-B-K9    4     30.0 
Gi0/2     auto   on         29.9    AIR-AP3802I-B-K9    4     30.0 
Gi0/3     auto   on         29.9    AIR-AP3802I-B-K9    4     30.0 
Gi0/4     auto   on         29.9    AIR-AP3802I-B-K9    4     30.0 
Gi0/5     auto   off        0.0     n/a                 n/a   30.0 
Gi0/6     auto   off        0.0     n/a                 n/a   30.0 
Gi0/7     auto   off        0.0     n/a                 n/a   30.0 
Gi0/8     auto   off        0.0     n/a                 n/a   30.0 """,
 'show environment all':"""^
% Invalid input detected at '^' marker.
""",
}
