ip_address = '172.20.64.37'
software = 'software'
hardware = 'hardware'
read_results = {
 'show version':"""Cisco IOS XE Software, Version 16.06.04
Cisco IOS Software [Everest], Catalyst L3 Switch Software (CAT9K_IOSXE), Version 16.6.4, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2018 by Cisco Systems, Inc.
Compiled Sun 08-Jul-18 04:21 by mcpre


Cisco IOS-XE software, Copyright (c) 2005-2018 by cisco Systems, Inc.
All rights reserved.  Certain components of Cisco IOS-XE software are
licensed under the GNU General Public License ("GPL") Version 2.0.  The
software code licensed under GPL Version 2.0 is free software that comes
with ABSOLUTELY NO WARRANTY.  You can redistribute and/or modify such
GPL code under the terms of GPL Version 2.0.  For more details, see the
documentation or "License Notice" file accompanying the IOS-XE software,
or the applicable URL provided on the flyer accompanying the IOS-XE
software.


ROM: IOS-XE ROMMON
BOOTLDR: System Bootstrap, Version 16.6.2r[FC1], RELEASE SOFTWARE (P)

sx1-525hosp-1443-clinical uptime is 2 years, 14 weeks, 5 days, 53 minutes
Uptime for this control processor is 2 years, 14 weeks, 5 days, 55 minutes
System returned to ROM by PowerOn
System restarted at 15:23:50 MDT Fri Mar 15 2019
System image file is "bootflash:packages.conf"
Last reload reason: PowerOn



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


Technology Package License Information: 

-----------------------------------------------------------------
Technology-package                   Technology-package
Current             Type             Next reboot  
------------------------------------------------------------------
network-advantage   Permanent        network-advantage
dna-advantage       Subscription     dna-advantage

cisco C9407R (X86) processor (revision V01) with 1916973K/6147K bytes of memory.
Processor board ID FXS2220Q0DD
2 Virtual Ethernet interfaces
192 Gigabit Ethernet interfaces
          8 Ten Gigabit Ethernet interfaces
2 Forty Gigabit Ethernet interfaces
32768K bytes of non-volatile configuration memory.
15958412K bytes of physical memory.
10444800K bytes of Bootflash at bootflash:.
1638400K bytes of Crash Files at crashinfo:.
0K bytes of WebUI ODM Files at webui:.

Configuration register is 0x102
""",
 'show run':"""Building configuration...

Current configuration : 39030 bytes
!
! Last configuration change at 18:07:05 MDT Tue May 4 2021 by u0597604
! NVRAM config last updated at 21:29:55 MDT Sun Jun 20 2021 by noc-orionncm
!
version 16.6
no service pad
service timestamps debug datetime msec localtime
service timestamps log datetime msec localtime
service password-encryption
service compress-config
no platform punt-keepalive disable-kernel-core
!
hostname sx1-525hosp-1443-clinical
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
enable secret 5 $1$oUxa$.zFLZB7TEneCcuiwhD6Kl/
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
software auto-upgrade enable
!
          boot system bootflash:packages.conf
power redundancy-mode redundant n+n
no power supply autoLC shutdown
power supply autoLC priority 1 2 5 6 7
!
!
!
!
no ip source-route
no ip routing
!
ip name-server 172.20.120.20
ip domain name net.utah.edu
!
!
!
ip dhcp snooping
!
!
!
!
!
!
!
vtp domain vtp-525hosp
vtp mode transparent
udld aggressive

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
authentication mac-move permit
!
crypto pki trustpoint TP-self-signed-3661210606
 enrollment selfsigned
 subject-name cn=IOS-Self-Signed-Certificate-3661210606
 revocation-check none
 rsakeypair TP-self-signed-3661210606
!
          !
crypto pki certificate chain TP-self-signed-3661210606
 certificate self-signed 01
  30820330 30820218 A0030201 02020101 300D0609 2A864886 F70D0101 05050030 
  31312F30 2D060355 04031326 494F532D 53656C66 2D536967 6E65642D 43657274 
  69666963 6174652D 33363631 32313036 3036301E 170D3139 30333135 30393139 
  35335A17 0D323030 31303130 30303030 305A3031 312F302D 06035504 03132649 
  4F532D53 656C662D 5369676E 65642D43 65727469 66696361 74652D33 36363132 
  31303630 36308201 22300D06 092A8648 86F70D01 01010500 0382010F 00308201 
  0A028201 0100C913 01E29692 0E024B00 83EB5D17 A56313EA 80AF70BA 27D7E929 
  E6BEF505 EC6DC2FA 87965508 D879C368 60EAD1BF 63D0597D EDAA633C 2DD1FC74 
  489E7759 B21D537B 56186CAA 4A9F1C5B 359D3547 1128AAB6 8BCC24F0 EA0B6017 
  DC4F201E 4A8F5214 2B2AA722 069EBBCE AB68F3CE DDC89583 9A49270D 36ED4CC6 
  7BC296DC 869A2F87 6A042783 EAE6EAC5 B3DAC46B 864B4F6C A121FF37 A23E55B1 
  2DD09D0D 0F74229A EE3B085D 75E85E76 B016FF06 4B07492C 4E2D57B7 4AB23828 
  8D260DFF C48BDBFD C22390A9 8A97F391 D0A21E45 E9E23D54 CFC84BB9 50B81934 
  8F15C298 948E44FC 5C9B5637 E88AA528 40152E43 614EB2F4 6727C4B9 7B681DFB 
  C4BE7988 50A10203 010001A3 53305130 0F060355 1D130101 FF040530 030101FF 
  301F0603 551D2304 18301680 142CFF58 D91DF9A5 901B4BAD 85159B5E 52CFB510 
  78301D06 03551D0E 04160414 2CFF58D9 1DF9A590 1B4BAD85 159B5E52 CFB51078 
  300D0609 2A864886 F70D0101 05050003 82010100 392BD817 E68E6197 89CEAD7A 
  6124AD68 44996DF7 672B1BF2 7A296525 3C58BE16 7B907E24 6B5B32B0 3C41AEF7 
  55390ADC 999A3F71 D0472623 5702D53B 86CA492C 20D86380 912E0AF9 8D9A18EE 
  D947D60B 8AC2E405 985B980D 25BD70ED E4BAA971 99E853A4 A64CC1EC 8F2EFFBC 
  8DFCDEDF 1467A50A 6C7B6C55 36FFEE51 98E50549 AA0AC848 80E825D4 B5A4526E 
  EB60C307 EA508447 753C6190 CDC8914D 0C6A666A 5A77AF2B 3EF60398 3459D901 
  E1F97A96 2C37D64B A2BCE9A3 BFF7B323 837D1B6E 47477905 77B75B71 AB3DD7EE 
  2D3C7DB2 33559260 15521F05 E36612F2 2F5122C7 97AE92BF 329CC56A 1FEA9B76 
  2CC4200A 465EA9C1 C469091F 1524807A 2EB75D30
  	quit
!
!
!
diagnostic bootup level minimal
spanning-tree mode rapid-pvst
spanning-tree extend system-id
no errdisable detect cause gbic-invalid
errdisable recovery cause udld
errdisable recovery cause storm-control
!
!
redundancy
 mode sso
!
!
vlan 125
 name Clin-525Hosp-Floor1W-Zeroclients
!
vlan 332
 name clinical-525hosp-m
!
vlan 341
 name bldg_525_env
!
vlan 396
 name bldg-525-printer
!
vlan 540
 name 525-pacs
          !
vlan 607
 name clin-525-iStar
!
vlan 636
 name 525-lan-1w
!
vlan 681
 name rad
!
vlan 732
 name clinical-525hosp-swisstube
!
vlan 984
 name voip-525-1w
!
vlan 1037
 name 525-wmgmt
!
vlan 1209
 name clinical-0525hosp-ccure
!
vlan 1605
 name clin-bldg525-fm-cam
lldp run
!
!
class-map match-any system-cpp-police-topology-control
  description Topology control
class-map match-any system-cpp-police-sw-forward
  description Sw forwarding, L2 LVX data, LOGGING
class-map match-any system-cpp-default
  description DHCP Snooping, EWLC control, EWCL data 
class-map match-any system-cpp-police-sys-data
  description Learning cache ovfl, Crypto Control, Exception, EGR Exception, NFL SAMPLED DATA, Gold Pkt, RPF Failed
class-map match-any system-cpp-police-punt-webauth
  description Punt Webauth
class-map match-any system-cpp-police-l2lvx-control
  description L2 LVX control packets
class-map match-any system-cpp-police-forus
  description Forus Address resolution and Forus traffic
class-map match-any system-cpp-police-multicast-end-station
  description MCAST END STATION
class-map match-any system-cpp-police-multicast
  description Transit Traffic and MCAST Data
class-map match-any system-cpp-police-l2-control
  description L2 control
class-map match-any system-cpp-police-dot1x-auth
  description DOT1X Auth
class-map match-any system-cpp-police-data
  description ICMP redirect, ICMP_GEN and BROADCAST
class-map match-any system-cpp-police-stackwise-virt-control
  description Stackwise Virtual
class-map match-any non-client-nrt-class
class-map match-any system-cpp-police-routing-control
  description Routing control
class-map match-any system-cpp-police-protocol-snooping
  description Protocol snooping
class-map match-any system-cpp-police-system-critical
            description System Critical
!
policy-map system-cpp-policy
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
 description #temp uplink
 switchport access vlan 636
 switchport mode trunk
 switchport voice vlan 984
 spanning-tree portfast
 ip dhcp snooping trust
!
interface GigabitEthernet1/0/2
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet1/0/3
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet1/0/4
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet1/0/5
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet1/0/6
 switchport access vlan 636
 switchport mode access
           switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet1/0/7
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet1/0/8
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet1/0/9
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet1/0/10
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet1/0/11
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet1/0/12
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet1/0/13
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet1/0/14
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet1/0/15
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet1/0/16
 switchport access vlan 636
           switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet1/0/17
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet1/0/18
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet1/0/19
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet1/0/20
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet1/0/21
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet1/0/22
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet1/0/23
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet1/0/24
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet1/0/25
 switchport access vlan 1605
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/26
 switchport access vlan 636
           switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet1/0/27
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet1/0/28
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet1/0/29
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet1/0/30
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet1/0/31
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet1/0/32
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet1/0/33
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet1/0/34
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet1/0/35
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet1/0/36
           switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet1/0/37
 switchport access vlan 636
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/38
 switchport access vlan 636
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/39
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet1/0/40
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet1/0/41
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet1/0/42
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet1/0/43
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet1/0/44
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet1/0/45
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet1/0/46
 switchport access vlan 636
           switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet1/0/47
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet1/0/48
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet2/0/1
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet2/0/2
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet2/0/3
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet2/0/4
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet2/0/5
 switchport access vlan 1605
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet2/0/6
 switchport access vlan 1605
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet2/0/7
 switchport access vlan 1605
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet2/0/8
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet2/0/9
 switchport access vlan 396
 switchport mode access
           spanning-tree portfast
!
interface GigabitEthernet2/0/10
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet2/0/11
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet2/0/12
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet2/0/13
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet2/0/14
 switchport access vlan 396
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet2/0/15
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet2/0/16
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet2/0/17
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet2/0/18
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet2/0/19
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet2/0/20
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet2/0/21
           switchport access vlan 396
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet2/0/22
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet2/0/23
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet2/0/24
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet2/0/25
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet2/0/26
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet2/0/27
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet2/0/28
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet2/0/29
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet2/0/30
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet2/0/31
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet2/0/32
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
!
          interface GigabitEthernet2/0/33
 switchport access vlan 125
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet2/0/34
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet2/0/35
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet2/0/36
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet2/0/37
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet2/0/38
 switchport access vlan 1605
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet2/0/39
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet2/0/40
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet2/0/41
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet2/0/42
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet2/0/43
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet2/0/44
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
          !
interface GigabitEthernet2/0/45
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet2/0/46
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet2/0/47
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet2/0/48
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
!
interface TenGigabitEthernet3/0/1
 description t3/0/1:dx1-525 t2/11
 switchport mode trunk
 ip dhcp snooping trust
!
interface TenGigabitEthernet3/0/2
 description t3/0/2:dx2-525 t4/0/11
 switchport mode trunk
 ip dhcp snooping trust
!
interface TenGigabitEthernet3/0/3
!
interface TenGigabitEthernet3/0/4
!
interface TenGigabitEthernet3/0/5
!
interface TenGigabitEthernet3/0/6
!
interface TenGigabitEthernet3/0/7
!
interface TenGigabitEthernet3/0/8
!
interface FortyGigabitEthernet3/0/9
!
interface FortyGigabitEthernet3/0/10
!
interface GigabitEthernet5/0/1
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet5/0/2
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
          interface GigabitEthernet5/0/3
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet5/0/4
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet5/0/5
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet5/0/6
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet5/0/7
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet5/0/8
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet5/0/9
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet5/0/10
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet5/0/11
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet5/0/12
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
          !
interface GigabitEthernet5/0/13
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet5/0/14
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet5/0/15
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet5/0/16
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet5/0/17
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet5/0/18
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet5/0/19
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet5/0/20
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet5/0/21
 switchport access vlan 125
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet5/0/22
 switchport access vlan 125
 switchport mode access
 switchport voice vlan 984
           spanning-tree portfast
!
interface GigabitEthernet5/0/23
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet5/0/24
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet5/0/25
 description #SwissTubes
 switchport access vlan 732
 switchport mode access
 power inline never
 spanning-tree portfast
!
interface GigabitEthernet5/0/26
 description #SwissTubes
 switchport access vlan 732
 switchport mode access
 power inline never
 spanning-tree portfast
!
interface GigabitEthernet5/0/27
 description #SwissTubes
 switchport access vlan 732
 switchport mode access
 power inline never
 spanning-tree portfast
!
interface GigabitEthernet5/0/28
 description #SwissTubes
 switchport access vlan 732
 switchport mode access
 power inline never
 spanning-tree portfast
!
interface GigabitEthernet5/0/29
 description #SwissTubes
 switchport access vlan 732
 switchport mode access
 power inline never
 spanning-tree portfast
!
interface GigabitEthernet5/0/30
 description #SwissTubes
 switchport access vlan 732
 switchport mode access
 power inline never
 spanning-tree portfast
!
interface GigabitEthernet5/0/31
 description #CCure jack 1283
 switchport access vlan 607
           switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet5/0/32
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet5/0/33
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet5/0/34
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet5/0/35
 switchport access vlan 341
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet5/0/36
 switchport access vlan 341
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet5/0/37
 description #CCure Jack 1285
 switchport access vlan 607
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet5/0/38
 description #AP
 switchport access vlan 1037
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet5/0/39
 description #AP
 switchport access vlan 1037
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet5/0/40
 description #AP
 switchport access vlan 1037
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet5/0/41
 description #AP
 switchport access vlan 1037
 switchport mode access
           spanning-tree portfast
!
interface GigabitEthernet5/0/42
 description #AP
 switchport access vlan 1037
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet5/0/43
 description #AP
 switchport access vlan 1037
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet5/0/44
 description #AP
 switchport access vlan 1037
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet5/0/45
 description #AP
 switchport access vlan 1037
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet5/0/46
 description #AP
 switchport access vlan 1037
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet5/0/47
 description #AP
 switchport access vlan 1037
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet5/0/48
 description #AP
 switchport access vlan 1037
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet6/0/1
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet6/0/2
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet6/0/3
 switchport access vlan 636
 switchport mode access
           switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet6/0/4
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet6/0/5
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet6/0/6
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet6/0/7
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet6/0/8
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet6/0/9
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet6/0/10
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet6/0/11
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet6/0/12
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet6/0/13
 description CCURE
           switchport access vlan 1209
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet6/0/14
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet6/0/15
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet6/0/16
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet6/0/17
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet6/0/18
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet6/0/19
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet6/0/20
 description Wireless AP
 switchport access vlan 1037
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet6/0/21
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet6/0/22
 description Wireless AP
 switchport access vlan 1037
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
          !
interface GigabitEthernet6/0/23
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet6/0/24
 description Wireless AP
 switchport access vlan 1037
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet6/0/25
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet6/0/26
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet6/0/27
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet6/0/28
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet6/0/29
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet6/0/30
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet6/0/31
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet6/0/32
 switchport access vlan 636
 switchport mode access
           switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet6/0/33
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet6/0/34
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet6/0/35
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet6/0/36
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet6/0/37
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet6/0/38
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet6/0/39
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet6/0/40
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet6/0/41
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet6/0/42
 switchport access vlan 636
           switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet6/0/43
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet6/0/44
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet6/0/45
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet6/0/46
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet6/0/47
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface GigabitEthernet6/0/48
 description #UPS
 switchport access vlan 332
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
!
interface Vlan1
 no ip address
 no ip route-cache
 shutdown
!
interface Vlan332
 description clinical-525hosp-m
 ip address 172.20.64.37 255.255.255.0
 no ip route-cache
!
ip default-gateway 172.20.64.1
ip forward-protocol nd
no ip http server
no ip http secure-server
!
ip ssh version 2
!
!
          ip sla enable reaction-alerts
logging facility local6
logging source-interface Vlan332
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
snmp-server group CliNOCGrv3RO v3 priv read CliNOCViewRO access 70
snmp-server group CliNOCGrv3RO v3 auth context vlan- match prefix 
snmp-server group CliNOCGrv3RW v3 priv write CliNOCViewRW access 71
snmp-server view CliNOCViewRO internet included
snmp-server view CliNOCViewRW internet included
snmp-server location Bldg. 525 Room 1443
snmp-server contact BC-509406 Y-334731
snmp-server context vlan-1
snmp-server context vlan-125
snmp-server context vlan-332
snmp-server context vlan-341
snmp-server context vlan-396
snmp-server context vlan-540
snmp-server context vlan-607
snmp-server context vlan-636
snmp-server context vlan-681
snmp-server context vlan-732
snmp-server context vlan-984
snmp-server context vlan-1037
snmp-server context vlan-1209
snmp-server context vlan-1605
snmp ifmib ifindex persist
          tacacs server TAC-EBC
 address ipv4 172.31.17.180
 key 7 09650A0C304112302B0E1D6B
tacacs server TAC-SECONDARY
 address ipv4 10.64.32.5
 key 7 04724F032665496C291B1C56
!
!
!
!
control-plane
 service-policy input system-cpp-policy
!
privilege exec level 1 show configuration
privilege exec level 1 show
banner login ^C
sx1-525hosp-1443-clinical

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
 password 7 046E1F0707230D1D5D
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
!
mac address-table notification mac-move
wsma agent exec
!
wsma agent config
!
wsma agent filesys
          !
wsma agent notify
!
!
end
""",
 'show int status':"""Port      Name               Status       Vlan       Duplex  Speed Type 
Gi1/0/1   #temp uplink       notconnect   636          auto   auto 10/100/1000BaseTX
Gi1/0/2                      notconnect   636          auto   auto 10/100/1000BaseTX
Gi1/0/3                      notconnect   636          auto   auto 10/100/1000BaseTX
Gi1/0/4                      notconnect   636          auto   auto 10/100/1000BaseTX
Gi1/0/5                      notconnect   636          auto   auto 10/100/1000BaseTX
Gi1/0/6                      notconnect   636          auto   auto 10/100/1000BaseTX
Gi1/0/7                      notconnect   636          auto   auto 10/100/1000BaseTX
Gi1/0/8                      notconnect   636          auto   auto 10/100/1000BaseTX
Gi1/0/9                      notconnect   636          auto   auto 10/100/1000BaseTX
Gi1/0/10                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi1/0/11                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi1/0/12                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi1/0/13                     connected    636        a-full a-1000 10/100/1000BaseTX
Gi1/0/14                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi1/0/15                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi1/0/16                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi1/0/17                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi1/0/18                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi1/0/19                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi1/0/20                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi1/0/21                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi1/0/22                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi1/0/23                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi1/0/24                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi1/0/25                     notconnect   1605         auto   auto 10/100/1000BaseTX
Gi1/0/26                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi1/0/27                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi1/0/28                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi1/0/29                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi1/0/30                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi1/0/31                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi1/0/32                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi1/0/33                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi1/0/34                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi1/0/35                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi1/0/36                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi1/0/37                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi1/0/38                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi1/0/39                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi1/0/40                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi1/0/41                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi1/0/42                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi1/0/43                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi1/0/44                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi1/0/45                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi1/0/46                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi1/0/47                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi1/0/48                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi2/0/1                      notconnect   396          auto   auto 10/100/1000BaseTX
Gi2/0/2                      notconnect   396          auto   auto 10/100/1000BaseTX
Gi2/0/3                      notconnect   396          auto   auto 10/100/1000BaseTX
Gi2/0/4                      notconnect   396          auto   auto 10/100/1000BaseTX
Gi2/0/5                      connected    1605       a-full  a-100 10/100/1000BaseTX
Gi2/0/6                      connected    1605       a-full  a-100 10/100/1000BaseTX
Gi2/0/7                      connected    1605       a-full  a-100 10/100/1000BaseTX
Gi2/0/8                      notconnect   396          auto   auto 10/100/1000BaseTX
Gi2/0/9                      notconnect   396          auto   auto 10/100/1000BaseTX
          
Port      Name               Status       Vlan       Duplex  Speed Type 
Gi2/0/10                     notconnect   396          auto   auto 10/100/1000BaseTX
Gi2/0/11                     notconnect   396          auto   auto 10/100/1000BaseTX
Gi2/0/12                     notconnect   396          auto   auto 10/100/1000BaseTX
Gi2/0/13                     notconnect   396          auto   auto 10/100/1000BaseTX
Gi2/0/14                     notconnect   396          auto   auto 10/100/1000BaseTX
Gi2/0/15                     notconnect   396          auto   auto 10/100/1000BaseTX
Gi2/0/16                     notconnect   396          auto   auto 10/100/1000BaseTX
Gi2/0/17                     notconnect   396          auto   auto 10/100/1000BaseTX
Gi2/0/18                     notconnect   396          auto   auto 10/100/1000BaseTX
Gi2/0/19                     notconnect   396          auto   auto 10/100/1000BaseTX
Gi2/0/20                     notconnect   396          auto   auto 10/100/1000BaseTX
Gi2/0/21                     notconnect   396          auto   auto 10/100/1000BaseTX
Gi2/0/22                     notconnect   396          auto   auto 10/100/1000BaseTX
Gi2/0/23                     notconnect   396          auto   auto 10/100/1000BaseTX
Gi2/0/24                     notconnect   396          auto   auto 10/100/1000BaseTX
Gi2/0/25                     notconnect   396          auto   auto 10/100/1000BaseTX
Gi2/0/26                     notconnect   396          auto   auto 10/100/1000BaseTX
Gi2/0/27                     notconnect   396          auto   auto 10/100/1000BaseTX
Gi2/0/28                     notconnect   396          auto   auto 10/100/1000BaseTX
Gi2/0/29                     notconnect   396          auto   auto 10/100/1000BaseTX
Gi2/0/30                     notconnect   396          auto   auto 10/100/1000BaseTX
Gi2/0/31                     notconnect   396          auto   auto 10/100/1000BaseTX
Gi2/0/32                     notconnect   396          auto   auto 10/100/1000BaseTX
Gi2/0/33                     notconnect   125          auto   auto 10/100/1000BaseTX
Gi2/0/34                     notconnect   396          auto   auto 10/100/1000BaseTX
Gi2/0/35                     notconnect   396          auto   auto 10/100/1000BaseTX
Gi2/0/36                     notconnect   396          auto   auto 10/100/1000BaseTX
Gi2/0/37                     notconnect   396          auto   auto 10/100/1000BaseTX
Gi2/0/38                     connected    1605       a-full  a-100 10/100/1000BaseTX
Gi2/0/39                     notconnect   396          auto   auto 10/100/1000BaseTX
Gi2/0/40                     notconnect   396          auto   auto 10/100/1000BaseTX
Gi2/0/41                     notconnect   396          auto   auto 10/100/1000BaseTX
Gi2/0/42                     notconnect   396          auto   auto 10/100/1000BaseTX
Gi2/0/43                     notconnect   396          auto   auto 10/100/1000BaseTX
Gi2/0/44                     notconnect   396          auto   auto 10/100/1000BaseTX
Gi2/0/45                     notconnect   396          auto   auto 10/100/1000BaseTX
Gi2/0/46                     notconnect   396          auto   auto 10/100/1000BaseTX
Gi2/0/47                     notconnect   396          auto   auto 10/100/1000BaseTX
Gi2/0/48                     notconnect   396          auto   auto 10/100/1000BaseTX
Te3/0/1   t3/0/1:dx1-525 t2/ connected    trunk        full    10G SFP-10GBase-SR
Te3/0/2   t3/0/2:dx2-525 t4/ connected    trunk        full    10G SFP-10GBase-SR
Te3/0/3                      notconnect   1            auto  a-10G 
Te3/0/4                      notconnect   1            auto  a-10G 
Te3/0/5                      notconnect   1            auto  a-10G 
Te3/0/6                      notconnect   1            auto  a-10G 
Te3/0/7                      notconnect   1            auto  a-10G 
Te3/0/8                      notconnect   1            auto  a-10G 
Fo3/0/9                      inactive     1            auto   auto 
Fo3/0/10                     inactive     1            auto   auto 
Gi5/0/1                      notconnect   636          auto   auto 10/100/1000BaseTX
Gi5/0/2                      notconnect   636          auto   auto 10/100/1000BaseTX
Gi5/0/3                      notconnect   636          auto   auto 10/100/1000BaseTX
Gi5/0/4                      notconnect   636          auto   auto 10/100/1000BaseTX
Gi5/0/5                      notconnect   636          auto   auto 10/100/1000BaseTX
Gi5/0/6                      notconnect   636          auto   auto 10/100/1000BaseTX
Gi5/0/7                      notconnect   636          auto   auto 10/100/1000BaseTX
Gi5/0/8                      notconnect   636          auto   auto 10/100/1000BaseTX
Gi5/0/9                      notconnect   636          auto   auto 10/100/1000BaseTX
Gi5/0/10                     notconnect   636          auto   auto 10/100/1000BaseTX
          
Port      Name               Status       Vlan       Duplex  Speed Type 
Gi5/0/11                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi5/0/12                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi5/0/13                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi5/0/14                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi5/0/15                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi5/0/16                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi5/0/17                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi5/0/18                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi5/0/19                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi5/0/20                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi5/0/21                     notconnect   125          auto   auto 10/100/1000BaseTX
Gi5/0/22                     notconnect   125          auto   auto 10/100/1000BaseTX
Gi5/0/23                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi5/0/24                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi5/0/25  #SwissTubes        connected    732        a-full  a-100 10/100/1000BaseTX
Gi5/0/26  #SwissTubes        connected    732        a-full  a-100 10/100/1000BaseTX
Gi5/0/27  #SwissTubes        connected    732        a-full  a-100 10/100/1000BaseTX
Gi5/0/28  #SwissTubes        notconnect   732          auto   auto 10/100/1000BaseTX
Gi5/0/29  #SwissTubes        connected    732        a-full  a-100 10/100/1000BaseTX
Gi5/0/30  #SwissTubes        notconnect   732          auto   auto 10/100/1000BaseTX
Gi5/0/31  #CCure jack 1283   connected    607        a-half   a-10 10/100/1000BaseTX
Gi5/0/32                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi5/0/33                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi5/0/34                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi5/0/35                     connected    341        a-full  a-100 10/100/1000BaseTX
Gi5/0/36                     connected    341        a-full  a-100 10/100/1000BaseTX
Gi5/0/37  #CCure Jack 1285   notconnect   607          auto   auto 10/100/1000BaseTX
Gi5/0/38  #AP                notconnect   1037         auto   auto 10/100/1000BaseTX
Gi5/0/39  #AP                notconnect   1037         auto   auto 10/100/1000BaseTX
Gi5/0/40  #AP                notconnect   1037         auto   auto 10/100/1000BaseTX
Gi5/0/41  #AP                notconnect   1037         auto   auto 10/100/1000BaseTX
Gi5/0/42  #AP                notconnect   1037         auto   auto 10/100/1000BaseTX
Gi5/0/43  #AP                notconnect   1037         auto   auto 10/100/1000BaseTX
Gi5/0/44  #AP                connected    1037       a-full a-1000 10/100/1000BaseTX
Gi5/0/45  #AP                connected    1037       a-full a-1000 10/100/1000BaseTX
Gi5/0/46  #AP                notconnect   1037         auto   auto 10/100/1000BaseTX
Gi5/0/47  #AP                connected    1037       a-full  a-100 10/100/1000BaseTX
Gi5/0/48  #AP                notconnect   1037         auto   auto 10/100/1000BaseTX
Gi6/0/1                      notconnect   636          auto   auto 10/100/1000BaseTX
Gi6/0/2                      notconnect   636          auto   auto 10/100/1000BaseTX
Gi6/0/3                      notconnect   636          auto   auto 10/100/1000BaseTX
Gi6/0/4                      notconnect   636          auto   auto 10/100/1000BaseTX
Gi6/0/5                      notconnect   636          auto   auto 10/100/1000BaseTX
Gi6/0/6                      notconnect   636          auto   auto 10/100/1000BaseTX
Gi6/0/7                      notconnect   636          auto   auto 10/100/1000BaseTX
Gi6/0/8                      notconnect   636          auto   auto 10/100/1000BaseTX
Gi6/0/9                      notconnect   636          auto   auto 10/100/1000BaseTX
Gi6/0/10                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi6/0/11                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi6/0/12                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi6/0/13  CCURE              connected    1209       a-full a-1000 10/100/1000BaseTX
Gi6/0/14                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi6/0/15                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi6/0/16                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi6/0/17                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi6/0/18                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi6/0/19                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi6/0/20  Wireless AP        connected    1037       a-full a-1000 10/100/1000BaseTX
Gi6/0/21                     notconnect   636          auto   auto 10/100/1000BaseTX
          
Port      Name               Status       Vlan       Duplex  Speed Type 
Gi6/0/22  Wireless AP        connected    1037       a-full a-1000 10/100/1000BaseTX
Gi6/0/23                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi6/0/24  Wireless AP        connected    1037       a-full a-1000 10/100/1000BaseTX
Gi6/0/25                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi6/0/26                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi6/0/27                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi6/0/28                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi6/0/29                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi6/0/30                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi6/0/31                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi6/0/32                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi6/0/33                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi6/0/34                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi6/0/35                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi6/0/36                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi6/0/37                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi6/0/38                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi6/0/39                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi6/0/40                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi6/0/41                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi6/0/42                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi6/0/43                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi6/0/44                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi6/0/45                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi6/0/46                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi6/0/47                     notconnect   636          auto   auto 10/100/1000BaseTX
Gi6/0/48  #UPS               connected    332        a-full  a-100 10/100/1000BaseTX""",
 'show run | section interface':"""match interface input
 collect interface output
interface GigabitEthernet0/0
 vrf forwarding Mgmt-vrf
 no ip address
 no ip route-cache
 shutdown
 negotiation auto
interface GigabitEthernet1/0/1
 description #temp uplink
 switchport access vlan 636
 switchport mode trunk
 switchport voice vlan 984
 spanning-tree portfast
 ip dhcp snooping trust
interface GigabitEthernet1/0/2
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet1/0/3
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet1/0/4
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet1/0/5
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet1/0/6
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet1/0/7
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet1/0/8
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet1/0/9
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet1/0/10
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
           spanning-tree portfast
interface GigabitEthernet1/0/11
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet1/0/12
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet1/0/13
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet1/0/14
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet1/0/15
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet1/0/16
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet1/0/17
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet1/0/18
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet1/0/19
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet1/0/20
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet1/0/21
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet1/0/22
 switchport access vlan 636
 switchport mode access
           switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet1/0/23
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet1/0/24
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet1/0/25
 switchport access vlan 1605
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/26
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet1/0/27
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet1/0/28
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet1/0/29
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet1/0/30
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet1/0/31
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet1/0/32
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet1/0/33
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet1/0/34
 switchport access vlan 636
 switchport mode access
           switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet1/0/35
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet1/0/36
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet1/0/37
 switchport access vlan 636
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/38
 switchport access vlan 636
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/39
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet1/0/40
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet1/0/41
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet1/0/42
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet1/0/43
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet1/0/44
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet1/0/45
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet1/0/46
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
           spanning-tree portfast
interface GigabitEthernet1/0/47
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet1/0/48
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet2/0/1
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet2/0/2
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet2/0/3
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet2/0/4
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet2/0/5
 switchport access vlan 1605
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet2/0/6
 switchport access vlan 1605
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet2/0/7
 switchport access vlan 1605
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet2/0/8
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet2/0/9
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet2/0/10
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet2/0/11
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet2/0/12
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
          interface GigabitEthernet2/0/13
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet2/0/14
 switchport access vlan 396
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet2/0/15
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet2/0/16
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet2/0/17
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet2/0/18
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet2/0/19
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet2/0/20
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet2/0/21
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet2/0/22
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet2/0/23
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet2/0/24
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet2/0/25
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet2/0/26
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet2/0/27
 switchport access vlan 396
           switchport mode access
 spanning-tree portfast
interface GigabitEthernet2/0/28
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet2/0/29
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet2/0/30
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet2/0/31
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet2/0/32
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet2/0/33
 switchport access vlan 125
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet2/0/34
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet2/0/35
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet2/0/36
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet2/0/37
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet2/0/38
 switchport access vlan 1605
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet2/0/39
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet2/0/40
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet2/0/41
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet2/0/42
           switchport access vlan 396
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet2/0/43
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet2/0/44
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet2/0/45
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet2/0/46
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet2/0/47
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet2/0/48
 switchport access vlan 396
 switchport mode access
 spanning-tree portfast
interface TenGigabitEthernet3/0/1
 description t3/0/1:dx1-525 t2/11
 switchport mode trunk
 ip dhcp snooping trust
interface TenGigabitEthernet3/0/2
 description t3/0/2:dx2-525 t4/0/11
 switchport mode trunk
 ip dhcp snooping trust
interface TenGigabitEthernet3/0/3
interface TenGigabitEthernet3/0/4
interface TenGigabitEthernet3/0/5
interface TenGigabitEthernet3/0/6
interface TenGigabitEthernet3/0/7
interface TenGigabitEthernet3/0/8
interface FortyGigabitEthernet3/0/9
interface FortyGigabitEthernet3/0/10
interface GigabitEthernet5/0/1
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet5/0/2
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet5/0/3
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet5/0/4
           switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet5/0/5
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet5/0/6
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet5/0/7
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet5/0/8
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet5/0/9
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet5/0/10
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet5/0/11
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet5/0/12
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet5/0/13
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet5/0/14
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet5/0/15
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
          interface GigabitEthernet5/0/16
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet5/0/17
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet5/0/18
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet5/0/19
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet5/0/20
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet5/0/21
 switchport access vlan 125
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet5/0/22
 switchport access vlan 125
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet5/0/23
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet5/0/24
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet5/0/25
 description #SwissTubes
 switchport access vlan 732
 switchport mode access
 power inline never
 spanning-tree portfast
interface GigabitEthernet5/0/26
 description #SwissTubes
 switchport access vlan 732
 switchport mode access
 power inline never
 spanning-tree portfast
interface GigabitEthernet5/0/27
 description #SwissTubes
           switchport access vlan 732
 switchport mode access
 power inline never
 spanning-tree portfast
interface GigabitEthernet5/0/28
 description #SwissTubes
 switchport access vlan 732
 switchport mode access
 power inline never
 spanning-tree portfast
interface GigabitEthernet5/0/29
 description #SwissTubes
 switchport access vlan 732
 switchport mode access
 power inline never
 spanning-tree portfast
interface GigabitEthernet5/0/30
 description #SwissTubes
 switchport access vlan 732
 switchport mode access
 power inline never
 spanning-tree portfast
interface GigabitEthernet5/0/31
 description #CCure jack 1283
 switchport access vlan 607
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet5/0/32
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet5/0/33
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet5/0/34
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet5/0/35
 switchport access vlan 341
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet5/0/36
 switchport access vlan 341
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet5/0/37
 description #CCure Jack 1285
 switchport access vlan 607
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet5/0/38
 description #AP
 switchport access vlan 1037
 switchport mode access
           spanning-tree portfast
interface GigabitEthernet5/0/39
 description #AP
 switchport access vlan 1037
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet5/0/40
 description #AP
 switchport access vlan 1037
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet5/0/41
 description #AP
 switchport access vlan 1037
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet5/0/42
 description #AP
 switchport access vlan 1037
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet5/0/43
 description #AP
 switchport access vlan 1037
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet5/0/44
 description #AP
 switchport access vlan 1037
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet5/0/45
 description #AP
 switchport access vlan 1037
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet5/0/46
 description #AP
 switchport access vlan 1037
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet5/0/47
 description #AP
 switchport access vlan 1037
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet5/0/48
 description #AP
 switchport access vlan 1037
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet6/0/1
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet6/0/2
 switchport access vlan 636
 switchport mode access
           switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet6/0/3
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet6/0/4
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet6/0/5
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet6/0/6
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet6/0/7
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet6/0/8
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet6/0/9
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet6/0/10
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet6/0/11
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet6/0/12
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet6/0/13
 description CCURE
 switchport access vlan 1209
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet6/0/14
 switchport access vlan 636
           switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet6/0/15
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet6/0/16
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet6/0/17
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet6/0/18
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet6/0/19
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet6/0/20
 description Wireless AP
 switchport access vlan 1037
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet6/0/21
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet6/0/22
 description Wireless AP
 switchport access vlan 1037
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet6/0/23
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet6/0/24
 description Wireless AP
 switchport access vlan 1037
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet6/0/25
 switchport access vlan 636
 switchport mode access
           switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet6/0/26
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet6/0/27
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet6/0/28
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet6/0/29
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet6/0/30
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet6/0/31
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet6/0/32
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet6/0/33
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet6/0/34
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet6/0/35
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet6/0/36
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet6/0/37
 switchport access vlan 636
           switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet6/0/38
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet6/0/39
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet6/0/40
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet6/0/41
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet6/0/42
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet6/0/43
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet6/0/44
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet6/0/45
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet6/0/46
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet6/0/47
 switchport access vlan 636
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
interface GigabitEthernet6/0/48
 description #UPS
 switchport access vlan 332
 switchport mode access
 switchport voice vlan 984
 spanning-tree portfast
          interface Vlan1
 no ip address
 no ip route-cache
 shutdown
interface Vlan332
 description clinical-525hosp-m
 ip address 172.20.64.37 255.255.255.0
 no ip route-cache
logging source-interface Vlan332""",
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
interface GigabitEthernet2/0/1
interface GigabitEthernet2/0/2
interface GigabitEthernet2/0/3
interface GigabitEthernet2/0/4
interface GigabitEthernet2/0/5
interface GigabitEthernet2/0/6
interface GigabitEthernet2/0/7
interface GigabitEthernet2/0/8
          interface GigabitEthernet2/0/9
interface GigabitEthernet2/0/10
interface GigabitEthernet2/0/11
interface GigabitEthernet2/0/12
interface GigabitEthernet2/0/13
interface GigabitEthernet2/0/14
interface GigabitEthernet2/0/15
interface GigabitEthernet2/0/16
interface GigabitEthernet2/0/17
interface GigabitEthernet2/0/18
interface GigabitEthernet2/0/19
interface GigabitEthernet2/0/20
interface GigabitEthernet2/0/21
interface GigabitEthernet2/0/22
interface GigabitEthernet2/0/23
interface GigabitEthernet2/0/24
interface GigabitEthernet2/0/25
interface GigabitEthernet2/0/26
interface GigabitEthernet2/0/27
interface GigabitEthernet2/0/28
interface GigabitEthernet2/0/29
interface GigabitEthernet2/0/30
interface GigabitEthernet2/0/31
interface GigabitEthernet2/0/32
interface GigabitEthernet2/0/33
interface GigabitEthernet2/0/34
interface GigabitEthernet2/0/35
interface GigabitEthernet2/0/36
interface GigabitEthernet2/0/37
interface GigabitEthernet2/0/38
interface GigabitEthernet2/0/39
interface GigabitEthernet2/0/40
interface GigabitEthernet2/0/41
interface GigabitEthernet2/0/42
interface GigabitEthernet2/0/43
interface GigabitEthernet2/0/44
interface GigabitEthernet2/0/45
interface GigabitEthernet2/0/46
interface GigabitEthernet2/0/47
interface GigabitEthernet2/0/48
interface TenGigabitEthernet3/0/1
interface TenGigabitEthernet3/0/2
interface TenGigabitEthernet3/0/3
interface TenGigabitEthernet3/0/4
interface TenGigabitEthernet3/0/5
interface TenGigabitEthernet3/0/6
interface TenGigabitEthernet3/0/7
interface TenGigabitEthernet3/0/8
interface FortyGigabitEthernet3/0/9
interface FortyGigabitEthernet3/0/10
interface GigabitEthernet5/0/1
interface GigabitEthernet5/0/2
interface GigabitEthernet5/0/3
interface GigabitEthernet5/0/4
interface GigabitEthernet5/0/5
interface GigabitEthernet5/0/6
interface GigabitEthernet5/0/7
interface GigabitEthernet5/0/8
interface GigabitEthernet5/0/9
          interface GigabitEthernet5/0/10
interface GigabitEthernet5/0/11
interface GigabitEthernet5/0/12
interface GigabitEthernet5/0/13
interface GigabitEthernet5/0/14
interface GigabitEthernet5/0/15
interface GigabitEthernet5/0/16
interface GigabitEthernet5/0/17
interface GigabitEthernet5/0/18
interface GigabitEthernet5/0/19
interface GigabitEthernet5/0/20
interface GigabitEthernet5/0/21
interface GigabitEthernet5/0/22
interface GigabitEthernet5/0/23
interface GigabitEthernet5/0/24
interface GigabitEthernet5/0/25
interface GigabitEthernet5/0/26
interface GigabitEthernet5/0/27
interface GigabitEthernet5/0/28
interface GigabitEthernet5/0/29
interface GigabitEthernet5/0/30
interface GigabitEthernet5/0/31
interface GigabitEthernet5/0/32
interface GigabitEthernet5/0/33
interface GigabitEthernet5/0/34
interface GigabitEthernet5/0/35
interface GigabitEthernet5/0/36
interface GigabitEthernet5/0/37
interface GigabitEthernet5/0/38
interface GigabitEthernet5/0/39
interface GigabitEthernet5/0/40
interface GigabitEthernet5/0/41
interface GigabitEthernet5/0/42
interface GigabitEthernet5/0/43
interface GigabitEthernet5/0/44
interface GigabitEthernet5/0/45
interface GigabitEthernet5/0/46
interface GigabitEthernet5/0/47
interface GigabitEthernet5/0/48
interface GigabitEthernet6/0/1
interface GigabitEthernet6/0/2
interface GigabitEthernet6/0/3
interface GigabitEthernet6/0/4
interface GigabitEthernet6/0/5
interface GigabitEthernet6/0/6
interface GigabitEthernet6/0/7
interface GigabitEthernet6/0/8
interface GigabitEthernet6/0/9
interface GigabitEthernet6/0/10
interface GigabitEthernet6/0/11
interface GigabitEthernet6/0/12
interface GigabitEthernet6/0/13
interface GigabitEthernet6/0/14
interface GigabitEthernet6/0/15
interface GigabitEthernet6/0/16
interface GigabitEthernet6/0/17
interface GigabitEthernet6/0/18
interface GigabitEthernet6/0/19
interface GigabitEthernet6/0/20
          interface GigabitEthernet6/0/21
interface GigabitEthernet6/0/22
interface GigabitEthernet6/0/23
interface GigabitEthernet6/0/24
interface GigabitEthernet6/0/25
interface GigabitEthernet6/0/26
interface GigabitEthernet6/0/27
interface GigabitEthernet6/0/28
interface GigabitEthernet6/0/29
interface GigabitEthernet6/0/30
interface GigabitEthernet6/0/31
interface GigabitEthernet6/0/32
interface GigabitEthernet6/0/33
interface GigabitEthernet6/0/34
interface GigabitEthernet6/0/35
interface GigabitEthernet6/0/36
interface GigabitEthernet6/0/37
interface GigabitEthernet6/0/38
interface GigabitEthernet6/0/39
interface GigabitEthernet6/0/40
interface GigabitEthernet6/0/41
interface GigabitEthernet6/0/42
interface GigabitEthernet6/0/43
interface GigabitEthernet6/0/44
interface GigabitEthernet6/0/45
interface GigabitEthernet6/0/46
interface GigabitEthernet6/0/47
interface GigabitEthernet6/0/48
interface Vlan1
interface Vlan332
logging source-interface Vlan332""",
 'show interface link':"""^
% Invalid input detected at '^' marker.
""",
 'show interface':"""Vlan1 is administratively down, line protocol is down 
  Hardware is Ethernet SVI, address is 700f.6add.3e43 (bia 700f.6add.3e43)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters never
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     14301396 packets input, 915289344 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 2 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Vlan332 is up, line protocol is up 
  Hardware is Ethernet SVI, address is 700f.6add.3e45 (bia 700f.6add.3e45)
  Description: clinical-525hosp-m
  Internet address is 172.20.64.37/24
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 00:00:23, output hang never
  Last clearing of "" counters never
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 6000 bits/sec, 6 packets/sec
  5 minute output rate 9000 bits/sec, 4 packets/sec
     591568585 packets input, 91986539309 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     411136104 packets output, 98014861032 bytes, 0 underruns
     0 output errors, 1 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet0/0 is administratively down, line protocol is down 
  Hardware is RP management port, address is 700f.6add.3e69 (bia 700f.6add.3e69)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto Duplex, Auto Speed, link type is auto, media type is RJ45
  output flow-control is unsupported, input flow-control is unsupported
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
     0 watchdog, 0 multicast, 0 pause input
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     1 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/1 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7131.5930 (bia 00b7.7131.5930)
  Description: #temp uplink
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 254/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 2y13w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     3 packets input, 7205 bytes, 0 no buffer
     Received 2 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     1 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     119 packets output, 11995 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/2 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7131.5931 (bia 00b7.7131.5931)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/3 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7131.5932 (bia 00b7.7131.5932)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y31w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 17560711
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     432324109 packets input, 282950597910 bytes, 0 no buffer
     Received 1159309 broadcasts (759258 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 759258 multicast, 0 pause input
     0 input packets with dribble condition detected
     678506503 packets output, 415614822331 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     36910 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/4 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7131.5933 (bia 00b7.7131.5933)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y32w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 30130603
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     583348505 packets input, 445896392219 bytes, 0 no buffer
     Received 1956521 broadcasts (987423 multicasts)
     0 runts, 0 giants, 0 throttles 
               0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 987423 multicast, 0 pause input
     0 input packets with dribble condition detected
     802192428 packets output, 513593227215 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     161561 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/5 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7131.5934 (bia 00b7.7131.5934)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y32w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 45979466
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     511294176 packets input, 332747337474 bytes, 0 no buffer
     Received 2099014 broadcasts (1279815 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 1279815 multicast, 647512 pause input
     0 input packets with dribble condition detected
     724215776 packets output, 401430383611 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     158395 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/6 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7131.5935 (bia 00b7.7131.5935)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y32w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 714334
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     89324313 packets input, 17426227226 bytes, 0 no buffer
     Received 1683865 broadcasts (707555 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 707555 multicast, 0 pause input
     0 input packets with dribble condition detected
               324159063 packets output, 96341616816 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     2886 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/7 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7131.5936 (bia 00b7.7131.5936)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y31w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 25400968
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     495676994 packets input, 309097528568 bytes, 0 no buffer
     Received 1044876 broadcasts (898513 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 898513 multicast, 0 pause input
     0 input packets with dribble condition detected
     710691341 packets output, 387369920144 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     77831 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/8 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7131.5937 (bia 00b7.7131.5937)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y31w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 1846532
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     57797873 packets input, 10338366724 bytes, 0 no buffer
     Received 795566 broadcasts (728716 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 728716 multicast, 0 pause input
     0 input packets with dribble condition detected
     281492711 packets output, 61128833167 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     65903 unknown protocol drops
               0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/9 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7131.5938 (bia 00b7.7131.5938)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 1y31w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 23683294
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     752930833 packets input, 483586730478 bytes, 0 no buffer
     Received 1684194 broadcasts (792538 multicasts)
     0 runts, 0 giants, 0 throttles 
     1 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 792538 multicast, 0 pause input
     0 input packets with dribble condition detected
     981278098 packets output, 683583423802 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     132282 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/10 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7131.5939 (bia 00b7.7131.5939)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y31w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 33768604
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     844841587 packets input, 540086875463 bytes, 0 no buffer
     Received 1016095 broadcasts (876980 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 876980 multicast, 0 pause input
     0 input packets with dribble condition detected
     1121830335 packets output, 831891959232 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     82142 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
          GigabitEthernet1/0/11 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7131.593a (bia 00b7.7131.593a)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y32w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 10111779
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     64576509 packets input, 9605387165 bytes, 0 no buffer
     Received 776731 broadcasts (717157 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 717157 multicast, 0 pause input
     0 input packets with dribble condition detected
     291267033 packets output, 72322477690 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     58380 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/12 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7131.593b (bia 00b7.7131.593b)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y32w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 1568326
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     106070444 packets input, 16042755965 bytes, 0 no buffer
     Received 764674 broadcasts (709819 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 709819 multicast, 0 pause input
     0 input packets with dribble condition detected
     368609173 packets output, 143986062528 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     8508 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/13 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 00b7.7131.593c (bia 00b7.7131.593c)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
               reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 00:00:00, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 3595054690
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 5000 bits/sec, 5 packets/sec
  5 minute output rate 17000 bits/sec, 15 packets/sec
     893821549 packets input, 403907527883 bytes, 0 no buffer
     Received 5466188 broadcasts (5044149 multicasts)
     2747 runts, 0 giants, 0 throttles 
     174205 input errors, 9 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 5044149 multicast, 0 pause input
     0 input packets with dribble condition detected
     1553789455 packets output, 912502570983 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     246410 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/14 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7131.593d (bia 00b7.7131.593d)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/15 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7131.593e (bia 00b7.7131.593e)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
            Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y32w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 2928735
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     81486298 packets input, 13296155452 bytes, 0 no buffer
     Received 756494 broadcasts (717852 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 717852 multicast, 0 pause input
     0 input packets with dribble condition detected
     308412840 packets output, 69357893116 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     6293 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/16 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7131.593f (bia 00b7.7131.593f)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y32w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 685507
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     85004417 packets input, 12866539369 bytes, 0 no buffer
     Received 738572 broadcasts (715628 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 715628 multicast, 0 pause input
     0 input packets with dribble condition detected
     309857353 packets output, 88429087676 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     5028 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/17 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7131.5940 (bia 00b7.7131.5940)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
            Last input 2y14w, output 1y32w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 2686268
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     108217473 packets input, 16356244814 bytes, 0 no buffer
     Received 1753919 broadcasts (709617 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 709617 multicast, 0 pause input
     0 input packets with dribble condition detected
     329535389 packets output, 69855913760 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     8220 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/18 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7131.5941 (bia 00b7.7131.5941)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y32w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 16103919
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     747598595 packets input, 539814711188 bytes, 0 no buffer
     Received 915694 broadcasts (771124 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 771124 multicast, 0 pause input
     0 input packets with dribble condition detected
     966259112 packets output, 673342985081 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     78223 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/19 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7131.5942 (bia 00b7.7131.5942)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y32w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 3262690
            Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     86144962 packets input, 13280543378 bytes, 0 no buffer
     Received 730594 broadcasts (710376 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 710376 multicast, 0 pause input
     0 input packets with dribble condition detected
     343465579 packets output, 130525968066 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     7879 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/20 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7131.5943 (bia 00b7.7131.5943)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y32w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 4503078
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     91796311 packets input, 12399081901 bytes, 0 no buffer
     Received 773246 broadcasts (715470 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 715470 multicast, 0 pause input
     0 input packets with dribble condition detected
     333876807 packets output, 120974316641 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     55260 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/21 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7131.5944 (bia 00b7.7131.5944)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y32w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 505928
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
            5 minute output rate 0 bits/sec, 0 packets/sec
     82269301 packets input, 13819703192 bytes, 0 no buffer
     Received 766093 broadcasts (718569 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 718569 multicast, 0 pause input
     0 input packets with dribble condition detected
     315868807 packets output, 78996987892 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     7832 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/22 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7131.5945 (bia 00b7.7131.5945)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y31w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 17642680
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     688783486 packets input, 500028372431 bytes, 0 no buffer
     Received 1063487 broadcasts (931469 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 931469 multicast, 0 pause input
     0 input packets with dribble condition detected
     917179751 packets output, 597279081937 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     66612 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/23 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7131.5946 (bia 00b7.7131.5946)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y32w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 3212063
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     103620608 packets input, 15432978087 bytes, 0 no buffer
     Received 765007 broadcasts (709910 multicasts)
               0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 709910 multicast, 0 pause input
     0 input packets with dribble condition detected
     362651765 packets output, 139421732114 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     8906 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/24 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7131.5947 (bia 00b7.7131.5947)
  MTU 1500 bytes, BW 10000 Kbit/sec, DLY 1000 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 1y30w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 24253673
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     199230442 packets input, 146522085023 bytes, 0 no buffer
     Received 344054 broadcasts (52803 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 52803 multicast, 0 pause input
     0 input packets with dribble condition detected
     396899624 packets output, 215521100185 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     71219 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/25 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7131.5948 (bia 00b7.7131.5948)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 44w0d, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     520 packets input, 393048 bytes, 0 no buffer
     Received 443 broadcasts (386 multicasts)
     0 runts, 0 giants, 0 throttles 
     9 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 386 multicast, 0 pause input
               0 input packets with dribble condition detected
     51681 packets output, 6607012 bytes, 0 underruns
     0 output errors, 0 collisions, 4 interface resets
     39 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/26 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7131.5949 (bia 00b7.7131.5949)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 2y14w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     65 packets input, 16592 bytes, 0 no buffer
     Received 64 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     2 input errors, 1 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     6158 packets output, 556471 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/27 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7131.594a (bia 00b7.7131.594a)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 1y31w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 16542245
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     603659202 packets input, 434836667048 bytes, 0 no buffer
     Received 518220 broadcasts (273243 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 273243 multicast, 0 pause input
     0 input packets with dribble condition detected
     834161209 packets output, 528530228095 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
               161323 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/28 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7131.594b (bia 00b7.7131.594b)
  MTU 1500 bytes, BW 10000 Kbit/sec, DLY 1000 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y32w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 2446584399
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     623433605 packets input, 495136047484 bytes, 0 no buffer
     Received 212851 broadcasts (92518 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 92518 multicast, 0 pause input
     0 input packets with dribble condition detected
     825585076 packets output, 524455556447 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     59211 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/29 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7131.594c (bia 00b7.7131.594c)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y31w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 1680821
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     86139943 packets input, 10422697154 bytes, 0 no buffer
     Received 730651 broadcasts (728727 multicasts)
     0 runts, 0 giants, 0 throttles 
     1 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 728727 multicast, 0 pause input
     0 input packets with dribble condition detected
     313166744 packets output, 86193927787 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     1322 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
               0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/30 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7131.594d (bia 00b7.7131.594d)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y31w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 587654
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     63032280 packets input, 9895692934 bytes, 0 no buffer
     Received 798684 broadcasts (729342 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 729342 multicast, 0 pause input
     0 input packets with dribble condition detected
     313211637 packets output, 107879656159 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     56982 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/31 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7131.594e (bia 00b7.7131.594e)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y32w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 49952181
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     739421274 packets input, 559070664072 bytes, 0 no buffer
     Received 1866882 broadcasts (932584 multicasts)
     0 runts, 0 giants, 0 throttles 
     1 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 932584 multicast, 0 pause input
     0 input packets with dribble condition detected
     951611509 packets output, 640877438391 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     157880 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/32 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7131.594f (bia 00b7.7131.594f)
            MTU 1500 bytes, BW 10000 Kbit/sec, DLY 1000 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y30w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 49453792
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     547536894 packets input, 407149514047 bytes, 0 no buffer
     Received 1622813 broadcasts (898871 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 898871 multicast, 0 pause input
     0 input packets with dribble condition detected
     785258037 packets output, 479520933563 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     40093 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/33 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7131.5950 (bia 00b7.7131.5950)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y31w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 793865
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     8334835 packets input, 1918586491 bytes, 0 no buffer
     Received 99641 broadcasts (25264 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 25264 multicast, 0 pause input
     0 input packets with dribble condition detected
     231223458 packets output, 34395878799 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     74045 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/34 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7131.5951 (bia 00b7.7131.5951)
  MTU 1500 bytes, BW 10000 Kbit/sec, DLY 1000 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
            Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y30w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 40747552
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     892311537 packets input, 481538055630 bytes, 0 no buffer
     Received 1621764 broadcasts (1297895 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 1297895 multicast, 0 pause input
     0 input packets with dribble condition detected
     1134269160 packets output, 783680136903 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     171236 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/35 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7131.5952 (bia 00b7.7131.5952)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y31w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 408034
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     52869456 packets input, 7227674404 bytes, 0 no buffer
     Received 803446 broadcasts (728624 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 728624 multicast, 0 pause input
     0 input packets with dribble condition detected
     279621914 packets output, 66942106278 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     73825 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/36 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7131.5953 (bia 00b7.7131.5953)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
            ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y31w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 1731958
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     12809712 packets input, 2372533668 bytes, 0 no buffer
     Received 36897 broadcasts (27394 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 27394 multicast, 0 pause input
     0 input packets with dribble condition detected
     236025159 packets output, 37694541588 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     2326 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/37 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7131.5954 (bia 00b7.7131.5954)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 254/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 35w1d, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     64 packets input, 22557 bytes, 0 no buffer
     Received 32 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     2 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     604 packets output, 77841 bytes, 0 underruns
     0 output errors, 0 collisions, 3 interface resets
     9 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/38 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7131.5955 (bia 00b7.7131.5955)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 35w1d, output hang never
  Last clearing of "" counters 2y14w
            Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     30 packets input, 4675 bytes, 0 no buffer
     Received 10 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     1308 packets output, 155457 bytes, 0 underruns
     0 output errors, 0 collisions, 3 interface resets
     4 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/39 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7131.5956 (bia 00b7.7131.5956)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y31w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 30758880
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     602056225 packets input, 379535359673 bytes, 0 no buffer
     Received 1517456 broadcasts (890286 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 890286 multicast, 0 pause input
     0 input packets with dribble condition detected
     834594372 packets output, 578049825361 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     94355 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/40 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7131.5957 (bia 00b7.7131.5957)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y29w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 38274205
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
            5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     606940783 packets input, 469518131835 bytes, 0 no buffer
     Received 1608968 broadcasts (880024 multicasts)
     0 runts, 0 giants, 0 throttles 
     1 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 880024 multicast, 0 pause input
     0 input packets with dribble condition detected
     866236918 packets output, 563855926426 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     79620 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/41 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7131.5958 (bia 00b7.7131.5958)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 1y31w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 29421427
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     591252740 packets input, 425810107584 bytes, 0 no buffer
     Received 1306699 broadcasts (806420 multicasts)
     1 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 806420 multicast, 0 pause input
     0 input packets with dribble condition detected
     820143290 packets output, 512186738194 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     61305 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/42 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7131.5959 (bia 00b7.7131.5959)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y28w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 270174
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     4641140 packets input, 2247044039 bytes, 0 no buffer
               Received 164917 broadcasts (38433 multicasts)
     0 runts, 0 giants, 0 throttles 
     5 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 38433 multicast, 0 pause input
     0 input packets with dribble condition detected
     231483669 packets output, 32751235834 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     353 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/43 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7131.595a (bia 00b7.7131.595a)
  MTU 1500 bytes, BW 10000 Kbit/sec, DLY 1000 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y28w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 543678
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     15611227 packets input, 2980559420 bytes, 0 no buffer
     Received 271270 broadcasts (72634 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 72634 multicast, 0 pause input
     0 input packets with dribble condition detected
     249280169 packets output, 37427183155 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     155775 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/44 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7131.595b (bia 00b7.7131.595b)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y30w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 111809019
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     397996044 packets input, 270492346397 bytes, 0 no buffer
     Received 1028029 broadcasts (907214 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
               0 watchdog, 907214 multicast, 0 pause input
     0 input packets with dribble condition detected
     622841131 packets output, 346860561746 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     50949 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/45 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7131.595c (bia 00b7.7131.595c)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y31w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 60117173
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     800093417 packets input, 564550782375 bytes, 0 no buffer
     Received 1775752 broadcasts (786103 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 786103 multicast, 0 pause input
     0 input packets with dribble condition detected
     1066497239 packets output, 791864287456 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     116466 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/46 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7131.595d (bia 00b7.7131.595d)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y37w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 43773584
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     424098171 packets input, 324246015515 bytes, 0 no buffer
     Received 911850 broadcasts (750545 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 750545 multicast, 0 pause input
     0 input packets with dribble condition detected
     619924225 packets output, 366850843466 bytes, 0 underruns
               0 output errors, 0 collisions, 2 interface resets
     86758 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/47 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7131.595e (bia 00b7.7131.595e)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y31w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 1795434
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     51964260 packets input, 7407708921 bytes, 0 no buffer
     Received 768287 broadcasts (728442 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 728442 multicast, 0 pause input
     0 input packets with dribble condition detected
     278727481 packets output, 65903975398 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     39266 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/48 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7131.595f (bia 00b7.7131.595f)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y32w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 66714748
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     827448898 packets input, 549604520769 bytes, 0 no buffer
     Received 1743111 broadcasts (821576 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 821576 multicast, 0 pause input
     0 input packets with dribble condition detected
     1091037757 packets output, 801189801519 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     99151 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
               0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet2/0/1 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is a093.518e.587c (bia a093.518e.587c)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet2/0/2 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is a093.518e.587d (bia a093.518e.587d)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet2/0/3 is down, line protocol is down (notconnect) 
            Hardware is Gigabit Ethernet, address is a093.518e.587e (bia a093.518e.587e)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 44w0d, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     19 packets input, 15830 bytes, 0 no buffer
     Received 12 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     2 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     817 packets output, 67742 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     5 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet2/0/4 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is a093.518e.587f (bia a093.518e.587f)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 2y12w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     1576 packets input, 1048083 bytes, 0 no buffer
     Received 1555 broadcasts (1536 multicasts)
     0 runts, 0 giants, 0 throttles 
     1 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 1536 multicast, 0 pause input
     0 input packets with dribble condition detected
     10724180 packets output, 791192103 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     4 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet2/0/5 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is a093.518e.5880 (bia a093.518e.5880)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 2/255
            Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 00:00:00, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 1043000 bits/sec, 133 packets/sec
  5 minute output rate 8000 bits/sec, 13 packets/sec
     17819048125 packets input, 23479098893437 bytes, 0 no buffer
     Received 3748 broadcasts (3427 multicasts)
     0 runts, 0 giants, 0 throttles 
     4 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 3427 multicast, 0 pause input
     0 input packets with dribble condition detected
     746440392 packets output, 67640022409 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     2 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet2/0/6 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is a093.518e.5881 (bia a093.518e.5881)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 4/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 00:00:00, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 1611000 bits/sec, 171 packets/sec
  5 minute output rate 8000 bits/sec, 13 packets/sec
     14215846148 packets input, 18120839442343 bytes, 0 no buffer
     Received 4640 broadcasts (4359 multicasts)
     0 runts, 0 giants, 0 throttles 
     4 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 4359 multicast, 0 pause input
     0 input packets with dribble condition detected
     734720266 packets output, 66780843933 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet2/0/7 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is a093.518e.5882 (bia a093.518e.5882)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 4/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
            input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 00:00:00, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 1643000 bits/sec, 174 packets/sec
  5 minute output rate 8000 bits/sec, 13 packets/sec
     19820646545 packets input, 26499314103729 bytes, 0 no buffer
     Received 1415 broadcasts (1238 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 1238 multicast, 0 pause input
     0 input packets with dribble condition detected
     736775063 packets output, 66870959077 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     2 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet2/0/8 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is a093.518e.5883 (bia a093.518e.5883)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y29w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 8802
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     2311202 packets input, 271260601 bytes, 0 no buffer
     Received 320664 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     560419726 packets output, 43028306066 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     345 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet2/0/9 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is a093.518e.5884 (bia a093.518e.5884)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y28w, output hang never
            Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 11247
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     2057578 packets input, 210241536 bytes, 0 no buffer
     Received 316241 broadcasts (8 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 8 multicast, 0 pause input
     0 input packets with dribble condition detected
     568718882 packets output, 41000273418 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     93 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet2/0/10 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is a093.518e.5885 (bia a093.518e.5885)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet2/0/11 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is a093.518e.5886 (bia a093.518e.5886)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y28w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
            Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     1692011 packets input, 158273500 bytes, 0 no buffer
     Received 279300 broadcasts (16 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 16 multicast, 0 pause input
     0 input packets with dribble condition detected
     508764872 packets output, 36661876475 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     104 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet2/0/12 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is a093.518e.5887 (bia a093.518e.5887)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 1y28w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     1616300 packets input, 155700765 bytes, 0 no buffer
     Received 246342 broadcasts (76 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 76 multicast, 0 pause input
     0 input packets with dribble condition detected
     438114619 packets output, 31562924610 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     113 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet2/0/13 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is a093.518e.5888 (bia a093.518e.5888)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 6w3d, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 2677871890
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
               12720767 packets input, 1618768053 bytes, 0 no buffer
     Received 3226657 broadcasts (1300810 multicasts)
     45 runts, 0 giants, 0 throttles 
     217 input errors, 216 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 1300810 multicast, 0 pause input
     0 input packets with dribble condition detected
     2272936206 packets output, 237980631154 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     415 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet2/0/14 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is a093.518e.5889 (bia a093.518e.5889)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 2y13w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     32 packets input, 14482 bytes, 0 no buffer
     Received 21 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     13 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     31994 packets output, 2567636 bytes, 0 underruns
     0 output errors, 0 collisions, 3 interface resets
     13 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet2/0/15 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is a093.518e.588a (bia a093.518e.588a)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y28w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 11082
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     2127797 packets input, 205339088 bytes, 0 no buffer
     Received 333478 broadcasts (20 multicasts)
     0 runts, 0 giants, 0 throttles 
               0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 20 multicast, 0 pause input
     0 input packets with dribble condition detected
     568894784 packets output, 41046313311 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     99 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet2/0/16 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is a093.518e.588b (bia a093.518e.588b)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet2/0/17 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is a093.518e.588c (bia a093.518e.588c)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y33w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 10269
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     2230461 packets input, 238597018 bytes, 0 no buffer
     Received 383543 broadcasts (136089 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 136089 multicast, 0 pause input
     0 input packets with dribble condition detected
               472661331 packets output, 36232727261 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     5 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet2/0/18 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is a093.518e.588d (bia a093.518e.588d)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y33w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 6357
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     888733 packets input, 65474500 bytes, 0 no buffer
     Received 6189 broadcasts (14 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 14 multicast, 0 pause input
     0 input packets with dribble condition detected
     470161617 packets output, 34077933279 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     558 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet2/0/19 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is a093.518e.588e (bia a093.518e.588e)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
               0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet2/0/20 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is a093.518e.588f (bia a093.518e.588f)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y29w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     1221751 packets input, 103827823 bytes, 0 no buffer
     Received 23683 broadcasts (0 multicasts)
     4 runts, 0 giants, 0 throttles 
     1 input errors, 1 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     321491924 packets output, 23688022030 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     592 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet2/0/21 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is a093.518e.5890 (bia a093.518e.5890)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 1y31w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     1139541 packets input, 96813939 bytes, 0 no buffer
     Received 21755 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     1 input errors, 1 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     283311375 packets output, 21184975744 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     565 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
          GigabitEthernet2/0/22 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is a093.518e.5891 (bia a093.518e.5891)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 1y31w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     1133318 packets input, 96260458 bytes, 0 no buffer
     Received 21750 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     280030378 packets output, 20947921257 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     566 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet2/0/23 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is a093.518e.5892 (bia a093.518e.5892)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y31w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     1126954 packets input, 93104734 bytes, 0 no buffer
     Received 20913 broadcasts (0 multicasts)
     1 runts, 0 giants, 0 throttles 
     3 input errors, 3 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     267654171 packets output, 20348285105 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     613 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet2/0/24 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is a093.518e.5893 (bia a093.518e.5893)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
               reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 1y31w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     1164565 packets input, 102932862 bytes, 0 no buffer
     Received 20168 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     5 input errors, 5 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     258464292 packets output, 19518392696 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     618 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet2/0/25 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is a093.518e.5894 (bia a093.518e.5894)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 2y12w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     22 packets input, 8535 bytes, 0 no buffer
     Received 10 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     1 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     372 packets output, 31819 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     2 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet2/0/26 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is a093.518e.5895 (bia a093.518e.5895)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
            Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 44w0d, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     14 packets input, 7971 bytes, 0 no buffer
     Received 8 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     1 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     488 packets output, 37736 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     2 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet2/0/27 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is a093.518e.5896 (bia a093.518e.5896)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y31w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     962309 packets input, 81957315 bytes, 0 no buffer
     Received 19291 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     243898568 packets output, 18205227192 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     619 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet2/0/28 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is a093.518e.5897 (bia a093.518e.5897)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
            Last input 2y14w, output 1y31w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     222607516 packets input, 14267557876 bytes, 0 no buffer
     Received 19717 broadcasts (0 multicasts)
     1 runts, 0 giants, 0 throttles 
     2 input errors, 2 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     466175818 packets output, 32647840491 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     678 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet2/0/29 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is a093.518e.5898 (bia a093.518e.5898)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 1y31w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 15648
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     1287449 packets input, 120005840 bytes, 0 no buffer
     Received 45150 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     2 input errors, 2 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     273177947 packets output, 20765872237 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     24328 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet2/0/30 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is a093.518e.5899 (bia a093.518e.5899)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y30w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
            Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     1106215 packets input, 92217407 bytes, 0 no buffer
     Received 22381 broadcasts (0 multicasts)
     2 runts, 0 giants, 0 throttles 
     1 input errors, 1 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     290959815 packets output, 21697637348 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     693 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet2/0/31 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is a093.518e.589a (bia a093.518e.589a)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y32w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     959630 packets input, 80173388 bytes, 0 no buffer
     Received 19884 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     1 input errors, 1 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     249199550 packets output, 18687260412 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     698 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet2/0/32 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is a093.518e.589b (bia a093.518e.589b)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y29w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
            5 minute output rate 0 bits/sec, 0 packets/sec
     1096633 packets input, 92221498 bytes, 0 no buffer
     Received 21750 broadcasts (0 multicasts)
     3 runts, 0 giants, 0 throttles 
     1 input errors, 1 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     290660548 packets output, 21568811299 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     667 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet2/0/33 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is a093.518e.589c (bia a093.518e.589c)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y30w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 17196
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     24139777 packets input, 2393253720 bytes, 0 no buffer
     Received 47778 broadcasts (20024 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 20024 multicast, 0 pause input
     0 input packets with dribble condition detected
     396313254 packets output, 43648110092 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     5775 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet2/0/34 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is a093.518e.589d (bia a093.518e.589d)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y30w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 12714
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     1783881 packets input, 172245888 bytes, 0 no buffer
     Received 262450 broadcasts (12 multicasts)
               0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 12 multicast, 0 pause input
     0 input packets with dribble condition detected
     515112906 packets output, 38364277863 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     100 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet2/0/35 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is a093.518e.589e (bia a093.518e.589e)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y28w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 11247
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     2101826 packets input, 203025459 bytes, 0 no buffer
     Received 314140 broadcasts (8 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 8 multicast, 0 pause input
     0 input packets with dribble condition detected
     572230933 packets output, 41273591173 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     97 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet2/0/36 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is a093.518e.589f (bia a093.518e.589f)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y30w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 4401
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     2759203 packets input, 262912753 bytes, 0 no buffer
     Received 495715 broadcasts (191208 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 191208 multicast, 0 pause input
               0 input packets with dribble condition detected
     534769950 packets output, 49817160893 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     9 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet2/0/37 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is a093.518e.58a0 (bia a093.518e.58a0)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet2/0/38 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is a093.518e.58a1 (bia a093.518e.58a1)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 4/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 00:00:00, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 1726000 bits/sec, 174 packets/sec
  5 minute output rate 14000 bits/sec, 23 packets/sec
     5904288697 packets input, 7396913601277 bytes, 0 no buffer
     Received 4191 broadcasts (3853 multicasts)
     0 runts, 0 giants, 0 throttles 
     1 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 3853 multicast, 0 pause input
     0 input packets with dribble condition detected
     903227357 packets output, 79805641166 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
               9 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet2/0/39 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is a093.518e.58a2 (bia a093.518e.58a2)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y29w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 6438
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     3309278 packets input, 341247505 bytes, 0 no buffer
     Received 681982 broadcasts (274444 multicasts)
     0 runts, 0 giants, 0 throttles 
     1 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 274444 multicast, 0 pause input
     0 input packets with dribble condition detected
     561246203 packets output, 43807913606 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     143 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet2/0/40 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is a093.518e.58a3 (bia a093.518e.58a3)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y29w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 4155
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     1386715 packets input, 117273532 bytes, 0 no buffer
     Received 27098 broadcasts (0 multicasts)
     4 runts, 0 giants, 0 throttles 
     2 input errors, 2 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     373741736 packets output, 27451640210 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     530 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
               0 output buffer failures, 0 output buffers swapped out
GigabitEthernet2/0/41 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is a093.518e.58a4 (bia a093.518e.58a4)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y31w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 6357
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     2893057 packets input, 294090643 bytes, 0 no buffer
     Received 329456 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     517009150 packets output, 41129223882 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     97 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet2/0/42 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is a093.518e.58a5 (bia a093.518e.58a5)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 1y29w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     1186891 packets input, 101660843 bytes, 0 no buffer
     Received 23991 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     5 input errors, 5 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     403733944 packets output, 29315282747 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     440 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet2/0/43 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is a093.518e.58a6 (bia a093.518e.58a6)
            MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y30w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 1791
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     2126219 packets input, 209949913 bytes, 0 no buffer
     Received 291278 broadcasts (8 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 8 multicast, 0 pause input
     0 input packets with dribble condition detected
     522219691 packets output, 37844585182 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     2 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet2/0/44 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is a093.518e.58a7 (bia a093.518e.58a7)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 1y31w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     1174640 packets input, 123580305 bytes, 0 no buffer
     Received 89043 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     270447621 packets output, 20165296779 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     68579 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet2/0/45 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is a093.518e.58a8 (bia a093.518e.58a8)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
            Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y31w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 7335
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     1983662 packets input, 184721221 bytes, 0 no buffer
     Received 266717 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     515025942 packets output, 39121021410 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     94 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet2/0/46 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is a093.518e.58a9 (bia a093.518e.58a9)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y32w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     914356 packets input, 76840017 bytes, 0 no buffer
     Received 18095 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     1 input errors, 1 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     219771124 packets output, 16683666518 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     720 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet2/0/47 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is a093.518e.58aa (bia a093.518e.58aa)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
            ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y31w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 7335
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     3271422 packets input, 303517219 bytes, 0 no buffer
     Received 328686 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     517761780 packets output, 42018391802 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     92 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet2/0/48 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is a093.518e.58ab (bia a093.518e.58ab)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y31w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 7740
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     1092569 packets input, 92465431 bytes, 0 no buffer
     Received 21075 broadcasts (0 multicasts)
     1 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     267857361 packets output, 20124781900 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     644 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet3/0/1 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet, address is 700f.6add.3e6c (bia 700f.6add.3e6c)
  Description: t3/0/1:dx1-525 t2/11
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-SR
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 00:00:00, output hang never
            Last clearing of "" counters 2y14w
  Input queue: 0/375/8352/6 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 6242000 bits/sec, 1849 packets/sec
  5 minute output rate 7079000 bits/sec, 823 packets/sec
     95284860885 packets input, 40552526362447 bytes, 0 no buffer
     Received 57992313817 broadcasts (2220066577 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 2220066577 multicast, 0 pause input
     0 input packets with dribble condition detected
     88292411356 packets output, 87710064565390 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     767586737 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet3/0/2 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet, address is 700f.6add.3e6d (bia 700f.6add.3e6d)
  Description: t3/0/2:dx2-525 t4/0/11
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-SR
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 00:00:00, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/1151/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 57000 bits/sec, 76 packets/sec
  5 minute output rate 1000 bits/sec, 1 packets/sec
     13673482401 packets input, 4756555979331 bytes, 0 no buffer
     Received 6572076412 broadcasts (2405066297 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 2405066297 multicast, 0 pause input
     0 input packets with dribble condition detected
     3651588408 packets output, 3135133641348 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     2666883 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet3/0/3 is down, line protocol is down (notconnect) 
  Hardware is Ten Gigabit Ethernet, address is 700f.6add.3e6e (bia 700f.6add.3e6e)
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 10Gb/s, link type is auto, media type is 
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet3/0/4 is down, line protocol is down (notconnect) 
  Hardware is Ten Gigabit Ethernet, address is 700f.6add.3e6f (bia 700f.6add.3e6f)
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 10Gb/s, link type is auto, media type is 
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet3/0/5 is down, line protocol is down (notconnect) 
  Hardware is Ten Gigabit Ethernet, address is 700f.6add.3e70 (bia 700f.6add.3e70)
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 10Gb/s, link type is auto, media type is 
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet3/0/6 is down, line protocol is down (notconnect) 
  Hardware is Ten Gigabit Ethernet, address is 700f.6add.3e71 (bia 700f.6add.3e71)
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 10Gb/s, link type is auto, media type is 
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet3/0/7 is down, line protocol is down (notconnect) 
  Hardware is Ten Gigabit Ethernet, address is 700f.6add.3e72 (bia 700f.6add.3e72)
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 10Gb/s, link type is auto, media type is 
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet3/0/8 is down, line protocol is down (notconnect) 
  Hardware is Ten Gigabit Ethernet, address is 700f.6add.3e73 (bia 700f.6add.3e73)
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 10Gb/s, link type is auto, media type is 
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
FortyGigabitEthernet3/0/9 is down, line protocol is down (inactive) 
  Hardware is Forty Gigabit Ethernet, address is 700f.6add.3e74 (bia 700f.6add.3e74)
  MTU 1500 bytes, BW 40000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
FortyGigabitEthernet3/0/10 is down, line protocol is down (inactive) 
  Hardware is Forty Gigabit Ethernet, address is 700f.6add.3e75 (bia 700f.6add.3e75)
  MTU 1500 bytes, BW 40000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet5/0/1 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00ea.bdc4.9a90 (bia 00ea.bdc4.9a90)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 8w3d, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     1192 packets input, 92734 bytes, 0 no buffer
     Received 7 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     5840 packets output, 600271 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
               6 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet5/0/2 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00ea.bdc4.9a91 (bia 00ea.bdc4.9a91)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet5/0/3 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00ea.bdc4.9a92 (bia 00ea.bdc4.9a92)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
               0 output buffer failures, 0 output buffers swapped out
GigabitEthernet5/0/4 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00ea.bdc4.9a93 (bia 00ea.bdc4.9a93)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet5/0/5 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00ea.bdc4.9a94 (bia 00ea.bdc4.9a94)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet5/0/6 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00ea.bdc4.9a95 (bia 00ea.bdc4.9a95)
            MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet5/0/7 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00ea.bdc4.9a96 (bia 00ea.bdc4.9a96)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet5/0/8 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00ea.bdc4.9a97 (bia 00ea.bdc4.9a97)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
            Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet5/0/9 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00ea.bdc4.9a98 (bia 00ea.bdc4.9a98)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet5/0/10 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00ea.bdc4.9a99 (bia 00ea.bdc4.9a99)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
            ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet5/0/11 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00ea.bdc4.9a9a (bia 00ea.bdc4.9a9a)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet5/0/12 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00ea.bdc4.9a9b (bia 00ea.bdc4.9a9b)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
            Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet5/0/13 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00ea.bdc4.9a9c (bia 00ea.bdc4.9a9c)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 1y9w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     305 packets input, 90076 bytes, 0 no buffer
     Received 304 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     6236 packets output, 686293 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     52 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet5/0/14 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00ea.bdc4.9a9d (bia 00ea.bdc4.9a9d)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet5/0/15 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00ea.bdc4.9a9e (bia 00ea.bdc4.9a9e)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet5/0/16 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00ea.bdc4.9a9f (bia 00ea.bdc4.9a9f)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet5/0/17 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00ea.bdc4.9aa0 (bia 00ea.bdc4.9aa0)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet5/0/18 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00ea.bdc4.9aa1 (bia 00ea.bdc4.9aa1)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 1y30w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     86 packets input, 31628 bytes, 0 no buffer
     Received 30 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     3 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
               0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     1727 packets output, 201158 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     6 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet5/0/19 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00ea.bdc4.9aa2 (bia 00ea.bdc4.9aa2)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 44w0d, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     12 packets input, 1902 bytes, 0 no buffer
     Received 5 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     334 packets output, 36993 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     2 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet5/0/20 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00ea.bdc4.9aa3 (bia 00ea.bdc4.9aa3)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
               0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet5/0/21 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00ea.bdc4.9aa4 (bia 00ea.bdc4.9aa4)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 6w3d, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     76115157 packets input, 5239954099 bytes, 0 no buffer
     Received 1143 broadcasts (36 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 36 multicast, 0 pause input
     0 input packets with dribble condition detected
     265402973 packets output, 98879356013 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     36 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet5/0/22 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00ea.bdc4.9aa5 (bia 00ea.bdc4.9aa5)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 6w2d, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     384905318 packets input, 26766162520 bytes, 0 no buffer
     Received 772830 broadcasts (771185 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 771185 multicast, 0 pause input
     0 input packets with dribble condition detected
     612223943 packets output, 536662408908 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     167 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
               0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet5/0/23 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00ea.bdc4.9aa6 (bia 00ea.bdc4.9aa6)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 2y12w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     30 packets input, 12448 bytes, 0 no buffer
     Received 10 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     1 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     2286 packets output, 188805 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     2 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet5/0/24 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00ea.bdc4.9aa7 (bia 00ea.bdc4.9aa7)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 2y12w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     28 packets input, 4501 bytes, 0 no buffer
     Received 10 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     659 packets output, 81981 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     2 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet5/0/25 is up, line protocol is up (connected) 
            Hardware is Gigabit Ethernet, address is 00ea.bdc4.9aa8 (bia 00ea.bdc4.9aa8)
  Description: #SwissTubes
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 00:00:00, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 1000 bits/sec, 2 packets/sec
     18364063 packets input, 1212482280 bytes, 0 no buffer
     Received 101 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     137649841 packets output, 12886277518 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet5/0/26 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 00ea.bdc4.9aa9 (bia 00ea.bdc4.9aa9)
  Description: #SwissTubes
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 00:00:00, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 1000 bits/sec, 2 packets/sec
     20152501 packets input, 1335910764 bytes, 0 no buffer
     Received 103 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     139439549 packets output, 13006029173 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet5/0/27 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 00ea.bdc4.9aaa (bia 00ea.bdc4.9aaa)
            Description: #SwissTubes
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 00:00:01, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 1000 bits/sec, 2 packets/sec
     18380816 packets input, 1213661818 bytes, 0 no buffer
     Received 97 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     137666829 packets output, 12887319424 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet5/0/28 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00ea.bdc4.9aab (bia 00ea.bdc4.9aab)
  Description: #SwissTubes
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y23w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     7464939 packets input, 491880532 bytes, 0 no buffer
     Received 370 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     1 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     50224640 packets output, 4683652716 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet5/0/29 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 00ea.bdc4.9aac (bia 00ea.bdc4.9aac)
  Description: #SwissTubes
            MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 00:00:01, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 2000 bits/sec, 2 packets/sec
     20307894 packets input, 1336918448 bytes, 0 no buffer
     Received 470 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     1 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     139600009 packets output, 13011431952 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet5/0/30 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00ea.bdc4.9aad (bia 00ea.bdc4.9aad)
  Description: #SwissTubes
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet5/0/31 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 00ea.bdc4.9aae (bia 00ea.bdc4.9aae)
  Description: #CCure jack 1283
  MTU 1500 bytes, BW 10000 Kbit/sec, DLY 1000 usec, 
               reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Half-duplex, 10Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 00:00:01, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 2952367058
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 1000 bits/sec, 2 packets/sec
     33304580 packets input, 3356398075 bytes, 0 no buffer
     Received 2445 broadcasts (0 multicasts)
     7826 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     167328913 packets output, 18506901164 bytes, 0 underruns
     5466 output errors, 7385 collisions, 2 interface resets
     2182 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet5/0/32 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00ea.bdc4.9aaf (bia 00ea.bdc4.9aaf)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 1y23w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 15114623
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     19479673 packets input, 5020403212 bytes, 0 no buffer
     Received 457 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     58207546 packets output, 54125475933 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     13 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet5/0/33 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00ea.bdc4.9ab0 (bia 00ea.bdc4.9ab0)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
            Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet5/0/34 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00ea.bdc4.9ab1 (bia 00ea.bdc4.9ab1)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y8w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 515340082
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     19100611 packets input, 2082904259 bytes, 0 no buffer
     Received 1855 broadcasts (0 multicasts)
     2 runts, 0 giants, 0 throttles 
     72 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     316924876 packets output, 36474377788 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     707 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet5/0/35 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 00ea.bdc4.9ab2 (bia 00ea.bdc4.9ab2)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
            Last input 2y14w, output 00:00:00, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 2000 bits/sec, 1 packets/sec
  5 minute output rate 2000 bits/sec, 4 packets/sec
     178172758 packets input, 46860970925 bytes, 0 no buffer
     Received 16720 broadcasts (75 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 75 multicast, 49 pause input
     0 input packets with dribble condition detected
     1052873298 packets output, 84731288622 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet5/0/36 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 00ea.bdc4.9ab3 (bia 00ea.bdc4.9ab3)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 00:00:01, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 7000 bits/sec, 10 packets/sec
  5 minute output rate 8000 bits/sec, 13 packets/sec
     7587982397 packets input, 553560918213 bytes, 0 no buffer
     Received 108628 broadcasts (539 multicasts)
     0 runts, 0 giants, 0 throttles 
     1 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 539 multicast, 48 pause input
     0 input packets with dribble condition detected
     8461456084 packets output, 621090872113 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     12442 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet5/0/37 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00ea.bdc4.9ab4 (bia 00ea.bdc4.9ab4)
  Description: #CCure Jack 1285
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 1y26w, output hang never
  Last clearing of "" counters 2y14w
            Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     32 packets input, 6338 bytes, 0 no buffer
     Received 21 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     76 packets output, 10282 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     8 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet5/0/38 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00ea.bdc4.9ab5 (bia 00ea.bdc4.9ab5)
  Description: #AP
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet5/0/39 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00ea.bdc4.9ab6 (bia 00ea.bdc4.9ab6)
  Description: #AP
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 44w0d, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
            Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     29 packets input, 10583 bytes, 0 no buffer
     Received 17 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     1 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     256 packets output, 34863 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     5 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet5/0/40 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00ea.bdc4.9ab7 (bia 00ea.bdc4.9ab7)
  Description: #AP
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet5/0/41 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00ea.bdc4.9ab8 (bia 00ea.bdc4.9ab8)
  Description: #AP
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 44w0d, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
            Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     21 packets input, 8445 bytes, 0 no buffer
     Received 9 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     1 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     254 packets output, 32602 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     2 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet5/0/42 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00ea.bdc4.9ab9 (bia 00ea.bdc4.9ab9)
  Description: #AP
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet5/0/43 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00ea.bdc4.9aba (bia 00ea.bdc4.9aba)
  Description: #AP
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 1y30w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
            5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     17 packets input, 3274 bytes, 0 no buffer
     Received 10 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     311 packets output, 49938 bytes, 0 underruns
     0 output errors, 0 collisions, 3 interface resets
     4 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet5/0/44 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 00ea.bdc4.9abb (bia 00ea.bdc4.9abb)
  Description: #AP
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 00:00:00, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 1531421250
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 3000 bits/sec, 2 packets/sec
  5 minute output rate 3015000 bits/sec, 1333 packets/sec
     1139665710 packets input, 371126386324 bytes, 0 no buffer
     Received 6193089 broadcasts (5389916 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 5389916 multicast, 0 pause input
     0 input packets with dribble condition detected
     54877847719 packets output, 17239269374140 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     4900 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet5/0/45 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 00ea.bdc4.9abc (bia 00ea.bdc4.9abc)
  Description: #AP
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 00:00:00, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 1004291749
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 1000 bits/sec, 1 packets/sec
            5 minute output rate 3020000 bits/sec, 1341 packets/sec
     712033229 packets input, 234847528175 bytes, 0 no buffer
     Received 6192809 broadcasts (5389598 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 5389598 multicast, 0 pause input
     0 input packets with dribble condition detected
     54131357667 packets output, 16404575993489 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     4939 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet5/0/46 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00ea.bdc4.9abd (bia 00ea.bdc4.9abd)
  Description: #AP
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y26w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 1405360164
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     1133916968 packets input, 288902437533 bytes, 0 no buffer
     Received 2183504 broadcasts (1772361 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 1772361 multicast, 0 pause input
     0 input packets with dribble condition detected
     19954816798 packets output, 7758375137800 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     173 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet5/0/47 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 00ea.bdc4.9abe (bia 00ea.bdc4.9abe)
  Description: #AP
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 00:00:00, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 169
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 8000 bits/sec, 8 packets/sec
               20510850 packets input, 4611875469 bytes, 0 no buffer
     Received 5349278 broadcasts (1790591 multicasts)
     0 runts, 0 giants, 0 throttles 
     2033 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 1790591 multicast, 0 pause input
     0 input packets with dribble condition detected
     687143241 packets output, 98154319652 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     3352951 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet5/0/48 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00ea.bdc4.9abf (bia 00ea.bdc4.9abf)
  Description: #AP
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y29w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 459639919
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     508672937 packets input, 163609654683 bytes, 0 no buffer
     Received 2016267 broadcasts (1636797 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 1636797 multicast, 0 pause input
     0 input packets with dribble condition detected
     16136756393 packets output, 5423635843901 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     182 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet6/0/1 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7132.5194 (bia 00b7.7132.5194)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet6/0/2 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7132.5195 (bia 00b7.7132.5195)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet6/0/3 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7132.5196 (bia 00b7.7132.5196)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet6/0/4 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7132.5197 (bia 00b7.7132.5197)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet6/0/5 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7132.5198 (bia 00b7.7132.5198)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
               0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet6/0/6 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7132.5199 (bia 00b7.7132.5199)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet6/0/7 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7132.519a (bia 00b7.7132.519a)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
               0 output buffer failures, 0 output buffers swapped out
GigabitEthernet6/0/8 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7132.519b (bia 00b7.7132.519b)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet6/0/9 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7132.519c (bia 00b7.7132.519c)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet6/0/10 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7132.519d (bia 00b7.7132.519d)
            MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet6/0/11 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7132.519e (bia 00b7.7132.519e)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet6/0/12 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7132.519f (bia 00b7.7132.519f)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
            Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet6/0/13 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 00b7.7132.51a0 (bia 00b7.7132.51a0)
  Description: CCURE
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 00:00:00, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 4000 bits/sec, 2 packets/sec
     9977689 packets input, 1620190167 bytes, 0 no buffer
     Received 14450 broadcasts (0 multicasts)
     52 runts, 0 giants, 0 throttles 
     459 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 2608 pause input
     0 input packets with dribble condition detected
     67798024 packets output, 8494216901 bytes, 0 underruns
     0 output errors, 0 collisions, 4 interface resets
     9358 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet6/0/14 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7132.51a1 (bia 00b7.7132.51a1)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
            input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet6/0/15 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7132.51a2 (bia 00b7.7132.51a2)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet6/0/16 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7132.51a3 (bia 00b7.7132.51a3)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
            Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet6/0/17 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7132.51a4 (bia 00b7.7132.51a4)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet6/0/18 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7132.51a5 (bia 00b7.7132.51a5)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet6/0/19 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7132.51a6 (bia 00b7.7132.51a6)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet6/0/20 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 00b7.7132.51a7 (bia 00b7.7132.51a7)
  Description: Wireless AP
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 00:00:00, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 948991801
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 6000 bits/sec, 3 packets/sec
            5 minute output rate 3036000 bits/sec, 1366 packets/sec
     985205554 packets input, 289351898870 bytes, 0 no buffer
     Received 6594167 broadcasts (6425951 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 6425951 multicast, 0 pause input
     0 input packets with dribble condition detected
     48571446192 packets output, 15070674693444 bytes, 0 underruns
     0 output errors, 0 collisions, 3 interface resets
     156129 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet6/0/21 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7132.51a8 (bia 00b7.7132.51a8)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet6/0/22 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 00b7.7132.51a9 (bia 00b7.7132.51a9)
  Description: Wireless AP
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 00:00:00, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 452908913
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 10000 bits/sec, 1 packets/sec
  5 minute output rate 3072000 bits/sec, 1370 packets/sec
     680092645 packets input, 309726186826 bytes, 0 no buffer
               Received 6524755 broadcasts (6390692 multicasts)
     0 runts, 0 giants, 0 throttles 
     2 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 6390692 multicast, 0 pause input
     0 input packets with dribble condition detected
     48596002322 packets output, 14503994096501 bytes, 0 underruns
     0 output errors, 0 collisions, 3 interface resets
     133248 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet6/0/23 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7132.51aa (bia 00b7.7132.51aa)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet6/0/24 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 00b7.7132.51ab (bia 00b7.7132.51ab)
  Description: Wireless AP
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 00:00:00, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 812274545
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 941000 bits/sec, 171 packets/sec
  5 minute output rate 6020000 bits/sec, 1724 packets/sec
     1285499386 packets input, 848928977263 bytes, 0 no buffer
     Received 6524096 broadcasts (6390534 multicasts)
     0 runts, 0 giants, 0 throttles 
               3 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 6390534 multicast, 0 pause input
     0 input packets with dribble condition detected
     49327563421 packets output, 15130490440669 bytes, 0 underruns
     0 output errors, 0 collisions, 3 interface resets
     133017 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet6/0/25 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7132.51ac (bia 00b7.7132.51ac)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet6/0/26 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7132.51ad (bia 00b7.7132.51ad)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet6/0/27 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7132.51ae (bia 00b7.7132.51ae)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet6/0/28 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7132.51af (bia 00b7.7132.51af)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 44w0d, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     28 packets input, 5501 bytes, 0 no buffer
     Received 10 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     530 packets output, 63017 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     2 unknown protocol drops
               0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet6/0/29 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7132.51b0 (bia 00b7.7132.51b0)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet6/0/30 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7132.51b1 (bia 00b7.7132.51b1)
  MTU 1500 bytes, BW 10000 Kbit/sec, DLY 1000 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y32w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 82376932
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     496748659 packets input, 380872770129 bytes, 0 no buffer
     Received 887493 broadcasts (137936 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 137936 multicast, 0 pause input
     0 input packets with dribble condition detected
     719617057 packets output, 474946250603 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     147280 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
          GigabitEthernet6/0/31 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7132.51b2 (bia 00b7.7132.51b2)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y32w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 82505235
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     735967993 packets input, 562196740747 bytes, 0 no buffer
     Received 1234138 broadcasts (175229 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 175229 multicast, 0 pause input
     0 input packets with dribble condition detected
     944440207 packets output, 630387656961 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     214513 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet6/0/32 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7132.51b3 (bia 00b7.7132.51b3)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet6/0/33 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7132.51b4 (bia 00b7.7132.51b4)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
               reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y32w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 142556275
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     786882073 packets input, 579470978243 bytes, 0 no buffer
     Received 1827946 broadcasts (685016 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 685016 multicast, 0 pause input
     0 input packets with dribble condition detected
     1002048869 packets output, 660934576265 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     289151 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet6/0/34 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7132.51b5 (bia 00b7.7132.51b5)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y32w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 103400047
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     756775287 packets input, 529263739209 bytes, 0 no buffer
     Received 1318736 broadcasts (184572 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 184572 multicast, 1 pause input
     0 input packets with dribble condition detected
     961153239 packets output, 605457977326 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     210119 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet6/0/35 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7132.51b6 (bia 00b7.7132.51b6)
  MTU 1500 bytes, BW 10000 Kbit/sec, DLY 1000 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
            Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 1y32w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 22286326
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     381567113 packets input, 266136496858 bytes, 0 no buffer
     Received 355432 broadcasts (40807 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 40807 multicast, 0 pause input
     0 input packets with dribble condition detected
     609978109 packets output, 395093118262 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     46642 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet6/0/36 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7132.51b7 (bia 00b7.7132.51b7)
  MTU 1500 bytes, BW 10000 Kbit/sec, DLY 1000 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 1y32w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 180778765
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     431915805 packets input, 270818819816 bytes, 0 no buffer
     Received 673063 broadcasts (115916 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 115916 multicast, 0 pause input
     0 input packets with dribble condition detected
     574756637 packets output, 431701351487 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     149153 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet6/0/37 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7132.51b8 (bia 00b7.7132.51b8)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
            Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet6/0/38 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7132.51b9 (bia 00b7.7132.51b9)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet6/0/39 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7132.51ba (bia 00b7.7132.51ba)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet6/0/40 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7132.51bb (bia 00b7.7132.51bb)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 1y32w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 63856016
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     739096533 packets input, 545751116065 bytes, 0 no buffer
     Received 2096995 broadcasts (1053935 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 1053935 multicast, 0 pause input
     0 input packets with dribble condition detected
     978977587 packets output, 634670521068 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     143049 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet6/0/41 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7132.51bc (bia 00b7.7132.51bc)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet6/0/42 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7132.51bd (bia 00b7.7132.51bd)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet6/0/43 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7132.51be (bia 00b7.7132.51be)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet6/0/44 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7132.51bf (bia 00b7.7132.51bf)
  MTU 1500 bytes, BW 10000 Kbit/sec, DLY 1000 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y31w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 52239276
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     760861854 packets input, 580050006888 bytes, 0 no buffer
     Received 1999361 broadcasts (1039880 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 1039880 multicast, 0 pause input
     0 input packets with dribble condition detected
     987541328 packets output, 645282303266 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     188031 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet6/0/45 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7132.51c0 (bia 00b7.7132.51c0)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y31w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 195281939
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     682807897 packets input, 500539199810 bytes, 0 no buffer
     Received 1947166 broadcasts (958019 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 958019 multicast, 0 pause input
               0 input packets with dribble condition detected
     918729092 packets output, 611332772785 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     192043 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet6/0/46 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7132.51c1 (bia 00b7.7132.51c1)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 1y30w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     4671569 packets input, 1056940228 bytes, 0 no buffer
     Received 700203 broadcasts (247382 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 247382 multicast, 0 pause input
     0 input packets with dribble condition detected
     225762869 packets output, 27388654312 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     72 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet6/0/47 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 00b7.7132.51c2 (bia 00b7.7132.51c2)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 2y14w, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     200409 packets input, 184849736 bytes, 0 no buffer
     Received 651 broadcasts (209 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 209 multicast, 0 pause input
     0 input packets with dribble condition detected
     234169 packets output, 193742222 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
               113 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet6/0/48 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 00b7.7132.51c3 (bia 00b7.7132.51c3)
  Description: #UPS
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 2y14w, output 00:00:01, output hang never
  Last clearing of "" counters 2y14w
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 117486561
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 2000 bits/sec, 3 packets/sec
     44497892 packets input, 5763093292 bytes, 0 no buffer
     Received 519442 broadcasts (394993 multicasts)
     173 runts, 0 giants, 0 throttles 
     1 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 394993 multicast, 0 pause input
     0 input packets with dribble condition detected
     277895578 packets output, 27381143898 bytes, 0 underruns
     865 output errors, 207 collisions, 2 interface resets
     1 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out""",
 'show inventory':"""NAME: "Chassis", DESCR: "Cisco Catalyst 9400 Series 7 Slot Chassis"
PID: C9407R            , VID: V01  , SN: FXS2220Q0DD

NAME: "Slot 1 - Linecard", DESCR: "Cisco Catalyst 9400 Series 48-Port UPOE 10/100/1000 (RJ-45)"
PID: C9400-LC-48U      , VID: V02  , SN: JAE22320ENW

NAME: "Slot 2 - Linecard", DESCR: "Cisco Catalyst 9400 Series 48-Port UPOE 10/100/1000 (RJ-45)"
PID: C9400-LC-48U      , VID: V02  , SN: JAE22320EQN

NAME: "Slot 5 - Linecard", DESCR: "Cisco Catalyst 9400 Series 48-Port UPOE 10/100/1000 (RJ-45)"
PID: C9400-LC-48U      , VID: V02  , SN: JAE2232099T

NAME: "Slot 6 - Linecard", DESCR: "Cisco Catalyst 9400 Series 48-Port UPOE 10/100/1000 (RJ-45)"
PID: C9400-LC-48U      , VID: V02  , SN: JAE2233047J

NAME: "Slot 3 - Supervisor", DESCR: "Cisco Catalyst 9400 Series Supervisor 1 Module"
PID: C9400-SUP-1       , VID: V02  , SN: JAE22310B1U

NAME: "TenGigabitEthernet3/0/1", DESCR: "SFP+ 10GBASE-SR"
PID: SFP-10G-SR          , VID: A    , SN: FNS154210U3     

NAME: "TenGigabitEthernet3/0/2", DESCR: "SFP+ 10GBASE-SR"
PID: SFP-10G-SR          , VID: A    , SN: FNS20460089     

NAME: "Power Supply Module 1", DESCR: "Cisco Catalyst 9400 Series 3200W AC Power Supply"
PID: C9400-PWR-3200AC  , VID: V01  , SN: DTM222801LL

NAME: "Power Supply Module 2", DESCR: "Cisco Catalyst 9400 Series 3200W AC Power Supply"
PID: C9400-PWR-3200AC  , VID: V01  , SN: DTM222801GB

NAME: "Fan Tray", DESCR: "Cisco Catalyst 9400 Series 7 Slot Chassis Fan Tray"
PID: C9407-FAN         , VID: V01  , SN: FXS2220Q1YG

""",
 'show interface counters':"""Port            InOctets    InUcastPkts    InMcastPkts    InBcastPkts 
Gi1/0/1             7205              1              0              2 
Gi1/0/2                0              0              0              0 
Gi1/0/3     282950597910      431164800         759258         400051 
Gi1/0/4     445896392219      581391984         987423         969098 
Gi1/0/5     332747337474      509195162        1279815         819199 
Gi1/0/6      17426227226       87640448         707555         976310 
Gi1/0/7     309097528568      494632118         898513         146363 
Gi1/0/8      10338366724       57002307         728716          66850 
Gi1/0/9     483586730478      751246639         792538         891656 
Gi1/0/10    540086875463      843825492         876980         139115 
Gi1/0/11      9605387165       63799778         717157          59574 
Gi1/0/12     16042755965      105305770         709819          54855 
Gi1/0/13    403907553255      888355466        5044150         422039 
Gi1/0/14               0              0              0              0 
Gi1/0/15     13296155452       80729804         717852          38642 
Gi1/0/16     12866539369       84265845         715628          22944 
Gi1/0/17     16356244814      106463554         709617        1044302 
Gi1/0/18    539814711188      746682901         771124         144570 
Gi1/0/19     13280543378       85414368         710376          20218 
Gi1/0/20     12399081901       91023065         715470          57776 
Gi1/0/21     13819703192       81503208         718569          47524 
Gi1/0/22    500028372431      687719999         931469         132018 
Gi1/0/23     15432978087      102855601         709910          55097 
Gi1/0/24    146522085023      198886388          52803         291251 
Gi1/0/25          393048             77            386             57 
Gi1/0/26           16592              1              0             64 
Gi1/0/27    434836667048      603140982         273243         244977 
Gi1/0/28    495136047484      623220754          92518         120333 
Gi1/0/29     10422697154       85409292         728727           1924 
Gi1/0/30      9895692934       62233596         729342          69342 
Gi1/0/31    559070664072      737554392         932584         934298 
Gi1/0/32    407149514047      545914081         898871         723942 
Gi1/0/33      1918586491        8235194          25264          74377 
Gi1/0/34    481538055630      890689773        1297895         323869 
Gi1/0/35      7227674404       52066010         728624          74822 
Gi1/0/36      2372533668       12772815          27394           9503 
Gi1/0/37           22557             32              0             32 
Gi1/0/38            4675             20              0             10 
Gi1/0/39    379535359673      600538769         890286         627170 
Gi1/0/40    469518131835      605331815         880024         728944 
Gi1/0/41    425810107584      589946041         806420         500279 
Gi1/0/42      2247044039        4476223          38433         126484 
Gi1/0/43      2980559420       15339957          72634         198636 
Gi1/0/44    270492346397      396968015         907214         120815 
Gi1/0/45    564550782375      798317665         786103         989649 
Gi1/0/46    324246015515      423186321         750545         161305 
Gi1/0/47      7407708921       51195973         728442          39845 
Gi1/0/48    549604520769      825705787         821576         921535 
Gi2/0/1                0              0              0              0 
Gi2/0/2                0              0              0              0 
Gi2/0/3            15830              7              0             12 
Gi2/0/4          1048083             21           1536             19 
Gi2/0/5   23479100456306    17819045791           3427            321 
Gi2/0/6   18120841599205    14215843281           4359            281 
Gi2/0/7   26499316465696    19820647074           1238            177 
Gi2/0/8        271260601        1990538              0         320664 
Gi2/0/9        210241536        1741337              8         316233 
          
Port            InOctets    InUcastPkts    InMcastPkts    InBcastPkts 
Gi2/0/10               0              0              0              0 
Gi2/0/11       158273500        1412711             16         279284 
Gi2/0/12       155700765        1369958             76         246266 
Gi2/0/13      1618768053        9494110        1300810        1925847 
Gi2/0/14           14482             11              0             21 
Gi2/0/15       205339088        1794319             20         333458 
Gi2/0/16               0              0              0              0 
Gi2/0/17       238597018        1846918         136089         247454 
Gi2/0/18        65474500         882544             14           6175 
Gi2/0/19               0              0              0              0 
Gi2/0/20       103827823        1198068              0          23683 
Gi2/0/21        96813939        1117786              0          21755 
Gi2/0/22        96260458        1111568              0          21750 
Gi2/0/23        93104734        1106041              0          20913 
Gi2/0/24       102932862        1144397              0          20168 
Gi2/0/25            8535             12              0             10 
Gi2/0/26            7971              6              0              8 
Gi2/0/27        81957315         943018              0          19291 
Gi2/0/28     14267557876      222587799              0          19717 
Gi2/0/29       120005840        1242299              0          45150 
Gi2/0/30        92217407        1083834              0          22381 
Gi2/0/31        80173388         939746              0          19884 
Gi2/0/32        92221498        1074883              0          21750 
Gi2/0/33      2393253720       24091999          20024          27754 
Gi2/0/34       172245888        1521431             12         262438 
Gi2/0/35       203025459        1787686              8         314132 
Gi2/0/36       262912753        2263488         191208         304507 
Gi2/0/37               0              0              0              0 
Gi2/0/38   7396916208025     5904286501           3853            338 
Gi2/0/39       341247505        2627296         274444         407538 
Gi2/0/40       117273532        1359617              0          27098 
Gi2/0/41       294090643        2563601              0         329456 
Gi2/0/42       101660843        1162900              0          23991 
Gi2/0/43       209949913        1834941              8         291270 
Gi2/0/44       123580305        1085597              0          89043 
Gi2/0/45       184721221        1716945              0         266717 
Gi2/0/46        76840017         896261              0          18095 
Gi2/0/47       303517219        2942736              0         328686 
Gi2/0/48        92465431        1071494              0          21075 
Te3/0/1   40552533372109    37292551288    53759686217     4232640178 
Te3/0/2    4756556049949     7101406045     2405066536     4167010596 
Te3/0/3                0              0              0              0 
Te3/0/4                0              0              0              0 
Te3/0/5                0              0              0              0 
Te3/0/6                0              0              0              0 
Te3/0/7                0              0              0              0 
Te3/0/8                0              0              0              0 
Fo3/0/9                0              0              0              0 
Fo3/0/10               0              0              0              0 
Gi5/0/1            92734           1185              0              7 
Gi5/0/2                0              0              0              0 
Gi5/0/3                0              0              0              0 
Gi5/0/4                0              0              0              0 
Gi5/0/5                0              0              0              0 
Gi5/0/6                0              0              0              0 
Gi5/0/7                0              0              0              0 
Gi5/0/8                0              0              0              0 
Gi5/0/9                0              0              0              0 
Gi5/0/10               0              0              0              0 
          
Port            InOctets    InUcastPkts    InMcastPkts    InBcastPkts 
Gi5/0/11               0              0              0              0 
Gi5/0/12               0              0              0              0 
Gi5/0/13           90076              1              0            304 
Gi5/0/14               0              0              0              0 
Gi5/0/15               0              0              0              0 
Gi5/0/16               0              0              0              0 
Gi5/0/17               0              0              0              0 
Gi5/0/18           31628             56              0             30 
Gi5/0/19            1902              7              0              5 
Gi5/0/20               0              0              0              0 
Gi5/0/21      5239954099       76114014             36           1107 
Gi5/0/22     26766162520      384132488         771185           1645 
Gi5/0/23           12448             20              0             10 
Gi5/0/24            4501             18              0             10 
Gi5/0/25      1212482542       18363966              0            101 
Gi5/0/26      1335911026       20152402              0            103 
Gi5/0/27      1213662080       18380723              0             97 
Gi5/0/28       491880532        7464569              0            370 
Gi5/0/29      1336918646       20307427              0            470 
Gi5/0/30               0              0              0              0 
Gi5/0/31      3356398145       33302136              0           2445 
Gi5/0/32      5020403212       19479216              0            457 
Gi5/0/33               0              0              0              0 
Gi5/0/34      2082904259       19098756              0           1855 
Gi5/0/35     46860974002      178156057             75          16645 
Gi5/0/36    553560930380     7587873907            539         108089 
Gi5/0/37            6338             11              0             21 
Gi5/0/38               0              0              0              0 
Gi5/0/39           10583             12              0             17 
Gi5/0/40               0              0              0              0 
Gi5/0/41            8445             12              0              9 
Gi5/0/42               0              0              0              0 
Gi5/0/43            3274              7              0             10 
Gi5/0/44    371126402455     1133472698        5389917         803173 
Gi5/0/45    234847528175      705840420        5389598         803211 
Gi5/0/46    288902437533     1131733464        1772361         411143 
Gi5/0/47      4611875469       15161572        1790591        3558687 
Gi5/0/48    163609654683      506656670        1636797         379470 
Gi6/0/1                0              0              0              0 
Gi6/0/2                0              0              0              0 
Gi6/0/3                0              0              0              0 
Gi6/0/4                0              0              0              0 
Gi6/0/5                0              0              0              0 
Gi6/0/6                0              0              0              0 
Gi6/0/7                0              0              0              0 
Gi6/0/8                0              0              0              0 
Gi6/0/9                0              0              0              0 
Gi6/0/10               0              0              0              0 
Gi6/0/11               0              0              0              0 
Gi6/0/12               0              0              0              0 
Gi6/0/13      1620190167        9963239              0          14450 
Gi6/0/14               0              0              0              0 
Gi6/0/15               0              0              0              0 
Gi6/0/16               0              0              0              0 
Gi6/0/17               0              0              0              0 
Gi6/0/18               0              0              0              0 
Gi6/0/19               0              0              0              0 
Gi6/0/20    289351898870      978611387        6425951         168216 
Gi6/0/21               0              0              0              0 
          
Port            InOctets    InUcastPkts    InMcastPkts    InBcastPkts 
Gi6/0/22    309726186826      673567890        6390692         134063 
Gi6/0/23               0              0              0              0 
Gi6/0/24    848928977263     1278975290        6390534         133562 
Gi6/0/25               0              0              0              0 
Gi6/0/26               0              0              0              0 
Gi6/0/27               0              0              0              0 
Gi6/0/28            5501             18              0             10 
Gi6/0/29               0              0              0              0 
Gi6/0/30    380872770129      495861166         137936         749557 
Gi6/0/31    562196740747      734733855         175229        1058909 
Gi6/0/32               0              0              0              0 
Gi6/0/33    579470978243      785054127         685016        1142930 
Gi6/0/34    529263739209      755456551         184572        1134164 
Gi6/0/35    266136496858      381211681          40807         314625 
Gi6/0/36    270818819816      431242742         115916         557147 
Gi6/0/37               0              0              0              0 
Gi6/0/38               0              0              0              0 
Gi6/0/39               0              0              0              0 
Gi6/0/40    545751116065      736999538        1053935        1043060 
Gi6/0/41               0              0              0              0 
Gi6/0/42               0              0              0              0 
Gi6/0/43               0              0              0              0 
Gi6/0/44    580050006888      758862493        1039880         959481 
Gi6/0/45    500539199810      680860731         958019         989147 
Gi6/0/46      1056940228        3971366         247382         452821 
Gi6/0/47       184849736         199758            209            442 
Gi6/0/48      5763093292       43978450         394993         124449 

Port           OutOctets   OutUcastPkts   OutMcastPkts   OutBcastPkts 
Gi1/0/1            11995              1            118              0 
Gi1/0/2                0              0              0              0 
Gi1/0/3     415614822331      465786310       93581341      119138852 
Gi1/0/4     513593227215      594719760       90445389      117027279 
Gi1/0/5     401430383611      515408287       91117943      117689546 
Gi1/0/6      96341616816      116419585       90721344      117018134 
Gi1/0/7     387369920144      497852986       93445840      119392515 
Gi1/0/8      61128833167       68789261       93363032      119340418 
Gi1/0/9     683583423802      770788305       93005860      117483933 
Gi1/0/10    831891959232      909347095       93214795      119268445 
Gi1/0/11     72322477690       81108469       91699635      118458929 
Gi1/0/12    143986062528      157788006       92108565      118712602 
Gi1/0/13    912502606152     1013547891      301114669      239127090 
Gi1/0/14               0              0              0              0 
Gi1/0/15     69357893116       98231896       91699472      118481472 
Gi1/0/16     88429087676       99648114       91705896      118503343 
Gi1/0/17     69855913760      121863512       90720771      116951106 
Gi1/0/18    673342985081      756225989       91651163      118381960 
Gi1/0/19    130525968066      132610512       92108203      118746864 
Gi1/0/20    120974316641      123702213       91705865      118468729 
Gi1/0/21     78996987892      105696533       91698844      118473430 
Gi1/0/22    597279081937      703201847       94201837      119776067 
Gi1/0/23    139421732114      152512025       91687851      118451889 
Gi1/0/24    215521100185      218057471       73163819      105678334 
Gi1/0/25         6607012           2705          43086           5890 
Gi1/0/26          556471            442           1171           4545 
Gi1/0/27    528530228095      622529150       93430936      118201123 
Gi1/0/28    524455556447      615514873       91664389      118405814 
Gi1/0/29     86193927787       98973347       94346983      119846414 
Gi1/0/30    107879656159       99087212       94346358      119778067 
          
Port           OutOctets   OutUcastPkts   OutMcastPkts   OutBcastPkts 
Gi1/0/31    640877438391      740723491       92659260      118228758 
Gi1/0/32    479520933563      567744122       96912192      120601723 
Gi1/0/33     34395878799       17086119       94353295      119784044 
Gi1/0/34    783680136903      917149053       96273193      120846914 
Gi1/0/35     66942106278       65503258       94346298      119772358 
Gi1/0/36     37694541588       21819608       94353623      119851928 
Gi1/0/37           77841             59            389            156 
Gi1/0/38          155457             44            890            374 
Gi1/0/39    578049825361      622233781       93455635      118904956 
Gi1/0/40    563855926426      645588114       98787897      121860907 
Gi1/0/41    512186738194      607578198       93533374      119031718 
Gi1/0/42     32751235834       14580591       96465215      120437863 
Gi1/0/43     37427183155       24423520      101103418      123753231 
Gi1/0/44    346860561746      406737141       95581581      120522409 
Gi1/0/45    791864287456      854393343       93562051      118541845 
Gi1/0/46    366850843466      429302507       79363419      111258299 
Gi1/0/47     65903975398       65615041       93619525      119492915 
Gi1/0/48    801189801519      881831488       91600590      117605679 
Gi2/0/1                0              0              0              0 
Gi2/0/2                0              0              0              0 
Gi2/0/3            67742             30             92            695 
Gi2/0/4        791192103         158397        1176931        9388852 
Gi2/0/5      67640031720      609910132      119474116       17056270 
Gi2/0/6      66780854671      598994603      118730146       16995647 
Gi2/0/7      66870968002      610807867      118299623        7667694 
Gi2/0/8      43028306066       11083998       55940035      493395693 
Gi2/0/9      41000273418        9189304       56529339      503000239 
Gi2/0/10               0              0              0              0 
Gi2/0/11     36661876475        7769408       50323340      450672124 
Gi2/0/12     31562924610        6910785       42972433      388231401 
Gi2/0/13    237980631154       32778042      293630973     1946527191 
Gi2/0/14         2567636           1942           5185          24867 
Gi2/0/15     41046313311        9308095       56549900      503036789 
Gi2/0/16               0              0              0              0 
Gi2/0/17     36232727261        9663732       49633329      413364270 
Gi2/0/18     34077933279        7070271       49730705      413360641 
Gi2/0/19               0              0              0              0 
Gi2/0/20     23688022030        5244425       33323698      282923801 
Gi2/0/21     21184975744        5344352       31024198      246942825 
Gi2/0/22     20947921257        5061083       30895814      244073481 
Gi2/0/23     20348285105        5042240       29520774      233091157 
Gi2/0/24     19518392696        4849725       28750809      224863758 
Gi2/0/25           31819             17             52            303 
Gi2/0/26           37736             20             38            430 
Gi2/0/27     18205227192        4221021       27160313      212517234 
Gi2/0/28     32647840491      226055728       27375427      212744663 
Gi2/0/29     20765872237        5529242       29991240      237657465 
Gi2/0/30     21697637348        4879065       31273665      254807085 
Gi2/0/31     18687260412        4661243       27672779      216865528 
Gi2/0/32     21568811299        4473398       30476237      255710913 
Gi2/0/33     43648110092       32021956       48491696      315799602 
Gi2/0/34     38364277863        9291926       52665263      453155717 
Gi2/0/35     41273591173        9304502       56909098      506017333 
Gi2/0/36     49817160893       16549749       53812655      464407546 
Gi2/0/37               0              0              0              0 
Gi2/0/38     79805661392      822737113       74257093        6233382 
Gi2/0/39     43807913606       11614407       55772401      493859395 
Gi2/0/40     27451640210        6089358       38459538      329192840 
Gi2/0/41     41129223882       11677751       53060480      452270919 
          
Port           OutOctets   OutUcastPkts   OutMcastPkts   OutBcastPkts 
Gi2/0/42     29315282747        5848430       40791191      357094323 
Gi2/0/43     37844585182        9000068       53183887      460035736 
Gi2/0/44     20165296779        4815295       29741922      235890404 
Gi2/0/45     39121021410        9596377       53068747      452360818 
Gi2/0/46     16683666518        3867382       24939165      190964577 
Gi2/0/47     42018391802       12338375       53072685      452350720 
Gi2/0/48     20124781900        4866554       29528097      233462710 
Te3/0/1   87710072366300    88120785951      137777144       33855702 
Te3/0/2    3135133642828     3529657170      119989912        1941343 
Te3/0/3                0              0              0              0 
Te3/0/4                0              0              0              0 
Te3/0/5                0              0              0              0 
Te3/0/6                0              0              0              0 
Te3/0/7                0              0              0              0 
Te3/0/8                0              0              0              0 
Fo3/0/9                0              0              0              0 
Fo3/0/10               0              0              0              0 
Gi5/0/1           600271           1254           2765           1821 
Gi5/0/2                0              0              0              0 
Gi5/0/3                0              0              0              0 
Gi5/0/4                0              0              0              0 
Gi5/0/5                0              0              0              0 
Gi5/0/6                0              0              0              0 
Gi5/0/7                0              0              0              0 
Gi5/0/8                0              0              0              0 
Gi5/0/9                0              0              0              0 
Gi5/0/10               0              0              0              0 
Gi5/0/11               0              0              0              0 
Gi5/0/12               0              0              0              0 
Gi5/0/13          686293            112           3763           2361 
Gi5/0/14               0              0              0              0 
Gi5/0/15               0              0              0              0 
Gi5/0/16               0              0              0              0 
Gi5/0/17               0              0              0              0 
Gi5/0/18          201158            122           1113            492 
Gi5/0/19           36993             13            137            184 
Gi5/0/20               0              0              0              0 
Gi5/0/21     98879356013      100473953      105235996       59693024 
Gi5/0/22    536662408908      455862477      102336589       54024877 
Gi5/0/23          188805             95            284           1907 
Gi5/0/24           81981             32            214            413 
Gi5/0/25     12886279783       27298617      105591307        4759939 
Gi5/0/26     13006031052       29088259      105591395        4759916 
Gi5/0/27     12887321303       27315781      105591124        4759945 
Gi5/0/28      4683652716       11565538       37826363         832739 
Gi5/0/29     13011433767       29249279      105591209        4759541 
Gi5/0/30               0              0              0              0 
Gi5/0/31     18506903231       34214528      128157692        4956712 
Gi5/0/32     54125475933       44495879        8408630        5303037 
Gi5/0/33               0              0              0              0 
Gi5/0/34     36474377788       18913298      145197239      152814339 
Gi5/0/35     84731292683      182925939      160795216      709152190 
Gi5/0/36    621090884307     7591933342      160795271      708727637 
Gi5/0/37           10282              6             66              4 
Gi5/0/38               0              0              0              0 
Gi5/0/39           34863             22            176             58 
Gi5/0/40               0              0              0              0 
Gi5/0/41           32602             17            162             75 
Gi5/0/42               0              0              0              0 
          
Port           OutOctets   OutUcastPkts   OutMcastPkts   OutBcastPkts 
Gi5/0/43           49938             15            194            102 
Gi5/0/44  17239273894331     1766037638    52417632499      694193770 
Gi5/0/45  16404580479882     1036095473    52400045029      695233219 
Gi5/0/46   7758375137800     2084240242    17794021423       76555133 
Gi5/0/47     98154330116       13148579      410070232      263924508 
Gi5/0/48   5423635843901      712483320    15352704595       71568478 
Gi6/0/1                0              0              0              0 
Gi6/0/2                0              0              0              0 
Gi6/0/3                0              0              0              0 
Gi6/0/4                0              0              0              0 
Gi6/0/5                0              0              0              0 
Gi6/0/6                0              0              0              0 
Gi6/0/7                0              0              0              0 
Gi6/0/8                0              0              0              0 
Gi6/0/9                0              0              0              0 
Gi6/0/10               0              0              0              0 
Gi6/0/11               0              0              0              0 
Gi6/0/12               0              0              0              0 
Gi6/0/13      8494216901       11210783       54876554        1710687 
Gi6/0/14               0              0              0              0 
Gi6/0/15               0              0              0              0 
Gi6/0/16               0              0              0              0 
Gi6/0/17               0              0              0              0 
Gi6/0/18               0              0              0              0 
Gi6/0/19               0              0              0              0 
Gi6/0/20  15070674693444     1555818898    46333846762      681780532 
Gi6/0/21               0              0              0              0 
Gi6/0/22  14503994096501      908678451    47000799038      686524833 
Gi6/0/23               0              0              0              0 
Gi6/0/24  15130490440669     1648912072    46996861812      681789537 
Gi6/0/25               0              0              0              0 
Gi6/0/26               0              0              0              0 
Gi6/0/27               0              0              0              0 
Gi6/0/28           63017             63            274            193 
Gi6/0/29               0              0              0              0 
Gi6/0/30    474946250603      510265556       91592333      117759168 
Gi6/0/31    630387656961      735401225       91571062      117467920 
Gi6/0/32               0              0              0              0 
Gi6/0/33    660934576265      793607415       91060512      117380942 
Gi6/0/34    605457977326      752218658       91557358      117377223 
Gi6/0/35    395093118262      400083110       91689942      118205057 
Gi6/0/36    431701351487      474126624       46803571       53826442 
Gi6/0/37               0              0              0              0 
Gi6/0/38               0              0              0              0 
Gi6/0/39               0              0              0              0 
Gi6/0/40    634670521068      772112069       90747158      116118360 
Gi6/0/41               0              0              0              0 
Gi6/0/42               0              0              0              0 
Gi6/0/43               0              0              0              0 
Gi6/0/44    645282303266      775678472       93310048      118552808 
Gi6/0/45    611332772785      706814422       93391586      118523084 
Gi6/0/46     27388654312       10009522       95558638      120194709 
Gi6/0/47       193742222         202051           7515          24603 
Gi6/0/48     27381143898       54460359      202479467       20955752 """,
 'show cdp nei detail':"""-------------------------
Device ID: ap-0525-1-1438
Entry address(es): 
  IP address: 172.20.85.220
  IPv6 address: FE80::72EA:1AFF:FEE3:9270  (link-local)
Platform: cisco AIR-AP1815W-B-K9,  Capabilities: Router Trans-Bridge 
Interface: GigabitEthernet6/0/24,  Port ID (outgoing port): GigabitEthernet0
Holdtime : 140 sec

Version :
Cisco AP Software, ap1g5-k9w8 Version: 8.5.151.0
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 2014-2015 by Cisco Systems, Inc.

advertisement version: 2
Duplex: full
Power drawn: 8.600 Watts
Power request id: 46341, Power management id: 4
Power request levels are:8600 0 0 0 0 
Management address(es): 
  IP address: 172.20.85.220

-------------------------
Device ID: ap-0525-1-1240
Entry address(es): 
  IP address: 172.20.96.70
  IPv6 address: FE80::A2B4:39FF:FE87:B71E  (link-local)
Platform: cisco AIR-AP2802I-B-K9,  Capabilities: Router Trans-Bridge 
Interface: GigabitEthernet5/0/45,  Port ID (outgoing port): GigabitEthernet0
Holdtime : 129 sec

Version :
Cisco AP Software, ap3g3-k9w8 Version: 8.5.151.0
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 2014-2015 by Cisco Systems, Inc.

advertisement version: 2
Duplex: full
Management address(es): 
  IP address: 172.20.96.70

-------------------------
Device ID: ap-0525-1-1412
Entry address(es): 
  IP address: 172.20.96.109
  IPv6 address: FE80::2EE:ABFF:FE3F:7FA8  (link-local)
Platform: cisco AIR-AP1815W-B-K9,  Capabilities: Router Trans-Bridge 
Interface: GigabitEthernet6/0/22,  Port ID (outgoing port): GigabitEthernet0
Holdtime : 145 sec

Version :
Cisco AP Software, ap1g5-k9w8 Version: 8.5.151.0
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 2014-2015 by Cisco Systems, Inc.

advertisement version: 2
Duplex: full
Power drawn: 8.600 Watts
Power request id: 42130, Power management id: 3
          Power request levels are:8600 0 0 0 0 
Management address(es): 
  IP address: 172.20.96.109

-------------------------
Device ID: ap-0525-1-1033
Entry address(es): 
  IP address: 172.20.85.159
  IPv6 address: FE80::3E51:EFF:FE3D:EFF0  (link-local)
Platform: cisco AIR-AP2802I-B-K9,  Capabilities: Router Trans-Bridge 
Interface: GigabitEthernet5/0/44,  Port ID (outgoing port): GigabitEthernet0
Holdtime : 168 sec

Version :
Cisco AP Software, ap3g3-k9w8 Version: 8.5.151.0
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 2014-2015 by Cisco Systems, Inc.

advertisement version: 2
Duplex: full
Management address(es): 
  IP address: 172.20.85.159

-------------------------
Device ID: dx2-525hosp-4659-clinical.net.utah.edu
Entry address(es): 
  IP address: 172.20.64.14
Platform: cisco C9410R,  Capabilities: Switch IGMP 
Interface: TenGigabitEthernet3/0/2,  Port ID (outgoing port): TenGigabitEthernet4/0/11
Holdtime : 140 sec

Version :
Cisco IOS Software [Everest], Catalyst L3 Switch Software (CAT9K_IOSXE), Version 16.6.4a, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2018 by Cisco Systems, Inc.
Compiled Fri 26-Oct-18 18:15 by mcpre

advertisement version: 2
VTP Management Domain: 'vtp-525hosp'
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 172.20.64.14

-------------------------
Device ID: dx1-525hosp-b244-clinical.net.utah.edu
Entry address(es): 
  IP address: 172.20.64.69
Platform: cisco C9407R,  Capabilities: Switch IGMP 
Interface: TenGigabitEthernet3/0/1,  Port ID (outgoing port): TenGigabitEthernet5/0/11
Holdtime : 162 sec

Version :
Cisco IOS Software [Everest], Catalyst L3 Switch Software (CAT9K_IOSXE), Version 16.6.3, RELEASE SOFTWARE (fc8)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2018 by Cisco Systems, Inc.
Compiled Wed 28-Feb-18 23:34 by mcpre

advertisement version: 2
          VTP Management Domain: 'vtp-525hosp'
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 172.20.64.69

-------------------------
Device ID: ap-0525-1-1039A
Entry address(es): 
  IP address: 172.20.96.185
  IPv6 address: FE80::2EE:ABFF:FE3F:7828  (link-local)
Platform: cisco AIR-AP1815W-B-K9,  Capabilities: Router Trans-Bridge 
Interface: GigabitEthernet6/0/20,  Port ID (outgoing port): GigabitEthernet0
Holdtime : 167 sec

Version :
Cisco AP Software, ap1g5-k9w8 Version: 8.5.151.0
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 2014-2015 by Cisco Systems, Inc.

advertisement version: 2
Duplex: full
Power drawn: 8.600 Watts
Power request id: 20928, Power management id: 4
Power request levels are:8600 0 0 0 0 
Management address(es): 
  IP address: 172.20.96.185


Total cdp entries displayed : 7""",
 'show module all':"""^
% Invalid input detected at '^' marker.
""",
 'show module':"""Chassis Type: C9407R              

Mod Ports Card Type                                   Model          Serial No.
---+-----+--------------------------------------+--------------+--------------
1   48   48-Port UPOE 10/100/1000 (RJ-45)            C9400-LC-48U   JAE22320ENW
2   48   48-Port UPOE 10/100/1000 (RJ-45)            C9400-LC-48U   JAE22320EQN
3   10   Supervisor 1 Module                         C9400-SUP-1    JAE22310B1U
5   48   48-Port UPOE 10/100/1000 (RJ-45)            C9400-LC-48U   JAE2232099T
6   48   48-Port UPOE 10/100/1000 (RJ-45)            C9400-LC-48U   JAE2233047J

Mod MAC addresses                    Hw   Fw           Sw                 Status
---+--------------------------------+----+------------+------------------+--------
1   00B7.7131.5930 to 00B7.7131.595F 1.1  16.6.2r[FC1]  16.06.04           ok        
2   A093.518E.587C to A093.518E.58AB 1.1  16.6.2r[FC1]  16.06.04           ok        
3   700F.6ADD.3E6C to 700F.6ADD.3E75 2.0  16.6.2r[FC1]  16.06.04           ok        
5   00EA.BDC4.9A90 to 00EA.BDC4.9ABF 1.1  16.6.2r[FC1]  16.06.04           ok        
6   00B7.7132.5194 to 00B7.7132.51C3 1.1  16.6.2r[FC1]  16.06.04           ok        

Mod Redundancy Role     Operating Redundancy Mode Configured Redundancy Mode
---+-------------------+-------------------------+---------------------------
3   Active              active                    sso                       
""",
 'show run | section snmp':"""snmp-server group CliNOCGrv3RO v3 priv read CliNOCViewRO access 70
snmp-server group CliNOCGrv3RO v3 auth context vlan- match prefix 
snmp-server group CliNOCGrv3RW v3 priv write CliNOCViewRW access 71
snmp-server view CliNOCViewRO internet included
snmp-server view CliNOCViewRW internet included
snmp-server location Bldg. 525 Room 1443
snmp-server contact BC-509406 Y-334731
snmp-server context vlan-1
snmp-server context vlan-125
snmp-server context vlan-332
snmp-server context vlan-341
snmp-server context vlan-396
snmp-server context vlan-540
snmp-server context vlan-607
snmp-server context vlan-636
snmp-server context vlan-681
snmp-server context vlan-732
snmp-server context vlan-984
snmp-server context vlan-1037
snmp-server context vlan-1209
snmp-server context vlan-1605
snmp ifmib ifindex persist""",
 'show run | in snmp':"""snmp-server group CliNOCGrv3RO v3 priv read CliNOCViewRO access 70
snmp-server group CliNOCGrv3RO v3 auth context vlan- match prefix 
snmp-server group CliNOCGrv3RW v3 priv write CliNOCViewRW access 71
snmp-server view CliNOCViewRO internet included
snmp-server view CliNOCViewRW internet included
snmp-server location Bldg. 525 Room 1443
snmp-server contact BC-509406 Y-334731
snmp-server context vlan-1
snmp-server context vlan-125
snmp-server context vlan-332
snmp-server context vlan-341
snmp-server context vlan-396
snmp-server context vlan-540
snmp-server context vlan-607
snmp-server context vlan-636
snmp-server context vlan-681
snmp-server context vlan-732
snmp-server context vlan-984
snmp-server context vlan-1037
snmp-server context vlan-1209
snmp-server context vlan-1605
snmp ifmib ifindex persist""",
 'show snmp user':"""User name: CliNONUserv3RO
Engine ID: 800000090300700F6ADD3E69
storage-type: nonvolatile	 active
Authentication Protocol: MD5
Privacy Protocol: DES
Group-name: CliNOCGrv3RW

User name: CliNONUserv3Rw
Engine ID: 800000090300700F6ADD3E69
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
    150 permit 10.71.24.17 (13806824 matches)
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
    10 permit tcp 155.98.253.0 0.0.0.255 any eq 22 (80 matches)
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
Extended IP access list IP-Adm-V4-Int-ACL-global
Extended IP access list implicit_deny
    10 deny ip any any
Extended IP access list preauth_v4
    10 permit udp any any eq domain
    20 permit tcp any any eq domain
    30 permit udp any eq bootps any
    40 permit udp any any eq bootpc
    50 permit udp any eq bootpc any
    60 deny ip any any
IPv6 access list implicit_deny_v6
    deny ipv6 any any sequence 10
IPv6 access list preauth_v6
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
logging source-interface Vlan332
logging host 172.24.29.14
logging host 10.71.24.11
logging host 155.98.253.244""",
 'show run | in logging':"""logging buffered notifications
logging console critical
logging facility local6
logging source-interface Vlan332
logging host 172.24.29.14
logging host 10.71.24.11
logging host 155.98.253.244""",
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
 All    0180.c200.0021    STATIC      CPU
 All    ffff.ffff.ffff    STATIC      CPU
   1    780c.f0bb.d492    DYNAMIC     Te3/0/1
   1    b08b.cfe2.d5a2    DYNAMIC     Te3/0/2
 332    0000.0c9f.f14c    DYNAMIC     Te3/0/1
 332    003a.9c3f.d7c1    DYNAMIC     Te3/0/1
 332    003a.9c40.0dc1    DYNAMIC     Te3/0/1
 332    00c0.b729.995b    DYNAMIC     Te3/0/1
 332    00c0.b766.84ed    DYNAMIC     Te3/0/1
 332    00c0.b768.dab8    DYNAMIC     Te3/0/1
 332    00c0.b76d.680e    DYNAMIC     Te3/0/1
 332    00c0.b774.55ff    DYNAMIC     Te3/0/1
 332    00c0.b794.5f61    DYNAMIC     Te3/0/1
 332    00c0.b7b3.9c91    DYNAMIC     Te3/0/1
 332    00c0.b7c3.f756    DYNAMIC     Te3/0/1
 332    00c0.b7c4.265b    DYNAMIC     Te3/0/1
 332    00c0.b7c9.570a    DYNAMIC     Te3/0/1
 332    00c0.b7d2.aba8    DYNAMIC     Te3/0/1
 332    00c0.b7e1.f27f    DYNAMIC     Te3/0/1
 332    00c0.b7e9.b142    DYNAMIC     Te3/0/1
 332    00c0.b7eb.4796    DYNAMIC     Te3/0/1
 332    00c0.b7f1.17eb    DYNAMIC     Te3/0/1
 332    00c0.b7f1.212e    DYNAMIC     Te3/0/1
 332    00c0.b7f1.214a    DYNAMIC     Te3/0/1
 332    00c0.b7f1.216d    DYNAMIC     Te3/0/1
 332    00c0.b7f1.21a0    DYNAMIC     Te3/0/1
 332    00c0.b7f1.21a3    DYNAMIC     Te3/0/1
 332    00c0.b7fa.064c    DYNAMIC     Gi6/0/48
 332    2829.8623.8502    DYNAMIC     Te3/0/1
 332    34ed.1bc4.2dec    DYNAMIC     Te3/0/1
 332    503d.e583.2cff    DYNAMIC     Te3/0/1
 332    700f.6add.3e45    STATIC      Vl332 
 332    7018.a722.fac9    DYNAMIC     Te3/0/1
 332    a093.51d2.5c45    DYNAMIC     Te3/0/1
 636    0000.0c9f.f27c    DYNAMIC     Te3/0/1
           636    0007.3276.768b    DYNAMIC     Te3/0/1
 636    0007.3276.d063    DYNAMIC     Te3/0/1
 636    000c.c601.b914    DYNAMIC     Te3/0/1
 636    001d.9722.03cd    DYNAMIC     Te3/0/1
 636    001d.9722.03d0    DYNAMIC     Te3/0/1
 636    0020.4afb.fe78    DYNAMIC     Te3/0/1
 636    0020.4afc.007a    DYNAMIC     Te3/0/1
 636    003a.9c3f.d7c1    DYNAMIC     Te3/0/1
 636    003a.9c40.0dc1    DYNAMIC     Te3/0/1
 636    10e7.c600.d393    DYNAMIC     Te3/0/1
 636    10e7.c608.2401    DYNAMIC     Te3/0/1
 636    1860.2424.1ed2    DYNAMIC     Te3/0/1
 636    1860.246d.a019    DYNAMIC     Te3/0/1
 636    1860.24ab.be4c    DYNAMIC     Te3/0/1
 636    3448.ed84.1e95    DYNAMIC     Te3/0/1
 636    40b0.341d.daf8    DYNAMIC     Te3/0/1
 636    40b0.3439.a539    DYNAMIC     Te3/0/1
 636    40b0.343b.ffdd    DYNAMIC     Te3/0/1
 636    40b0.343b.ffea    DYNAMIC     Te3/0/1
 636    40b0.343e.4b24    DYNAMIC     Te3/0/1
 636    40b0.343e.4b25    DYNAMIC     Te3/0/1
 636    40b0.343e.687e    DYNAMIC     Te3/0/1
 636    40b0.3441.d107    DYNAMIC     Te3/0/1
 636    40b0.3443.884d    DYNAMIC     Te3/0/1
 636    40b0.3443.8855    DYNAMIC     Te3/0/1
 636    40b0.3444.c362    DYNAMIC     Te3/0/1
 636    40b0.3444.c366    DYNAMIC     Te3/0/1
 636    40b0.3444.c37d    DYNAMIC     Te3/0/1
 636    40b0.3444.c37f    DYNAMIC     Te3/0/1
 636    40b0.3445.41bf    DYNAMIC     Te3/0/1
 636    6c2b.59c9.5cb0    DYNAMIC     Gi1/0/13
 636    6c2b.59e9.ce2d    DYNAMIC     Te3/0/1
 636    6c2b.59e9.d2df    DYNAMIC     Te3/0/1
 636    6c2b.59ea.c748    DYNAMIC     Te3/0/1
 636    6c2b.59ea.c7ca    DYNAMIC     Te3/0/1
 636    6c2b.59ea.cdb1    DYNAMIC     Te3/0/1
 636    6c2b.59ea.fda6    DYNAMIC     Te3/0/1
 636    6c2b.59eb.4653    DYNAMIC     Te3/0/1
 636    6c2b.59eb.577a    DYNAMIC     Te3/0/1
 636    6c2b.59f4.2f72    DYNAMIC     Te3/0/1
 636    6c2b.59f4.aa7d    DYNAMIC     Te3/0/1
 636    705a.0f4a.4082    DYNAMIC     Te3/0/1
 636    98e7.f42e.46e4    DYNAMIC     Te3/0/1
 636    a08c.fdc2.c9d1    DYNAMIC     Te3/0/1
 636    a08c.fdc2.c9db    DYNAMIC     Te3/0/1
 636    a08c.fdd2.70b3    DYNAMIC     Te3/0/1
 636    a08c.fdd3.0f02    DYNAMIC     Te3/0/1
 636    a08c.fdda.7c63    DYNAMIC     Te3/0/1
 636    a08c.fdda.7c66    DYNAMIC     Te3/0/1
 636    a08c.fddc.7574    DYNAMIC     Te3/0/1
 636    a08c.fddc.f38e    DYNAMIC     Te3/0/1
 636    a08c.fddc.f390    DYNAMIC     Te3/0/1
 636    a08c.fdde.d6c4    DYNAMIC     Te3/0/1
 636    a08c.fdde.e6cc    DYNAMIC     Te3/0/1
 636    a093.51d2.5c6d    DYNAMIC     Te3/0/1
 636    a0c5.f2c0.1368    DYNAMIC     Te3/0/1
 636    a4bb.6d4d.0b5e    DYNAMIC     Te3/0/1
 636    a4bb.6d4d.163d    DYNAMIC     Te3/0/1
 636    a4bb.6d4d.1919    DYNAMIC     Te3/0/1
           636    a4bb.6d4d.1c6e    DYNAMIC     Te3/0/1
 636    a4bb.6d4d.4abb    DYNAMIC     Te3/0/1
 636    a4bb.6d4d.94fb    DYNAMIC     Te3/0/1
 636    a4bb.6d4d.955a    DYNAMIC     Te3/0/1
 636    a4bb.6d4d.9653    DYNAMIC     Te3/0/1
 636    a4bb.6d4d.9950    DYNAMIC     Te3/0/1
 636    a4bb.6d4d.a248    DYNAMIC     Te3/0/1
 636    a4bb.6d4d.a324    DYNAMIC     Te3/0/1
 636    a4bb.6d4d.a442    DYNAMIC     Te3/0/1
 636    a4bb.6d4d.a48c    DYNAMIC     Te3/0/1
 636    a4bb.6d4d.a8a5    DYNAMIC     Te3/0/1
 636    a4bb.6d4d.a8a8    DYNAMIC     Te3/0/1
 636    a4bb.6d4d.c3c5    DYNAMIC     Te3/0/1
 636    a4bb.6d4d.c528    DYNAMIC     Te3/0/1
 636    a4bb.6d4d.c5b0    DYNAMIC     Te3/0/1
 636    a4bb.6d4d.c636    DYNAMIC     Te3/0/1
 636    a4bb.6d4d.c647    DYNAMIC     Te3/0/1
 636    a4bb.6d4d.c648    DYNAMIC     Te3/0/1
 636    a4bb.6d4d.d00c    DYNAMIC     Te3/0/1
 636    a4bb.6d4d.d020    DYNAMIC     Te3/0/1
 636    a4bb.6d4d.d3f8    DYNAMIC     Te3/0/1
 636    a4bb.6d4e.bd86    DYNAMIC     Te3/0/1
 636    a4bb.6d4e.d69b    DYNAMIC     Te3/0/1
 636    a4bb.6d4e.d825    DYNAMIC     Te3/0/1
 636    a4bb.6d4e.da75    DYNAMIC     Te3/0/1
 636    a4bb.6d4e.db73    DYNAMIC     Te3/0/1
 636    a4bb.6d4e.db94    DYNAMIC     Te3/0/1
 636    a4bb.6d4e.dcc2    DYNAMIC     Te3/0/1
 636    a4bb.6d4e.dcc3    DYNAMIC     Te3/0/1
 636    a4bb.6d4e.dcca    DYNAMIC     Te3/0/1
 636    a4bb.6d4e.e728    DYNAMIC     Te3/0/1
 636    a4bb.6d4e.e997    DYNAMIC     Te3/0/1
 636    a4bb.6d4e.f0c7    DYNAMIC     Te3/0/1
 636    a4bb.6d4f.6d0d    DYNAMIC     Te3/0/1
 636    a4bb.6d4f.723e    DYNAMIC     Te3/0/1
 636    a4bb.6d4f.7295    DYNAMIC     Te3/0/1
 636    a4bb.6d4f.741d    DYNAMIC     Te3/0/1
 636    a4bb.6d4f.7b8a    DYNAMIC     Te3/0/1
 636    a4bb.6d4f.8570    DYNAMIC     Te3/0/1
 636    a4bb.6d4f.8bc8    DYNAMIC     Te3/0/1
 636    a4bb.6d4f.90ff    DYNAMIC     Te3/0/1
 636    a4bb.6d4f.91bc    DYNAMIC     Te3/0/1
 636    a4bb.6d4f.9290    DYNAMIC     Te3/0/1
 636    a4bb.6d4f.9303    DYNAMIC     Te3/0/1
 636    ace2.d30f.8d50    DYNAMIC     Te3/0/1
 636    b00c.d134.70ce    DYNAMIC     Te3/0/1
 636    bce9.2fd4.8680    DYNAMIC     Te3/0/1
 636    c03e.baac.fe05    DYNAMIC     Te3/0/1
 636    c8d3.ffa1.e16b    DYNAMIC     Te3/0/1
 636    c8d3.ffa4.1dd3    DYNAMIC     Te3/0/1
 636    c8d3.ffb3.edbe    DYNAMIC     Te3/0/1
 636    c8d3.ffb3.ee04    DYNAMIC     Te3/0/1
 636    c8d3.ffb3.ee07    DYNAMIC     Te3/0/1
 636    c8d3.ffb3.ee0b    DYNAMIC     Te3/0/1
 636    c8d3.ffb3.ee10    DYNAMIC     Te3/0/1
 636    c8d3.ffb3.ee12    DYNAMIC     Te3/0/1
 636    c8d3.ffb7.f6c4    DYNAMIC     Te3/0/1
 636    c8d3.ffb7.f6d0    DYNAMIC     Te3/0/1
 636    c8d3.ffb8.ba56    DYNAMIC     Te3/0/1
           636    c8d3.ffb8.bd3c    DYNAMIC     Te3/0/1
 636    c8d3.ffb8.bd47    DYNAMIC     Te3/0/1
 636    c8d3.ffbc.424e    DYNAMIC     Te3/0/1
 636    c8d9.d209.6e5a    DYNAMIC     Te3/0/1
 636    c8f7.50d1.4de3    DYNAMIC     Te3/0/1
 636    e454.e85c.ddd4    DYNAMIC     Te3/0/1
 636    ec8e.b56e.7904    DYNAMIC     Te3/0/1
 636    ec8e.b57a.8315    DYNAMIC     Te3/0/1
 636    fc3f.db02.949a    DYNAMIC     Te3/0/1
 636    fc3f.db06.6563    DYNAMIC     Te3/0/1
 984    0000.0c9f.f3d8    DYNAMIC     Te3/0/1
 984    003a.9c3f.d7c1    DYNAMIC     Te3/0/1
 984    003a.9c40.0dc1    DYNAMIC     Te3/0/1
 984    34ed.1bc4.2dec    DYNAMIC     Te3/0/1
 984    a009.ed0c.55c2    DYNAMIC     Gi1/0/13
 984    a093.51d2.5c6d    DYNAMIC     Te3/0/1
 396    0000.0c9f.f18c    DYNAMIC     Te3/0/1
 396    0007.4d44.af5c    DYNAMIC     Te3/0/1
 396    0007.4d47.08b1    DYNAMIC     Te3/0/1
 396    0007.4d47.532e    DYNAMIC     Te3/0/1
 396    0007.4d4a.6fdc    DYNAMIC     Te3/0/1
 396    0007.4d4a.f169    DYNAMIC     Te3/0/1
 396    0007.4d4b.b37d    DYNAMIC     Te3/0/1
 396    0007.4d62.0311    DYNAMIC     Te3/0/1
 396    0007.4d66.3a5b    DYNAMIC     Te3/0/1
 396    0007.4d6e.f07d    DYNAMIC     Te3/0/1
 396    0007.4d76.144d    DYNAMIC     Te3/0/1
 396    0007.4d95.0774    DYNAMIC     Te3/0/1
 396    0007.4d95.07b2    DYNAMIC     Te3/0/1
 396    0007.4d95.3ca9    DYNAMIC     Te3/0/1
 396    0007.4d96.689c    DYNAMIC     Te3/0/1
 396    0007.4d96.bda4    DYNAMIC     Te3/0/1
 396    0007.4d96.dd4c    DYNAMIC     Te3/0/1
 396    0007.4da6.5065    DYNAMIC     Te3/0/1
 396    0007.4da6.50f6    DYNAMIC     Te3/0/1
 396    0007.4da6.6f4f    DYNAMIC     Te3/0/1
 396    0007.4da7.e2dc    DYNAMIC     Te3/0/1
 396    0007.4dad.e959    DYNAMIC     Te3/0/1
 396    000c.c601.aeb8    DYNAMIC     Te3/0/1
 396    000c.c601.aebc    DYNAMIC     Te3/0/1
 396    000c.c601.b16a    DYNAMIC     Te3/0/1
 396    000c.c601.b8da    DYNAMIC     Te3/0/1
 396    000c.c603.0e0c    DYNAMIC     Te3/0/1
 396    0011.0af0.065c    DYNAMIC     Te3/0/1
 396    0011.0af2.d149    DYNAMIC     Te3/0/1
 396    0012.7980.8869    DYNAMIC     Te3/0/1
 396    0012.7982.ac16    DYNAMIC     Te3/0/1
 396    0013.21be.cf7e    DYNAMIC     Te3/0/1
 396    0017.088e.d1d1    DYNAMIC     Te3/0/1
 396    0018.fea0.c29d    DYNAMIC     Te3/0/1
 396    001a.4b26.2d2c    DYNAMIC     Te3/0/1
 396    001b.781d.457d    DYNAMIC     Te3/0/1
 396    001b.78e6.64fe    DYNAMIC     Te3/0/1
 396    001e.0b15.fe1f    DYNAMIC     Te3/0/1
 396    0021.5a7d.d895    DYNAMIC     Te3/0/1
 396    0021.5a7d.d897    DYNAMIC     Te3/0/1
 396    0021.5a7d.d8d9    DYNAMIC     Te3/0/1
 396    0021.5a7d.d8e8    DYNAMIC     Te3/0/1
 396    0021.5a7f.1882    DYNAMIC     Te3/0/1
           396    0021.5a7f.41c7    DYNAMIC     Te3/0/1
 396    0021.5a90.111e    DYNAMIC     Te3/0/1
 396    0021.5a94.b681    DYNAMIC     Te3/0/1
 396    0023.7d84.0b14    DYNAMIC     Te3/0/1
 396    0023.7d8c.2531    DYNAMIC     Te3/0/1
 396    0023.7d8c.2587    DYNAMIC     Te3/0/1
 396    0025.b3eb.438d    DYNAMIC     Te3/0/1
 396    0025.b3f6.cd8f    DYNAMIC     Te3/0/1
 396    003a.9c3f.d7c1    DYNAMIC     Te3/0/1
 396    003a.9c40.0dc1    DYNAMIC     Te3/0/1
 396    0040.9d69.6fc4    DYNAMIC     Te3/0/1
 396    0068.eb81.1b35    DYNAMIC     Te3/0/1
 396    040e.3c0b.eb99    DYNAMIC     Te3/0/1
 396    040e.3c6c.3838    DYNAMIC     Te3/0/1
 396    040e.3ce8.1fcd    DYNAMIC     Te3/0/1
 396    082e.5fb9.3e3f    DYNAMIC     Te3/0/1
 396    082e.5fb9.c88d    DYNAMIC     Te3/0/1
 396    082e.5fbb.bfe5    DYNAMIC     Te3/0/1
 396    082e.5fbc.c3d3    DYNAMIC     Te3/0/1
 396    101f.7444.74e8    DYNAMIC     Te3/0/1
 396    1060.4b14.2a0c    DYNAMIC     Te3/0/1
 396    1060.4b14.2a1f    DYNAMIC     Te3/0/1
 396    1062.e517.ea4b    DYNAMIC     Te3/0/1
 396    1458.d03c.c922    DYNAMIC     Te3/0/1
 396    18a9.05ff.c3e9    DYNAMIC     Te3/0/1
 396    2426.4206.fa83    DYNAMIC     Te3/0/1
 396    24be.05e9.0c26    DYNAMIC     Te3/0/1
 396    2c27.d711.0bb4    DYNAMIC     Te3/0/1
 396    2c44.fd05.30ef    DYNAMIC     Te3/0/1
 396    2c44.fd05.30f8    DYNAMIC     Te3/0/1
 396    2c44.fd05.c83c    DYNAMIC     Te3/0/1
 396    2c44.fd06.9637    DYNAMIC     Te3/0/1
 396    2c59.e575.66a4    DYNAMIC     Te3/0/1
 396    2c59.e5d4.4e0f    DYNAMIC     Te3/0/1
 396    2c59.e5d5.533b    DYNAMIC     Te3/0/1
 396    2c76.8a3e.08fc    DYNAMIC     Te3/0/1
 396    2c76.8a3e.08fe    DYNAMIC     Te3/0/1
 396    2c76.8a3e.1801    DYNAMIC     Te3/0/1
 396    2c76.8a3e.1802    DYNAMIC     Te3/0/1
 396    2c76.8a3e.1806    DYNAMIC     Te3/0/1
 396    2c76.8a3e.1f2d    DYNAMIC     Te3/0/1
 396    2c76.8a3e.1f30    DYNAMIC     Te3/0/1
 396    2c76.8a3e.62e7    DYNAMIC     Te3/0/1
 396    2c76.8a3e.bef0    DYNAMIC     Te3/0/1
 396    2c76.8a3e.bef6    DYNAMIC     Te3/0/1
 396    2c76.8a3e.ce5e    DYNAMIC     Te3/0/1
 396    2c76.8a3e.ce62    DYNAMIC     Te3/0/1
 396    2c76.8a3e.ce66    DYNAMIC     Te3/0/1
 396    2c76.8a3e.ce78    DYNAMIC     Te3/0/1
 396    2c76.8a41.df94    DYNAMIC     Te3/0/1
 396    3024.a9f7.0207    DYNAMIC     Te3/0/1
 396    30e1.713d.c457    DYNAMIC     Te3/0/1
 396    30e1.71bd.b001    DYNAMIC     Te3/0/1
 396    3464.a968.515c    DYNAMIC     Te3/0/1
 396    3464.a96d.3ee6    DYNAMIC     Te3/0/1
 396    34ed.1bc4.2dec    DYNAMIC     Te3/0/1
 396    3822.e2f8.3953    DYNAMIC     Te3/0/1
 396    3822.e2fe.131d    DYNAMIC     Te3/0/1
 396    3822.e2ff.0c60    DYNAMIC     Te3/0/1
           396    3863.bb04.79b3    DYNAMIC     Te3/0/1
 396    3863.bbde.b220    DYNAMIC     Te3/0/1
 396    38ea.a76c.7a04    DYNAMIC     Te3/0/1
 396    3c4a.9243.9f3b    DYNAMIC     Te3/0/1
 396    3c4a.9243.9f41    DYNAMIC     Te3/0/1
 396    3c52.82bd.cb4e    DYNAMIC     Te3/0/1
 396    3ca8.2a02.2fc7    DYNAMIC     Te3/0/1
 396    3ca8.2a06.d2e8    DYNAMIC     Te3/0/1
 396    3ca8.2a07.f68d    DYNAMIC     Te3/0/1
 396    3ca8.2af5.9c9c    DYNAMIC     Te3/0/1
 396    3cd9.2b0e.1f1f    DYNAMIC     Te3/0/1
 396    40a8.f0b5.64ac    DYNAMIC     Te3/0/1
 396    40b0.3426.8a0c    DYNAMIC     Te3/0/1
 396    441e.a132.0361    DYNAMIC     Te3/0/1
 396    441e.a133.0486    DYNAMIC     Te3/0/1
 396    441e.a135.3d56    DYNAMIC     Te3/0/1
 396    441e.a135.3d62    DYNAMIC     Te3/0/1
 396    441e.a135.3d6f    DYNAMIC     Te3/0/1
 396    441e.a135.3d71    DYNAMIC     Te3/0/1
 396    441e.a135.3d81    DYNAMIC     Te3/0/1
 396    441e.a135.3dad    DYNAMIC     Te3/0/1
 396    480f.cfc8.5c46    DYNAMIC     Te3/0/1
 396    480f.cfc8.6c1f    DYNAMIC     Te3/0/1
 396    480f.cfe8.71d9    DYNAMIC     Te3/0/1
 396    480f.cff9.32ca    DYNAMIC     Te3/0/1
 396    5065.f35a.83d7    DYNAMIC     Te3/0/1
 396    5820.b14d.2a0c    DYNAMIC     Te3/0/1
 396    5820.b14d.6c58    DYNAMIC     Te3/0/1
 396    5820.b150.a32c    DYNAMIC     Te3/0/1
 396    5820.b150.c32c    DYNAMIC     Te3/0/1
 396    5820.b150.c343    DYNAMIC     Te3/0/1
 396    5820.b150.c344    DYNAMIC     Te3/0/1
 396    5820.b150.c396    DYNAMIC     Te3/0/1
 396    5820.b150.c3ba    DYNAMIC     Te3/0/1
 396    5820.b150.daae    DYNAMIC     Te3/0/1
 396    5ca6.2d2d.32fc    DYNAMIC     Te3/0/1
 396    5cb9.010e.0358    DYNAMIC     Te3/0/1
 396    5cb9.0111.bdd5    DYNAMIC     Te3/0/1
 396    5cb9.0111.bf85    DYNAMIC     Te3/0/1
 396    5cb9.0112.b03a    DYNAMIC     Te3/0/1
 396    6451.0624.07f3    DYNAMIC     Te3/0/1
 396    68ab.8a82.6522    DYNAMIC     Te3/0/1
 396    6c02.e0f5.e50f    DYNAMIC     Te3/0/1
 396    6c3b.e508.400d    DYNAMIC     Te3/0/1
 396    6c3b.e508.62c8    DYNAMIC     Te3/0/1
 396    6c3b.e508.62cf    DYNAMIC     Te3/0/1
 396    6c3b.e509.5045    DYNAMIC     Te3/0/1
 396    6cc2.1722.1a3c    DYNAMIC     Te3/0/1
 396    705a.0fa4.2ccb    DYNAMIC     Te3/0/1
 396    7446.a04c.d33b    DYNAMIC     Te3/0/1
 396    7446.a052.1704    DYNAMIC     Te3/0/1
 396    7446.a052.177c    DYNAMIC     Te3/0/1
 396    781c.5a60.2b13    DYNAMIC     Te3/0/1
 396    78ac.c082.e3bd    DYNAMIC     Te3/0/1
 396    78e3.b5f7.5764    DYNAMIC     Te3/0/1
 396    80c1.6e94.4937    DYNAMIC     Te3/0/1
 396    80e8.2c7e.2333    DYNAMIC     Te3/0/1
 396    842a.fd79.a5db    DYNAMIC     Te3/0/1
 396    842a.fd79.b515    DYNAMIC     Te3/0/1
           396    8851.fbeb.3fda    DYNAMIC     Te3/0/1
 396    8851.fbeb.4f84    DYNAMIC     Te3/0/1
 396    8851.fbeb.7fa5    DYNAMIC     Te3/0/1
 396    8851.fbec.42d9    DYNAMIC     Te3/0/1
 396    8cdc.d45d.429d    DYNAMIC     Te3/0/1
 396    8cdc.d45d.c496    DYNAMIC     Te3/0/1
 396    9457.a515.beef    DYNAMIC     Te3/0/1
 396    9457.a5d1.bf45    DYNAMIC     Te3/0/1
 396    984b.e13e.0d8c    DYNAMIC     Te3/0/1
 396    98e7.f4a3.406d    DYNAMIC     Te3/0/1
 396    98e7.f4a3.9755    DYNAMIC     Te3/0/1
 396    98e7.f4a6.05f6    DYNAMIC     Te3/0/1
 396    98e7.f4a6.f061    DYNAMIC     Te3/0/1
 396    9c7b.ef85.8df6    DYNAMIC     Te3/0/1
 396    9c8e.9985.4cb6    DYNAMIC     Te3/0/1
 396    9cb6.541b.d595    DYNAMIC     Te3/0/1
 396    a08c.fd17.2ffb    DYNAMIC     Te3/0/1
 396    a08c.fd62.ac41    DYNAMIC     Te3/0/1
 396    a08c.fde6.f43f    DYNAMIC     Te3/0/1
 396    a093.51d2.5c6d    DYNAMIC     Te3/0/1
 396    a0b3.cc9a.a572    DYNAMIC     Te3/0/1
 396    a0b3.cc9a.b458    DYNAMIC     Te3/0/1
 396    a0b3.cc9a.b4c4    DYNAMIC     Te3/0/1
 396    a0b3.cc9a.b4e3    DYNAMIC     Te3/0/1
 396    a0b3.cc9a.c41e    DYNAMIC     Te3/0/1
 396    a0b3.cc9a.c4db    DYNAMIC     Te3/0/1
 396    a0b3.cc9e.b460    DYNAMIC     Te3/0/1
 396    a0b3.cc9f.e23a    DYNAMIC     Te3/0/1
 396    a0d3.c17f.c88a    DYNAMIC     Te3/0/1
 396    a0d3.c181.9c7b    DYNAMIC     Te3/0/1
 396    ac16.2d39.857e    DYNAMIC     Te3/0/1
 396    ace2.d349.6c59    DYNAMIC     Te3/0/1
 396    b00c.d1e3.5e38    DYNAMIC     Te3/0/1
 396    b05a.dac1.8345    DYNAMIC     Te3/0/1
 396    b05a.dac2.c21c    DYNAMIC     Te3/0/1
 396    b4b5.2ff7.b9ff    DYNAMIC     Te3/0/1
 396    b4b5.2ff8.a375    DYNAMIC     Te3/0/1
 396    b4b5.2ff8.db8b    DYNAMIC     Te3/0/1
 396    b4b6.8604.1551    DYNAMIC     Te3/0/1
 396    b4b6.86c4.7b1c    DYNAMIC     Te3/0/1
 396    b4b6.86c8.44e0    DYNAMIC     Te3/0/1
 396    bce9.2fd1.182a    DYNAMIC     Te3/0/1
 396    bce9.2fd1.1836    DYNAMIC     Te3/0/1
 396    bce9.2fd1.184a    DYNAMIC     Te3/0/1
 396    bce9.2fd1.2b2a    DYNAMIC     Te3/0/1
 396    bce9.2fd2.2fff    DYNAMIC     Te3/0/1
 396    bce9.2fd2.5fc3    DYNAMIC     Te3/0/1
 396    bce9.2fd2.5fd5    DYNAMIC     Te3/0/1
 396    bce9.2fd2.5fd7    DYNAMIC     Te3/0/1
 396    bce9.2fd2.5fe5    DYNAMIC     Te3/0/1
 396    bce9.2fd2.bba0    DYNAMIC     Te3/0/1
 396    bce9.2fd2.db2e    DYNAMIC     Te3/0/1
 396    bce9.2fd3.8e45    DYNAMIC     Te3/0/1
 396    bce9.2fd3.8e47    DYNAMIC     Te3/0/1
 396    bce9.2fd4.1676    DYNAMIC     Te3/0/1
 396    bce9.2fd4.492b    DYNAMIC     Te3/0/1
 396    bce9.2fd4.67b5    DYNAMIC     Te3/0/1
 396    bce9.2fd4.86f8    DYNAMIC     Te3/0/1
 396    bce9.2fd4.96ba    DYNAMIC     Te3/0/1
           396    bce9.2fd4.96ca    DYNAMIC     Te3/0/1
 396    bce9.2fd4.96e4    DYNAMIC     Te3/0/1
 396    bce9.2fd4.96ec    DYNAMIC     Te3/0/1
 396    bce9.2fd4.96ee    DYNAMIC     Te3/0/1
 396    bce9.2fd4.96f0    DYNAMIC     Te3/0/1
 396    bce9.2fd4.a604    DYNAMIC     Te3/0/1
 396    bce9.2fd4.a678    DYNAMIC     Te3/0/1
 396    bce9.2fd4.c6a0    DYNAMIC     Te3/0/1
 396    bce9.2fd4.d8aa    DYNAMIC     Te3/0/1
 396    bce9.2fd4.d8be    DYNAMIC     Te3/0/1
 396    bce9.2fd4.d8d8    DYNAMIC     Te3/0/1
 396    bce9.2fd4.f806    DYNAMIC     Te3/0/1
 396    bce9.2fd7.09b8    DYNAMIC     Te3/0/1
 396    bce9.2fd7.09c0    DYNAMIC     Te3/0/1
 396    bce9.2fd7.09c6    DYNAMIC     Te3/0/1
 396    bce9.2fd7.09c8    DYNAMIC     Te3/0/1
 396    bce9.2fd7.09d0    DYNAMIC     Te3/0/1
 396    bce9.2fd7.a910    DYNAMIC     Te3/0/1
 396    bce9.2fd7.f863    DYNAMIC     Te3/0/1
 396    bce9.2fd7.f883    DYNAMIC     Te3/0/1
 396    c434.6b1a.a5a8    DYNAMIC     Te3/0/1
 396    c8cb.b861.ec36    DYNAMIC     Te3/0/1
 396    c8cb.b863.2b9a    DYNAMIC     Te3/0/1
 396    c8d3.ff0f.d6c6    DYNAMIC     Te3/0/1
 396    c8d9.d2cf.77ef    DYNAMIC     Te3/0/1
 396    d0bf.9c30.79dc    DYNAMIC     Te3/0/1
 396    d0bf.9c36.841a    DYNAMIC     Te3/0/1
 396    dc4a.3eb2.ce7f    DYNAMIC     Te3/0/1
 396    dc4a.3eb3.9cd7    DYNAMIC     Te3/0/1
 396    e839.358d.4df3    DYNAMIC     Te3/0/1
 396    e839.358d.81db    DYNAMIC     Te3/0/1
 396    e839.358d.f1a6    DYNAMIC     Te3/0/1
 396    e839.358e.30f0    DYNAMIC     Te3/0/1
 396    e8d8.d196.d68d    DYNAMIC     Te3/0/1
 396    e8d8.d1e5.8934    DYNAMIC     Te3/0/1
 396    ec8e.b525.79bd    DYNAMIC     Te3/0/1
 396    ec8e.b526.793e    DYNAMIC     Te3/0/1
 396    ec8e.b5bc.2b13    DYNAMIC     Te3/0/1
 396    ecb1.d7f8.0df7    DYNAMIC     Te3/0/1
 396    f092.1c61.7307    DYNAMIC     Te3/0/1
 396    f092.1c61.730f    DYNAMIC     Te3/0/1
 396    f092.1c61.87a2    DYNAMIC     Te3/0/1
 396    f092.1c62.ed7e    DYNAMIC     Te3/0/1
 396    f092.1c62.ed8a    DYNAMIC     Te3/0/1
 396    f092.1c62.ed8d    DYNAMIC     Te3/0/1
 396    f092.1c62.ed8e    DYNAMIC     Te3/0/1
 396    f092.1c62.fd4d    DYNAMIC     Te3/0/1
 396    f430.b971.658a    DYNAMIC     Te3/0/1
 396    f430.b973.d281    DYNAMIC     Te3/0/1
 396    f439.0906.6c2e    DYNAMIC     Te3/0/1
 396    f80d.acd5.b352    DYNAMIC     Te3/0/1
 396    f80d.acd7.5dc5    DYNAMIC     Te3/0/1
 396    f80d.acd7.5dd1    DYNAMIC     Te3/0/1
 396    f80d.acd7.5dd9    DYNAMIC     Te3/0/1
 396    fc3f.db50.0c1c    DYNAMIC     Te3/0/1
 396    fc3f.db51.506a    DYNAMIC     Te3/0/1
 396    fc3f.dbbd.1d43    DYNAMIC     Te3/0/1
 396    fc3f.dbbe.4bc9    DYNAMIC     Te3/0/1
 396    fc3f.dbbe.8f7c    DYNAMIC     Te3/0/1
           396    fc3f.dbbf.1fc2    DYNAMIC     Te3/0/1
 396    fc3f.dbc3.a733    DYNAMIC     Te3/0/1
 341    0000.0c9f.f155    DYNAMIC     Te3/0/1
 341    0001.0554.1ca2    DYNAMIC     Te3/0/1
 341    0001.3e03.7ab7    DYNAMIC     Te3/0/1
 341    0001.3e03.7b28    DYNAMIC     Te3/0/1
 341    0001.3e03.7c98    DYNAMIC     Te3/0/1
 341    0001.3e03.9ca0    DYNAMIC     Te3/0/1
 341    0001.f08f.3020    DYNAMIC     Gi5/0/36
 341    0001.f08f.3036    DYNAMIC     Te3/0/1
 341    0001.f091.f144    DYNAMIC     Gi5/0/35
 341    0020.4afc.4c51    DYNAMIC     Te3/0/1
 341    003a.9c3f.d7c1    DYNAMIC     Te3/0/1
 341    003a.9c40.0dc1    DYNAMIC     Te3/0/1
 341    0040.9d2c.dac5    DYNAMIC     Te3/0/1
 341    0040.ae08.4bbc    DYNAMIC     Te3/0/1
 341    0090.3329.78d5    DYNAMIC     Te3/0/1
 341    00d0.c9c1.2fc2    DYNAMIC     Te3/0/1
 341    00d0.c9c1.2fce    DYNAMIC     Te3/0/1
 341    00d0.c9c1.577e    DYNAMIC     Te3/0/1
 341    00d0.c9c7.bba5    DYNAMIC     Te3/0/1
 341    1862.e4cd.30c2    DYNAMIC     Te3/0/1
 341    88d7.f6c2.bd3d    DYNAMIC     Te3/0/1
 341    9070.656a.a15d    DYNAMIC     Te3/0/1
 341    9070.65c4.8f88    DYNAMIC     Te3/0/1
 341    9070.65d3.a551    DYNAMIC     Te3/0/1
 341    a093.51d2.5c6d    DYNAMIC     Te3/0/1
 341    c4f3.126d.5cfc    DYNAMIC     Te3/0/1
 540    0000.0c9f.f21c    DYNAMIC     Te3/0/1
 540    0019.9972.d8f1    DYNAMIC     Te3/0/1
 540    001f.2905.d796    DYNAMIC     Te3/0/1
 540    003a.9c3f.d7c1    DYNAMIC     Te3/0/1
 540    003a.9c40.0dc1    DYNAMIC     Te3/0/1
 540    4c52.621a.66f2    DYNAMIC     Te3/0/1
 540    901b.0ea7.a9ad    DYNAMIC     Te3/0/1
 540    901b.0efe.da35    DYNAMIC     Te3/0/1
 540    a093.51d2.5c6d    DYNAMIC     Te3/0/1
 540    ecb1.d739.105c    DYNAMIC     Te3/0/1
 607    0000.0c9f.f25f    DYNAMIC     Te3/0/1
 607    0024.ae03.4c80    DYNAMIC     Te3/0/1
 607    003a.9c3f.d7c1    DYNAMIC     Te3/0/1
 607    003a.9c40.0dc1    DYNAMIC     Te3/0/1
 607    0050.f900.8bf4    DYNAMIC     Te3/0/1
 607    0050.f900.d1eb    DYNAMIC     Te3/0/1
 607    0050.f901.5cf7    DYNAMIC     Te3/0/1
 607    0050.f901.a7d3    DYNAMIC     Gi5/0/31
 607    34ed.1bc4.2dec    DYNAMIC     Te3/0/1
 607    a093.51d2.5c6d    DYNAMIC     Te3/0/1
 732    0000.0c9f.f2dc    DYNAMIC     Te3/0/1
 732    0001.0554.1c84    DYNAMIC     Te3/0/1
 732    0022.db01.b43a    DYNAMIC     Gi5/0/29
 732    0022.db01.c4d5    DYNAMIC     Gi5/0/26
 732    0022.db01.c58f    DYNAMIC     Gi5/0/27
 732    0022.db01.c674    DYNAMIC     Gi5/0/25
 732    003a.9c3f.d7c1    DYNAMIC     Te3/0/1
 732    003a.9c40.0dc1    DYNAMIC     Te3/0/1
 732    34ed.1bc4.2dec    DYNAMIC     Te3/0/1
 732    a093.51d2.5c6d    DYNAMIC     Te3/0/1
1037    0000.0c9f.f40d    DYNAMIC     Te3/0/1
          1037    000b.86c0.b6fe    DYNAMIC     Gi5/0/47
1037    000b.86c4.9060    DYNAMIC     Te3/0/1
1037    0027.9048.1320    DYNAMIC     Te3/0/1
1037    0027.9048.1f80    DYNAMIC     Te3/0/1
1037    0027.9048.1f90    DYNAMIC     Te3/0/1
1037    003a.9c3f.d7c1    DYNAMIC     Te3/0/1
1037    003a.9c40.0dc1    DYNAMIC     Te3/0/1
1037    006b.f125.c708    DYNAMIC     Te3/0/1
1037    006b.f125.c7b6    DYNAMIC     Te3/0/1
1037    006b.f125.cb8c    DYNAMIC     Te3/0/1
1037    006b.f125.cb9a    DYNAMIC     Te3/0/1
1037    006b.f125.cc2e    DYNAMIC     Te3/0/1
1037    006b.f125.cf4e    DYNAMIC     Te3/0/1
1037    006b.f125.d0aa    DYNAMIC     Te3/0/1
1037    006b.f125.d3b4    DYNAMIC     Te3/0/1
1037    006b.f125.d3c2    DYNAMIC     Te3/0/1
1037    006b.f125.d3da    DYNAMIC     Te3/0/1
1037    006b.f125.d3dc    DYNAMIC     Te3/0/1
1037    006b.f125.d3fc    DYNAMIC     Te3/0/1
1037    006b.f125.d412    DYNAMIC     Te3/0/1
1037    006b.f125.d54c    DYNAMIC     Te3/0/1
1037    006b.f125.d730    DYNAMIC     Te3/0/1
1037    006b.f125.d744    DYNAMIC     Te3/0/1
1037    006b.f125.d784    DYNAMIC     Te3/0/1
1037    006b.f125.d79e    DYNAMIC     Te3/0/1
1037    006b.f125.d882    DYNAMIC     Te3/0/1
1037    006b.f125.d8a2    DYNAMIC     Te3/0/1
1037    0081.c424.1d04    DYNAMIC     Te3/0/1
1037    0081.c467.0fba    DYNAMIC     Te3/0/1
1037    0081.c467.1ffe    DYNAMIC     Te3/0/1
1037    00d7.8f1e.b5d0    DYNAMIC     Te3/0/1
1037    00d7.8f1e.b608    DYNAMIC     Te3/0/1
1037    00d7.8f1e.bf38    DYNAMIC     Te3/0/1
1037    00d7.8f1e.bf78    DYNAMIC     Te3/0/1
1037    00d7.8fa6.e7fc    DYNAMIC     Te3/0/1
1037    00d7.8fa6.f336    DYNAMIC     Te3/0/1
1037    00d7.8fa6.f3a4    DYNAMIC     Te3/0/1
1037    00eb.d510.0d70    DYNAMIC     Te3/0/1
1037    00eb.d510.5660    DYNAMIC     Te3/0/1
1037    00ee.ab3f.5498    DYNAMIC     Te3/0/1
1037    00ee.ab3f.5ad0    DYNAMIC     Te3/0/1
1037    00ee.ab3f.5e38    DYNAMIC     Te3/0/1
1037    00ee.ab3f.5e68    DYNAMIC     Te3/0/1
1037    00ee.ab3f.5f08    DYNAMIC     Te3/0/1
1037    00ee.ab3f.5fb0    DYNAMIC     Te3/0/1
1037    00ee.ab3f.6168    DYNAMIC     Te3/0/1
1037    00ee.ab3f.6198    DYNAMIC     Te3/0/1
1037    00ee.ab3f.61a0    DYNAMIC     Te3/0/1
1037    00ee.ab3f.6298    DYNAMIC     Te3/0/1
1037    00ee.ab3f.7158    DYNAMIC     Te3/0/1
1037    00ee.ab3f.7238    DYNAMIC     Te3/0/1
1037    00ee.ab3f.72a8    DYNAMIC     Te3/0/1
1037    00ee.ab3f.72e8    DYNAMIC     Te3/0/1
1037    00ee.ab3f.7300    DYNAMIC     Te3/0/1
1037    00ee.ab3f.7318    DYNAMIC     Te3/0/1
1037    00ee.ab3f.7340    DYNAMIC     Te3/0/1
1037    00ee.ab3f.7350    DYNAMIC     Te3/0/1
1037    00ee.ab3f.7370    DYNAMIC     Te3/0/1
1037    00ee.ab3f.73a8    DYNAMIC     Te3/0/1
          1037    00ee.ab3f.7420    DYNAMIC     Te3/0/1
1037    00ee.ab3f.7430    DYNAMIC     Te3/0/1
1037    00ee.ab3f.7470    DYNAMIC     Te3/0/1
1037    00ee.ab3f.7828    DYNAMIC     Gi6/0/20
1037    00ee.ab3f.7870    DYNAMIC     Te3/0/1
1037    00ee.ab3f.7880    DYNAMIC     Te3/0/1
1037    00ee.ab3f.78f8    DYNAMIC     Te3/0/1
1037    00ee.ab3f.7908    DYNAMIC     Te3/0/1
1037    00ee.ab3f.7928    DYNAMIC     Te3/0/1
1037    00ee.ab3f.7ab0    DYNAMIC     Te3/0/1
1037    00ee.ab3f.7b68    DYNAMIC     Te3/0/1
1037    00ee.ab3f.7bf0    DYNAMIC     Te3/0/1
1037    00ee.ab3f.7c88    DYNAMIC     Te3/0/1
1037    00ee.ab3f.7cd8    DYNAMIC     Te3/0/1
1037    00ee.ab3f.7cf0    DYNAMIC     Te3/0/1
1037    00ee.ab3f.7d08    DYNAMIC     Te3/0/1
1037    00ee.ab3f.7d30    DYNAMIC     Te3/0/1
1037    00ee.ab3f.7de8    DYNAMIC     Te3/0/1
1037    00ee.ab3f.7e08    DYNAMIC     Te3/0/1
1037    00ee.ab3f.7e68    DYNAMIC     Te3/0/1
1037    00ee.ab3f.7ec0    DYNAMIC     Te3/0/1
1037    00ee.ab3f.7f40    DYNAMIC     Te3/0/1
1037    00ee.ab3f.7f50    DYNAMIC     Te3/0/1
1037    00ee.ab3f.7f58    DYNAMIC     Te3/0/1
1037    00ee.ab3f.7f90    DYNAMIC     Te3/0/1
1037    00ee.ab3f.7fa8    DYNAMIC     Gi6/0/22
1037    00ee.ab3f.8008    DYNAMIC     Te3/0/1
1037    00ee.ab3f.8090    DYNAMIC     Te3/0/1
1037    00ee.ab3f.80c8    DYNAMIC     Te3/0/1
1037    00ee.ab3f.80f8    DYNAMIC     Te3/0/1
1037    00ee.ab3f.8248    DYNAMIC     Te3/0/1
1037    00ee.ab3f.8328    DYNAMIC     Te3/0/1
1037    00ee.ab3f.84b8    DYNAMIC     Te3/0/1
1037    00ee.ab3f.8510    DYNAMIC     Te3/0/1
1037    00ee.ab3f.8558    DYNAMIC     Te3/0/1
1037    00ee.ab3f.8578    DYNAMIC     Te3/0/1
1037    00ee.ab3f.8580    DYNAMIC     Te3/0/1
1037    00ee.ab3f.85d8    DYNAMIC     Te3/0/1
1037    00ee.ab3f.8648    DYNAMIC     Te3/0/1
1037    00ee.ab3f.86e0    DYNAMIC     Te3/0/1
1037    00ee.ab3f.86f8    DYNAMIC     Te3/0/1
1037    00ee.ab3f.87b8    DYNAMIC     Te3/0/1
1037    00ee.ab3f.88e0    DYNAMIC     Te3/0/1
1037    00ee.ab3f.8908    DYNAMIC     Te3/0/1
1037    00ee.ab3f.8a38    DYNAMIC     Te3/0/1
1037    00ee.ab3f.8ad8    DYNAMIC     Te3/0/1
1037    00f6.634a.6020    DYNAMIC     Te3/0/1
1037    00f6.634a.69a6    DYNAMIC     Te3/0/1
1037    00f6.634a.69b4    DYNAMIC     Te3/0/1
1037    00f6.634a.69c4    DYNAMIC     Te3/0/1
1037    00f6.634a.69ca    DYNAMIC     Te3/0/1
1037    00f6.634a.69ce    DYNAMIC     Te3/0/1
1037    00f6.634a.69d8    DYNAMIC     Te3/0/1
1037    00f6.634a.69ee    DYNAMIC     Te3/0/1
1037    00f6.634a.6a78    DYNAMIC     Te3/0/1
1037    00f6.634a.6a84    DYNAMIC     Te3/0/1
1037    00f6.634a.6a86    DYNAMIC     Te3/0/1
1037    00f6.634a.6a9e    DYNAMIC     Te3/0/1
1037    0462.7381.8bd8    DYNAMIC     Te3/0/1
          1037    0462.7383.5f90    DYNAMIC     Te3/0/1
1037    0462.73c7.d38c    DYNAMIC     Te3/0/1
1037    0462.73db.5ab4    DYNAMIC     Te3/0/1
1037    0462.73e1.f210    DYNAMIC     Te3/0/1
1037    0462.73e8.e024    DYNAMIC     Te3/0/1
1037    0462.73f0.cef4    DYNAMIC     Te3/0/1
1037    0462.73f0.cf60    DYNAMIC     Te3/0/1
1037    10b3.d5b0.a014    DYNAMIC     Te3/0/1
1037    10b3.d5b0.a2a6    DYNAMIC     Te3/0/1
1037    10b3.d5b6.071a    DYNAMIC     Te3/0/1
1037    10b3.d5bf.e006    DYNAMIC     Te3/0/1
1037    10b3.d5cb.645c    DYNAMIC     Te3/0/1
1037    10b3.d5cb.6636    DYNAMIC     Te3/0/1
1037    10b3.d5cb.6642    DYNAMIC     Te3/0/1
1037    10b3.d5cb.6a0a    DYNAMIC     Te3/0/1
1037    10b3.d5e9.b8cc    DYNAMIC     Te3/0/1
1037    10b3.d6b3.a0f8    DYNAMIC     Te3/0/1
1037    10b3.d6b3.a10a    DYNAMIC     Te3/0/1
1037    10b3.d6b3.a312    DYNAMIC     Te3/0/1
1037    1880.902e.4aba    DYNAMIC     Te3/0/1
1037    1880.902e.5f58    DYNAMIC     Te3/0/1
1037    2416.9dd9.eb00    DYNAMIC     Te3/0/1
1037    2416.9dd9.eb08    DYNAMIC     Te3/0/1
1037    2416.9dd9.eb7e    DYNAMIC     Te3/0/1
1037    2416.9dd9.ebcc    DYNAMIC     Te3/0/1
1037    2416.9dd9.f0a0    DYNAMIC     Te3/0/1
1037    2416.9dd9.f0f6    DYNAMIC     Te3/0/1
1037    2416.9dd9.f110    DYNAMIC     Te3/0/1
1037    2416.9dd9.f126    DYNAMIC     Te3/0/1
1037    2416.9dd9.f136    DYNAMIC     Te3/0/1
1037    2416.9dd9.f200    DYNAMIC     Te3/0/1
1037    2416.9dd9.f2ac    DYNAMIC     Te3/0/1
1037    2416.9dd9.f2dc    DYNAMIC     Te3/0/1
1037    2416.9df5.09e6    DYNAMIC     Te3/0/1
1037    3890.a578.0156    DYNAMIC     Te3/0/1
1037    3890.a578.153e    DYNAMIC     Te3/0/1
1037    3890.a578.1782    DYNAMIC     Te3/0/1
1037    3890.a578.1ae6    DYNAMIC     Te3/0/1
1037    3c51.0e3d.e7c8    DYNAMIC     Te3/0/1
1037    3c51.0e3d.efa0    DYNAMIC     Te3/0/1
1037    3c51.0e3d.efae    DYNAMIC     Te3/0/1
1037    3c51.0e3d.efb8    DYNAMIC     Te3/0/1
1037    3c51.0e3d.eff0    DYNAMIC     Gi5/0/44
1037    3c51.0e3d.f404    DYNAMIC     Te3/0/1
1037    3c51.0e3d.f414    DYNAMIC     Te3/0/1
1037    3c51.0e3d.f428    DYNAMIC     Te3/0/1
1037    3c51.0e3d.f430    DYNAMIC     Te3/0/1
1037    3c51.0e3d.f434    DYNAMIC     Te3/0/1
1037    3c51.0e3d.f436    DYNAMIC     Te3/0/1
1037    3c51.0e40.cf46    DYNAMIC     Te3/0/1
1037    3c51.0e49.db14    DYNAMIC     Te3/0/1
1037    3c51.0e49.e318    DYNAMIC     Te3/0/1
1037    3c51.0e60.5526    DYNAMIC     Te3/0/1
1037    3c51.0e60.631a    DYNAMIC     Te3/0/1
1037    3c51.0efa.5e64    DYNAMIC     Te3/0/1
1037    3c51.0efa.686e    DYNAMIC     Te3/0/1
1037    3c51.0efa.6880    DYNAMIC     Te3/0/1
1037    4c71.0d0f.1dd8    DYNAMIC     Te3/0/1
1037    4c71.0d0f.1f28    DYNAMIC     Te3/0/1
          1037    4c71.0d0f.23d0    DYNAMIC     Te3/0/1
1037    4c71.0d0f.2e44    DYNAMIC     Te3/0/1
1037    4c71.0d33.8eca    DYNAMIC     Te3/0/1
1037    4c71.0d3d.9b2a    DYNAMIC     Te3/0/1
1037    4c71.0d3e.db20    DYNAMIC     Te3/0/1
1037    4c71.0d3e.db24    DYNAMIC     Te3/0/1
1037    4c71.0d3e.db6e    DYNAMIC     Te3/0/1
1037    4c71.0d3f.2010    DYNAMIC     Te3/0/1
1037    4c71.0d90.4fce    DYNAMIC     Te3/0/1
1037    4ce1.76b9.c324    DYNAMIC     Te3/0/1
1037    4ce1.76cb.49c0    DYNAMIC     Te3/0/1
1037    4ce1.76cb.50fc    DYNAMIC     Te3/0/1
1037    4ce1.76cb.5116    DYNAMIC     Te3/0/1
1037    4ce1.76ef.e862    DYNAMIC     Te3/0/1
1037    500f.804a.06d4    DYNAMIC     Te3/0/1
1037    500f.8098.16a4    DYNAMIC     Te3/0/1
1037    500f.8098.1742    DYNAMIC     Te3/0/1
1037    502f.a8df.8b18    DYNAMIC     Te3/0/1
1037    503d.e583.2cff    DYNAMIC     Te3/0/1
1037    5ca6.2d2d.32c8    DYNAMIC     Te3/0/1
1037    5ca6.2d2d.32d2    DYNAMIC     Te3/0/1
1037    5ca6.2d2d.32dc    DYNAMIC     Te3/0/1
1037    5ca6.2d2d.32e2    DYNAMIC     Te3/0/1
1037    5ca6.2db6.f820    DYNAMIC     Te3/0/1
1037    5ca6.2db6.f882    DYNAMIC     Te3/0/1
1037    5ca6.2db6.f886    DYNAMIC     Te3/0/1
1037    5ca6.2db6.fbb8    DYNAMIC     Te3/0/1
1037    5ca6.2db6.fbca    DYNAMIC     Te3/0/1
1037    5ca6.2dd7.50d6    DYNAMIC     Te3/0/1
1037    5ca6.2dd7.50e0    DYNAMIC     Te3/0/1
1037    5ca6.2dd7.50e6    DYNAMIC     Te3/0/1
1037    5ca6.2dd7.50ec    DYNAMIC     Te3/0/1
1037    5ca6.2dd7.5132    DYNAMIC     Te3/0/1
1037    5ca6.2dd7.56f0    DYNAMIC     Te3/0/1
1037    5ca6.2dd7.570c    DYNAMIC     Te3/0/1
1037    5ca6.2dd7.5714    DYNAMIC     Te3/0/1
1037    5ca6.2dd7.574e    DYNAMIC     Te3/0/1
1037    5ca6.2de6.3968    DYNAMIC     Te3/0/1
1037    5ca6.2de6.3976    DYNAMIC     Te3/0/1
1037    5ca6.2de6.397a    DYNAMIC     Te3/0/1
1037    5ca6.2de6.397e    DYNAMIC     Te3/0/1
1037    5ca6.2de6.3984    DYNAMIC     Te3/0/1
1037    689e.0b9a.0b6a    DYNAMIC     Te3/0/1
1037    6c8b.d313.d40a    DYNAMIC     Te3/0/1
1037    7018.a722.fab5    DYNAMIC     Te3/0/1
1037    70b3.1713.adf8    DYNAMIC     Te3/0/1
1037    70db.981a.1ba4    DYNAMIC     Te3/0/1
1037    70df.2fa2.6afc    DYNAMIC     Te3/0/1
1037    70ea.1a6a.bd58    DYNAMIC     Te3/0/1
1037    70ea.1ae3.7ee0    DYNAMIC     Te3/0/1
1037    70ea.1ae3.87a0    DYNAMIC     Te3/0/1
1037    70ea.1ae3.87c8    DYNAMIC     Te3/0/1
1037    70ea.1ae3.8ab0    DYNAMIC     Te3/0/1
1037    70ea.1ae3.8b68    DYNAMIC     Te3/0/1
1037    70ea.1ae3.8bd8    DYNAMIC     Te3/0/1
1037    70ea.1ae3.8bf8    DYNAMIC     Te3/0/1
1037    70ea.1ae3.8d58    DYNAMIC     Te3/0/1
1037    70ea.1ae3.8e10    DYNAMIC     Te3/0/1
1037    70ea.1ae3.8e48    DYNAMIC     Te3/0/1
          1037    70ea.1ae3.8fd8    DYNAMIC     Te3/0/1
1037    70ea.1ae3.9168    DYNAMIC     Te3/0/1
1037    70ea.1ae3.9200    DYNAMIC     Te3/0/1
1037    70ea.1ae3.9270    DYNAMIC     Gi6/0/24
1037    70ea.1ae3.92c0    DYNAMIC     Te3/0/1
1037    70ea.1ae3.92e0    DYNAMIC     Te3/0/1
1037    70ea.1ae3.92e8    DYNAMIC     Te3/0/1
1037    70ea.1ae3.9578    DYNAMIC     Te3/0/1
1037    7872.5d1c.2c84    DYNAMIC     Te3/0/1
1037    7872.5d62.af70    DYNAMIC     Te3/0/1
1037    78ba.f993.483c    DYNAMIC     Te3/0/1
1037    80e0.1d3c.7608    DYNAMIC     Te3/0/1
1037    84b2.61b0.4d04    DYNAMIC     Te3/0/1
1037    84b2.61b0.4e80    DYNAMIC     Te3/0/1
1037    84b2.61b9.80c8    DYNAMIC     Te3/0/1
1037    84b2.61bf.ab34    DYNAMIC     Te3/0/1
1037    84b8.02a4.6cc0    DYNAMIC     Te3/0/1
1037    84b8.02a7.bd94    DYNAMIC     Te3/0/1
1037    84b8.02b8.32c8    DYNAMIC     Te3/0/1
1037    88f0.3137.db08    DYNAMIC     Te3/0/1
1037    a023.9f66.123c    DYNAMIC     Te3/0/1
1037    a093.51d2.5c6d    DYNAMIC     Te3/0/1
1037    a0b4.395d.85d0    DYNAMIC     Te3/0/1
1037    a0b4.395d.87bc    DYNAMIC     Te3/0/1
1037    a0b4.395d.8d10    DYNAMIC     Te3/0/1
1037    a0b4.3978.c188    DYNAMIC     Te3/0/1
1037    a0b4.3978.c1a0    DYNAMIC     Te3/0/1
1037    a0b4.3978.c1da    DYNAMIC     Te3/0/1
1037    a0b4.3978.c1ee    DYNAMIC     Te3/0/1
1037    a0b4.3978.d59c    DYNAMIC     Te3/0/1
1037    a0b4.3987.a772    DYNAMIC     Te3/0/1
1037    a0b4.3987.aa50    DYNAMIC     Te3/0/1
1037    a0b4.3987.b6ee    DYNAMIC     Te3/0/1
1037    a0b4.3987.b71a    DYNAMIC     Te3/0/1
1037    a0b4.3987.b71e    DYNAMIC     Gi5/0/45
1037    a0b4.3987.c79c    DYNAMIC     Te3/0/1
1037    a0b4.398d.6886    DYNAMIC     Te3/0/1
1037    a0b4.398d.7234    DYNAMIC     Te3/0/1
1037    a0b4.398d.7266    DYNAMIC     Te3/0/1
1037    a0b4.398d.7864    DYNAMIC     Te3/0/1
1037    a0b4.398d.788c    DYNAMIC     Te3/0/1
1037    a0b4.398d.78b6    DYNAMIC     Te3/0/1
1037    a0b4.398d.78ba    DYNAMIC     Te3/0/1
1037    a0b4.39c5.79aa    DYNAMIC     Te3/0/1
1037    a0b4.39c5.79d4    DYNAMIC     Te3/0/1
1037    a0ec.f9fe.48cc    DYNAMIC     Te3/0/1
1037    a453.0ec4.1e40    DYNAMIC     Te3/0/1
1037    a89d.2155.e2c0    DYNAMIC     Te3/0/1
1037    a89d.2155.e350    DYNAMIC     Te3/0/1
1037    a89d.2164.2c98    DYNAMIC     Te3/0/1
1037    a89d.2169.e744    DYNAMIC     Te3/0/1
1037    a89d.2169.e7f0    DYNAMIC     Te3/0/1
1037    a89d.2169.e84c    DYNAMIC     Te3/0/1
1037    ac3a.673d.730e    DYNAMIC     Te3/0/1
1037    ac3a.673d.7380    DYNAMIC     Te3/0/1
1037    ac3a.6749.4576    DYNAMIC     Te3/0/1
1037    ac3a.6749.459a    DYNAMIC     Te3/0/1
1037    ac3a.6749.4bb4    DYNAMIC     Te3/0/1
1037    ac3a.6749.4be6    DYNAMIC     Te3/0/1
          1037    ac3a.6749.4bf4    DYNAMIC     Te3/0/1
1037    ac3a.6749.4cd4    DYNAMIC     Te3/0/1
1037    ac3a.675e.6238    DYNAMIC     Te3/0/1
1037    ac3a.676b.e940    DYNAMIC     Te3/0/1
1037    ac3a.676b.ea5a    DYNAMIC     Te3/0/1
1037    ac3a.676b.eb08    DYNAMIC     Te3/0/1
1037    ac4a.676d.0d3e    DYNAMIC     Te3/0/1
1037    ac4a.676d.38f6    DYNAMIC     Te3/0/1
1037    ac4a.676d.3bf6    DYNAMIC     Te3/0/1
1037    ac4a.676d.3bfe    DYNAMIC     Te3/0/1
1037    ac4a.676d.3c1e    DYNAMIC     Te3/0/1
1037    ac4a.676d.3ca8    DYNAMIC     Te3/0/1
1037    ac7a.562b.7972    DYNAMIC     Te3/0/1
1037    ac7a.562b.7986    DYNAMIC     Te3/0/1
1037    ac7a.562b.7cc4    DYNAMIC     Te3/0/1
1037    ac7a.562b.7cc8    DYNAMIC     Te3/0/1
1037    b026.80df.6246    DYNAMIC     Te3/0/1
1037    b08b.cfa8.1584    DYNAMIC     Te3/0/1
1037    b08b.cfa8.169e    DYNAMIC     Te3/0/1
1037    b827.eb27.ddf1    DYNAMIC     Te3/0/1
1037    b827.eb28.2bc4    DYNAMIC     Te3/0/1
1037    b827.eb93.a06a    DYNAMIC     Te3/0/1
1037    b827.ebd3.3ba2    DYNAMIC     Te3/0/1
1037    b827.ebef.d1c4    DYNAMIC     Te3/0/1
1037    b827.ebf0.1ef6    DYNAMIC     Te3/0/1
1037    b827.ebfb.524f    DYNAMIC     Te3/0/1
1037    cc7f.761e.525e    DYNAMIC     Te3/0/1
1037    cc7f.761e.5278    DYNAMIC     Te3/0/1
1037    cc7f.7623.4ce6    DYNAMIC     Te3/0/1
1037    cc7f.7623.501a    DYNAMIC     Te3/0/1
1037    cc7f.7623.5028    DYNAMIC     Te3/0/1
1037    d46d.5091.e598    DYNAMIC     Te3/0/1
1037    d4c9.3c5a.16a0    DYNAMIC     Te3/0/1
1037    d4c9.3ce6.c2b8    DYNAMIC     Te3/0/1
1037    e41f.7b8c.1402    DYNAMIC     Te3/0/1
1037    e4aa.5d00.12fc    DYNAMIC     Te3/0/1
1037    e4aa.5d6c.a120    DYNAMIC     Te3/0/1
1037    e4aa.5dd2.b500    DYNAMIC     Te3/0/1
1037    e4aa.5dd9.5fc0    DYNAMIC     Te3/0/1
1037    f4cf.e2ac.333c    DYNAMIC     Te3/0/1
1037    f4db.e6bf.e398    DYNAMIC     Te3/0/1
1037    f4db.e6bf.e548    DYNAMIC     Te3/0/1
1037    f4db.e6f4.a31c    DYNAMIC     Te3/0/1
1037    f4db.e6f4.a65a    DYNAMIC     Te3/0/1
1037    f4db.e6f4.aa3c    DYNAMIC     Te3/0/1
1037    f4db.e6f4.aacc    DYNAMIC     Te3/0/1
1037    f4db.e6f4.aad6    DYNAMIC     Te3/0/1
1037    f4db.e6f4.aae0    DYNAMIC     Te3/0/1
1037    f4db.e6f4.c188    DYNAMIC     Te3/0/1
1037    f4db.e6fa.6764    DYNAMIC     Te3/0/1
1037    f4db.e6fd.4660    DYNAMIC     Te3/0/1
1037    f4db.e6fd.46ac    DYNAMIC     Te3/0/1
1037    f4db.e6fd.46ba    DYNAMIC     Te3/0/1
1037    f4db.e6fd.46ee    DYNAMIC     Te3/0/1
1037    f4db.e6fd.4784    DYNAMIC     Te3/0/1
1037    f4db.e6ff.4160    DYNAMIC     Te3/0/1
1037    f4db.e6ff.418e    DYNAMIC     Te3/0/1
1037    f4db.e6ff.41ce    DYNAMIC     Te3/0/1
1037    f4db.e6ff.41da    DYNAMIC     Te3/0/1
          1037    f4db.e6ff.41ec    DYNAMIC     Te3/0/1
1037    f4db.e6ff.41f4    DYNAMIC     Te3/0/1
1037    f4db.e6ff.4232    DYNAMIC     Te3/0/1
1037    f4db.e6ff.5294    DYNAMIC     Te3/0/1
1037    f4db.e6ff.52e6    DYNAMIC     Te3/0/1
1037    f4db.e6ff.552a    DYNAMIC     Te3/0/1
1037    f80b.cbfd.0d30    DYNAMIC     Te3/0/1
1037    f80b.cbfd.0d54    DYNAMIC     Te3/0/1
 125    0000.0c9f.f07d    DYNAMIC     Te3/0/1
 125    0020.4afb.fdd2    DYNAMIC     Te3/0/1
 125    003a.9c3f.d7c1    DYNAMIC     Te3/0/1
 125    003a.9c40.0dc1    DYNAMIC     Te3/0/1
 125    a093.51d2.5c6d    DYNAMIC     Te3/0/1
 125    bce9.2fd4.a616    DYNAMIC     Te3/0/1
1605    0000.0c9f.f645    DYNAMIC     Te3/0/1
1605    0018.8526.1007    DYNAMIC     Gi2/0/5
1605    0018.8526.1020    DYNAMIC     Gi2/0/7
1605    0018.8526.11cd    DYNAMIC     Gi2/0/6
1605    0018.8528.e889    DYNAMIC     Gi2/0/38
1605    003a.9c3f.d7c1    DYNAMIC     Te3/0/1
1605    003a.9c40.0dc1    DYNAMIC     Te3/0/1
1605    0040.8cfa.1b3b    DYNAMIC     Te3/0/1
1605    0040.8cfa.1b48    DYNAMIC     Te3/0/1
1605    0040.8cfa.1b4a    DYNAMIC     Te3/0/1
1605    0040.8cfa.3683    DYNAMIC     Te3/0/1
1605    0040.8cfa.5d75    DYNAMIC     Te3/0/1
1605    0040.8cfa.5d79    DYNAMIC     Te3/0/1
1605    a093.51d2.5c6d    DYNAMIC     Te3/0/1
1605    accc.8e5c.c83b    DYNAMIC     Te3/0/1
1605    accc.8ea1.e489    DYNAMIC     Te3/0/1
1605    accc.8ec1.21fe    DYNAMIC     Te3/0/1
1605    accc.8ec1.21ff    DYNAMIC     Te3/0/1
1605    accc.8ec1.2204    DYNAMIC     Te3/0/1
1605    accc.8ec1.220d    DYNAMIC     Te3/0/1
1605    accc.8ec1.220f    DYNAMIC     Te3/0/1
1605    accc.8ec1.2213    DYNAMIC     Te3/0/1
1209    0000.0c9f.f4b9    DYNAMIC     Te3/0/1
1209    003a.9c3f.d7c1    DYNAMIC     Te3/0/1
1209    003a.9c40.0dc1    DYNAMIC     Te3/0/1
1209    0050.f964.eeb6    DYNAMIC     Te3/0/1
1209    0050.f965.42a4    DYNAMIC     Te3/0/1
1209    0050.f9fe.e7d8    DYNAMIC     Gi6/0/13
1209    a093.51d2.5c6d    DYNAMIC     Te3/0/1
Total Mac Addresses for this criterion: 923""",
 'show run | section tacacs':"""aaa group server tacacs+ NOC-TAC
 server name TAC-EBC
 server name TAC-SECONDARY
tacacs server TAC-EBC
 address ipv4 172.31.17.180
 key 7 09650A0C304112302B0E1D6B
tacacs server TAC-SECONDARY
 address ipv4 10.64.32.5
 key 7 04724F032665496C291B1C56""",
 'show run | in tacacs':"""aaa group server tacacs+ NOC-TAC
tacacs server TAC-EBC
tacacs server TAC-SECONDARY""",
 'show power inline':"""Available:4800.0(w)  Used:166.8(w)  Remaining:4633.2(w)

Interface Admin  Oper            Power(Watts)     Device              Class
                            From PS    To Device                    
--------- ------ ---------- ---------- ---------- ------------------- -----

Gi1/0/1   auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/2   auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/3   auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/4   auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/5   auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/6   auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/7   auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/8   auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/9   auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/10  auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/11  auto   faulty     0.0        0.0        n/a                 n/a  
Gi1/0/12  auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/13  auto   on         4.0        4.0        Ieee PD             1    
Gi1/0/14  auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/15  auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/16  auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/17  auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/18  auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/19  auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/20  auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/21  auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/22  auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/23  auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/24  auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/25  auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/26  auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/27  auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/28  auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/29  auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/30  auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/31  auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/32  auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/33  auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/34  auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/35  auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/36  auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/37  auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/38  auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/39  auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/40  auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/41  auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/42  auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/43  auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/44  auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/45  auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/46  auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/47  auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/48  auto   off        0.0        0.0        n/a                 n/a  
Gi2/0/1   auto   off        0.0        0.0        n/a                 n/a  
Gi2/0/2   auto   off        0.0        0.0        n/a                 n/a  
Gi2/0/3   auto   off        0.0        0.0        n/a                 n/a  
Gi2/0/4   auto   off        0.0        0.0        n/a                 n/a  
          Interface Admin  Oper            Power(Watts)     Device              Class
                            From PS    To Device                    
--------- ------ ---------- ---------- ---------- ------------------- -----

Gi2/0/5   auto   on         15.4       15.4       Ieee PD             0    
Gi2/0/6   auto   on         15.4       15.4       Ieee PD             0    
Gi2/0/7   auto   on         15.4       15.4       Ieee PD             0    
Gi2/0/8   auto   off        0.0        0.0        n/a                 n/a  
Gi2/0/9   auto   off        0.0        0.0        n/a                 n/a  
Gi2/0/10  auto   off        0.0        0.0        n/a                 n/a  
Gi2/0/11  auto   off        0.0        0.0        n/a                 n/a  
Gi2/0/12  auto   off        0.0        0.0        n/a                 n/a  
Gi2/0/13  auto   off        0.0        0.0        n/a                 n/a  
Gi2/0/14  auto   off        0.0        0.0        n/a                 n/a  
Gi2/0/15  auto   off        0.0        0.0        n/a                 n/a  
Gi2/0/16  auto   off        0.0        0.0        n/a                 n/a  
Gi2/0/17  auto   off        0.0        0.0        n/a                 n/a  
Gi2/0/18  auto   off        0.0        0.0        n/a                 n/a  
Gi2/0/19  auto   off        0.0        0.0        n/a                 n/a  
Gi2/0/20  auto   off        0.0        0.0        n/a                 n/a  
Gi2/0/21  auto   off        0.0        0.0        n/a                 n/a  
Gi2/0/22  auto   off        0.0        0.0        n/a                 n/a  
Gi2/0/23  auto   off        0.0        0.0        n/a                 n/a  
Gi2/0/24  auto   off        0.0        0.0        n/a                 n/a  
Gi2/0/25  auto   off        0.0        0.0        n/a                 n/a  
Gi2/0/26  auto   off        0.0        0.0        n/a                 n/a  
Gi2/0/27  auto   off        0.0        0.0        n/a                 n/a  
Gi2/0/28  auto   off        0.0        0.0        n/a                 n/a  
Gi2/0/29  auto   off        0.0        0.0        n/a                 n/a  
Gi2/0/30  auto   off        0.0        0.0        n/a                 n/a  
Gi2/0/31  auto   off        0.0        0.0        n/a                 n/a  
Gi2/0/32  auto   off        0.0        0.0        n/a                 n/a  
Gi2/0/33  auto   off        0.0        0.0        n/a                 n/a  
Gi2/0/34  auto   off        0.0        0.0        n/a                 n/a  
Gi2/0/35  auto   off        0.0        0.0        n/a                 n/a  
Gi2/0/36  auto   off        0.0        0.0        n/a                 n/a  
Gi2/0/37  auto   off        0.0        0.0        n/a                 n/a  
Gi2/0/38  auto   on         15.4       15.4       Ieee PD             3    
Gi2/0/39  auto   off        0.0        0.0        n/a                 n/a  
Gi2/0/40  auto   off        0.0        0.0        n/a                 n/a  
Gi2/0/41  auto   off        0.0        0.0        n/a                 n/a  
Gi2/0/42  auto   off        0.0        0.0        n/a                 n/a  
Gi2/0/43  auto   off        0.0        0.0        n/a                 n/a  
Gi2/0/44  auto   off        0.0        0.0        n/a                 n/a  
Gi2/0/45  auto   off        0.0        0.0        n/a                 n/a  
Gi2/0/46  auto   off        0.0        0.0        n/a                 n/a  
Gi2/0/47  auto   off        0.0        0.0        n/a                 n/a  
Gi2/0/48  auto   off        0.0        0.0        n/a                 n/a  
Gi5/0/1   auto   off        0.0        0.0        n/a                 n/a  
Gi5/0/2   auto   off        0.0        0.0        n/a                 n/a  
Gi5/0/3   auto   off        0.0        0.0        n/a                 n/a  
Gi5/0/4   auto   off        0.0        0.0        n/a                 n/a  
Gi5/0/5   auto   off        0.0        0.0        n/a                 n/a  
Gi5/0/6   auto   off        0.0        0.0        n/a                 n/a  
Gi5/0/7   auto   off        0.0        0.0        n/a                 n/a  
Gi5/0/8   auto   off        0.0        0.0        n/a                 n/a  
Gi5/0/9   auto   off        0.0        0.0        n/a                 n/a  
Gi5/0/10  auto   off        0.0        0.0        n/a                 n/a  
Gi5/0/11  auto   off        0.0        0.0        n/a                 n/a  
Gi5/0/12  auto   off        0.0        0.0        n/a                 n/a  
Gi5/0/13  auto   off        0.0        0.0        n/a                 n/a  
Gi5/0/14  auto   off        0.0        0.0        n/a                 n/a  
Gi5/0/15  auto   off        0.0        0.0        n/a                 n/a  
          Interface Admin  Oper            Power(Watts)     Device              Class
                            From PS    To Device                    
--------- ------ ---------- ---------- ---------- ------------------- -----

Gi5/0/16  auto   off        0.0        0.0        n/a                 n/a  
Gi5/0/17  auto   off        0.0        0.0        n/a                 n/a  
Gi5/0/18  auto   off        0.0        0.0        n/a                 n/a  
Gi5/0/19  auto   off        0.0        0.0        n/a                 n/a  
Gi5/0/20  auto   off        0.0        0.0        n/a                 n/a  
Gi5/0/21  auto   off        0.0        0.0        n/a                 n/a  
Gi5/0/22  auto   off        0.0        0.0        n/a                 n/a  
Gi5/0/23  auto   off        0.0        0.0        n/a                 n/a  
Gi5/0/24  auto   off        0.0        0.0        n/a                 n/a  
Gi5/0/25  off    off        0.0        0.0        n/a                 n/a  
Gi5/0/26  off    off        0.0        0.0        n/a                 n/a  
Gi5/0/27  off    off        0.0        0.0        n/a                 n/a  
Gi5/0/28  off    off        0.0        0.0        n/a                 n/a  
Gi5/0/29  off    off        0.0        0.0        n/a                 n/a  
Gi5/0/30  off    off        0.0        0.0        n/a                 n/a  
Gi5/0/31  auto   off        0.0        0.0        n/a                 n/a  
Gi5/0/32  auto   off        0.0        0.0        n/a                 n/a  
Gi5/0/33  auto   off        0.0        0.0        n/a                 n/a  
Gi5/0/34  auto   off        0.0        0.0        n/a                 n/a  
Gi5/0/35  auto   off        0.0        0.0        n/a                 n/a  
Gi5/0/36  auto   off        0.0        0.0        n/a                 n/a  
Gi5/0/37  auto   off        0.0        0.0        n/a                 n/a  
Gi5/0/38  auto   off        0.0        0.0        n/a                 n/a  
Gi5/0/39  auto   off        0.0        0.0        n/a                 n/a  
Gi5/0/40  auto   off        0.0        0.0        n/a                 n/a  
Gi5/0/41  auto   off        0.0        0.0        n/a                 n/a  
Gi5/0/42  auto   off        0.0        0.0        n/a                 n/a  
Gi5/0/43  auto   off        0.0        0.0        n/a                 n/a  
Gi5/0/44  auto   on         30.0       30.0       AIR-AP2802I-B-K9    4    
Gi5/0/45  auto   on         30.0       30.0       AIR-AP2802I-B-K9    4    
Gi5/0/46  auto   off        0.0        0.0        n/a                 n/a  
Gi5/0/47  auto   on         15.4       15.4       Ieee PD             0    
Gi5/0/48  auto   off        0.0        0.0        n/a                 n/a  
Gi6/0/1   auto   off        0.0        0.0        n/a                 n/a  
Gi6/0/2   auto   off        0.0        0.0        n/a                 n/a  
Gi6/0/3   auto   off        0.0        0.0        n/a                 n/a  
Gi6/0/4   auto   off        0.0        0.0        n/a                 n/a  
Gi6/0/5   auto   off        0.0        0.0        n/a                 n/a  
Gi6/0/6   auto   off        0.0        0.0        n/a                 n/a  
Gi6/0/7   auto   off        0.0        0.0        n/a                 n/a  
Gi6/0/8   auto   off        0.0        0.0        n/a                 n/a  
Gi6/0/9   auto   off        0.0        0.0        n/a                 n/a  
Gi6/0/10  auto   off        0.0        0.0        n/a                 n/a  
Gi6/0/11  auto   off        0.0        0.0        n/a                 n/a  
Gi6/0/12  auto   off        0.0        0.0        n/a                 n/a  
Gi6/0/13  auto   off        0.0        0.0        n/a                 n/a  
Gi6/0/14  auto   off        0.0        0.0        n/a                 n/a  
Gi6/0/15  auto   off        0.0        0.0        n/a                 n/a  
Gi6/0/16  auto   off        0.0        0.0        n/a                 n/a  
Gi6/0/17  auto   off        0.0        0.0        n/a                 n/a  
Gi6/0/18  auto   off        0.0        0.0        n/a                 n/a  
Gi6/0/19  auto   off        0.0        0.0        n/a                 n/a  
Gi6/0/20  auto   on         8.6        8.6        AIR-AP1815W-B-K9    4    
Gi6/0/21  auto   off        0.0        0.0        n/a                 n/a  
Gi6/0/22  auto   on         8.6        8.6        AIR-AP1815W-B-K9    4    
Gi6/0/23  auto   off        0.0        0.0        n/a                 n/a  
Gi6/0/24  auto   on         8.6        8.6        AIR-AP1815W-B-K9    4    
Gi6/0/25  auto   off        0.0        0.0        n/a                 n/a  
Gi6/0/26  auto   off        0.0        0.0        n/a                 n/a  
          Interface Admin  Oper            Power(Watts)     Device              Class
                            From PS    To Device                    
--------- ------ ---------- ---------- ---------- ------------------- -----

Gi6/0/27  auto   off        0.0        0.0        n/a                 n/a  
Gi6/0/28  auto   off        0.0        0.0        n/a                 n/a  
Gi6/0/29  auto   off        0.0        0.0        n/a                 n/a  
Gi6/0/30  auto   off        0.0        0.0        n/a                 n/a  
Gi6/0/31  auto   off        0.0        0.0        n/a                 n/a  
Gi6/0/32  auto   off        0.0        0.0        n/a                 n/a  
Gi6/0/33  auto   off        0.0        0.0        n/a                 n/a  
Gi6/0/34  auto   off        0.0        0.0        n/a                 n/a  
Gi6/0/35  auto   off        0.0        0.0        n/a                 n/a  
Gi6/0/36  auto   off        0.0        0.0        n/a                 n/a  
Gi6/0/37  auto   off        0.0        0.0        n/a                 n/a  
Gi6/0/38  auto   off        0.0        0.0        n/a                 n/a  
Gi6/0/39  auto   off        0.0        0.0        n/a                 n/a  
Gi6/0/40  auto   off        0.0        0.0        n/a                 n/a  
Gi6/0/41  auto   off        0.0        0.0        n/a                 n/a  
Gi6/0/42  auto   off        0.0        0.0        n/a                 n/a  
Gi6/0/43  auto   off        0.0        0.0        n/a                 n/a  
Gi6/0/44  auto   off        0.0        0.0        n/a                 n/a  
Gi6/0/45  auto   off        0.0        0.0        n/a                 n/a  
Gi6/0/46  auto   off        0.0        0.0        n/a                 n/a  
Gi6/0/47  auto   off        0.0        0.0        n/a                 n/a  
Gi6/0/48  auto   off        0.0        0.0        n/a                 n/a  
--------- ------ ---------- ---------- ---------- ------------------- -----

Totals:          11   on    166.8      166.8     
""",
 'show environment all':"""Sensor List:  Environmental Monitoring 
 Sensor           Location          State             Reading
 Temp: Coretemp   R0                Normal            46 Celsius
 Temp: DopplerD   R0                Normal            53 Celsius
 V1: VX1          R0                Normal            872 mV
 V1: VX2          R0                Normal            1504 mV
 V1: VX3          R0                Normal            1055 mV
 V1: VX4          R0                Normal            852 mV
 V1: VX5          R0                Normal            1514 mV
 V1: VX6          R0                Normal            1305 mV
 V1: VX7          R0                Normal            1005 mV
 V1: VX8          R0                Normal            1100 mV
 V1: VX9          R0                Normal            1203 mV
 V1: VX10         R0                Normal            1703 mV
 V1: VX11         R0                Normal            1226 mV
 V1: VX12         R0                Normal            1799 mV
 V1: VX13         R0                Normal            2506 mV
 V1: VX14         R0                Normal            3295 mV
 V1: VX15         R0                Normal            5052 mV
 V1: VX16         R0                Normal            900 mV
 Temp:   outlet   R0                Normal            37 Celsius
 Temp:    inlet   R0                Normal            24 Celsius
 HotSwap: Volts   R0                Normal            53 V DC
 HotSwap: Power   R0                Normal            265 Watts
 V1: VX1          1/0               Normal            1000 mV
 V1: VX2          1/0               Normal            1497 mV
 V1: VX3          1/0               Normal            1801 mV
 V1: VX4          1/0               Normal            3294 mV
 V1: VX5          1/0               Normal            3335 mV
 V1: VX6          1/0               Normal            1502 mV
 V1: VX7          1/0               Normal            1029 mV
 V1: VX8          1/0               Normal            3298 mV
 V1: VX9          1/0               Normal            12039 mV
 V1: VX10         1/0               Normal            1000 mV
 V1: VX11         1/0               Normal            1030 mV
 Temp:   Outlet   1/0               Normal            27 Celsius
 Temp:    Inlet   1/0               Normal            21 Celsius
 HotSwap: Volts   1/0               Normal            53 V DC
 HotSwap: Power   1/0               Normal            434 Watts
 V1: VX1          2/0               Normal            1000 mV
 V1: VX2          2/0               Normal            1500 mV
 V1: VX3          2/0               Normal            1798 mV
 V1: VX4          2/0               Normal            3290 mV
 V1: VX5          2/0               Normal            3324 mV
 V1: VX6          2/0               Normal            1499 mV
 V1: VX7          2/0               Normal            1030 mV
 V1: VX8          2/0               Normal            3294 mV
 V1: VX9          2/0               Normal            12019 mV
 V1: VX10         2/0               Normal            999 mV
 V1: VX11         2/0               Normal            1033 mV
 Temp:   Outlet   2/0               Normal            27 Celsius
 Temp:    Inlet   2/0               Normal            21 Celsius
 HotSwap: Volts   2/0               Normal            53 V DC
 HotSwap: Power   2/0               Normal            420 Watts
 V1: VX1          5/0               Normal            1003 mV
 V1: VX2          5/0               Normal            1504 mV
 V1: VX3          5/0               Normal            1801 mV
 V1: VX4          5/0               Normal            3290 mV
 V1: VX5          5/0               Normal            3331 mV
           V1: VX6          5/0               Normal            1501 mV
 V1: VX7          5/0               Normal            1030 mV
 V1: VX8          5/0               Normal            3301 mV
 V1: VX9          5/0               Normal            12059 mV
 V1: VX10         5/0               Normal            1000 mV
 V1: VX11         5/0               Normal            1031 mV
 Temp:   Outlet   5/0               Normal            28 Celsius
 Temp:    Inlet   5/0               Normal            22 Celsius
 HotSwap: Volts   5/0               Normal            53 V DC
 HotSwap: Power   5/0               Normal            429 Watts
 V1: VX1          6/0               Normal            996 mV
 V1: VX2          6/0               Normal            1500 mV
 V1: VX3          6/0               Normal            1801 mV
 V1: VX4          6/0               Normal            3301 mV
 V1: VX5          6/0               Normal            3349 mV
 V1: VX6          6/0               Normal            1498 mV
 V1: VX7          6/0               Normal            1030 mV
 V1: VX8          6/0               Normal            3312 mV
 V1: VX9          6/0               Normal            12063 mV
 V1: VX10         6/0               Normal            1005 mV
 V1: VX11         6/0               Normal            1036 mV
 Temp:   Outlet   6/0               Normal            27 Celsius
 Temp:    Inlet   6/0               Normal            22 Celsius
 HotSwap: Volts   6/0               Normal            53 V DC
 HotSwap: Power   6/0               Normal            435 Watts

""",
}
