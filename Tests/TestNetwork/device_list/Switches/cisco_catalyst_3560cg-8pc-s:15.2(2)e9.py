ip_address = '172.31.16.43'
software = 'software'
hardware = 'hardware'
read_results = {
 'show version':"""Cisco IOS Software, C3560C Software (C3560c405ex-UNIVERSALK9-M), Version 15.2(2)E9, RELEASE SOFTWARE (fc4)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2018 by Cisco Systems, Inc.
Compiled Sat 08-Sep-18 17:00 by prod_rel_team

ROM: Bootstrap program is C3560C boot loader
BOOTLDR: C3560C Boot Loader (C3560C-HBOOT-M) Version 12.2(55r)EX11, RELEASE SOFTWARE (fc1)

sx1-482-102tower-5344-tower uptime is 21 weeks, 2 days, 6 hours, 32 minutes
System returned to ROM by power-on
System image file is "flash:/c3560c405ex-universalk9-mz.152-2.E9.bin"
Last reload reason: Unknown reason



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
License Type: Permanent
Next reload license Level: ipbase

cisco WS-C3560CG-8PC-S (PowerPC) processor (revision D0) with 131072K bytes of memory.
Processor board ID FOC1725Y4Y5
Last reset from power-on
2 Virtual Ethernet interfaces
10 Gigabit Ethernet interfaces
The password-recovery mechanism is enabled.

512K bytes of flash-simulated non-volatile configuration memory.
Base ethernet MAC Address       : F8:4F:57:D4:0A:80
Motherboard assembly number     : 73-13272-07
Power supply part number        : 341-0407-01
Motherboard serial number       : FOC17253CGC
Power supply serial number      : LIT172207NH
Model revision number           : D0
Motherboard revision number     : A0
Model number                    : WS-C3560CG-8PC-S
System serial number            : FOC1725Y4Y5
Top Assembly Part Number        : 800-33676-03
Top Assembly Revision Number    : A0
Version ID                      : V03
CLEI Code Number                : CMMD900ARC
Hardware Board Revision Number  : 0x00


Switch Ports Model                     SW Version            SW Image                 
          ------ ----- -----                     ----------            ----------               
*    1 10    WS-C3560CG-8PC-S          15.2(2)E9             C3560c405ex-UNIVERSALK9-M


Configuration register is 0xF
""",
 'show run':"""Building configuration...

Current configuration : 10943 bytes
!
! Last configuration change at 23:35:36 MDT Tue May 16 2006 by u0800148
!
version 15.2
no service pad
service timestamps debug datetime msec localtime
service timestamps log datetime msec localtime
service password-encryption
!
hostname sx1-482-102tower-5344-tower
!
boot-start-marker
boot-end-marker
!
logging buffered notifications
logging console critical
enable secret 5 $1$4.rA$OtDd6bg4OJFe2lz7jjnnc1
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
ip domain-name net.utah.edu
ip name-server 172.20.120.20
vtp domain vtp-482-102tower
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
crypto pki trustpoint TP-self-signed-1473514112
 enrollment selfsigned
 subject-name cn=IOS-Self-Signed-Certificate-1473514112
 revocation-check none
 rsakeypair TP-self-signed-1473514112
!
!
crypto pki certificate chain TP-self-signed-1473514112
 certificate self-signed 01
  30820244 308201AD A0030201 02020101 300D0609 2A864886 F70D0101 04050030 
  31312F30 2D060355 04031326 494F532D 53656C66 2D536967 6E65642D 43657274 
  69666963 6174652D 31343733 35313431 3132301E 170D3933 30333031 30303030 
  35355A17 0D323030 31303130 30303030 305A3031 312F302D 06035504 03132649 
  4F532D53 656C662D 5369676E 65642D43 65727469 66696361 74652D31 34373335 
  31343131 3230819F 300D0609 2A864886 F70D0101 01050003 818D0030 81890281 
  8100D80F BBD069F6 5DD494C4 808260F5 44EE6754 A5307199 55FB5554 418CDD38 
  E26B9A8A F109155C 1323704E 2F997858 C4C25BD9 22B0947D B221041B F562E33F 
  48588B2B 1190F6F9 3BE6312B 313E71D0 E919B722 0D01B763 D4E62ED6 52642CA6 
  AFE03938 68F5669B 31A5557F EE8238EB 8B034B33 783F1F35 DCBD6CBF B5D80E84 
  F5D90203 010001A3 6C306A30 0F060355 1D130101 FF040530 030101FF 30170603 
  551D1104 10300E82 0C737831 2D313032 2D746F6D 2E301F06 03551D23 04183016 
  80148CBE 7DE97108 1C9EBB7A 4B4CAC83 83B0E394 0E07301D 0603551D 0E041604 
  148CBE7D E971081C 9EBB7A4B 4CAC8383 B0E3940E 07300D06 092A8648 86F70D01 
  01040500 03818100 1E7488A7 211455EA 10BAE41F BC0895E7 318AB1C6 13513CD3 
  A1567238 63343AC5 F840750C 2BC91A60 E9A20F5C C8F1E811 EFEF5F83 A124A96D 
  8B06A203 A931EE32 8AFA0FC5 19A3F19D 17042B23 7956A80B 2CF4346F 71600D48 
  D9B3B190 87A8D903 AF90B6EF E8729D6E 8D5D5628 1C702797 453ED7A7 85914AE9 
  CFFF24BA 1E0E2030
  	quit
!
spanning-tree mode rapid-pvst
spanning-tree extend system-id
!
!
!
!
vlan internal allocation policy ascending
!
vlan 152
 name 102tower-floor5-clinical
!
vlan 153
 name 102tower-floor5-voip
!
vlan 800
 name 482-102tower-m
!
vlan 986
 name ebc-892-nocws
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
 switchport access vlan 152
 switchport mode access
 switchport voice vlan 153
 spanning-tree portfast
!
interface GigabitEthernet0/2
 switchport access vlan 986
 switchport mode access
 switchport voice vlan 153
 spanning-tree portfast
!
interface GigabitEthernet0/3
 switchport access vlan 152
 switchport mode access
 switchport voice vlan 153
 spanning-tree portfast
!
interface GigabitEthernet0/4
 switchport access vlan 986
 switchport mode access
 switchport voice vlan 153
 spanning-tree portfast
!
interface GigabitEthernet0/5
 switchport access vlan 986
 switchport mode access
 switchport voice vlan 153
 spanning-tree portfast
!
interface GigabitEthernet0/6
 switchport access vlan 986
 switchport mode access
 switchport voice vlan 153
 spanning-tree portfast
!
interface GigabitEthernet0/7
 switchport trunk encapsulation dot1q
 switchport mode trunk
 spanning-tree portfast
!
interface GigabitEthernet0/8
 switchport access vlan 152
 switchport mode access
 switchport voice vlan 153
 spanning-tree portfast
!
interface GigabitEthernet0/9
 switchport access vlan 986
 switchport mode access
           spanning-tree bpdufilter enable
!
interface GigabitEthernet0/10
 switchport trunk encapsulation dot1q
 switchport mode trunk
!
interface Vlan1
 no ip address
 no ip route-cache
 no ip mroute-cache
 shutdown
!
interface Vlan800
 description 482-102tower-m
 ip address 172.31.16.43 255.255.255.0
 no ip route-cache
 no ip mroute-cache
!
ip default-gateway 172.31.16.1
ip forward-protocol nd
no ip http server
no ip http secure-server
!
ip ssh version 2
!
!
ip sla enable reaction-alerts
logging facility local6
logging source-interface Vlan800
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
access-list 73 remark ========= Voice Access 5-15-2020
access-list 73 permit 155.97.178.19
access-list 73 deny   any log
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
snmp-server group VoiceRO v3 priv read VoicePhones access 73
snmp-server group VoiceRO v3 auth context vlan- match prefix 
snmp-server group NOCGrv3RO v3 priv read NOCViewRO access 70
snmp-server group NOCGrv3RO v3 auth context vlan- match prefix 
snmp-server group NOCGrv3RW v3 priv write NOCViewRW access 71
snmp-server view NOCViewRO internet included
snmp-server view NOCViewRW internet included
snmp-server view VoicePhones internet included
snmp-server location Bldg. 482 Room 5344
snmp-server contact BC-1 Y-1
snmp ifmib ifindex persist
tacacs server TAC-EBC
 address ipv4 172.31.17.180
 key 7 10674D1C2C5317292C06336A
tacacs server TAC-SECONDARY
 address ipv4 10.64.32.5
 key 7 09650A0C304112302B0E1D6B
!
!
privilege exec level 1 show configuration
privilege exec level 1 show
banner login ^C
sx1-482-102tower-5344-tower

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
 password 7 1422060A04066B7870
 login authentication console
 stopbits 1
line vty 0 4
 access-class 199 in
 exec-timeout 30 0
 password 7 113C0D041F104A5F50
 transport input ssh
line vty 5 15
 access-class 199 in
           exec-timeout 30 0
 password 7 113C0D041F104A5F50
 transport input ssh
!
!
end
""",
 'show int status':"""Port      Name               Status       Vlan       Duplex  Speed Type 
Gi0/1                        connected    152        a-full a-1000 10/100/1000BaseTX
Gi0/2                        notconnect   986          auto   auto 10/100/1000BaseTX
Gi0/3                        notconnect   152          auto   auto 10/100/1000BaseTX
Gi0/4                        notconnect   986          auto   auto 10/100/1000BaseTX
Gi0/5                        notconnect   986          auto   auto 10/100/1000BaseTX
Gi0/6                        connected    986        a-full a-1000 10/100/1000BaseTX
Gi0/7                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi0/8                        notconnect   152          auto   auto 10/100/1000BaseTX
Gi0/9                        notconnect   986          auto   auto Not Present
Gi0/10                       connected    trunk      a-full a-1000 10/100/1000BaseTX""",
 'show run | section interface':"""interface GigabitEthernet0/1
 switchport access vlan 152
 switchport mode access
 switchport voice vlan 153
 spanning-tree portfast
interface GigabitEthernet0/2
 switchport access vlan 986
 switchport mode access
 switchport voice vlan 153
 spanning-tree portfast
interface GigabitEthernet0/3
 switchport access vlan 152
 switchport mode access
 switchport voice vlan 153
 spanning-tree portfast
interface GigabitEthernet0/4
 switchport access vlan 986
 switchport mode access
 switchport voice vlan 153
 spanning-tree portfast
interface GigabitEthernet0/5
 switchport access vlan 986
 switchport mode access
 switchport voice vlan 153
 spanning-tree portfast
interface GigabitEthernet0/6
 switchport access vlan 986
 switchport mode access
 switchport voice vlan 153
 spanning-tree portfast
interface GigabitEthernet0/7
 switchport trunk encapsulation dot1q
 switchport mode trunk
 spanning-tree portfast
interface GigabitEthernet0/8
 switchport access vlan 152
 switchport mode access
 switchport voice vlan 153
 spanning-tree portfast
interface GigabitEthernet0/9
 switchport access vlan 986
 switchport mode access
 spanning-tree bpdufilter enable
interface GigabitEthernet0/10
 switchport trunk encapsulation dot1q
 switchport mode trunk
interface Vlan1
 no ip address
 no ip route-cache
 no ip mroute-cache
 shutdown
interface Vlan800
 description 482-102tower-m
 ip address 172.31.16.43 255.255.255.0
 no ip route-cache
 no ip mroute-cache
logging source-interface Vlan800""",
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
interface Vlan1
interface Vlan800
logging source-interface Vlan800""",
 'show interface link':"""^
% Invalid input detected at '^' marker.
""",
 'show interface':"""Vlan1 is administratively down, line protocol is down 
  Hardware is EtherSVI, address is f84f.57d4.0ac0 (bia f84f.57d4.0ac0)
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
Vlan800 is up, line protocol is up 
  Hardware is EtherSVI, address is f84f.57d4.0ac1 (bia f84f.57d4.0ac1)
  Description: 482-102tower-m
  Internet address is 172.31.16.43/24
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
     7638979 packets input, 1162998561 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     6199132 packets output, 1698778215 bytes, 0 underruns
     0 output errors, 2 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet0/1 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is f84f.57d4.0a81 (bia f84f.57d4.0a81)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:01, output 00:00:01, output hang never
  Last clearing of "" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
            Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 3000 bits/sec, 2 packets/sec
     3303576 packets input, 817067156 bytes, 0 no buffer
     Received 429959 broadcasts (429920 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 429920 multicast, 0 pause input
     0 input packets with dribble condition detected
     35585213 packets output, 5983432032 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet0/2 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is f84f.57d4.0a82 (bia f84f.57d4.0a82)
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
GigabitEthernet0/3 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is f84f.57d4.0a83 (bia f84f.57d4.0a83)
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
GigabitEthernet0/4 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is f84f.57d4.0a84 (bia f84f.57d4.0a84)
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
GigabitEthernet0/5 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is f84f.57d4.0a85 (bia f84f.57d4.0a85)
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
GigabitEthernet0/6 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is f84f.57d4.0a86 (bia f84f.57d4.0a86)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:10:40, output 00:00:01, output hang never
  Last clearing of "" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 2000 bits/sec, 2 packets/sec
  5 minute output rate 6000 bits/sec, 5 packets/sec
     80049879 packets input, 70081301499 bytes, 0 no buffer
     Received 2393738 broadcasts (348245 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 348245 multicast, 0 pause input
     0 input packets with dribble condition detected
     99809874 packets output, 38568979633 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet0/7 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is f84f.57d4.0a87 (bia f84f.57d4.0a87)
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
  Hardware is Gigabit Ethernet, address is f84f.57d4.0a88 (bia f84f.57d4.0a88)
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
  Hardware is Gigabit Ethernet, address is f84f.57d4.0a89 (bia f84f.57d4.0a89)
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
GigabitEthernet0/10 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is f84f.57d4.0a8a (bia f84f.57d4.0a8a)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not set
  Full-duplex, 1000Mb/s, link type is auto, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output 00:00:01, output hang never
  Last clearing of "" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 9000 bits/sec, 8 packets/sec
  5 minute output rate 2000 bits/sec, 3 packets/sec
     140512850 packets input, 45354351114 bytes, 0 no buffer
     Received 78691075 broadcasts (73212560 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 73212560 multicast, 0 pause input
     0 input packets with dribble condition detected
     102863144 packets output, 73929485360 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out""",
 'show inventory':"""NAME: "1", DESCR: "WS-C3560CG-8PC-S"
PID: WS-C3560CG-8PC-S  , VID: V03  , SN: FOC1725Y4Y5

""",
 'show interface counters':"""Port            InOctets    InUcastPkts    InMcastPkts    InBcastPkts 
Gi0/1          817067156        2873617         429920             39 
Gi0/2                  0              0              0              0 
Gi0/3                  0              0              0              0 
Gi0/4                  0              0              0              0 
Gi0/5                  0              0              0              0 
Gi0/6        70081301907       77656144         348245        2045494 
Gi0/7                  0              0              0              0 
Gi0/8                  0              0              0              0 
Gi0/9                  0              0              0              0 
Gi0/10       45354358813       61821845       73212567        5478522 

Port           OutOctets   OutUcastPkts   OutMcastPkts   OutBcastPkts 
Gi0/1         5983432339        4571255       26462220        4551741 
Gi0/2                  0              0              0              0 
Gi0/3                  0              0              0              0 
Gi0/4                  0              0              0              0 
Gi0/5                  0              0              0              0 
Gi0/6        38568980457       53741941       42341586        3726355 
Gi0/7                  0              0              0              0 
Gi0/8                  0              0              0              0 
Gi0/9                  0              0              0              0 
Gi0/10       73929509378       86728897       14089063        2045266 """,
 'show cdp nei detail':"""-------------------------
Device ID: sx1-482-102tower-5w-4401-102tower.net.ut
Entry address(es): 
  IP address: 172.31.16.14
Platform: cisco WS-C4510R+E,  Capabilities: Switch IGMP 
Interface: GigabitEthernet0/10,  Port ID (outgoing port): GigabitEthernet7/43
Holdtime : 150 sec

Version :
Cisco IOS Software, Catalyst 4500 L3 Switch  Software (cat4500es8-UNIVERSALK9-M), Version 15.2(3)E1, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2015 by Cisco Systems, Inc.
Compiled Tue 28-Apr-15 07:41 by prod_rel_team

advertisement version: 2
VTP Management Domain: 'vtp-102tower'
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 172.31.16.14
Spare Pair PoE: Yes, Spare Pair Detection Required: No
Spare Pair PD Config: Disable, Spare Pair PSE Operational: No


Total cdp entries displayed : 1""",
 'show module all':"""^
% Invalid input detected at '^' marker.
""",
 'show module':"""^
% Invalid input detected at '^' marker.
""",
 'show run | section snmp':"""snmp-server group VoiceRO v3 priv read VoicePhones access 73
snmp-server group VoiceRO v3 auth context vlan- match prefix 
snmp-server group NOCGrv3RO v3 priv read NOCViewRO access 70
snmp-server group NOCGrv3RO v3 auth context vlan- match prefix 
snmp-server group NOCGrv3RW v3 priv write NOCViewRW access 71
snmp-server view NOCViewRO internet included
snmp-server view NOCViewRW internet included
snmp-server view VoicePhones internet included
snmp-server location Bldg. 482 Room 5344
snmp-server contact BC-1 Y-1
snmp ifmib ifindex persist""",
 'show run | in snmp':"""snmp-server group VoiceRO v3 priv read VoicePhones access 73
snmp-server group VoiceRO v3 auth context vlan- match prefix 
snmp-server group NOCGrv3RO v3 priv read NOCViewRO access 70
snmp-server group NOCGrv3RO v3 auth context vlan- match prefix 
snmp-server group NOCGrv3RW v3 priv write NOCViewRW access 71
snmp-server view NOCViewRO internet included
snmp-server view NOCViewRW internet included
snmp-server view VoicePhones internet included
snmp-server location Bldg. 482 Room 5344
snmp-server contact BC-1 Y-1
snmp ifmib ifindex persist""",
 'show snmp user':"""User name: prognosis
Engine ID: 800000090300F84F57D40A81
storage-type: nonvolatile	 active
Authentication Protocol: MD5
Privacy Protocol: DES
Group-name: VoiceRO

User name: NONUserv3RO
Engine ID: 800000090300F84F57D40A81
storage-type: nonvolatile	 active
Authentication Protocol: MD5
Privacy Protocol: DES
Group-name: NOCGrv3RW

User name: NONUserv3Rw
Engine ID: 800000090300F84F57D40A81
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
    170 permit 10.71.24.19 (1230868 matches)
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
Standard IP access list 73
    10 permit 155.97.178.19
    20 deny   any log
Extended IP access list 199
    10 permit tcp 155.98.253.0 0.0.0.255 any eq 22 (70 matches)
    20 permit tcp host 172.20.150.100 any eq 22
    30 permit tcp host 155.100.126.162 any eq 22
              40 permit tcp host 155.100.126.163 any eq 22
    50 permit tcp host 10.64.2.70 any eq 22
    60 permit tcp host 155.99.239.130 any eq 22
    70 permit tcp host 155.97.152.244 any eq 22
    80 permit tcp host 155.100.123.72 any eq 22
    90 permit tcp 155.99.254.128 0.0.0.127 any eq 22 (22 matches)
    100 permit tcp 155.98.164.192 0.0.0.31 any eq 22 (42 matches)
    110 permit tcp host 10.71.24.11 any eq 22
    120 permit tcp host 10.71.24.12 any eq 22
    130 permit tcp host 10.71.24.13 any eq 22
    140 permit tcp host 10.71.24.14 any eq 22
    150 permit tcp host 10.71.24.15 any eq 22
    160 permit tcp host 10.71.24.16 any eq 22
    170 permit tcp host 10.71.24.17 any eq 22
    180 permit tcp host 10.71.24.18 any eq 22
    190 permit tcp host 10.71.24.19 any eq 22 (90 matches)
    200 permit tcp host 10.71.24.20 any eq 22
    210 permit tcp host 10.71.24.21 any eq 22
    220 permit tcp host 10.71.24.22 any eq 22
    230 permit tcp host 10.71.24.23 any eq 22
    240 permit tcp host 10.71.24.25 any eq 22
    250 permit tcp host 10.71.25.65 any eq 22
    260 permit tcp host 10.71.25.164 any eq 22
    270 deny ip any any log (20 matches)
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
logging source-interface Vlan800
logging host 155.98.204.52
logging host 155.98.253.244
logging host 172.24.29.14
logging host 10.70.24.10""",
 'show run | in logging':"""logging buffered notifications
logging console critical
logging facility local6
logging source-interface Vlan800
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
 986    0000.0c9f.f3da    DYNAMIC     Gi0/10
 986    0005.73a0.03da    DYNAMIC     Gi0/10
 986    003a.9c3f.ffc1    DYNAMIC     Gi0/10
 986    003a.9c40.5ec1    DYNAMIC     Gi0/10
 986    3c07.5456.6bb3    DYNAMIC     Gi0/10
 986    3c08.f61d.a0d2    DYNAMIC     Gi0/10
 986    8cdc.d434.9b0b    DYNAMIC     Gi0/6
 153    0004.f25c.d49f    DYNAMIC     Gi0/10
 153    0004.f261.b422    DYNAMIC     Gi0/10
 153    0004.f261.b5bf    DYNAMIC     Gi0/10
 153    0004.f26c.9985    DYNAMIC     Gi0/10
 153    0004.f270.ba06    DYNAMIC     Gi0/10
 153    0004.f272.6548    DYNAMIC     Gi0/10
 153    0004.f272.66a5    DYNAMIC     Gi0/10
 153    0004.f280.ba47    DYNAMIC     Gi0/10
 153    0004.f289.bb8c    DYNAMIC     Gi0/10
 153    0004.f290.42d1    DYNAMIC     Gi0/10
 153    0004.f2c3.e84c    DYNAMIC     Gi0/10
 153    0004.f2c3.e985    DYNAMIC     Gi0/10
 153    0004.f2c3.e987    DYNAMIC     Gi0/10
 153    0004.f2c3.ea48    DYNAMIC     Gi0/10
 153    0004.f2c3.ea62    DYNAMIC     Gi0/10
 153    0004.f2c3.eab0    DYNAMIC     Gi0/10
 153    0004.f2c3.eabe    DYNAMIC     Gi0/10
 153    0004.f2c3.eb67    DYNAMIC     Gi0/10
 153    0004.f2c3.ebe3    DYNAMIC     Gi0/10
 153    0004.f2c3.ec92    DYNAMIC     Gi0/10
 153    0004.f2c4.972a    DYNAMIC     Gi0/10
 153    0004.f2c6.c7e8    DYNAMIC     Gi0/10
 153    0004.f2ce.2564    DYNAMIC     Gi0/10
 153    0004.f2ce.bb7d    DYNAMIC     Gi0/10
 153    0004.f2ce.bd7b    DYNAMIC     Gi0/10
 153    0004.f2ce.be0d    DYNAMIC     Gi0/10
 153    0004.f2ce.bead    DYNAMIC     Gi0/10
           153    0004.f2ce.c0bf    DYNAMIC     Gi0/10
 153    0004.f2cf.9c09    DYNAMIC     Gi0/10
 153    0004.f2cf.a16e    DYNAMIC     Gi0/10
 153    0004.f2db.ce2b    DYNAMIC     Gi0/10
 153    0004.f2db.cf0a    DYNAMIC     Gi0/10
 153    0004.f2db.cf2f    DYNAMIC     Gi0/10
 153    0004.f2db.d023    DYNAMIC     Gi0/10
 153    0004.f2dc.3900    DYNAMIC     Gi0/10
 153    0004.f2dc.397e    DYNAMIC     Gi0/1
 153    0004.f2dc.3985    DYNAMIC     Gi0/10
 153    0004.f2dc.3a9a    DYNAMIC     Gi0/10
 153    0004.f2dc.3b5e    DYNAMIC     Gi0/10
 153    0004.f2dc.3be7    DYNAMIC     Gi0/10
 153    0004.f2dc.3c92    DYNAMIC     Gi0/10
 153    0004.f2dc.3d92    DYNAMIC     Gi0/10
 153    0004.f2dc.7c94    DYNAMIC     Gi0/10
 153    0004.f2fd.96e5    DYNAMIC     Gi0/10
 153    0004.f2fe.028e    DYNAMIC     Gi0/10
 153    0004.f2ff.04ee    DYNAMIC     Gi0/10
 153    3c08.f61d.a0d2    DYNAMIC     Gi0/10
 153    64f6.9d71.b7c0    DYNAMIC     Gi0/10
 153    c81f.ea87.58f9    DYNAMIC     Gi0/10
 152    0004.f2dc.397e    DYNAMIC     Gi0/1
 152    104f.a8ef.2023    DYNAMIC     Gi0/10
 152    18db.f230.5575    DYNAMIC     Gi0/10
 152    3c08.f61d.a0d2    DYNAMIC     Gi0/10
 152    a4bb.6d5b.05f4    DYNAMIC     Gi0/10
 152    dc4a.3e84.82af    DYNAMIC     Gi0/10
   1    3c08.f61d.a0d2    DYNAMIC     Gi0/10
 800    002a.101e.b6ec    DYNAMIC     Gi0/10
 800    002a.101e.bfe4    DYNAMIC     Gi0/10
 800    002a.101e.c39e    DYNAMIC     Gi0/10
 800    002a.101e.c3f0    DYNAMIC     Gi0/10
 800    002a.101e.c416    DYNAMIC     Gi0/10
 800    002a.101e.c45e    DYNAMIC     Gi0/10
 800    002a.101e.c474    DYNAMIC     Gi0/10
 800    002a.101e.c5a8    DYNAMIC     Gi0/10
 800    002a.101e.d09e    DYNAMIC     Gi0/10
 800    002a.101e.d288    DYNAMIC     Gi0/10
 800    002a.101e.d34c    DYNAMIC     Gi0/10
 800    002a.101e.d358    DYNAMIC     Gi0/10
 800    002a.101e.d376    DYNAMIC     Gi0/10
 800    002a.101e.d496    DYNAMIC     Gi0/10
 800    002a.101e.d4a0    DYNAMIC     Gi0/10
 800    002a.101e.d4ae    DYNAMIC     Gi0/10
 800    002a.101e.d504    DYNAMIC     Gi0/10
 800    002a.101e.d730    DYNAMIC     Gi0/10
 800    002a.101e.dbf6    DYNAMIC     Gi0/10
 800    002a.101e.dddc    DYNAMIC     Gi0/10
 800    002a.1034.6b84    DYNAMIC     Gi0/10
 800    002a.1034.6c08    DYNAMIC     Gi0/10
 800    002a.1034.6c40    DYNAMIC     Gi0/10
 800    002a.1034.6c76    DYNAMIC     Gi0/10
 800    002a.1034.6c86    DYNAMIC     Gi0/10
 800    002a.1034.6c96    DYNAMIC     Gi0/10
 800    002a.1034.6cb4    DYNAMIC     Gi0/10
 800    002a.1034.6d0a    DYNAMIC     Gi0/10
 800    002a.1034.6d0c    DYNAMIC     Gi0/10
 800    002a.1034.731e    DYNAMIC     Gi0/10
           800    002a.1034.732c    DYNAMIC     Gi0/10
 800    002a.1034.737c    DYNAMIC     Gi0/10
 800    002a.1034.73b2    DYNAMIC     Gi0/10
 800    002a.1034.73cc    DYNAMIC     Gi0/10
 800    002a.1034.73da    DYNAMIC     Gi0/10
 800    002a.1034.7916    DYNAMIC     Gi0/10
 800    002a.1034.7b40    DYNAMIC     Gi0/10
 800    002a.1034.7b6e    DYNAMIC     Gi0/10
 800    002a.1034.7c64    DYNAMIC     Gi0/10
 800    002a.1034.7d0a    DYNAMIC     Gi0/10
 800    002a.1034.7d46    DYNAMIC     Gi0/10
 800    002a.1034.7d78    DYNAMIC     Gi0/10
 800    002a.1034.7fc8    DYNAMIC     Gi0/10
 800    002a.1034.826c    DYNAMIC     Gi0/10
 800    002a.1034.827c    DYNAMIC     Gi0/10
 800    002a.1034.828a    DYNAMIC     Gi0/10
 800    002a.1034.8294    DYNAMIC     Gi0/10
 800    002a.1034.82b0    DYNAMIC     Gi0/10
 800    002a.1034.82b6    DYNAMIC     Gi0/10
 800    002a.1034.82ba    DYNAMIC     Gi0/10
 800    002a.1034.82bc    DYNAMIC     Gi0/10
 800    002a.1034.82c4    DYNAMIC     Gi0/10
 800    002a.1034.838e    DYNAMIC     Gi0/10
 800    002a.1060.2f36    DYNAMIC     Gi0/10
 800    002a.1060.2f3c    DYNAMIC     Gi0/10
 800    002a.1060.2f5a    DYNAMIC     Gi0/10
 800    002a.1060.2fae    DYNAMIC     Gi0/10
 800    002a.1060.300e    DYNAMIC     Gi0/10
 800    002a.1060.30a6    DYNAMIC     Gi0/10
 800    002a.1060.3bfe    DYNAMIC     Gi0/10
 800    002a.1060.3c0c    DYNAMIC     Gi0/10
 800    002a.1060.3c5e    DYNAMIC     Gi0/10
 800    002a.1060.3c68    DYNAMIC     Gi0/10
 800    002a.1060.3c96    DYNAMIC     Gi0/10
 800    002a.1060.3c98    DYNAMIC     Gi0/10
 800    002a.1060.3cb8    DYNAMIC     Gi0/10
 800    002a.1060.3ffe    DYNAMIC     Gi0/10
 800    002a.1060.411e    DYNAMIC     Gi0/10
 800    002a.1060.447a    DYNAMIC     Gi0/10
 800    002a.1060.4696    DYNAMIC     Gi0/10
 800    0042.68a7.637e    DYNAMIC     Gi0/10
 800    00a6.caff.849c    DYNAMIC     Gi0/10
 800    00a6.caff.8d18    DYNAMIC     Gi0/10
 800    00a6.caff.8d78    DYNAMIC     Gi0/10
 800    00a6.caff.8e0a    DYNAMIC     Gi0/10
 800    00a6.caff.8e0c    DYNAMIC     Gi0/10
 800    00d7.8f1e.a536    DYNAMIC     Gi0/10
 800    00d7.8f1e.a558    DYNAMIC     Gi0/10
 800    00d7.8fa6.d08c    DYNAMIC     Gi0/10
 800    00d7.8fa6.d2dc    DYNAMIC     Gi0/10
 800    00d7.8fa6.d32a    DYNAMIC     Gi0/10
 800    00d7.8fa6.d98c    DYNAMIC     Gi0/10
 800    00d7.8fa6.d98e    DYNAMIC     Gi0/10
 800    00f6.634a.4dd4    DYNAMIC     Gi0/10
 800    00f6.634a.53a8    DYNAMIC     Gi0/10
 800    00f6.634a.53d4    DYNAMIC     Gi0/10
 800    00f6.634a.5414    DYNAMIC     Gi0/10
 800    00f6.634a.541e    DYNAMIC     Gi0/10
 800    00f6.634a.5430    DYNAMIC     Gi0/10
           800    00f6.634a.543c    DYNAMIC     Gi0/10
 800    00f6.634a.543e    DYNAMIC     Gi0/10
 800    00f6.634a.5440    DYNAMIC     Gi0/10
 800    00f6.634a.5442    DYNAMIC     Gi0/10
 800    00f6.634a.544a    DYNAMIC     Gi0/10
 800    00f6.6373.8212    DYNAMIC     Gi0/10
 800    00f6.6373.8694    DYNAMIC     Gi0/10
 800    3c08.f61d.a0d2    DYNAMIC     Gi0/10
 800    500f.8098.15da    DYNAMIC     Gi0/10
 800    58ac.78f8.5472    DYNAMIC     Gi0/10
 800    58ac.78f8.54b6    DYNAMIC     Gi0/10
 800    58ac.78f8.571a    DYNAMIC     Gi0/10
 800    64f6.9d71.b7c0    DYNAMIC     Gi0/10
 800    6c41.6ab8.5209    DYNAMIC     Gi0/10
Total Mac Addresses for this criterion: 186""",
 'show run | section tacacs':"""aaa group server tacacs+ NOC-TAC
 server name TAC-EBC
 server name TAC-SECONDARY
tacacs server TAC-EBC
 address ipv4 172.31.17.180
 key 7 10674D1C2C5317292C06336A
tacacs server TAC-SECONDARY
 address ipv4 10.64.32.5
 key 7 09650A0C304112302B0E1D6B""",
 'show run | in tacacs':"""aaa group server tacacs+ NOC-TAC
tacacs server TAC-EBC
tacacs server TAC-SECONDARY""",
 'show power inline':"""Available:124.0(w)  Used:8.0(w)  Remaining:116.0(w)

Interface Admin  Oper       Power   Device              Class Max
                            (Watts)                            
--------- ------ ---------- ------- ------------------- ----- ----
Gi0/1     auto   on         8.0     Ieee PD             4     30.0 
Gi0/2     auto   off        0.0     n/a                 n/a   30.0 
Gi0/3     auto   off        0.0     n/a                 n/a   30.0 
Gi0/4     auto   off        0.0     n/a                 n/a   30.0 
Gi0/5     auto   off        0.0     n/a                 n/a   30.0 
Gi0/6     auto   off        0.0     n/a                 n/a   30.0 
Gi0/7     auto   off        0.0     n/a                 n/a   30.0 
Gi0/8     auto   off        0.0     n/a                 n/a   30.0 """,
 'show environment all':"""^
% Invalid input detected at '^' marker.
""",
}
