ip_address = '172.20.72.202'
software = 'software'
hardware = 'hardware'
read_results = {
 'show version':"""Cisco IOS Software, IOS-XE Software, Catalyst L3 Switch Software (CAT3K_CAA-UNIVERSALK9-M), Version 03.06.06E RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2016 by Cisco Systems, Inc.
Compiled Sat 17-Dec-16 00:22 by prod_rel_team



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
BOOTLDR: CAT3K_CAA Boot Loader (CAT3K_CAA-HBOOT-M) Version 1.2, RELEASE SOFTWARE (P)

sx2-SJHC-126-SJHC uptime is 1 year, 13 weeks, 1 day, 2 hours, 58 minutes
Uptime for this control processor is 1 year, 13 weeks, 1 day, 3 hours, 1 minute
System returned to ROM by Power Failure at 12:50:14 MST Wed Jan 2 2019
System restarted at 13:17:51 MDT Wed Mar 25 2020
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
Processor board ID FDO1911E4J1
4 Virtual Ethernet interfaces
48 Gigabit Ethernet interfaces
4 Ten Gigabit Ethernet interfaces
2048K bytes of non-volatile configuration memory.
4194304K bytes of physical memory.
          250456K bytes of Crash Files at crashinfo:.
1609272K bytes of Flash at flash:.
0K bytes of Dummy USB Flash at usbflash0:.
0K bytes of  at webui:.

Base Ethernet MAC Address          : b0:aa:77:af:13:80
Motherboard Assembly Number        : 73-15776-03
Motherboard Serial Number          : FDO191206ST
Model Revision Number              : D0
Motherboard Revision Number        : A0
Model Number                       : WS-C3650-48PQ
System Serial Number               : FDO1911E4J1


Switch Ports Model              SW Version        SW Image              Mode   
------ ----- -----              ----------        ----------            ----   
*    1 52    WS-C3650-48PQ      03.06.06E         cat3k_caa-universalk9 INSTALL


Configuration register is 0x102
""",
 'show run':"""Building configuration...

Current configuration : 17881 bytes
!
! Last configuration change at 20:47:29 MDT Thu Jun 10 2021 by noc-orionncm
! NVRAM config last updated at 21:23:31 MDT Sun Jun 20 2021 by noc-orionncm
!
version 15.2
no service pad
service timestamps debug datetime msec localtime
service timestamps log datetime msec localtime
service password-encryption
service compress-config
!
hostname sx2-SJHC-126-SJHC
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
enable secret 5 $1$DAsR$ksAIPQ7uwWMdBCjXI1oW1.
!
software auto-upgrade enable
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
ip dhcp snooping
!
!
ip device tracking probe delay 10
qos queue-softmax-multiplier 100
vtp domain vtp-3701southjordan
vtp mode transparent
udld aggressive

authentication mac-move permit
!
flow record IPV4
 match ipv4 tos
 match ipv4 protocol
 match ipv4 source address
 match ipv4 destination address
 match transport source-port
 match transport destination-port
 match interface input
 collect interface output
 collect counter bytes long
 collect counter packets long
!
!
flow exporter FLOWCO
 destination 155.98.253.184
 transport udp 2055
!
!
flow monitor NETFLOW
 exporter FLOWCO
 record IPV4
!
!
!
errdisable recovery cause udld
errdisable recovery cause bpduguard
errdisable recovery cause security-violation
errdisable recovery cause channel-misconfig
errdisable recovery cause pagp-flap
errdisable recovery cause dtp-flap
errdisable recovery cause link-flap
errdisable recovery cause sfp-config-mismatch
errdisable recovery cause gbic-invalid
errdisable recovery cause l2ptguard
errdisable recovery cause psecure-violation
errdisable recovery cause port-mode-failure
          errdisable recovery cause dhcp-rate-limit
errdisable recovery cause pppoe-ia-rate-limit
errdisable recovery cause mac-limit
errdisable recovery cause vmps
errdisable recovery cause storm-control
errdisable recovery cause inline-power
errdisable recovery cause arp-inspection
errdisable recovery cause loopback
errdisable recovery cause psp
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
vlan 110
 name SoJo_Flr1-ZeroClients
!
vlan 523
 name Daybreak-1-west
!
vlan 525
 name 3701southjordan-m
!
vlan 527
 name Daybreak-Printer
!
vlan 532
 name sjhc-3701-ucard
!
vlan 953
 name 3701southjordan-voip
!
vlan 1610
 name clin-3701daybreak-fm-cam
lldp run
!
ip tftp blocksize 8192
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
interface GigabitEthernet0/0
 vrf forwarding Mgmt-vrf
 no ip address
 no ip route-cache
 shutdown
 negotiation auto
!
interface GigabitEthernet1/0/1
 description Huntsman
 switchport access vlan 523
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/2
 description Data Voice
 switchport access vlan 110
 switchport mode access
 switchport voice vlan 953
 spanning-tree portfast
!
interface GigabitEthernet1/0/3
 description Data Voice
 switchport access vlan 110
 switchport mode access
 switchport voice vlan 953
 spanning-tree portfast
!
interface GigabitEthernet1/0/4
 description Data Voice
 switchport access vlan 523
 switchport mode access
 switchport voice vlan 953
 spanning-tree portfast
!
interface GigabitEthernet1/0/5
 description Data Voice
 switchport access vlan 523
 switchport mode access
 switchport voice vlan 953
 spanning-tree portfast
!
interface GigabitEthernet1/0/6
 description Printer VLAN
 switchport access vlan 527
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/7
 description Data Voice
 switchport access vlan 523
 switchport mode access
 switchport voice vlan 953
 spanning-tree portfast
!
interface GigabitEthernet1/0/8
           description Data Voice
 switchport access vlan 523
 switchport mode access
 switchport voice vlan 953
 spanning-tree portfast
!
interface GigabitEthernet1/0/9
 description Data Voice
 switchport access vlan 523
 switchport mode access
 switchport voice vlan 953
 spanning-tree portfast
!
interface GigabitEthernet1/0/10
 description Data Voice
 switchport access vlan 523
 switchport mode access
 switchport voice vlan 953
 spanning-tree portfast
!
interface GigabitEthernet1/0/11
 description Data Voice
 switchport access vlan 523
 switchport mode access
 switchport voice vlan 953
 spanning-tree portfast
!
interface GigabitEthernet1/0/12
 description Data Voice
 switchport access vlan 523
 switchport mode access
 switchport voice vlan 953
 spanning-tree portfast
!
interface GigabitEthernet1/0/13
 description Data Voice
 switchport access vlan 523
 switchport mode access
 switchport voice vlan 953
 spanning-tree portfast
!
interface GigabitEthernet1/0/14
 switchport access vlan 523
 switchport mode access
 switchport voice vlan 953
 spanning-tree portfast
!
interface GigabitEthernet1/0/15
 description Data Voice
 switchport access vlan 523
 switchport mode access
 switchport voice vlan 953
 spanning-tree portfast
!
interface GigabitEthernet1/0/16
 description Printer VLAN
 switchport access vlan 527
 switchport mode access
 spanning-tree portfast
          !
interface GigabitEthernet1/0/17
 description Data Voice
 switchport access vlan 110
 switchport mode access
 switchport voice vlan 953
 spanning-tree portfast
!
interface GigabitEthernet1/0/18
 description Data Voice
 switchport access vlan 523
 switchport mode access
 switchport voice vlan 953
 spanning-tree portfast
!
interface GigabitEthernet1/0/19
 description Data Voice
 switchport access vlan 523
 switchport mode access
 switchport voice vlan 953
 spanning-tree portfast
!
interface GigabitEthernet1/0/20
 description Data Voice
 switchport access vlan 523
 switchport mode access
 switchport voice vlan 953
 spanning-tree portfast
!
interface GigabitEthernet1/0/21
 description Controler 
 switchport access vlan 523
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/22
 description Data Voice
 switchport access vlan 110
 switchport mode access
 switchport voice vlan 953
 spanning-tree portfast
!
interface GigabitEthernet1/0/23
 description Controler
 switchport access vlan 523
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/24
 description Data Voice
 switchport access vlan 523
 switchport mode access
 switchport voice vlan 953
 spanning-tree portfast
!
interface GigabitEthernet1/0/25
 description Data Voice
 switchport access vlan 110
 switchport mode access
           switchport voice vlan 953
 spanning-tree portfast
!
interface GigabitEthernet1/0/26
 description Data Voice
 switchport access vlan 523
 switchport mode access
 switchport voice vlan 953
 spanning-tree portfast
!
interface GigabitEthernet1/0/27
 description FM CAM
 switchport access vlan 110
 switchport mode access
 switchport voice vlan 953
 spanning-tree portfast
!
interface GigabitEthernet1/0/28
 description FM CAM
 switchport access vlan 1610
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/29
 description Controler 
 switchport access vlan 523
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/30
 description FM CAM
 switchport access vlan 1610
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/31
 description FM CAM
 switchport access vlan 1610
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/32
 description FM CAM
 switchport access vlan 1610
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/33
 description FM CAM
 switchport access vlan 1610
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/34
 description FM CAM
 switchport access vlan 110
 switchport mode access
 switchport voice vlan 953
 spanning-tree portfast
          !
interface GigabitEthernet1/0/35
 description FM CAM
 switchport access vlan 1610
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/36
 description FM CAM
 switchport access vlan 110
 switchport mode access
 switchport voice vlan 953
 spanning-tree portfast
!
interface GigabitEthernet1/0/37
 description Printer
 switchport access vlan 527
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/38
 description Data for ER entance
 switchport access vlan 523
 switchport mode access
 switchport voice vlan 953
 spanning-tree portfast
!
interface GigabitEthernet1/0/39
 description FM CAM
 switchport access vlan 1610
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/40
 description FM CAM
 switchport access vlan 1610
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/41
 description Printer VLAN
 switchport access vlan 527
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/42
 description Printer VLAN
 switchport access vlan 527
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/43
 description Printer VLAN
 switchport access vlan 527
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/44
 description Printer VLAN
           switchport access vlan 527
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/45
 switchport access vlan 523
 switchport mode access
 switchport voice vlan 953
 spanning-tree portfast
!
interface GigabitEthernet1/0/46
 switchport access vlan 523
 switchport mode access
 switchport voice vlan 953
 spanning-tree portfast
!
interface GigabitEthernet1/0/47
 description Printer VLAN
 switchport access vlan 532
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/48
 description Printer VLAN
 switchport access vlan 532
 switchport mode access
 spanning-tree portfast
!
interface TenGigabitEthernet1/1/1
!
interface TenGigabitEthernet1/1/2
!
interface TenGigabitEthernet1/1/3
 description key:t1/1/3:r2-3701SJHC-bo22:t1/10
 switchport mode trunk
 switchport priority extend trust
 ip dhcp snooping trust
!
interface TenGigabitEthernet1/1/4
 description key:t1/1/4:r1-3701SJHC-bo22:t1/10
 switchport mode trunk
 switchport priority extend trust
 ip dhcp snooping trust
!
interface Vlan1
 no ip address
 no ip route-cache
 shutdown
!
interface Vlan525
 description 3701southjordan-m
 ip address 172.20.72.202 255.255.255.224
 no ip route-cache
!
interface Vlan1610
 no ip address
!
interface Vlan1616
 no ip address
          !
ip default-gateway 172.20.72.193
ip forward-protocol nd
no ip http server
no ip http secure-server
ip ssh version 2
!
!
ip sla enable reaction-alerts
logging facility local6
logging source-interface Vlan525
logging host 155.98.204.52
logging host 155.98.253.244
logging host 10.71.24.11
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
snmp-server group CliNOCGrv3RO v3 priv read CliNOCViewRO access 70
snmp-server group CliNOCGrv3RO v3 auth context vlan- match prefix 
snmp-server group CliNOCGrv3RW v3 priv write CliNOCViewRW access 71
snmp-server view VoicePhones internet included
snmp-server view CliNOCViewRO internet included
snmp-server view CliNOCViewRW internet included
snmp-server location Bldg. 3701 Room 1W
snmp-server contact BC-506589 Y-Y-061769
snmp ifmib ifindex persist
          tacacs server TAC-EBC
 address ipv4 172.31.17.180
 key 7 0808084B205D003532091545
tacacs server TAC-SECONDARY
 address ipv4 10.64.32.5
 key 7 032D1F0E2F4B246E6E0B0044
!
!
!
privilege exec level 1 show configuration
privilege exec level 1 show
banner login ^C

sx2-3701SJHC-126-SJHC


          
University of Utah Network:  All use of this device must comply
with the University of Utah policies and procedures.  Any use of
this device, whether deliberate or not will be hnetwork should be reported
by calling the Campus Helpdesk at 581-4000, or via e-mail 
at
helpdesk@utah.edu

DO NOT LOGIN
if you are not authorized by NetCom at the University of Utah.


^C
!
line con 0
 exec-timeout 15 0
 password 7 107B1D180D15535858
 login authentication console
 stopbits 1
line aux 0
 stopbits 1
line vty 0 4
 access-class 199 in
 exec-timeout 30 0
 password 7 0814584F011B444446
 transport input ssh
line vty 5 15
 access-class 199 in
 exec-timeout 30 0
 password 7 0814584F011B444446
 transport input ssh
!
ntp server time.utah.edu
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
Gi1/0/1   Huntsman           notconnect   523          auto   auto 10/100/1000BaseTX
Gi1/0/2   Data Voice         connected    110        a-full a-1000 10/100/1000BaseTX
Gi1/0/3   Data Voice         notconnect   110          auto   auto 10/100/1000BaseTX
Gi1/0/4   Data Voice         connected    523        a-full  a-100 10/100/1000BaseTX
Gi1/0/5   Data Voice         connected    523        a-full  a-100 10/100/1000BaseTX
Gi1/0/6   Printer VLAN       connected    527        a-full  a-100 10/100/1000BaseTX
Gi1/0/7   Data Voice         connected    523        a-full a-1000 10/100/1000BaseTX
Gi1/0/8   Data Voice         connected    523        a-full a-1000 10/100/1000BaseTX
Gi1/0/9   Data Voice         connected    523        a-full a-1000 10/100/1000BaseTX
Gi1/0/10  Data Voice         connected    523        a-full a-1000 10/100/1000BaseTX
Gi1/0/11  Data Voice         connected    523        a-full a-1000 10/100/1000BaseTX
Gi1/0/12  Data Voice         connected    523        a-full a-1000 10/100/1000BaseTX
Gi1/0/13  Data Voice         connected    523        a-full a-1000 10/100/1000BaseTX
Gi1/0/14                     connected    523        a-full a-1000 10/100/1000BaseTX
Gi1/0/15  Data Voice         connected    523        a-full a-1000 10/100/1000BaseTX
Gi1/0/16  Printer VLAN       connected    527        a-full a-1000 10/100/1000BaseTX
Gi1/0/17  Data Voice         connected    110        a-full  a-100 10/100/1000BaseTX
Gi1/0/18  Data Voice         connected    523        a-half  a-100 10/100/1000BaseTX
Gi1/0/19  Data Voice         notconnect   523          auto   auto 10/100/1000BaseTX
Gi1/0/20  Data Voice         notconnect   523          auto   auto 10/100/1000BaseTX
Gi1/0/21  Controler          connected    523        a-full a-1000 10/100/1000BaseTX
Gi1/0/22  Data Voice         connected    110        a-full a-1000 10/100/1000BaseTX
Gi1/0/23  Controler          connected    523        a-full  a-100 10/100/1000BaseTX
Gi1/0/24  Data Voice         notconnect   523          auto   auto 10/100/1000BaseTX
Gi1/0/25  Data Voice         connected    110        a-full a-1000 10/100/1000BaseTX
Gi1/0/26  Data Voice         connected    523        a-full a-1000 10/100/1000BaseTX
Gi1/0/27  FM CAM             connected    110        a-full a-1000 10/100/1000BaseTX
Gi1/0/28  FM CAM             notconnect   1610         auto   auto 10/100/1000BaseTX
Gi1/0/29  Controler          connected    523        a-full  a-100 10/100/1000BaseTX
Gi1/0/30  FM CAM             notconnect   1610         auto   auto 10/100/1000BaseTX
Gi1/0/31  FM CAM             notconnect   1610         auto   auto 10/100/1000BaseTX
Gi1/0/32  FM CAM             notconnect   1610         auto   auto 10/100/1000BaseTX
Gi1/0/33  FM CAM             notconnect   1610         auto   auto 10/100/1000BaseTX
Gi1/0/34  FM CAM             connected    110        a-full a-1000 10/100/1000BaseTX
Gi1/0/35  FM CAM             notconnect   1610         auto   auto 10/100/1000BaseTX
Gi1/0/36  FM CAM             connected    110        a-full a-1000 10/100/1000BaseTX
Gi1/0/37  Printer            notconnect   527          auto   auto 10/100/1000BaseTX
Gi1/0/38  Data for ER entanc notconnect   523          auto   auto 10/100/1000BaseTX
Gi1/0/39  FM CAM             notconnect   1610         auto   auto 10/100/1000BaseTX
Gi1/0/40  FM CAM             notconnect   1610         auto   auto 10/100/1000BaseTX
Gi1/0/41  Printer VLAN       connected    527        a-full  a-100 10/100/1000BaseTX
Gi1/0/42  Printer VLAN       connected    527        a-full a-1000 10/100/1000BaseTX
Gi1/0/43  Printer VLAN       connected    527        a-full  a-100 10/100/1000BaseTX
Gi1/0/44  Printer VLAN       notconnect   527          auto   auto 10/100/1000BaseTX
Gi1/0/45                     notconnect   523          auto   auto 10/100/1000BaseTX
Gi1/0/46                     notconnect   523          auto   auto 10/100/1000BaseTX
Gi1/0/47  Printer VLAN       connected    532        a-half   a-10 10/100/1000BaseTX
Gi1/0/48  Printer VLAN       connected    532        a-half   a-10 10/100/1000BaseTX
Te1/1/1                      notconnect   1            auto   auto unknown
Te1/1/2                      notconnect   1            auto   auto unknown
Te1/1/3   key:t1/1/3:r2-3701 connected    trunk        full    10G SFP-10GBase-SR
Te1/1/4   key:t1/1/4:r1-3701 connected    trunk        full    10G SFP-10GBase-LR""",
 'show run | section interface':"""match interface input
 collect interface output
interface GigabitEthernet0/0
 vrf forwarding Mgmt-vrf
 no ip address
 no ip route-cache
 shutdown
 negotiation auto
interface GigabitEthernet1/0/1
 description Huntsman
 switchport access vlan 523
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/2
 description Data Voice
 switchport access vlan 110
 switchport mode access
 switchport voice vlan 953
 spanning-tree portfast
interface GigabitEthernet1/0/3
 description Data Voice
 switchport access vlan 110
 switchport mode access
 switchport voice vlan 953
 spanning-tree portfast
interface GigabitEthernet1/0/4
 description Data Voice
 switchport access vlan 523
 switchport mode access
 switchport voice vlan 953
 spanning-tree portfast
interface GigabitEthernet1/0/5
 description Data Voice
 switchport access vlan 523
 switchport mode access
 switchport voice vlan 953
 spanning-tree portfast
interface GigabitEthernet1/0/6
 description Printer VLAN
 switchport access vlan 527
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/7
 description Data Voice
 switchport access vlan 523
 switchport mode access
 switchport voice vlan 953
 spanning-tree portfast
interface GigabitEthernet1/0/8
 description Data Voice
 switchport access vlan 523
 switchport mode access
 switchport voice vlan 953
 spanning-tree portfast
interface GigabitEthernet1/0/9
 description Data Voice
 switchport access vlan 523
 switchport mode access
 switchport voice vlan 953
           spanning-tree portfast
interface GigabitEthernet1/0/10
 description Data Voice
 switchport access vlan 523
 switchport mode access
 switchport voice vlan 953
 spanning-tree portfast
interface GigabitEthernet1/0/11
 description Data Voice
 switchport access vlan 523
 switchport mode access
 switchport voice vlan 953
 spanning-tree portfast
interface GigabitEthernet1/0/12
 description Data Voice
 switchport access vlan 523
 switchport mode access
 switchport voice vlan 953
 spanning-tree portfast
interface GigabitEthernet1/0/13
 description Data Voice
 switchport access vlan 523
 switchport mode access
 switchport voice vlan 953
 spanning-tree portfast
interface GigabitEthernet1/0/14
 switchport access vlan 523
 switchport mode access
 switchport voice vlan 953
 spanning-tree portfast
interface GigabitEthernet1/0/15
 description Data Voice
 switchport access vlan 523
 switchport mode access
 switchport voice vlan 953
 spanning-tree portfast
interface GigabitEthernet1/0/16
 description Printer VLAN
 switchport access vlan 527
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/17
 description Data Voice
 switchport access vlan 110
 switchport mode access
 switchport voice vlan 953
 spanning-tree portfast
interface GigabitEthernet1/0/18
 description Data Voice
 switchport access vlan 523
 switchport mode access
 switchport voice vlan 953
 spanning-tree portfast
interface GigabitEthernet1/0/19
 description Data Voice
 switchport access vlan 523
 switchport mode access
 switchport voice vlan 953
 spanning-tree portfast
          interface GigabitEthernet1/0/20
 description Data Voice
 switchport access vlan 523
 switchport mode access
 switchport voice vlan 953
 spanning-tree portfast
interface GigabitEthernet1/0/21
 description Controler 
 switchport access vlan 523
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/22
 description Data Voice
 switchport access vlan 110
 switchport mode access
 switchport voice vlan 953
 spanning-tree portfast
interface GigabitEthernet1/0/23
 description Controler
 switchport access vlan 523
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/24
 description Data Voice
 switchport access vlan 523
 switchport mode access
 switchport voice vlan 953
 spanning-tree portfast
interface GigabitEthernet1/0/25
 description Data Voice
 switchport access vlan 110
 switchport mode access
 switchport voice vlan 953
 spanning-tree portfast
interface GigabitEthernet1/0/26
 description Data Voice
 switchport access vlan 523
 switchport mode access
 switchport voice vlan 953
 spanning-tree portfast
interface GigabitEthernet1/0/27
 description FM CAM
 switchport access vlan 110
 switchport mode access
 switchport voice vlan 953
 spanning-tree portfast
interface GigabitEthernet1/0/28
 description FM CAM
 switchport access vlan 1610
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/29
 description Controler 
 switchport access vlan 523
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/30
 description FM CAM
 switchport access vlan 1610
           switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/31
 description FM CAM
 switchport access vlan 1610
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/32
 description FM CAM
 switchport access vlan 1610
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/33
 description FM CAM
 switchport access vlan 1610
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/34
 description FM CAM
 switchport access vlan 110
 switchport mode access
 switchport voice vlan 953
 spanning-tree portfast
interface GigabitEthernet1/0/35
 description FM CAM
 switchport access vlan 1610
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/36
 description FM CAM
 switchport access vlan 110
 switchport mode access
 switchport voice vlan 953
 spanning-tree portfast
interface GigabitEthernet1/0/37
 description Printer
 switchport access vlan 527
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/38
 description Data for ER entance
 switchport access vlan 523
 switchport mode access
 switchport voice vlan 953
 spanning-tree portfast
interface GigabitEthernet1/0/39
 description FM CAM
 switchport access vlan 1610
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/40
 description FM CAM
 switchport access vlan 1610
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/41
 description Printer VLAN
 switchport access vlan 527
 switchport mode access
           spanning-tree portfast
interface GigabitEthernet1/0/42
 description Printer VLAN
 switchport access vlan 527
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/43
 description Printer VLAN
 switchport access vlan 527
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/44
 description Printer VLAN
 switchport access vlan 527
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/45
 switchport access vlan 523
 switchport mode access
 switchport voice vlan 953
 spanning-tree portfast
interface GigabitEthernet1/0/46
 switchport access vlan 523
 switchport mode access
 switchport voice vlan 953
 spanning-tree portfast
interface GigabitEthernet1/0/47
 description Printer VLAN
 switchport access vlan 532
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/48
 description Printer VLAN
 switchport access vlan 532
 switchport mode access
 spanning-tree portfast
interface TenGigabitEthernet1/1/1
interface TenGigabitEthernet1/1/2
interface TenGigabitEthernet1/1/3
 description key:t1/1/3:r2-3701SJHC-bo22:t1/10
 switchport mode trunk
 switchport priority extend trust
 ip dhcp snooping trust
interface TenGigabitEthernet1/1/4
 description key:t1/1/4:r1-3701SJHC-bo22:t1/10
 switchport mode trunk
 switchport priority extend trust
 ip dhcp snooping trust
interface Vlan1
 no ip address
 no ip route-cache
 shutdown
interface Vlan525
 description 3701southjordan-m
 ip address 172.20.72.202 255.255.255.224
 no ip route-cache
interface Vlan1610
 no ip address
interface Vlan1616
           no ip address
logging source-interface Vlan525""",
 'show run | in interface':"""match interface input
 collect interface output
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
interface Vlan525
interface Vlan1610
interface Vlan1616
          logging source-interface Vlan525""",
 'show interface link':"""^
% Invalid input detected at '^' marker.
""",
 'show interface':"""Vlan1 is administratively down, line protocol is down 
  Hardware is Ethernet SVI, address is b0aa.77af.13c7 (bia b0aa.77af.13c7)
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
     16701961 packets input, 2655199526 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 1 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Vlan525 is up, line protocol is up 
  Hardware is Ethernet SVI, address is b0aa.77af.13f8 (bia b0aa.77af.13f8)
  Description: 3701southjordan-m
  Internet address is 172.20.72.202/27
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
  5 minute input rate 9000 bits/sec, 7 packets/sec
  5 minute output rate 5000 bits/sec, 4 packets/sec
     369342364 packets input, 62009571970 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     129978617 packets output, 35103324141 bytes, 0 underruns
     0 output errors, 2 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Vlan1610 is up, line protocol is up 
  Hardware is Ethernet SVI, address is b0aa.77af.13e7 (bia b0aa.77af.13e7)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:01, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
            5 minute output rate 0 bits/sec, 0 packets/sec
     125293791 packets input, 13743165175 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 2 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Vlan1616 is down, line protocol is down 
  Hardware is Ethernet SVI, address is b0aa.77af.13d8 (bia b0aa.77af.13d8)
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
     0 output errors, 0 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet0/0 is administratively down, line protocol is down 
  NOTE: Packet counters for management port are meaningful 
        only when it is physically located at stack master
  Hardware is RP management port, address is b0aa.77af.1380 (bia b0aa.77af.1380)
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
  Hardware is Gigabit Ethernet, address is b0aa.77af.1381 (bia b0aa.77af.1381)
  Description: Huntsman
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
GigabitEthernet1/0/2 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is b0aa.77af.1382 (bia b0aa.77af.1382)
  Description: Data Voice
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 20w3d, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 2000 bits/sec, 3 packets/sec
     51841592 packets input, 3495504496 bytes, 0 no buffer
     Received 33092 broadcasts (16 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 16 multicast, 0 pause input
     0 input packets with dribble condition detected
     160176082 packets output, 35435562658 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
          GigabitEthernet1/0/3 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is b0aa.77af.1383 (bia b0aa.77af.1383)
  Description: Data Voice
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
GigabitEthernet1/0/4 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is b0aa.77af.1384 (bia b0aa.77af.1384)
  Description: Data Voice
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:40:03, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 3000 bits/sec, 5 packets/sec
     261113525 packets input, 357686234145 bytes, 0 no buffer
     Received 170830 broadcasts (94302 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 94302 multicast, 0 pause input
     0 input packets with dribble condition detected
     226540810 packets output, 24341768773 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/5 is up, line protocol is up (connected) 
            Hardware is Gigabit Ethernet, address is b0aa.77af.1385 (bia b0aa.77af.1385)
  Description: Data Voice
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:01:05, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 721763721
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 8000 bits/sec, 7 packets/sec
     93207377 packets input, 11281557281 bytes, 0 no buffer
     Received 3778237 broadcasts (3588426 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 3588426 multicast, 0 pause input
     0 input packets with dribble condition detected
     415852446 packets output, 94004827510 bytes, 0 underruns
     721763721 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/6 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is b0aa.77af.1386 (bia b0aa.77af.1386)
  Description: Printer VLAN
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:01:44, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 7000 bits/sec, 13 packets/sec
     1091969 packets input, 85146325 bytes, 0 no buffer
     Received 696279 broadcasts (672418 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 672418 multicast, 0 pause input
     0 input packets with dribble condition detected
     772316984 packets output, 54059024379 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/7 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is b0aa.77af.1387 (bia b0aa.77af.1387)
            Description: Data Voice
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:01:09, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 3780332
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 16000 bits/sec, 17 packets/sec
  5 minute output rate 45000 bits/sec, 20 packets/sec
     759866693 packets input, 162210483007 bytes, 0 no buffer
     Received 4383547 broadcasts (4204774 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 4204774 multicast, 0 pause input
     0 input packets with dribble condition detected
     1241181424 packets output, 714619986793 bytes, 0 underruns
     3780332 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/8 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is b0aa.77af.1388 (bia b0aa.77af.1388)
  Description: Data Voice
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:13:03, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 6088
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 13000 bits/sec, 8 packets/sec
  5 minute output rate 23000 bits/sec, 15 packets/sec
     383397123 packets input, 175951143716 bytes, 0 no buffer
     Received 2873186 broadcasts (2752795 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 2752795 multicast, 0 pause input
     0 input packets with dribble condition detected
     713317583 packets output, 267071647370 bytes, 0 underruns
     6088 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/9 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is b0aa.77af.1389 (bia b0aa.77af.1389)
  Description: Data Voice
            MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:14, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 6475650
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 10000 bits/sec, 6 packets/sec
  5 minute output rate 38000 bits/sec, 13 packets/sec
     1318551254 packets input, 329063218079 bytes, 0 no buffer
     Received 5328128 broadcasts (5166861 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 5166861 multicast, 0 pause input
     0 input packets with dribble condition detected
     1869047119 packets output, 1388584145302 bytes, 0 underruns
     6475650 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/10 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is b0aa.77af.138a (bia b0aa.77af.138a)
  Description: Data Voice
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:02, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 1275997
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 22000 bits/sec, 9 packets/sec
  5 minute output rate 42000 bits/sec, 16 packets/sec
     812603197 packets input, 233786284965 bytes, 0 no buffer
     Received 5402168 broadcasts (5158248 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 5158248 multicast, 0 pause input
     0 input packets with dribble condition detected
     1241674391 packets output, 814213749884 bytes, 0 underruns
     1275997 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/11 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is b0aa.77af.138b (bia b0aa.77af.138b)
  Description: Data Voice
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
               reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:25, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 2259754
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 31000 bits/sec, 5 packets/sec
  5 minute output rate 64000 bits/sec, 11 packets/sec
     700388593 packets input, 168694284607 bytes, 0 no buffer
     Received 5234505 broadcasts (5012024 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 5012024 multicast, 0 pause input
     0 input packets with dribble condition detected
     1112037974 packets output, 661920878519 bytes, 0 underruns
     2259754 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/12 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is b0aa.77af.138c (bia b0aa.77af.138c)
  Description: Data Voice
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:25, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 3985787
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 5000 bits/sec, 4 packets/sec
  5 minute output rate 13000 bits/sec, 11 packets/sec
     340544880 packets input, 126473446458 bytes, 0 no buffer
     Received 4571838 broadcasts (4136275 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 4136275 multicast, 0 pause input
     0 input packets with dribble condition detected
     674850261 packets output, 259961044774 bytes, 0 underruns
     3985787 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/13 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is b0aa.77af.138d (bia b0aa.77af.138d)
  Description: Data Voice
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
            Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:01, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 4000 bits/sec, 5 packets/sec
     9311265 packets input, 3422140909 bytes, 0 no buffer
     Received 1316513 broadcasts (1316484 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 1316484 multicast, 0 pause input
     0 input packets with dribble condition detected
     258541398 packets output, 30792587495 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/14 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is b0aa.77af.138e (bia b0aa.77af.138e)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:10, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 475047
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 11000 bits/sec, 5 packets/sec
  5 minute output rate 24000 bits/sec, 12 packets/sec
     254391670 packets input, 75121071111 bytes, 0 no buffer
     Received 2693323 broadcasts (2608723 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 2608723 multicast, 0 pause input
     0 input packets with dribble condition detected
     478630629 packets output, 212986307089 bytes, 0 underruns
     475047 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/15 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is b0aa.77af.138f (bia b0aa.77af.138f)
  Description: Data Voice
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
            Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:11:44, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 1706307
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 20000 bits/sec, 29 packets/sec
  5 minute output rate 89000 bits/sec, 28 packets/sec
     796990198 packets input, 158603709754 bytes, 0 no buffer
     Received 6463289 broadcasts (6232973 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 6232973 multicast, 0 pause input
     0 input packets with dribble condition detected
     1527494528 packets output, 915917939222 bytes, 0 underruns
     1706307 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/16 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is b0aa.77af.1390 (bia b0aa.77af.1390)
  Description: Printer VLAN
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 8000 bits/sec, 13 packets/sec
     3766629 packets input, 342683025 bytes, 0 no buffer
     Received 784891 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     458360963 packets output, 32934169218 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/17 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is b0aa.77af.1391 (bia b0aa.77af.1391)
  Description: Data Voice
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
            input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 1000 bits/sec, 2 packets/sec
  5 minute output rate 3000 bits/sec, 5 packets/sec
     45947898 packets input, 3677806287 bytes, 0 no buffer
     Received 10526 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     118478120 packets output, 9623164865 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/18 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is b0aa.77af.1392 (bia b0aa.77af.1392)
  Description: Data Voice
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Half-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 02:06:49, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 8000 bits/sec, 7 packets/sec
     10677870 packets input, 7981166057 bytes, 0 no buffer
     Received 751836 broadcasts (700209 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 700209 multicast, 0 pause input
     0 input packets with dribble condition detected
     345126303 packets output, 53265167942 bytes, 0 underruns
     28260 output errors, 4442 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 3586 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/19 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is b0aa.77af.1393 (bia b0aa.77af.1393)
  Description: Data Voice
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
     23119627 packets input, 2897549916 bytes, 0 no buffer
     Received 1249594 broadcasts (1063561 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 1063561 multicast, 0 pause input
     0 input packets with dribble condition detected
     210437708 packets output, 39161810903 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/20 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is b0aa.77af.1394 (bia b0aa.77af.1394)
  Description: Data Voice
  MTU 1500 bytes, BW 10000 Kbit/sec, DLY 1000 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 11w4d, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 265998
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     656419531 packets input, 165652586329 bytes, 0 no buffer
     Received 3150907 broadcasts (3020512 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 3020512 multicast, 2 pause input
     0 input packets with dribble condition detected
     1084188717 packets output, 798036658448 bytes, 0 underruns
     265998 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/21 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is b0aa.77af.1395 (bia b0aa.77af.1395)
  Description: Controler 
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
            Last input 00:04:04, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 795791
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 54000 bits/sec, 30 packets/sec
  5 minute output rate 43000 bits/sec, 28 packets/sec
     280790906 packets input, 123623245265 bytes, 0 no buffer
     Received 637469 broadcasts (615304 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 615304 multicast, 0 pause input
     0 input packets with dribble condition detected
     250955291 packets output, 65870368124 bytes, 0 underruns
     795791 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/22 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is b0aa.77af.1396 (bia b0aa.77af.1396)
  Description: Data Voice
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:11, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 2000 bits/sec, 3 packets/sec
     13855385 packets input, 1114034207 bytes, 0 no buffer
     Received 602918 broadcasts (588272 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 588272 multicast, 0 pause input
     0 input packets with dribble condition detected
     72354445 packets output, 9184297332 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/23 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is b0aa.77af.1397 (bia b0aa.77af.1397)
  Description: Controler
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
            Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 5000 bits/sec, 4 packets/sec
     23676857 packets input, 1830577165 bytes, 0 no buffer
     Received 59065 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     58505517 packets output, 6390670581 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/24 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is b0aa.77af.1398 (bia b0aa.77af.1398)
  Description: Data Voice
  MTU 1500 bytes, BW 10000 Kbit/sec, DLY 1000 usec, 
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
     158303275 packets input, 12336434298 bytes, 0 no buffer
     Received 246211 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     86 input errors, 86 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     343984880 packets output, 35181683439 bytes, 0 underruns
     85631 output errors, 31990 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/25 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is b0aa.77af.1399 (bia b0aa.77af.1399)
  Description: Data Voice
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 1w1d, output never, output hang never
  Last clearing of "" counters never
            Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 1000 bits/sec, 1 packets/sec
  5 minute output rate 3000 bits/sec, 4 packets/sec
     97133218 packets input, 6742759726 bytes, 0 no buffer
     Received 33097 broadcasts (57 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 57 multicast, 0 pause input
     0 input packets with dribble condition detected
     202015645 packets output, 74616462828 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/26 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is b0aa.77af.139a (bia b0aa.77af.139a)
  Description: Data Voice
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:58, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 10000 bits/sec, 6 packets/sec
  5 minute output rate 24000 bits/sec, 15 packets/sec
     220783800 packets input, 55951557892 bytes, 0 no buffer
     Received 2237362 broadcasts (2206043 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 2206043 multicast, 1 pause input
     0 input packets with dribble condition detected
     405409146 packets output, 287940407645 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/27 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is b0aa.77af.139b (bia b0aa.77af.139b)
  Description: FM CAM
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:03, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
            Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 2000 bits/sec, 4 packets/sec
     46438702 packets input, 3581799094 bytes, 0 no buffer
     Received 606944 broadcasts (588284 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 588284 multicast, 0 pause input
     0 input packets with dribble condition detected
     107246609 packets output, 38054975056 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/28 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is b0aa.77af.139c (bia b0aa.77af.139c)
  Description: FM CAM
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
     45 packets input, 26730 bytes, 0 no buffer
     Received 45 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     530 packets output, 95745 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/29 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is b0aa.77af.139d (bia b0aa.77af.139d)
  Description: Controler 
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
            Output queue: 0/40 (size/max)
  5 minute input rate 3000 bits/sec, 5 packets/sec
  5 minute output rate 7000 bits/sec, 8 packets/sec
     31000298 packets input, 2406824580 bytes, 0 no buffer
     Received 61420 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     64716954 packets output, 6940630676 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/30 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is b0aa.77af.139e (bia b0aa.77af.139e)
  Description: FM CAM
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
  Hardware is Gigabit Ethernet, address is b0aa.77af.139f (bia b0aa.77af.139f)
  Description: FM CAM
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
  Hardware is Gigabit Ethernet, address is b0aa.77af.13a0 (bia b0aa.77af.13a0)
  Description: FM CAM
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
     2 packets input, 1188 bytes, 0 no buffer
     Received 2 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     46 packets output, 7596 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/33 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is b0aa.77af.13a1 (bia b0aa.77af.13a1)
  Description: FM CAM
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
GigabitEthernet1/0/34 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is b0aa.77af.13a2 (bia b0aa.77af.13a2)
  Description: FM CAM
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:08, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 2000 bits/sec, 4 packets/sec
     53504464 packets input, 4233697893 bytes, 0 no buffer
     Received 603786 broadcasts (588291 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 588291 multicast, 0 pause input
     0 input packets with dribble condition detected
     116299772 packets output, 45705276134 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/35 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is b0aa.77af.13a3 (bia b0aa.77af.13a3)
  Description: FM CAM
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
               5 packets input, 2970 bytes, 0 no buffer
     Received 5 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     57 packets output, 11436 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/36 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is b0aa.77af.13a4 (bia b0aa.77af.13a4)
  Description: FM CAM
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:14, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 2000 bits/sec, 4 packets/sec
     19422965 packets input, 1525080074 bytes, 0 no buffer
     Received 603331 broadcasts (588268 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 588268 multicast, 0 pause input
     0 input packets with dribble condition detected
     78175374 packets output, 14742351363 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/37 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is b0aa.77af.13a5 (bia b0aa.77af.13a5)
  Description: Printer
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 11w4d, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     1990465 packets input, 182492041 bytes, 0 no buffer
               Received 660743 broadcasts (624784 multicasts)
     0 runts, 0 giants, 0 throttles 
     1 input errors, 1 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 624784 multicast, 0 pause input
     0 input packets with dribble condition detected
     622893353 packets output, 43742415426 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/38 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is b0aa.77af.13a6 (bia b0aa.77af.13a6)
  Description: Data for ER entance
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 11w4d, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 2864929
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     950908782 packets input, 187811797735 bytes, 0 no buffer
     Received 4855022 broadcasts (4710385 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 4710385 multicast, 0 pause input
     0 input packets with dribble condition detected
     1664114569 packets output, 1595089404324 bytes, 0 underruns
     2864929 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/39 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is b0aa.77af.13a7 (bia b0aa.77af.13a7)
  Description: FM CAM
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
     1 packets input, 594 bytes, 0 no buffer
     Received 1 broadcasts (0 multicasts)
               0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     32 packets output, 5390 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/40 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is b0aa.77af.13a8 (bia b0aa.77af.13a8)
  Description: FM CAM
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
     33 packets input, 19602 bytes, 0 no buffer
     Received 33 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     484 packets output, 82846 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/41 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is b0aa.77af.13a9 (bia b0aa.77af.13a9)
  Description: Printer VLAN
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:03:11, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 7000 bits/sec, 12 packets/sec
     359674 packets input, 33749681 bytes, 0 no buffer
     Received 64865 broadcasts (61389 multicasts)
     0 runts, 0 giants, 0 throttles 
               0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 61389 multicast, 0 pause input
     0 input packets with dribble condition detected
     58822461 packets output, 4060626515 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/42 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is b0aa.77af.13aa (bia b0aa.77af.13aa)
  Description: Printer VLAN
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:02:12, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 8000 bits/sec, 13 packets/sec
     24689464 packets input, 3311501851 bytes, 0 no buffer
     Received 3785881 broadcasts (2110778 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 2110778 multicast, 0 pause input
     0 input packets with dribble condition detected
     804504101 packets output, 76041244553 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/43 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is b0aa.77af.13ab (bia b0aa.77af.13ab)
  Description: Printer VLAN
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 7000 bits/sec, 12 packets/sec
     5105303 packets input, 507516719 bytes, 0 no buffer
     Received 686760 broadcasts (642425 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
               0 watchdog, 642425 multicast, 12693 pause input
     0 input packets with dribble condition detected
     776541265 packets output, 54498261964 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/44 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is b0aa.77af.13ac (bia b0aa.77af.13ac)
  Description: Printer VLAN
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
     2048520 packets input, 184752782 bytes, 0 no buffer
     Received 539122 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     314793882 packets output, 22885591888 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/45 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is b0aa.77af.13ad (bia b0aa.77af.13ad)
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
     601224579 packets input, 832789462064 bytes, 0 no buffer
     Received 600331 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
               434296647 packets output, 33963309421 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/46 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is b0aa.77af.13ae (bia b0aa.77af.13ae)
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
     3566042629 packets input, 3915150234296 bytes, 0 no buffer
     Received 3556711061 broadcasts (3556110328 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 3556110328 multicast, 0 pause input
     0 input packets with dribble condition detected
     132461949 packets output, 14644592359 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/47 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is b0aa.77af.13af (bia b0aa.77af.13af)
  Description: Printer VLAN
  MTU 1500 bytes, BW 10000 Kbit/sec, DLY 1000 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Half-duplex, 10Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 1000 bits/sec, 1 packets/sec
     7650584 packets input, 828998677 bytes, 0 no buffer
     Received 66190 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     64137130 packets output, 5933568196 bytes, 0 underruns
     3482 output errors, 635 collisions, 1 interface resets
               0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/48 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is b0aa.77af.13b0 (bia b0aa.77af.13b0)
  Description: Printer VLAN
  MTU 1500 bytes, BW 10000 Kbit/sec, DLY 1000 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Half-duplex, 10Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     7809482 packets input, 865409370 bytes, 0 no buffer
     Received 66240 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     64141921 packets output, 5931622481 bytes, 0 underruns
     3527 output errors, 791 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/1/1 is down, line protocol is down (notconnect) 
  Hardware is Ten Gigabit Ethernet, address is b0aa.77af.13b1 (bia b0aa.77af.13b1)
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not set
  Auto-duplex, Auto-speed, link type is auto, media type is unknown
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
TenGigabitEthernet1/1/2 is down, line protocol is down (notconnect) 
  Hardware is Ten Gigabit Ethernet, address is b0aa.77af.13b2 (bia b0aa.77af.13b2)
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not set
  Auto-duplex, Auto-speed, link type is auto, media type is unknown
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
TenGigabitEthernet1/1/3 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet, address is b0aa.77af.13b3 (bia b0aa.77af.13b3)
  Description: key:t1/1/3:r2-3701SJHC-bo22:t1/10
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not set
  Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-SR
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 13210000 bits/sec, 1448 packets/sec
  5 minute output rate 1000 bits/sec, 2 packets/sec
     22594849519 packets input, 25243288998337 bytes, 0 no buffer
     Received 1147073558 broadcasts (387378530 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 387378530 multicast, 0 pause input
     0 input packets with dribble condition detected
     115681610 packets output, 11425633350 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
          TenGigabitEthernet1/1/4 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet, address is b0aa.77af.13b4 (bia b0aa.77af.13b4)
  Description: key:t1/1/4:r1-3701SJHC-bo22:t1/10
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
  5 minute input rate 399000 bits/sec, 169 packets/sec
  5 minute output rate 244000 bits/sec, 159 packets/sec
     11468133823 packets input, 7920695992964 bytes, 0 no buffer
     Received 1301947123 broadcasts (527286580 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 527286580 multicast, 0 pause input
     0 input packets with dribble condition detected
     12573341286 packets output, 7145889216417 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out""",
 'show inventory':"""NAME: "c36xx Stack", DESCR: "c36xx Stack"
PID: WS-C3650-48PQ     , VID: V01  , SN: FDO1911E4J1

NAME: "Switch 1", DESCR: "WS-C3650-48PQ-S"
PID: WS-C3650-48PQ-S   , VID: V01  , SN: FDO1911E4J1

NAME: "Switch 1 - Power Supply A", DESCR: "Switch 1 - Power Supply A"
PID: PWR-C2-1025WAC    , VID: V01  , SN: LIT18280V8S

NAME: "Switch 1 - Power Supply B", DESCR: "Switch 1 - Power Supply B"
PID: PWR-C2-1025WAC    , VID: V02  , SN: LIT19521485

NAME: "TenGigabitEthernet1/1/3", DESCR: "SFP-10GBase-SR"
PID: SFP-10G-SR         , VID: V02  , SN: USXSR81824     

NAME: "TenGigabitEthernet1/1/4", DESCR: "SFP-10GBase-LR"
PID: SFP-10G-LR         , VID: V02  , SN: USXLR79721     

""",
 'show interface counters':"""Port            InOctets    InUcastPkts    InMcastPkts    InBcastPkts 
Gi1/0/1                0              0              0              0 
Gi1/0/2       3495504496       51808500             16          33076 
Gi1/0/3                0              0              0              0 
Gi1/0/4     357686234145      260942695          94302          76528 
Gi1/0/5      11281557281       89429140        3588426         189811 
Gi1/0/6         85146325         395690         672418          23861 
Gi1/0/7     162210483007      755483146        4204774         178773 
Gi1/0/8     175951143716      380523937        2752795         120391 
Gi1/0/9     329063218079     1313223126        5166861         161267 
Gi1/0/10    233786284965      807201029        5158248         243920 
Gi1/0/11    168694284607      695154088        5012024         222481 
Gi1/0/12    126473450829      335973069        4136275         435563 
Gi1/0/13      3422141184        7994752        1316485             29 
Gi1/0/14     75121076157      251698376        2608723          84600 
Gi1/0/15    158603724549      790527028        6232973         230316 
Gi1/0/16       342683116        2981739              0         784891 
Gi1/0/17      3677806287       45937372              0          10526 
Gi1/0/18      7981166057        9926034         700209          51627 
Gi1/0/19      2897549916       21870033        1063561         186033 
Gi1/0/20    165652586329      653268624        3020512         130395 
Gi1/0/21    123623245265      280153437         615304          22165 
Gi1/0/22      1114034207       13252467         588272          14646 
Gi1/0/23      1830577456       23617796              0          59065 
Gi1/0/24     12336434298      158057064              0         246211 
Gi1/0/25      6742759918       97100124             57          33040 
Gi1/0/26     55951561571      218546460        2206043          31319 
Gi1/0/27      3581799584       45831761         588285          18660 
Gi1/0/28           26730              0              0             45 
Gi1/0/29      2406824871       30938882              0          61420 
Gi1/0/30               0              0              0              0 
Gi1/0/31               0              0              0              0 
Gi1/0/32            1188              0              0              2 
Gi1/0/33               0              0              0              0 
Gi1/0/34      4233698237       52900683         588291          15495 
Gi1/0/35            2970              0              0              5 
Gi1/0/36      1525080290       18819637         588268          15063 
Gi1/0/37       182492041        1329722         624784          35959 
Gi1/0/38    187811797735      946053760        4710385         144637 
Gi1/0/39             594              0              0              1 
Gi1/0/40           19602              0              0             33 
Gi1/0/41        33749681         294809          61389           3476 
Gi1/0/42      3311502134       20903585        2110778        1675104 
Gi1/0/43       507516881        4418544         642426          44335 
Gi1/0/44       184752782        1509398              0         539122 
Gi1/0/45    832789462064      600624248              0         600331 
Gi1/0/46   3915150234296        9331568     3556110328         600733 
Gi1/0/47       828998677        7584394              0          66190 
Gi1/0/48       865409370        7743242              0          66240 
Te1/1/1                0              0              0              0 
Te1/1/2                0              0              0              0 
Te1/1/3   25243288998337    21447775961      387378530      759695028 
Te1/1/4    7920695992964    10166186700      527286580      774660543 

Port           OutOctets   OutUcastPkts   OutMcastPkts   OutBcastPkts 
Gi1/0/1                0              0              0              0 
Gi1/0/2      35435562658       52943363      104323641        2909078 
Gi1/0/3                0              0              0              0 
          
Port           OutOctets   OutUcastPkts   OutMcastPkts   OutBcastPkts 
Gi1/0/4      24341768773      108692945       75160062       42687803 
Gi1/0/5      94004827510       89953786      239179700       86718960 
Gi1/0/6      54059024379       27071837       77981154      667263993 
Gi1/0/7     714619986793      916069690      238394081       86717653 
Gi1/0/8     267071647370      386592112      239937467       86788004 
Gi1/0/9    1388584145302     1543680528      238618470       86748121 
Gi1/0/10    814213749884      916220997      238787969       86665425 
Gi1/0/11    661920878519      786476486      238874604       86686884 
Gi1/0/12    259961058444      353355036      235024060       86471244 
Gi1/0/13     30792590562       16954695      154677494       86909243 
Gi1/0/14    212986319414      282196057      142288101       54146551 
Gi1/0/15    915917964203     1195568807      245994629       85931234 
Gi1/0/16     32934175030       11983913       46029741      400347387 
Gi1/0/17      9623164865       47407712       69166988        1903420 
Gi1/0/18     53265167942       18330314      239940929       86855060 
Gi1/0/19     39161810903       33884170      112122807       64430731 
Gi1/0/20    798036658448      835918046      181924438       66346233 
Gi1/0/21     65870368124      199986623       34519910       16448758 
Gi1/0/22      9184297332       24103673       47003333        1247439 
Gi1/0/23      6390673878       22157712       19969042       16378795 
Gi1/0/24     35181683439      143857925      127703025       72423930 
Gi1/0/25     74616464382       95269456      103851761        2894447 
Gi1/0/26    287940418335      325336518       59970854       20101847 
Gi1/0/27     38054976762       59175036       46810423        1261171 
Gi1/0/28           95745             28            449             53 
Gi1/0/29      6940633849       28464257       19948651       16304078 
Gi1/0/30               0              0              0              0 
Gi1/0/31               0              0              0              0 
Gi1/0/32            7596              2             32             12 
Gi1/0/33               0              0              0              0 
Gi1/0/34     45705277948       68259660       46795806        1244329 
Gi1/0/35           11436              3             49              5 
Gi1/0/36     14742353049       30129499       46800896        1245000 
Gi1/0/37     43742415426       21947117       63029667      537916569 
Gi1/0/38   1595089404324     1399751101      193358796       71004672 
Gi1/0/39            5390              1             19             12 
Gi1/0/40           82846             18            327            139 
Gi1/0/41      4060631696        1087975        5935581       51798973 
Gi1/0/42     76041249949       61002736       77878846      665622589 
Gi1/0/43     54498267235       31640348       77956453      666944533 
Gi1/0/44     22885591888       18502029       31930325      264361528 
Gi1/0/45     33963309421      312595263       78583477       43117907 
Gi1/0/46     14644592359       10767108       78578955       43115886 
Gi1/0/47      5933568196       11186237       52153456         797437 
Gi1/0/48      5931622481       11191097       52153437         797387 
Te1/1/1                0              0              0              0 
Te1/1/2                0              0              0              0 
Te1/1/3      11425633350         194295       93065192       22422123 
Te1/1/4    7145889216417     8932867489     3633017192        7456605 """,
 'show cdp nei detail':"""-------------------------
Device ID: r1-3701sj-b022.net.utah.edu
Entry address(es): 
  IP address: 10.104.197.2
Platform: Cisco C6816-X-LE,  Capabilities: Router Switch IGMP 
Interface: TenGigabitEthernet1/1/4,  Port ID (outgoing port): TenGigabitEthernet1/10
Holdtime : 179 sec

Version :
Cisco IOS Software, c6848x Software (c6848x-ADVENTERPRISEK9-M), Version 15.5(1)SY1, RELEASE SOFTWARE (fc6)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2018 by Cisco Systems, Inc.
Compiled Sun 04-Mar-18 06:24 by prod_rel_team

advertisement version: 2
VTP Management Domain: 'vtp-daybreak'
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 10.104.197.2

-------------------------
Device ID: r2-3701sj-b022.net.utah.edu
Entry address(es): 
  IP address: 10.104.197.3
Platform: Cisco C6816-X-LE,  Capabilities: Router Switch IGMP 
Interface: TenGigabitEthernet1/1/3,  Port ID (outgoing port): TenGigabitEthernet1/10
Holdtime : 151 sec

Version :
Cisco IOS Software, c6848x Software (c6848x-ADVENTERPRISEK9-M), Version 15.5(1)SY1, RELEASE SOFTWARE (fc6)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2018 by Cisco Systems, Inc.
Compiled Sun 04-Mar-18 06:24 by prod_rel_team

advertisement version: 2
VTP Management Domain: 'vtp-daybreak'
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 10.104.197.3


Total cdp entries displayed : 2""",
 'show module all':"""^
% Invalid input detected at '^' marker.
""",
 'show module':"""Switch  Ports    Model                Serial No.   MAC address     Hw Ver.       Sw Ver. 
------  -----   ---------             -----------  --------------  -------       --------
 1       52     WS-C3650-48PQ-S       FDO1911E4J1  b0aa.77af.1380  V01           03.06.06E   """,
 'show run | section snmp':"""snmp-server group VoiceRO v3 priv read VoicePhones access 73
snmp-server group VoiceRO v3 auth context vlan- match prefix 
snmp-server group CliNOCGrv3RO v3 priv read CliNOCViewRO access 70
snmp-server group CliNOCGrv3RO v3 auth context vlan- match prefix 
snmp-server group CliNOCGrv3RW v3 priv write CliNOCViewRW access 71
snmp-server view VoicePhones internet included
snmp-server view CliNOCViewRO internet included
snmp-server view CliNOCViewRW internet included
snmp-server location Bldg. 3701 Room 1W
snmp-server contact BC-506589 Y-Y-061769
snmp ifmib ifindex persist""",
 'show run | in snmp':"""snmp-server group VoiceRO v3 priv read VoicePhones access 73
snmp-server group VoiceRO v3 auth context vlan- match prefix 
snmp-server group CliNOCGrv3RO v3 priv read CliNOCViewRO access 70
snmp-server group CliNOCGrv3RO v3 auth context vlan- match prefix 
snmp-server group CliNOCGrv3RW v3 priv write CliNOCViewRW access 71
snmp-server view VoicePhones internet included
snmp-server view CliNOCViewRO internet included
snmp-server view CliNOCViewRW internet included
snmp-server location Bldg. 3701 Room 1W
snmp-server contact BC-506589 Y-Y-061769
snmp ifmib ifindex persist""",
 'show snmp user':"""User name: prognosis
Engine ID: 800000090300B0AA77AF1380
storage-type: nonvolatile	 active
Authentication Protocol: MD5
Privacy Protocol: DES
Group-name: VoiceRO

User name: CliNONUserv3RO
Engine ID: 800000090300B0AA77AF1380
storage-type: nonvolatile	 active
Authentication Protocol: MD5
Privacy Protocol: DES
Group-name: CliNOCGrv3RO

User name: CliNONUserv3Rw
Engine ID: 800000090300B0AA77AF1380
storage-type: nonvolatile	 active
Authentication Protocol: MD5
Privacy Protocol: DES
Group-name: CliNOCGrv3RW
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
    120 permit 10.71.24.14 (7065544 matches)
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
    110 permit 10.71.24.13
    100 permit 10.71.24.12
    130 permit 10.71.24.15
    120 permit 10.71.24.14 (6162 matches)
    90 permit 10.71.24.11
    30 permit 155.100.123.72
    240 permit 10.71.25.164
    60 permit 155.98.164.192, wildcard bits 0.0.0.31
    70 permit 155.99.254.128, wildcard bits 0.0.0.127
    80 permit 155.98.253.0, wildcard bits 0.0.0.255
    250 deny   any log
Standard IP access list 73
    10 permit 155.97.178.19 (8204127 matches)
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
    90 permit tcp 155.99.254.128 0.0.0.127 any eq 22 (28 matches)
    100 permit tcp 155.98.164.192 0.0.0.31 any eq 22 (106 matches)
    110 permit tcp host 10.71.24.11 any eq 22
    120 permit tcp host 10.71.24.12 any eq 22
    130 permit tcp host 10.71.24.13 any eq 22
    140 permit tcp host 10.71.24.14 any eq 22 (92 matches)
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
hw-switch switch 1 logging onboard message level 3
logging facility local6
logging source-interface Vlan525
logging host 155.98.204.52
logging host 155.98.253.244
logging host 10.71.24.11""",
 'show run | in logging':"""logging buffered notifications
logging console critical
hw-switch switch 1 logging onboard message level 3
logging facility local6
logging source-interface Vlan525
logging host 155.98.204.52
logging host 155.98.253.244
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
   1    bcf1.f260.e24d    DYNAMIC     Te1/1/4
   1    bcf1.f260.e4bc    DYNAMIC     Te1/1/3
 525    0000.0c07.ac09    DYNAMIC     Te1/1/4
 525    00ee.ab08.6e5c    DYNAMIC     Te1/1/4
 525    70ea.1a04.6e9c    DYNAMIC     Te1/1/4
 525    70ea.1a04.795c    DYNAMIC     Te1/1/4
 525    b0aa.77af.13f8    STATIC      Vl525 
 525    bcf1.f260.e24d    DYNAMIC     Te1/1/4
 525    bcf1.f260.e25d    DYNAMIC     Te1/1/4
 525    bcf1.f260.e4cc    DYNAMIC     Te1/1/4
1610    0000.0c07.ac17    DYNAMIC     Te1/1/4
1610    0018.8528.bf14    DYNAMIC     Te1/1/4
1610    b0aa.77af.13e7    STATIC      Vl1610 
1610    bcf1.f260.e24d    DYNAMIC     Te1/1/4
1610    bcf1.f260.e25d    DYNAMIC     Te1/1/4
1610    bcf1.f260.e4cc    DYNAMIC     Te1/1/4
 527    0000.0c07.ac0b    DYNAMIC     Te1/1/4
 527    0001.e692.2407    DYNAMIC     Te1/1/4
 527    0007.4d41.af70    DYNAMIC     Gi1/0/43
 527    0007.4d47.25ec    DYNAMIC     Te1/1/4
 527    0007.4d54.76ea    DYNAMIC     Te1/1/4
 527    0007.4d54.8467    DYNAMIC     Te1/1/4
 527    0007.4d62.049a    DYNAMIC     Te1/1/4
 527    0007.4d7f.88c5    DYNAMIC     Te1/1/4
 527    0007.4d85.a378    DYNAMIC     Te1/1/4
 527    0007.4d86.1416    DYNAMIC     Te1/1/4
 527    0007.4d8a.7a61    DYNAMIC     Te1/1/4
 527    0007.4d8a.7a66    DYNAMIC     Te1/1/4
 527    0007.4d8a.7b5d    DYNAMIC     Te1/1/4
 527    0007.4d94.5692    DYNAMIC     Te1/1/4
 527    0007.4d94.864e    DYNAMIC     Te1/1/4
 527    0007.4d96.2ccf    DYNAMIC     Te1/1/4
 527    0007.4d9e.0e5e    DYNAMIC     Gi1/0/6
           527    0007.4da5.3328    DYNAMIC     Gi1/0/41
 527    0007.4da6.4d09    DYNAMIC     Te1/1/4
 527    000c.c601.b112    DYNAMIC     Te1/1/4
 527    001b.78e5.bfbd    DYNAMIC     Te1/1/4
 527    0021.5a80.909e    DYNAMIC     Te1/1/4
 527    0023.7d88.1f88    DYNAMIC     Te1/1/4
 527    0023.7d88.4b86    DYNAMIC     Te1/1/4
 527    0023.7d88.9189    DYNAMIC     Te1/1/4
 527    0023.7d88.ada5    DYNAMIC     Te1/1/4
 527    0023.7d88.db91    DYNAMIC     Te1/1/4
 527    0023.7d88.fde1    DYNAMIC     Te1/1/4
 527    0023.7d88.fdfd    DYNAMIC     Te1/1/4
 527    0023.7d89.1177    DYNAMIC     Te1/1/4
 527    0023.7d89.61c9    DYNAMIC     Te1/1/4
 527    0023.7d89.7129    DYNAMIC     Te1/1/4
 527    0023.7d89.8081    DYNAMIC     Te1/1/4
 527    0023.7d89.8473    DYNAMIC     Te1/1/4
 527    0023.7d89.9179    DYNAMIC     Te1/1/4
 527    0023.7d89.b14b    DYNAMIC     Te1/1/4
 527    0023.7d89.b14c    DYNAMIC     Te1/1/4
 527    0025.b3f6.1e62    DYNAMIC     Te1/1/4
 527    00ee.ab08.6e6c    DYNAMIC     Te1/1/4
 527    082e.5f6a.b2e9    DYNAMIC     Te1/1/4
 527    101f.7444.84c0    DYNAMIC     Te1/1/4
 527    101f.7447.7a09    DYNAMIC     Te1/1/4
 527    101f.7448.1695    DYNAMIC     Te1/1/4
 527    101f.7448.1696    DYNAMIC     Te1/1/4
 527    101f.7448.20fc    DYNAMIC     Te1/1/4
 527    101f.7448.3e3c    DYNAMIC     Te1/1/4
 527    101f.7448.4e28    DYNAMIC     Gi1/0/42
 527    101f.7448.5141    DYNAMIC     Te1/1/4
 527    101f.7448.5142    DYNAMIC     Te1/1/4
 527    101f.7448.5183    DYNAMIC     Te1/1/4
 527    101f.7448.5185    DYNAMIC     Te1/1/4
 527    101f.7448.5188    DYNAMIC     Te1/1/4
 527    101f.7448.5189    DYNAMIC     Te1/1/4
 527    101f.7448.6e0e    DYNAMIC     Te1/1/4
 527    101f.7448.7515    DYNAMIC     Te1/1/4
 527    101f.7448.c502    DYNAMIC     Te1/1/4
 527    101f.7449.eeb2    DYNAMIC     Te1/1/4
 527    101f.7449.eeb4    DYNAMIC     Te1/1/4
 527    1cc1.de13.c977    DYNAMIC     Te1/1/4
 527    2426.42a6.a291    DYNAMIC     Te1/1/4
 527    2426.42a6.a2ae    DYNAMIC     Te1/1/4
 527    2426.42a6.a2ca    DYNAMIC     Te1/1/4
 527    2c27.d70f.31b8    DYNAMIC     Te1/1/4
 527    2c27.d712.0388    DYNAMIC     Te1/1/4
 527    2c27.d712.03f0    DYNAMIC     Te1/1/4
 527    2c27.d712.962a    DYNAMIC     Te1/1/4
 527    2c27.d712.c254    DYNAMIC     Te1/1/4
 527    2c27.d712.d2a5    DYNAMIC     Te1/1/4
 527    2c41.3881.19bc    DYNAMIC     Te1/1/4
 527    2c41.3881.3956    DYNAMIC     Te1/1/4
 527    2c41.3881.5a73    DYNAMIC     Gi1/0/16
 527    2c41.3882.2406    DYNAMIC     Te1/1/4
 527    2c41.3882.2408    DYNAMIC     Te1/1/4
 527    2c41.3882.240f    DYNAMIC     Te1/1/4
 527    2c41.3882.2410    DYNAMIC     Te1/1/4
 527    2c41.3882.2415    DYNAMIC     Te1/1/4
           527    2c41.3882.2416    DYNAMIC     Te1/1/4
 527    2c41.3882.2417    DYNAMIC     Te1/1/4
 527    2c41.3882.2427    DYNAMIC     Te1/1/4
 527    2c41.3882.247b    DYNAMIC     Te1/1/4
 527    2c41.3882.2484    DYNAMIC     Te1/1/4
 527    2c41.3882.2485    DYNAMIC     Te1/1/4
 527    2c41.3882.2487    DYNAMIC     Te1/1/4
 527    2c41.3882.2488    DYNAMIC     Te1/1/4
 527    2c41.3882.2489    DYNAMIC     Te1/1/4
 527    2c41.3882.248c    DYNAMIC     Te1/1/4
 527    2c41.3882.248d    DYNAMIC     Te1/1/4
 527    2c41.3882.248e    DYNAMIC     Te1/1/4
 527    2c41.3882.2490    DYNAMIC     Te1/1/4
 527    2c41.3882.2493    DYNAMIC     Te1/1/4
 527    2c41.3882.2495    DYNAMIC     Te1/1/4
 527    2c41.3882.2497    DYNAMIC     Te1/1/4
 527    2c41.3882.24b8    DYNAMIC     Te1/1/4
 527    2c41.3882.8180    DYNAMIC     Te1/1/4
 527    2c41.3882.81a4    DYNAMIC     Te1/1/4
 527    2c41.3882.81a5    DYNAMIC     Te1/1/4
 527    2c41.3882.81a7    DYNAMIC     Te1/1/4
 527    2c41.3882.81aa    DYNAMIC     Te1/1/4
 527    2c41.3882.81ab    DYNAMIC     Te1/1/4
 527    2c41.3882.81ad    DYNAMIC     Te1/1/4
 527    2c41.3882.81dd    DYNAMIC     Te1/1/4
 527    2c41.3882.81f6    DYNAMIC     Te1/1/4
 527    2c41.3882.81f8    DYNAMIC     Te1/1/4
 527    2c41.3882.81fb    DYNAMIC     Te1/1/4
 527    2c41.3882.9100    DYNAMIC     Te1/1/4
 527    2c41.3882.b1b6    DYNAMIC     Te1/1/4
 527    2c41.3882.b1c5    DYNAMIC     Te1/1/4
 527    2c41.3882.b1cd    DYNAMIC     Te1/1/4
 527    2c76.8a3e.1800    DYNAMIC     Te1/1/4
 527    3024.a9c7.cca1    DYNAMIC     Te1/1/4
 527    30e1.71bb.5098    DYNAMIC     Te1/1/4
 527    3822.e2d9.4c86    DYNAMIC     Te1/1/4
 527    3863.bb04.9142    DYNAMIC     Te1/1/4
 527    3cd9.2b0f.a00e    DYNAMIC     Te1/1/4
 527    3cd9.2b0f.e47f    DYNAMIC     Te1/1/4
 527    3cd9.2b9e.0c1a    DYNAMIC     Te1/1/4
 527    3cd9.2b9e.0c1d    DYNAMIC     Te1/1/4
 527    3cd9.2b9e.0c55    DYNAMIC     Te1/1/4
 527    3cd9.2b9e.1c2d    DYNAMIC     Te1/1/4
 527    3cd9.2ba0.c516    DYNAMIC     Te1/1/4
 527    3cd9.2ba1.3669    DYNAMIC     Te1/1/4
 527    3cd9.2ba2.239b    DYNAMIC     Te1/1/4
 527    3cd9.2ba2.4340    DYNAMIC     Te1/1/4
 527    40b0.3420.de3e    DYNAMIC     Te1/1/4
 527    40b0.3423.4efb    DYNAMIC     Te1/1/4
 527    40b0.3423.9e2a    DYNAMIC     Te1/1/4
 527    441e.a12f.aa9b    DYNAMIC     Te1/1/4
 527    441e.a133.e533    DYNAMIC     Te1/1/4
 527    441e.a133.e549    DYNAMIC     Te1/1/4
 527    5065.f356.82a8    DYNAMIC     Te1/1/4
 527    5cb9.010e.b89b    DYNAMIC     Te1/1/4
 527    5cb9.0111.afed    DYNAMIC     Te1/1/4
 527    68ab.8a82.97bc    DYNAMIC     Te1/1/4
 527    68ab.8a82.9830    DYNAMIC     Te1/1/4
 527    68b5.99ab.a9a9    DYNAMIC     Te1/1/4
           527    6c3b.e509.b205    DYNAMIC     Te1/1/4
 527    705a.0fa4.e611    DYNAMIC     Te1/1/4
 527    70ea.1a04.6ead    DYNAMIC     Te1/1/4
 527    70ea.1a04.796c    DYNAMIC     Te1/1/4
 527    781c.5aa1.c8c4    DYNAMIC     Te1/1/4
 527    8851.fbea.cc82    DYNAMIC     Te1/1/4
 527    9457.a5ce.291d    DYNAMIC     Te1/1/4
 527    9c7b.ef85.35cb    DYNAMIC     Te1/1/4
 527    9c8e.9985.0502    DYNAMIC     Te1/1/4
 527    9c8e.9985.052c    DYNAMIC     Te1/1/4
 527    9c8e.9985.054f    DYNAMIC     Te1/1/4
 527    9c8e.9985.05aa    DYNAMIC     Te1/1/4
 527    9c8e.9985.05ff    DYNAMIC     Te1/1/4
 527    9c8e.9985.0b24    DYNAMIC     Te1/1/4
 527    9c8e.9985.0b94    DYNAMIC     Te1/1/4
 527    9c8e.9985.1502    DYNAMIC     Te1/1/4
 527    9c8e.9985.1503    DYNAMIC     Te1/1/4
 527    9c8e.9985.1504    DYNAMIC     Te1/1/4
 527    9c8e.9985.1505    DYNAMIC     Te1/1/4
 527    9c8e.9985.1516    DYNAMIC     Te1/1/4
 527    9c8e.9985.151b    DYNAMIC     Te1/1/4
 527    9c8e.9985.151c    DYNAMIC     Te1/1/4
 527    9c8e.9985.1544    DYNAMIC     Te1/1/4
 527    9c8e.9985.1545    DYNAMIC     Te1/1/4
 527    9c8e.9985.15c2    DYNAMIC     Te1/1/4
 527    9c8e.9985.15da    DYNAMIC     Te1/1/4
 527    9c8e.9985.15f8    DYNAMIC     Te1/1/4
 527    9c8e.9985.15f9    DYNAMIC     Te1/1/4
 527    9c8e.9985.2554    DYNAMIC     Te1/1/4
 527    9c8e.9985.255e    DYNAMIC     Te1/1/4
 527    9c8e.9985.2560    DYNAMIC     Te1/1/4
 527    9c8e.9985.2565    DYNAMIC     Te1/1/4
 527    9c8e.9985.2567    DYNAMIC     Te1/1/4
 527    9c8e.9985.256b    DYNAMIC     Te1/1/4
 527    9c8e.9985.257e    DYNAMIC     Te1/1/4
 527    9c8e.9985.25fb    DYNAMIC     Te1/1/4
 527    9c8e.9985.25fc    DYNAMIC     Te1/1/4
 527    9c8e.9985.2bd4    DYNAMIC     Te1/1/4
 527    9c8e.9985.350b    DYNAMIC     Te1/1/4
 527    9c8e.9985.3513    DYNAMIC     Te1/1/4
 527    9c8e.9985.351f    DYNAMIC     Te1/1/4
 527    9c8e.9985.3520    DYNAMIC     Te1/1/4
 527    9c8e.9985.3530    DYNAMIC     Te1/1/4
 527    9c8e.9985.3548    DYNAMIC     Te1/1/4
 527    9c8e.9985.354c    DYNAMIC     Te1/1/4
 527    9c8e.9985.354e    DYNAMIC     Te1/1/4
 527    9c8e.9985.3553    DYNAMIC     Te1/1/4
 527    9c8e.9985.3554    DYNAMIC     Te1/1/4
 527    9c8e.9985.35c7    DYNAMIC     Te1/1/4
 527    9c8e.9985.35f0    DYNAMIC     Te1/1/4
 527    9c8e.9985.4575    DYNAMIC     Te1/1/4
 527    9c8e.9985.4595    DYNAMIC     Te1/1/4
 527    9c8e.9985.45ca    DYNAMIC     Te1/1/4
 527    9c8e.9985.5504    DYNAMIC     Te1/1/4
 527    9c8e.9985.554b    DYNAMIC     Te1/1/4
 527    9c8e.9985.8ee9    DYNAMIC     Te1/1/4
 527    9c8e.9985.9e8f    DYNAMIC     Te1/1/4
 527    9c8e.9985.9edd    DYNAMIC     Te1/1/4
 527    9c8e.9985.9eea    DYNAMIC     Te1/1/4
           527    9c8e.9985.ae36    DYNAMIC     Te1/1/4
 527    9c8e.9985.ae37    DYNAMIC     Te1/1/4
 527    9c8e.9985.ae38    DYNAMIC     Te1/1/4
 527    9c8e.9985.ae7f    DYNAMIC     Te1/1/4
 527    9c8e.9985.aea1    DYNAMIC     Te1/1/4
 527    9c8e.9985.aea8    DYNAMIC     Te1/1/4
 527    9c8e.9985.aea9    DYNAMIC     Te1/1/4
 527    9c8e.9985.aebb    DYNAMIC     Te1/1/4
 527    9c8e.9985.bab6    DYNAMIC     Te1/1/4
 527    9c8e.9985.bac1    DYNAMIC     Te1/1/4
 527    9c8e.9985.da87    DYNAMIC     Te1/1/4
 527    9c8e.9985.dab7    DYNAMIC     Te1/1/4
 527    9c8e.9985.daba    DYNAMIC     Te1/1/4
 527    9c8e.9985.dacb    DYNAMIC     Te1/1/4
 527    9c8e.9985.dadd    DYNAMIC     Te1/1/4
 527    9c8e.9985.e473    DYNAMIC     Te1/1/4
 527    9c8e.9985.e47c    DYNAMIC     Te1/1/4
 527    9c8e.9985.e47e    DYNAMIC     Te1/1/4
 527    9c8e.9985.e480    DYNAMIC     Te1/1/4
 527    9c8e.9985.e482    DYNAMIC     Te1/1/4
 527    9c8e.9985.e48b    DYNAMIC     Te1/1/4
 527    9c8e.9985.ea04    DYNAMIC     Te1/1/4
 527    9c8e.9985.ea10    DYNAMIC     Te1/1/4
 527    9c8e.9985.f497    DYNAMIC     Te1/1/4
 527    9c8e.9985.f4b2    DYNAMIC     Te1/1/4
 527    9c8e.9985.f4bd    DYNAMIC     Te1/1/4
 527    9c8e.9985.f4bf    DYNAMIC     Te1/1/4
 527    9c8e.9985.f4c0    DYNAMIC     Te1/1/4
 527    9c8e.9985.f4c8    DYNAMIC     Te1/1/4
 527    9c8e.9985.f4f2    DYNAMIC     Te1/1/4
 527    9c8e.9985.fe7a    DYNAMIC     Te1/1/4
 527    9c8e.9986.033f    DYNAMIC     Te1/1/4
 527    9c8e.9986.2279    DYNAMIC     Te1/1/4
 527    9c8e.9986.327d    DYNAMIC     Te1/1/4
 527    9c8e.9986.3284    DYNAMIC     Te1/1/4
 527    9c8e.9986.3286    DYNAMIC     Te1/1/4
 527    9c8e.9986.3289    DYNAMIC     Te1/1/4
 527    9c8e.9986.32f7    DYNAMIC     Te1/1/4
 527    9c8e.9986.32f9    DYNAMIC     Te1/1/4
 527    9c8e.9986.4238    DYNAMIC     Te1/1/4
 527    9c8e.9986.4262    DYNAMIC     Te1/1/4
 527    9c8e.9986.7250    DYNAMIC     Te1/1/4
 527    9c8e.9986.8245    DYNAMIC     Te1/1/4
 527    9c8e.9986.9268    DYNAMIC     Te1/1/4
 527    9c8e.9986.d629    DYNAMIC     Te1/1/4
 527    9c8e.9986.d694    DYNAMIC     Te1/1/4
 527    9c8e.9986.d695    DYNAMIC     Te1/1/4
 527    9c8e.9986.d697    DYNAMIC     Te1/1/4
 527    9c8e.9986.d69f    DYNAMIC     Te1/1/4
 527    9c8e.9986.d6ae    DYNAMIC     Te1/1/4
 527    9c8e.9986.d6c3    DYNAMIC     Te1/1/4
 527    9c8e.9986.e613    DYNAMIC     Te1/1/4
 527    9c8e.9986.e6a4    DYNAMIC     Te1/1/4
 527    9c8e.9986.e6af    DYNAMIC     Te1/1/4
 527    9c8e.9986.e6ec    DYNAMIC     Te1/1/4
 527    9c8e.9986.e6f4    DYNAMIC     Te1/1/4
 527    9c8e.9986.f60b    DYNAMIC     Te1/1/4
 527    9c8e.9986.f61a    DYNAMIC     Te1/1/4
 527    9c8e.9988.275a    DYNAMIC     Te1/1/4
           527    9c8e.9989.2130    DYNAMIC     Te1/1/4
 527    9c8e.9989.2132    DYNAMIC     Te1/1/4
 527    9cb6.541b.0ca3    DYNAMIC     Te1/1/4
 527    a0d3.c181.9078    DYNAMIC     Te1/1/4
 527    ace2.d3d8.a384    DYNAMIC     Te1/1/4
 527    bcf1.f260.e24d    DYNAMIC     Te1/1/4
 527    bcf1.f260.e25d    DYNAMIC     Te1/1/4
 527    bcf1.f260.e4cc    DYNAMIC     Te1/1/4
 527    d485.6440.dfc9    DYNAMIC     Te1/1/4
 527    dc4a.3eb1.fc03    DYNAMIC     Te1/1/4
 527    f092.1c66.362b    DYNAMIC     Te1/1/4
 527    f430.b929.3e28    DYNAMIC     Te1/1/4
 527    f430.b96f.a5d9    DYNAMIC     Te1/1/4
 527    f430.b96f.a5db    DYNAMIC     Te1/1/4
 527    f430.b96f.d5c3    DYNAMIC     Te1/1/4
 527    f4ce.463b.6818    DYNAMIC     Te1/1/4
 527    f4ce.463c.6c82    DYNAMIC     Te1/1/4
 527    f4ce.463c.ce72    DYNAMIC     Te1/1/4
 527    f4ce.463c.ce75    DYNAMIC     Te1/1/4
 527    f4ce.4649.cd43    DYNAMIC     Te1/1/4
 527    f4ce.464a.7683    DYNAMIC     Te1/1/4
 527    f4ce.464a.769f    DYNAMIC     Te1/1/4
 527    f8b4.6a0f.4626    DYNAMIC     Te1/1/4
 527    f8b4.6a0f.9b5e    DYNAMIC     Te1/1/4
 527    fc3f.db51.200f    DYNAMIC     Te1/1/4
 523    0000.0c07.ac07    DYNAMIC     Te1/1/4
 523    0001.2990.5d34    DYNAMIC     Gi1/0/5
 523    0008.00d3.1f46    DYNAMIC     Te1/1/4
 523    000c.c601.b084    DYNAMIC     Te1/1/4
 523    000c.c601.b20a    DYNAMIC     Te1/1/4
 523    0013.9537.7663    DYNAMIC     Te1/1/4
 523    0019.998e.858e    DYNAMIC     Te1/1/4
 523    001e.679b.dcf8    DYNAMIC     Te1/1/4
 523    0020.4ad6.62e8    DYNAMIC     Te1/1/4
 523    0020.4ad6.91bc    DYNAMIC     Te1/1/4
 523    0020.4afb.d425    DYNAMIC     Gi1/0/23
 523    0020.4afb.e585    DYNAMIC     Gi1/0/29
 523    0020.4afb.fe7c    DYNAMIC     Te1/1/4
 523    0020.4afb.fe82    DYNAMIC     Te1/1/4
 523    0020.4afb.ffbd    DYNAMIC     Te1/1/4
 523    0020.4afc.5b60    DYNAMIC     Te1/1/4
 523    0024.dd01.41c1    DYNAMIC     Te1/1/4
 523    0040.9db0.c420    DYNAMIC     Gi1/0/5
 523    0090.333f.83bc    DYNAMIC     Te1/1/4
 523    0cc4.7a72.8e8a    DYNAMIC     Te1/1/4
 523    0cc4.7a72.a230    DYNAMIC     Te1/1/4
 523    1062.e515.e7b2    DYNAMIC     Te1/1/4
 523    1062.e515.e84e    DYNAMIC     Gi1/0/12
 523    1062.e519.41f6    DYNAMIC     Te1/1/4
 523    1062.e51b.86d5    DYNAMIC     Te1/1/4
 523    1062.e51b.86d7    DYNAMIC     Te1/1/4
 523    1062.e51b.871c    DYNAMIC     Te1/1/4
 523    1062.e51b.8746    DYNAMIC     Te1/1/4
 523    1062.e51b.87a8    DYNAMIC     Te1/1/4
 523    10e7.c606.1380    DYNAMIC     Te1/1/4
 523    10e7.c608.22fc    DYNAMIC     Te1/1/4
 523    10e7.c612.e050    DYNAMIC     Te1/1/4
 523    10e7.c613.dfd7    DYNAMIC     Gi1/0/9
 523    2c41.3882.0da5    DYNAMIC     Te1/1/4
           523    3c2a.f460.bd82    DYNAMIC     Gi1/0/18
 523    50cd.22b4.2ee1    DYNAMIC     Gi1/0/9
 523    6805.ca28.c34e    DYNAMIC     Te1/1/4
 523    6c2b.59c8.3939    DYNAMIC     Te1/1/4
 523    6c2b.59c9.5cec    DYNAMIC     Te1/1/4
 523    6c2b.59c9.79de    DYNAMIC     Te1/1/4
 523    6c2b.59d2.c44a    DYNAMIC     Te1/1/4
 523    6c2b.59d5.344f    DYNAMIC     Te1/1/4
 523    6c2b.59d5.3838    DYNAMIC     Te1/1/4
 523    6c2b.59f6.60a4    DYNAMIC     Te1/1/4
 523    6c2b.59f8.c7da    DYNAMIC     Te1/1/4
 523    707c.6901.1a3d    DYNAMIC     Gi1/0/13
 523    84a9.3e60.7a81    DYNAMIC     Te1/1/4
 523    901b.0eea.7f75    DYNAMIC     Te1/1/4
 523    9c8e.99ed.9078    DYNAMIC     Te1/1/4
 523    a009.ed07.877a    DYNAMIC     Gi1/0/10
 523    a08c.fdeb.fed5    DYNAMIC     Te1/1/4
 523    a08c.fdf0.6ee7    DYNAMIC     Te1/1/4
 523    a4bb.6d4d.500f    DYNAMIC     Gi1/0/10
 523    a4bb.6d6c.1653    DYNAMIC     Te1/1/4
 523    a4bb.6d6c.2fa9    DYNAMIC     Te1/1/4
 523    a4bb.6d6c.928d    DYNAMIC     Te1/1/4
 523    a4bb.6d77.c601    DYNAMIC     Te1/1/4
 523    ac1f.6b46.c2cf    DYNAMIC     Te1/1/4
 523    ace2.d308.5406    DYNAMIC     Gi1/0/8
 523    bcf1.f260.e24d    DYNAMIC     Te1/1/4
 523    bcf1.f260.e25d    DYNAMIC     Te1/1/4
 523    bcf1.f260.e4cc    DYNAMIC     Te1/1/4
 523    c0a2.6d00.08bb    DYNAMIC     Te1/1/4
 523    c0a2.6d00.0e99    DYNAMIC     Te1/1/4
 523    c81f.ea6c.c1e8    DYNAMIC     Gi1/0/12
 523    c81f.eabf.6317    DYNAMIC     Gi1/0/14
 523    c8d3.ffa1.de4d    DYNAMIC     Te1/1/4
 523    c8d3.ffa4.1dbe    DYNAMIC     Gi1/0/7
 523    c8d9.d294.bcce    DYNAMIC     Te1/1/4
 523    c8d9.d2ba.4d34    DYNAMIC     Te1/1/4
 523    c8d9.d2ba.4d42    DYNAMIC     Te1/1/4
 523    c8d9.d2ba.4d45    DYNAMIC     Gi1/0/21
 523    d478.56b6.6c75    DYNAMIC     Gi1/0/11
 523    d4c9.3cbc.be6c    DYNAMIC     Te1/1/4
 523    d8b1.901a.0e08    DYNAMIC     Te1/1/4
 523    e454.e85c.e965    DYNAMIC     Gi1/0/15
 523    e454.e867.545b    DYNAMIC     Te1/1/4
 523    e454.e879.064e    DYNAMIC     Te1/1/4
 523    e454.e879.09b7    DYNAMIC     Te1/1/4
 523    e454.e87e.d359    DYNAMIC     Te1/1/4
 523    e4b9.7af6.bdb0    DYNAMIC     Te1/1/4
 523    e4b9.7af9.c920    DYNAMIC     Te1/1/4
 523    e840.f20b.2e23    DYNAMIC     Te1/1/4
 523    ec8e.b56e.7983    DYNAMIC     Te1/1/4
 523    ec8e.b56f.f295    DYNAMIC     Gi1/0/26
 523    ec8e.b56f.f300    DYNAMIC     Te1/1/4
 523    ecb1.d752.f116    DYNAMIC     Te1/1/4
 523    ecb1.d75d.a3d7    DYNAMIC     Gi1/0/11
 523    fc3f.db02.948e    DYNAMIC     Te1/1/4
 523    fc3f.db0d.f32e    DYNAMIC     Gi1/0/14
 523    fc3f.db0f.9bbd    DYNAMIC     Te1/1/4
 953    0000.0c07.ac12    DYNAMIC     Te1/1/4
 953    50cd.22b4.2ee1    DYNAMIC     Gi1/0/9
           953    707c.6901.1a3d    DYNAMIC     Gi1/0/13
 953    8483.7180.3ad9    DYNAMIC     Gi1/0/34
 953    a009.ed07.877a    DYNAMIC     Gi1/0/10
 953    bcf1.f260.e24d    DYNAMIC     Te1/1/4
 953    bcf1.f260.e25d    DYNAMIC     Te1/1/4
 953    bcf1.f260.e4cc    DYNAMIC     Te1/1/4
 953    c81f.ea6c.c1e8    DYNAMIC     Gi1/0/12
 953    c81f.eabb.a9fa    DYNAMIC     Gi1/0/36
 953    c81f.eabb.b500    DYNAMIC     Gi1/0/27
 953    c81f.eabf.3e50    DYNAMIC     Gi1/0/22
 953    c81f.eabf.6317    DYNAMIC     Gi1/0/14
 953    d478.56b6.6c75    DYNAMIC     Gi1/0/11
 110    0000.0c07.ac0a    DYNAMIC     Te1/1/4
 110    0024.dd01.4208    DYNAMIC     Gi1/0/17
 110    2cea.7f19.da7d    DYNAMIC     Gi1/0/22
 110    2cea.7f1a.ec5d    DYNAMIC     Gi1/0/27
 110    6c2b.5954.0d22    DYNAMIC     Gi1/0/2
 110    6c2b.5954.109b    DYNAMIC     Te1/1/4
 110    6c2b.5954.13e6    DYNAMIC     Te1/1/4
 110    6c2b.5955.db6c    DYNAMIC     Te1/1/4
 110    6c2b.5955.db74    DYNAMIC     Te1/1/4
 110    6c2b.5956.aa71    DYNAMIC     Te1/1/4
 110    6c2b.5956.b5c5    DYNAMIC     Te1/1/4
 110    6c2b.5956.b5f5    DYNAMIC     Te1/1/4
 110    6c2b.5957.b903    DYNAMIC     Te1/1/4
 110    6c2b.5957.fd7e    DYNAMIC     Te1/1/4
 110    6c2b.5957.fd85    DYNAMIC     Gi1/0/34
 110    6c2b.5957.fdab    DYNAMIC     Gi1/0/25
 110    6c2b.5957.fe09    DYNAMIC     Te1/1/4
 110    6c2b.5958.01e6    DYNAMIC     Te1/1/4
 110    6c2b.5958.02ad    DYNAMIC     Te1/1/4
 110    6c2b.5971.f063    DYNAMIC     Gi1/0/36
 110    70ea.1a04.796c    DYNAMIC     Te1/1/4
 110    8483.7180.3ad9    DYNAMIC     Gi1/0/34
 110    bcf1.f260.e24d    DYNAMIC     Te1/1/4
 110    bcf1.f260.e25d    DYNAMIC     Te1/1/4
 110    bcf1.f260.e4cc    DYNAMIC     Te1/1/4
 110    c81f.eabb.a9fa    DYNAMIC     Gi1/0/36
 110    c81f.eabb.b500    DYNAMIC     Gi1/0/27
 110    c81f.eabf.3e50    DYNAMIC     Gi1/0/22
 532    0000.0c07.ac0e    DYNAMIC     Te1/1/4
 532    0050.f900.f0b3    DYNAMIC     Te1/1/4
 532    0050.f900.f0ed    DYNAMIC     Te1/1/4
 532    0050.f900.f3e9    DYNAMIC     Te1/1/4
 532    0050.f900.f514    DYNAMIC     Te1/1/4
 532    0050.f900.f82d    DYNAMIC     Gi1/0/47
 532    0050.f901.3913    DYNAMIC     Gi1/0/48
 532    0050.f901.680a    DYNAMIC     Te1/1/4
 532    00ee.ab08.6e6c    DYNAMIC     Te1/1/4
 532    70ea.1a04.6ead    DYNAMIC     Te1/1/4
 532    70ea.1a04.796c    DYNAMIC     Te1/1/4
 532    bcf1.f260.e24d    DYNAMIC     Te1/1/4
 532    bcf1.f260.e25d    DYNAMIC     Te1/1/4
 532    bcf1.f260.e4cc    DYNAMIC     Te1/1/4
Total Mac Addresses for this criterion: 462""",
 'show run | section tacacs':"""aaa group server tacacs+ NOC-TAC
 server name TAC-EBC
 server name TAC-SECONDARY
tacacs server TAC-EBC
 address ipv4 172.31.17.180
 key 7 0808084B205D003532091545
tacacs server TAC-SECONDARY
 address ipv4 10.64.32.5
 key 7 032D1F0E2F4B246E6E0B0044""",
 'show run | in tacacs':"""aaa group server tacacs+ NOC-TAC
tacacs server TAC-EBC
tacacs server TAC-SECONDARY""",
 'show power inline':"""Module   Available     Used     Remaining
          (Watts)     (Watts)    (Watts) 
------   ---------   --------   ---------
1          1550.0       44.0      1506.0
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
Gi1/0/9   auto   on         4.0     Ieee PD             1     30.0 
Gi1/0/10  auto   on         4.0     Ieee PD             1     30.0 
Gi1/0/11  auto   on         4.0     Ieee PD             1     30.0 
Gi1/0/12  auto   on         4.0     Ieee PD             1     30.0 
Gi1/0/13  auto   on         4.0     Ieee PD             1     30.0 
Gi1/0/14  auto   on         4.0     Ieee PD             1     30.0 
Gi1/0/15  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/16  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/17  auto   on         4.0     Ieee PD             1     30.0 
Gi1/0/18  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/19  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/20  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/21  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/22  auto   on         4.0     Ieee PD             1     30.0 
Gi1/0/23  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/24  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/25  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/26  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/27  auto   on         4.0     Ieee PD             1     30.0 
Gi1/0/28  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/29  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/30  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/31  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/32  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/33  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/34  auto   on         4.0     Ieee PD             1     30.0 
Gi1/0/35  auto   off        0.0     n/a                 n/a   30.0 
Gi1/0/36  auto   on         4.0     Ieee PD             1     30.0 
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
FAN PS-2 is OK
Switch 1: SYSTEM TEMPERATURE is OK
SW  PID                 Serial#     Status           Sys Pwr  PoE Pwr  Watts
--  ------------------  ----------  ---------------  -------  -------  -----
1A  PWR-C2-1025WAC      LIT18280V8S  OK              Good     Good     1025
1B  PWR-C2-1025WAC      LIT19521485  OK              Good     Good     1025
""",
}
