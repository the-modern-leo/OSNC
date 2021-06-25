ip_address = '172.20.84.5'
software = 'software'
hardware = 'hardware'
read_results = {
 'show version':"""Cisco IOS Software, IOS-XE Software, Catalyst L3 Switch Software (CAT3K_CAA-UNIVERSALK9-M), Version 03.07.04E RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2016 by Cisco Systems, Inc.
Compiled Thu 19-May-16 11:48 by prod_rel_team



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
BOOTLDR: CAT3K_CAA Boot Loader (CAT3K_CAA-HBOOT-M) Version 3.58, RELEASE SOFTWARE (P)

dx1-522wpav-wm320-clinical uptime is 4 years, 16 weeks, 6 days, 22 hours, 33 minutes
Uptime for this control processor is 4 years, 16 weeks, 6 days, 22 hours, 35 minutes
System returned to ROM by Power Failure
System restarted at 17:15:35 MST Mon Feb 27 2017
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

cisco WS-C3850-24XS (MIPS) processor with 4194304K bytes of physical memory.
Processor board ID FOC2046U22R
3 Virtual Ethernet interfaces
32 Ten Gigabit Ethernet interfaces
2 Forty Gigabit Ethernet interfaces
2048K bytes of non-volatile configuration memory.
4194304K bytes of physical memory.
          255037K bytes of Crash Files at crashinfo:.
3417161K bytes of Flash at flash:.
0K bytes of Dummy USB Flash at usbflash0:.
0K bytes of  at webui:.

Base Ethernet MAC Address          : 08:cc:a7:5a:98:80
Motherboard Assembly Number        : 73-16649-06
Motherboard Serial Number          : FOC20305Q3N
Model Revision Number              : J0
Motherboard Revision Number        : A0
Model Number                       : WS-C3850-24XS
System Serial Number               : FOC2046U22R


Switch Ports Model              SW Version        SW Image              Mode   
------ ----- -----              ----------        ----------            ----   
*    1 34    WS-C3850-24XS      03.07.04E         cat3k_caa-universalk9 INSTALL


Configuration register is 0x102
""",
 'show run':"""Building configuration...

Current configuration : 14933 bytes
!
! Last configuration change at 12:01:26 MDT Mon Apr 26 2021 by noc-orionncm
! NVRAM config last updated at 21:40:24 MDT Sun Jun 20 2021 by noc-orionncm
!
version 15.2
no service pad
service timestamps debug datetime msec localtime
service timestamps log datetime msec localtime
service password-encryption
service compress-config
!
hostname dx1-522wpav-wm320-clinical
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
enable secret 5 $1$LDJQ$sng2RMmQUA4hiC7lXfOFM1
!
software auto-upgrade enable
!
aaa new-model
!
!
aaa group server tacacs+ default
 server name TAC-DDC
 server name TAC-PARK
!
aaa group server tacacs+ NOC-TAC
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
switch 1 provision ws-c3850-24xs
!
!
!
!
!
coap http enable
!
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
vtp domain vtp-522wpav
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
diagnostic bootup level minimal
          !
spanning-tree mode rapid-pvst
spanning-tree extend system-id
spanning-tree vlan 1-4094 priority 28672
hw-switch switch 1 logging onboard message level 3
!
redundancy
 mode sso
!
!
vlan 118
 name Clin-522WPav-Floor1-Zeroclients
!
vlan 119
 name Clin-522WPav-Floor2-Zeroclients
!
vlan 120
 name Clin-522WPav-Floor3-Zeroclients
!
vlan 121
 name Clin-522WPav-Floor4-Zeroclients
!
vlan 122
 name Clin-522WPav-Floor5-Zeroclients
!
vlan 201
 name clinical-522wpav-Things
!
vlan 269
 name clinical-522wpav-kronos-2
!
vlan 273
 name clinical-522wpavilion-kronoscloc
!
vlan 301
 name clin-525hosp-ScPro-Wrks
!
vlan 302
 name clin-522wpavilion-scriptcenter
!
vlan 452
 name GuestHouseCC
!
vlan 467
 name Vocera-Ilo-mgmt
!
vlan 545
 name clinical-Outpatient-pharm-E2EE
!
vlan 550
 name 522-TIGR-patientTV
!
vlan 603
 name clinical-522wpav-ehs
!
vlan 606
 name clin-522-iStar
!
vlan 625
           name clinical-522wpav-cam-5
!
vlan 628
 name 522-lan-EEG
!
vlan 647
 name 522-lan-2
!
vlan 648
 name 522-lan-1
!
vlan 649
 name 522-lan-b-a
!
vlan 650
 name 522-printer
!
vlan 651
 name 522wpav-m
!
vlan 652
 name 522-wmgmt
!
vlan 653
 name 522-env
!
vlan 668
 name 522-dvdnow-kiosk
!
vlan 682
 name clin-522hosp-utility-fm
!
vlan 685
 name 522-lan-5
!
vlan 686
 name 522-lan-4
!
vlan 687
 name 522-lan-3
!
vlan 700
 name r2clinical<->dx1-522
!
vlan 701
 name dx1-522-1_dx-hosp2
!
vlan 703
 name clinical-522wpav-pulm_beaker
!
vlan 730
 name clinical-522wpav-swiss-server
!
vlan 731
 name clinical-522wpav-swisstube
!
vlan 773
 name clin-525-ATTmetrocell
!
          vlan 842
 name fw-wpavilion-mgmt
!
vlan 920
 name Phillips_Monitoring_522
!
vlan 923
 name clin-5100acc-philips
!
vlan 992
 name VoIP-522-1
!
vlan 993
 name VoIP-522-2
!
vlan 994
 name VoIP-522-3
!
vlan 995
 name VoIP-522-4
!
vlan 996
 name VoIP-522-5
!
vlan 1025
 name clinical-522wpavilion-cbord
!
vlan 1033
 name ap-522-mgmt
!
vlan 1042
 name clin-522-AV
!
vlan 1061
 name clin-522-paging
!
vlan 1081
 name pci-522-cashreg
!
vlan 1110
 name wpav-rtls
!
vlan 1601
 name clin-522wpavilion_pharmcam
!
vlan 1602
 name clinical-522wpav-fm-cam
!
vlan 3000
 name Codeblue-Private
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
interface Port-channel10
 description key:dx1-522 <-> dx2-522
 switchport mode trunk
!
interface Port-channel30
 description key:Uplink to Clinical node
 switchport mode trunk
 ip dhcp snooping trust
!
interface GigabitEthernet0/0
 vrf forwarding Mgmt-vrf
 no ip address
 no ip route-cache
 shutdown
 negotiation auto
!
interface TenGigabitEthernet1/0/1
 description key:1/0/1:r1-clinical:eX/X
 switchport mode trunk
 channel-group 30 mode active
!
interface TenGigabitEthernet1/0/2
 description key:1/0/2:dx2-522wpav-w5260-clinical:t1/0/2
 switchport mode trunk
 channel-group 10 mode active
!
interface TenGigabitEthernet1/0/3
 description key:1/0/3:sx1-522wpav-wm320-clinical:t5/1
 switchport trunk allowed vlan 118,201,269,273,606,649-653,682,730,731,992,1033
 switchport trunk allowed vlan add 1042,1110
 switchport mode trunk
!
interface TenGigabitEthernet1/0/4
 description key:1/0/4:sx2-522wpav-wm320-clinical:t1/1/1
 switchport trunk allowed vlan 651,1033
 switchport mode trunk
!
interface TenGigabitEthernet1/0/5
 description key:1/0/5:sx1-522wpav-w1665-clinical:t5/1
 switchport trunk allowed vlan 1-684,688-4094
 switchport mode trunk
!
interface TenGigabitEthernet1/0/6
 description key:1/0/6:sx2-522wpav-w1665-clinical:t1/1/1
 switchport trunk allowed vlan 118,301,606,648-651,653,731,992,1033,1081,1110
 switchport trunk allowed vlan add 1601,1602
           switchport mode trunk
!
interface TenGigabitEthernet1/0/7
 description key:1/0/7:sx1-522wpav-w2250-clinical:t5/1
 switchport trunk allowed vlan 1-684,688-4094
 switchport mode trunk
!
interface TenGigabitEthernet1/0/8
 description key:1/0/8:sx2-522wpav-w2250-clinical:t1/1/1
 switchport trunk allowed vlan 651,1033
 switchport mode trunk
!
interface TenGigabitEthernet1/0/9
 description key:1/0/9:sx1-522wpav-w3235-clinical:t5/1
 switchport trunk allowed vlan 1-685,687-4094
 switchport mode trunk
!
interface TenGigabitEthernet1/0/10
 description key:1/0/10:sx2-522wpav-w1665:t1/1/1
 switchport mode trunk
!
interface TenGigabitEthernet1/0/11
 description key:1/0/11:sx1-522wpav-w4240-clinical:t5/1
 switchport mode trunk
!
interface TenGigabitEthernet1/0/12
 description key:1/0/12:sx2-522wpav-w4240-clinical:t1/1/1
 switchport trunk allowed vlan 651,1033
 switchport mode trunk
!
interface TenGigabitEthernet1/0/13
 description key:1/0/13:sx1-522wpav-w5260-clinical:t5/1
 switchport mode trunk
!
interface TenGigabitEthernet1/0/14
 description temporary link to sx1-522wpavilion-b 3750
 switchport trunk allowed vlan 467,550,606,649-653,682,842,992,1033,1081,1110
 switchport trunk allowed vlan add 1602
 switchport mode trunk
!
interface TenGigabitEthernet1/0/15
!
interface TenGigabitEthernet1/0/16
!
interface TenGigabitEthernet1/0/17
!
interface TenGigabitEthernet1/0/18
!
interface TenGigabitEthernet1/0/19
!
interface TenGigabitEthernet1/0/20
!
interface TenGigabitEthernet1/0/21
!
interface TenGigabitEthernet1/0/22
 description TEMP UPLINK - dx1-522-old
 switchport trunk allowed vlan 1-685,688-4094
 switchport mode trunk
!
          interface TenGigabitEthernet1/0/23
 description key:1/0/23:dx2-522wpav-w5260-clinical:t1/0/23
 switchport mode trunk
 channel-group 10 mode active
!
interface TenGigabitEthernet1/0/24
 description key:1/0/24:r2-clinical:eX/X
 switchport mode trunk
 channel-group 30 mode active
!
interface TenGigabitEthernet1/1/1
!
interface TenGigabitEthernet1/1/2
!
interface TenGigabitEthernet1/1/3
!
interface TenGigabitEthernet1/1/4
!
interface TenGigabitEthernet1/1/5
!
interface TenGigabitEthernet1/1/6
!
interface TenGigabitEthernet1/1/7
!
interface TenGigabitEthernet1/1/8
!
interface FortyGigabitEthernet1/1/1
!
interface FortyGigabitEthernet1/1/2
!
interface Vlan1
 no ip address
 no ip route-cache
 shutdown
!
interface Vlan301
 no ip address
!
interface Vlan651
 description clinical-522wpav-m
 ip address 172.20.84.5 255.255.255.128
 no ip route-cache
!
ip default-gateway 172.20.84.1
ip forward-protocol nd
no ip http server
no ip http secure-server
ip tftp blocksize 8192
ip ssh version 2
!
!
ip sla enable reaction-alerts
logging facility local6
logging source-interface Vlan651
logging host 10.71.24.11
logging host 172.24.29.14
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
snmp-server group CliNOCGrv3RO v3 priv read CliNOCViewRO access 70
snmp-server group CliNOCGrv3RO v3 auth context vlan- match prefix 
snmp-server group CliNOCGrv3RW v3 priv write CliNOCViewRW access 71
snmp-server view CliNOCViewRO internet included
snmp-server view CliNOCViewRW internet included
snmp-server location Bldg. 522 Room wm320
snmp-server contact BC-507881 Y-319847
snmp ifmib ifindex persist
tacacs server TAC-DDC
 address ipv4 155.97.160.52
 key 7 100D2339061C410F21573F3B65
tacacs server TAC-PARK
 address ipv4 155.98.253.200
 key 7 1551212C072178200560203252
tacacs server TAC-EBC
 address ipv4 172.31.17.180
 key 7 002D57032D1F0E242F23550F
tacacs server TAC-SECONDARY
 address ipv4 10.64.32.5
 key 7 0808084B205D003532091545
!
!
!
no vstack
privilege exec level 1 show configuration
privilege exec level 1 show
banner login ^C

dx1-522wpav-wm320-clinical.net.utah.edu

          
University of Utah Network: All use of this device must comply
with the University of Utah policies and procedures. Any use of
this device, whether deliberate or not will be held legally
responsible. See University of Utah Information Security
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
 password 7 046E1F0707230D1D5D
 login authentication console
 stopbits 1
line aux 0
 stopbits 1
line vty 0 4
 access-class 199 in
 exec-timeout 30 0
 password 7 0233105A03044E7218
 transport input ssh
line vty 5 15
 access-class 199 in
 exec-timeout 30 0
 password 7 0233105A03044E7218
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
Te1/0/1   key:1/0/1:r1-clini connected    trunk        full    10G SFP-10GBase-LR
Te1/0/2   key:1/0/2:dx2-522w connected    trunk        full    10G SFP-10GBase-SR
Te1/0/3   key:1/0/3:sx1-522w connected    trunk        full    10G SFP-10GBase-SR
Te1/0/4   key:1/0/4:sx2-522w notconnect   1            full    10G unknown
Te1/0/5   key:1/0/5:sx1-522w connected    trunk        full    10G SFP-10GBase-SR
Te1/0/6   key:1/0/6:sx2-522w connected    trunk        full    10G SFP-10GBase-SR
Te1/0/7   key:1/0/7:sx1-522w connected    trunk        full    10G SFP-10GBase-SR
Te1/0/8   key:1/0/8:sx2-522w notconnect   1            full    10G SFP-10GBase-SR
Te1/0/9   key:1/0/9:sx1-522w connected    trunk        full    10G SFP-10GBase-SR
Te1/0/10  key:1/0/10:sx2-522 connected    trunk        full    10G SFP-10GBase-SR
Te1/0/11  key:1/0/11:sx1-522 connected    trunk        full    10G SFP-10GBase-SR
Te1/0/12  key:1/0/12:sx2-522 notconnect   1            full    10G SFP-10GBase-SR
Te1/0/13  key:1/0/13:sx1-522 connected    trunk        full    10G SFP-10GBase-SR
Te1/0/14  temporary link to  notconnect   1            full    10G SFP-10GBase-SR
Te1/0/15                     notconnect   1            auto   auto unknown
Te1/0/16                     notconnect   1            auto   auto unknown
Te1/0/17                     notconnect   1            auto   auto unknown
Te1/0/18                     notconnect   1            auto   auto unknown
Te1/0/19                     notconnect   1            auto   auto unknown
Te1/0/20                     notconnect   1            full    10G unknown
Te1/0/21                     notconnect   1            auto   auto unknown
Te1/0/22  TEMP UPLINK - dx1- notconnect   1            full    10G unknown
Te1/0/23  key:1/0/23:dx2-522 connected    trunk        full    10G SFP-10GBase-SR
Te1/0/24  key:1/0/24:r2-clin connected    trunk        full    10G SFP-10GBase-LR
Po10      key:dx1-522 <-> dx connected    trunk      a-full  a-10G 
Po30      key:Uplink to Clin connected    trunk      a-full  a-10G """,
 'show run | section interface':"""match interface input
 collect interface output
interface Port-channel10
 description key:dx1-522 <-> dx2-522
 switchport mode trunk
interface Port-channel30
 description key:Uplink to Clinical node
 switchport mode trunk
 ip dhcp snooping trust
interface GigabitEthernet0/0
 vrf forwarding Mgmt-vrf
 no ip address
 no ip route-cache
 shutdown
 negotiation auto
interface TenGigabitEthernet1/0/1
 description key:1/0/1:r1-clinical:eX/X
 switchport mode trunk
 channel-group 30 mode active
interface TenGigabitEthernet1/0/2
 description key:1/0/2:dx2-522wpav-w5260-clinical:t1/0/2
 switchport mode trunk
 channel-group 10 mode active
interface TenGigabitEthernet1/0/3
 description key:1/0/3:sx1-522wpav-wm320-clinical:t5/1
 switchport trunk allowed vlan 118,201,269,273,606,649-653,682,730,731,992,1033
 switchport trunk allowed vlan add 1042,1110
 switchport mode trunk
interface TenGigabitEthernet1/0/4
 description key:1/0/4:sx2-522wpav-wm320-clinical:t1/1/1
 switchport trunk allowed vlan 651,1033
 switchport mode trunk
interface TenGigabitEthernet1/0/5
 description key:1/0/5:sx1-522wpav-w1665-clinical:t5/1
 switchport trunk allowed vlan 1-684,688-4094
 switchport mode trunk
interface TenGigabitEthernet1/0/6
 description key:1/0/6:sx2-522wpav-w1665-clinical:t1/1/1
 switchport trunk allowed vlan 118,301,606,648-651,653,731,992,1033,1081,1110
 switchport trunk allowed vlan add 1601,1602
 switchport mode trunk
interface TenGigabitEthernet1/0/7
 description key:1/0/7:sx1-522wpav-w2250-clinical:t5/1
 switchport trunk allowed vlan 1-684,688-4094
 switchport mode trunk
interface TenGigabitEthernet1/0/8
 description key:1/0/8:sx2-522wpav-w2250-clinical:t1/1/1
 switchport trunk allowed vlan 651,1033
 switchport mode trunk
interface TenGigabitEthernet1/0/9
 description key:1/0/9:sx1-522wpav-w3235-clinical:t5/1
 switchport trunk allowed vlan 1-685,687-4094
 switchport mode trunk
interface TenGigabitEthernet1/0/10
 description key:1/0/10:sx2-522wpav-w1665:t1/1/1
 switchport mode trunk
interface TenGigabitEthernet1/0/11
 description key:1/0/11:sx1-522wpav-w4240-clinical:t5/1
 switchport mode trunk
          interface TenGigabitEthernet1/0/12
 description key:1/0/12:sx2-522wpav-w4240-clinical:t1/1/1
 switchport trunk allowed vlan 651,1033
 switchport mode trunk
interface TenGigabitEthernet1/0/13
 description key:1/0/13:sx1-522wpav-w5260-clinical:t5/1
 switchport mode trunk
interface TenGigabitEthernet1/0/14
 description temporary link to sx1-522wpavilion-b 3750
 switchport trunk allowed vlan 467,550,606,649-653,682,842,992,1033,1081,1110
 switchport trunk allowed vlan add 1602
 switchport mode trunk
interface TenGigabitEthernet1/0/15
interface TenGigabitEthernet1/0/16
interface TenGigabitEthernet1/0/17
interface TenGigabitEthernet1/0/18
interface TenGigabitEthernet1/0/19
interface TenGigabitEthernet1/0/20
interface TenGigabitEthernet1/0/21
interface TenGigabitEthernet1/0/22
 description TEMP UPLINK - dx1-522-old
 switchport trunk allowed vlan 1-685,688-4094
 switchport mode trunk
interface TenGigabitEthernet1/0/23
 description key:1/0/23:dx2-522wpav-w5260-clinical:t1/0/23
 switchport mode trunk
 channel-group 10 mode active
interface TenGigabitEthernet1/0/24
 description key:1/0/24:r2-clinical:eX/X
 switchport mode trunk
 channel-group 30 mode active
interface TenGigabitEthernet1/1/1
interface TenGigabitEthernet1/1/2
interface TenGigabitEthernet1/1/3
interface TenGigabitEthernet1/1/4
interface TenGigabitEthernet1/1/5
interface TenGigabitEthernet1/1/6
interface TenGigabitEthernet1/1/7
interface TenGigabitEthernet1/1/8
interface FortyGigabitEthernet1/1/1
interface FortyGigabitEthernet1/1/2
interface Vlan1
 no ip address
 no ip route-cache
 shutdown
interface Vlan301
 no ip address
interface Vlan651
 description clinical-522wpav-m
 ip address 172.20.84.5 255.255.255.128
 no ip route-cache
logging source-interface Vlan651""",
 'show run | in interface':"""match interface input
 collect interface output
interface Port-channel10
interface Port-channel30
interface GigabitEthernet0/0
interface TenGigabitEthernet1/0/1
interface TenGigabitEthernet1/0/2
interface TenGigabitEthernet1/0/3
interface TenGigabitEthernet1/0/4
interface TenGigabitEthernet1/0/5
interface TenGigabitEthernet1/0/6
interface TenGigabitEthernet1/0/7
interface TenGigabitEthernet1/0/8
interface TenGigabitEthernet1/0/9
interface TenGigabitEthernet1/0/10
interface TenGigabitEthernet1/0/11
interface TenGigabitEthernet1/0/12
interface TenGigabitEthernet1/0/13
interface TenGigabitEthernet1/0/14
interface TenGigabitEthernet1/0/15
interface TenGigabitEthernet1/0/16
interface TenGigabitEthernet1/0/17
interface TenGigabitEthernet1/0/18
interface TenGigabitEthernet1/0/19
interface TenGigabitEthernet1/0/20
interface TenGigabitEthernet1/0/21
interface TenGigabitEthernet1/0/22
interface TenGigabitEthernet1/0/23
interface TenGigabitEthernet1/0/24
interface TenGigabitEthernet1/1/1
interface TenGigabitEthernet1/1/2
interface TenGigabitEthernet1/1/3
interface TenGigabitEthernet1/1/4
interface TenGigabitEthernet1/1/5
interface TenGigabitEthernet1/1/6
interface TenGigabitEthernet1/1/7
interface TenGigabitEthernet1/1/8
interface FortyGigabitEthernet1/1/1
interface FortyGigabitEthernet1/1/2
interface Vlan1
interface Vlan301
interface Vlan651
logging source-interface Vlan651""",
 'show interface link':"""^
% Invalid input detected at '^' marker.
""",
 'show interface':"""GigabitEthernet0/0 is administratively down, line protocol is down 
  NOTE: Packet counters for management port are meaningful 
        only when it is physically located at stack master
  Hardware is RP management port, address is 08cc.a75a.9880 (bia 08cc.a75a.9880)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Unknown, Unknown, link type is auto, media type is RJ45
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
Vlan1 is administratively down, line protocol is down 
  Hardware is Ethernet SVI, address is 08cc.a75a.98c7 (bia 08cc.a75a.98c7)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 46w4d, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     591377332 packets input, 81710443480 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 1 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Vlan301 is up, line protocol is up 
  Hardware is Ethernet SVI, address is 08cc.a75a.98e2 (bia 08cc.a75a.98e2)
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
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     311712028 packets input, 29079821313 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 1 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Vlan651 is up, line protocol is up 
  Hardware is Ethernet SVI, address is 08cc.a75a.98c4 (bia 08cc.a75a.98c4)
  Description: clinical-522wpav-m
  Internet address is 172.20.84.5/25
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/75/46781/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 16000 bits/sec, 14 packets/sec
  5 minute output rate 22000 bits/sec, 12 packets/sec
     1947408058 packets input, 298645472576 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     621633660 packets output, 192391936557 bytes, 0 underruns
     0 output errors, 2 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/0/1 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet, address is 08cc.a75a.9881 (bia 08cc.a75a.9881)
  Description: key:1/0/1:r1-clinical:eX/X
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not set
  Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-LR
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 1606896
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 55000 bits/sec, 69 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     6007602476 packets input, 663540054244 bytes, 0 no buffer
     Received 5795280476 broadcasts (41627272 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
               0 watchdog, 41627272 multicast, 0 pause input
     0 input packets with dribble condition detected
     356314280 packets output, 80051754251 bytes, 0 underruns
     1606896 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/0/2 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet, address is 08cc.a75a.9882 (bia 08cc.a75a.9882)
  Description: key:1/0/2:dx2-522wpav-w5260-clinical:t1/0/2
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not set
  Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-SR
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:11, output never, output hang never
  Last clearing of "" counters 3y4w
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 814566
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 64000 bits/sec, 60 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     32474493309 packets input, 32717178919869 bytes, 0 no buffer
     Received 28832078473 broadcasts (1607263945 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 1607263945 multicast, 0 pause input
     0 input packets with dribble condition detected
     1482232455 packets output, 323113063204 bytes, 0 underruns
     814566 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/0/3 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet, address is 08cc.a75a.9883 (bia 08cc.a75a.9883)
  Description: key:1/0/3:sx1-522wpav-wm320-clinical:t5/1
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not set
  Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-SR
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 355464416
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 3000 bits/sec, 5 packets/sec
  5 minute output rate 37000 bits/sec, 41 packets/sec
     3258196475 packets input, 671408283378 bytes, 0 no buffer
     Received 429814429 broadcasts (379736003 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 379736003 multicast, 0 pause input
               0 input packets with dribble condition detected
     8926796620 packets output, 3071844899264 bytes, 0 underruns
     355464416 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/0/4 is down, line protocol is down (notconnect) 
  Hardware is Ten Gigabit Ethernet, address is 08cc.a75a.9884 (bia 08cc.a75a.9884)
  Description: key:1/0/4:sx2-522wpav-wm320-clinical:t1/1/1
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not set
  Full-duplex, 10Gb/s, link type is auto, media type is unknown
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 3y4w, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     56801580 packets input, 16033126663 bytes, 0 no buffer
     Received 5902204 broadcasts (5902114 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 5902114 multicast, 0 pause input
     0 input packets with dribble condition detected
     360715063 packets output, 41070134039 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/0/5 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet, address is 08cc.a75a.9885 (bia 08cc.a75a.9885)
  Description: key:1/0/5:sx1-522wpav-w1665-clinical:t5/1
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not set
  Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-SR
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 20518579
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 78000 bits/sec, 95 packets/sec
     43128311 packets input, 9945764812 bytes, 0 no buffer
     Received 21494477 broadcasts (20731593 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 20731593 multicast, 0 pause input
     0 input packets with dribble condition detected
               35237275933 packets output, 22936715915974 bytes, 0 underruns
     20518579 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/0/6 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet, address is 08cc.a75a.9886 (bia 08cc.a75a.9886)
  Description: key:1/0/6:sx2-522wpav-w1665-clinical:t1/1/1
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not set
  Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-SR
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 2297308
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 31000 bits/sec, 40 packets/sec
     183865549 packets input, 30722060816 bytes, 0 no buffer
     Received 116240492 broadcasts (110204252 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 110204252 multicast, 0 pause input
     0 input packets with dribble condition detected
     5514563520 packets output, 682600243507 bytes, 0 underruns
     2297308 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/0/7 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet, address is 08cc.a75a.9887 (bia 08cc.a75a.9887)
  Description: key:1/0/7:sx1-522wpav-w2250-clinical:t5/1
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not set
  Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-SR
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:06, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 178394246
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 78000 bits/sec, 95 packets/sec
     36062627 packets input, 7697783565 bytes, 0 no buffer
     Received 28892450 broadcasts (23728696 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 23728696 multicast, 0 pause input
     0 input packets with dribble condition detected
     35231209921 packets output, 22934398425472 bytes, 0 underruns
               178394246 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/0/8 is down, line protocol is down (notconnect) 
  Hardware is Ten Gigabit Ethernet, address is 08cc.a75a.9888 (bia 08cc.a75a.9888)
  Description: key:1/0/8:sx2-522wpav-w2250-clinical:t1/1/1
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not set
  Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-SR
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 3y3w, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 436
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     8108056 packets input, 1903564497 bytes, 0 no buffer
     Received 5803282 broadcasts (5803281 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 5803281 multicast, 0 pause input
     0 input packets with dribble condition detected
     283672361 packets output, 29684084351 bytes, 0 underruns
     436 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/0/9 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet, address is 08cc.a75a.9889 (bia 08cc.a75a.9889)
  Description: key:1/0/9:sx1-522wpav-w3235-clinical:t5/1
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not set
  Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-SR
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:01, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 3402699
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 3000 bits/sec, 3 packets/sec
  5 minute output rate 81000 bits/sec, 97 packets/sec
     380447150 packets input, 71301913963 bytes, 0 no buffer
     Received 369525774 broadcasts (259737971 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 259737971 multicast, 0 pause input
     0 input packets with dribble condition detected
     35709632953 packets output, 23008285533160 bytes, 0 underruns
     3402699 output errors, 0 collisions, 3 interface resets
               0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/0/10 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet, address is 08cc.a75a.988a (bia 08cc.a75a.988a)
  Description: key:1/0/10:sx2-522wpav-w1665:t1/1/1
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not set
  Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-SR
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:02, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 15078
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 82000 bits/sec, 99 packets/sec
     8582062 packets input, 1977104822 bytes, 0 no buffer
     Received 4996318 broadcasts (4959224 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 4959224 multicast, 0 pause input
     0 input packets with dribble condition detected
     3426780132 packets output, 364660967794 bytes, 0 underruns
     15078 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/0/11 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet, address is 08cc.a75a.988b (bia 08cc.a75a.988b)
  Description: key:1/0/11:sx1-522wpav-w4240-clinical:t5/1
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not set
  Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-SR
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:03, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 37291751
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 83000 bits/sec, 99 packets/sec
     28926140 packets input, 7226690248 bytes, 0 no buffer
     Received 20803846 broadcasts (20729659 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 20729659 multicast, 0 pause input
     0 input packets with dribble condition detected
     35985662011 packets output, 23034718429513 bytes, 0 underruns
     37291751 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
               0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/0/12 is down, line protocol is down (notconnect) 
  Hardware is Ten Gigabit Ethernet, address is 08cc.a75a.988c (bia 08cc.a75a.988c)
  Description: key:1/0/12:sx2-522wpav-w4240-clinical:t1/1/1
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not set
  Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-SR
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 3y1w, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 226374
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     7942523 packets input, 1895539356 bytes, 0 no buffer
     Received 6046687 broadcasts (6046687 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 6046687 multicast, 0 pause input
     0 input packets with dribble condition detected
     291996200 packets output, 30432644375 bytes, 0 underruns
     226374 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/0/13 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet, address is 08cc.a75a.988d (bia 08cc.a75a.988d)
  Description: key:1/0/13:sx1-522wpav-w5260-clinical:t5/1
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not set
  Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-SR
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:01, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 590872309
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 82000 bits/sec, 99 packets/sec
     15563300 packets input, 3739152219 bytes, 0 no buffer
     Received 14582203 broadcasts (14582127 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 14582127 multicast, 0 pause input
     0 input packets with dribble condition detected
     10648027253 packets output, 1095759510292 bytes, 0 underruns
     590872309 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
               0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/0/14 is down, line protocol is down (notconnect) 
  Hardware is Ten Gigabit Ethernet, address is 08cc.a75a.988e (bia 08cc.a75a.988e)
  Description: temporary link to sx1-522wpavilion-b 3750
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not set
  Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-SR
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y21w, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     79629587 packets input, 17218907662 bytes, 0 no buffer
     Received 29625135 broadcasts (29548280 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 29548280 multicast, 0 pause input
     0 input packets with dribble condition detected
     926122587 packets output, 87916510124 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/0/15 is down, line protocol is down (notconnect) 
  Hardware is Ten Gigabit Ethernet, address is 08cc.a75a.988f (bia 08cc.a75a.988f)
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
          TenGigabitEthernet1/0/16 is down, line protocol is down (notconnect) 
  Hardware is Ten Gigabit Ethernet, address is 08cc.a75a.9890 (bia 08cc.a75a.9890)
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
TenGigabitEthernet1/0/17 is down, line protocol is down (notconnect) 
  Hardware is Ten Gigabit Ethernet, address is 08cc.a75a.9891 (bia 08cc.a75a.9891)
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
TenGigabitEthernet1/0/18 is down, line protocol is down (notconnect) 
  Hardware is Ten Gigabit Ethernet, address is 08cc.a75a.9892 (bia 08cc.a75a.9892)
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
TenGigabitEthernet1/0/19 is down, line protocol is down (notconnect) 
  Hardware is Ten Gigabit Ethernet, address is 08cc.a75a.9893 (bia 08cc.a75a.9893)
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
TenGigabitEthernet1/0/20 is down, line protocol is down (notconnect) 
  Hardware is Ten Gigabit Ethernet, address is 08cc.a75a.9894 (bia 08cc.a75a.9894)
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not set
            Full-duplex, 10Gb/s, link type is auto, media type is unknown
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 4y5w, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     45 packets input, 9460 bytes, 0 no buffer
     Received 45 broadcasts (45 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 45 multicast, 0 pause input
     0 input packets with dribble condition detected
     77 packets output, 15993 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/0/21 is down, line protocol is down (notconnect) 
  Hardware is Ten Gigabit Ethernet, address is 08cc.a75a.9895 (bia 08cc.a75a.9895)
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
TenGigabitEthernet1/0/22 is down, line protocol is down (notconnect) 
  Hardware is Ten Gigabit Ethernet, address is 08cc.a75a.9896 (bia 08cc.a75a.9896)
  Description: TEMP UPLINK - dx1-522-old
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not set
  Full-duplex, 10Gb/s, link type is auto, media type is unknown
  input flow-control is off, output flow-control is unsupported 
            ARP type: ARPA, ARP Timeout 04:00:00
  Last input 3y1w, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 15125306
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     402984237751 packets input, 168323180990583 bytes, 0 no buffer
     Received 4833594866 broadcasts (2914936241 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 2914936241 multicast, 0 pause input
     0 input packets with dribble condition detected
     1449539999 packets output, 444046126870 bytes, 0 underruns
     15125306 output errors, 0 collisions, 3 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/0/23 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet, address is 08cc.a75a.9897 (bia 08cc.a75a.9897)
  Description: key:1/0/23:dx2-522wpav-w5260-clinical:t1/0/23
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not set
  Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-SR
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:14, output never, output hang never
  Last clearing of "" counters 3y4w
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 16405677
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 60000 bits/sec, 80 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     32732334183 packets input, 34190426007235 bytes, 0 no buffer
     Received 32584527625 broadcasts (1159088818 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 1159088818 multicast, 0 pause input
     0 input packets with dribble condition detected
     1818656959 packets output, 468044806936 bytes, 0 underruns
     16405677 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/0/24 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet, address is 08cc.a75a.9898 (bia 08cc.a75a.9898)
  Description: key:1/0/24:r2-clinical:eX/X
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not set
  Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-LR
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
            Last input 00:00:00, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 167774
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 52000 bits/sec, 63 packets/sec
  5 minute output rate 25000 bits/sec, 15 packets/sec
     6315830148 packets input, 782788240909 bytes, 0 no buffer
     Received 6003957749 broadcasts (465698528 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 465698528 multicast, 0 pause input
     0 input packets with dribble condition detected
     339175861 packets output, 73237336674 bytes, 0 underruns
     167774 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/1/1 is down, line protocol is down (notconnect) 
  Hardware is not present
  Hardware is Ten Gigabit Ethernet, address is 08cc.a75a.9899 (bia 08cc.a75a.9899)
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not set
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
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/1/2 is down, line protocol is down (notconnect) 
  Hardware is not present
  Hardware is Ten Gigabit Ethernet, address is 08cc.a75a.989a (bia 08cc.a75a.989a)
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not set
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
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/1/3 is down, line protocol is down (notconnect) 
  Hardware is not present
  Hardware is Ten Gigabit Ethernet, address is 08cc.a75a.989b (bia 08cc.a75a.989b)
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not set
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
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/1/4 is down, line protocol is down (notconnect) 
  Hardware is not present
  Hardware is Ten Gigabit Ethernet, address is 08cc.a75a.989c (bia 08cc.a75a.989c)
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not set
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
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/1/5 is down, line protocol is down (notconnect) 
  Hardware is not present
  Hardware is Ten Gigabit Ethernet, address is 08cc.a75a.989d (bia 08cc.a75a.989d)
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not set
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
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/1/6 is down, line protocol is down (notconnect) 
  Hardware is not present
  Hardware is Ten Gigabit Ethernet, address is 08cc.a75a.989e (bia 08cc.a75a.989e)
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not set
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
     0 output errors, 0 collisions, 0 interface resets
               0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/1/7 is down, line protocol is down (notconnect) 
  Hardware is not present
  Hardware is Ten Gigabit Ethernet, address is 08cc.a75a.989f (bia 08cc.a75a.989f)
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not set
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
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/1/8 is down, line protocol is down (notconnect) 
  Hardware is not present
  Hardware is Ten Gigabit Ethernet, address is 08cc.a75a.98a0 (bia 08cc.a75a.98a0)
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not set
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
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
FortyGigabitEthernet1/1/1 is down, line protocol is down (notconnect) 
            Hardware is not present
  Hardware is Forty Gigabit Ethernet, address is 08cc.a75a.98a1 (bia 08cc.a75a.98a1)
  MTU 1500 bytes, BW 40000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not set
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
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
FortyGigabitEthernet1/1/2 is down, line protocol is down (notconnect) 
  Hardware is not present
  Hardware is Forty Gigabit Ethernet, address is 08cc.a75a.98a2 (bia 08cc.a75a.98a2)
  MTU 1500 bytes, BW 40000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not set
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
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
Port-channel10 is up, line protocol is up (connected) 
  Hardware is EtherChannel, address is 08cc.a75a.9882 (bia 08cc.a75a.9882)
  Description: key:dx1-522 <-> dx2-522
  MTU 1500 bytes, BW 20000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
            Keepalive set (10 sec)
  Full-duplex, 10Gb/s, link type is auto, media type is 
  input flow-control is off, output flow-control is unsupported 
  Members in this channel: Te1/0/2 Te1/0/23 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output never, output hang never
  Last clearing of "" counters 3y4w
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 4270682626
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 122000 bits/sec, 139 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     65209978392 packets input, 66909278127352 bytes, 0 no buffer
     Received 61416814937 broadcasts (2766554883 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 2766554883 multicast, 0 pause input
     0 input packets with dribble condition detected
     3303811750 packets output, 792404030897 bytes, 0 underruns
     17220243 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
Port-channel30 is up, line protocol is up (connected) 
  Hardware is EtherChannel, address is 08cc.a75a.9898 (bia 08cc.a75a.9898)
  Description: key:Uplink to Clinical node
  MTU 1500 bytes, BW 20000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 10Gb/s, link type is auto, media type is 
  input flow-control is off, output flow-control is unsupported 
  Members in this channel: Te1/0/1 Te1/0/24 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 106000 bits/sec, 129 packets/sec
  5 minute output rate 25000 bits/sec, 16 packets/sec
     12323433049 packets input, 1446328332259 bytes, 0 no buffer
     Received 11799238545 broadcasts (507326072 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 507326072 multicast, 0 pause input
     0 input packets with dribble condition detected
     695490142 packets output, 153289091077 bytes, 0 underruns
     1774670 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out""",
 'show inventory':"""NAME: "c38xx Stack", DESCR: "c38xx Stack"
PID: WS-C3850-24XS     , VID: V02  , SN: FOC2046U22R

NAME: "Switch 1", DESCR: "WS-C3850-24XS-S"
PID: WS-C3850-24XS-S   , VID: V02  , SN: FOC2046U22R

NAME: "Switch 1 - Power Supply A", DESCR: "Switch 1 - Power Supply A"
PID: PWR-C1-1100WAC    , VID: V02  , SN: DTN2039V392

NAME: "Switch 1 - Power Supply B", DESCR: "Switch 1 - Power Supply B"
PID: PWR-C1-1100WAC    , VID: V02  , SN: DTN2039V370

NAME: "Te1/0/3", DESCR: "SFP-10GBase-SR"
PID: SFP-10G-SR         , VID: V03  , SN: EA601120913    

NAME: "Te1/0/1", DESCR: "SFP-10GBase-LR"
PID: SFP-10G-LR         , VID: V01  , SN: ECL142401G7    

NAME: "Te1/0/2", DESCR: "SFP-10GBase-SR"
PID: SFP-10G-SR         , VID: V03  , SN: EA612201407    

NAME: "Te1/0/5", DESCR: "SFP-10GBase-SR"
PID: SFP-10G-SR         , VID: V03  , SN: EA601120915    

NAME: "Te1/0/6", DESCR: "SFP-10GBase-SR"
PID: SFP-10G-SR         , VID: V03  , SN: EA601120914    

NAME: "Te1/0/7", DESCR: "SFP-10GBase-SR"
PID: SFP-10G-SR         , VID: V03  , SN: EA601120916    

NAME: "Te1/0/8", DESCR: "SFP-10GBase-SR"
PID: SFP-10G-SR         , VID: V03  , SN: EA505310107    

NAME: "Te1/0/9", DESCR: "SFP-10GBase-SR"
PID: SFP-10G-SR         , VID: V03  , SN: EA509291541    

NAME: "Te1/0/10", DESCR: "SFP-10GBase-SR"
PID: SFP-10G-SR         , VID: V03  , SN: EA170217685    

NAME: "Te1/0/11", DESCR: "SFP-10GBase-SR"
PID: SFP-10G-SR         , VID: V03  , SN: EA170217684    

NAME: "Te1/0/12", DESCR: "SFP-10GBase-SR"
PID: SFP-10G-SR         , VID: V03  , SN: EA170217683    

NAME: "Te1/0/13", DESCR: "SFP-10GBase-SR"
PID: SFP-10G-SR         , VID: V03  , SN: EA170217682    

NAME: "Te1/0/14", DESCR: "SFP-10GBase-SR"
PID: SFP-10G-SR         , VID: V03  , SN: EA170217681    

NAME: "Te1/0/23", DESCR: "SFP-10GBase-SR"
PID: SFP-10G-SR         , VID: V03  , SN: EA612201406    

NAME: "Te1/0/24", DESCR: "SFP-10GBase-LR"
PID: SFP-10G-LR         , VID: V02  , SN: FNS17511U9B    

""",
 'show interface counters':"""Port            InOctets    InUcastPkts    InMcastPkts    InBcastPkts 
Te1/0/1     663540091350      212322105     4336594840     1458685956 
Te1/0/2   32717178958444     3642414838    27377067961     1455010783 
Te1/0/3     671408285606     2828382046      379736027       50078428 
Te1/0/4      16033126663       50899376        5902114             90 
Te1/0/5       9945765234       21633834       20731594         762884 
Te1/0/6      30722061080       67625057      110204256        6036240 
Te1/0/7       7697783565        7170177       23728696        5163754 
Te1/0/8       1903564497        2304774        5803281              1 
Te1/0/9      71301916323       10921376      259737984      109787803 
Te1/0/10      1977105375        3585744        4959226          37094 
Te1/0/11      7226690248        8122294       20729659          74187 
Te1/0/12      1895539356        1895836        6046687              0 
Te1/0/13      3739152957         981097       14582130             76 
Te1/0/14     17218907662       50004452       29548280          76855 
Te1/0/15               0              0              0              0 
Te1/0/16               0              0              0              0 
Te1/0/17               0              0              0              0 
Te1/0/18               0              0              0              0 
Te1/0/19               0              0              0              0 
Te1/0/20            9460              0             45              0 
Te1/0/21               0              0              0              0 
Te1/0/22  168323180990583   398150642885     2914936241     1918658625 
Te1/0/23  34190426007235      147806558    31223859890     1360667735 
Te1/0/24    782788240909      311872399     4760665824     1243291925 
Po10      66909278127352     3793163455    58601129731     2815685206 
Po30       1446328332259      524194504     9097260664     2701977881 

Port           OutOctets   OutUcastPkts   OutMcastPkts   OutBcastPkts 
Te1/0/1      80051754403      195104825      160819462         389994 
Te1/0/2     323113063415     1427666005       34086367       20480085 
Te1/0/3    3071844921054     3401728390     3731651915     1793416502 
Te1/0/4      41070134039      148547049      127741264       84426750 
Te1/0/5   22936715964178     8511233553    22124497316     4601545534 
Te1/0/6     682600260049      208047020     3159691809     2146824861 
Te1/0/7   22934398473334     8509312760    22124740541     4597157089 
Te1/0/8      29684084351       67222306      127389001       89061054 
Te1/0/9   23008285580961     8494062130    22474566181     4741005099 
Te1/0/10    364661017474       13219783     2766874605      646686215 
Te1/0/11  23034718478878     8495327547    22641664118     4848670815 
Te1/0/12     30432644375       67073172      132793998       92129030 
Te1/0/13   1095759559442       21753844     7924973866     2701300013 
Te1/0/14     87916510124       52844440      425844769      447433378 
Te1/0/15               0              0              0              0 
Te1/0/16               0              0              0              0 
Te1/0/17               0              0              0              0 
Te1/0/18               0              0              0              0 
Te1/0/19               0              0              0              0 
Te1/0/20           15993              0             77              0 
Te1/0/21               0              0              0              0 
Te1/0/22    444046126870     1050677893       96370399      302491707 
Te1/0/23    468044806936     1766515938       29483297       22657724 
Te1/0/24     73237336674      219115988      120033373          26500 
Po10        792404030897     3197096096       63570345       43145309 
Po30        153289091077      414220813      280852835         416494 """,
 'show cdp nei detail':"""-------------------------
Device ID: sx1-522wpav-wm320-clinical.net.utah.edu
Entry address(es): 
  IP address: 172.20.84.18
Platform: cisco WS-C4510R+E,  Capabilities: Switch IGMP 
Interface: TenGigabitEthernet1/0/3,  Port ID (outgoing port): TenGigabitEthernet5/7
Holdtime : 155 sec

Version :
Cisco IOS Software, IOS-XE Software, Catalyst 4500 L3 Switch  Software (cat4500es8-UNIVERSALK9-M), Version 03.09.00.E RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2016 by Cisco Systems, Inc.
Compiled Tue 19-Jul-16 12:34 by prod_rel_team

advertisement version: 2
VTP Management Domain: 'vtp-522wpav'
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 172.20.84.18

-------------------------
Device ID: r2-clinical-park.net.utah.edu(JPG224500DL)
Entry address(es): 
  IP address: 10.104.216.3
Platform: N77-C7710,  Capabilities: Router Switch IGMP CVTA phone port 
Interface: TenGigabitEthernet1/0/24,  Port ID (outgoing port): Ethernet1/9
Holdtime : 134 sec

Version :
Cisco Nexus Operating System (NX-OS) Software, Version 8.2(2)

advertisement version: 2
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 172.29.1.17

-------------------------
Device ID: sx2-0522wpav-w1665-clinical.net.utah.edu
Entry address(es): 
  IP address: 172.20.84.26
Platform: cisco WS-C3850-48P,  Capabilities: Switch IGMP 
Interface: TenGigabitEthernet1/0/6,  Port ID (outgoing port): TenGigabitEthernet1/1/4
Holdtime : 144 sec

Version :
Cisco IOS Software, Catalyst L3 Switch Software (CAT3K_CAA-UNIVERSALK9-M), Version 15.2(2)E6, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2016 by Cisco Systems, Inc.
Compiled Sat 17-Dec-16 00:22 by prod_rel_team

advertisement version: 2
VTP Management Domain: 'vtp-522wpav'
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 172.20.84.26
          
-------------------------
Device ID: sx1-522wpav-w3235-clinical.net.utah.edu
Entry address(es): 
  IP address: 172.20.84.33
Platform: cisco WS-C4510R+E,  Capabilities: Switch IGMP 
Interface: TenGigabitEthernet1/0/9,  Port ID (outgoing port): TenGigabitEthernet5/1
Holdtime : 174 sec

Version :
Cisco IOS Software, IOS-XE Software, Catalyst 4500 L3 Switch  Software (cat4500es8-UNIVERSALK9-M), Version 03.09.00.E RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2016 by Cisco Systems, Inc.
Compiled Tue 19-Jul-16 12:34 by prod_rel_team

advertisement version: 2
VTP Management Domain: 'vtp-522wpav'
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 172.20.84.33

-------------------------
Device ID: sx3-522wpav-w1665-clinical.net.utah.edu
Entry address(es): 
  IP address: 172.20.84.29
Platform: cisco C9300-48U,  Capabilities: Switch IGMP 
Interface: TenGigabitEthernet1/0/10,  Port ID (outgoing port): TenGigabitEthernet1/1/1
Holdtime : 171 sec

Version :
Cisco IOS Software [Gibraltar], Catalyst L3 Switch Software (CAT9K_IOSXE), Version 16.12.3a, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2020 by Cisco Systems, Inc.
Compiled Tue 28-Apr-20 09:37 by mcpre

advertisement version: 2
VTP Management Domain: 'vtp-522wpav'
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 172.20.84.29

-------------------------
Device ID: sx1-522wpav-w2250-clinical.net.utah.edu
Entry address(es): 
  IP address: 172.20.84.27
Platform: cisco WS-C4510R+E,  Capabilities: Switch IGMP 
Interface: TenGigabitEthernet1/0/7,  Port ID (outgoing port): TenGigabitEthernet5/1
Holdtime : 125 sec

Version :
Cisco IOS Software, IOS-XE Software, Catalyst 4500 L3 Switch  Software (cat4500es8-UNIVERSALK9-M), Version 03.09.00.E RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2016 by Cisco Systems, Inc.
Compiled Tue 19

          advertisement version: 2
VTP Management Domain: 'vtp-522wpav'
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 172.20.84.27

-------------------------
Device ID: sx1-522wpav-w1665-clinical.net.utah.edu
Entry address(es): 
  IP address: 172.20.84.9
Platform: cisco WS-C4510R+E,  Capabilities: Switch IGMP 
Interface: TenGigabitEthernet1/0/5,  Port ID (outgoing port): TenGigabitEthernet5/1
Holdtime : 150 sec

Version :
Cisco IOS Software, IOS-XE Software, Catalyst 4500 L3 Switch  Software (cat4500es8-UNIVERSALK9-M), Version 03.09.00.E RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2016 by Cisco Systems, Inc.
Compiled Tue 19-Jul-16 12:34 by prod_rel_team

advertisement version: 2
VTP Management Domain: 'vtp-522wpav'
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 172.20.84.9

-------------------------
Device ID: r1-clinical-b244.net.utah.edu(JPG22480005)
Entry address(es): 
  IP address: 10.104.216.2
Platform: N77-C7710,  Capabilities: Router Switch IGMP CVTA phone port 
Interface: TenGigabitEthernet1/0/1,  Port ID (outgoing port): Ethernet1/9
Holdtime : 127 sec

Version :
Cisco Nexus Operating System (NX-OS) Software, Version 8.2(2)

advertisement version: 2
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 172.29.1.16

-------------------------
Device ID: sx1-522wpav-w4240-clinical.net.utah.edu
Entry address(es): 
  IP address: 172.20.84.35
Platform: cisco WS-C4510R+E,  Capabilities: Switch IGMP 
Interface: TenGigabitEthernet1/0/11,  Port ID (outgoing port): TenGigabitEthernet5/1
Holdtime : 149 sec

Version :
Cisco IOS Software, IOS-XE Software, Catalyst 4500 L3 Switch  Software (cat4500es8-UNIVERSALK9-M), Version 03.09.00.E RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2016 by Cisco Systems, Inc.
          Compiled Tue 19-Jul-16 12:34 by prod_rel_team

advertisement version: 2
VTP Management Domain: 'vtp-522wpav'
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 172.20.84.35

-------------------------
Device ID: sx1-522wpavilion-5.net.utah.edu
Entry address(es): 
  IP address: 172.20.84.16
Platform: cisco WS-C4510R+E,  Capabilities: Switch IGMP 
Interface: TenGigabitEthernet1/0/13,  Port ID (outgoing port): TenGigabitEthernet5/1
Holdtime : 176 sec

Version :
Cisco IOS Software, Catalyst 4500 L3 Switch  Software (cat4500es8-UNIVERSALK9-M), Version 15.2(3)E, RELEASE SOFTWARE (fc4)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2014 by Cisco Systems, Inc.
Compiled Sun 07-Dec-14 17:59 by prod_rel_team

advertisement version: 2
VTP Management Domain: '522wpavilion'
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 172.20.84.16

-------------------------
Device ID: dx2-522wpav-w5260-clinical.net.utah.edu
Entry address(es): 
  IP address: 172.20.84.6
Platform: cisco WS-C3850-24XS,  Capabilities: Switch IGMP 
Interface: TenGigabitEthernet1/0/23,  Port ID (outgoing port): TenGigabitEthernet1/0/23
Holdtime : 149 sec

Version :
Cisco IOS Software, IOS-XE Software, Catalyst L3 Switch Software (CAT3K_CAA-UNIVERSALK9-M), Version 03.07.04E RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2016 by Cisco Systems, Inc.
Compiled Thu 19-May-16 11:48 by prod_rel_team

advertisement version: 2
VTP Management Domain: 'vtp-522wpav'
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 172.20.84.6

-------------------------
Device ID: dx2-522wpav-w5260-clinical.net.utah.edu
Entry address(es): 
  IP address: 172.20.84.6
Platform: cisco WS-C3850-24XS,  Capabilities: Switch IGMP 
Interface: TenGigabitEthernet1/0/2,  Port ID (outgoing port): TenGigabitEthernet1/0/2
          Holdtime : 147 sec

Version :
Cisco IOS Software, IOS-XE Software, Catalyst L3 Switch Software (CAT3K_CAA-UNIVERSALK9-M), Version 03.07.04E RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2016 by Cisco Systems, Inc.
Compiled Thu 19-May-16 11:48 by prod_rel_team

advertisement version: 2
VTP Management Domain: 'vtp-522wpav'
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 172.20.84.6


Total cdp entries displayed : 12""",
 'show module all':"""^
% Invalid input detected at '^' marker.
""",
 'show module':"""Switch  Ports    Model                Serial No.   MAC address     Hw Ver.       Sw Ver. 
------  -----   ---------             -----------  --------------  -------       --------
 1       34     WS-C3850-24XS-S       FOC2046U22R  08cc.a75a.9880  V02           03.07.04E   """,
 'show run | section snmp':"""snmp-server group CliNOCGrv3RO v3 priv read CliNOCViewRO access 70
snmp-server group CliNOCGrv3RO v3 auth context vlan- match prefix 
snmp-server group CliNOCGrv3RW v3 priv write CliNOCViewRW access 71
snmp-server view CliNOCViewRO internet included
snmp-server view CliNOCViewRW internet included
snmp-server location Bldg. 522 Room wm320
snmp-server contact BC-507881 Y-319847
snmp ifmib ifindex persist""",
 'show run | in snmp':"""snmp-server group CliNOCGrv3RO v3 priv read CliNOCViewRO access 70
snmp-server group CliNOCGrv3RO v3 auth context vlan- match prefix 
snmp-server group CliNOCGrv3RW v3 priv write CliNOCViewRW access 71
snmp-server view CliNOCViewRO internet included
snmp-server view CliNOCViewRW internet included
snmp-server location Bldg. 522 Room wm320
snmp-server contact BC-507881 Y-319847
snmp ifmib ifindex persist""",
 'show snmp user':"""User name: CliNONUserv3RO
Engine ID: 80000009030008CCA75A9880
storage-type: nonvolatile	 active
Authentication Protocol: MD5
Privacy Protocol: DES
Group-name: CliNOCGrv3RO

User name: CliNONUserv3Rw
Engine ID: 80000009030008CCA75A9880
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
    150 permit 10.71.24.17 (4366075 matches)
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
    90 permit tcp 155.99.254.128 0.0.0.127 any eq 22 (6 matches)
    100 permit tcp 155.98.164.192 0.0.0.31 any eq 22 (10 matches)
    110 permit tcp host 10.71.24.11 any eq 22
    120 permit tcp host 10.71.24.12 any eq 22
    130 permit tcp host 10.71.24.13 any eq 22
    140 permit tcp host 10.71.24.14 any eq 22
    150 permit tcp host 10.71.24.15 any eq 22
    160 permit tcp host 10.71.24.16 any eq 22
    170 permit tcp host 10.71.24.17 any eq 22 (88 matches)
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
logging source-interface Vlan651
logging host 10.71.24.11
logging host 172.24.29.14
logging host 155.98.253.244""",
 'show run | in logging':"""logging buffered notifications
logging console critical
hw-switch switch 1 logging onboard message level 3
logging facility local6
logging source-interface Vlan651
logging host 10.71.24.11
logging host 172.24.29.14
logging host 155.98.253.244""",
 'show mac address-table':"""Mac Address Table
-------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
 All    0100.0ccc.cccc    STATIC      CPU
 All    0100.0ccc.cccd    STATIC      CPU
 All    0100.0ccc.ccce    STATIC      CPU
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
   1    002f.5cfd.d450    DYNAMIC     Po30
   1    003a.9c40.0dc1    DYNAMIC     Po30
   1    006b.f18d.2940    DYNAMIC     Te1/0/11
   1    006b.f18d.29c0    DYNAMIC     Te1/0/9
   1    00d7.8f0d.7880    DYNAMIC     Te1/0/7
   1    00de.fbd2.acc1    DYNAMIC     Po30
   1    08cc.a75a.a482    DYNAMIC     Po10
   1    08cc.a75a.a497    DYNAMIC     Po10
   1    34f8.e7a5.793c    DYNAMIC     Po30
   1    5897.bd35.8d40    DYNAMIC     Te1/0/13
   1    7018.a733.1935    DYNAMIC     Te1/0/10
   1    a0e0.af58.ccc0    DYNAMIC     Te1/0/5
 651    0000.0c9f.f28b    DYNAMIC     Po30
 651    0026.f20a.0000    DYNAMIC     Po30
 651    003a.9c3f.d7c1    DYNAMIC     Po30
 651    003a.9c40.0dc1    DYNAMIC     Po30
 651    00c0.b7f1.1f6a    DYNAMIC     Po30
 651    08cc.a75a.98c4    STATIC      Vl651 
 269    0000.0c9f.f10d    DYNAMIC     Po30
 269    0026.f20a.0000    DYNAMIC     Po30
 269    003a.9c3f.d7c1    DYNAMIC     Po30
 273    0000.0c9f.f111    DYNAMIC     Po30
 273    0026.f20a.0000    DYNAMIC     Po30
 273    003a.9c3f.d7c1    DYNAMIC     Po30
 273    0040.5805.ec9d    DYNAMIC     Po30
 273    0040.5809.3df3    DYNAMIC     Po30
 273    0040.580b.2e35    DYNAMIC     Po30
 273    0040.580d.ca2a    DYNAMIC     Po30
 273    0040.580d.cf33    DYNAMIC     Po30
 273    0040.580d.d07f    DYNAMIC     Po30
 273    0040.580e.4c26    DYNAMIC     Po30
 273    0040.580e.ee66    DYNAMIC     Po30
           273    0040.580f.275a    DYNAMIC     Po30
 452    0000.0c9f.f1c4    DYNAMIC     Po30
 452    0026.f20a.0000    DYNAMIC     Po30
 452    003a.9c3f.d7c1    DYNAMIC     Po30
 467    0000.0c9f.f1d3    DYNAMIC     Po30
 467    0026.f20a.0000    DYNAMIC     Po30
 467    003a.9c3f.d7c1    DYNAMIC     Po30
 550    0000.0c9f.f226    DYNAMIC     Po30
 550    0026.f20a.0000    DYNAMIC     Po30
 550    003a.9c3f.d7c1    DYNAMIC     Po30
 603    0000.0c9f.f25b    DYNAMIC     Po30
 603    0026.f20a.0000    DYNAMIC     Po30
 603    003a.9c3f.d7c1    DYNAMIC     Po30
 603    003a.9c40.0dc1    DYNAMIC     Po30
 603    a4bb.6d77.4734    DYNAMIC     Po30
 606    0000.0c9f.f25e    DYNAMIC     Po30
 606    0026.f20a.0000    DYNAMIC     Po30
 606    003a.9c3f.d7c1    DYNAMIC     Po30
 606    0050.f900.7e18    DYNAMIC     Po30
 625    0000.0c9f.f271    DYNAMIC     Po30
 625    0026.f20a.0000    DYNAMIC     Po30
 625    003a.9c3f.d7c1    DYNAMIC     Po30
 628    0000.0c9f.f274    DYNAMIC     Po30
 628    0026.f20a.0000    DYNAMIC     Po30
 628    003a.9c3f.d7c1    DYNAMIC     Po30
 628    003a.9c40.0dc1    DYNAMIC     Po30
 628    1060.4b83.7c0b    DYNAMIC     Po30
 628    1060.4b85.d5d6    DYNAMIC     Po30
 628    1860.24b1.1394    DYNAMIC     Po30
 628    480f.cf30.80e1    DYNAMIC     Po30
 628    480f.cf45.0c95    DYNAMIC     Po30
 628    5065.f348.0b05    DYNAMIC     Po30
 628    6451.064c.61a5    DYNAMIC     Po30
 628    6c3b.e51b.5eeb    DYNAMIC     Po30
 628    6c3b.e520.0615    DYNAMIC     Po30
 628    6c3b.e520.464c    DYNAMIC     Po30
 628    90b1.1c79.0477    DYNAMIC     Po30
 628    90b1.1c79.1180    DYNAMIC     Po30
 628    90b1.1c79.67be    DYNAMIC     Po30
 628    90b1.1c82.08d4    DYNAMIC     Po30
 628    90b1.1c8c.6b3d    DYNAMIC     Po30
 628    90b1.1c8c.9845    DYNAMIC     Po30
 628    a048.1c92.7f0f    DYNAMIC     Po30
 628    c8f7.50f8.c741    DYNAMIC     Po30
 628    ec8e.b579.8e3d    DYNAMIC     Po30
 628    ec8e.b579.8e95    DYNAMIC     Po30
 628    f092.1cf6.9e19    DYNAMIC     Po30
 647    0000.0c9f.f287    DYNAMIC     Po30
 647    000c.c601.b838    DYNAMIC     Po30
 647    001d.9722.01f5    DYNAMIC     Po30
 647    0020.4afa.c127    DYNAMIC     Po30
 647    0020.4afb.fea0    DYNAMIC     Po30
 647    0025.90e6.f0de    DYNAMIC     Po30
 647    0025.90e7.126c    DYNAMIC     Po30
 647    0026.f20a.0000    DYNAMIC     Po30
 647    003a.9c3f.d7c1    DYNAMIC     Po30
 647    003a.9c40.0dc1    DYNAMIC     Po30
 647    0cc4.7a4f.7caa    DYNAMIC     Po30
 647    1062.e515.e7da    DYNAMIC     Po30
           647    10e7.c600.d39e    DYNAMIC     Po30
 647    10e7.c600.d3a7    DYNAMIC     Po30
 647    10e7.c60c.38a9    DYNAMIC     Po30
 647    10e7.c60c.38ab    DYNAMIC     Po30
 647    1860.2421.a038    DYNAMIC     Po30
 647    1860.246d.a272    DYNAMIC     Po30
 647    3005.5cfc.720a    DYNAMIC     Po30
 647    54bf.648f.5956    DYNAMIC     Po30
 647    68ab.8a82.6570    DYNAMIC     Po30
 647    6c2b.59c9.7c3b    DYNAMIC     Po30
 647    6c2b.59c9.b3e5    DYNAMIC     Po30
 647    6c2b.59ef.1933    DYNAMIC     Po30
 647    6c2b.59f1.2597    DYNAMIC     Po30
 647    a0dd.e5fc.7d19    DYNAMIC     Po30
 647    a4bb.6d77.9c65    DYNAMIC     Po30
 647    a4bb.6d77.c5d5    DYNAMIC     Po30
 647    ace2.d304.50ba    DYNAMIC     Po30
 647    ace2.d304.50c5    DYNAMIC     Po30
 647    ace2.d312.a04b    DYNAMIC     Po30
 647    e4b9.7af4.b4ae    DYNAMIC     Po30
 648    0000.0c9f.f288    DYNAMIC     Po30
 648    000c.c601.b816    DYNAMIC     Po30
 648    001d.9722.01f7    DYNAMIC     Po30
 648    001d.9722.0374    DYNAMIC     Po30
 648    0026.f20a.0000    DYNAMIC     Po30
 648    003a.9c3f.d7c1    DYNAMIC     Po30
 648    003a.9c40.0dc1    DYNAMIC     Po30
 648    1062.e517.c70e    DYNAMIC     Po30
 648    1062.e517.eefb    DYNAMIC     Po30
 648    1062.e567.9771    DYNAMIC     Po30
 648    10e7.c606.12d5    DYNAMIC     Po30
 648    10e7.c60c.38dc    DYNAMIC     Po30
 648    10e7.c60c.3912    DYNAMIC     Po30
 648    10e7.c60c.391d    DYNAMIC     Po30
 648    10e7.c610.c5e4    DYNAMIC     Po30
 648    1860.246d.a04f    DYNAMIC     Po30
 648    3448.ed2b.1760    DYNAMIC     Po30
 648    3448.ede2.a76d    DYNAMIC     Po30
 648    34f6.2d9a.d2b6    DYNAMIC     Po30
 648    480f.cf32.613a    DYNAMIC     Po30
 648    480f.cfc8.5cd3    DYNAMIC     Po30
 648    5065.f340.0d04    DYNAMIC     Po30
 648    5065.f350.2f44    DYNAMIC     Po30
 648    68ab.8a82.97fa    DYNAMIC     Po30
 648    6c2b.59c9.b542    DYNAMIC     Po30
 648    6c2b.59d5.1c24    DYNAMIC     Po30
 648    6c2b.59d5.35dd    DYNAMIC     Po30
 648    6c2b.59d5.380c    DYNAMIC     Po30
 648    6c2b.59d5.3ea0    DYNAMIC     Po30
 648    6c2b.59d5.3fb0    DYNAMIC     Po30
 648    6c2b.59d6.6a79    DYNAMIC     Po30
 648    6c2b.59d6.6f7d    DYNAMIC     Po30
 648    6c2b.59d6.d27a    DYNAMIC     Po30
 648    781c.5af2.7220    DYNAMIC     Po30
 648    9cc7.d129.6c05    DYNAMIC     Po30
 648    a08c.fdd2.7041    DYNAMIC     Po30
 648    a0b3.cc9d.250f    DYNAMIC     Po30
 648    a4bb.6d4d.4aae    DYNAMIC     Po30
 648    a4bb.6d77.c21b    DYNAMIC     Po30
           648    a4bb.6dcf.9444    DYNAMIC     Po30
 648    ace2.d302.9339    DYNAMIC     Po30
 648    ace2.d303.d11c    DYNAMIC     Po30
 648    ace2.d306.cbd1    DYNAMIC     Po30
 648    ace2.d30f.8cc2    DYNAMIC     Po30
 648    c8d9.d294.5c02    DYNAMIC     Po30
 648    c8d9.d294.604a    DYNAMIC     Po30
 648    c8f7.50fe.79cb    DYNAMIC     Po30
 648    dc4a.3e7f.b4cc    DYNAMIC     Po30
 648    dc4a.3e93.6796    DYNAMIC     Po30
 648    e454.e85c.e7aa    DYNAMIC     Po30
 648    e454.e876.fc17    DYNAMIC     Po30
 648    e454.e897.19f8    DYNAMIC     Po30
 648    e454.e897.1a43    DYNAMIC     Po30
 648    e4b9.7af9.d621    DYNAMIC     Po30
 648    fc3f.db0f.7f9b    DYNAMIC     Po30
 649    0000.0c9f.f289    DYNAMIC     Po30
 649    0007.3279.0c54    DYNAMIC     Po30
 649    000c.29c3.1a3a    DYNAMIC     Po30
 649    000c.29f5.0158    DYNAMIC     Po30
 649    001d.9722.01e3    DYNAMIC     Po30
 649    001d.9722.0351    DYNAMIC     Po30
 649    0026.f20a.0000    DYNAMIC     Po30
 649    003a.9c3f.d7c1    DYNAMIC     Po30
 649    003a.9c40.0dc1    DYNAMIC     Po30
 649    004e.019b.b74e    DYNAMIC     Po30
 649    0050.c2b1.b272    DYNAMIC     Po30
 649    0050.c2b1.b813    DYNAMIC     Po30
 649    00c0.eb10.f6f8    DYNAMIC     Po30
 649    00c0.eb10.f700    DYNAMIC     Po30
 649    00ee.ab3f.73d8    DYNAMIC     Po30
 649    1062.e51b.8713    DYNAMIC     Po30
 649    10e7.c60c.398f    DYNAMIC     Po30
 649    10e7.c610.c55c    DYNAMIC     Po30
 649    10e7.c610.c5d5    DYNAMIC     Po30
 649    1803.73db.3726    DYNAMIC     Po30
 649    1803.73db.3727    DYNAMIC     Po30
 649    1860.2421.9e30    DYNAMIC     Po30
 649    1860.2421.9fbc    DYNAMIC     Po30
 649    1860.2421.a08d    DYNAMIC     Po30
 649    1860.2421.a091    DYNAMIC     Po30
 649    1860.2484.1592    DYNAMIC     Po30
 649    1860.2498.a265    DYNAMIC     Po30
 649    2067.7cdb.2ae6    DYNAMIC     Po30
 649    2426.4206.b89d    DYNAMIC     Po30
 649    2426.421e.ac44    DYNAMIC     Po30
 649    3814.2893.b10e    DYNAMIC     Po30
 649    480f.cf42.2ace    DYNAMIC     Po30
 649    5065.f33f.1405    DYNAMIC     Po30
 649    5882.a894.d356    DYNAMIC     Po30
 649    6879.ed74.855a    DYNAMIC     Po30
 649    6c2b.59c9.865a    DYNAMIC     Po30
 649    6c2b.59c9.b1bb    DYNAMIC     Po30
 649    6c2b.59c9.b1fd    DYNAMIC     Po30
 649    6c2b.59c9.b453    DYNAMIC     Po30
 649    6c2b.59cc.9d16    DYNAMIC     Po30
 649    6c2b.59cc.cb9e    DYNAMIC     Po30
 649    6c2b.59d2.fab8    DYNAMIC     Po30
 649    6c2b.59d3.db86    DYNAMIC     Po30
           649    6c2b.59d5.196e    DYNAMIC     Po30
 649    705a.0f48.b7c7    DYNAMIC     Po30
 649    8c04.ba5a.d88e    DYNAMIC     Po30
 649    8cae.4cea.e7e0    DYNAMIC     Po30
 649    8cec.4bb0.ead3    DYNAMIC     Po30
 649    9457.a5bc.041b    DYNAMIC     Po30
 649    98e7.43d5.69f8    DYNAMIC     Po30
 649    98e7.43e6.9c59    DYNAMIC     Po30
 649    a08c.fdd1.ac61    DYNAMIC     Po30
 649    a08c.fdd1.af41    DYNAMIC     Po30
 649    a08c.fde6.f4c1    DYNAMIC     Po30
 649    a4bb.6d4d.1025    DYNAMIC     Po30
 649    a4bb.6d4d.dd2d    DYNAMIC     Po30
 649    a4bb.6d77.9d08    DYNAMIC     Po30
 649    a4bb.6d7a.77bf    DYNAMIC     Po30
 649    a4bb.6d7f.ab41    DYNAMIC     Po30
 649    a4bb.6d80.3c34    DYNAMIC     Po30
 649    a4bb.6d80.7b9d    DYNAMIC     Po30
 649    a4bb.6d9c.8bdb    DYNAMIC     Po30
 649    a4bb.6dcf.8106    DYNAMIC     Po30
 649    a4bb.6ddb.d34a    DYNAMIC     Po30
 649    ace2.d301.6973    DYNAMIC     Po30
 649    ace2.d312.4257    DYNAMIC     Po30
 649    ace2.d314.31e9    DYNAMIC     Po30
 649    b8ac.6fb0.a69b    DYNAMIC     Po30
 649    c8d3.ffa4.1ca3    DYNAMIC     Po30
 649    c8f7.50db.c19d    DYNAMIC     Po30
 649    c8f7.50f8.cbac    DYNAMIC     Po30
 649    dc4a.3e7d.bfad    DYNAMIC     Po30
 649    dc4a.3e7e.4629    DYNAMIC     Po30
 649    dc4a.3e84.ff58    DYNAMIC     Po30
 649    dc4a.3e93.6772    DYNAMIC     Po30
 649    dc4a.3e93.683a    DYNAMIC     Po30
 649    e454.e858.a9e0    DYNAMIC     Po30
 649    e454.e85c.dadf    DYNAMIC     Po30
 649    e454.e85d.08a9    DYNAMIC     Po30
 649    e454.e85d.4434    DYNAMIC     Po30
 649    e454.e85d.8a2c    DYNAMIC     Po30
 649    e454.e862.a894    DYNAMIC     Po30
 649    e454.e86d.07d0    DYNAMIC     Po30
 649    e454.e878.47c1    DYNAMIC     Po30
 649    e454.e894.7dab    DYNAMIC     Po30
 649    e454.e895.77d5    DYNAMIC     Po30
 649    e454.e895.8582    DYNAMIC     Po30
 649    e4b9.7af4.af6d    DYNAMIC     Po30
 649    e4b9.7af9.b5a1    DYNAMIC     Po30
 649    e4b9.7af9.b8a8    DYNAMIC     Po30
 649    e4b9.7afb.2345    DYNAMIC     Po30
 649    ecb1.d7f9.da45    DYNAMIC     Po30
 649    f092.1cef.37de    DYNAMIC     Po30
 650    0000.0c9f.f28a    DYNAMIC     Po30
 650    0007.4d41.b062    DYNAMIC     Po30
 650    0007.4d43.2af4    DYNAMIC     Po30
 650    0007.4d47.2601    DYNAMIC     Po30
 650    0007.4d4b.b600    DYNAMIC     Po30
 650    0007.4d65.b6dc    DYNAMIC     Po30
 650    000e.7fe0.2ae7    DYNAMIC     Po30
 650    000e.7fe8.f1c5    DYNAMIC     Po30
 650    0011.85fa.fe52    DYNAMIC     Po30
           650    0011.85fc.a048    DYNAMIC     Po30
 650    001b.78e7.f2e4    DYNAMIC     Po30
 650    001b.8232.47fa    DYNAMIC     Po30
 650    001b.8232.892b    DYNAMIC     Po30
 650    001b.8232.8a06    DYNAMIC     Po30
 650    001b.8232.8a1d    DYNAMIC     Po30
 650    001b.8232.cacb    DYNAMIC     Po30
 650    001e.0b17.5b9e    DYNAMIC     Po30
 650    0021.5a81.31e9    DYNAMIC     Po30
 650    0021.5a88.2874    DYNAMIC     Po30
 650    0021.5a98.9f3e    DYNAMIC     Po30
 650    0021.5a98.9f6d    DYNAMIC     Po30
 650    0021.5a98.9f80    DYNAMIC     Po30
 650    0021.5a99.2859    DYNAMIC     Po30
 650    0021.5a99.8729    DYNAMIC     Po30
 650    0021.5a99.8736    DYNAMIC     Po30
 650    0021.5a99.87f9    DYNAMIC     Po30
 650    0025.b3f8.b4b4    DYNAMIC     Po30
 650    0026.f20a.0000    DYNAMIC     Po30
 650    003a.9c3f.d7c1    DYNAMIC     Po30
 650    003a.9c40.0dc1    DYNAMIC     Po30
 650    101f.7448.652d    DYNAMIC     Po30
 650    1458.d03d.4f73    DYNAMIC     Po30
 650    1cc1.de10.1888    DYNAMIC     Po30
 650    2426.4206.f55c    DYNAMIC     Po30
 650    2426.4235.23f7    DYNAMIC     Po30
 650    2426.4235.51b3    DYNAMIC     Po30
 650    2426.4260.def8    DYNAMIC     Po30
 650    24be.05ed.22f4    DYNAMIC     Po30
 650    2c44.fd06.963e    DYNAMIC     Po30
 650    2c59.e5d4.cea1    DYNAMIC     Po30
 650    30e1.713c.9016    DYNAMIC     Po30
 650    30e1.71bb.53b0    DYNAMIC     Po30
 650    3464.a969.fc89    DYNAMIC     Po30
 650    34f6.2db6.21ea    DYNAMIC     Po30
 650    3ca8.2a06.e221    DYNAMIC     Po30
 650    3ca8.2a07.f68f    DYNAMIC     Po30
 650    3ca8.2af7.a23a    DYNAMIC     Po30
 650    3ca8.2af8.0f81    DYNAMIC     Po30
 650    3ca8.2af8.4570    DYNAMIC     Po30
 650    3ca8.2af8.fee9    DYNAMIC     Po30
 650    3ca8.2af9.7d62    DYNAMIC     Po30
 650    3ca8.2af9.7dad    DYNAMIC     Po30
 650    3ca8.2afa.b292    DYNAMIC     Po30
 650    3ca8.2afb.73df    DYNAMIC     Po30
 650    3cd9.2b0f.b244    DYNAMIC     Po30
 650    40b0.3423.37c4    DYNAMIC     Po30
 650    40b0.3425.7629    DYNAMIC     Po30
 650    480f.cff9.32c3    DYNAMIC     Po30
 650    48ba.4ede.3327    DYNAMIC     Po30
 650    5820.b14c.b7a3    DYNAMIC     Po30
 650    5820.b14d.5c25    DYNAMIC     Po30
 650    5820.b14d.8976    DYNAMIC     Po30
 650    5cb9.010e.034a    DYNAMIC     Po30
 650    68ab.8a82.0d16    DYNAMIC     Po30
 650    6cc2.1724.3509    DYNAMIC     Po30
 650    6cc2.1729.4fdf    DYNAMIC     Po30
 650    705a.0fa3.7e43    DYNAMIC     Po30
 650    705a.0fa4.d6f6    DYNAMIC     Po30
           650    705a.0fa6.7beb    DYNAMIC     Po30
 650    70ea.1ae3.8c90    DYNAMIC     Po30
 650    78e3.b5f8.90ed    DYNAMIC     Po30
 650    80ce.6258.01f6    DYNAMIC     Po30
 650    8cdc.d45b.02f6    DYNAMIC     Po30
 650    8cdc.d45d.f34e    DYNAMIC     Po30
 650    9457.a514.e6ba    DYNAMIC     Po30
 650    9457.a5cc.10e0    DYNAMIC     Po30
 650    9457.a5ce.19d5    DYNAMIC     Po30
 650    98e7.f408.60da    DYNAMIC     Po30
 650    9c7b.ef82.532c    DYNAMIC     Po30
 650    9c7b.ef82.533b    DYNAMIC     Po30
 650    9cb6.541b.3b32    DYNAMIC     Po30
 650    9cb6.541b.7832    DYNAMIC     Po30
 650    a08c.fd16.adea    DYNAMIC     Po30
 650    a0d3.c180.88ce    DYNAMIC     Po30
 650    a0d3.c1ea.04e8    DYNAMIC     Po30
 650    a0d3.c1ed.a2ee    DYNAMIC     Po30
 650    ace2.d342.71f1    DYNAMIC     Po30
 650    b4b5.2ff3.89d0    DYNAMIC     Po30
 650    b4b5.2ff8.2c55    DYNAMIC     Po30
 650    b4b5.2ff8.dba1    DYNAMIC     Po30
 650    c434.6b18.3891    DYNAMIC     Po30
 650    c434.6b1a.97e7    DYNAMIC     Po30
 650    c465.1642.cb2b    DYNAMIC     Po30
 650    c8d3.ff0c.fca9    DYNAMIC     Po30
 650    c8d3.ff10.b9ac    DYNAMIC     Po30
 650    c8d3.ff10.b9bd    DYNAMIC     Po30
 650    d0bf.9c33.b980    DYNAMIC     Po30
 650    ec8e.b527.4cb2    DYNAMIC     Po30
 650    ec9a.7464.e1ad    DYNAMIC     Po30
 650    f4ce.4636.0146    DYNAMIC     Po30
 650    f4ce.4639.d115    DYNAMIC     Po30
 650    f4ce.4639.f156    DYNAMIC     Po30
 650    f4ce.4649.598a    DYNAMIC     Po30
 650    f8b4.6adf.d7f0    DYNAMIC     Po30
 650    fc15.b42e.8b40    DYNAMIC     Po30
 650    fc15.b476.ad39    DYNAMIC     Po30
 650    fc3f.db50.3c8d    DYNAMIC     Po30
 652    08cc.a75a.a482    DYNAMIC     Po10
 653    0000.0c9f.f28d    DYNAMIC     Po30
 653    0001.f093.481a    DYNAMIC     Po30
 653    0001.f093.48c6    DYNAMIC     Po30
 653    0003.1d09.3266    DYNAMIC     Po30
 653    000b.ab41.29c7    DYNAMIC     Po30
 653    0026.f20a.0000    DYNAMIC     Po30
 653    003a.9c3f.d7c1    DYNAMIC     Po30
 653    003a.9c40.0dc1    DYNAMIC     Po30
 653    c400.ad27.e74f    DYNAMIC     Po30
 668    08cc.a75a.a482    DYNAMIC     Po10
 685    0000.0c9f.f2ad    DYNAMIC     Po30
 685    0004.f2fd.279b    DYNAMIC     Po30
 685    0007.327c.b3d0    DYNAMIC     Po30
 685    0007.327c.b410    DYNAMIC     Po30
 685    0007.327c.b7f2    DYNAMIC     Po30
 685    000c.c601.b096    DYNAMIC     Po30
 685    000c.c601.b114    DYNAMIC     Po30
 685    000c.c601.b824    DYNAMIC     Po30
 685    000c.c601.b87c    DYNAMIC     Po30
           685    000c.c604.51aa    DYNAMIC     Po30
 685    0020.4afb.e428    DYNAMIC     Po30
 685    0020.4afb.e4fd    DYNAMIC     Po30
 685    0020.4afb.f656    DYNAMIC     Po30
 685    0024.dd01.43ba    DYNAMIC     Po30
 685    0026.f20a.0000    DYNAMIC     Po30
 685    003a.9c3f.d7c1    DYNAMIC     Po30
 685    1860.246f.90eb    DYNAMIC     Po30
 685    3c52.8201.fa26    DYNAMIC     Po30
 685    6416.7f75.d92b    DYNAMIC     Po30
 685    6c2b.59c9.b072    DYNAMIC     Po30
 685    6c2b.59d3.dc08    DYNAMIC     Po30
 685    6c2b.59ea.a1cb    DYNAMIC     Po30
 685    6c2b.59ee.df2d    DYNAMIC     Po30
 685    ace2.d301.0fb6    DYNAMIC     Po30
 685    ace2.d30c.1b9c    DYNAMIC     Po30
 685    ecb1.d743.6dff    DYNAMIC     Po30
 685    ecb1.d75c.6086    DYNAMIC     Po30
 686    0000.0c9f.f2ae    DYNAMIC     Po30
 686    0007.327c.b942    DYNAMIC     Po30
 686    0007.327c.b9b0    DYNAMIC     Po30
 686    000c.c601.b21a    DYNAMIC     Po30
 686    000c.c601.b822    DYNAMIC     Po30
 686    000c.c601.b842    DYNAMIC     Po30
 686    000c.c601.b91e    DYNAMIC     Po30
 686    0020.4afb.d456    DYNAMIC     Po30
 686    0020.4afb.e439    DYNAMIC     Po30
 686    0020.4afb.e56e    DYNAMIC     Po30
 686    0020.4afb.f65d    DYNAMIC     Po30
 686    0021.5a98.9f28    DYNAMIC     Po30
 686    0026.f20a.0000    DYNAMIC     Po30
 686    003a.9c3f.d7c1    DYNAMIC     Po30
 686    003a.9c40.0dc1    DYNAMIC     Po30
 686    1062.e515.e69c    DYNAMIC     Po30
 686    1062.e515.e759    DYNAMIC     Po30
 686    1062.e515.e7e1    DYNAMIC     Po30
 686    1062.e51b.86d1    DYNAMIC     Po30
 686    10e7.c606.15bd    DYNAMIC     Po30
 686    10e7.c616.5935    DYNAMIC     Po30
 686    10e7.c641.1f11    DYNAMIC     Po30
 686    1860.246f.90b1    DYNAMIC     Po30
 686    1860.246f.918d    DYNAMIC     Po30
 686    5cb9.0111.bf13    DYNAMIC     Po30
 686    6879.ed74.855b    DYNAMIC     Po30
 686    6c2b.59eb.1898    DYNAMIC     Po30
 686    a08c.fdd1.ac62    DYNAMIC     Po30
 686    a4bb.6d78.344b    DYNAMIC     Po30
 686    ace2.d311.1995    DYNAMIC     Po30
 686    c8f7.50fe.83b5    DYNAMIC     Po30
 686    c8f7.50fe.85db    DYNAMIC     Po30
 686    dc4a.3e89.1364    DYNAMIC     Po30
 686    e454.e84e.7bb7    DYNAMIC     Po30
 686    ec8e.b56e.75f7    DYNAMIC     Po30
 686    ec8e.b56e.79d5    DYNAMIC     Po30
 687    0000.0c9f.f2af    DYNAMIC     Po30
 687    0007.327d.179b    DYNAMIC     Po30
 687    0007.327d.1d0b    DYNAMIC     Po30
 687    000c.c601.b8ee    DYNAMIC     Po30
 687    000c.c601.b8f0    DYNAMIC     Po30
           687    000c.c601.b906    DYNAMIC     Po30
 687    0020.4afa.dc0e    DYNAMIC     Po30
 687    0020.4afa.dcdd    DYNAMIC     Po30
 687    0026.f20a.0000    DYNAMIC     Po30
 687    003a.9c3f.d7c1    DYNAMIC     Po30
 687    003a.9c40.0dc1    DYNAMIC     Po30
 687    10e7.c608.2ae7    DYNAMIC     Po30
 687    10e7.c60c.38a5    DYNAMIC     Po30
 687    10e7.c621.8a98    DYNAMIC     Po30
 687    1860.2426.c31b    DYNAMIC     Po30
 687    1860.246d.9f69    DYNAMIC     Po30
 687    2426.4235.682f    DYNAMIC     Po30
 687    3c52.827b.aec4    DYNAMIC     Po30
 687    480f.cf5c.f783    DYNAMIC     Po30
 687    480f.cf5f.08dd    DYNAMIC     Po30
 687    6c2b.59c9.9028    DYNAMIC     Po30
 687    6c2b.59c9.c6d0    DYNAMIC     Po30
 687    6c2b.59d3.d835    DYNAMIC     Po30
 687    705a.0f32.75b4    DYNAMIC     Po30
 687    8cdc.d43f.c214    DYNAMIC     Po30
 687    ace2.d303.d039    DYNAMIC     Po30
 687    ace2.d30f.8cea    DYNAMIC     Po30
 687    c8d9.d209.61ea    DYNAMIC     Po30
 687    c8d9.d209.6388    DYNAMIC     Po30
 687    dc4a.3e6c.0473    DYNAMIC     Po30
 687    e454.e89b.8f9c    DYNAMIC     Po30
 700    08cc.a75a.a482    DYNAMIC     Po10
 701    0000.0c9f.f2bd    DYNAMIC     Po30
 701    0026.f20a.0000    DYNAMIC     Po30
 701    003a.9c3f.d7c1    DYNAMIC     Po30
 701    003a.9c40.0dc1    DYNAMIC     Po30
 701    0040.9d28.4bf5    DYNAMIC     Po30
 701    0040.9d33.81b7    DYNAMIC     Po30
 842    0000.0c9f.f34a    DYNAMIC     Po30
 842    0026.f20a.0000    DYNAMIC     Po30
 842    003a.9c3f.d7c1    DYNAMIC     Po30
 920    0000.0c9f.f398    DYNAMIC     Po30
 920    0026.f20a.0000    DYNAMIC     Po30
 920    003a.9c3f.d7c1    DYNAMIC     Po30
 992    0000.0c9f.f3e0    DYNAMIC     Po30
 992    0004.f2ff.e9de    DYNAMIC     Po30
 992    0026.f20a.0000    DYNAMIC     Po30
 992    003a.9c3f.d7c1    DYNAMIC     Po30
 992    6416.7f1e.569d    DYNAMIC     Po30
 992    6416.7f29.ef3a    DYNAMIC     Po30
 992    6416.7f38.83c7    DYNAMIC     Po30
 992    6416.7f60.0117    DYNAMIC     Po30
 992    6416.7f60.f33c    DYNAMIC     Po30
 992    6416.7f77.74fd    DYNAMIC     Po30
 993    0000.0c9f.f3e1    DYNAMIC     Po30
 993    0026.f20a.0000    DYNAMIC     Po30
 993    003a.9c3f.d7c1    DYNAMIC     Po30
 994    0000.0c9f.f3e2    DYNAMIC     Po30
 994    0026.f20a.0000    DYNAMIC     Po30
 994    003a.9c3f.d7c1    DYNAMIC     Po30
 995    0000.0c9f.f3e3    DYNAMIC     Po30
 995    0026.f20a.0000    DYNAMIC     Po30
 995    003a.9c3f.d7c1    DYNAMIC     Po30
 996    0000.0c9f.f3e4    DYNAMIC     Po30
           996    0026.f20a.0000    DYNAMIC     Po30
 996    003a.9c3f.d7c1    DYNAMIC     Po30
1033    0000.0c9f.f409    DYNAMIC     Po30
1033    0026.f20a.0000    DYNAMIC     Po30
1033    0027.e388.fc32    DYNAMIC     Po30
1033    003a.9c3f.d7c1    DYNAMIC     Po30
1033    003a.9c40.0dc1    DYNAMIC     Po30
1033    006b.f125.cad4    DYNAMIC     Po30
1033    006b.f125.d368    DYNAMIC     Po30
1033    006b.f125.d4f0    DYNAMIC     Po30
1033    006b.f125.d726    DYNAMIC     Po30
1033    006b.f125.d728    DYNAMIC     Po30
1033    006b.f125.d7b2    DYNAMIC     Po30
1033    006b.f125.d8a0    DYNAMIC     Po30
1033    006b.f19c.bc5c    DYNAMIC     Po30
1033    006b.f1b4.d30c    DYNAMIC     Po30
1033    006b.f1b4.d3ac    DYNAMIC     Po30
1033    006b.f1b4.d3dc    DYNAMIC     Po30
1033    006b.f1e2.11c0    DYNAMIC     Po30
1033    006b.f1f2.d0e4    DYNAMIC     Po30
1033    006b.f1f4.ab28    DYNAMIC     Po30
1033    006b.f1f4.ab2c    DYNAMIC     Po30
1033    006b.f1f4.acdc    DYNAMIC     Po30
1033    006b.f1f4.ace4    DYNAMIC     Po30
1033    0078.8863.2e44    DYNAMIC     Po30
1033    00c1.64d8.6a50    DYNAMIC     Po30
1033    00d7.8f1e.b566    DYNAMIC     Po30
1033    00d7.8f1e.b57e    DYNAMIC     Po30
1033    00d7.8f1e.bbb0    DYNAMIC     Po30
1033    00d7.8fa6.e856    DYNAMIC     Po30
1033    00ee.ab3f.55d0    DYNAMIC     Po30
1033    00ee.ab3f.56f0    DYNAMIC     Po30
1033    00ee.ab3f.5a00    DYNAMIC     Po30
1033    00ee.ab3f.5ae8    DYNAMIC     Po30
1033    00ee.ab3f.5bb8    DYNAMIC     Po30
1033    00ee.ab3f.5bc0    DYNAMIC     Po30
1033    00ee.ab3f.5cb8    DYNAMIC     Po30
1033    00ee.ab3f.5e30    DYNAMIC     Po30
1033    00ee.ab3f.5f78    DYNAMIC     Po30
1033    00ee.ab3f.60b0    DYNAMIC     Po30
1033    00ee.ab3f.6350    DYNAMIC     Po30
1033    00ee.ab3f.6410    DYNAMIC     Po30
1033    00ee.ab3f.7278    DYNAMIC     Po30
1033    00ee.ab3f.73c8    DYNAMIC     Po30
1033    00ee.ab3f.7518    DYNAMIC     Po30
1033    00ee.ab3f.76c0    DYNAMIC     Po30
1033    00ee.ab3f.7800    DYNAMIC     Po30
1033    00ee.ab3f.7838    DYNAMIC     Po30
1033    00ee.ab3f.7840    DYNAMIC     Po30
1033    00ee.ab3f.7850    DYNAMIC     Po30
1033    00ee.ab3f.7890    DYNAMIC     Po30
1033    00ee.ab3f.78b0    DYNAMIC     Po30
1033    00ee.ab3f.78c0    DYNAMIC     Po30
1033    00ee.ab3f.7958    DYNAMIC     Po30
1033    00ee.ab3f.7960    DYNAMIC     Po30
1033    00ee.ab3f.7990    DYNAMIC     Po30
1033    00ee.ab3f.79e0    DYNAMIC     Po30
1033    00ee.ab3f.7a88    DYNAMIC     Po30
1033    00ee.ab3f.7b20    DYNAMIC     Po30
          1033    00ee.ab3f.7bb8    DYNAMIC     Po30
1033    00ee.ab3f.7c30    DYNAMIC     Po30
1033    00ee.ab3f.7c70    DYNAMIC     Po30
1033    00ee.ab3f.7cb0    DYNAMIC     Po30
1033    00ee.ab3f.7d20    DYNAMIC     Po30
1033    00ee.ab3f.7e90    DYNAMIC     Po30
1033    00ee.ab3f.7fc0    DYNAMIC     Po30
1033    00ee.ab3f.7fe0    DYNAMIC     Po30
1033    00ee.ab3f.80a0    DYNAMIC     Po30
1033    00ee.ab3f.80c0    DYNAMIC     Po30
1033    00ee.ab3f.8128    DYNAMIC     Po30
1033    00ee.ab3f.82c8    DYNAMIC     Po30
1033    00ee.ab3f.8460    DYNAMIC     Po30
1033    00ee.ab3f.8650    DYNAMIC     Po30
1033    00fe.c8a1.547c    DYNAMIC     Po30
1033    0462.7384.8374    DYNAMIC     Po30
1033    0462.7385.bd10    DYNAMIC     Po30
1033    3c51.0e3d.efb6    DYNAMIC     Po30
1033    3c51.0e3d.f338    DYNAMIC     Po30
1033    3c51.0e3d.f418    DYNAMIC     Po30
1033    3c51.0efa.688a    DYNAMIC     Po30
1033    3c51.0efa.68c8    DYNAMIC     Po30
1033    70b3.1713.adfa    DYNAMIC     Po30
1033    70b3.1713.adfc    DYNAMIC     Po30
1033    70b3.1713.ae04    DYNAMIC     Po30
1033    70b3.1713.b204    DYNAMIC     Po30
1033    70b3.1713.b28c    DYNAMIC     Po30
1033    70b3.1713.b2a2    DYNAMIC     Po30
1033    70b3.1713.b2b0    DYNAMIC     Po30
1033    70ea.1ae3.7890    DYNAMIC     Po30
1033    70ea.1ae3.7bf0    DYNAMIC     Po30
1033    70ea.1ae3.7e88    DYNAMIC     Po30
1033    70ea.1ae3.8700    DYNAMIC     Po30
1033    70ea.1ae3.8738    DYNAMIC     Po30
1033    70ea.1ae3.87e8    DYNAMIC     Po30
1033    70ea.1ae3.8a70    DYNAMIC     Po30
1033    70ea.1ae3.8ad8    DYNAMIC     Po30
1033    70ea.1ae3.8af8    DYNAMIC     Po30
1033    70ea.1ae3.8b50    DYNAMIC     Po30
1033    70ea.1ae3.8b88    DYNAMIC     Po30
1033    70ea.1ae3.8bc0    DYNAMIC     Po30
1033    70ea.1ae3.8c08    DYNAMIC     Po30
1033    70ea.1ae3.8c18    DYNAMIC     Po30
1033    70ea.1ae3.8c50    DYNAMIC     Po30
1033    70ea.1ae3.8cc0    DYNAMIC     Po30
1033    70ea.1ae3.8d20    DYNAMIC     Po30
1033    70ea.1ae3.8d68    DYNAMIC     Po30
1033    70ea.1ae3.8db0    DYNAMIC     Po30
1033    70ea.1ae3.8ef0    DYNAMIC     Po30
1033    70ea.1ae3.8f28    DYNAMIC     Po30
1033    70ea.1ae3.9020    DYNAMIC     Po30
1033    70ea.1ae3.9478    DYNAMIC     Po30
1033    74a2.e6bd.43a0    DYNAMIC     Po30
1033    74a2.e6be.d04c    DYNAMIC     Po30
1033    78ba.f988.c734    DYNAMIC     Po30
1033    78ba.f988.c7c4    DYNAMIC     Po30
1033    78ba.f989.db60    DYNAMIC     Po30
1033    78ba.f98c.560c    DYNAMIC     Po30
1033    78ba.f98c.64f8    DYNAMIC     Po30
          1033    78ba.f98c.65c0    DYNAMIC     Po30
1033    78ba.f98c.65cc    DYNAMIC     Po30
1033    78ba.f98c.65e8    DYNAMIC     Po30
1033    78ba.f99a.bdf8    DYNAMIC     Po30
1033    78ba.f99d.b12c    DYNAMIC     Po30
1033    84b8.02a6.8db8    DYNAMIC     Po30
1033    84b8.02af.d82c    DYNAMIC     Po30
1033    84b8.02b3.aa30    DYNAMIC     Po30
1033    84b8.02b3.aba8    DYNAMIC     Po30
1033    84b8.02b3.af04    DYNAMIC     Po30
1033    84b8.02b8.3160    DYNAMIC     Po30
1033    881d.fc3f.b244    DYNAMIC     Po30
1033    88f0.3179.b530    DYNAMIC     Po30
1033    a03d.6f02.4f4c    DYNAMIC     Po30
1033    a03d.6f0a.0e28    DYNAMIC     Po30
1033    a0b4.395d.9fd0    DYNAMIC     Po30
1033    a0b4.3978.d5e0    DYNAMIC     Po30
1033    a0b4.3978.d67a    DYNAMIC     Po30
1033    a0b4.3978.d6bc    DYNAMIC     Po30
1033    a0b4.3978.d8ec    DYNAMIC     Po30
1033    a0b4.3978.d94a    DYNAMIC     Po30
1033    a0b4.3987.b2fc    DYNAMIC     Po30
1033    a0b4.3987.c4be    DYNAMIC     Po30
1033    a0b4.3987.c75a    DYNAMIC     Po30
1033    a0b4.3987.c790    DYNAMIC     Po30
1033    a0b4.3987.c7a4    DYNAMIC     Po30
1033    a0b4.3987.c7e8    DYNAMIC     Po30
1033    a0b4.3987.c828    DYNAMIC     Po30
1033    a0b4.398d.7206    DYNAMIC     Po30
1033    a0b4.398d.78aa    DYNAMIC     Po30
1033    a0b4.398d.78b4    DYNAMIC     Po30
1033    a0b4.398d.7ad6    DYNAMIC     Po30
1033    a0b4.39c5.783c    DYNAMIC     Po30
1033    a0b4.39c5.788a    DYNAMIC     Po30
1033    a0b4.39c5.7972    DYNAMIC     Po30
1033    a0b4.39c5.79b2    DYNAMIC     Po30
1033    a0b4.39c5.7af2    DYNAMIC     Po30
1033    a0b4.39c5.7b54    DYNAMIC     Po30
1033    a0b4.39c5.7b88    DYNAMIC     Po30
1033    a46c.2af7.af98    DYNAMIC     Po30
1033    a46c.2af7.aff4    DYNAMIC     Po30
1033    a89d.2164.2c0c    DYNAMIC     Po30
1033    a89d.2164.3078    DYNAMIC     Po30
1033    a89d.216f.bb2c    DYNAMIC     Po30
1033    d4c9.3c2a.09c8    DYNAMIC     Po30
1033    d4c9.3cf7.5610    DYNAMIC     Po30
1033    e4aa.5d77.a988    DYNAMIC     Po30
1033    e4aa.5d9b.2a24    DYNAMIC     Po30
1033    f4db.e6b2.510c    DYNAMIC     Po30
1033    f4db.e6f4.a000    DYNAMIC     Po30
1033    f4db.e6f4.a980    DYNAMIC     Po30
1033    f4db.e6f4.a988    DYNAMIC     Po30
1033    f4db.e6f4.a9b0    DYNAMIC     Po30
1033    f4db.e6f4.a9b8    DYNAMIC     Po30
1033    f4db.e6f4.a9be    DYNAMIC     Po30
1033    f4db.e6f4.aa00    DYNAMIC     Po30
1033    f4db.e6f4.aa40    DYNAMIC     Po30
1033    f4db.e6f4.aa48    DYNAMIC     Po30
1033    f4db.e6f4.aa9a    DYNAMIC     Po30
          1033    f4db.e6f4.bbc6    DYNAMIC     Po30
1033    f4db.e6f4.bbc8    DYNAMIC     Po30
1033    f4db.e6f4.bbd8    DYNAMIC     Po30
1033    f4db.e6f4.bc3e    DYNAMIC     Po30
1033    f4db.e6f4.bc44    DYNAMIC     Po30
1033    f4db.e6f4.bc46    DYNAMIC     Po30
1033    f4db.e6f4.bc5c    DYNAMIC     Po30
1033    f4db.e6f4.bc92    DYNAMIC     Po30
1033    f4db.e6f4.bee6    DYNAMIC     Po30
1033    f4db.e6f4.c18e    DYNAMIC     Po30
1033    f4db.e6f4.c192    DYNAMIC     Po30
1033    f4db.e6f4.c1b2    DYNAMIC     Po30
1033    f4db.e6fd.4656    DYNAMIC     Po30
1033    f4db.e6fd.4676    DYNAMIC     Po30
1033    f4db.e6fd.467e    DYNAMIC     Po30
1033    f4db.e6fd.46a2    DYNAMIC     Po30
1033    f4db.e6fd.46bc    DYNAMIC     Po30
1033    f4db.e6fd.46c2    DYNAMIC     Po30
1033    f4db.e6fd.46c6    DYNAMIC     Po30
1033    f4db.e6fd.46de    DYNAMIC     Po30
1033    f4db.e6fd.46e0    DYNAMIC     Po30
1033    f4db.e6ff.415e    DYNAMIC     Po30
1033    f4db.e6ff.4162    DYNAMIC     Po30
1033    f4db.e6ff.4164    DYNAMIC     Po30
1033    f4db.e6ff.4172    DYNAMIC     Po30
1033    f4db.e6ff.4178    DYNAMIC     Po30
1033    f4db.e6ff.4198    DYNAMIC     Po30
1033    f4db.e6ff.41c4    DYNAMIC     Po30
1033    f4db.e6ff.41cc    DYNAMIC     Po30
1033    f4db.e6ff.41d2    DYNAMIC     Po30
1033    f4db.e6ff.41ea    DYNAMIC     Po30
1033    f4db.e6ff.4230    DYNAMIC     Po30
1033    f4db.e6ff.423e    DYNAMIC     Po30
1033    f4db.e6ff.42aa    DYNAMIC     Po30
1033    f4db.e6ff.52ec    DYNAMIC     Po30
1033    f4db.e6ff.554c    DYNAMIC     Po30
1081    0000.0c9f.f439    DYNAMIC     Po30
1081    0012.4e2d.77fd    DYNAMIC     Te1/0/6
1081    0026.f20a.0000    DYNAMIC     Po30
1081    003a.9c3f.d7c1    DYNAMIC     Po30
1081    003a.9c40.0dc1    DYNAMIC     Po30
1601    0000.0c9f.f641    DYNAMIC     Po30
1601    0026.f20a.0000    DYNAMIC     Po30
1601    003a.9c3f.d7c1    DYNAMIC     Po30
3000    0026.f20a.0000    DYNAMIC     Po30
1025    0000.0c9f.f401    DYNAMIC     Po30
1025    0026.f20a.0000    DYNAMIC     Po30
1025    003a.9c3f.d7c1    DYNAMIC     Po30
1025    1062.e51a.60fa    DYNAMIC     Po30
1025    a4bb.6d78.3cf8    DYNAMIC     Po30
1025    c8f7.50fe.4f1e    DYNAMIC     Po30
1025    c8f7.50fe.beb2    DYNAMIC     Po30
1025    e4b9.7af6.a8b8    DYNAMIC     Po30
1602    0000.0c9f.f642    DYNAMIC     Po30
1602    0026.f20a.0000    DYNAMIC     Po30
1602    003a.9c3f.d7c1    DYNAMIC     Po30
 302    0000.0c9f.f12e    DYNAMIC     Po30
 302    0026.f20a.0000    DYNAMIC     Po30
 302    003a.9c3f.d7c1    DYNAMIC     Po30
          1110    0000.0c9f.f456    DYNAMIC     Po30
1110    0016.2511.d6da    DYNAMIC     Po30
1110    0016.2511.e5c8    DYNAMIC     Po30
1110    0016.2511.e5c9    DYNAMIC     Po30
1110    0016.2511.e5d5    DYNAMIC     Po30
1110    0016.2511.e5df    DYNAMIC     Po30
1110    0026.f20a.0000    DYNAMIC     Po30
1110    003a.9c3f.d7c1    DYNAMIC     Po30
 301    0000.0c9f.f12d    DYNAMIC     Po30
 301    0007.b8e0.5eda    DYNAMIC     Po30
 301    0026.f20a.0000    DYNAMIC     Po30
 301    003a.9c3f.d7c1    DYNAMIC     Po30
 301    08cc.a75a.98e2    STATIC      Vl301 
 731    0000.0c9f.f2db    DYNAMIC     Po30
 731    0026.f20a.0000    DYNAMIC     Po30
 731    003a.9c3f.d7c1    DYNAMIC     Po30
 730    0000.0c9f.f2da    DYNAMIC     Po30
 730    0026.f20a.0000    DYNAMIC     Po30
 730    003a.9c3f.d7c1    DYNAMIC     Po30
 730    2067.7cd6.51d8    DYNAMIC     Po30
 773    0000.0c9f.f305    DYNAMIC     Po30
 773    0026.f20a.0000    DYNAMIC     Po30
 773    003a.9c3f.d7c1    DYNAMIC     Po30
 773    003a.9c40.0dc1    DYNAMIC     Po30
 545    0000.0c9f.f221    DYNAMIC     Po30
 545    0026.f20a.0000    DYNAMIC     Po30
 545    003a.9c3f.d7c1    DYNAMIC     Po30
 545    6c2b.59cc.ba3e    DYNAMIC     Po30
 682    0000.0c9f.f2aa    DYNAMIC     Po30
 682    0026.f20a.0000    DYNAMIC     Po30
 682    003a.9c3f.d7c1    DYNAMIC     Po30
 118    0000.0c9f.f076    DYNAMIC     Po30
 118    0026.f20a.0000    DYNAMIC     Po30
 118    003a.9c3f.d7c1    DYNAMIC     Po30
 118    6c2b.5963.efcd    DYNAMIC     Po30
 119    0000.0c9f.f077    DYNAMIC     Po30
 119    0026.f20a.0000    DYNAMIC     Po30
 119    003a.9c3f.d7c1    DYNAMIC     Po30
 119    6c2b.5944.db07    DYNAMIC     Po30
 119    6c2b.5949.3b95    DYNAMIC     Po30
 119    6c2b.5949.3c5a    DYNAMIC     Po30
 119    6c2b.594c.288d    DYNAMIC     Po30
 119    6c2b.594d.21e5    DYNAMIC     Po30
 119    6c2b.594e.361e    DYNAMIC     Po30
 119    6c2b.5954.0dd8    DYNAMIC     Po30
 119    6c2b.5954.127c    DYNAMIC     Po30
 119    6c2b.5954.12ee    DYNAMIC     Po30
 119    6c2b.5954.2cef    DYNAMIC     Po30
 119    6c2b.5954.2d37    DYNAMIC     Po30
 119    6c2b.5954.2d77    DYNAMIC     Po30
 120    0000.0c9f.f078    DYNAMIC     Po30
 120    0026.f20a.0000    DYNAMIC     Po30
 120    003a.9c3f.d7c1    DYNAMIC     Po30
 120    2cea.7f26.1237    DYNAMIC     Po30
 120    6c2b.5944.cc70    DYNAMIC     Po30
 120    6c2b.5944.ddb4    DYNAMIC     Po30
 120    6c2b.5946.a8a9    DYNAMIC     Po30
 120    6c2b.5947.90c9    DYNAMIC     Po30
 120    6c2b.5947.92d4    DYNAMIC     Po30
           120    6c2b.594c.28aa    DYNAMIC     Po30
 120    6c2b.594c.3ef7    DYNAMIC     Po30
 120    6c2b.594d.24ba    DYNAMIC     Po30
 120    6c2b.5954.0e18    DYNAMIC     Po30
 120    6c2b.5954.0f7d    DYNAMIC     Po30
 120    6c2b.5954.1281    DYNAMIC     Po30
 120    6c2b.5954.1295    DYNAMIC     Po30
 120    6c2b.5954.129f    DYNAMIC     Po30
 120    6c2b.5954.2d41    DYNAMIC     Po30
 120    6c2b.5954.2da1    DYNAMIC     Po30
 120    6c2b.5967.30c4    DYNAMIC     Po30
 120    b07b.253e.1a2d    DYNAMIC     Po30
 120    b07b.253e.deb7    DYNAMIC     Po30
 121    0000.0c9f.f079    DYNAMIC     Po30
 121    0026.f20a.0000    DYNAMIC     Po30
 121    003a.9c3f.d7c1    DYNAMIC     Po30
 121    6c2b.5944.ccad    DYNAMIC     Po30
 121    6c2b.5944.cd07    DYNAMIC     Po30
 121    6c2b.5944.d8af    DYNAMIC     Po30
 121    6c2b.5946.a8d1    DYNAMIC     Po30
 121    6c2b.5946.a8d9    DYNAMIC     Po30
 121    6c2b.5946.a9cc    DYNAMIC     Po30
 121    6c2b.5946.eecc    DYNAMIC     Po30
 121    6c2b.5947.92ca    DYNAMIC     Po30
 121    6c2b.5948.1b2c    DYNAMIC     Po30
 121    6c2b.5949.3ab9    DYNAMIC     Po30
 121    6c2b.5949.3b70    DYNAMIC     Po30
 121    6c2b.594b.c7c6    DYNAMIC     Po30
 121    6c2b.594c.288c    DYNAMIC     Po30
 121    6c2b.594d.2311    DYNAMIC     Po30
 121    6c2b.5953.aee5    DYNAMIC     Po30
 121    6c2b.5954.0dc8    DYNAMIC     Po30
 121    6c2b.5954.0e5b    DYNAMIC     Po30
 121    6c2b.5954.12a7    DYNAMIC     Po30
 121    6c2b.5954.12e4    DYNAMIC     Po30
 121    6c2b.5954.1430    DYNAMIC     Po30
 121    6c2b.5954.1445    DYNAMIC     Po30
 121    6c2b.5973.a03e    DYNAMIC     Po30
 122    0000.0c9f.f07a    DYNAMIC     Po30
 122    0026.f20a.0000    DYNAMIC     Po30
 122    003a.9c3f.d7c1    DYNAMIC     Po30
 122    6c2b.5946.a884    DYNAMIC     Po30
 122    6c2b.5946.ef41    DYNAMIC     Po30
 122    6c2b.5948.1e2a    DYNAMIC     Po30
 122    6c2b.5949.3946    DYNAMIC     Po30
 122    6c2b.5949.398f    DYNAMIC     Po30
 122    6c2b.5949.399c    DYNAMIC     Po30
 122    6c2b.5949.3a0a    DYNAMIC     Po30
 122    6c2b.5949.3ae0    DYNAMIC     Po30
 122    6c2b.5949.3afe    DYNAMIC     Po30
 122    6c2b.594b.c7c5    DYNAMIC     Po30
 122    6c2b.594b.c816    DYNAMIC     Po30
 122    6c2b.594b.c8f8    DYNAMIC     Po30
 122    6c2b.594b.c950    DYNAMIC     Po30
 122    6c2b.594c.28b3    DYNAMIC     Po30
 122    6c2b.594d.221c    DYNAMIC     Po30
 122    6c2b.594d.239b    DYNAMIC     Po30
 122    6c2b.594d.23a0    DYNAMIC     Po30
 122    6c2b.594d.23f7    DYNAMIC     Po30
           122    6c2b.594d.253e    DYNAMIC     Po30
 122    6c2b.5963.f157    DYNAMIC     Po30
 923    0000.0c07.ac37    DYNAMIC     Po30
 923    0000.0c9f.f39b    DYNAMIC     Po30
 923    0026.f20a.0000    DYNAMIC     Po30
 923    003a.9c3f.d7c1    DYNAMIC     Po30
 923    c4c6.03d2.bac1    DYNAMIC     Po30
 703    0000.0c9f.f2bf    DYNAMIC     Po30
 703    0026.f20a.0000    DYNAMIC     Po30
 703    003a.9c3f.d7c1    DYNAMIC     Po30
1042    0000.0c9f.f412    DYNAMIC     Po30
1042    0005.a61a.514c    DYNAMIC     Po30
1042    001d.c112.d6e4    DYNAMIC     Po30
1042    001d.c150.363e    DYNAMIC     Po30
1042    0026.f20a.0000    DYNAMIC     Po30
1042    003a.9c3f.d7c1    DYNAMIC     Po30
1042    94db.5646.0607    DYNAMIC     Po30
1042    b42e.9987.2e4b    DYNAMIC     Po30
1042    d46a.9189.dc3c    DYNAMIC     Po30
1042    d46a.91d5.0046    DYNAMIC     Po30
1061    0000.0c9f.f425    DYNAMIC     Po30
1061    0002.c18a.828e    DYNAMIC     Po30
1061    0002.c18a.8f3f    DYNAMIC     Po30
1061    0002.c18a.a11e    DYNAMIC     Po30
1061    0002.c18a.a72e    DYNAMIC     Po30
1061    0026.f20a.0000    DYNAMIC     Po30
1061    003a.9c3f.d7c1    DYNAMIC     Po30
1061    003a.9c40.0dc1    DYNAMIC     Po30
 201    0000.0c9f.f0c9    DYNAMIC     Po30
 201    0026.f20a.0000    DYNAMIC     Po30
 201    003a.9c3f.d7c1    DYNAMIC     Po30
 201    00a0.a42c.4eb9    DYNAMIC     Po30
 201    00a0.a42c.535e    DYNAMIC     Po30
 201    00a0.a42c.543a    DYNAMIC     Po30
 201    00a0.a42c.7ede    DYNAMIC     Po30
Total Mac Addresses for this criterion: 915""",
 'show run | section tacacs':"""aaa group server tacacs+ default
 server name TAC-DDC
 server name TAC-PARK
aaa group server tacacs+ NOC-TAC
 server name TAC-EBC
 server name TAC-SECONDARY
tacacs server TAC-DDC
 address ipv4 155.97.160.52
 key 7 100D2339061C410F21573F3B65
tacacs server TAC-PARK
 address ipv4 155.98.253.200
 key 7 1551212C072178200560203252
tacacs server TAC-EBC
 address ipv4 172.31.17.180
 key 7 002D57032D1F0E242F23550F
tacacs server TAC-SECONDARY
 address ipv4 10.64.32.5
 key 7 0808084B205D003532091545""",
 'show run | in tacacs':"""aaa group server tacacs+ default
aaa group server tacacs+ NOC-TAC
tacacs server TAC-DDC
tacacs server TAC-PARK
tacacs server TAC-EBC
tacacs server TAC-SECONDARY""",
 'show power inline':"""Module   Available     Used     Remaining
          (Watts)     (Watts)    (Watts) 
------   ---------   --------   ---------
1             n/a        n/a         n/a
Interface Admin  Oper       Power   Device              Class Max
                            (Watts)                            
--------- ------ ---------- ------- ------------------- ----- ----""",
 'show environment all':"""Switch 1 FAN 1 is OK
Switch 1 FAN 2 is OK
Switch 1 FAN 3 is OK
FAN PS-1 is OK
FAN PS-2 is OK
Switch 1: SYSTEM TEMPERATURE is OK
SW  PID                 Serial#     Status           Sys Pwr  PoE Pwr  Watts
--  ------------------  ----------  ---------------  -------  -------  -----
1A  PWR-C1-1100WAC      DTN2039V392  OK              Good     Good     1100
1B  PWR-C1-1100WAC      DTN2039V370  OK              Good     Good     1100
""",
}
