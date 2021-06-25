ip_address = '155.101.126.152'
software = 'software'
hardware = 'hardware'
read_results = {
 'show version':"""Cisco IOS Software, IOS-XE Software, Catalyst L3 Switch Software (CAT3K_CAA-UNIVERSALK9-M), Version 03.06.05E RELEASE SOFTWARE (fc2)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2016 by Cisco Systems, Inc.
Compiled Thu 02-Jun-16 09:03 by prod_rel_team



Cisco IOS-XE software, Copyright (c) 2005-2015 by cisco Systems, Inc.
All rights reserved.  Certain components of Cisco IOS-XE software are
licensed under the GNU General Public License ("GPL") Version 2.0.  The
software code licensed under GPL Version 2.0 is free software that comes
with ABSOLUTELY NO WARRANTY.  You can redistribute and/or modify such
GPL code under the terms of GPL Version 2.0.
(http://www.gnu.org/licenses/gpl-2.0.html) For more details, see the
documentation or "License Notice" file accompanying the IOS-XE software,
or the applicable URL provided on the flyer accompanying the IOS-XE
software.



ROM: IOS-XE ROMMON
BOOTLDR: CAT3K_CAA Boot Loader (CAT3K_CAA-HBOOT-M) Version 1.18, RELEASE SOFTWARE (P)

dx2-001park-parkservices-park uptime is 4 years, 43 weeks, 4 hours, 20 minutes
Uptime for this control processor is 4 years, 43 weeks, 4 hours, 24 minutes
System returned to ROM by Power Failure
System restarted at 12:04:45 MDT Mon Aug 29 2016
System image file is "flash:packages.conf"
Last reload reason: Power Failure



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

License Level: Ipbase
License Type: Permanent
Next reload license Level: Ipbase

cisco WS-C3650-48PQ (MIPS) processor with 4194304K bytes of physical memory.
Processor board ID FDO2003E2BP
2 Virtual Ethernet interfaces
48 Gigabit Ethernet interfaces
4 Ten Gigabit Ethernet interfaces
2048K bytes of non-volatile configuration memory.
4194304K bytes of physical memory.
          252000K bytes of Crash Files at crashinfo:.
1611414K bytes of Flash at flash:.
0K bytes of Dummy USB Flash at usbflash0:.
0K bytes of  at webui:.

Base Ethernet MAC Address          : 00:c8:8b:a9:ad:00
Motherboard Assembly Number        : 73-15903-04
Motherboard Serial Number          : FDO20031C3G
Model Revision Number              : K0
Motherboard Revision Number        : B0
Model Number                       : WS-C3650-48PQ
System Serial Number               : FDO2003E2BP


Switch Ports Model              SW Version        SW Image              Mode   
------ ----- -----              ----------        ----------            ----   
*    1 52    WS-C3650-48PQ      03.06.05E         cat3k_caa-universalk9 INSTALL


Configuration register is 0x102
""",
 'show run':"""Building configuration...

Current configuration : 15303 bytes
!
! Last configuration change at 11:21:42 MDT Sat May 22 2021 by u0627652
! NVRAM config last updated at 11:21:47 MDT Sat May 22 2021 by u0627652
!
version 15.2
no service pad
service timestamps debug datetime msec localtime
service timestamps log datetime msec localtime
service password-encryption
service compress-config
!
hostname dx2-001park-parkservices-park
!
boot-start-marker
boot-end-marker
!
!
vrf definition Mgmt-vrf
 !
 address-family ipv4
 exit-address-family
 !
 address-family ipv6
 exit-address-family
!
logging buffered notifications
logging console critical
enable secret 5 $1$KzPR$gY9dijvgouniL6XLuQymW/
!
software auto-upgrade enable
!
aaa new-model
!
!
aaa group server tacacs+ NOC-TAC
 server name TAC-DDC
 server name TAC-PARK
 server name TAC-EBC
 server name TAC-SECONDARY
!
aaa authentication login default group NOC-TAC line enable none
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
switch 1 provision ws-c3650-48pq
!
!
!
!
!
no ip source-route
!
ip domain-name net.utah.edu
ip name-server 172.20.120.20
!
!
qos queue-softmax-multiplier 100
vtp domain vtp-001park
vtp mode transparent
!
crypto pki trustpoint TP-self-signed-1199360277
 enrollment selfsigned
 subject-name cn=IOS-Self-Signed-Certificate-1199360277
 revocation-check none
 rsakeypair TP-self-signed-1199360277
!
!
crypto pki certificate chain TP-self-signed-1199360277
 certificate self-signed 01
  3082023E 308201A7 A0030201 02020101 300D0609 2A864886 F70D0101 04050030 
  31312F30 2D060355 04031326 494F532D 53656C66 2D536967 6E65642D 43657274 
  69666963 6174652D 31313939 33363032 3737301E 170D3136 30353034 31363032 
  34365A17 0D323030 31303130 30303030 305A3031 312F302D 06035504 03132649 
  4F532D53 656C662D 5369676E 65642D43 65727469 66696361 74652D31 31393933 
  36303237 3730819F 300D0609 2A864886 F70D0101 01050003 818D0030 81890281 
  8100D63A 7D595E07 078EC991 691B6A4E 329356A7 56097DC1 0F3F72E4 7D240373 
  59280922 8EF1DC3F 8CDA180F E0AB069A ABE9E5D4 166E516C 33941AA3 D9C8FE2C 
  7ECC7130 F2DD2A81 28E8FA0B 47A7DB17 E1ED8B2F 8AF425CF 1293A2B1 9BDA6689 
  1B235566 3942737D BE94EF46 76DCFC7A 7FF946E0 8F176B1E A143A1FD 13748A89 
  9C710203 010001A3 66306430 0F060355 1D130101 FF040530 030101FF 30110603 
  551D1104 0A300882 06537769 74636830 1F060355 1D230418 30168014 3CABFCF3 
  AEE9FFC3 1569BBFE D190DE8C E0C8B121 301D0603 551D0E04 1604143C ABFCF3AE 
  E9FFC315 69BBFED1 90DE8CE0 C8B12130 0D06092A 864886F7 0D010104 05000381 
  810061A3 C6461509 80152C02 66766BBB B6AA4F36 000E2676 59B993EB C5F9B941 
  6C8621E6 AA70D44C 6CB2C74B 998FA8EE 7DC3DDEA 7DDB0245 4DF1F2AB F0FCF383 
  E2A1A20C FCD62C39 B143D52D C2A05EC6 2EC8F39B 109F1BA8 8EEA6028 D05EC698 
  BEC45BFD 566C5955 820979B7 3812E5EB D4671B16 E4782BCF A267C5E3 0837F406 8FCB
  	quit
diagnostic bootup level minimal
file prompt quiet
!
spanning-tree mode rapid-pvst
spanning-tree extend system-id
hw-switch switch 1 logging onboard message level 3
!
redundancy
 mode sso
!
!
          vlan 140
 name park-001park-nac-untrust
!
vlan 145
 name park-001park-nac-trust
!
vlan 150
 name park-043navsci-nac-untrust
!
vlan 155
 name park-043navsci-nac-trust
!
vlan 160
 name park-372kenn-nac-untrust
!
vlan 165
 name park-372kenn-nac-trust
!
vlan 201
 name park-083biology-untrust-nac
!
vlan 202
 name park-008aeb-untrust-nac
!
vlan 203
 name park-013math-untrust-nac
!
vlan 295
 name park-044-nac-untrust
!
vlan 307
 name park-0001park-voipmonitoring    
!
vlan 405
 name park-008aeb-ca-wired
!
vlan 406
 name park-082biology-ca-wired
!
vlan 407
 name park-044bldg-trust
!
vlan 411
 name park-013lcb-cleanaccess-wired
!
vlan 415
 name park-001park-hr-LAN
!
vlan 457
 name park-040ssb-ca-wireless
!
vlan 522
 name park-040ssb-admin-inside
!
vlan 534
 name park-067bookstore-POS
!
vlan 562
 name park-004kh-pci
          !
vlan 720
 name park-001park-cas-trusted
!
vlan 789
 name fw-campusvpn-3
!
vlan 820
 name park-001park-m
!
vlan 831
 name park-001park-oob
lldp run
!
!
class-map match-any non-client-nrt-class
!
policy-map port_child_policy
 class non-client-nrt-class
  bandwidth remaining ratio 10
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
!
!
!
!
interface Port-channel30
 description #park:e1/9
 switchport mode trunk
!
interface GigabitEthernet0/0
 vrf forwarding Mgmt-vrf
 no ip address
 negotiation auto
!
interface GigabitEthernet1/0/1
 description #ts1-park
 switchport access vlan 831
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/2
 description #nacserver06-park Trusted
 switchport trunk native vlan 720
 switchport trunk allowed vlan 2,3,145,155,165,307-309,311-314,406,407,411,591
 switchport trunk allowed vlan add 592,720
 switchport mode trunk
!
interface GigabitEthernet1/0/3
 description #nacserver06-park untrusted
 switchport trunk allowed vlan 140,150,160,201,203,295
           switchport mode trunk
!
interface GigabitEthernet1/0/4
 switchport mode access
!
interface GigabitEthernet1/0/5
 description Nectar - Packet Broker Testing
 switchport mode trunk
!
interface GigabitEthernet1/0/6
 description Orion Web Poller
 switchport access vlan 145
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/7
!
interface GigabitEthernet1/0/8
!
interface GigabitEthernet1/0/9
!
interface GigabitEthernet1/0/10
!
interface GigabitEthernet1/0/11
!
interface GigabitEthernet1/0/12
!
interface GigabitEthernet1/0/13
!
interface GigabitEthernet1/0/14
!
interface GigabitEthernet1/0/15
 description #gi0/15_fw-campusvpn-3_trust - Shutdown 8/13/2018 CHG0044792
 switchport mode trunk
 shutdown
!
interface GigabitEthernet1/0/16
 description #gi0/16_fw-campusvpn-3_untrust - Shutdown 8/13/2018 CHG0044792
 switchport access vlan 789
 switchport mode access
 shutdown
 spanning-tree portfast
!
interface GigabitEthernet1/0/17
!
interface GigabitEthernet1/0/18
 switchport access vlan 699
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/19
 switchport access vlan 843
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/20
!
interface GigabitEthernet1/0/21
 switchport mode trunk
          !
interface GigabitEthernet1/0/22
 switchport mode trunk
!
interface GigabitEthernet1/0/23
!
interface GigabitEthernet1/0/24
!
interface GigabitEthernet1/0/25
 description NECTAR VOIP MONITORING
 switchport access vlan 307
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/26
 description NECTAR VOIP MONITORING
 switchport access vlan 307
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/27
!
interface GigabitEthernet1/0/28
!
interface GigabitEthernet1/0/29
!
interface GigabitEthernet1/0/30
!
interface GigabitEthernet1/0/31
!
interface GigabitEthernet1/0/32
!
interface GigabitEthernet1/0/33
!
interface GigabitEthernet1/0/34
!
interface GigabitEthernet1/0/35
!
interface GigabitEthernet1/0/36
!
interface GigabitEthernet1/0/37
!
interface GigabitEthernet1/0/38
!
interface GigabitEthernet1/0/39
!
interface GigabitEthernet1/0/40
!
interface GigabitEthernet1/0/41
!
interface GigabitEthernet1/0/42
!
interface GigabitEthernet1/0/43
!
interface GigabitEthernet1/0/44
!
interface GigabitEthernet1/0/45
!
interface GigabitEthernet1/0/46
          !
interface GigabitEthernet1/0/47
 description new nexus 9k demarc management
 switchport access vlan 831
 switchport mode access
!
interface GigabitEthernet1/0/48
 description new nexus 9k demarc management
 switchport access vlan 831
 switchport mode access
!
interface TenGigabitEthernet1/1/1
 description key:Te1/1/1:r1-park-ebc:Eth7/10
 switchport mode trunk
!
interface TenGigabitEthernet1/1/2
 description key:Te1/1/2:r2-park-park:Eth7/10
 switchport mode trunk
!
interface TenGigabitEthernet1/1/3
!
interface TenGigabitEthernet1/1/4
!
interface Vlan1
 no ip address
 shutdown
!
interface Vlan820
 ip address 155.101.126.152 255.255.255.240
 no ip route-cache
!
ip default-gateway 155.101.126.145
ip forward-protocol nd
no ip http server
ip http authentication local
no ip http secure-server
ip ssh version 2
!
!
logging facility local6
logging source-interface Vlan820
logging host 155.98.253.244
logging host 172.24.29.14
logging host 10.71.24.11
access-list 70 remark ==== APIC Server access ====
access-list 70 permit 10.64.2.70
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
access-list 70 remark ---- Old Orion IP addresses ----
access-list 70 permit 172.20.150.100
access-list 70 permit 10.71.24.13
          access-list 70 permit 10.71.24.12
access-list 70 permit 10.71.24.15
access-list 70 permit 10.71.24.14
access-list 70 permit 10.71.24.11
access-list 70 remark ---- New Orion IP addresses ----
access-list 70 permit 10.71.24.10
access-list 70 permit 155.100.123.72
access-list 70 permit 155.98.164.192 0.0.0.31
access-list 70 permit 155.99.254.128 0.0.0.127
access-list 70 permit 155.98.253.0 0.0.0.255
access-list 70 deny   any log
access-list 71 remark ==== Update 7-31-2019 RT and TS ====
access-list 71 remark ==== NOC SNMP RW ====
access-list 71 remark ---- APIC Server access ----
access-list 71 permit 10.64.2.70
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
access-list 71 remark ---- Old Orion IP addresses ----
access-list 71 permit 172.20.150.100
access-list 71 permit 10.71.24.13
access-list 71 permit 10.71.24.12
access-list 71 permit 10.71.24.15
access-list 71 permit 10.71.24.14
access-list 71 permit 10.71.24.11
access-list 71 remark ---- New Orion IP addresses ----
access-list 71 permit 10.71.24.10
access-list 71 permit 155.100.123.72
access-list 71 permit 155.98.164.192 0.0.0.31
access-list 71 permit 155.99.254.128 0.0.0.127
access-list 71 permit 155.98.253.0 0.0.0.255
access-list 71 deny   any log
access-list 73 remark === Monitor Team SNMP RO === rlt 12/21/2012
access-list 73 permit 155.98.219.11
access-list 73 permit 155.98.219.21
access-list 73 permit 155.100.122.47
access-list 73 permit 155.100.122.46
access-list 73 permit 155.100.122.50
access-list 73 deny   any log
access-list 199 remark ==== Update 7-31-2019 RT and TS ====
access-list 199 remark ==== line VTY 0-15 inbound ====
access-list 199 remark ---- NetOpS Workstations-Servers-Pollers ----
access-list 199 permit tcp 155.98.253.0 0.0.0.255 any eq 22
access-list 199 permit tcp host 172.20.150.100 any eq 22
access-list 199 permit tcp host 155.100.126.162 any eq 22
access-list 199 permit tcp host 155.100.126.163 any eq 22
access-list 199 permit tcp host 10.64.2.70 any eq 22
access-list 199 remark ---- door1 & door2 ----
access-list 199 permit tcp host 155.99.239.130 any eq 22
access-list 199 permit tcp host 155.97.152.244 any eq 22
access-list 199 remark ---- NOC Citrix IP ----
access-list 199 permit tcp host 155.100.123.72 any eq 22
          access-list 199 remark ---- Wireless Subnet ----
access-list 199 permit tcp 155.99.254.128 0.0.0.127 any eq 22
access-list 199 remark ---- VPN Connections ----
access-list 199 permit tcp 155.98.164.192 0.0.0.31 any eq 22
access-list 199 remark ---- New Orion Address ----
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
access-list 199 deny   ip any any log
!
snmp-server engineID local 0000000902000007EB449840
snmp-server community 99U#u#U!x RO 70
snmp-server community @u9e4tax RW 71
snmp-server community Yx5XdagKRsmD3Oi RO 70
snmp-server enable traps snmp authentication linkdown linkup coldstart warmstart
snmp-server enable traps vlancreate
snmp-server enable traps vlandelete
snmp-server enable traps envmon fan shutdown supply temperature status
snmp-server enable traps config
snmp-server host 155.98.253.148 ******** 
snmp-server host 155.98.253.149 ******** 
snmp-server host 155.98.253.152 version 2c ******** 
snmp-server host 155.98.253.152 version 2c 99U#u#U!x 
snmp-server host 155.98.253.148 v2c 
snmp-server host 155.98.253.149 v2c 
snmp ifmib ifindex persist
tacacs-server key 7 100D2339061C410F21573F3B65
tacacs server TAC-DDC
 address ipv4 155.97.160.52
 key 7 100D2339061C410F21573F3B65
tacacs server TAC-PARK
 address ipv4 155.98.253.200
 key 7 01502C245800550B0C1F5B1958
tacacs server TAC-EBC
 address ipv4 172.31.17.180
 key 7 032D1F0E2F4B246E6E0B0044
tacacs server TAC-SECONDARY
 address ipv4 10.64.32.5
 key 7 04724F032665496C291B1C56
!
!
!
no vstack
banner login ^C
dx2-001park
          
University of Utah Network: All use of this device must comply
with the University of Utah policies and procedures. Any use of
this device, whether deliberate or indeliberate will be held 
          
legally
responsible. See the University of Utah Policies and Procedures
1-15 Information Resource Policy for more detail.
(www.admin.utah.edu/ppmanual/1/1-15.html)

Problems within the University of Utah's network should be 

reported
by calling the Campus Helpdesk at 581-4000, or via e-mail at
helpdesk@utah.edu

DO NOT LOGIN
if you are not authorized by NetCom at the University of Utah.
^C
!
line con 0
 exec-timeout 5 0
 password 7 0814584F011B444446
 stopbits 1
line aux 0
 stopbits 1
line vty 0 4
 access-class 199 in
 exec-timeout 5 0
 password 7 13300313030E45797F
 transport input ssh
line vty 5 15
 access-class 199 in
 exec-timeout 5 0
 password 7 13300313030E45797F
 transport input ssh
!
ntp server 155.97.154.154
ntp server 155.97.159.10
wsma agent exec
 profile httplistener
 profile httpslistener
!
wsma agent config
 profile httplistener
 profile httpslistener
!
wsma agent filesys
 profile httplistener
 profile httpslistener
!
wsma agent notify
 profile httplistener
 profile httpslistener
!
!
wsma profile listener httplistener
 transport http
!
wsma profile listener httpslistener
 transport https
!
ap group default-group
          end
""",
 'show int status':"""Port      Name               Status       Vlan       Duplex  Speed Type 
Gi1/0/1   #ts1-park          notconnect   831          auto   auto 10/100/1000BaseTX
Gi1/0/2   #nacserver06-park  notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/3   #nacserver06-park  notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/4                      notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/5   Nectar - Packet Br notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/6   Orion Web Poller   notconnect   145          auto   auto 10/100/1000BaseTX
Gi1/0/7                      notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/8                      notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/9                      notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/10                     notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/11                     notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/12                     notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/13                     notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/14                     notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/15  #gi0/15_fw-campusv disabled     1            auto   auto 10/100/1000BaseTX
Gi1/0/16  #gi0/16_fw-campusv disabled     789          auto   auto 10/100/1000BaseTX
Gi1/0/17                     notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/18                     notconnect   699          auto   auto 10/100/1000BaseTX
Gi1/0/19                     notconnect   843          auto   auto 10/100/1000BaseTX
Gi1/0/20                     notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/21                     notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/22                     notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/23                     notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/24                     notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/25  NECTAR VOIP MONITO notconnect   307          auto   auto 10/100/1000BaseTX
Gi1/0/26  NECTAR VOIP MONITO notconnect   307          auto   auto 10/100/1000BaseTX
Gi1/0/27                     notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/28                     notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/29                     notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/30                     notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/31                     notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/32                     notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/33                     notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/34                     notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/35                     notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/36                     notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/37                     notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/38                     notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/39                     notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/40                     notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/41                     notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/42                     notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/43                     notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/44                     notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/45                     notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/46                     notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/47  new nexus 9k demar notconnect   831          auto   auto 10/100/1000BaseTX
Gi1/0/48  new nexus 9k demar notconnect   831          auto   auto 10/100/1000BaseTX
Te1/1/1   key:Te1/1/1:r1-par connected    trunk        full    10G SFP-10GBase-LR
Te1/1/2   key:Te1/1/2:r2-par connected    trunk        full    10G SFP-10GBase-LR
Te1/1/3                      notconnect   1            full    10G unknown
Te1/1/4                      notconnect   1            full    10G unknown
Po30      #park:e1/9         notconnect   1            auto   auto """,
 'show run | section interface':"""interface Port-channel30
 description #park:e1/9
 switchport mode trunk
interface GigabitEthernet0/0
 vrf forwarding Mgmt-vrf
 no ip address
 negotiation auto
interface GigabitEthernet1/0/1
 description #ts1-park
 switchport access vlan 831
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/2
 description #nacserver06-park Trusted
 switchport trunk native vlan 720
 switchport trunk allowed vlan 2,3,145,155,165,307-309,311-314,406,407,411,591
 switchport trunk allowed vlan add 592,720
 switchport mode trunk
interface GigabitEthernet1/0/3
 description #nacserver06-park untrusted
 switchport trunk allowed vlan 140,150,160,201,203,295
 switchport mode trunk
interface GigabitEthernet1/0/4
 switchport mode access
interface GigabitEthernet1/0/5
 description Nectar - Packet Broker Testing
 switchport mode trunk
interface GigabitEthernet1/0/6
 description Orion Web Poller
 switchport access vlan 145
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/7
interface GigabitEthernet1/0/8
interface GigabitEthernet1/0/9
interface GigabitEthernet1/0/10
interface GigabitEthernet1/0/11
interface GigabitEthernet1/0/12
interface GigabitEthernet1/0/13
interface GigabitEthernet1/0/14
interface GigabitEthernet1/0/15
 description #gi0/15_fw-campusvpn-3_trust - Shutdown 8/13/2018 CHG0044792
 switchport mode trunk
 shutdown
interface GigabitEthernet1/0/16
 description #gi0/16_fw-campusvpn-3_untrust - Shutdown 8/13/2018 CHG0044792
 switchport access vlan 789
 switchport mode access
 shutdown
 spanning-tree portfast
interface GigabitEthernet1/0/17
interface GigabitEthernet1/0/18
 switchport access vlan 699
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/19
 switchport access vlan 843
 switchport mode access
 spanning-tree portfast
          interface GigabitEthernet1/0/20
interface GigabitEthernet1/0/21
 switchport mode trunk
interface GigabitEthernet1/0/22
 switchport mode trunk
interface GigabitEthernet1/0/23
interface GigabitEthernet1/0/24
interface GigabitEthernet1/0/25
 description NECTAR VOIP MONITORING
 switchport access vlan 307
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/26
 description NECTAR VOIP MONITORING
 switchport access vlan 307
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/27
interface GigabitEthernet1/0/28
interface GigabitEthernet1/0/29
interface GigabitEthernet1/0/30
interface GigabitEthernet1/0/31
interface GigabitEthernet1/0/32
interface GigabitEthernet1/0/33
interface GigabitEthernet1/0/34
interface GigabitEthernet1/0/35
interface GigabitEthernet1/0/36
interface GigabitEthernet1/0/37
interface GigabitEthernet1/0/38
interface GigabitEthernet1/0/39
interface GigabitEthernet1/0/40
interface GigabitEthernet1/0/41
interface GigabitEthernet1/0/42
interface GigabitEthernet1/0/43
interface GigabitEthernet1/0/44
interface GigabitEthernet1/0/45
interface GigabitEthernet1/0/46
interface GigabitEthernet1/0/47
 description new nexus 9k demarc management
 switchport access vlan 831
 switchport mode access
interface GigabitEthernet1/0/48
 description new nexus 9k demarc management
 switchport access vlan 831
 switchport mode access
interface TenGigabitEthernet1/1/1
 description key:Te1/1/1:r1-park-ebc:Eth7/10
 switchport mode trunk
interface TenGigabitEthernet1/1/2
 description key:Te1/1/2:r2-park-park:Eth7/10
 switchport mode trunk
interface TenGigabitEthernet1/1/3
interface TenGigabitEthernet1/1/4
interface Vlan1
 no ip address
 shutdown
interface Vlan820
 ip address 155.101.126.152 255.255.255.240
 no ip route-cache
          logging source-interface Vlan820""",
 'show run | in interface':"""interface Port-channel30
interface GigabitEthernet0/0
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
interface GigabitEthernet1/0/29
interface GigabitEthernet1/0/30
interface GigabitEthernet1/0/31
interface GigabitEthernet1/0/32
interface GigabitEthernet1/0/33
interface GigabitEthernet1/0/34
interface GigabitEthernet1/0/35
interface GigabitEthernet1/0/36
interface GigabitEthernet1/0/37
interface GigabitEthernet1/0/38
interface GigabitEthernet1/0/39
interface GigabitEthernet1/0/40
interface GigabitEthernet1/0/41
interface GigabitEthernet1/0/42
interface GigabitEthernet1/0/43
interface GigabitEthernet1/0/44
interface GigabitEthernet1/0/45
interface GigabitEthernet1/0/46
interface GigabitEthernet1/0/47
interface GigabitEthernet1/0/48
interface TenGigabitEthernet1/1/1
interface TenGigabitEthernet1/1/2
interface TenGigabitEthernet1/1/3
interface TenGigabitEthernet1/1/4
interface Vlan1
interface Vlan820
logging source-interface Vlan820""",
 'show interface link':"""^
% Invalid input detected at '^' marker.
""",
 'show interface':"""Vlan1 is administratively down, line protocol is down 
  Hardware is Ethernet SVI, address is 00c8.8ba9.ad47 (bia 00c8.8ba9.ad47)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y41w, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     69660881 packets input, 10719577661 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 1 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Vlan820 is up, line protocol is up 
  Hardware is Ethernet SVI, address is 00c8.8ba9.ad5b (bia 00c8.8ba9.ad5b)
  Internet address is 155.101.126.152/28
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 3000 bits/sec, 5 packets/sec
  5 minute output rate 4000 bits/sec, 4 packets/sec
     897872898 packets input, 89036350394 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     351504596 packets output, 101972904643 bytes, 0 underruns
     0 output errors, 2 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet0/0 is down, line protocol is down 
  NOTE: Packet counters for management port are meaningful 
        only when it is physically located at stack master
  Hardware is RP management port, address is 00c8.8ba9.ad00 (bia 00c8.8ba9.ad00)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Unknown, Unknown, link type is auto, media type is 100BaseTX
  output flow-control is unsupported, input flow-control is unsupported
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
            Queueing strategy: fifo
  Output queue: 0/0 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/1 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00c8.8ba9.ad01 (bia 00c8.8ba9.ad01)
  Description: #ts1-park
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
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
GigabitEthernet1/0/2 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00c8.8ba9.ad02 (bia 00c8.8ba9.ad02)
  Description: #nacserver06-park Trusted
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
            5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     3720226 packets input, 405589314 bytes, 0 no buffer
     Received 7392 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     10643874 packets output, 1120526806 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/3 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00c8.8ba9.ad03 (bia 00c8.8ba9.ad03)
  Description: #nacserver06-park untrusted
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     2605011 packets input, 309796670 bytes, 0 no buffer
     Received 2597621 broadcasts (2502949 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 2502949 multicast, 0 pause input
     0 input packets with dribble condition detected
     3978359 packets output, 292627184 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/4 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00c8.8ba9.ad04 (bia 00c8.8ba9.ad04)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
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
GigabitEthernet1/0/5 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00c8.8ba9.ad05 (bia 00c8.8ba9.ad05)
  Description: Nectar - Packet Broker Testing
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y43w, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 9315067
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     68517 packets input, 5545281 bytes, 0 no buffer
     Received 62338 broadcasts (62184 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 62184 multicast, 0 pause input
     0 input packets with dribble condition detected
     1761630 packets output, 173963059 bytes, 0 underruns
     9315067 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/6 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00c8.8ba9.ad06 (bia 00c8.8ba9.ad06)
  Description: Orion Web Poller
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y48w, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 235307642
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     13150454053 packets input, 1982322056991 bytes, 0 no buffer
               Received 13719082 broadcasts (5056760 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 5056760 multicast, 85354 pause input
     0 input packets with dribble condition detected
     22009795948 packets output, 28663772694613 bytes, 0 underruns
     235307642 output errors, 0 collisions, 4 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/7 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00c8.8ba9.ad07 (bia 00c8.8ba9.ad07)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
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
GigabitEthernet1/0/8 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00c8.8ba9.ad08 (bia 00c8.8ba9.ad08)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
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
GigabitEthernet1/0/9 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00c8.8ba9.ad09 (bia 00c8.8ba9.ad09)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
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
GigabitEthernet1/0/10 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00c8.8ba9.ad0a (bia 00c8.8ba9.ad0a)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
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
GigabitEthernet1/0/11 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00c8.8ba9.ad0b (bia 00c8.8ba9.ad0b)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
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
GigabitEthernet1/0/12 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00c8.8ba9.ad0c (bia 00c8.8ba9.ad0c)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
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
GigabitEthernet1/0/13 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00c8.8ba9.ad0d (bia 00c8.8ba9.ad0d)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
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
GigabitEthernet1/0/14 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00c8.8ba9.ad0e (bia 00c8.8ba9.ad0e)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
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
GigabitEthernet1/0/15 is administratively down, line protocol is down (disabled) 
            Hardware is Gigabit Ethernet, address is 00c8.8ba9.ad0f (bia 00c8.8ba9.ad0f)
  Description: #gi0/15_fw-campusvpn-3_trust - Shutdown 8/13/2018 CHG0044792
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 57604950
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     4412675782 packets input, 3239731506727 bytes, 0 no buffer
     Received 958424 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     7821516398 packets output, 5931939188399 bytes, 0 underruns
     57604950 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/16 is administratively down, line protocol is down (disabled) 
  Hardware is Gigabit Ethernet, address is 00c8.8ba9.ad10 (bia 00c8.8ba9.ad10)
  Description: #gi0/16_fw-campusvpn-3_untrust - Shutdown 8/13/2018 CHG0044792
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 142261739
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     15478601751 packets input, 10939042124834 bytes, 0 no buffer
     Received 7129100 broadcasts (7040785 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 7040785 multicast, 0 pause input
     0 input packets with dribble condition detected
     12369633842 packets output, 7430314321246 bytes, 0 underruns
     142261739 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/17 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00c8.8ba9.ad11 (bia 00c8.8ba9.ad11)
            MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
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
GigabitEthernet1/0/18 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00c8.8ba9.ad12 (bia 00c8.8ba9.ad12)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
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
GigabitEthernet1/0/19 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00c8.8ba9.ad13 (bia 00c8.8ba9.ad13)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
            Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
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
GigabitEthernet1/0/20 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00c8.8ba9.ad14 (bia 00c8.8ba9.ad14)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
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
GigabitEthernet1/0/21 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00c8.8ba9.ad15 (bia 00c8.8ba9.ad15)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
            ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
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
GigabitEthernet1/0/22 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00c8.8ba9.ad16 (bia 00c8.8ba9.ad16)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
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
GigabitEthernet1/0/23 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00c8.8ba9.ad17 (bia 00c8.8ba9.ad17)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters never
            Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     11 packets input, 6534 bytes, 0 no buffer
     Received 11 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     87 packets output, 11967 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/24 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00c8.8ba9.ad18 (bia 00c8.8ba9.ad18)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
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
GigabitEthernet1/0/25 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00c8.8ba9.ad19 (bia 00c8.8ba9.ad19)
  Description: NECTAR VOIP MONITORING
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y19w, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
            Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     2734853656 packets input, 3723881116383 bytes, 0 no buffer
     Received 66760 broadcasts (9302 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 9302 multicast, 0 pause input
     0 input packets with dribble condition detected
     1615174106 packets output, 169189536818 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/26 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00c8.8ba9.ad1a (bia 00c8.8ba9.ad1a)
  Description: NECTAR VOIP MONITORING
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y19w, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     2648455137 packets input, 3794467758818 bytes, 0 no buffer
     Received 69150 broadcasts (8923 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 8923 multicast, 0 pause input
     0 input packets with dribble condition detected
     1492674720 packets output, 126369653057 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/27 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00c8.8ba9.ad1b (bia 00c8.8ba9.ad1b)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
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
  Hardware is Gigabit Ethernet, address is 00c8.8ba9.ad1c (bia 00c8.8ba9.ad1c)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
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
GigabitEthernet1/0/29 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00c8.8ba9.ad1d (bia 00c8.8ba9.ad1d)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
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
GigabitEthernet1/0/30 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00c8.8ba9.ad1e (bia 00c8.8ba9.ad1e)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
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
GigabitEthernet1/0/31 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00c8.8ba9.ad1f (bia 00c8.8ba9.ad1f)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
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
GigabitEthernet1/0/32 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00c8.8ba9.ad20 (bia 00c8.8ba9.ad20)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
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
GigabitEthernet1/0/33 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00c8.8ba9.ad21 (bia 00c8.8ba9.ad21)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
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
GigabitEthernet1/0/34 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00c8.8ba9.ad22 (bia 00c8.8ba9.ad22)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
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
GigabitEthernet1/0/35 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00c8.8ba9.ad23 (bia 00c8.8ba9.ad23)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
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
GigabitEthernet1/0/36 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00c8.8ba9.ad24 (bia 00c8.8ba9.ad24)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
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
GigabitEthernet1/0/37 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00c8.8ba9.ad25 (bia 00c8.8ba9.ad25)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
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
GigabitEthernet1/0/38 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00c8.8ba9.ad26 (bia 00c8.8ba9.ad26)
            MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
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
GigabitEthernet1/0/39 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00c8.8ba9.ad27 (bia 00c8.8ba9.ad27)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
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
GigabitEthernet1/0/40 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00c8.8ba9.ad28 (bia 00c8.8ba9.ad28)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
            Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
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
GigabitEthernet1/0/41 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00c8.8ba9.ad29 (bia 00c8.8ba9.ad29)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
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
GigabitEthernet1/0/42 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00c8.8ba9.ad2a (bia 00c8.8ba9.ad2a)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
            ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
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
GigabitEthernet1/0/43 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00c8.8ba9.ad2b (bia 00c8.8ba9.ad2b)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
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
GigabitEthernet1/0/44 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00c8.8ba9.ad2c (bia 00c8.8ba9.ad2c)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters never
            Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
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
GigabitEthernet1/0/45 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00c8.8ba9.ad2d (bia 00c8.8ba9.ad2d)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
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
GigabitEthernet1/0/46 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00c8.8ba9.ad2e (bia 00c8.8ba9.ad2e)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
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
GigabitEthernet1/0/47 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00c8.8ba9.ad2f (bia 00c8.8ba9.ad2f)
  Description: new nexus 9k demarc management
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y26w, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     1754598 packets input, 144173830 bytes, 0 no buffer
     Received 160565 broadcasts (152477 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 152477 multicast, 0 pause input
     0 input packets with dribble condition detected
     16655775 packets output, 2382418476 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/48 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00c8.8ba9.ad30 (bia 00c8.8ba9.ad30)
  Description: new nexus 9k demarc management
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y26w, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
            5 minute output rate 0 bits/sec, 0 packets/sec
     2674066 packets input, 207208081 bytes, 0 no buffer
     Received 160610 broadcasts (152479 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 152479 multicast, 0 pause input
     0 input packets with dribble condition detected
     17579809 packets output, 2901289873 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/1/1 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet, address is 00c8.8ba9.ad31 (bia 00c8.8ba9.ad31)
  Description: key:Te1/1/1:r1-park-ebc:Eth7/10
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not set
  Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-LR
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 38000 bits/sec, 43 packets/sec
  5 minute output rate 7000 bits/sec, 8 packets/sec
     26024665117 packets input, 21604187860918 bytes, 0 no buffer
     Received 3748360208 broadcasts (1864483361 multicasts)
     0 runts, 0 giants, 0 throttles 
     36 input errors, 33 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 1864483361 multicast, 0 pause input
     0 input packets with dribble condition detected
     20322979353 packets output, 16356477360840 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/1/2 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet, address is 00c8.8ba9.ad32 (bia 00c8.8ba9.ad32)
  Description: key:Te1/1/2:r2-park-park:Eth7/10
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not set
  Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-LR
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 54000 bits/sec, 11 packets/sec
  5 minute output rate 30000 bits/sec, 35 packets/sec
               23115537165 packets input, 21344741618133 bytes, 0 no buffer
     Received 2758151782 broadcasts (1656898288 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 1656898288 multicast, 0 pause input
     0 input packets with dribble condition detected
     19521729225 packets output, 7646195256077 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/1/3 is down, line protocol is down (notconnect) 
  Hardware is Ten Gigabit Ethernet, address is 00c8.8ba9.ad33 (bia 00c8.8ba9.ad33)
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not set
  Full-duplex, 10Gb/s, link type is auto, media type is unknown
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
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
TenGigabitEthernet1/1/4 is down, line protocol is down (notconnect) 
  Hardware is Ten Gigabit Ethernet, address is 00c8.8ba9.ad34 (bia 00c8.8ba9.ad34)
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not set
  Full-duplex, 10Gb/s, link type is auto, media type is unknown
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 4y7w, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     32 packets input, 9068 bytes, 0 no buffer
     Received 32 broadcasts (32 multicasts)
     0 runts, 0 giants, 0 throttles 
               0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 32 multicast, 0 pause input
     0 input packets with dribble condition detected
     79 packets output, 13571 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
Port-channel30 is down, line protocol is down (notconnect) 
  Hardware is EtherChannel, address is 00c8.8ba9.ad31 (bia 00c8.8ba9.ad31)
  Description: #park:e1/9
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, link type is auto, media type is 
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 4w6d, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     48909432496 packets input, 42834399787911 bytes, 0 no buffer
     Received 6368440567 broadcasts (3447245238 multicasts)
     0 runts, 0 giants, 0 throttles 
     36 input errors, 33 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 3447245238 multicast, 0 pause input
     0 input packets with dribble condition detected
     39666020594 packets output, 23985102043978 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out""",
 'show inventory':"""NAME: "c36xx Stack", DESCR: "c36xx Stack"
PID: WS-C3650-48PQ     , VID: V03  , SN: FDO2003E2BP

NAME: "Switch 1", DESCR: "WS-C3650-48FQ-S"
PID: WS-C3650-48FQ-S   , VID: V03  , SN: FDO2003E2BP

NAME: "Switch 1 - Power Supply A", DESCR: "Switch 1 - Power Supply A"
PID: PWR-C2-1025WAC    , VID: V02  , SN: DCB1951C0QZ

NAME: "TenGigabitEthernet1/1/1", DESCR: "SFP-10GBase-LR"
PID: SFP-10G-LR         , VID: V02  , SN: EA509010950    

NAME: "TenGigabitEthernet1/1/2", DESCR: "SFP-10GBase-LR"
PID: SFP-10G-LR         , VID: V02  , SN: EA509010949    

""",
 'show interface counters':"""Port            InOctets    InUcastPkts    InMcastPkts    InBcastPkts 
Gi1/0/1                0              0              0              0 
Gi1/0/2        405589314        3712834              0           7392 
Gi1/0/3        309796670           7390        2502949          94672 
Gi1/0/4                0              0              0              0 
Gi1/0/5          5545281           6179          62184            154 
Gi1/0/6    1982322056991    13136734971        5056760        8662322 
Gi1/0/7                0              0              0              0 
Gi1/0/8                0              0              0              0 
Gi1/0/9                0              0              0              0 
Gi1/0/10               0              0              0              0 
Gi1/0/11               0              0              0              0 
Gi1/0/12               0              0              0              0 
Gi1/0/13               0              0              0              0 
Gi1/0/14               0              0              0              0 
Gi1/0/15   3239731506727     4411717358              0         958424 
Gi1/0/16  10939042124834    15471472651        7040785          88315 
Gi1/0/17               0              0              0              0 
Gi1/0/18               0              0              0              0 
Gi1/0/19               0              0              0              0 
Gi1/0/20               0              0              0              0 
Gi1/0/21               0              0              0              0 
Gi1/0/22               0              0              0              0 
Gi1/0/23            6534              0              0             11 
Gi1/0/24               0              0              0              0 
Gi1/0/25   3723881116383     2734786896           9302          57458 
Gi1/0/26   3794467758818     2648385987           8923          60227 
Gi1/0/27               0              0              0              0 
Gi1/0/28               0              0              0              0 
Gi1/0/29               0              0              0              0 
Gi1/0/30               0              0              0              0 
Gi1/0/31               0              0              0              0 
Gi1/0/32               0              0              0              0 
Gi1/0/33               0              0              0              0 
Gi1/0/34               0              0              0              0 
Gi1/0/35               0              0              0              0 
Gi1/0/36               0              0              0              0 
Gi1/0/37               0              0              0              0 
Gi1/0/38               0              0              0              0 
Gi1/0/39               0              0              0              0 
Gi1/0/40               0              0              0              0 
Gi1/0/41               0              0              0              0 
Gi1/0/42               0              0              0              0 
Gi1/0/43               0              0              0              0 
Gi1/0/44               0              0              0              0 
Gi1/0/45               0              0              0              0 
Gi1/0/46               0              0              0              0 
Gi1/0/47       144173830        1594033         152477           8088 
Gi1/0/48       207208081        2513456         152479           8131 
Te1/1/1   21604187903925    22276305065     1864483476     1883876946 
Te1/1/2   21344741625471    20357385392     1656898304     1101253514 
Te1/1/3                0              0              0              0 
Te1/1/4             9068              0             32              0 
Po30      42834399787911    42540991929     3447245238     2921195329 

Port           OutOctets   OutUcastPkts   OutMcastPkts   OutBcastPkts 
Gi1/0/1                0              0              0              0 
Gi1/0/2       1120526806        3981229        6568006          94639 
          
Port           OutOctets   OutUcastPkts   OutMcastPkts   OutBcastPkts 
Gi1/0/3        292627184          88700        3889659              0 
Gi1/0/4                0              0              0              0 
Gi1/0/5        173963059          25949         656080        1079601 
Gi1/0/6   28663772694613    21925921192       76329672        7545084 
Gi1/0/7                0              0              0              0 
Gi1/0/8                0              0              0              0 
Gi1/0/9                0              0              0              0 
Gi1/0/10               0              0              0              0 
Gi1/0/11               0              0              0              0 
Gi1/0/12               0              0              0              0 
Gi1/0/13               0              0              0              0 
Gi1/0/14               0              0              0              0 
Gi1/0/15   5931939188399     5164234066     1417400814     1239881518 
Gi1/0/16   7430314321246    12277522818       91409151         701873 
Gi1/0/17               0              0              0              0 
Gi1/0/18               0              0              0              0 
Gi1/0/19               0              0              0              0 
Gi1/0/20               0              0              0              0 
Gi1/0/21               0              0              0              0 
Gi1/0/22               0              0              0              0 
Gi1/0/23           11967             10             77              0 
Gi1/0/24               0              0              0              0 
Gi1/0/25    169189536818     1541931285       72976387         266434 
Gi1/0/26    126369653057     1419435182       72975845         263693 
Gi1/0/27               0              0              0              0 
Gi1/0/28               0              0              0              0 
Gi1/0/29               0              0              0              0 
Gi1/0/30               0              0              0              0 
Gi1/0/31               0              0              0              0 
Gi1/0/32               0              0              0              0 
Gi1/0/33               0              0              0              0 
Gi1/0/34               0              0              0              0 
Gi1/0/35               0              0              0              0 
Gi1/0/36               0              0              0              0 
Gi1/0/37               0              0              0              0 
Gi1/0/38               0              0              0              0 
Gi1/0/39               0              0              0              0 
Gi1/0/40               0              0              0              0 
Gi1/0/41               0              0              0              0 
Gi1/0/42               0              0              0              0 
Gi1/0/43               0              0              0              0 
Gi1/0/44               0              0              0              0 
Gi1/0/45               0              0              0              0 
Gi1/0/46               0              0              0              0 
Gi1/0/47      2382418476        2805496       13840319           9960 
Gi1/0/48      2901289873        3731396       13838485           9928 
Te1/1/1   16356477461149    19478588744      844106610         284251 
Te1/1/2    7646195283531    19244636551      224189576       52903312 
Te1/1/3                0              0              0              0 
Te1/1/4            13571              0             79              0 
Po30      23985102043978    38718484485      937543916        9992193 """,
 'show cdp nei detail':"""-------------------------
Device ID: r1-park-ebc.net.utah.edu
Entry address(es): 
  IP address: 155.101.114.2
Platform: cisco C9606R,  Capabilities: Router Switch 
Interface: TenGigabitEthernet1/1/1,  Port ID (outgoing port): TwentyFiveGigE6/0/11
Holdtime : 123 sec

Version :
Cisco IOS Software [Gibraltar], Catalyst L3 Switch Software (CAT9K_IOSXE), Version 16.12.5b, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2021 by Cisco Systems, Inc.
Compiled Thu 25-Mar-21 13:21 by mcpre

advertisement version: 2
VTP Management Domain: 'r1-park'
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 155.101.114.2

-------------------------
Device ID: r2-park-park.net.utah.edu
Entry address(es): 
  IP address: 155.101.114.3
Platform: cisco C9606R,  Capabilities: Router Switch 
Interface: TenGigabitEthernet1/1/2,  Port ID (outgoing port): TwentyFiveGigE6/0/11
Holdtime : 166 sec

Version :
Cisco IOS Software [Gibraltar], Catalyst L3 Switch Software (CAT9K_IOSXE), Version 16.12.5b, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2021 by Cisco Systems, Inc.
Compiled Thu 25-Mar-21 13:21 by mcpre

advertisement version: 2
VTP Management Domain: 'r2-park'
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 155.101.114.3


Total cdp entries displayed : 2""",
 'show module all':"""^
% Invalid input detected at '^' marker.
""",
 'show module':"""Switch  Ports    Model                Serial No.   MAC address     Hw Ver.       Sw Ver. 
------  -----   ---------             -----------  --------------  -------       --------
 1       52     WS-C3650-48FQ-S       FDO2003E2BP  00c8.8ba9.ad00  V03           03.06.05E   """,
 'show run | section snmp':"""snmp-server engineID local 0000000902000007EB449840
snmp-server community 99U#u#U!x RO 70
snmp-server community @u9e4tax RW 71
snmp-server community Yx5XdagKRsmD3Oi RO 70
snmp-server enable traps snmp authentication linkdown linkup coldstart warmstart
snmp-server enable traps vlancreate
snmp-server enable traps vlandelete
snmp-server enable traps envmon fan shutdown supply temperature status
snmp-server enable traps config
snmp-server host 155.98.253.148 ******** 
snmp-server host 155.98.253.149 ******** 
snmp-server host 155.98.253.152 version 2c ******** 
snmp-server host 155.98.253.152 version 2c 99U#u#U!x 
snmp-server host 155.98.253.148 v2c 
snmp-server host 155.98.253.149 v2c 
snmp ifmib ifindex persist""",
 'show run | in snmp':"""snmp-server engineID local 0000000902000007EB449840
snmp-server community 99U#u#U!x RO 70
snmp-server community @u9e4tax RW 71
snmp-server community Yx5XdagKRsmD3Oi RO 70
snmp-server enable traps snmp authentication linkdown linkup coldstart warmstart
snmp-server enable traps vlancreate
snmp-server enable traps vlandelete
snmp-server enable traps envmon fan shutdown supply temperature status
snmp-server enable traps config
snmp-server host 155.98.253.148 ******** 
snmp-server host 155.98.253.149 ******** 
snmp-server host 155.98.253.152 version 2c ******** 
snmp-server host 155.98.253.152 version 2c 99U#u#U!x 
snmp-server host 155.98.253.148 v2c 
snmp-server host 155.98.253.149 v2c 
snmp ifmib ifindex persist""",
 'show snmp user':"""""",
 'show access-list':"""Standard IP access list 70
    10 permit 10.64.2.70
    50 permit 155.100.126.163
    40 permit 155.100.126.162
    200 permit 10.71.24.21
    190 permit 10.71.24.20
    220 permit 10.71.24.23
    210 permit 10.71.24.22
    160 permit 10.71.24.17
    150 permit 10.71.24.16
    180 permit 10.71.24.19
    170 permit 10.71.24.18 (115911946 matches)
    20 permit 172.20.150.100
    120 permit 10.71.24.13
    110 permit 10.71.24.12
    140 permit 10.71.24.15
    130 permit 10.71.24.14
    100 permit 10.71.24.11
    90 permit 10.71.24.10
    30 permit 155.100.123.72
    60 permit 155.98.164.192, wildcard bits 0.0.0.31
    70 permit 155.99.254.128, wildcard bits 0.0.0.127
    80 permit 155.98.253.0, wildcard bits 0.0.0.255 (14 matches)
    230 deny   any log
Standard IP access list 71
    10 permit 10.64.2.70
    50 permit 155.100.126.163
    40 permit 155.100.126.162
    200 permit 10.71.24.21
    190 permit 10.71.24.20
    220 permit 10.71.24.23
    210 permit 10.71.24.22
    160 permit 10.71.24.17
    150 permit 10.71.24.16
    180 permit 10.71.24.19
    170 permit 10.71.24.18
    20 permit 172.20.150.100
    120 permit 10.71.24.13
    110 permit 10.71.24.12
    140 permit 10.71.24.15
    130 permit 10.71.24.14
    100 permit 10.71.24.11
    90 permit 10.71.24.10
    30 permit 155.100.123.72
    60 permit 155.98.164.192, wildcard bits 0.0.0.31
    70 permit 155.99.254.128, wildcard bits 0.0.0.127
    80 permit 155.98.253.0, wildcard bits 0.0.0.255
    230 deny   any log
Standard IP access list 73
    10 permit 155.98.219.11
    20 permit 155.98.219.21
    30 permit 155.100.122.47
    40 permit 155.100.122.46
    50 permit 155.100.122.50
    60 deny   any log
Extended IP access list 199
    10 permit tcp 155.98.253.0 0.0.0.255 any eq 22 (1732 matches)
    20 permit tcp host 172.20.150.100 any eq 22
    30 permit tcp host 155.100.126.162 any eq 22
              40 permit tcp host 155.100.126.163 any eq 22
    50 permit tcp host 10.64.2.70 any eq 22
    60 permit tcp host 155.99.239.130 any eq 22
    70 permit tcp host 155.97.152.244 any eq 22
    80 permit tcp host 155.100.123.72 any eq 22
    90 permit tcp 155.99.254.128 0.0.0.127 any eq 22 (36 matches)
    100 permit tcp 155.98.164.192 0.0.0.31 any eq 22 (104 matches)
    110 permit tcp host 10.71.24.11 any eq 22
    120 permit tcp host 10.71.24.12 any eq 22
    130 permit tcp host 10.71.24.13 any eq 22
    140 permit tcp host 10.71.24.14 any eq 22
    150 permit tcp host 10.71.24.15 any eq 22
    160 permit tcp host 10.71.24.16 any eq 22
    170 permit tcp host 10.71.24.17 any eq 22
    180 permit tcp host 10.71.24.18 any eq 22 (9598 matches)
    190 permit tcp host 10.71.24.19 any eq 22
    200 permit tcp host 10.71.24.20 any eq 22
    210 permit tcp host 10.71.24.21 any eq 22
    220 permit tcp host 10.71.24.22 any eq 22
    230 permit tcp host 10.71.24.23 any eq 22
    240 deny ip any any log (222 matches)
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
hw-switch switch 1 logging onboard message level 3
logging facility local6
logging source-interface Vlan820
logging host 155.98.253.244
logging host 172.24.29.14
logging host 10.71.24.11""",
 'show run | in logging':"""logging buffered notifications
logging console critical
hw-switch switch 1 logging onboard message level 3
logging facility local6
logging source-interface Vlan820
logging host 155.98.253.244
logging host 172.24.29.14
logging host 10.71.24.11""",
 'show mac address-table':"""Mac Address Table
-------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
 All    0100.0ccc.cccc    STATIC      CPU
 All    0100.0ccc.cccd    STATIC      CPU
 All    0100.0ccc.ccce    STATIC      CPU
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
   1    b0c5.3cee.680a    DYNAMIC     Te1/1/1
   1    b0c5.3cee.870a    DYNAMIC     Te1/1/2
 820    0000.0c07.ac0a    DYNAMIC     Te1/1/1
 820    00c8.8ba9.ad5b    STATIC      Vl820 
 820    40b5.c17d.b982    DYNAMIC     Te1/1/1
 820    b0c5.3cee.680a    DYNAMIC     Te1/1/1
 820    bc4a.5664.45c2    DYNAMIC     Te1/1/1
 140    b0c5.3cee.680a    DYNAMIC     Te1/1/1
 145    b0c5.3cee.680a    DYNAMIC     Te1/1/1
 150    b0c5.3cee.680a    DYNAMIC     Te1/1/1
 155    b0c5.3cee.680a    DYNAMIC     Te1/1/1
 165    b0c5.3cee.680a    DYNAMIC     Te1/1/1
 201    b0c5.3cee.680a    DYNAMIC     Te1/1/1
 203    b0c5.3cee.680a    DYNAMIC     Te1/1/1
 295    b0c5.3cee.680a    DYNAMIC     Te1/1/1
 789    0000.0c07.ac0a    DYNAMIC     Te1/1/1
 789    40b5.c17d.b982    DYNAMIC     Te1/1/1
 789    b0c5.3cee.680a    DYNAMIC     Te1/1/1
 789    bc4a.5664.45c2    DYNAMIC     Te1/1/1
 831    0000.0c07.ac0a    DYNAMIC     Te1/1/1
 831    b0c5.3cee.680a    DYNAMIC     Te1/1/1
 831    bc4a.5664.45c2    DYNAMIC     Te1/1/1
 522    0000.0c07.ac0a    DYNAMIC     Te1/1/1
 522    0000.8595.5e0b    DYNAMIC     Te1/1/1
 522    0011.85fa.e72c    DYNAMIC     Te1/1/1
 522    0050.5689.4ad5    DYNAMIC     Te1/1/1
 522    0050.5689.61dc    DYNAMIC     Te1/1/1
 522    0050.5689.6a31    DYNAMIC     Te1/1/1
 522    0050.5689.6bfa    DYNAMIC     Te1/1/1
 522    0050.5689.7d0e    DYNAMIC     Te1/1/1
 522    0050.56a5.7197    DYNAMIC     Te1/1/1
 522    0068.eb4f.eb5d    DYNAMIC     Te1/1/1
 522    00c0.ff50.9717    DYNAMIC     Te1/1/1
           522    00e0.6152.fe65    DYNAMIC     Te1/1/1
 522    1065.30fa.67f1    DYNAMIC     Te1/1/1
 522    1803.7316.ec18    DYNAMIC     Te1/1/1
 522    1803.7317.76fe    DYNAMIC     Te1/1/1
 522    1803.7324.4366    DYNAMIC     Te1/1/1
 522    1803.7324.4a6b    DYNAMIC     Te1/1/1
 522    1803.734f.eb57    DYNAMIC     Te1/1/1
 522    1803.7350.592d    DYNAMIC     Te1/1/1
 522    1803.7350.5934    DYNAMIC     Te1/1/1
 522    1803.7350.59ab    DYNAMIC     Te1/1/1
 522    1803.7350.5a03    DYNAMIC     Te1/1/1
 522    1803.73d8.2742    DYNAMIC     Te1/1/1
 522    1860.24c5.4995    DYNAMIC     Te1/1/1
 522    1866.da06.a13a    DYNAMIC     Te1/1/1
 522    1866.da06.a13c    DYNAMIC     Te1/1/1
 522    1866.da06.a1bc    DYNAMIC     Te1/1/1
 522    1866.da06.a299    DYNAMIC     Te1/1/1
 522    1866.da06.ae4c    DYNAMIC     Te1/1/1
 522    1866.da06.ae89    DYNAMIC     Te1/1/1
 522    1866.da06.aef0    DYNAMIC     Te1/1/1
 522    1866.da06.af85    DYNAMIC     Te1/1/1
 522    1866.da06.af9a    DYNAMIC     Te1/1/1
 522    1866.da06.afaa    DYNAMIC     Te1/1/1
 522    1866.da06.b116    DYNAMIC     Te1/1/1
 522    1866.da06.b1bf    DYNAMIC     Te1/1/1
 522    1866.da06.b1d5    DYNAMIC     Te1/1/1
 522    1866.da06.b1f5    DYNAMIC     Te1/1/1
 522    1866.da06.b2f4    DYNAMIC     Te1/1/1
 522    1866.da06.b409    DYNAMIC     Te1/1/1
 522    1866.da06.b419    DYNAMIC     Te1/1/1
 522    1866.da06.b42c    DYNAMIC     Te1/1/1
 522    1866.da06.b441    DYNAMIC     Te1/1/1
 522    1866.da06.d350    DYNAMIC     Te1/1/1
 522    1866.da06.f83e    DYNAMIC     Te1/1/1
 522    1866.da27.f9d4    DYNAMIC     Te1/1/1
 522    1866.da2a.bd8b    DYNAMIC     Te1/1/1
 522    1866.da2a.cbab    DYNAMIC     Te1/1/1
 522    1866.da3f.ce7a    DYNAMIC     Te1/1/1
 522    2c59.e576.ef06    DYNAMIC     Te1/1/1
 522    3417.eba7.c170    DYNAMIC     Te1/1/1
 522    3417.eba8.6f33    DYNAMIC     Te1/1/1
 522    3417.eba9.055e    DYNAMIC     Te1/1/1
 522    3417.eba9.85ee    DYNAMIC     Te1/1/1
 522    3417.ebb5.4323    DYNAMIC     Te1/1/1
 522    3417.ebca.4c3e    DYNAMIC     Te1/1/1
 522    3417.ebca.a6ad    DYNAMIC     Te1/1/1
 522    3417.ebca.a988    DYNAMIC     Te1/1/1
 522    3417.ebd4.7126    DYNAMIC     Te1/1/1
 522    40b5.c17d.b982    DYNAMIC     Te1/1/1
 522    484d.7ef4.c41f    DYNAMIC     Te1/1/1
 522    484d.7ef4.c4fa    DYNAMIC     Te1/1/1
 522    484d.7ef4.c6d2    DYNAMIC     Te1/1/1
 522    484d.7ef4.c6e6    DYNAMIC     Te1/1/1
 522    484d.7ef4.dc50    DYNAMIC     Te1/1/1
 522    484d.7ef4.dd4e    DYNAMIC     Te1/1/1
 522    484d.7ef4.df85    DYNAMIC     Te1/1/1
 522    484d.7ef4.df8b    DYNAMIC     Te1/1/1
 522    484d.7ef4.f754    DYNAMIC     Te1/1/1
 522    484d.7ef4.f802    DYNAMIC     Te1/1/1
           522    484d.7ef4.f960    DYNAMIC     Te1/1/1
 522    484d.7ef4.f9e5    DYNAMIC     Te1/1/1
 522    484d.7ef4.fa02    DYNAMIC     Te1/1/1
 522    484d.7ef4.fa12    DYNAMIC     Te1/1/1
 522    484d.7ef4.fa42    DYNAMIC     Te1/1/1
 522    484d.7ef4.fa4b    DYNAMIC     Te1/1/1
 522    484d.7ef4.fa99    DYNAMIC     Te1/1/1
 522    484d.7ef4.fe50    DYNAMIC     Te1/1/1
 522    484d.7ef4.fe87    DYNAMIC     Te1/1/1
 522    484d.7ef4.fef6    DYNAMIC     Te1/1/1
 522    484d.7ef4.ff1c    DYNAMIC     Te1/1/1
 522    484d.7ef5.00bb    DYNAMIC     Te1/1/1
 522    509a.4c42.e1c0    DYNAMIC     Te1/1/1
 522    509a.4c42.e3f5    DYNAMIC     Te1/1/1
 522    509a.4c43.a1e0    DYNAMIC     Te1/1/1
 522    509a.4c43.a561    DYNAMIC     Te1/1/1
 522    509a.4c43.a720    DYNAMIC     Te1/1/1
 522    509a.4c43.a8bc    DYNAMIC     Te1/1/1
 522    509a.4c43.b65a    DYNAMIC     Te1/1/1
 522    509a.4c58.8364    DYNAMIC     Te1/1/1
 522    509a.4c58.8bdf    DYNAMIC     Te1/1/1
 522    509a.4c58.8e83    DYNAMIC     Te1/1/1
 522    509a.4c58.91c4    DYNAMIC     Te1/1/1
 522    509a.4c58.9304    DYNAMIC     Te1/1/1
 522    54bf.6464.8bc4    DYNAMIC     Te1/1/1
 522    54bf.6464.8e86    DYNAMIC     Te1/1/1
 522    54bf.6464.90ac    DYNAMIC     Te1/1/1
 522    54bf.6464.9136    DYNAMIC     Te1/1/1
 522    54bf.6464.91c9    DYNAMIC     Te1/1/1
 522    54bf.6465.5b3d    DYNAMIC     Te1/1/1
 522    54bf.646a.b797    DYNAMIC     Te1/1/1
 522    54bf.646a.bf82    DYNAMIC     Te1/1/1
 522    54bf.646a.c0f6    DYNAMIC     Te1/1/1
 522    54bf.646a.c1e6    DYNAMIC     Te1/1/1
 522    54bf.646a.c255    DYNAMIC     Te1/1/1
 522    54bf.646a.c2cb    DYNAMIC     Te1/1/1
 522    54bf.646a.c2ea    DYNAMIC     Te1/1/1
 522    54bf.646a.c35b    DYNAMIC     Te1/1/1
 522    54bf.646a.c3f6    DYNAMIC     Te1/1/1
 522    54bf.646a.c55c    DYNAMIC     Te1/1/1
 522    54bf.6470.8172    DYNAMIC     Te1/1/1
 522    54bf.6470.8267    DYNAMIC     Te1/1/1
 522    54bf.6470.8284    DYNAMIC     Te1/1/1
 522    54bf.6470.8293    DYNAMIC     Te1/1/1
 522    54bf.649a.fa63    DYNAMIC     Te1/1/1
 522    54bf.649b.04f1    DYNAMIC     Te1/1/1
 522    54bf.649b.9afc    DYNAMIC     Te1/1/1
 522    54bf.649b.9b61    DYNAMIC     Te1/1/1
 522    54bf.649b.9ba0    DYNAMIC     Te1/1/1
 522    54bf.649f.7d5a    DYNAMIC     Te1/1/1
 522    54bf.649f.9dfb    DYNAMIC     Te1/1/1
 522    54bf.649f.a1e8    DYNAMIC     Te1/1/1
 522    54bf.649f.a386    DYNAMIC     Te1/1/1
 522    54bf.649f.a38a    DYNAMIC     Te1/1/1
 522    54bf.649f.a39e    DYNAMIC     Te1/1/1
 522    54bf.649f.a4a8    DYNAMIC     Te1/1/1
 522    54bf.649f.a4ca    DYNAMIC     Te1/1/1
 522    54bf.649f.a5ee    DYNAMIC     Te1/1/1
 522    54bf.649f.a5ff    DYNAMIC     Te1/1/1
           522    54bf.649f.a61e    DYNAMIC     Te1/1/1
 522    54bf.649f.a632    DYNAMIC     Te1/1/1
 522    54bf.649f.b208    DYNAMIC     Te1/1/1
 522    54bf.649f.b264    DYNAMIC     Te1/1/1
 522    5838.793a.70af    DYNAMIC     Te1/1/1
 522    6012.8bff.96e6    DYNAMIC     Te1/1/1
 522    6400.6a5f.98ce    DYNAMIC     Te1/1/1
 522    6400.6a61.e537    DYNAMIC     Te1/1/1
 522    6400.6a96.f492    DYNAMIC     Te1/1/1
 522    6c2b.59d1.8a64    DYNAMIC     Te1/1/1
 522    6c2b.59d1.e5ea    DYNAMIC     Te1/1/1
 522    6c2b.59d1.ed15    DYNAMIC     Te1/1/1
 522    6c2b.59d1.f131    DYNAMIC     Te1/1/1
 522    6c2b.59d1.f20f    DYNAMIC     Te1/1/1
 522    6c2b.59d2.1d91    DYNAMIC     Te1/1/1
 522    6c2b.59de.3651    DYNAMIC     Te1/1/1
 522    6c2b.59ee.7ea9    DYNAMIC     Te1/1/1
 522    6c2b.59ee.82e8    DYNAMIC     Te1/1/1
 522    6c2b.59ee.8484    DYNAMIC     Te1/1/1
 522    6c2b.59ee.908f    DYNAMIC     Te1/1/1
 522    6c2b.59f3.5089    DYNAMIC     Te1/1/1
 522    6c2b.59f3.544b    DYNAMIC     Te1/1/1
 522    6c2b.59f3.79e5    DYNAMIC     Te1/1/1
 522    781c.5af2.56f2    DYNAMIC     Te1/1/1
 522    782b.cb86.63b2    DYNAMIC     Te1/1/1
 522    842b.2b5c.05bb    DYNAMIC     Te1/1/1
 522    84ba.3b1a.5cd3    DYNAMIC     Te1/1/1
 522    90b1.1c70.4d94    DYNAMIC     Te1/1/1
 522    90b1.1c83.3199    DYNAMIC     Te1/1/1
 522    90b1.1c83.3a7b    DYNAMIC     Te1/1/1
 522    90b1.1c92.0097    DYNAMIC     Te1/1/1
 522    90b1.1c92.3b2a    DYNAMIC     Te1/1/1
 522    90b1.1ca0.f9b8    DYNAMIC     Te1/1/1
 522    9890.96a3.d990    DYNAMIC     Te1/1/1
 522    9890.96aa.eb34    DYNAMIC     Te1/1/1
 522    9890.96c0.4121    DYNAMIC     Te1/1/1
 522    9890.96d2.2a93    DYNAMIC     Te1/1/1
 522    9890.96dc.a9bd    DYNAMIC     Te1/1/1
 522    9890.96dc.b6ab    DYNAMIC     Te1/1/1
 522    9890.96dc.ba74    DYNAMIC     Te1/1/1
 522    9890.96dc.bcca    DYNAMIC     Te1/1/1
 522    9890.96dc.bda3    DYNAMIC     Te1/1/1
 522    9890.96dc.bdd8    DYNAMIC     Te1/1/1
 522    9890.96dc.bdee    DYNAMIC     Te1/1/1
 522    9890.96dc.bdf1    DYNAMIC     Te1/1/1
 522    9890.96dc.befd    DYNAMIC     Te1/1/1
 522    9890.96df.d16a    DYNAMIC     Te1/1/1
 522    9890.96df.d197    DYNAMIC     Te1/1/1
 522    9890.96df.d23c    DYNAMIC     Te1/1/1
 522    9890.96df.d52a    DYNAMIC     Te1/1/1
 522    9890.96e2.c9e1    DYNAMIC     Te1/1/1
 522    9890.96e2.d07b    DYNAMIC     Te1/1/1
 522    98e7.f405.a2dc    DYNAMIC     Te1/1/1
 522    a036.9f70.da0f    DYNAMIC     Te1/1/1
 522    a0ce.c816.7acd    DYNAMIC     Te1/1/1
 522    a0ce.c8da.cbba    DYNAMIC     Te1/1/1
 522    a4bb.6d9c.c11e    DYNAMIC     Te1/1/1
 522    a4bb.6d9c.eb23    DYNAMIC     Te1/1/1
 522    a4bb.6d9c.fba3    DYNAMIC     Te1/1/1
           522    a4bb.6d9c.fc9f    DYNAMIC     Te1/1/1
 522    a4bb.6d9e.945e    DYNAMIC     Te1/1/1
 522    a4bb.6dbe.6cbe    DYNAMIC     Te1/1/1
 522    a4bb.6dbe.70ca    DYNAMIC     Te1/1/1
 522    a4bb.6dbf.9336    DYNAMIC     Te1/1/1
 522    a860.b621.64fb    DYNAMIC     Te1/1/1
 522    b022.7a84.77c6    DYNAMIC     Te1/1/1
 522    b0c5.3cee.680a    DYNAMIC     Te1/1/1
 522    b4b6.862f.e0b8    DYNAMIC     Te1/1/1
 522    b8ca.3a91.092d    DYNAMIC     Te1/1/1
 522    b8ca.3aa1.4e89    DYNAMIC     Te1/1/1
 522    b8ca.3aa1.4ef5    DYNAMIC     Te1/1/1
 522    bc4a.5664.45c2    DYNAMIC     Te1/1/1
 522    c465.16d0.c60c    DYNAMIC     Te1/1/1
 522    cc48.3aa8.afcc    DYNAMIC     Te1/1/1
 522    d89e.f319.9689    DYNAMIC     Te1/1/1
 522    d89e.f31c.6b90    DYNAMIC     Te1/1/1
 522    d89e.f31c.6b95    DYNAMIC     Te1/1/1
 522    d89e.f31c.6bca    DYNAMIC     Te1/1/1
 522    d89e.f31c.6be7    DYNAMIC     Te1/1/1
 522    d89e.f31c.7ba2    DYNAMIC     Te1/1/1
 522    d89e.f31c.7c26    DYNAMIC     Te1/1/1
 522    d89e.f31c.7c98    DYNAMIC     Te1/1/1
 522    d89e.f31c.7cb8    DYNAMIC     Te1/1/1
 522    d89e.f31c.7d21    DYNAMIC     Te1/1/1
 522    d89e.f31c.7db2    DYNAMIC     Te1/1/1
 522    d89e.f31c.7f31    DYNAMIC     Te1/1/1
 522    d89e.f31c.7fac    DYNAMIC     Te1/1/1
 522    d89e.f31c.7fae    DYNAMIC     Te1/1/1
 522    d89e.f31c.7fc4    DYNAMIC     Te1/1/1
 522    d89e.f31c.7fc5    DYNAMIC     Te1/1/1
 522    d89e.f325.6909    DYNAMIC     Te1/1/1
 522    d89e.f33d.b230    DYNAMIC     Te1/1/1
 522    d89e.f343.b466    DYNAMIC     Te1/1/1
 522    d89e.f343.b663    DYNAMIC     Te1/1/1
 522    d89e.f343.b7c6    DYNAMIC     Te1/1/1
 522    d89e.f349.7567    DYNAMIC     Te1/1/1
 522    d89e.f349.84d0    DYNAMIC     Te1/1/1
 522    d89e.f349.85bc    DYNAMIC     Te1/1/1
 522    dc4a.3eb0.3dbc    DYNAMIC     Te1/1/1
 522    e454.e888.f330    DYNAMIC     Te1/1/1
 522    e454.e88b.7eb3    DYNAMIC     Te1/1/1
 522    e454.e88b.dfff    DYNAMIC     Te1/1/1
 522    e454.e88b.e8c5    DYNAMIC     Te1/1/1
 522    e454.e88b.e8df    DYNAMIC     Te1/1/1
 522    e454.e88b.edff    DYNAMIC     Te1/1/1
 522    e454.e88b.ef6e    DYNAMIC     Te1/1/1
 522    e454.e88b.efa9    DYNAMIC     Te1/1/1
 522    e454.e88b.efd0    DYNAMIC     Te1/1/1
 522    e454.e88b.f052    DYNAMIC     Te1/1/1
 522    e454.e88b.f1ff    DYNAMIC     Te1/1/1
 522    e454.e88d.2132    DYNAMIC     Te1/1/1
 522    e454.e88d.458a    DYNAMIC     Te1/1/1
 522    e454.e88d.4d62    DYNAMIC     Te1/1/1
 522    e454.e88d.4fc8    DYNAMIC     Te1/1/1
 522    e454.e88d.51cb    DYNAMIC     Te1/1/1
 522    e454.e88d.51e8    DYNAMIC     Te1/1/1
 522    e454.e88d.5206    DYNAMIC     Te1/1/1
 522    e454.e897.a96a    DYNAMIC     Te1/1/1
           522    e454.e897.ae5c    DYNAMIC     Te1/1/1
 522    e454.e897.afe9    DYNAMIC     Te1/1/1
 522    e454.e897.b58c    DYNAMIC     Te1/1/1
 522    e454.e8a6.3cc7    DYNAMIC     Te1/1/1
 522    e454.e8a7.d341    DYNAMIC     Te1/1/1
 522    e454.e8b9.171d    DYNAMIC     Te1/1/1
 522    f48e.38a7.67cd    DYNAMIC     Te1/1/1
 522    f48e.38ab.8fd7    DYNAMIC     Te1/1/1
 522    f8b1.56ce.1bce    DYNAMIC     Te1/1/1
 522    f8b1.56ce.2763    DYNAMIC     Te1/1/1
 522    f8b1.56d1.b06d    DYNAMIC     Te1/1/1
 522    f8b1.56d2.6a45    DYNAMIC     Te1/1/1
 522    f8b1.56da.3cdc    DYNAMIC     Te1/1/1
 522    f8b1.56de.273b    DYNAMIC     Te1/1/1
 415    0000.0c07.ac0a    DYNAMIC     Te1/1/1
 415    40b5.c17d.b982    DYNAMIC     Te1/1/1
 415    b0c5.3cee.680a    DYNAMIC     Te1/1/1
 415    bc4a.5664.45c2    DYNAMIC     Te1/1/1
 307    0000.0c07.ac0a    DYNAMIC     Te1/1/1
 307    b0c5.3cee.680a    DYNAMIC     Te1/1/1
 307    bc4a.5664.45c2    DYNAMIC     Te1/1/1
Total Mac Addresses for this criterion: 311""",
 'show run | section tacacs':"""aaa group server tacacs+ NOC-TAC
 server name TAC-DDC
 server name TAC-PARK
 server name TAC-EBC
 server name TAC-SECONDARY
tacacs-server key 7 100D2339061C410F21573F3B65
tacacs server TAC-DDC
 address ipv4 155.97.160.52
 key 7 100D2339061C410F21573F3B65
tacacs server TAC-PARK
 address ipv4 155.98.253.200
 key 7 01502C245800550B0C1F5B1958
tacacs server TAC-EBC
 address ipv4 172.31.17.180
 key 7 032D1F0E2F4B246E6E0B0044
tacacs server TAC-SECONDARY
 address ipv4 10.64.32.5
 key 7 04724F032665496C291B1C56""",
 'show run | in tacacs':"""aaa group server tacacs+ NOC-TAC
tacacs-server key 7 100D2339061C410F21573F3B65
tacacs server TAC-DDC
tacacs server TAC-PARK
tacacs server TAC-EBC
tacacs server TAC-SECONDARY""",
 'show power inline':"""Module   Available     Used     Remaining
          (Watts)     (Watts)    (Watts) 
------   ---------   --------   ---------
1           775.0        0.0       775.0
Interface Admin  Oper       Power   Device              Class Max
                            (Watts)                            
--------- ------ ---------- ------- ------------------- ----- ----
Gi1/0/1   auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/2   auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/3   auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/4   auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/5   auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/6   auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/7   auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/8   auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/9   auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/10  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/11  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/12  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/13  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/14  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/15  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/16  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/17  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/18  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/19  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/20  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/21  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/22  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/23  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/24  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/25  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/26  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/27  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/28  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/29  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/30  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/31  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/32  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/33  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/34  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/35  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/36  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/37  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/38  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/39  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/40  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/41  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/42  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/43  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/44  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/45  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/46  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/47  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/48  auto   off        0.0     n/a                 n/a   30.0 """,
 'show environment all':"""Switch 1 FAN 1 is OK
Switch 1 FAN 2 is OK
Switch 1 FAN 3 is OK
FAN PS-1 is OK
FAN PS-2 is NOT PRESENT
Switch 1: SYSTEM TEMPERATURE is OK
SW  PID                 Serial#     Status           Sys Pwr  PoE Pwr  Watts
--  ------------------  ----------  ---------------  -------  -------  -----
1A  PWR-C2-1025WAC      DCB1951C0QZ  OK              Good     Good     1025
1B  Not Present       
""",
}
