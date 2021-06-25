ip_address = '172.20.64.14'
software = 'software'
hardware = 'hardware'
read_results = {
 'show version':"""Cisco IOS XE Software, Version 16.06.04a
Cisco IOS Software [Everest], Catalyst L3 Switch Software (CAT9K_IOSXE), Version 16.6.4a, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2018 by Cisco Systems, Inc.
Compiled Fri 26-Oct-18 18:15 by mcpre


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

dx2-525hosp-4659-clinical uptime is 21 weeks, 5 days, 5 hours, 51 minutes
Uptime for this control processor is 21 weeks, 5 days, 5 hours, 53 minutes
System returned to ROM by PowerOn
System restarted at 09:23:41 MST Sun Jan 24 2021
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

cisco C9410R (X86) processor (revision V01) with 1916969K/6147K bytes of memory.
Processor board ID FXS2226Q030
2 Virtual Ethernet interfaces
144 Gigabit Ethernet interfaces
          32 Ten Gigabit Ethernet interfaces
2 Forty Gigabit Ethernet interfaces
32768K bytes of non-volatile configuration memory.
15958444K bytes of physical memory.
10444800K bytes of Bootflash at bootflash:.
1638400K bytes of Crash Files at crashinfo:.
0K bytes of WebUI ODM Files at webui:.

Configuration register is 0x102
""",
 'show run':"""Building configuration...

Current configuration : 44767 bytes
!
! Last configuration change at 13:13:02 MDT Thu May 27 2021 by u0597604
! NVRAM config last updated at 21:24:35 MDT Sun Jun 20 2021 by noc-orionncm
!
version 16.6
no service pad
service timestamps debug datetime msec localtime
service timestamps log datetime msec localtime
service password-encryption
service compress-config
no platform punt-keepalive disable-kernel-core
!
hostname dx2-525hosp-4659-clinical
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
enable secret 5 $1$axNH$F8lnlmQIXo9T3kUghtDYo1
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
power supply autoLC priority 1 2 3 4 7 8 9 10
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
ip dhcp snooping vlan 1-4094
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

ipv6 mld snooping
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
  69666963 6174652D 33363631 32313036 3036301E 170D3139 30313331 31313037 
  30385A17 0D323030 31303130 30303030 305A3031 312F302D 06035504 03132649 
  4F532D53 656C662D 5369676E 65642D43 65727469 66696361 74652D33 36363132 
  31303630 36308201 22300D06 092A8648 86F70D01 01010500 0382010F 00308201 
  0A028201 0100A1C2 FC23DF5E BE83C364 5D78856E 1C327F78 E3B27772 27869DED 
  C4A0A20D 790D76A8 57760BA0 282AE693 ECCC652C DDB90D19 03091726 96AAAFF1 
  5F72AC68 211138E7 5493BBD0 3B8B0553 E47AE6A8 193E3D52 03821610 982E5E6D 
  A527BA1E BF978E46 D2920970 DDBC0297 4E6459F4 9AB2EF97 25414DB5 1C225464 
  906C4EAB 545C136D CFF974AE EAA74726 577D7074 13A070E0 8E0AB0B1 58026502 
  F443C932 58973385 8F0A3F04 AC5E9534 FAB5258F 8BCB54C6 7D34F723 E948820F 
  81D5E1FB D8B3EAAB D83F5BD7 3693BF59 6922B66E 6880F81A FCFA3C3E D233EFDC 
  B4ECCC87 08FAB8A9 6051A15D C60D373E 14EE0911 442D8662 8879AAE5 8B885AC1 
  5C9C835C F1AB0203 010001A3 53305130 0F060355 1D130101 FF040530 030101FF 
  301F0603 551D2304 18301680 14783AF5 63526003 79B6FA4A 1A7DA70E 7EF1EC91 
  A7301D06 03551D0E 04160414 783AF563 52600379 B6FA4A1A 7DA70E7E F1EC91A7 
  300D0609 2A864886 F70D0101 05050003 82010100 7368BFB8 C0E91BCC 8E4F10F4 
  B07EC667 F9077AEC 2DDE5BFD DC641A07 A536314C AE10CF99 9CBE92F0 65F048CB 
  59A5E80C C8DFDA0F 22AD04F8 815B20B3 A6FAB5EF 828C48B5 66FA2701 43D0716B 
  A23C00C7 5BC7F7D4 7F24852F 22DF4289 28AEAB43 3A282E03 8CF73955 E614EA7E 
  FBE1C9BB 02FF8575 9177E1B5 78F2C757 88C86030 5C5182B1 8DBCBCB4 9F2039D9 
  A23111AF 4BB44DB5 68E75D97 4CD87952 1959A7DC 961D0389 674325DF 76AE64CE 
  5C6A2A42 33131FDD BE19166D 99844259 A4370EA0 754A19CA E0C0B315 AE4D983C 
  092024BA D888D234 C3987E0C 2053AC30 7FD308CA 14ED1082 B7796F89 59C11DA8 
  833A6DBE 53940014 24126409 677C0884 8E74375E
  	quit
!
!
!
diagnostic bootup level minimal
!
spanning-tree mode rapid-pvst
spanning-tree extend system-id
spanning-tree vlan 1-4094 priority 16384
no errdisable detect cause gbic-invalid
errdisable recovery cause udld
errdisable recovery cause storm-control
!
!
redundancy
 mode sso
!
!
vlan 123
 name Clin-525Hosp-FloorB-Zeroclients
!
vlan 124
 name Clin-525Hosp-FloorA-Zeroclients
!
vlan 125
 name Clin-525Hosp-Floor1W-Zeroclients
!
vlan 126
           name Clin-525Hosp-Floor1E-Zeroclients
!
vlan 127
 name Clin-525Hosp-Floor2-Zeroclients
!
vlan 128
 name Clin-525Hosp-Floor3-Zeroclients
!
vlan 129
 name Clin-525Hosp-Floor4-Zeroclients
!
vlan 130
 name Clin-525Hosp-Floor5-Zeroclients
!
vlan 131
 name Clin-525Hosp-Floor6-Zeroclients
!
vlan 132
 name Clin-525Hosp-OR-CPA-Zeroclients
!
vlan 270
 name clinical-525hosp-kronosclocks
!
vlan 332
 name 525-mgmt
!
vlan 337
 name ob_trac_vu
!
vlan 338
 name clin-525hosp_ABACUS
!
vlan 341
 name bldg_525_env
!
vlan 345
 name hosp_bed_monitoring
!
vlan 396
 name bldg-525-printer
!
vlan 418
 name fw-525hosp-4671-phillips
!
vlan 540
 name 525-PACS
!
vlan 551
 name clinical-525hosp-A-omnicell
!
vlan 575
 name clin-525-LAN-1-infill
!
vlan 600
 name 525OR-OmniCell
!
vlan 607
 name clin-525-iStar
!
          vlan 610
 name clinical-525hosp-flr4-omnicell
!
vlan 620
 name bldg342-fm
!
vlan 629
 name 525-RadTech-Lan
!
vlan 630
 name 525-lan-6
!
vlan 631
 name 525-lan-5
!
vlan 632
 name 525-lan-4
!
vlan 633
 name 525-lan-3
!
vlan 634
 name 525-lan-2
!
vlan 635
 name 525-lan-1e
!
vlan 636
 name 525-lan-1w
!
vlan 637
 name 525-lan-a
!
vlan 638
 name 525-lan-b
!
vlan 640
 name EP-MRI
!
vlan 680
 name clin-525hospBAS-fm
!
vlan 732
 name clinical-525hosp-swisstube
!
vlan 770
 name 525-OR-CPA
!
vlan 771
 name 525-radiology-lan
!
vlan 772
 name 525-OR-CPA-1
!
vlan 773
 name clinical-525hosp-ATTmetrocell
!
vlan 850
 name clin-services-mgmt
          !
vlan 921
 name Phillips_Monitoring_525
!
vlan 942
 name VoIP-526-HGP
!
vlan 983
 name VoIP-525-A
!
vlan 984
 name voIP-525-1
!
vlan 986
 name VoIP-525-2
!
vlan 987
 name VoIP-525-3
!
vlan 988
 name VoIP-525-4
!
vlan 989
 name VoIP-525-5
!
vlan 990
 name VoIP-525-6
!
vlan 1037
 name 525-wmgmt
!
vlan 1041
 name clinical-525-AV
!
vlan 1060
 name clin-525-paging
!
vlan 1075
 name 525-nac-untrust
!
vlan 1076
 name 525-nac-trust
!
vlan 1112
 name main-rtls
!
vlan 1209
 name clinical-0525hosp-ccure
!
vlan 1600
 name clin-525hosp_pharmcam
!
vlan 1605
 name clin-bldg525-fm-cam
!
vlan 1616
 name clin-525-infill-FMcam
!
vlan 1621
           name clin-525hosp_pharmcam-1
!
vlan 1672
 name clin-526hgp-fm
!
vlan 1700
 name Clin-525Hosp-PatientMonCam
!
vlan 1800
 name em-radio-dx2-525hosp-4659
!
vlan 1900 
!
vlan 3000
 name clin-codeblue
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
  description Learning cache ovfl, Crypto Control, Exception, EGR Exception, NFL SAMPLED DATA, RPF Failed
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
class-map match-any system-cpp-police-control-low-priority
  description General punt
class-map match-any non-client-nrt-class
class-map match-any system-cpp-police-routing-control
  description Routing control
class-map match-any system-cpp-police-protocol-snooping
  description Protocol snooping
class-map match-any system-cpp-police-system-critical
  description System Critical and Gold pkt
!
policy-map system-cpp-policy
 class system-cpp-police-control-low-priority
  police rate 200 pps
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
 description key:Uplink to dist nodes
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
interface GigabitEthernet1/0/1
 switchport access vlan 607
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet1/0/2
 switchport access vlan 607
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet1/0/3
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet1/0/4
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet1/0/5
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet1/0/6
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
          !
interface GigabitEthernet1/0/7
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet1/0/8
 switchport access vlan 771
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet1/0/9
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet1/0/10
 description #swisstube
 switchport access vlan 732
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/11
 switchport access vlan 270
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet1/0/12
 switchport access vlan 270
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet1/0/13
 description #Omnicell
 switchport access vlan 600
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/14
 description #New OR HVAC RITM0300645
 switchport access vlan 341
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/15
 description #Omnicell
 switchport access vlan 600
 switchport mode access
 speed 10
 spanning-tree portfast
!
interface GigabitEthernet1/0/16
 description #Omnicell
 switchport access vlan 600
           switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/17
 switchport access vlan 341
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet1/0/18
 description #BMDI 100/full
 switchport access vlan 418
 speed 100
 duplex full
 spanning-tree portfast
!
interface GigabitEthernet1/0/19
 description #RTLS
 switchport access vlan 1112
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet1/0/20
 description #RTLS
 switchport access vlan 1112
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet1/0/21
 switchport access vlan 1041
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet1/0/22
 switchport access vlan 1041
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet1/0/23
 description Wireless AP
 switchport access vlan 1037
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/24
 description Wireless AP
 switchport access vlan 1037
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/25
 switchport access vlan 396
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
          !
interface GigabitEthernet1/0/26
 switchport access vlan 396
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet1/0/27
 switchport access vlan 396
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet1/0/28
 switchport access vlan 396
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet1/0/29
 switchport access vlan 396
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet1/0/30
 switchport access vlan 396
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet1/0/31
 switchport access vlan 396
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet1/0/32
 switchport access vlan 396
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet1/0/33
 switchport access vlan 396
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet1/0/34
 switchport access vlan 396
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet1/0/35
 switchport access vlan 396
 switchport mode access
 switchport voice vlan 988
           spanning-tree portfast
!
interface GigabitEthernet1/0/36
 switchport access vlan 396
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet1/0/37
 description NetBeez
 switchport access vlan 1037
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet1/0/38
 description #AP
 switchport access vlan 1037
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet1/0/39
 description #AP
 switchport access vlan 1037
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet1/0/40
 description #AP
 switchport access vlan 1037
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet1/0/41
 description #AP
 switchport access vlan 1037
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet1/0/42
 description #AP
 switchport access vlan 1037
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet1/0/43
 description #AP
 switchport access vlan 1037
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet1/0/44
 description #AP
           switchport access vlan 1037
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet1/0/45
 description #AP
 switchport access vlan 1037
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet1/0/46
 description #AP
 switchport access vlan 1037
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet1/0/47
 description #Emergency Radio (on roof)
 switchport access vlan 1900
 switchport mode access
 power inline never
!
interface GigabitEthernet1/0/48
 description #AP
 switchport access vlan 1037
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface TenGigabitEthernet4/0/1
 description key:sx1-525hosp-1511:ten5/1
 switchport mode trunk
 switchport priority extend trust
 storm-control broadcast level 2.00
 storm-control action shutdown
 storm-control action trap
!
interface TenGigabitEthernet4/0/2
 description key:sx1-525hosp-b244:ten5/2
 switchport mode trunk
 switchport priority extend trust
 storm-control broadcast level 2.00
 storm-control action shutdown
 storm-control action trap
!
interface TenGigabitEthernet4/0/3
 description key:sx1-525hosp-4270:ten1/1
 switchport mode trunk
 switchport priority extend trust
 storm-control broadcast level 2.00
 storm-control action shutdown
 storm-control action trap
!
interface TenGigabitEthernet4/0/4
 description key:sx1-525hosp-3043:ten1/2
 switchport mode trunk
           switchport priority extend trust
 storm-control broadcast level 2.00
 storm-control action shutdown
 storm-control action trap
!
interface TenGigabitEthernet4/0/5
 description key:sx1-525hosp-1873:ten1/2
 switchport mode trunk
 switchport priority extend trust
 storm-control broadcast level 2.00
 storm-control action shutdown
 storm-control action trap
!
interface TenGigabitEthernet4/0/6
 description key:sx2-525hosp-3745:ten5/1
 switchport mode trunk
 switchport priority extend trust
 storm-control broadcast level 2.00
 storm-control action shutdown
 storm-control action trap
!
interface TenGigabitEthernet4/0/7
 description key:sx1-525hosp-3745:ten5/1
 switchport mode trunk
 switchport priority extend trust
 storm-control broadcast level 2.00
 storm-control action shutdown
 storm-control action trap
!
interface TenGigabitEthernet4/0/8
 description key:sx1-525hosp-3306:ten5/1
 switchport mode trunk
 switchport priority extend trust
 storm-control broadcast level 2.00
 storm-control action shutdown
 storm-control action trap
!
interface TenGigabitEthernet4/0/9
 description key:sx2-525hosp-a371:t1/1/2
 switchport mode trunk
 switchport priority extend trust
 storm-control broadcast level 2.00
 storm-control action shutdown
 storm-control action trap
!
interface TenGigabitEthernet4/0/10
 description key:sx1-525hosp-4317:ten5/2
 switchport trunk allowed vlan 129,270,332,341,345,357,380,396,540,607,610,632
 switchport trunk allowed vlan add 681,732,770,921,988,1037,1075,1076
 switchport mode trunk
 switchport priority extend trust
 storm-control broadcast level 2.00
 storm-control action shutdown
 storm-control action trap
!
interface TenGigabitEthernet4/0/11
 description key:sx1-525hosp-1443:ten1/2
 switchport trunk allowed vlan 125,332,341,396,540,607,636,681,732,984,1037
 switchport trunk allowed vlan add 1075,1076,1209,1605
           switchport mode trunk
 switchport priority extend trust
 storm-control broadcast level 2.00
 storm-control action shutdown
 storm-control action trap
!
interface TenGigabitEthernet4/0/12
!
interface TenGigabitEthernet4/0/13
 description key:sx1-525hosp-5105:ten5/2
 switchport mode trunk
 switchport priority extend trust
 storm-control broadcast level 2.00
 storm-control action shutdown
 storm-control action trap
!
interface TenGigabitEthernet4/0/14
 description key:sx1-525hosp-6103:ten5/2
 switchport mode trunk
 switchport priority extend trust
 storm-control broadcast level 2.00
 storm-control action shutdown
 storm-control action trap
!
interface TenGigabitEthernet4/0/15
 description key:sx1-525hosp-a371:ten5/2
 switchport trunk allowed vlan 124,270,332,338,341,396,551,637,732,773,983,1037
 switchport trunk allowed vlan add 1060,1600,1605,1621
 switchport mode trunk
 switchport priority extend trust
 storm-control broadcast level 2.00
 storm-control action shutdown
 storm-control action trap
!
interface TenGigabitEthernet4/0/16
 description key:sx1-525hosp-2411:ten5/1
 switchport mode trunk
 switchport priority extend trust
 storm-control broadcast level 2.00
 storm-control action shutdown
 storm-control action trap
!
interface TenGigabitEthernet4/0/17
 description key:sx1-525hosp-2741:ten5/2
 switchport mode trunk
 switchport priority extend trust
 storm-control broadcast level 2.00
 storm-control action shutdown
 storm-control action trap
!
interface TenGigabitEthernet4/0/18
 description key:sx2-525hosp-4317:te1/1/2
 switchport trunk allowed vlan 129,270,332,341,345,357,380,396,540,551,607,610
 switchport trunk allowed vlan add 632,681,732,770,921,988,1037,1075,1076,1112
 switchport mode trunk
 storm-control broadcast level 2.00
 storm-control action shutdown
 storm-control action trap
!
          interface TenGigabitEthernet4/0/19
 description #key:sx1-525hosp-4625:e5/2
 switchport mode trunk
 switchport priority extend trust
 storm-control broadcast level 2.00
 storm-control action shutdown
 storm-control action trap
!
interface TenGigabitEthernet4/0/20
 description key:sx1-525hosp-2673:t1/1/3
 switchport trunk allowed vlan 128,332,341,396,600,607,633,655,770,772,987,1037
 switchport mode trunk
 load-interval 30
 storm-control broadcast level 2.00
 storm-control action shutdown
 storm-control action trap
!
interface TenGigabitEthernet4/0/21
 storm-control broadcast level 2.00
 storm-control action shutdown
 storm-control action trap
!
interface TenGigabitEthernet4/0/22
 description key:sx1-525hosp-1437b:t5/1
 switchport mode trunk
 switchport priority extend trust
 storm-control broadcast level 2.00
 storm-control action shutdown
 storm-control action trap
!
interface TenGigabitEthernet4/0/23
 description key:sx1-525hosp-2255:g2/1/1
 switchport trunk allowed vlan 124,127,270,332,338,341,396,551,600,607,634,637
 switchport trunk allowed vlan add 732,986,1037,1075,1076,1112,1605,1621
 switchport mode trunk
 switchport priority extend trust
 storm-control broadcast level 2.00
 storm-control action shutdown
 storm-control action trap
!
interface TenGigabitEthernet4/0/24
 description key:sx1-525hosp-a673:g1/0/49
 switchport trunk allowed vlan 124,270,332,341,396,551,607,629,637,732,942,983
 switchport trunk allowed vlan add 1037,1075,1076,1112,1209,1605,1672
 switchport mode trunk
 switchport priority extend trust
 storm-control broadcast level 2.00
 storm-control action shutdown
 storm-control action trap
!
interface TenGigabitEthernet5/0/1
 description key:r1-clinical:e2/10
 switchport mode trunk
 channel-group 30 mode active
 ip dhcp snooping trust
!
interface TenGigabitEthernet5/0/2
 description key:r2-clinical:e2/10
 switchport mode trunk
           channel-group 30 mode active
 ip dhcp snooping trust
!
interface TenGigabitEthernet5/0/3
 description t5/0/3:sx1-525-infill:t5/0/2
 switchport mode trunk
!
interface TenGigabitEthernet5/0/4
 description t5/0/4:sx2-525infill:t1/0/2
 switchport mode trunk
!
interface TenGigabitEthernet5/0/5
 description t5/0/5:sx1-525-1408:t1/1/2
 switchport mode trunk
!
interface TenGigabitEthernet5/0/6
 description t5/0/6:sx1-525-1408:t5/0/2
 switchport mode trunk
!
interface TenGigabitEthernet5/0/7
 switchport mode trunk
!
interface TenGigabitEthernet5/0/8
 description #temp uplink to old switch
 switchport mode trunk
 ip dhcp snooping trust
!
interface FortyGigabitEthernet5/0/9
!
interface FortyGigabitEthernet5/0/10
!
interface GigabitEthernet7/0/1
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet7/0/2
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet7/0/3
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet7/0/4
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet7/0/5
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
           spanning-tree portfast
!
interface GigabitEthernet7/0/6
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet7/0/7
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet7/0/8
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet7/0/9
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet7/0/10
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet7/0/11
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet7/0/12
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet7/0/13
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet7/0/14
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet7/0/15
 switchport access vlan 632
 switchport mode access
           switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet7/0/16
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet7/0/17
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet7/0/18
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet7/0/19
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet7/0/20
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet7/0/21
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet7/0/22
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet7/0/23
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet7/0/24
 switchport access vlan 123
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet7/0/25
 switchport access vlan 632
           switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet7/0/26
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet7/0/27
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet7/0/28
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet7/0/29
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet7/0/30
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet7/0/31
 switchport access vlan 396
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet7/0/32
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet7/0/33
 description Paging
 switchport access vlan 1060
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet7/0/34
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet7/0/35
           switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet7/0/36
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet7/0/37
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet7/0/38
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet7/0/39
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet7/0/40
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet7/0/41
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet7/0/42
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet7/0/43
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet7/0/44
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
          interface GigabitEthernet7/0/45
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet7/0/46
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet7/0/47
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet7/0/48
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet8/0/1
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet8/0/2
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet8/0/3
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet8/0/4
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet8/0/5
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet8/0/6
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
          !
interface GigabitEthernet8/0/7
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet8/0/8
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet8/0/9
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet8/0/10
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet8/0/11
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet8/0/12
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet8/0/13
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet8/0/14
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet8/0/15
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet8/0/16
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
           spanning-tree portfast
!
interface GigabitEthernet8/0/17
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet8/0/18
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet8/0/19
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet8/0/20
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet8/0/21
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet8/0/22
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet8/0/23
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet8/0/24
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet8/0/25
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet8/0/26
 switchport access vlan 632
 switchport mode access
           switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet8/0/27
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet8/0/28
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet8/0/29
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet8/0/30
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet8/0/31
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet8/0/32
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet8/0/33
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet8/0/34
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet8/0/35
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet8/0/36
 switchport access vlan 632
           switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet8/0/37
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet8/0/38
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet8/0/39
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet8/0/40
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet8/0/41
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet8/0/42
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet8/0/43
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet8/0/44
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet8/0/45
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet8/0/46
           switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet8/0/47
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface GigabitEthernet8/0/48
 description #UPS
 switchport access vlan 332
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
!
interface Vlan1
 no ip address
 no ip route-cache
 shutdown
!
interface Vlan332
 description clinical-525hosp-m
 ip address 172.20.64.14 255.255.255.0
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
snmp-server group CliNOCGrv3RO v3 priv read CliNOCViewRO access 70
snmp-server group CliNOCGrv3RO v3 auth context vlan- match prefix 
snmp-server group CliNOCGrv3RW v3 priv write CliNOCViewRW access 71
snmp-server view VoicePhones internet included
snmp-server view CliNOCViewRO internet included
snmp-server view CliNOCViewRW internet included
snmp-server location Bldg. 525 Room 4659-new
snmp-server contact BC-509403 Y-334728
snmp-server context vlan-1
snmp-server context vlan-123
snmp-server context vlan-124
snmp-server context vlan-125
snmp-server context vlan-126
snmp-server context vlan-127
snmp-server context vlan-128
snmp-server context vlan-129
snmp-server context vlan-130
snmp-server context vlan-131
snmp-server context vlan-132
snmp-server context vlan-270
snmp-server context vlan-332
snmp-server context vlan-337
snmp-server context vlan-338
snmp-server context vlan-341
snmp-server context vlan-345
snmp-server context vlan-396
snmp-server context vlan-418
snmp-server context vlan-540
snmp-server context vlan-551
snmp-server context vlan-575
snmp-server context vlan-600
snmp-server context vlan-607
snmp-server context vlan-610
snmp-server context vlan-620
snmp-server context vlan-629
snmp-server context vlan-630
snmp-server context vlan-631
snmp-server context vlan-632
snmp-server context vlan-633
          snmp-server context vlan-634
snmp-server context vlan-635
snmp-server context vlan-636
snmp-server context vlan-637
snmp-server context vlan-638
snmp-server context vlan-640
snmp-server context vlan-680
snmp-server context vlan-732
snmp-server context vlan-770
snmp-server context vlan-771
snmp-server context vlan-772
snmp-server context vlan-773
snmp-server context vlan-850
snmp-server context vlan-921
snmp-server context vlan-942
snmp-server context vlan-983
snmp-server context vlan-984
snmp-server context vlan-986
snmp-server context vlan-987
snmp-server context vlan-988
snmp-server context vlan-989
snmp-server context vlan-990
snmp-server context vlan-1037
snmp-server context vlan-1041
snmp-server context vlan-1060
snmp-server context vlan-1075
snmp-server context vlan-1076
snmp-server context vlan-1112
snmp-server context vlan-1209
snmp-server context vlan-1600
snmp-server context vlan-1605
snmp-server context vlan-1616
snmp-server context vlan-1621
snmp-server context vlan-1672
snmp-server context vlan-1700
snmp-server context vlan-1800
snmp-server context vlan-1900
snmp-server context vlan-3000
snmp ifmib ifindex persist
tacacs server TAC-EBC
 address ipv4 172.31.17.180
 key 7 032D1F0E2F4B246E6E0B0044
tacacs server TAC-SECONDARY
 address ipv4 10.64.32.5
 key 7 07266549674D1C273710124D
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
dx2-525hosp-4659-new

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
 password 7 053E120E294E0F5A4D
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
Gi1/0/1                      connected    607        a-half   a-10 10/100/1000BaseTX
Gi1/0/2                      connected    607        a-half   a-10 10/100/1000BaseTX
Gi1/0/3                      notconnect   632          auto   auto 10/100/1000BaseTX
Gi1/0/4                      notconnect   632          auto   auto 10/100/1000BaseTX
Gi1/0/5                      notconnect   632          auto   auto 10/100/1000BaseTX
Gi1/0/6                      notconnect   632          auto   auto 10/100/1000BaseTX
Gi1/0/7                      notconnect   632          auto   auto 10/100/1000BaseTX
Gi1/0/8                      connected    771        a-full a-1000 10/100/1000BaseTX
Gi1/0/9                      notconnect   632          auto   auto 10/100/1000BaseTX
Gi1/0/10  #swisstube         connected    732        a-full  a-100 10/100/1000BaseTX
Gi1/0/11                     connected    270        a-full  a-100 10/100/1000BaseTX
Gi1/0/12                     connected    270        a-full  a-100 10/100/1000BaseTX
Gi1/0/13  #Omnicell          notconnect   600          auto   auto 10/100/1000BaseTX
Gi1/0/14  #New OR HVAC RITM0 connected    341        a-full  a-100 10/100/1000BaseTX
Gi1/0/15  #Omnicell          connected    600        a-full     10 10/100/1000BaseTX
Gi1/0/16  #Omnicell          connected    600        a-full a-1000 10/100/1000BaseTX
Gi1/0/17                     connected    341        a-full  a-100 10/100/1000BaseTX
Gi1/0/18  #BMDI 100/full     connected    418          full    100 10/100/1000BaseTX
Gi1/0/19  #RTLS              notconnect   1112         auto   auto 10/100/1000BaseTX
Gi1/0/20  #RTLS              connected    1112       a-full  a-100 10/100/1000BaseTX
Gi1/0/21                     notconnect   1041         auto   auto 10/100/1000BaseTX
Gi1/0/22                     connected    1041       a-full  a-100 10/100/1000BaseTX
Gi1/0/23  Wireless AP        notconnect   1037         auto   auto 10/100/1000BaseTX
Gi1/0/24  Wireless AP        connected    1037       a-full a-1000 10/100/1000BaseTX
Gi1/0/25                     connected    396        a-full  a-100 10/100/1000BaseTX
Gi1/0/26                     connected    396        a-full a-1000 10/100/1000BaseTX
Gi1/0/27                     connected    396        a-full a-1000 10/100/1000BaseTX
Gi1/0/28                     connected    396        a-full a-1000 10/100/1000BaseTX
Gi1/0/29                     connected    396        a-full a-1000 10/100/1000BaseTX
Gi1/0/30                     connected    396        a-full a-1000 10/100/1000BaseTX
Gi1/0/31                     connected    396        a-full a-1000 10/100/1000BaseTX
Gi1/0/32                     connected    396        a-full  a-100 10/100/1000BaseTX
Gi1/0/33                     connected    396        a-full  a-100 10/100/1000BaseTX
Gi1/0/34                     connected    396        a-full  a-100 10/100/1000BaseTX
Gi1/0/35                     connected    396        a-full  a-100 10/100/1000BaseTX
Gi1/0/36                     connected    396        a-full a-1000 10/100/1000BaseTX
Gi1/0/37  NetBeez            connected    1037       a-full  a-100 10/100/1000BaseTX
Gi1/0/38  #AP                notconnect   1037         auto   auto 10/100/1000BaseTX
Gi1/0/39  #AP                connected    1037       a-full a-1000 10/100/1000BaseTX
Gi1/0/40  #AP                connected    1037       a-full a-1000 10/100/1000BaseTX
Gi1/0/41  #AP                connected    1037       a-full a-1000 10/100/1000BaseTX
Gi1/0/42  #AP                connected    1037       a-full a-1000 10/100/1000BaseTX
Gi1/0/43  #AP                connected    1037       a-full a-1000 10/100/1000BaseTX
Gi1/0/44  #AP                connected    1037       a-full a-1000 10/100/1000BaseTX
Gi1/0/45  #AP                connected    1037       a-full a-1000 10/100/1000BaseTX
Gi1/0/46  #AP                connected    1037       a-full a-1000 10/100/1000BaseTX
Gi1/0/47  #Emergency Radio ( connected    1900       a-full a-1000 10/100/1000BaseTX
Gi1/0/48  #AP                connected    1037       a-full a-1000 10/100/1000BaseTX
Te4/0/1   key:sx1-525hosp-15 connected    trunk        full    10G SFP-10GBase-SR
Te4/0/2   key:sx1-525hosp-b2 connected    trunk        full    10G SFP-10GBase-SR
Te4/0/3   key:sx1-525hosp-42 connected    trunk        full    10G SFP-10GBase-SR
Te4/0/4   key:sx1-525hosp-30 connected    trunk        full    10G SFP-10GBase-SR
Te4/0/5   key:sx1-525hosp-18 connected    trunk        full    10G SFP-10GBase-SR
Te4/0/6   key:sx2-525hosp-37 connected    trunk        full    10G SFP-10GBase-SR
Te4/0/7   key:sx1-525hosp-37 connected    trunk        full    10G SFP-10GBase-SR
Te4/0/8   key:sx1-525hosp-33 connected    trunk        full    10G SFP-10GBase-SR
Te4/0/9   key:sx2-525hosp-a3 connected    trunk        full    10G SFP-10GBase-SR
          
Port      Name               Status       Vlan       Duplex  Speed Type 
Te4/0/10  key:sx1-525hosp-43 connected    trunk        full    10G SFP-10GBase-SR
Te4/0/11  key:sx1-525hosp-14 connected    trunk        full    10G SFP-10GBase-SR
Te4/0/12                     notconnect   1            full    10G SFP-10GBase-SR
Te4/0/13  key:sx1-525hosp-51 connected    trunk        full    10G SFP-10GBase-SR
Te4/0/14  key:sx1-525hosp-61 connected    trunk        full    10G SFP-10GBase-SR
Te4/0/15  key:sx1-525hosp-a3 connected    trunk        full    10G SFP-10GBase-SR
Te4/0/16  key:sx1-525hosp-24 connected    trunk        full    10G SFP-10GBase-SR
Te4/0/17  key:sx1-525hosp-27 connected    trunk        full    10G SFP-10GBase-SR
Te4/0/18  key:sx2-525hosp-43 connected    trunk        full    10G SFP-10GBase-SR
Te4/0/19  #key:sx1-525hosp-4 connected    trunk        full    10G SFP-10GBase-SR
Te4/0/20  key:sx1-525hosp-26 connected    trunk        full    10G SFP-10GBase-LR
Te4/0/21                     notconnect   1            auto  a-10G 
Te4/0/22  key:sx1-525hosp-14 connected    trunk        full    10G SFP-10GBase-SR
Te4/0/23  key:sx1-525hosp-22 connected    trunk        full   1000 1000BaseSX SFP
Te4/0/24  key:sx1-525hosp-a6 connected    trunk        full   1000 1000BaseSX SFP
Te5/0/1   key:r1-clinical:e2 connected    trunk        full    10G SFP-10GBase-SR
Te5/0/2   key:r2-clinical:e2 connected    trunk        full    10G SFP-10GBase-LR
Te5/0/3   t5/0/3:sx1-525-inf connected    trunk        full    10G SFP-10GBase-LR
Te5/0/4   t5/0/4:sx2-525infi connected    trunk        full    10G SFP-10GBase-LR
Te5/0/5   t5/0/5:sx1-525-140 connected    trunk        full    10G SFP-10GBase-LR
Te5/0/6   t5/0/6:sx1-525-140 connected    trunk        full    10G SFP-10GBase-LR
Te5/0/7                      notconnect   1            auto  a-10G 
Te5/0/8   #temp uplink to ol notconnect   1            auto  a-10G 
Fo5/0/9                      inactive     1            auto   auto 
Fo5/0/10                     inactive     1            auto   auto 
Gi7/0/1                      connected    129        a-full a-1000 10/100/1000BaseTX
Gi7/0/2                      connected    129        a-full a-1000 10/100/1000BaseTX
Gi7/0/3                      connected    632        a-full  a-100 10/100/1000BaseTX
Gi7/0/4                      connected    129        a-full a-1000 10/100/1000BaseTX
Gi7/0/5                      connected    632        a-full a-1000 10/100/1000BaseTX
Gi7/0/6                      connected    632        a-full a-1000 10/100/1000BaseTX
Gi7/0/7                      notconnect   632          auto   auto 10/100/1000BaseTX
Gi7/0/8                      connected    129        a-full a-1000 10/100/1000BaseTX
Gi7/0/9                      notconnect   632          auto   auto 10/100/1000BaseTX
Gi7/0/10                     connected    632        a-full  a-100 10/100/1000BaseTX
Gi7/0/11                     connected    129        a-full a-1000 10/100/1000BaseTX
Gi7/0/12                     notconnect   632          auto   auto 10/100/1000BaseTX
Gi7/0/13                     connected    632        a-full a-1000 10/100/1000BaseTX
Gi7/0/14                     connected    632        a-full  a-100 10/100/1000BaseTX
Gi7/0/15                     notconnect   632          auto   auto 10/100/1000BaseTX
Gi7/0/16                     connected    632        a-full a-1000 10/100/1000BaseTX
Gi7/0/17                     connected    632        a-full a-1000 10/100/1000BaseTX
Gi7/0/18                     connected    632        a-full a-1000 10/100/1000BaseTX
Gi7/0/19                     connected    129        a-full a-1000 10/100/1000BaseTX
Gi7/0/20                     connected    129        a-full a-1000 10/100/1000BaseTX
Gi7/0/21                     connected    632        a-full a-1000 10/100/1000BaseTX
Gi7/0/22                     connected    632        a-full a-1000 10/100/1000BaseTX
Gi7/0/23                     connected    632        a-full  a-100 10/100/1000BaseTX
Gi7/0/24                     connected    123        a-full a-1000 10/100/1000BaseTX
Gi7/0/25                     connected    632        a-full a-1000 10/100/1000BaseTX
Gi7/0/26                     connected    129        a-full a-1000 10/100/1000BaseTX
Gi7/0/27                     connected    129        a-full a-1000 10/100/1000BaseTX
Gi7/0/28                     connected    632        a-full a-1000 10/100/1000BaseTX
Gi7/0/29                     connected    632        a-full a-1000 10/100/1000BaseTX
Gi7/0/30                     connected    129        a-full a-1000 10/100/1000BaseTX
Gi7/0/31                     notconnect   396          auto   auto 10/100/1000BaseTX
Gi7/0/32                     connected    632        a-full  a-100 10/100/1000BaseTX
Gi7/0/33  Paging             connected    1060       a-full  a-100 10/100/1000BaseTX
Gi7/0/34                     notconnect   632          auto   auto 10/100/1000BaseTX
          
Port      Name               Status       Vlan       Duplex  Speed Type 
Gi7/0/35                     notconnect   632          auto   auto 10/100/1000BaseTX
Gi7/0/36                     notconnect   632          auto   auto 10/100/1000BaseTX
Gi7/0/37                     connected    632        a-full a-1000 10/100/1000BaseTX
Gi7/0/38                     connected    129        a-full a-1000 10/100/1000BaseTX
Gi7/0/39                     connected    129        a-full a-1000 10/100/1000BaseTX
Gi7/0/40                     connected    129        a-full a-1000 10/100/1000BaseTX
Gi7/0/41                     connected    129        a-full a-1000 10/100/1000BaseTX
Gi7/0/42                     connected    632        a-full a-1000 10/100/1000BaseTX
Gi7/0/43                     connected    632        a-full a-1000 10/100/1000BaseTX
Gi7/0/44                     connected    129        a-full a-1000 10/100/1000BaseTX
Gi7/0/45                     connected    129        a-full a-1000 10/100/1000BaseTX
Gi7/0/46                     connected    129        a-full a-1000 10/100/1000BaseTX
Gi7/0/47                     connected    129        a-full a-1000 10/100/1000BaseTX
Gi7/0/48                     connected    129        a-full a-1000 10/100/1000BaseTX
Gi8/0/1                      connected    632        a-full a-1000 10/100/1000BaseTX
Gi8/0/2                      connected    129        a-full a-1000 10/100/1000BaseTX
Gi8/0/3                      connected    632        a-full a-1000 10/100/1000BaseTX
Gi8/0/4                      connected    632        a-full a-1000 10/100/1000BaseTX
Gi8/0/5                      connected    129        a-full a-1000 10/100/1000BaseTX
Gi8/0/6                      notconnect   632          auto   auto 10/100/1000BaseTX
Gi8/0/7                      connected    129        a-full a-1000 10/100/1000BaseTX
Gi8/0/8                      connected    129        a-full  a-100 10/100/1000BaseTX
Gi8/0/9                      connected    129        a-full a-1000 10/100/1000BaseTX
Gi8/0/10                     connected    129        a-full a-1000 10/100/1000BaseTX
Gi8/0/11                     connected    129        a-full a-1000 10/100/1000BaseTX
Gi8/0/12                     connected    129        a-full a-1000 10/100/1000BaseTX
Gi8/0/13                     connected    129        a-full a-1000 10/100/1000BaseTX
Gi8/0/14                     notconnect   632          auto   auto 10/100/1000BaseTX
Gi8/0/15                     connected    129        a-full a-1000 10/100/1000BaseTX
Gi8/0/16                     connected    632        a-full  a-100 10/100/1000BaseTX
Gi8/0/17                     notconnect   632          auto   auto 10/100/1000BaseTX
Gi8/0/18                     connected    129        a-full a-1000 10/100/1000BaseTX
Gi8/0/19                     connected    632        a-full a-1000 10/100/1000BaseTX
Gi8/0/20                     connected    129        a-full a-1000 10/100/1000BaseTX
Gi8/0/21                     connected    129        a-full a-1000 10/100/1000BaseTX
Gi8/0/22                     connected    129        a-full a-1000 10/100/1000BaseTX
Gi8/0/23                     connected    632        a-full a-1000 10/100/1000BaseTX
Gi8/0/24                     connected    632        a-full a-1000 10/100/1000BaseTX
Gi8/0/25                     connected    129        a-full a-1000 10/100/1000BaseTX
Gi8/0/26                     connected    632        a-full a-1000 10/100/1000BaseTX
Gi8/0/27                     connected    129        a-full a-1000 10/100/1000BaseTX
Gi8/0/28                     connected    632        a-full a-1000 10/100/1000BaseTX
Gi8/0/29                     notconnect   632          auto   auto 10/100/1000BaseTX
Gi8/0/30                     connected    129        a-full a-1000 10/100/1000BaseTX
Gi8/0/31                     connected    632        a-full a-1000 10/100/1000BaseTX
Gi8/0/32                     connected    632        a-full a-1000 10/100/1000BaseTX
Gi8/0/33                     connected    632        a-full a-1000 10/100/1000BaseTX
Gi8/0/34                     connected    632        a-full a-1000 10/100/1000BaseTX
Gi8/0/35                     connected    632        a-full a-1000 10/100/1000BaseTX
Gi8/0/36                     connected    632        a-full a-1000 10/100/1000BaseTX
Gi8/0/37                     notconnect   632          auto   auto 10/100/1000BaseTX
Gi8/0/38                     connected    632        a-full  a-100 10/100/1000BaseTX
Gi8/0/39                     notconnect   632          auto   auto 10/100/1000BaseTX
Gi8/0/40                     notconnect   632          auto   auto 10/100/1000BaseTX
Gi8/0/41                     notconnect   632          auto   auto 10/100/1000BaseTX
Gi8/0/42                     notconnect   632          auto   auto 10/100/1000BaseTX
Gi8/0/43                     notconnect   632          auto   auto 10/100/1000BaseTX
Gi8/0/44                     notconnect   632          auto   auto 10/100/1000BaseTX
Gi8/0/45                     connected    129        a-full a-1000 10/100/1000BaseTX
          
Port      Name               Status       Vlan       Duplex  Speed Type 
Gi8/0/46                     connected    632        a-full  a-100 10/100/1000BaseTX
Gi8/0/47                     notconnect   632          auto   auto 10/100/1000BaseTX
Gi8/0/48  #UPS               connected    332        a-full  a-100 10/100/1000BaseTX
Po30      key:Uplink to dist connected    trunk      a-full  a-10G """,
 'show run | section interface':"""match interface input
 collect interface output
interface Port-channel30
 description key:Uplink to dist nodes
 switchport mode trunk
 ip dhcp snooping trust
interface GigabitEthernet0/0
 vrf forwarding Mgmt-vrf
 no ip address
 no ip route-cache
 shutdown
 negotiation auto
interface GigabitEthernet1/0/1
 switchport access vlan 607
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet1/0/2
 switchport access vlan 607
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet1/0/3
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet1/0/4
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet1/0/5
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet1/0/6
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet1/0/7
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet1/0/8
 switchport access vlan 771
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet1/0/9
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet1/0/10
 description #swisstube
           switchport access vlan 732
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/11
 switchport access vlan 270
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet1/0/12
 switchport access vlan 270
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet1/0/13
 description #Omnicell
 switchport access vlan 600
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/14
 description #New OR HVAC RITM0300645
 switchport access vlan 341
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/15
 description #Omnicell
 switchport access vlan 600
 switchport mode access
 speed 10
 spanning-tree portfast
interface GigabitEthernet1/0/16
 description #Omnicell
 switchport access vlan 600
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/17
 switchport access vlan 341
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet1/0/18
 description #BMDI 100/full
 switchport access vlan 418
 speed 100
 duplex full
 spanning-tree portfast
interface GigabitEthernet1/0/19
 description #RTLS
 switchport access vlan 1112
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet1/0/20
 description #RTLS
 switchport access vlan 1112
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet1/0/21
 switchport access vlan 1041
           switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet1/0/22
 switchport access vlan 1041
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet1/0/23
 description Wireless AP
 switchport access vlan 1037
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/24
 description Wireless AP
 switchport access vlan 1037
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/25
 switchport access vlan 396
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet1/0/26
 switchport access vlan 396
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet1/0/27
 switchport access vlan 396
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet1/0/28
 switchport access vlan 396
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet1/0/29
 switchport access vlan 396
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet1/0/30
 switchport access vlan 396
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet1/0/31
 switchport access vlan 396
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet1/0/32
 switchport access vlan 396
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet1/0/33
           switchport access vlan 396
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet1/0/34
 switchport access vlan 396
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet1/0/35
 switchport access vlan 396
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet1/0/36
 switchport access vlan 396
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet1/0/37
 description NetBeez
 switchport access vlan 1037
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet1/0/38
 description #AP
 switchport access vlan 1037
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet1/0/39
 description #AP
 switchport access vlan 1037
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet1/0/40
 description #AP
 switchport access vlan 1037
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet1/0/41
 description #AP
 switchport access vlan 1037
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet1/0/42
 description #AP
 switchport access vlan 1037
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet1/0/43
 description #AP
 switchport access vlan 1037
 switchport mode access
           switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet1/0/44
 description #AP
 switchport access vlan 1037
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet1/0/45
 description #AP
 switchport access vlan 1037
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet1/0/46
 description #AP
 switchport access vlan 1037
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet1/0/47
 description #Emergency Radio (on roof)
 switchport access vlan 1900
 switchport mode access
 power inline never
interface GigabitEthernet1/0/48
 description #AP
 switchport access vlan 1037
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface TenGigabitEthernet4/0/1
 description key:sx1-525hosp-1511:ten5/1
 switchport mode trunk
 switchport priority extend trust
 storm-control broadcast level 2.00
 storm-control action shutdown
 storm-control action trap
interface TenGigabitEthernet4/0/2
 description key:sx1-525hosp-b244:ten5/2
 switchport mode trunk
 switchport priority extend trust
 storm-control broadcast level 2.00
 storm-control action shutdown
 storm-control action trap
interface TenGigabitEthernet4/0/3
 description key:sx1-525hosp-4270:ten1/1
 switchport mode trunk
 switchport priority extend trust
 storm-control broadcast level 2.00
 storm-control action shutdown
 storm-control action trap
interface TenGigabitEthernet4/0/4
 description key:sx1-525hosp-3043:ten1/2
 switchport mode trunk
 switchport priority extend trust
 storm-control broadcast level 2.00
 storm-control action shutdown
 storm-control action trap
          interface TenGigabitEthernet4/0/5
 description key:sx1-525hosp-1873:ten1/2
 switchport mode trunk
 switchport priority extend trust
 storm-control broadcast level 2.00
 storm-control action shutdown
 storm-control action trap
interface TenGigabitEthernet4/0/6
 description key:sx2-525hosp-3745:ten5/1
 switchport mode trunk
 switchport priority extend trust
 storm-control broadcast level 2.00
 storm-control action shutdown
 storm-control action trap
interface TenGigabitEthernet4/0/7
 description key:sx1-525hosp-3745:ten5/1
 switchport mode trunk
 switchport priority extend trust
 storm-control broadcast level 2.00
 storm-control action shutdown
 storm-control action trap
interface TenGigabitEthernet4/0/8
 description key:sx1-525hosp-3306:ten5/1
 switchport mode trunk
 switchport priority extend trust
 storm-control broadcast level 2.00
 storm-control action shutdown
 storm-control action trap
interface TenGigabitEthernet4/0/9
 description key:sx2-525hosp-a371:t1/1/2
 switchport mode trunk
 switchport priority extend trust
 storm-control broadcast level 2.00
 storm-control action shutdown
 storm-control action trap
interface TenGigabitEthernet4/0/10
 description key:sx1-525hosp-4317:ten5/2
 switchport trunk allowed vlan 129,270,332,341,345,357,380,396,540,607,610,632
 switchport trunk allowed vlan add 681,732,770,921,988,1037,1075,1076
 switchport mode trunk
 switchport priority extend trust
 storm-control broadcast level 2.00
 storm-control action shutdown
 storm-control action trap
interface TenGigabitEthernet4/0/11
 description key:sx1-525hosp-1443:ten1/2
 switchport trunk allowed vlan 125,332,341,396,540,607,636,681,732,984,1037
 switchport trunk allowed vlan add 1075,1076,1209,1605
 switchport mode trunk
 switchport priority extend trust
 storm-control broadcast level 2.00
 storm-control action shutdown
 storm-control action trap
interface TenGigabitEthernet4/0/12
interface TenGigabitEthernet4/0/13
 description key:sx1-525hosp-5105:ten5/2
 switchport mode trunk
 switchport priority extend trust
 storm-control broadcast level 2.00
           storm-control action shutdown
 storm-control action trap
interface TenGigabitEthernet4/0/14
 description key:sx1-525hosp-6103:ten5/2
 switchport mode trunk
 switchport priority extend trust
 storm-control broadcast level 2.00
 storm-control action shutdown
 storm-control action trap
interface TenGigabitEthernet4/0/15
 description key:sx1-525hosp-a371:ten5/2
 switchport trunk allowed vlan 124,270,332,338,341,396,551,637,732,773,983,1037
 switchport trunk allowed vlan add 1060,1600,1605,1621
 switchport mode trunk
 switchport priority extend trust
 storm-control broadcast level 2.00
 storm-control action shutdown
 storm-control action trap
interface TenGigabitEthernet4/0/16
 description key:sx1-525hosp-2411:ten5/1
 switchport mode trunk
 switchport priority extend trust
 storm-control broadcast level 2.00
 storm-control action shutdown
 storm-control action trap
interface TenGigabitEthernet4/0/17
 description key:sx1-525hosp-2741:ten5/2
 switchport mode trunk
 switchport priority extend trust
 storm-control broadcast level 2.00
 storm-control action shutdown
 storm-control action trap
interface TenGigabitEthernet4/0/18
 description key:sx2-525hosp-4317:te1/1/2
 switchport trunk allowed vlan 129,270,332,341,345,357,380,396,540,551,607,610
 switchport trunk allowed vlan add 632,681,732,770,921,988,1037,1075,1076,1112
 switchport mode trunk
 storm-control broadcast level 2.00
 storm-control action shutdown
 storm-control action trap
interface TenGigabitEthernet4/0/19
 description #key:sx1-525hosp-4625:e5/2
 switchport mode trunk
 switchport priority extend trust
 storm-control broadcast level 2.00
 storm-control action shutdown
 storm-control action trap
interface TenGigabitEthernet4/0/20
 description key:sx1-525hosp-2673:t1/1/3
 switchport trunk allowed vlan 128,332,341,396,600,607,633,655,770,772,987,1037
 switchport mode trunk
 load-interval 30
 storm-control broadcast level 2.00
 storm-control action shutdown
 storm-control action trap
interface TenGigabitEthernet4/0/21
 storm-control broadcast level 2.00
 storm-control action shutdown
 storm-control action trap
          interface TenGigabitEthernet4/0/22
 description key:sx1-525hosp-1437b:t5/1
 switchport mode trunk
 switchport priority extend trust
 storm-control broadcast level 2.00
 storm-control action shutdown
 storm-control action trap
interface TenGigabitEthernet4/0/23
 description key:sx1-525hosp-2255:g2/1/1
 switchport trunk allowed vlan 124,127,270,332,338,341,396,551,600,607,634,637
 switchport trunk allowed vlan add 732,986,1037,1075,1076,1112,1605,1621
 switchport mode trunk
 switchport priority extend trust
 storm-control broadcast level 2.00
 storm-control action shutdown
 storm-control action trap
interface TenGigabitEthernet4/0/24
 description key:sx1-525hosp-a673:g1/0/49
 switchport trunk allowed vlan 124,270,332,341,396,551,607,629,637,732,942,983
 switchport trunk allowed vlan add 1037,1075,1076,1112,1209,1605,1672
 switchport mode trunk
 switchport priority extend trust
 storm-control broadcast level 2.00
 storm-control action shutdown
 storm-control action trap
interface TenGigabitEthernet5/0/1
 description key:r1-clinical:e2/10
 switchport mode trunk
 channel-group 30 mode active
 ip dhcp snooping trust
interface TenGigabitEthernet5/0/2
 description key:r2-clinical:e2/10
 switchport mode trunk
 channel-group 30 mode active
 ip dhcp snooping trust
interface TenGigabitEthernet5/0/3
 description t5/0/3:sx1-525-infill:t5/0/2
 switchport mode trunk
interface TenGigabitEthernet5/0/4
 description t5/0/4:sx2-525infill:t1/0/2
 switchport mode trunk
interface TenGigabitEthernet5/0/5
 description t5/0/5:sx1-525-1408:t1/1/2
 switchport mode trunk
interface TenGigabitEthernet5/0/6
 description t5/0/6:sx1-525-1408:t5/0/2
 switchport mode trunk
interface TenGigabitEthernet5/0/7
 switchport mode trunk
interface TenGigabitEthernet5/0/8
 description #temp uplink to old switch
 switchport mode trunk
 ip dhcp snooping trust
interface FortyGigabitEthernet5/0/9
interface FortyGigabitEthernet5/0/10
interface GigabitEthernet7/0/1
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
           spanning-tree portfast
interface GigabitEthernet7/0/2
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet7/0/3
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet7/0/4
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet7/0/5
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet7/0/6
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet7/0/7
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet7/0/8
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet7/0/9
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet7/0/10
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet7/0/11
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet7/0/12
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet7/0/13
 switchport access vlan 632
 switchport mode access
           switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet7/0/14
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet7/0/15
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet7/0/16
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet7/0/17
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet7/0/18
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet7/0/19
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet7/0/20
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet7/0/21
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet7/0/22
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet7/0/23
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet7/0/24
 switchport access vlan 123
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet7/0/25
 switchport access vlan 632
           switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet7/0/26
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet7/0/27
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet7/0/28
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet7/0/29
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet7/0/30
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet7/0/31
 switchport access vlan 396
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet7/0/32
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet7/0/33
 description Paging
 switchport access vlan 1060
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet7/0/34
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet7/0/35
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet7/0/36
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet7/0/37
           switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet7/0/38
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet7/0/39
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet7/0/40
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet7/0/41
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet7/0/42
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet7/0/43
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet7/0/44
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet7/0/45
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet7/0/46
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet7/0/47
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet7/0/48
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
          interface GigabitEthernet8/0/1
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet8/0/2
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet8/0/3
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet8/0/4
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet8/0/5
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet8/0/6
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet8/0/7
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet8/0/8
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet8/0/9
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet8/0/10
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet8/0/11
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet8/0/12
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
           spanning-tree portfast
interface GigabitEthernet8/0/13
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet8/0/14
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet8/0/15
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet8/0/16
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet8/0/17
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet8/0/18
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet8/0/19
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet8/0/20
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet8/0/21
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet8/0/22
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet8/0/23
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet8/0/24
 switchport access vlan 632
 switchport mode access
           switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet8/0/25
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet8/0/26
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet8/0/27
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet8/0/28
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet8/0/29
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet8/0/30
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet8/0/31
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet8/0/32
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet8/0/33
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet8/0/34
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet8/0/35
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet8/0/36
 switchport access vlan 632
           switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet8/0/37
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet8/0/38
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet8/0/39
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet8/0/40
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet8/0/41
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet8/0/42
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet8/0/43
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet8/0/44
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet8/0/45
 switchport access vlan 129
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet8/0/46
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet8/0/47
 switchport access vlan 632
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface GigabitEthernet8/0/48
           description #UPS
 switchport access vlan 332
 switchport mode access
 switchport voice vlan 988
 spanning-tree portfast
interface Vlan1
 no ip address
 no ip route-cache
 shutdown
interface Vlan332
 description clinical-525hosp-m
 ip address 172.20.64.14 255.255.255.0
 no ip route-cache
logging source-interface Vlan332""",
 'show run | in interface':"""match interface input
 collect interface output
interface Port-channel30
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
interface TenGigabitEthernet4/0/1
interface TenGigabitEthernet4/0/2
interface TenGigabitEthernet4/0/3
interface TenGigabitEthernet4/0/4
interface TenGigabitEthernet4/0/5
interface TenGigabitEthernet4/0/6
interface TenGigabitEthernet4/0/7
          interface TenGigabitEthernet4/0/8
interface TenGigabitEthernet4/0/9
interface TenGigabitEthernet4/0/10
interface TenGigabitEthernet4/0/11
interface TenGigabitEthernet4/0/12
interface TenGigabitEthernet4/0/13
interface TenGigabitEthernet4/0/14
interface TenGigabitEthernet4/0/15
interface TenGigabitEthernet4/0/16
interface TenGigabitEthernet4/0/17
interface TenGigabitEthernet4/0/18
interface TenGigabitEthernet4/0/19
interface TenGigabitEthernet4/0/20
interface TenGigabitEthernet4/0/21
interface TenGigabitEthernet4/0/22
interface TenGigabitEthernet4/0/23
interface TenGigabitEthernet4/0/24
interface TenGigabitEthernet5/0/1
interface TenGigabitEthernet5/0/2
interface TenGigabitEthernet5/0/3
interface TenGigabitEthernet5/0/4
interface TenGigabitEthernet5/0/5
interface TenGigabitEthernet5/0/6
interface TenGigabitEthernet5/0/7
interface TenGigabitEthernet5/0/8
interface FortyGigabitEthernet5/0/9
interface FortyGigabitEthernet5/0/10
interface GigabitEthernet7/0/1
interface GigabitEthernet7/0/2
interface GigabitEthernet7/0/3
interface GigabitEthernet7/0/4
interface GigabitEthernet7/0/5
interface GigabitEthernet7/0/6
interface GigabitEthernet7/0/7
interface GigabitEthernet7/0/8
interface GigabitEthernet7/0/9
interface GigabitEthernet7/0/10
interface GigabitEthernet7/0/11
interface GigabitEthernet7/0/12
interface GigabitEthernet7/0/13
interface GigabitEthernet7/0/14
interface GigabitEthernet7/0/15
interface GigabitEthernet7/0/16
interface GigabitEthernet7/0/17
interface GigabitEthernet7/0/18
interface GigabitEthernet7/0/19
interface GigabitEthernet7/0/20
interface GigabitEthernet7/0/21
interface GigabitEthernet7/0/22
interface GigabitEthernet7/0/23
interface GigabitEthernet7/0/24
interface GigabitEthernet7/0/25
interface GigabitEthernet7/0/26
interface GigabitEthernet7/0/27
interface GigabitEthernet7/0/28
interface GigabitEthernet7/0/29
interface GigabitEthernet7/0/30
interface GigabitEthernet7/0/31
interface GigabitEthernet7/0/32
          interface GigabitEthernet7/0/33
interface GigabitEthernet7/0/34
interface GigabitEthernet7/0/35
interface GigabitEthernet7/0/36
interface GigabitEthernet7/0/37
interface GigabitEthernet7/0/38
interface GigabitEthernet7/0/39
interface GigabitEthernet7/0/40
interface GigabitEthernet7/0/41
interface GigabitEthernet7/0/42
interface GigabitEthernet7/0/43
interface GigabitEthernet7/0/44
interface GigabitEthernet7/0/45
interface GigabitEthernet7/0/46
interface GigabitEthernet7/0/47
interface GigabitEthernet7/0/48
interface GigabitEthernet8/0/1
interface GigabitEthernet8/0/2
interface GigabitEthernet8/0/3
interface GigabitEthernet8/0/4
interface GigabitEthernet8/0/5
interface GigabitEthernet8/0/6
interface GigabitEthernet8/0/7
interface GigabitEthernet8/0/8
interface GigabitEthernet8/0/9
interface GigabitEthernet8/0/10
interface GigabitEthernet8/0/11
interface GigabitEthernet8/0/12
interface GigabitEthernet8/0/13
interface GigabitEthernet8/0/14
interface GigabitEthernet8/0/15
interface GigabitEthernet8/0/16
interface GigabitEthernet8/0/17
interface GigabitEthernet8/0/18
interface GigabitEthernet8/0/19
interface GigabitEthernet8/0/20
interface GigabitEthernet8/0/21
interface GigabitEthernet8/0/22
interface GigabitEthernet8/0/23
interface GigabitEthernet8/0/24
interface GigabitEthernet8/0/25
interface GigabitEthernet8/0/26
interface GigabitEthernet8/0/27
interface GigabitEthernet8/0/28
interface GigabitEthernet8/0/29
interface GigabitEthernet8/0/30
interface GigabitEthernet8/0/31
interface GigabitEthernet8/0/32
interface GigabitEthernet8/0/33
interface GigabitEthernet8/0/34
interface GigabitEthernet8/0/35
interface GigabitEthernet8/0/36
interface GigabitEthernet8/0/37
interface GigabitEthernet8/0/38
interface GigabitEthernet8/0/39
interface GigabitEthernet8/0/40
interface GigabitEthernet8/0/41
interface GigabitEthernet8/0/42
interface GigabitEthernet8/0/43
          interface GigabitEthernet8/0/44
interface GigabitEthernet8/0/45
interface GigabitEthernet8/0/46
interface GigabitEthernet8/0/47
interface GigabitEthernet8/0/48
interface Vlan1
interface Vlan332
logging source-interface Vlan332""",
 'show interface link':"""^
% Invalid input detected at '^' marker.
""",
 'show interface':"""Vlan1 is administratively down, line protocol is down 
  Hardware is Ethernet SVI, address is a093.51d2.5c43 (bia a093.51d2.5c43)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 21w4d, output never, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     676841 packets input, 77947392 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Vlan332 is up, line protocol is up 
  Hardware is Ethernet SVI, address is a093.51d2.5c45 (bia a093.51d2.5c45)
  Description: clinical-525hosp-m
  Internet address is 172.20.64.14/24
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 00:06:32, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 2000 bits/sec, 2 packets/sec
  5 minute output rate 3000 bits/sec, 2 packets/sec
     74957066 packets input, 12354411635 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     34765763 packets output, 9997017803 bytes, 0 underruns
     0 output errors, 0 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet0/0 is administratively down, line protocol is down 
  Hardware is RP management port, address is a093.51d2.5c4e (bia a093.51d2.5c4e)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto Duplex, Auto Speed, link type is auto, media type is RJ45
  output flow-control is unsupported, input flow-control is unsupported
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 13w2d
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
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/1 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c772.2940 (bia bc26.c772.2940)
  MTU 1500 bytes, BW 10000 Kbit/sec, DLY 1000 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Half-duplex, 10Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:19, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 3000 bits/sec, 3 packets/sec
     3087881 packets input, 400056409 bytes, 0 no buffer
     Received 663 broadcasts (0 multicasts)
     1827 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     32866678 packets output, 3430977656 bytes, 0 underruns
     1166 output errors, 1720 collisions, 0 interface resets
     648 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/2 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c772.2941 (bia bc26.c772.2941)
  MTU 1500 bytes, BW 10000 Kbit/sec, DLY 1000 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Half-duplex, 10Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:02:16, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 2000 bits/sec, 3 packets/sec
     2956331 packets input, 377978125 bytes, 0 no buffer
               Received 691 broadcasts (0 multicasts)
     1901 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     32750186 packets output, 3418841421 bytes, 0 underruns
     1069 output errors, 1782 collisions, 0 interface resets
     674 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/3 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is bc26.c772.2942 (bia bc26.c772.2942)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 13w2d
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
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/4 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is bc26.c772.2943 (bia bc26.c772.2943)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 13w2d
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
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/5 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is bc26.c772.2944 (bia bc26.c772.2944)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 13w2d
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
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/6 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is bc26.c772.2945 (bia bc26.c772.2945)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 13w2d
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
               0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/7 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is bc26.c772.2946 (bia bc26.c772.2946)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 13w2d
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
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/8 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c772.2947 (bia bc26.c772.2947)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:03:16, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 241129253
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 2000 bits/sec, 13 packets/sec
  5 minute output rate 91000 bits/sec, 31 packets/sec
     12004670 packets input, 2119839674 bytes, 0 no buffer
     Received 692 broadcasts (135 multicasts)
     0 runts, 0 giants, 0 throttles 
     1 input errors, 1 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 135 multicast, 0 pause input
     0 input packets with dribble condition detected
     207279181 packets output, 55501875837 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     16 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
               0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/9 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is bc26.c772.2948 (bia bc26.c772.2948)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 13w2d
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
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/10 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c772.2949 (bia bc26.c772.2949)
  Description: #swisstube
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:32, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 1000 bits/sec, 2 packets/sec
     2385337 packets input, 157370081 bytes, 0 no buffer
     Received 14 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     15672026 packets output, 1485571156 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
          GigabitEthernet1/0/11 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c772.294a (bia bc26.c772.294a)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:09:05, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 2000 bits/sec, 3 packets/sec
     576020 packets input, 87781875 bytes, 0 no buffer
     Received 2 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     26041426 packets output, 2585860212 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/12 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c772.294b (bia bc26.c772.294b)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:07, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 2000 bits/sec, 3 packets/sec
     708058 packets input, 104233044 bytes, 0 no buffer
     Received 1 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     26180725 packets output, 2611892227 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/13 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is bc26.c772.294c (bia bc26.c772.294c)
  Description: #Omnicell
            MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 13w2d
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
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/14 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c772.294d (bia bc26.c772.294d)
  Description: #New OR HVAC RITM0300645
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:23, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 2000 bits/sec, 3 packets/sec
  5 minute output rate 3000 bits/sec, 6 packets/sec
     3048421 packets input, 214267087 bytes, 0 no buffer
     Received 8522 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     8557336 packets output, 677956734 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     8498 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/15 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c772.294e (bia bc26.c772.294e)
  Description: #Omnicell
  MTU 1500 bytes, BW 10000 Kbit/sec, DLY 1000 usec, 
               reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 10Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:27, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 2000 bits/sec, 1 packets/sec
     3369605 packets input, 530488539 bytes, 0 no buffer
     Received 104654 broadcasts (30106 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 30106 multicast, 0 pause input
     0 input packets with dribble condition detected
     25766861 packets output, 4180856986 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     46969 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/16 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c772.294f (bia bc26.c772.294f)
  Description: #Omnicell
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:03, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 9894
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 1000 bits/sec, 1 packets/sec
  5 minute output rate 2000 bits/sec, 2 packets/sec
     6695924 packets input, 1700763884 bytes, 0 no buffer
     Received 38641 broadcasts (53 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 53 multicast, 0 pause input
     0 input packets with dribble condition detected
     43667081 packets output, 5153578759 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     38523 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/17 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c772.2950 (bia bc26.c772.2950)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
            Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:23, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 1921191345
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 13000 bits/sec, 7 packets/sec
  5 minute output rate 8000 bits/sec, 11 packets/sec
     38931901 packets input, 10344534663 bytes, 0 no buffer
     Received 1028331 broadcasts (12 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 12 multicast, 74 pause input
     0 input packets with dribble condition detected
     89153231 packets output, 9469467715 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     1028222 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/18 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c772.2951 (bia bc26.c772.2951)
  Description: #BMDI 100/full
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:08:07, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 1000 bits/sec, 1 packets/sec
     5567985 packets input, 4194756408 bytes, 0 no buffer
     Received 337793 broadcasts (337793 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 337793 multicast, 0 pause input
     0 input packets with dribble condition detected
     16489972 packets output, 1526023839 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/19 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is bc26.c772.2952 (bia bc26.c772.2952)
  Description: #RTLS
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
            Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 13w2d
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
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/20 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c772.2953 (bia bc26.c772.2953)
  Description: #RTLS
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:03, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 1866233788
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 4000 bits/sec, 5 packets/sec
     295722 packets input, 40909043 bytes, 0 no buffer
     Received 26202 broadcasts (26202 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 26202 multicast, 0 pause input
     0 input packets with dribble condition detected
     36540309 packets output, 3737340192 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/21 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is bc26.c772.2954 (bia bc26.c772.2954)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
            ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 13w2d
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
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/22 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c772.2955 (bia bc26.c772.2955)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 13w6d, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 4000 bits/sec, 6 packets/sec
     1031327 packets input, 510638900 bytes, 0 no buffer
     Received 1031327 broadcasts (194887 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 194887 multicast, 0 pause input
     0 input packets with dribble condition detected
     42324314 packets output, 3803639476 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/23 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is bc26.c772.2956 (bia bc26.c772.2956)
  Description: Wireless AP
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 6w2d, output 6w2d, output hang never
            Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     135 packets input, 13414 bytes, 0 no buffer
     Received 134 broadcasts (48 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 48 multicast, 0 pause input
     0 input packets with dribble condition detected
     333 packets output, 47088 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     37 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/24 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c772.2957 (bia bc26.c772.2957)
  Description: Wireless AP
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:09, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 30028673
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 4000 bits/sec, 3 packets/sec
  5 minute output rate 3037000 bits/sec, 1365 packets/sec
     26791269 packets input, 5229703233 bytes, 0 no buffer
     Received 738922 broadcasts (602272 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 602272 multicast, 0 pause input
     0 input packets with dribble condition detected
     5418114933 packets output, 1528409152532 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     13 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/25 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c772.2958 (bia bc26.c772.2958)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:27, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 27064
            Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 34000 bits/sec, 55 packets/sec
     2291244 packets input, 237579795 bytes, 0 no buffer
     Received 141889 broadcasts (134567 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 134567 multicast, 23644 pause input
     0 input packets with dribble condition detected
     436894765 packets output, 33865002226 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     113 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/26 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c772.2959 (bia bc26.c772.2959)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:21, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 24412
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 33000 bits/sec, 55 packets/sec
     2077307 packets input, 185174088 bytes, 0 no buffer
     Received 855081 broadcasts (300536 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 300536 multicast, 0 pause input
     0 input packets with dribble condition detected
     453072767 packets output, 35986523108 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     5 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/27 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c772.295a (bia bc26.c772.295a)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:27, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 51000
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
            5 minute output rate 33000 bits/sec, 55 packets/sec
     1633299 packets input, 146442599 bytes, 0 no buffer
     Received 279310 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     453279433 packets output, 36062816203 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/28 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c772.295b (bia bc26.c772.295b)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:05, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 45832
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 34000 bits/sec, 55 packets/sec
     2801838 packets input, 291382527 bytes, 0 no buffer
     Received 311117 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     454745834 packets output, 36732711339 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/29 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c772.295c (bia bc26.c772.295c)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:26, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 1344564
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 33000 bits/sec, 54 packets/sec
     1769160 packets input, 161886261 bytes, 0 no buffer
     Received 281929 broadcasts (0 multicasts)
               0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     453662214 packets output, 36610258284 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/30 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c772.295d (bia bc26.c772.295d)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:02, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/1 (size/max/drops/flushes); Total output drops: 90984
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 32000 bits/sec, 54 packets/sec
     2316384 packets input, 191929293 bytes, 0 no buffer
     Received 862049 broadcasts (581711 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 581711 multicast, 0 pause input
     0 input packets with dribble condition detected
     453800277 packets output, 36659417392 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/31 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c772.295e (bia bc26.c772.295e)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:20, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 543048
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 32000 bits/sec, 54 packets/sec
     1839070 packets input, 171479146 bytes, 0 no buffer
     Received 244723 broadcasts (229379 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 229379 multicast, 0 pause input
               0 input packets with dribble condition detected
     453322600 packets output, 35829402367 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/32 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c772.295f (bia bc26.c772.295f)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:12, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 35224
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 33000 bits/sec, 54 packets/sec
     1653087 packets input, 155605778 bytes, 0 no buffer
     Received 142073 broadcasts (131626 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 131626 multicast, 10702 pause input
     0 input packets with dribble condition detected
     436377166 packets output, 33821591809 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     125 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/33 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c772.2960 (bia bc26.c772.2960)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:23, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 10404
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 31000 bits/sec, 53 packets/sec
     716554 packets input, 81196371 bytes, 0 no buffer
     Received 167597 broadcasts (146198 multicasts)
     0 runts, 0 giants, 0 throttles 
     10 input errors, 4 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 146198 multicast, 0 pause input
     0 input packets with dribble condition detected
     403027499 packets output, 31285242574 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
               0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/34 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c772.2961 (bia bc26.c772.2961)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:03, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 41140
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 31000 bits/sec, 53 packets/sec
     1840673 packets input, 168379048 bytes, 0 no buffer
     Received 288310 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     436781782 packets output, 34657426646 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/35 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c772.2962 (bia bc26.c772.2962)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:13, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 40732
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 31000 bits/sec, 53 packets/sec
     513228 packets input, 36802585 bytes, 0 no buffer
     Received 157279 broadcasts (135380 multicasts)
     0 runts, 0 giants, 0 throttles 
     1 input errors, 1 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 135380 multicast, 0 pause input
     0 input packets with dribble condition detected
     434980120 packets output, 33687754767 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     104 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
               0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/36 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c772.2963 (bia bc26.c772.2963)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:03, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 808452
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 31000 bits/sec, 53 packets/sec
     1752550 packets input, 159382159 bytes, 0 no buffer
     Received 283258 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     453335270 packets output, 36009289920 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/37 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c772.2964 (bia bc26.c772.2964)
  Description: NetBeez
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:01, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 10000 bits/sec, 12 packets/sec
     5414708 packets input, 983103033 bytes, 0 no buffer
     Received 74755 broadcasts (72486 multicasts)
     0 runts, 0 giants, 0 throttles 
     5 input errors, 2 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 72486 multicast, 0 pause input
     0 input packets with dribble condition detected
     57005796 packets output, 6732151502 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/38 is down, line protocol is down (notconnect) 
            Hardware is Gigabit Ethernet, address is bc26.c772.2965 (bia bc26.c772.2965)
  Description: #AP
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 13w2d
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
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/39 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c772.2966 (bia bc26.c772.2966)
  Description: #AP
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:01, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 59182349
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 45000 bits/sec, 16 packets/sec
  5 minute output rate 3385000 bits/sec, 1368 packets/sec
     54249767 packets input, 17617611679 bytes, 0 no buffer
     Received 894618 broadcasts (893081 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 893081 multicast, 0 pause input
     0 input packets with dribble condition detected
     5494942727 packets output, 1608897384771 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     10 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/40 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c772.2967 (bia bc26.c772.2967)
            Description: #AP
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:13, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/1 (size/max/drops/flushes); Total output drops: 223587127
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 2000 bits/sec, 1 packets/sec
  5 minute output rate 2945000 bits/sec, 1325 packets/sec
     276408252 packets input, 73436680478 bytes, 0 no buffer
     Received 894483 broadcasts (892944 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 892944 multicast, 0 pause input
     0 input packets with dribble condition detected
     5900676645 packets output, 2096936198488 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     8 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/41 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c772.2968 (bia bc26.c772.2968)
  Description: #AP
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:01, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 52536494
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 85000 bits/sec, 57 packets/sec
  5 minute output rate 3033000 bits/sec, 1377 packets/sec
     586545189 packets input, 184420028779 bytes, 0 no buffer
     Received 867366 broadcasts (865824 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 865824 multicast, 0 pause input
     0 input packets with dribble condition detected
     6288567064 packets output, 2390341671648 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     12 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/42 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c772.2969 (bia bc26.c772.2969)
  Description: #AP
            MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:13, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 2201843131
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 163000 bits/sec, 63 packets/sec
  5 minute output rate 3579000 bits/sec, 1420 packets/sec
     969495265 packets input, 305949075118 bytes, 0 no buffer
     Received 867377 broadcasts (865861 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 865861 multicast, 0 pause input
     0 input packets with dribble condition detected
     7106277639 packets output, 3380917273337 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     5 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/43 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c772.296a (bia bc26.c772.296a)
  Description: #AP
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:08, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 293921409
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 209000 bits/sec, 44 packets/sec
  5 minute output rate 3033000 bits/sec, 1358 packets/sec
     459538762 packets input, 167167805202 bytes, 0 no buffer
     Received 867347 broadcasts (865813 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 865813 multicast, 0 pause input
     0 input packets with dribble condition detected
     6014987787 packets output, 2103667402344 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     6 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/44 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c772.296b (bia bc26.c772.296b)
  Description: #AP
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
               reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:07, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/1 (size/max/drops/flushes); Total output drops: 121172387
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 55000 bits/sec, 33 packets/sec
  5 minute output rate 4499000 bits/sec, 1466 packets/sec
     127345494 packets input, 35778302912 bytes, 0 no buffer
     Received 894804 broadcasts (893290 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 893290 multicast, 0 pause input
     0 input packets with dribble condition detected
     5615913222 packets output, 1733553388819 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     6 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/45 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c772.296c (bia bc26.c772.296c)
  Description: #AP
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:13, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 835494074
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 126000 bits/sec, 80 packets/sec
  5 minute output rate 6715000 bits/sec, 1673 packets/sec
     299780123 packets input, 100157072834 bytes, 0 no buffer
     Received 891794 broadcasts (890265 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 890265 multicast, 0 pause input
     0 input packets with dribble condition detected
     5990785248 packets output, 2163501581047 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     7 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/46 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c772.296d (bia bc26.c772.296d)
  Description: #AP
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
            Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:11, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 931798496
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 37000 bits/sec, 18 packets/sec
  5 minute output rate 3329000 bits/sec, 1372 packets/sec
     374387046 packets input, 122516463741 bytes, 0 no buffer
     Received 891845 broadcasts (890305 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 890305 multicast, 0 pause input
     0 input packets with dribble condition detected
     6252685836 packets output, 2519401506374 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     7 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/47 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c772.296e (bia bc26.c772.296e)
  Description: #Emergency Radio (on roof)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:56, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 1000 bits/sec, 2 packets/sec
     15231734 packets input, 2519159642 bytes, 0 no buffer
     Received 31 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     29184939 packets output, 3209399191 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/48 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c772.296f (bia bc26.c772.296f)
  Description: #AP
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
            Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:14, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 116156040
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 101000 bits/sec, 52 packets/sec
  5 minute output rate 5533000 bits/sec, 1580 packets/sec
     181128424 packets input, 41498220771 bytes, 0 no buffer
     Received 894313 broadcasts (892782 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 892782 multicast, 0 pause input
     0 input packets with dribble condition detected
     5919926301 packets output, 2172259204875 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     11 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet4/0/1 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet, address is b08b.cfe2.d598 (bia b08b.cfe2.d598)
  Description: key:sx1-525hosp-1511:ten5/1
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-SR
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 6w1d, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/12790/83 (size/max/drops/flushes); Total output drops: 1032
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 1000 bits/sec, 2 packets/sec
  5 minute output rate 247000 bits/sec, 233 packets/sec
     23225723 packets input, 2872157183 bytes, 10 no buffer
     Received 19262492 broadcasts (18389759 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 18389759 multicast, 0 pause input
     0 input packets with dribble condition detected
     2308709516 packets output, 294448393295 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     6179 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet4/0/2 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet, address is b08b.cfe2.d599 (bia b08b.cfe2.d599)
  Description: key:sx1-525hosp-b244:ten5/2
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
            Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-SR
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:02:17, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 1590764
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 6000 bits/sec, 8 packets/sec
  5 minute output rate 244000 bits/sec, 230 packets/sec
     83227643 packets input, 10091076367 bytes, 0 no buffer
     Received 57699736 broadcasts (56361733 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 56361733 multicast, 0 pause input
     0 input packets with dribble condition detected
     2306012339 packets output, 293199447401 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     527 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet4/0/3 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet, address is b08b.cfe2.d59a (bia b08b.cfe2.d59a)
  Description: key:sx1-525hosp-4270:ten1/1
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-SR
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 13w2d, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 3796545
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 1000 bits/sec, 1 packets/sec
  5 minute output rate 248000 bits/sec, 234 packets/sec
     19179973 packets input, 2489102144 bytes, 0 no buffer
     Received 9604381 broadcasts (9465770 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 9465770 multicast, 0 pause input
     0 input packets with dribble condition detected
     2329419388 packets output, 296350567436 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     239 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet4/0/4 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet, address is b08b.cfe2.d59b (bia b08b.cfe2.d59b)
  Description: key:sx1-525hosp-3043:ten1/2
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-SR
            input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 13w2d, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 3484243
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 1000 bits/sec, 3 packets/sec
  5 minute output rate 247000 bits/sec, 233 packets/sec
     40257169 packets input, 5047216014 bytes, 9 no buffer
     Received 17884951 broadcasts (17606720 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 17606720 multicast, 0 pause input
     0 input packets with dribble condition detected
     2325300824 packets output, 296938043946 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     34 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet4/0/5 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet, address is b08b.cfe2.d59c (bia b08b.cfe2.d59c)
  Description: key:sx1-525hosp-1873:ten1/2
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-SR
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:19, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 2055090
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 241000 bits/sec, 227 packets/sec
     13969295 packets input, 1317891387 bytes, 11 no buffer
     Received 13078069 broadcasts (12864437 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 12864437 multicast, 0 pause input
     0 input packets with dribble condition detected
     2322972373 packets output, 294523270716 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     157 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet4/0/6 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet, address is b08b.cfe2.d59d (bia b08b.cfe2.d59d)
  Description: key:sx2-525hosp-3745:ten5/1
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-SR
  input flow-control is off, output flow-control is unsupported 
            ARP type: ARPA, ARP Timeout 04:00:00
  Last input 1w5d, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 485788
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 241000 bits/sec, 227 packets/sec
     9053865 packets input, 821469084 bytes, 0 no buffer
     Received 8802328 broadcasts (8797592 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 8797592 multicast, 0 pause input
     0 input packets with dribble condition detected
     2319989198 packets output, 294561217932 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     17 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet4/0/7 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet, address is b08b.cfe2.d59e (bia b08b.cfe2.d59e)
  Description: key:sx1-525hosp-3745:ten5/1
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-SR
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 1w5d, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/328/0 (size/max/drops/flushes); Total output drops: 1008083
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 2000 bits/sec, 4 packets/sec
  5 minute output rate 240000 bits/sec, 226 packets/sec
     47121634 packets input, 5768636610 bytes, 12 no buffer
     Received 29887996 broadcasts (28864270 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 28864270 multicast, 0 pause input
     0 input packets with dribble condition detected
     2316626044 packets output, 295584202932 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     442 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet4/0/8 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet, address is b08b.cfe2.d59f (bia b08b.cfe2.d59f)
  Description: key:sx1-525hosp-3306:ten5/1
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-SR
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
            Last input 13w2d, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 36228429
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 240000 bits/sec, 226 packets/sec
     32169691 packets input, 3352981881 bytes, 6 no buffer
     Received 17176288 broadcasts (17011746 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 17011746 multicast, 0 pause input
     0 input packets with dribble condition detected
     2326008396 packets output, 296075028042 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     360 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet4/0/9 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet, address is b08b.cfe2.d5a0 (bia b08b.cfe2.d5a0)
  Description: key:sx2-525hosp-a371:t1/1/2
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-SR
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 13w2d, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/26/0 (size/max/drops/flushes); Total output drops: 11383350
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 3000 bits/sec, 5 packets/sec
  5 minute output rate 236000 bits/sec, 226 packets/sec
     70202778 packets input, 9472162078 bytes, 12 no buffer
     Received 44170774 broadcasts (43511273 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 43511273 multicast, 0 pause input
     0 input packets with dribble condition detected
     2293769812 packets output, 291412413254 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     9 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet4/0/10 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet, address is b08b.cfe2.d5a1 (bia b08b.cfe2.d5a1)
  Description: key:sx1-525hosp-4317:ten5/2
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-SR
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:01:16, output 00:00:00, output hang never
            Last clearing of "" counters 13w2d
  Input queue: 0/375/43/0 (size/max/drops/flushes); Total output drops: 6486422
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 5000 bits/sec, 7 packets/sec
  5 minute output rate 66000 bits/sec, 86 packets/sec
     58006667 packets input, 5041433483 bytes, 33 no buffer
     Received 57016453 broadcasts (55903229 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 55903229 multicast, 0 pause input
     0 input packets with dribble condition detected
     858828140 packets output, 85051981030 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     68773 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet4/0/11 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet, address is b08b.cfe2.d5a2 (bia b08b.cfe2.d5a2)
  Description: key:sx1-525hosp-1443:ten1/2
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-SR
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 13w2d, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 43956024
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 66000 bits/sec, 78 packets/sec
     14849912 packets input, 1490311782 bytes, 44 no buffer
     Received 13474507 broadcasts (13426906 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 13426906 multicast, 0 pause input
     0 input packets with dribble condition detected
     771914134 packets output, 77509034798 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     24 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet4/0/12 is down, line protocol is down (notconnect) 
  Hardware is Ten Gigabit Ethernet, address is b08b.cfe2.d5a3 (bia b08b.cfe2.d5a3)
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-SR
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 13w2d
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
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet4/0/13 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet, address is b08b.cfe2.d5a4 (bia b08b.cfe2.d5a4)
  Description: key:sx1-525hosp-5105:ten5/2
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-SR
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:01:58, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 29619258
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 2000 bits/sec, 4 packets/sec
  5 minute output rate 242000 bits/sec, 228 packets/sec
     37375890 packets input, 4156388253 bytes, 8 no buffer
     Received 20177916 broadcasts (19964506 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 19964506 multicast, 0 pause input
     0 input packets with dribble condition detected
     2322995393 packets output, 295581022296 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     209 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet4/0/14 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet, address is b08b.cfe2.d5a5 (bia b08b.cfe2.d5a5)
  Description: key:sx1-525hosp-6103:ten5/2
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-SR
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 13w2d, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 24125414
  Queueing strategy: fifo
            Output queue: 0/40 (size/max)
  5 minute input rate 1000 bits/sec, 2 packets/sec
  5 minute output rate 243000 bits/sec, 229 packets/sec
     36408564 packets input, 4088448650 bytes, 6 no buffer
     Received 17873561 broadcasts (17605518 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 17605518 multicast, 0 pause input
     0 input packets with dribble condition detected
     2325623898 packets output, 295492895477 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     47 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet4/0/15 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet, address is b08b.cfe2.d5a6 (bia b08b.cfe2.d5a6)
  Description: key:sx1-525hosp-a371:ten5/2
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-SR
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:02:53, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/53/0 (size/max/drops/flushes); Total output drops: 7498742
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 4000 bits/sec, 6 packets/sec
  5 minute output rate 64000 bits/sec, 81 packets/sec
     56429605 packets input, 7347345096 bytes, 35 no buffer
     Received 47054212 broadcasts (46684711 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 46684711 multicast, 0 pause input
     0 input packets with dribble condition detected
     771247316 packets output, 76772452800 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     146 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet4/0/16 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet, address is b08b.cfe2.d5a7 (bia b08b.cfe2.d5a7)
  Description: key:sx1-525hosp-2411:ten5/1
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-SR
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 13w2d, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 38792367
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
            5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 244000 bits/sec, 230 packets/sec
     33427750 packets input, 4378503078 bytes, 12 no buffer
     Received 13281200 broadcasts (12966533 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 12966533 multicast, 0 pause input
     0 input packets with dribble condition detected
     2326592096 packets output, 295766296830 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     54 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet4/0/17 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet, address is b08b.cfe2.d5a8 (bia b08b.cfe2.d5a8)
  Description: key:sx1-525hosp-2741:ten5/2
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-SR
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 13w2d, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 42902094
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 2000 bits/sec, 3 packets/sec
  5 minute output rate 243000 bits/sec, 230 packets/sec
     33011397 packets input, 3649418050 bytes, 11 no buffer
     Received 21941356 broadcasts (21660692 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 21660692 multicast, 0 pause input
     0 input packets with dribble condition detected
     2326931458 packets output, 295734831820 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     235 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet4/0/18 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet, address is b08b.cfe2.d5a9 (bia b08b.cfe2.d5a9)
  Description: key:sx2-525hosp-4317:te1/1/2
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-SR
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 13w2d, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 20008289
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 3000 bits/sec, 5 packets/sec
            5 minute output rate 71000 bits/sec, 93 packets/sec
     48642783 packets input, 4570906158 bytes, 9 no buffer
     Received 34360550 broadcasts (33022860 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 33022860 multicast, 0 pause input
     0 input packets with dribble condition detected
     916517813 packets output, 91327300397 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     43 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet4/0/19 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet, address is b08b.cfe2.d5aa (bia b08b.cfe2.d5aa)
  Description: #key:sx1-525hosp-4625:e5/2
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-SR
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 13w2d, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/151/0 (size/max/drops/flushes); Total output drops: 11925868
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 243000 bits/sec, 231 packets/sec
     39009002 packets input, 5176764268 bytes, 23 no buffer
     Received 9953657 broadcasts (9502515 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 9502515 multicast, 0 pause input
     0 input packets with dribble condition detected
     2339995484 packets output, 297103165183 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     5 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet4/0/20 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet, address is b08b.cfe2.d5ab (bia b08b.cfe2.d5ab)
  Description: key:sx1-525hosp-2673:t1/1/3
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-LR
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 9w4d, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/2 (size/max/drops/flushes); Total output drops: 102596439
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  30 second input rate 3000 bits/sec, 5 packets/sec
  30 second output rate 65000 bits/sec, 78 packets/sec
               38944609 packets input, 5064692602 bytes, 0 no buffer
     Received 33429994 broadcasts (30706649 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 30706649 multicast, 0 pause input
     0 input packets with dribble condition detected
     1217012247 packets output, 155730703185 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     717 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet4/0/21 is down, line protocol is down (notconnect) 
  Hardware is Ten Gigabit Ethernet, address is b08b.cfe2.d5ac (bia b08b.cfe2.d5ac)
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 10Gb/s, link type is auto, media type is 
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 13w2d
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
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet4/0/22 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet, address is b08b.cfe2.d5ad (bia b08b.cfe2.d5ad)
  Description: key:sx1-525hosp-1437b:t5/1
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-SR
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 13w2d, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 12230778
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 1000 bits/sec, 1 packets/sec
  5 minute output rate 246000 bits/sec, 232 packets/sec
     28306566 packets input, 3648582142 bytes, 17 no buffer
     Received 9621026 broadcasts (9333366 multicasts)
               0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 9333366 multicast, 0 pause input
     0 input packets with dribble condition detected
     2350735219 packets output, 297965561237 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     11 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet4/0/23 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet, address is b08b.cfe2.d5ae (bia b08b.cfe2.d5ae)
  Description: key:sx1-525hosp-2255:g2/1/1
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, link type is auto, media type is 1000BaseSX SFP
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 12w3d, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 46974769
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 4000 bits/sec, 4 packets/sec
  5 minute output rate 72000 bits/sec, 90 packets/sec
     31229260 packets input, 6870660301 bytes, 0 no buffer
     Received 26225998 broadcasts (25133589 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 25133589 multicast, 0 pause input
     0 input packets with dribble condition detected
     901557987 packets output, 91856991829 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     397 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet4/0/24 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet, address is b08b.cfe2.d5af (bia b08b.cfe2.d5af)
  Description: key:sx1-525hosp-a673:g1/0/49
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, link type is auto, media type is 1000BaseSX SFP
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 13w2d, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 5465169
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 73000 bits/sec, 90 packets/sec
     2048280 packets input, 329346241 bytes, 0 no buffer
     Received 1234963 broadcasts (1234633 multicasts)
     0 runts, 0 giants, 0 throttles 
               0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 1234633 multicast, 0 pause input
     0 input packets with dribble condition detected
     849211064 packets output, 87245921514 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     118 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet5/0/1 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet, address is a093.51d2.5c6c (bia a093.51d2.5c6c)
  Description: key:r1-clinical:e2/10
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-SR
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 2291971
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 1634000 bits/sec, 435 packets/sec
  5 minute output rate 1204000 bits/sec, 614 packets/sec
     5627325904 packets input, 4043965727309 bytes, 0 no buffer
     Received 1344532661 broadcasts (866873960 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 866873960 multicast, 0 pause input
     0 input packets with dribble condition detected
     4590615421 packets output, 1357733526871 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet5/0/2 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet, address is a093.51d2.5c6d (bia a093.51d2.5c6d)
  Description: key:r2-clinical:e2/10
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-LR
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 825
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 13728000 bits/sec, 2568 packets/sec
  5 minute output rate 538000 bits/sec, 255 packets/sec
     11747112614 packets input, 7201447513786 bytes, 0 no buffer
     Received 6280849519 broadcasts (1672853598 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
               0 watchdog, 1672853598 multicast, 0 pause input
     0 input packets with dribble condition detected
     2284548777 packets output, 614073618340 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet5/0/3 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet, address is a093.51d2.5c6e (bia a093.51d2.5c6e)
  Description: t5/0/3:sx1-525-infill:t5/0/2
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-LR
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 13w2d, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/136/0 (size/max/drops/flushes); Total output drops: 188497719
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 237000 bits/sec, 224 packets/sec
     53106481 packets input, 5530128517 bytes, 43 no buffer
     Received 14555410 broadcasts (13702782 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 13702782 multicast, 0 pause input
     0 input packets with dribble condition detected
     2345017287 packets output, 297881499565 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     5569 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet5/0/4 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet, address is a093.51d2.5c6f (bia a093.51d2.5c6f)
  Description: t5/0/4:sx2-525infill:t1/0/2
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-LR
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 13w2d, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 1211285614
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 2000 bits/sec, 2 packets/sec
  5 minute output rate 236000 bits/sec, 223 packets/sec
     35613666 packets input, 3237175195 bytes, 0 no buffer
     Received 25409685 broadcasts (25183073 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 25183073 multicast, 0 pause input
               0 input packets with dribble condition detected
     2336128381 packets output, 296883879311 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     66 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet5/0/5 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet, address is a093.51d2.5c70 (bia a093.51d2.5c70)
  Description: t5/0/5:sx1-525-1408:t1/1/2
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-LR
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 13w2d, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/1081/0 (size/max/drops/flushes); Total output drops: 1108351636
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 237000 bits/sec, 224 packets/sec
     24970472 packets input, 3603499967 bytes, 158 no buffer
     Received 9499146 broadcasts (9496972 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 9496972 multicast, 0 pause input
     0 input packets with dribble condition detected
     2321425829 packets output, 295457076298 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     16 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet5/0/6 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet, address is a093.51d2.5c71 (bia a093.51d2.5c71)
  Description: t5/0/6:sx1-525-1408:t5/0/2
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-LR
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 237000 bits/sec, 224 packets/sec
     3089728 packets input, 261196145 bytes, 0 no buffer
     Received 2845809 broadcasts (2845809 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 2845809 multicast, 0 pause input
     0 input packets with dribble condition detected
               591403103 packets output, 76920220997 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet5/0/7 is down, line protocol is down (notconnect) 
  Hardware is Ten Gigabit Ethernet, address is a093.51d2.5c72 (bia a093.51d2.5c72)
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 10Gb/s, link type is auto, media type is 
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 13w2d
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
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet5/0/8 is down, line protocol is down (notconnect) 
  Hardware is Ten Gigabit Ethernet, address is a093.51d2.5c73 (bia a093.51d2.5c73)
  Description: #temp uplink to old switch
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 10Gb/s, link type is auto, media type is 
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 13w2d
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
     0 output errors, 0 collisions, 0 interface resets
               0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
FortyGigabitEthernet5/0/9 is down, line protocol is down (inactive) 
  Hardware is Forty Gigabit Ethernet, address is a093.51d2.5c74 (bia a093.51d2.5c74)
  MTU 1500 bytes, BW 40000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 13w2d
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
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
FortyGigabitEthernet5/0/10 is down, line protocol is down (inactive) 
  Hardware is Forty Gigabit Ethernet, address is a093.51d2.5c75 (bia a093.51d2.5c75)
  MTU 1500 bytes, BW 40000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 13w2d
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
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
               0 output buffer failures, 0 output buffers swapped out
GigabitEthernet7/0/1 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.66b4 (bia bc26.c723.66b4)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:08:27, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 6000 bits/sec, 8 packets/sec
     9798448 packets input, 697231668 bytes, 0 no buffer
     Received 40 broadcasts (6 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 6 multicast, 0 pause input
     0 input packets with dribble condition detected
     61577851 packets output, 8220388208 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet7/0/2 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.66b5 (bia bc26.c723.66b5)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:04:01, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 6000 bits/sec, 8 packets/sec
     11487182 packets input, 1545050331 bytes, 0 no buffer
     Received 258 broadcasts (23 multicasts)
     0 runts, 0 giants, 0 throttles 
     2 input errors, 2 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 23 multicast, 0 pause input
     0 input packets with dribble condition detected
     57664896 packets output, 9096942154 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet7/0/3 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.66b6 (bia bc26.c723.66b6)
            MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:30, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 14000 bits/sec, 14 packets/sec
     11779046 packets input, 10519649510 bytes, 0 no buffer
     Received 488813 broadcasts (443566 multicasts)
     0 runts, 0 giants, 0 throttles 
     5 input errors, 5 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 443566 multicast, 0 pause input
     0 input packets with dribble condition detected
     103787723 packets output, 15300504847 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     29580 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet7/0/4 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.66b7 (bia bc26.c723.66b7)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:08:10, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 74000 bits/sec, 8 packets/sec
     83092522 packets input, 6273557871 bytes, 0 no buffer
     Received 270701 broadcasts (270609 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 270609 multicast, 0 pause input
     0 input packets with dribble condition detected
     130724652 packets output, 69330710967 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet7/0/5 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.66b8 (bia bc26.c723.66b8)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
            Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:07, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 281987098
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 6000 bits/sec, 2 packets/sec
  5 minute output rate 19000 bits/sec, 16 packets/sec
     163632170 packets input, 50652607294 bytes, 0 no buffer
     Received 773147 broadcasts (771624 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 771624 multicast, 0 pause input
     0 input packets with dribble condition detected
     426346594 packets output, 415106010058 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     10 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet7/0/6 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.66b9 (bia bc26.c723.66b9)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:01, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 13000 bits/sec, 14 packets/sec
     11954660 packets input, 10902902002 bytes, 0 no buffer
     Received 389458 broadcasts (350520 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 350520 multicast, 0 pause input
     0 input packets with dribble condition detected
     102108489 packets output, 14542002911 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     26205 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet7/0/7 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is bc26.c723.66ba (bia bc26.c723.66ba)
  MTU 1500 bytes, BW 10000 Kbit/sec, DLY 1000 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
            ARP type: ARPA, ARP Timeout 04:00:00
  Last input 21w0d, output 21w0d, output hang never
  Last clearing of "" counters 13w2d
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
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet7/0/8 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.66bb (bia bc26.c723.66bb)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:36, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 61000 bits/sec, 8 packets/sec
     18364886 packets input, 1250445146 bytes, 0 no buffer
     Received 9 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     65657116 packets output, 15837087580 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet7/0/9 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is bc26.c723.66bc (bia bc26.c723.66bc)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 13w2d
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
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet7/0/10 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.66bd (bia bc26.c723.66bd)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:06, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 15000 bits/sec, 14 packets/sec
     6837484 packets input, 873277408 bytes, 0 no buffer
     Received 385461 broadcasts (314423 multicasts)
     2 runts, 0 giants, 0 throttles 
     434 input errors, 218 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 314423 multicast, 0 pause input
     0 input packets with dribble condition detected
     103467343 packets output, 16638945791 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     65772 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet7/0/11 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.66be (bia bc26.c723.66be)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:01:54, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
            5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 6000 bits/sec, 8 packets/sec
     27198388 packets input, 1871769501 bytes, 0 no buffer
     Received 53 broadcasts (12 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 12 multicast, 0 pause input
     0 input packets with dribble condition detected
     80409947 packets output, 30991085585 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet7/0/12 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is bc26.c723.66bf (bia bc26.c723.66bf)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 13w2d
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
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet7/0/13 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.66c0 (bia bc26.c723.66c0)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:09:29, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 2000 bits/sec, 1 packets/sec
  5 minute output rate 17000 bits/sec, 15 packets/sec
     10181946 packets input, 2026188397 bytes, 0 no buffer
               Received 979 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     106426809 packets output, 16053746539 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet7/0/14 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.66c1 (bia bc26.c723.66c1)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:27, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 12000 bits/sec, 14 packets/sec
     360870 packets input, 55177883 bytes, 0 no buffer
     Received 155925 broadcasts (143320 multicasts)
     0 runts, 0 giants, 0 throttles 
     8 input errors, 2 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 143320 multicast, 0 pause input
     0 input packets with dribble condition detected
     88108364 packets output, 10299583892 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet7/0/15 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is bc26.c723.66c2 (bia bc26.c723.66c2)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 13w2d
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
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet7/0/16 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.66c3 (bia bc26.c723.66c3)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:01, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 1000 bits/sec, 2 packets/sec
  5 minute output rate 15000 bits/sec, 17 packets/sec
     16860436 packets input, 3088859317 bytes, 0 no buffer
     Received 578063 broadcasts (57403 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 57403 multicast, 0 pause input
     0 input packets with dribble condition detected
     122104881 packets output, 17135031102 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet7/0/17 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.66c4 (bia bc26.c723.66c4)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:04:45, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 12000 bits/sec, 13 packets/sec
     2014006 packets input, 717650089 bytes, 0 no buffer
     Received 270632 broadcasts (270608 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 270608 multicast, 0 pause input
     0 input packets with dribble condition detected
     97210219 packets output, 11665281212 bytes, 0 underruns
               0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet7/0/18 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.66c5 (bia bc26.c723.66c5)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 448547200
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 9000 bits/sec, 6 packets/sec
  5 minute output rate 30000 bits/sec, 21 packets/sec
     76278196 packets input, 22148242231 bytes, 0 no buffer
     Received 469029 broadcasts (442844 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 442844 multicast, 0 pause input
     0 input packets with dribble condition detected
     185471384 packets output, 67814646934 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     18674 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet7/0/19 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.66c6 (bia bc26.c723.66c6)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:08:29, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 6000 bits/sec, 8 packets/sec
     987095 packets input, 83843124 bytes, 0 no buffer
     Received 21 broadcasts (3 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 3 multicast, 0 pause input
     0 input packets with dribble condition detected
     50005141 packets output, 4613242818 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
               0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet7/0/20 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.66c7 (bia bc26.c723.66c7)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:09:04, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 7000 bits/sec, 10 packets/sec
     30583277 packets input, 2114618339 bytes, 0 no buffer
     Received 47 broadcasts (15 multicasts)
     0 runts, 0 giants, 0 throttles 
     1 input errors, 1 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 15 multicast, 0 pause input
     0 input packets with dribble condition detected
     82581320 packets output, 32885749083 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet7/0/21 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.66c8 (bia bc26.c723.66c8)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:05, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 328646558
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 4000 bits/sec, 2 packets/sec
  5 minute output rate 66000 bits/sec, 19 packets/sec
     82748142 packets input, 17847860942 bytes, 0 no buffer
     Received 433284 broadcasts (409649 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 409649 multicast, 0 pause input
     0 input packets with dribble condition detected
     187502566 packets output, 85415618954 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     18072 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet7/0/22 is up, line protocol is up (connected) 
            Hardware is Gigabit Ethernet, address is bc26.c723.66c9 (bia bc26.c723.66c9)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 364928167
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 12000 bits/sec, 5 packets/sec
  5 minute output rate 26000 bits/sec, 20 packets/sec
     62994010 packets input, 17643398189 bytes, 0 no buffer
     Received 402407 broadcasts (375778 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 375778 multicast, 0 pause input
     0 input packets with dribble condition detected
     160850174 packets output, 40454038779 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     18139 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet7/0/23 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.66ca (bia bc26.c723.66ca)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:01:51, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 11000 bits/sec, 13 packets/sec
     357501 packets input, 55467272 bytes, 0 no buffer
     Received 159207 broadcasts (146346 multicasts)
     0 runts, 0 giants, 0 throttles 
     4 input errors, 2 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 146346 multicast, 0 pause input
     0 input packets with dribble condition detected
     89317383 packets output, 10445137602 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet7/0/24 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.66cb (bia bc26.c723.66cb)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
            Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:59, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 66000 bits/sec, 11 packets/sec
     39480675 packets input, 2715985657 bytes, 0 no buffer
     Received 1268 broadcasts (9 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 9 multicast, 0 pause input
     0 input packets with dribble condition detected
     79436466 packets output, 45847074001 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet7/0/25 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.66cc (bia bc26.c723.66cc)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:03:26, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 11000 bits/sec, 13 packets/sec
     2821450 packets input, 2978491132 bytes, 0 no buffer
     Received 8559 broadcasts (2350 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 2350 multicast, 0 pause input
     0 input packets with dribble condition detected
     97567119 packets output, 11372373784 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     8 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet7/0/26 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.66cd (bia bc26.c723.66cd)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
            input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:02:35, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 6000 bits/sec, 9 packets/sec
     82030578 packets input, 6342024360 bytes, 0 no buffer
     Received 270781 broadcasts (270632 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 270632 multicast, 0 pause input
     0 input packets with dribble condition detected
     132736183 packets output, 80912067758 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet7/0/27 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.66ce (bia bc26.c723.66ce)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:08:39, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 7000 bits/sec, 13 packets/sec
  5 minute output rate 89000 bits/sec, 19 packets/sec
     29105500 packets input, 2356880158 bytes, 0 no buffer
     Received 270698 broadcasts (270608 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 270608 multicast, 0 pause input
     0 input packets with dribble condition detected
     80883708 packets output, 26672224526 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet7/0/28 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.66cf (bia bc26.c723.66cf)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output 00:00:01, output hang never
            Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 468727604
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 407000 bits/sec, 66 packets/sec
  5 minute output rate 431000 bits/sec, 67 packets/sec
     288698146 packets input, 181949972676 bytes, 0 no buffer
     Received 741878 broadcasts (711294 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 711294 multicast, 0 pause input
     0 input packets with dribble condition detected
     378570322 packets output, 258447435067 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     18203 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet7/0/29 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.66d0 (bia bc26.c723.66d0)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:01, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 616660610
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 13000 bits/sec, 9 packets/sec
  5 minute output rate 25000 bits/sec, 19 packets/sec
     164582625 packets input, 32159494583 bytes, 0 no buffer
     Received 746927 broadcasts (724141 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 724141 multicast, 0 pause input
     0 input packets with dribble condition detected
     280860817 packets output, 117606845006 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     18060 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet7/0/30 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.66d1 (bia bc26.c723.66d1)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:01:26, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
            Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 6000 bits/sec, 9 packets/sec
     26523169 packets input, 1837104275 bytes, 0 no buffer
     Received 94 broadcasts (28 multicasts)
     0 runts, 0 giants, 0 throttles 
     3 input errors, 3 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 28 multicast, 0 pause input
     0 input packets with dribble condition detected
     77095170 packets output, 29064425280 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet7/0/31 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is bc26.c723.66d2 (bia bc26.c723.66d2)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 13w2d
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
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet7/0/32 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.66d3 (bia bc26.c723.66d3)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:10:12, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 1000 bits/sec, 2 packets/sec
  5 minute output rate 12000 bits/sec, 16 packets/sec
               15485775 packets input, 1196312376 bytes, 0 no buffer
     Received 4146 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     6 input errors, 6 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     110734980 packets output, 12152891634 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     503 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet7/0/33 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.66d4 (bia bc26.c723.66d4)
  Description: Paging
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 19:40:23, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 1000 bits/sec, 1 packets/sec
     1550050 packets input, 333143140 bytes, 0 no buffer
     Received 1039934 broadcasts (437510 multicasts)
     0 runts, 0 giants, 0 throttles 
     8 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 437510 multicast, 0 pause input
     0 input packets with dribble condition detected
     18726388 packets output, 1816321370 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet7/0/34 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is bc26.c723.66d5 (bia bc26.c723.66d5)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 13w2d
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
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet7/0/35 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is bc26.c723.66d6 (bia bc26.c723.66d6)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 13w2d
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
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet7/0/36 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is bc26.c723.66d7 (bia bc26.c723.66d7)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 13w2d
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
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet7/0/37 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.66d8 (bia bc26.c723.66d8)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 782818715
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 18000 bits/sec, 7 packets/sec
  5 minute output rate 58000 bits/sec, 23 packets/sec
     130149744 packets input, 24758566249 bytes, 0 no buffer
     Received 469851 broadcasts (428788 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 428788 multicast, 0 pause input
     0 input packets with dribble condition detected
     240029660 packets output, 106005591373 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     18166 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet7/0/38 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.66d9 (bia bc26.c723.66d9)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:01:50, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 6000 bits/sec, 9 packets/sec
     6180047 packets input, 436627608 bytes, 0 no buffer
     Received 35 broadcasts (9 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 9 multicast, 0 pause input
     0 input packets with dribble condition detected
     58402671 packets output, 8186897780 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
               0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet7/0/39 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.66da (bia bc26.c723.66da)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:08:00, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 7000 bits/sec, 9 packets/sec
     1066515 packets input, 85219742 bytes, 0 no buffer
     Received 21 broadcasts (3 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 3 multicast, 0 pause input
     0 input packets with dribble condition detected
     50165295 packets output, 5290489862 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet7/0/40 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.66db (bia bc26.c723.66db)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:08:49, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 6000 bits/sec, 8 packets/sec
     1084255 packets input, 85972475 bytes, 0 no buffer
     Received 9 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     50196653 packets output, 5287579076 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
               0 output buffer failures, 0 output buffers swapped out
GigabitEthernet7/0/41 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.66dc (bia bc26.c723.66dc)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:09:01, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 5000 bits/sec, 8 packets/sec
     1074176 packets input, 85335994 bytes, 0 no buffer
     Received 9 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     50180761 packets output, 5289199281 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet7/0/42 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.66dd (bia bc26.c723.66dd)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:10, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 79776436
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 10000 bits/sec, 4 packets/sec
  5 minute output rate 27000 bits/sec, 18 packets/sec
     78936885 packets input, 32557280157 bytes, 0 no buffer
     Received 415501 broadcasts (400737 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 400737 multicast, 0 pause input
     0 input packets with dribble condition detected
     207129644 packets output, 97704392686 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     4277 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet7/0/43 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.66de (bia bc26.c723.66de)
            MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:01, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 535526749
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 30000 bits/sec, 25 packets/sec
  5 minute output rate 279000 bits/sec, 45 packets/sec
     116310738 packets input, 41822872526 bytes, 0 no buffer
     Received 799175 broadcasts (755382 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 755382 multicast, 0 pause input
     0 input packets with dribble condition detected
     213696084 packets output, 89486623843 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     17820 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet7/0/44 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.66df (bia bc26.c723.66df)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:02:54, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 5000 bits/sec, 11 packets/sec
  5 minute output rate 189000 bits/sec, 20 packets/sec
     25178792 packets input, 2018628447 bytes, 0 no buffer
     Received 270730 broadcasts (270609 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 270609 multicast, 0 pause input
     0 input packets with dribble condition detected
     77743638 packets output, 24288821732 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet7/0/45 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.66e0 (bia bc26.c723.66e0)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
            Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:01:24, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 6000 bits/sec, 9 packets/sec
     97173096 packets input, 7281861897 bytes, 0 no buffer
     Received 270701 broadcasts (270619 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 270619 multicast, 0 pause input
     0 input packets with dribble condition detected
     150653956 packets output, 98586701471 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet7/0/46 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.66e1 (bia bc26.c723.66e1)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:03:30, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 5000 bits/sec, 8 packets/sec
     26455593 packets input, 1816053445 bytes, 0 no buffer
     Received 128 broadcasts (9 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 9 multicast, 0 pause input
     0 input packets with dribble condition detected
     80785722 packets output, 28742714043 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet7/0/47 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.66e2 (bia bc26.c723.66e2)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
            ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:11:23, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 23000 bits/sec, 8 packets/sec
     28896525 packets input, 2001796962 bytes, 0 no buffer
     Received 23 broadcasts (6 multicasts)
     0 runts, 0 giants, 0 throttles 
     1 input errors, 1 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 6 multicast, 0 pause input
     0 input packets with dribble condition detected
     81099022 packets output, 30403930555 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet7/0/48 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.66e3 (bia bc26.c723.66e3)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:09:10, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 66000 bits/sec, 9 packets/sec
     52430990 packets input, 4187419613 bytes, 0 no buffer
     Received 270845 broadcasts (270627 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 270627 multicast, 0 pause input
     0 input packets with dribble condition detected
     100443235 packets output, 41965678743 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet8/0/1 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.78b4 (bia bc26.c723.78b4)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:05, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
            Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 409345442
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 5000 bits/sec, 4 packets/sec
  5 minute output rate 18000 bits/sec, 21 packets/sec
     75429889 packets input, 20426016599 bytes, 0 no buffer
     Received 676452 broadcasts (647649 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 647649 multicast, 0 pause input
     0 input packets with dribble condition detected
     183388379 packets output, 67178101324 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     16782 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet8/0/2 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.78b5 (bia bc26.c723.78b5)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:07:55, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 6000 bits/sec, 8 packets/sec
     972843 packets input, 132412282 bytes, 0 no buffer
     Received 270615 broadcasts (270608 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 270608 multicast, 0 pause input
     0 input packets with dribble condition detected
     49951022 packets output, 4608197219 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet8/0/3 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.78b6 (bia bc26.c723.78b6)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:26, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
            5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 13000 bits/sec, 15 packets/sec
     4675562 packets input, 1697211906 bytes, 0 no buffer
     Received 295173 broadcasts (272883 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 272883 multicast, 0 pause input
     0 input packets with dribble condition detected
     99122160 packets output, 13397619954 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     1826 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet8/0/4 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.78b7 (bia bc26.c723.78b7)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:51, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 16153
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 14000 bits/sec, 15 packets/sec
     6871020 packets input, 899031375 bytes, 0 no buffer
     Received 417568 broadcasts (406016 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 406016 multicast, 0 pause input
     0 input packets with dribble condition detected
     103584657 packets output, 16650358602 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     66 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet8/0/5 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.78b8 (bia bc26.c723.78b8)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:17, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 14000 bits/sec, 24 packets/sec
  5 minute output rate 99000 bits/sec, 27 packets/sec
     102533067 packets input, 10127041669 bytes, 0 no buffer
               Received 270705 broadcasts (270621 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 270621 multicast, 0 pause input
     0 input packets with dribble condition detected
     158480019 packets output, 112448007156 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet8/0/6 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is bc26.c723.78b9 (bia bc26.c723.78b9)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 13w2d
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
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet8/0/7 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.78ba (bia bc26.c723.78ba)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:08:41, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 3000 bits/sec, 5 packets/sec
  5 minute output rate 38000 bits/sec, 11 packets/sec
     29456705 packets input, 2039026537 bytes, 0 no buffer
     Received 52 broadcasts (10 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
               0 watchdog, 10 multicast, 0 pause input
     0 input packets with dribble condition detected
     81993142 packets output, 32449118786 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet8/0/8 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.78bb (bia bc26.c723.78bb)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:04:26, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 26000 bits/sec, 9 packets/sec
     22123224 packets input, 1541647239 bytes, 0 no buffer
     Received 27 broadcasts (3 multicasts)
     0 runts, 0 giants, 0 throttles 
     3 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 3 multicast, 0 pause input
     0 input packets with dribble condition detected
     76470570 packets output, 24742468145 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet8/0/9 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.78bc (bia bc26.c723.78bc)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:08:42, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 53000 bits/sec, 10 packets/sec
     32256159 packets input, 2221413070 bytes, 0 no buffer
     Received 12 broadcasts (3 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 3 multicast, 0 pause input
     0 input packets with dribble condition detected
     84660059 packets output, 36111648474 bytes, 0 underruns
               0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet8/0/10 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.78bd (bia bc26.c723.78bd)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:57, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 40000 bits/sec, 9 packets/sec
     23032289 packets input, 1590568823 bytes, 0 no buffer
     Received 22 broadcasts (6 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 6 multicast, 0 pause input
     0 input packets with dribble condition detected
     75783755 packets output, 24951866532 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet8/0/11 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.78be (bia bc26.c723.78be)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:05:53, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 7000 bits/sec, 9 packets/sec
     7952433 packets input, 869222765 bytes, 0 no buffer
     Received 270707 broadcasts (270609 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 270609 multicast, 0 pause input
     0 input packets with dribble condition detected
     60698720 packets output, 7759124511 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
               0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet8/0/12 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.78bf (bia bc26.c723.78bf)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:01:18, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 6000 bits/sec, 9 packets/sec
     34927725 packets input, 2733837740 bytes, 0 no buffer
     Received 270705 broadcasts (270622 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 270622 multicast, 0 pause input
     0 input packets with dribble condition detected
     86632318 packets output, 31315594392 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet8/0/13 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.78c0 (bia bc26.c723.78c0)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:08:20, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 6000 bits/sec, 9 packets/sec
     100872020 packets input, 7008760799 bytes, 0 no buffer
     Received 60 broadcasts (15 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 15 multicast, 0 pause input
     0 input packets with dribble condition detected
     151160285 packets output, 102245869354 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet8/0/14 is down, line protocol is down (notconnect) 
            Hardware is Gigabit Ethernet, address is bc26.c723.78c1 (bia bc26.c723.78c1)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 5w0d, output 5w0d, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     100 packets input, 8424 bytes, 0 no buffer
     Received 99 broadcasts (94 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 94 multicast, 0 pause input
     0 input packets with dribble condition detected
     45 packets output, 5273 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     51 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet8/0/15 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.78c2 (bia bc26.c723.78c2)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:03:05, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/1 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 15000 bits/sec, 29 packets/sec
  5 minute output rate 436000 bits/sec, 41 packets/sec
     88666733 packets input, 6604581023 bytes, 0 no buffer
     Received 270783 broadcasts (270627 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 270627 multicast, 0 pause input
     0 input packets with dribble condition detected
     141081347 packets output, 92933255890 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet8/0/16 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.78c3 (bia bc26.c723.78c3)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
            Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:01:18, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 12000 bits/sec, 14 packets/sec
     369247 packets input, 56099645 bytes, 0 no buffer
     Received 159063 broadcasts (146948 multicasts)
     0 runts, 0 giants, 0 throttles 
     1 input errors, 1 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 146948 multicast, 0 pause input
     0 input packets with dribble condition detected
     90953505 packets output, 10633172992 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet8/0/17 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is bc26.c723.78c4 (bia bc26.c723.78c4)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 5w0d, output 5w0d, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     1939 packets input, 292131 bytes, 0 no buffer
     Received 1939 broadcasts (1254 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 1254 multicast, 0 pause input
     0 input packets with dribble condition detected
     818 packets output, 105029 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     201 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet8/0/18 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.78c5 (bia bc26.c723.78c5)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
            input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:01:03, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 6000 bits/sec, 9 packets/sec
     94450536 packets input, 7070489973 bytes, 0 no buffer
     Received 270836 broadcasts (270640 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 270640 multicast, 0 pause input
     0 input packets with dribble condition detected
     143284321 packets output, 88194693266 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet8/0/19 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.78c6 (bia bc26.c723.78c6)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:01:39, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 39572
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 31000 bits/sec, 6 packets/sec
  5 minute output rate 17000 bits/sec, 18 packets/sec
     11687766 packets input, 9854076785 bytes, 0 no buffer
     Received 480630 broadcasts (430835 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 430835 multicast, 0 pause input
     0 input packets with dribble condition detected
     101713142 packets output, 14508971376 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     31679 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet8/0/20 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.78c7 (bia bc26.c723.78c7)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:06:24, output 00:00:00, output hang never
            Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 6000 bits/sec, 9 packets/sec
     17349799 packets input, 1183361113 bytes, 0 no buffer
     Received 11 broadcasts (3 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 3 multicast, 0 pause input
     0 input packets with dribble condition detected
     70428724 packets output, 22557166564 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet8/0/21 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.78c8 (bia bc26.c723.78c8)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:08:52, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 6000 bits/sec, 9 packets/sec
     23262779 packets input, 1602089828 bytes, 0 no buffer
     Received 81 broadcasts (21 multicasts)
     0 runts, 0 giants, 0 throttles 
     4 input errors, 4 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 21 multicast, 0 pause input
     0 input packets with dribble condition detected
     76362620 packets output, 27289127688 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet8/0/22 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.78c9 (bia bc26.c723.78c9)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:02:13, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
            Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 7000 bits/sec, 9 packets/sec
     13834572 packets input, 949108732 bytes, 0 no buffer
     Received 11 broadcasts (3 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 3 multicast, 0 pause input
     0 input packets with dribble condition detected
     67239734 packets output, 18131995265 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet8/0/23 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.78ca (bia bc26.c723.78ca)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:02:05, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 789615909
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 12000 bits/sec, 14 packets/sec
     191603429 packets input, 84922651144 bytes, 0 no buffer
     Received 413590 broadcasts (387345 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 387345 multicast, 0 pause input
     0 input packets with dribble condition detected
     334677637 packets output, 157893337925 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     13463 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet8/0/24 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.78cb (bia bc26.c723.78cb)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:03, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 103496
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 14000 bits/sec, 15 packets/sec
               3929717 packets input, 609680583 bytes, 0 no buffer
     Received 368927 broadcasts (300453 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 300453 multicast, 0 pause input
     0 input packets with dribble condition detected
     98805996 packets output, 13361531287 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     46316 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet8/0/25 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.78cc (bia bc26.c723.78cc)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:01:42, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 5000 bits/sec, 8 packets/sec
     20409513 packets input, 1766022540 bytes, 0 no buffer
     Received 270709 broadcasts (270605 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 270605 multicast, 0 pause input
     0 input packets with dribble condition detected
     71765603 packets output, 16954829155 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet8/0/26 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.78cd (bia bc26.c723.78cd)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:03, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 12000 bits/sec, 13 packets/sec
     11403390 packets input, 9868849626 bytes, 0 no buffer
     Received 554075 broadcasts (501639 multicasts)
     3210 runts, 0 giants, 0 throttles 
               210850 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 501639 multicast, 0 pause input
     0 input packets with dribble condition detected
     101598540 packets output, 14149893747 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     36070 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet8/0/27 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.78ce (bia bc26.c723.78ce)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:04:36, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 44000 bits/sec, 8 packets/sec
     41459703 packets input, 2909565136 bytes, 0 no buffer
     Received 11 broadcasts (3 multicasts)
     0 runts, 0 giants, 0 throttles 
     1 input errors, 1 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 3 multicast, 0 pause input
     0 input packets with dribble condition detected
     92190112 packets output, 37880178271 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet8/0/28 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.78cf (bia bc26.c723.78cf)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:05, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 1050213336
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 28000 bits/sec, 34 packets/sec
  5 minute output rate 132000 bits/sec, 43 packets/sec
     89056001 packets input, 20572481008 bytes, 0 no buffer
     Received 561765 broadcasts (416571 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 416571 multicast, 0 pause input
     0 input packets with dribble condition detected
               185445218 packets output, 64957100150 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     17938 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet8/0/29 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is bc26.c723.78d0 (bia bc26.c723.78d0)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 13w2d
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
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet8/0/30 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.78d1 (bia bc26.c723.78d1)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:08:22, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 5000 bits/sec, 8 packets/sec
     20101000 packets input, 1385739911 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     73217635 packets output, 23817626001 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
               0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet8/0/31 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.78d2 (bia bc26.c723.78d2)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:35, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 712640
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 11000 bits/sec, 12 packets/sec
     4711739 packets input, 1396139011 bytes, 0 no buffer
     Received 514925 broadcasts (438012 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 438012 multicast, 0 pause input
     0 input packets with dribble condition detected
     99029714 packets output, 13388012426 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     47785 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet8/0/32 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.78d3 (bia bc26.c723.78d3)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:09:37, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 997516381
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 11000 bits/sec, 12 packets/sec
     156947887 packets input, 83905964936 bytes, 0 no buffer
     Received 350773 broadcasts (333680 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 333680 multicast, 0 pause input
     0 input packets with dribble condition detected
     270890447 packets output, 115639182517 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     6039 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
          GigabitEthernet8/0/33 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.78d4 (bia bc26.c723.78d4)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:06:17, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 189852090
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 12000 bits/sec, 13 packets/sec
     19479150 packets input, 9843714978 bytes, 0 no buffer
     Received 304738 broadcasts (301244 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 301244 multicast, 0 pause input
     0 input packets with dribble condition detected
     119815160 packets output, 29847888855 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     599 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet8/0/34 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.78d5 (bia bc26.c723.78d5)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:03:49, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/1 (size/max/drops/flushes); Total output drops: 392474987
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 11000 bits/sec, 13 packets/sec
     30012993 packets input, 10797618476 bytes, 0 no buffer
     Received 312956 broadcasts (305394 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 305394 multicast, 0 pause input
     0 input packets with dribble condition detected
     132291196 packets output, 34826131182 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     2740 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet8/0/35 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.78d6 (bia bc26.c723.78d6)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
               reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:33, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 90581358
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 12000 bits/sec, 13 packets/sec
     33230046 packets input, 33118341260 bytes, 0 no buffer
     Received 330581 broadcasts (311721 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 311721 multicast, 0 pause input
     0 input packets with dribble condition detected
     121233697 packets output, 20358765754 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     2175 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet8/0/36 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.78d7 (bia bc26.c723.78d7)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:08, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 345694548
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 14000 bits/sec, 4 packets/sec
  5 minute output rate 49000 bits/sec, 19 packets/sec
     83097050 packets input, 20583324050 bytes, 0 no buffer
     Received 648352 broadcasts (582456 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 582456 multicast, 0 pause input
     0 input packets with dribble condition detected
     183393654 packets output, 65317306370 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     21294 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet8/0/37 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is bc26.c723.78d8 (bia bc26.c723.78d8)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
            Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 13w2d
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
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet8/0/38 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.78d9 (bia bc26.c723.78d9)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:51, output 00:00:01, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 11000 bits/sec, 13 packets/sec
     381367 packets input, 56276073 bytes, 0 no buffer
     Received 158173 broadcasts (146131 multicasts)
     0 runts, 0 giants, 0 throttles 
     1 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 146131 multicast, 0 pause input
     0 input packets with dribble condition detected
     91853119 packets output, 10738991409 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet8/0/39 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is bc26.c723.78da (bia bc26.c723.78da)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
            Last input never, output never, output hang never
  Last clearing of "" counters 13w2d
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
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet8/0/40 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is bc26.c723.78db (bia bc26.c723.78db)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 13w2d
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
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet8/0/41 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is bc26.c723.78dc (bia bc26.c723.78dc)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 13w2d
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
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet8/0/42 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is bc26.c723.78dd (bia bc26.c723.78dd)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 13w2d
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
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet8/0/43 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is bc26.c723.78de (bia bc26.c723.78de)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 13w2d
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
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet8/0/44 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is bc26.c723.78df (bia bc26.c723.78df)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 13w2d
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
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet8/0/45 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.78e0 (bia bc26.c723.78e0)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:53, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 57000 bits/sec, 12 packets/sec
     29513696 packets input, 2453366861 bytes, 0 no buffer
     Received 270691 broadcasts (270607 multicasts)
               0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 270607 multicast, 0 pause input
     0 input packets with dribble condition detected
     80785639 packets output, 26198423094 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet8/0/46 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.78e1 (bia bc26.c723.78e1)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:11, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 12000 bits/sec, 13 packets/sec
     1269945 packets input, 86480906 bytes, 0 no buffer
     Received 352486 broadcasts (2 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 2 multicast, 0 pause input
     0 input packets with dribble condition detected
     95335146 packets output, 11140863660 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet8/0/47 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is bc26.c723.78e2 (bia bc26.c723.78e2)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "" counters 13w2d
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
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet8/0/48 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is bc26.c723.78e3 (bia bc26.c723.78e3)
  Description: #UPS
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:27, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 1872013227
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 2000 bits/sec, 3 packets/sec
     661084 packets input, 63673485 bytes, 0 no buffer
     Received 15024 broadcasts (0 multicasts)
     3 runts, 0 giants, 0 throttles 
     226 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     48874743 packets output, 5227890308 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
Port-channel30 is up, line protocol is up (connected) 
  Hardware is EtherChannel, address is a093.51d2.5c6d (bia a093.51d2.5c6d)
  Description: key:Uplink to dist nodes
  MTU 1500 bytes, BW 20000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 10Gb/s, link type is auto, media type is 
  input flow-control is off, output flow-control is unsupported 
  Members in this channel: Te5/0/1 Te5/0/2 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output 00:00:00, output hang never
  Last clearing of "" counters 13w2d
  Input queue: 0/375/14518/1121 (size/max/drops/flushes); Total output drops: 2292796
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 15045000 bits/sec, 2990 packets/sec
  5 minute output rate 1742000 bits/sec, 868 packets/sec
     17374458232 packets input, 11245419427503 bytes, 0 no buffer
     Received 7625396733 broadcasts (2539741297 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 2539741297 multicast, 0 pause input
               0 input packets with dribble condition detected
     6875169723 packets output, 1971808734215 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     280191351 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out""",
 'show inventory':"""NAME: "Chassis", DESCR: "Cisco Catalyst 9400 Series 10 Slot Chassis"
PID: C9410R            , VID: V01  , SN: FXS2226Q030

NAME: "Slot 1 - Linecard", DESCR: "Cisco Catalyst 9400 Series 48-Port UPOE 10/100/1000 (RJ-45)"
PID: C9400-LC-48U      , VID: V02  , SN: JAE22280N09

NAME: "Slot 4 - Linecard", DESCR: "Cisco Catalyst 9400 Series 24-Port 10 Gigabit Ethernet (SFP+)"
PID: C9400-LC-24XS     , VID: V01  , SN: JAE222801VF

NAME: "TenGigabitEthernet4/0/1", DESCR: "SFP+ 10GBASE-SR"
PID: SFP-10G-SR          , VID: A    , SN: FNS15170VND     

NAME: "TenGigabitEthernet4/0/2", DESCR: "SFP+ 10GBASE-SR"
PID: SFP-10G-SR          , VID: A    , SN: FNS15170U5T     

NAME: "TenGigabitEthernet4/0/3", DESCR: "SFP+ 10GBASE-SR"
PID: SFP-10G-SR          , VID: A    , SN: FNS15170U5V     

NAME: "TenGigabitEthernet4/0/4", DESCR: "SFP+ 10GBASE-SR"
PID: SFP-10G-SR          , VID: A    , SN: FNS15170VN3     

NAME: "TenGigabitEthernet4/0/5", DESCR: "SFP+ 10GBASE-SR"
PID: SFP-10G-SR          , VID: A    , SN: FNS15170U5X     

NAME: "TenGigabitEthernet4/0/6", DESCR: "SFP+ 10GBASE-SR"
PID: SFP-10G-SR          , VID: A    , SN: FNS15170VNC     

NAME: "TenGigabitEthernet4/0/7", DESCR: "SFP+ 10GBASE-SR"
PID: SFP-10G-SR          , VID: A    , SN: FNS150901RL     

NAME: "TenGigabitEthernet4/0/8", DESCR: "SFP+ 10GBASE-SR"
PID: SFP-10G-SR          , VID: A    , SN: FNS15090BBC     

NAME: "TenGigabitEthernet4/0/9", DESCR: "SFP+ 10GBASE-SR"
PID: SFP-10G-SR          , VID: 1.0  , SN: USXSR68099      

NAME: "TenGigabitEthernet4/0/10", DESCR: "SFP+ 10GBASE-SR"
PID: SFP-10G-SR          , VID: A    , SN: FNS15090BAS     

NAME: "TenGigabitEthernet4/0/11", DESCR: "SFP+ 10GBASE-SR"
PID: SFP-10G-SR          , VID: A    , SN: FNS15170U5D     

NAME: "TenGigabitEthernet4/0/12", DESCR: "SFP+ 10GBASE-SR"
PID: SFP-10G-SR          , VID: A    , SN: FNS15170U4T     

NAME: "TenGigabitEthernet4/0/13", DESCR: "SFP+ 10GBASE-SR"
PID: SFP-10G-SR          , VID: A    , SN: FNS15170WL1     

NAME: "TenGigabitEthernet4/0/14", DESCR: "SFP+ 10GBASE-SR"
PID: SFP-10G-SR          , VID: A    , SN: FNS15170U4M     

NAME: "TenGigabitEthernet4/0/15", DESCR: "SFP+ 10GBASE-SR"
PID: SFP-10G-SR          , VID: A    , SN: FNS15170WN3     

NAME: "TenGigabitEthernet4/0/16", DESCR: "SFP+ 10GBASE-SR"
PID: SFP-10G-SR          , VID: A    , SN: FNS15170U5B     

NAME: "TenGigabitEthernet4/0/17", DESCR: "SFP+ 10GBASE-SR"
PID: SFP-10G-SR          , VID: A    , SN: FNS15170U4X     
          
NAME: "TenGigabitEthernet4/0/18", DESCR: "SFP+ 10GBASE-SR"
PID: SFP-10G-SR          , VID: 1.0  , SN: USXSR81795      

NAME: "TenGigabitEthernet4/0/19", DESCR: "SFP+ 10GBASE-SR"
PID: SFP-10G-SR          , VID: G2.5 , SN: AGD163246SF     

NAME: "TenGigabitEthernet4/0/20", DESCR: "SFP+ 10GBASE-LR"
PID: SFP-10G-LR          , VID: 1.0  , SN: USX1000000235087

NAME: "TenGigabitEthernet4/0/22", DESCR: "SFP+ 10GBASE-SR"
PID: SFP-10G-SR          , VID: A    , SN: ECL133106C8     

NAME: "TenGigabitEthernet4/0/23", DESCR: "GE SX"
PID: FTLF8519P2BCL-CS  , VID: B    , SN: FNS13010BXX     

NAME: "TenGigabitEthernet4/0/24", DESCR: "GE SX"
PID: FTLF8519P2BCL-C4  , VID: A    , SN: FNS133607NP     

NAME: "Slot 7 - Linecard", DESCR: "Cisco Catalyst 9400 Series 48-Port UPOE 10/100/1000 (RJ-45)"
PID: C9400-LC-48U      , VID: V02  , SN: JAE222809MC

NAME: "Slot 8 - Linecard", DESCR: "Cisco Catalyst 9400 Series 48-Port UPOE 10/100/1000 (RJ-45)"
PID: C9400-LC-48U      , VID: V02  , SN: JAE222805VD

NAME: "Slot 5 - Supervisor", DESCR: "Cisco Catalyst 9400 Series Supervisor 1 Module"
PID: C9400-SUP-1       , VID: V02  , SN: JAE22270XUG

NAME: "TenGigabitEthernet5/0/1", DESCR: "SFP+ 10GBASE-SR"
PID: SFP-10G-SR          , VID: A    , SN: FNS15170WLT     

NAME: "TenGigabitEthernet5/0/2", DESCR: "SFP+ 10GBASE-LR"
PID: SFP-10G-LR          , VID: A    , SN: FNS16421LGM     

NAME: "TenGigabitEthernet5/0/3", DESCR: "SFP+ 10GBASE-LR"
PID: SFP-10G-LR          , VID: A    , SN: FNS16111GEA     

NAME: "TenGigabitEthernet5/0/4", DESCR: "SFP+ 10GBASE-LR"
PID: SFP-10G-LR          , VID: 0004 , SN: ONT141701XK     

NAME: "TenGigabitEthernet5/0/5", DESCR: "SFP+ 10GBASE-LR"
PID: SFP-10G-LR          , VID: 1.0  , SN: USX1000000131044

NAME: "TenGigabitEthernet5/0/6", DESCR: "SFP+ 10GBASE-LR"
PID: SFP-10G-LR          , VID: 1.0  , SN: USX1000000131045

NAME: "Power Supply Module 1", DESCR: "Cisco Catalyst 9400 Series 3200W AC Power Supply"
PID: C9400-PWR-3200AC  , VID: V01  , SN: DTM2222025C

NAME: "Power Supply Module 2", DESCR: "Cisco Catalyst 9400 Series 3200W AC Power Supply"
PID: C9400-PWR-3200AC  , VID: V01  , SN: DTM222102J6

NAME: "Fan Tray", DESCR: "Cisco Catalyst 9400 Series 10 Slot Chassis Fan Tray"
PID: C9410-FAN         , VID: V01  , SN: FXS2225Q0RQ

""",
 'show interface counters':"""Port            InOctets    InUcastPkts    InMcastPkts    InBcastPkts 
Gi1/0/1        400056511        3087219              0            663 
Gi1/0/2        377978227        2955641              0            691 
Gi1/0/3                0              0              0              0 
Gi1/0/4                0              0              0              0 
Gi1/0/5                0              0              0              0 
Gi1/0/6                0              0              0              0 
Gi1/0/7                0              0              0              0 
Gi1/0/8       2119839674       12003978            135            557 
Gi1/0/9                0              0              0              0 
Gi1/0/10       157370279        2385326              0             14 
Gi1/0/11        87781875         576018              0              2 
Gi1/0/12       104233108         708058              0              1 
Gi1/0/13               0              0              0              0 
Gi1/0/14       214268670        3039920              0           8522 
Gi1/0/15       530489473        3264960          30106          74548 
Gi1/0/16      1700770068        6657304             53          38588 
Gi1/0/17     10344549576       37903638             12        1028319 
Gi1/0/18      4194768975        5230206         337793              0 
Gi1/0/19               0              0              0              0 
Gi1/0/20        40909107         269521          26202              0 
Gi1/0/21               0              0              0              0 
Gi1/0/22       510639494              0         194887         836441 
Gi1/0/23           13414              1             48             86 
Gi1/0/24      5229707716       26052373         602274         136650 
Gi1/0/25       237580574        2149362         134568           7322 
Gi1/0/26       185174088        1222226         300536         554545 
Gi1/0/27       146442663        1353990              0         279310 
Gi1/0/28       291383323        2490727              0         311118 
Gi1/0/29       161886325        1487232              0         281929 
Gi1/0/30       191929704        1454336         581715         280339 
Gi1/0/31       171479365        1594349         229380          15344 
Gi1/0/32       155605940        1511015         131627          10447 
Gi1/0/33        81200633         548970         146198          21400 
Gi1/0/34       168379203        1552364              0         288311 
Gi1/0/35        36802585         355949         135380          21899 
Gi1/0/36       159382314        1469293              0         283259 
Gi1/0/37       983104609        5339960          72486           2269 
Gi1/0/38               0              0              0              0 
Gi1/0/39     17617628869       53355197         893083           1537 
Gi1/0/40     73436682931      275513784         892944           1539 
Gi1/0/41    184420201263      585678720         865824           1542 
Gi1/0/42    305949141816      968628229         865862           1516 
Gi1/0/43    167168036281      458671916         865814           1534 
Gi1/0/44     35778450361      126451134         893290           1514 
Gi1/0/45    100157072834      298888329         890265           1529 
Gi1/0/46    122516463741      373495201         890305           1540 
Gi1/0/47      2519159642       15231703              0             31 
Gi1/0/48     41498220771      180234111         892782           1531 
Te4/0/1       2872159179        3963233       18389785         872733 
Te4/0/2      10091087402       25527908       56361827        1338003 
Te4/0/3       2489103265        9575592        9465786         138611 
Te4/0/4       5047218327       22372219       17606746         278231 
Te4/0/5       1317893296         891226       12864459         213632 
Te4/0/6        821470407         251537        8797606           4736 
Te4/0/7       5768641173       17233641       28864320        1023726 
Te4/0/8       3352983605       14993403       17011771         164542 
Te4/0/9       9472164787       26032004       43511304         659501 
          
Port            InOctets    InUcastPkts    InMcastPkts    InBcastPkts 
Te4/0/10      5041437440         990215       55903272        1113225 
Te4/0/11      1490312458        1375406       13426915          47601 
Te4/0/12               0              0              0              0 
Te4/0/13      4156390298       17197974       19964527         213410 
Te4/0/14      4088449686       18535004       17605532         268043 
Te4/0/15      7347348446        9375393       46684746         369501 
Te4/0/16      4378503822       20146550       12966544         314667 
Te4/0/17      3649419707       11070042       21660709         280664 
Te4/0/18      4570908976       14282233       33022886        1337692 
Te4/0/19      5176764728       29055346        9502521         451142 
Te4/0/20      5064695099        5514615       30706675        2723347 
Te4/0/21               0              0              0              0 
Te4/0/22      3648582708       18685540        9333373         287660 
Te4/0/23      6870664057        5003262       25133611        1092410 
Te4/0/24       329346305         813318        1234633            330 
Te5/0/1    4043966567943     4282795453      866874544      477659186 
Te5/0/2    7201452859560     5466266046     5967834049      313028954 
Te5/0/3       5530130046       38551072       13702798         852628 
Te5/0/4       3237177642       10203982       25183101         226612 
Te5/0/5       3603500775       15471326        9496983           2174 
Te5/0/6        261197081         243920        2845821              0 
Te5/0/7                0              0              0              0 
Te5/0/8                0              0              0              0 
Fo5/0/9                0              0              0              0 
Fo5/0/10               0              0              0              0 
Gi7/0/1        697232228        9798416              6             34 
Gi7/0/2       1545054884       11486935             23            235 
Gi7/0/3      10519652118       11290249         443566          45247 
Gi7/0/4       6273558499       82821830         270609             92 
Gi7/0/5      50652607294      162859023         771624           1523 
Gi7/0/6      10902902002       11565202         350520          38938 
Gi7/0/7                0              0              0              0 
Gi7/0/8       1250445146       18364877              0              9 
Gi7/0/9                0              0              0              0 
Gi7/0/10       873277408        6452023         314423          71038 
Gi7/0/11      1871769501       27198335             12             41 
Gi7/0/12               0              0              0              0 
Gi7/0/13      2026188397       10180967              0            979 
Gi7/0/14        55177883         204945         143320          12605 
Gi7/0/15               0              0              0              0 
Gi7/0/16      3088859317       16282373          57403         520660 
Gi7/0/17       717650089        1743374         270608             24 
Gi7/0/18     22148242231       75809167         442844          26185 
Gi7/0/19        83843124         987074              3             18 
Gi7/0/20      2114618339       30583230             15             32 
Gi7/0/21     17847860942       82314858         409649          23635 
Gi7/0/22     17643398189       62591603         375778          26629 
Gi7/0/23        55467272         198294         146346          12861 
Gi7/0/24      2715985657       39479407              9           1259 
Gi7/0/25      2978491132        2812891           2350           6209 
Gi7/0/26      6342024360       81759797         270632            149 
Gi7/0/27      2356880158       28834802         270608             90 
Gi7/0/28    181949972676      287956268         711294          30584 
Gi7/0/29     32159509586      163835789         724141          22786 
Gi7/0/30      1837104707       26523081             28             66 
Gi7/0/31               0              0              0              0 
Gi7/0/32      1196314428       15481656              0           4146 
Gi7/0/33       333143840         510116         437510         602426 
Gi7/0/34               0              0              0              0 
          
Port            InOctets    InUcastPkts    InMcastPkts    InBcastPkts 
Gi7/0/35               0              0              0              0 
Gi7/0/36               0              0              0              0 
Gi7/0/37     24758581079      129679980         428788          41063 
Gi7/0/38       436628040        6180018              9             26 
Gi7/0/39        85219742        1066494              3             18 
Gi7/0/40        85972539        1084247              0              9 
Gi7/0/41        85335994        1074167              0              9 
Gi7/0/42     32557289359       78521437         400738          14764 
Gi7/0/43     41822919764      115511702         755382          43793 
Gi7/0/44      2018628947       24908069         270609            121 
Gi7/0/45      7281862397       96902402         270619             82 
Gi7/0/46      1816053877       26455471              9            119 
Gi7/0/47      2001797394       28896508              6             17 
Gi7/0/48      4187420113       52160152         270627            218 
Gi8/0/1      20426016599       74753437         647649          28803 
Gi8/0/2        132412282         702228         270608              7 
Gi8/0/3       1697211906        4380389         272883          22290 
Gi8/0/4        899031375        6453452         406016          11552 
Gi8/0/5      10127041669      102262362         270621             84 
Gi8/0/6                0              0              0              0 
Gi8/0/7       2039026537       29456653             10             42 
Gi8/0/8       1541647239       22123197              3             24 
Gi8/0/9       2221413070       32256147              3              9 
Gi8/0/10      1590568823       23032267              6             16 
Gi8/0/11       869222765        7681726         270609             98 
Gi8/0/12      2733837740       34657020         270622             83 
Gi8/0/13      7008760799      100871960             15             45 
Gi8/0/14            8424              1             94              5 
Gi8/0/15      6604581023       88395950         270627            156 
Gi8/0/16        56099645         210184         146948          12115 
Gi8/0/17          292131              0           1254            685 
Gi8/0/18      7070489973       94179700         270640            196 
Gi8/0/19      9854076785       11207136         430835          49795 
Gi8/0/20      1183361113       17349788              3              8 
Gi8/0/21      1602089828       23262698             21             60 
Gi8/0/22       949108732       13834561              3              8 
Gi8/0/23     84922651144      191189839         387345          26245 
Gi8/0/24       609680583        3560790         300453          68474 
Gi8/0/25      1766022540       20138804         270605            104 
Gi8/0/26      9868849626       10849315         501639          52436 
Gi8/0/27      2909565136       41459692              3              8 
Gi8/0/28     20572481008       88494236         416571         145194 
Gi8/0/29               0              0              0              0 
Gi8/0/30      1385739911       20101000              0              0 
Gi8/0/31      1396139011        4196814         438012          76913 
Gi8/0/32     83905964936      156597114         333680          17093 
Gi8/0/33      9843715378       19174413         301245           3494 
Gi8/0/34     10797618476       29700037         305394           7562 
Gi8/0/35     33118341260       32899465         311721          18860 
Gi8/0/36     20583335096       82448754         582456          65896 
Gi8/0/37               0              0              0              0 
Gi8/0/38        56276211         223194         146132          12042 
Gi8/0/39               0              0              0              0 
Gi8/0/40               0              0              0              0 
Gi8/0/41               0              0              0              0 
Gi8/0/42               0              0              0              0 
Gi8/0/43               0              0              0              0 
Gi8/0/44               0              0              0              0 
Gi8/0/45      2453366861       29243005         270607             84 
          
Port            InOctets    InUcastPkts    InMcastPkts    InBcastPkts 
Gi8/0/46        86480906         917459              2         352484 
Gi8/0/47               0              0              0              0 
Gi8/0/48        63673485         646060              0          15024 
Po30      11245419427503     9749061499     6834708593      790688140 

Port           OutOctets   OutUcastPkts   OutMcastPkts   OutBcastPkts 
Gi1/0/1       3430980672        4055510       28214118         597081 
Gi1/0/2       3418845282        3938755       28214698         596766 
Gi1/0/3                0              0              0              0 
Gi1/0/4                0              0              0              0 
Gi1/0/5                0              0              0              0 
Gi1/0/6                0              0              0              0 
Gi1/0/7                0              0              0              0 
Gi1/0/8      55501976607        9982646       32683017      164613959 
Gi1/0/9                0              0              0              0 
Gi1/0/10      1485573260        3284418       12295851          91777 
Gi1/0/11      2585863468        1440036       23824320         777104 
Gi1/0/12      2611895944        1584085       23824286         772390 
Gi1/0/13               0              0              0              0 
Gi1/0/14       677960548        3192933        2225644        3138808 
Gi1/0/15      4180864033        4154974       16962127        4649794 
Gi1/0/16      5153583230        6475728       32195037        4996358 
Gi1/0/17      9469477849       36601098       43449829        9102411 
Gi1/0/18      1526026187        3594083       12525862         370051 
Gi1/0/19               0              0              0              0 
Gi1/0/20      3737345083       10378911       25763788         397657 
Gi1/0/21               0              0              0              0 
Gi1/0/22      3803644381         876620       26726184       14721568 
Gi1/0/23           47088             58            251             24 
Gi1/0/24   1528413868089       27206784     5385160312        5764645 
Gi1/0/25     33865041797       30055757       53873618      352965900 
Gi1/0/26     35986562030       44679930       54074619      354318721 
Gi1/0/27     36062854792       44628742       54056033      354595161 
Gi1/0/28     36732750580       46129853       54055943      354560546 
Gi1/0/29     36610297174       45014158       54056026      354592535 
Gi1/0/30     36659456705       45086025       54120612      354594146 
Gi1/0/31     35829442195       44471149       53992820      354859139 
Gi1/0/32     33821630725       29542514       53873576      352961581 
Gi1/0/33     31285286075       26658258       50706500      325663274 
Gi1/0/34     34657467681       30231131       53873098      352678077 
Gi1/0/35     33687795712       28233349       53870097      352877197 
Gi1/0/36     36009331406       44688944       54056042      354590809 
Gi1/0/37      6732164841       16037269       36999451        3969197 
Gi1/0/38               0              0              0              0 
Gi1/0/39   1608902127829       91913527     5396935164        6110967 
Gi1/0/40   2096940899033      497657683     5396924871        6110974 
Gi1/0/41   2390346501594      885521509     5396952268        6110969 
Gi1/0/42   3380922106279     1703225109     5396958740        6110981 
Gi1/0/43   2103672137821      611937812     5396956102        6110983 
Gi1/0/44   1733559117124      212894462     5396925444        6110981 
Gi1/0/45   2163501581047      587799853     5396874413        6110982 
Gi1/0/46   2519401506374      849702738     5396872144        6110954 
Gi1/0/47      3209399191       16262159       12721226         201554 
Gi1/0/48   2172259204875      516910762     5396904565        6110974 
Te4/0/1     294448773326      132640152     1382893227      793179012 
Te4/0/2     293199821571      143363948     1369112318      793538918 
Te4/0/3     296350948875      144585733     1391599710      793236835 
Te4/0/4     296938424315      148233919     1383880794      793188986 
Te4/0/5     294523648276      137381588     1392356388      793237243 
          
Port           OutOctets   OutUcastPkts   OutMcastPkts   OutBcastPkts 
Te4/0/6     294561595617      133848153     1392862903      793280989 
Te4/0/7     295584579423      138749231     1384606540      793273107 
Te4/0/8     296075405159      148228521     1384506841      793275870 
Te4/0/9     291412614995      142597039     1358099975      793074278 
Te4/0/10     85052029507      115779055      346523574      396526015 
Te4/0/11     77509079874       60607866      310325841      400980864 
Te4/0/12               0              0              0              0 
Te4/0/13    295581209890      148070420     1381508032      793418313 
Te4/0/14    295493083771      148393556     1383887110      793344611 
Te4/0/15     76772491899       69233715      308935642      393078357 
Te4/0/16    295766486085      140634736     1392619172      793339575 
Te4/0/17    295735020817      149892786     1383497239      793542856 
Te4/0/18     91327349444      137068827      381554435      397895064 
Te4/0/19    297103355009      154440479     1391999435      793557001 
Te4/0/20    155730743763       71311446      714584488      431116710 
Te4/0/21               0              0              0              0 
Te4/0/22    297965745179      165040959     1392140880      793554748 
Te4/0/23     91857035695       77027741      418892037      405638674 
Te4/0/24     87245965813       73055475      375497011      400659015 
Te5/0/1    1357734632070     4493950882       64488789       32179478 
Te5/0/2     614074102145     2265824941       18247893         477740 
Te5/0/3     297881763843      159465786     1391996073      793557409 
Te5/0/4     296884142374      161827132     1380436836      793866382 
Te5/0/5     295457343618      135864636     1391989674      793573581 
Te5/0/6      76920487935       41921593      314043102      235440470 
Te5/0/7                0              0              0              0 
Te5/0/8                0              0              0              0 
Fo5/0/9                0              0              0              0 
Fo5/0/10               0              0              0              0 
Gi7/0/1       8220397249       37358771       23910388         308795 
Gi7/0/2       9096951299       33480446       23880084         304464 
Gi7/0/3      15300531013       42734352       43328553       17725008 
Gi7/0/4      69330719681      106457099       23910343         357313 
Gi7/0/5     415106010058      365232005       43340247       17774342 
Gi7/0/6      14542002911       41041608       43325540       17741341 
Gi7/0/7                0              0              0              0 
Gi7/0/8      15837087580       41437989       23910327         308800 
Gi7/0/9                0              0              0              0 
Gi7/0/10     16638945791       42378454       43389545       17699344 
Gi7/0/11     30991085585       56192797       23910367         306783 
Gi7/0/12               0              0              0              0 
Gi7/0/13     16053746539       45175725       43435057       17816027 
Gi7/0/14     10299583892       31641830       40041576       16424958 
Gi7/0/15               0              0              0              0 
Gi7/0/16     17135031102       61487726       43369398       17247757 
Gi7/0/17     11665281212       35952185       43434912       17823122 
Gi7/0/18     67814646934      124402990       43270217       17798177 
Gi7/0/19      4613242818       25785977       23910356         308808 
Gi7/0/20     32885749083       58360792       23910358         310170 
Gi7/0/21     85415618954      126381646       43303661       17817259 
Gi7/0/22     40454038779       99710944       43341533       17797697 
Gi7/0/23     10445137602       32096512       40612714       16608157 
Gi7/0/24     45847074001       48871376       27375940        3189150 
Gi7/0/25     11372373784       36330405       43432628       17804086 
Gi7/0/26     80912067758      108467765       23910342         358076 
Gi7/0/27     26672224526       56612216       23910411         361081 
Gi7/0/28    258447435067      317774637       43002432       17793253 
Gi7/0/29    117606877314      219847472       43265350       17748247 
Gi7/0/30     29064434272       53689124       23103150         302993 
          
Port           OutOctets   OutUcastPkts   OutMcastPkts   OutBcastPkts 
Gi7/0/31               0              0              0              0 
Gi7/0/32     12152912852       49494018       43433980       17807183 
Gi7/0/33      1816323564        1304160       13437466        3984786 
Gi7/0/34               0              0              0              0 
Gi7/0/35               0              0              0              0 
Gi7/0/36               0              0              0              0 
Gi7/0/37    106005624257      178961347       43284819       17783769 
Gi7/0/38      8186907106       34187677       23910345         304751 
Gi7/0/39      5290497921       25946452       23910349         308583 
Gi7/0/40      5287586806       25977812       23910329         308601 
Gi7/0/41      5289207065       25960556       23910380         309914 
Gi7/0/42     97704420959      146011645       43307637       17810586 
Gi7/0/43     89486684695      152796123       43197402       17702860 
Gi7/0/44     24288830400       53464865       23910400         368475 
Gi7/0/45     98586710303      126376962       23910310         366788 
Gi7/0/46     28742722743       56572736       23910327         302761 
Gi7/0/47     30403940167       56872923       23910360         315844 
Gi7/0/48     41965688103       76169339       23910369         363632 
Gi8/0/1      67178101324      126617368       40360395       16410616 
Gi8/0/2       4608197219       25723989       23910349         316684 
Gi8/0/3      13397619954       37941276       43433452       17747432 
Gi8/0/4      16650358602       42389583       43435003       17760071 
Gi8/0/5     112448007156      134209703       23910354         359962 
Gi8/0/6                0              0              0              0 
Gi8/0/7      32449118786       57774344       23910261         308537 
Gi8/0/8      24742468145       52252939       23910257         307374 
Gi8/0/9      36111648474       60443326       23910358         306375 
Gi8/0/10     24951866532       51555297       23910353         318105 
Gi8/0/11      7759124511       36432212       23910407         356101 
Gi8/0/12     31315594392       62361826       23910384         360108 
Gi8/0/13    102245869354      126935346       23910320         314619 
Gi8/0/14            5273             10             25             10 
Gi8/0/15     92933255890      116813682       23910374         357291 
Gi8/0/16     10633172992       32575374       41379143       16998988 
Gi8/0/17          105029            258            359            201 
Gi8/0/18     88194693266      119016788       23910350         357183 
Gi8/0/19     14508971376       40648443       43338703       17725996 
Gi8/0/20     22557166564       46333621       23788373         306730 
Gi8/0/21     27289127688       52143966       23910359         308295 
Gi8/0/22     18131995265       43015608       23910324         313802 
Gi8/0/23    157893337925      273551846       43323630       17802161 
Gi8/0/24     13361531287       37699032       43404727       17702237 
Gi8/0/25     16954829155       47494499       23910359         360745 
Gi8/0/26     14149893747       40529720       43343538       17725282 
Gi8/0/27     37880178271       67971478       23910386         308248 
Gi8/0/28     64957100150      124469256       43296919       17679043 
Gi8/0/29               0              0              0              0 
Gi8/0/30     23817626001       48990742       23910325         316568 
Gi8/0/31     13388012426       37933760       43402789       17693165 
Gi8/0/32    115639182517      209708281       43374743       17807423 
Gi8/0/33     29847907081       58588190       43405683       17821461 
Gi8/0/34     34826149340       71072823       43401465       17817081 
Gi8/0/35     20358783912       60032543       43394951       17806376 
Gi8/0/36     65317335736      122280572       43408460       17704851 
Gi8/0/37               0              0              0              0 
Gi8/0/38     10739009794       33082061       41677240       17093992 
Gi8/0/39               0              0              0              0 
Gi8/0/40               0              0              0              0 
Gi8/0/41               0              0              0              0 
          
Port           OutOctets   OutUcastPkts   OutMcastPkts   OutBcastPkts 
Gi8/0/42               0              0              0              0 
Gi8/0/43               0              0              0              0 
Gi8/0/44               0              0              0              0 
Gi8/0/45     26198423094       56514571       23910356         360712 
Gi8/0/46     11140863660       34481228       43435015       17418903 
Gi8/0/47               0              0              0              0 
Gi8/0/48      5227890308        2660597       45278289         935857 
Po30       1971808734215     6759775823       82736682       32657218 """,
 'show cdp nei detail':"""-------------------------
Device ID: ap-0525-4-4438
Entry address(es): 
  IP address: 172.20.96.97
  IPv6 address: FE80::5EA6:2DFF:FEE6:397A  (link-local)
Platform: cisco AIR-AP2802I-B-K9,  Capabilities: Router Trans-Bridge 
Interface: GigabitEthernet1/0/46,  Port ID (outgoing port): GigabitEthernet0
Holdtime : 155 sec

Version :
Cisco AP Software, ap3g3-k9w8 Version: 8.5.151.0
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 2014-2015 by Cisco Systems, Inc.

advertisement version: 2
Duplex: full
Management address(es): 
  IP address: 172.20.96.97

-------------------------
Device ID: sx1-525hosp-1443-clinical.net.utah.edu
Entry address(es): 
  IP address: 172.20.64.37
Platform: cisco C9407R,  Capabilities: Switch IGMP 
Interface: TenGigabitEthernet4/0/11,  Port ID (outgoing port): TenGigabitEthernet3/0/2
Holdtime : 176 sec

Version :
Cisco IOS Software [Everest], Catalyst L3 Switch Software (CAT9K_IOSXE), Version 16.6.4, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2018 by Cisco Systems, Inc.
Compiled Sun 08-Jul-18 04:21 by mcpre

advertisement version: 2
VTP Management Domain: 'vtp-525hosp'
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 172.20.64.37

-------------------------
Device ID: sx2-525hosp-4317-clinical.net.utah.edu
Entry address(es): 
  IP address: 172.20.64.42
Platform: cisco C9300-48U,  Capabilities: Switch IGMP 
Interface: TenGigabitEthernet4/0/18,  Port ID (outgoing port): TenGigabitEthernet1/1/2
Holdtime : 179 sec

Version :
Cisco IOS Software [Everest], Catalyst L3 Switch Software (CAT9K_IOSXE), Version 16.6.5, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2018 by Cisco Systems, Inc.
Compiled Mon 10-Dec-18 12:52 by mcpre

advertisement version: 2
VTP Management Domain: 'vtp-525hosp'
Native VLAN: 1
Duplex: full
Management address(es): 
            IP address: 172.20.64.42

-------------------------
Device ID: sx1-525hosp-4270-clinical.net.utah.edu
Entry address(es): 
  IP address: 172.20.64.58
Platform: cisco WS-C3650-48PQ,  Capabilities: Switch IGMP 
Interface: TenGigabitEthernet4/0/3,  Port ID (outgoing port): TenGigabitEthernet1/1/1
Holdtime : 160 sec

Version :
Cisco IOS Software, IOS-XE Software, Catalyst L3 Switch Software (CAT3K_CAA-UNIVERSALK9-M), Version 03.07.03E RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2016 by Cisco Systems, Inc.
Compiled Wed 13-Jan-16 23:40 by prod_rel_team

advertisement version: 2
VTP Management Domain: 'vtp-525hosp'
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 172.20.64.58

-------------------------
Device ID: sx1-525hosp-4317-clinical.net.utah.edu
Entry address(es): 
  IP address: 172.20.64.70
Platform: cisco C9410R,  Capabilities: Switch IGMP 
Interface: TenGigabitEthernet4/0/10,  Port ID (outgoing port): TenGigabitEthernet5/0/2
Holdtime : 167 sec

Version :
Cisco IOS Software [Everest], Catalyst L3 Switch Software (CAT9K_IOSXE), Version 16.6.5, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2018 by Cisco Systems, Inc.
Compiled Mon 10-Dec-18 12:52 by mcpre

advertisement version: 2
VTP Management Domain: 'vtp-525hosp'
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 172.20.64.70

-------------------------
Device ID: ap-0525-4-4419
Entry address(es): 
  IP address: 172.20.96.44
  IPv6 address: FE80::1A80:90FF:FE2E:4ABA  (link-local)
Platform: cisco AIR-AP3802I-B-K9,  Capabilities: Router Trans-Bridge 
Interface: GigabitEthernet1/0/42,  Port ID (outgoing port): GigabitEthernet0
Holdtime : 166 sec

Version :
Cisco AP Software, ap3g3-k9w8 Version: 8.5.151.0
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 2014-2015 by Cisco Systems, Inc.

          advertisement version: 2
Duplex: full
Management address(es): 
  IP address: 172.20.96.44

-------------------------
Device ID: sx1-525hosp-2741-clinical.net.utah.edu
Entry address(es): 
  IP address: 172.20.64.16
Platform: cisco C9410R,  Capabilities: Switch IGMP 
Interface: TenGigabitEthernet4/0/17,  Port ID (outgoing port): TenGigabitEthernet5/0/2
Holdtime : 159 sec

Version :
Cisco IOS Software [Everest], Catalyst L3 Switch Software (CAT9K_IOSXE), Version 16.6.4, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2018 by Cisco Systems, Inc.
Compiled Sun 08-Jul-18 04:21 by mcpre

advertisement version: 2
VTP Management Domain: 'vtp-525hosp'
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 172.20.64.16

-------------------------
Device ID: sx1-525hosp-4525-clinical.net.utah.edu
Entry address(es): 
  IP address: 172.20.64.27
Platform: cisco C9410R,  Capabilities: Switch IGMP 
Interface: TenGigabitEthernet4/0/19,  Port ID (outgoing port): TenGigabitEthernet5/0/2
Holdtime : 126 sec

Version :
Cisco IOS Software [Gibraltar], Catalyst L3 Switch Software (CAT9K_IOSXE), Version 16.12.3a, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2020 by Cisco Systems, Inc.
Compiled Tue 28-Apr-20 09:37 by mcpre

advertisement version: 2
VTP Management Domain: 'vtp-525hosp'
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 172.20.64.27

-------------------------
Device ID: sx1-525hosp-1511-clinical.net.utah.edu
Entry address(es): 
  IP address: 172.20.64.12
Platform: cisco C9410R,  Capabilities: Switch IGMP 
Interface: TenGigabitEthernet4/0/1,  Port ID (outgoing port): TenGigabitEthernet5/0/2
Holdtime : 126 sec

Version :
Cisco IOS Software [Everest], Catalyst L3 Switch Software (CAT9K_IOSXE), Version 16.6.4, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2018 by Cisco Systems, Inc.
          Compiled Sun 08-Jul-18 04:21 by mcpre

advertisement version: 2
VTP Management Domain: 'vtp-525hosp'
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 172.20.64.12

-------------------------
Device ID: sx1-525hosp-3043-clinical.net.utah.edu
Entry address(es): 
  IP address: 172.20.64.24
Platform: cisco C9410R,  Capabilities: Switch IGMP 
Interface: TenGigabitEthernet4/0/4,  Port ID (outgoing port): TenGigabitEthernet5/0/2
Holdtime : 176 sec

Version :
Cisco IOS Software [Everest], Catalyst L3 Switch Software (CAT9K_IOSXE), Version 16.6.5, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2018 by Cisco Systems, Inc.
Compiled Mon 10-Dec-18 12:52 by mcpre

advertisement version: 2
VTP Management Domain: 'vtp-525hosp'
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 172.20.64.24

-------------------------
Device ID: ap-0525-4-4611
Entry address(es): 
  IP address: 172.20.96.140
  IPv6 address: FE80::2EB:D5FF:FE10:5660  (link-local)
Platform: cisco AIR-AP1810W-B-K9,  Capabilities: Router Trans-Bridge 
Interface: GigabitEthernet1/0/43,  Port ID (outgoing port): GigabitEthernet0
Holdtime : 120 sec

Version :
Cisco AP Software, ap1g4-k9w8 Version: 8.5.151.0
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 2014-2015 by Cisco Systems, Inc.

advertisement version: 2
Duplex: full
Management address(es): 
  IP address: 172.20.96.140

-------------------------
Device ID: ap-0525-4-4601
Entry address(es): 
  IP address: 172.20.96.130
  IPv6 address: FE80::227:90FF:FE48:1F90  (link-local)
Platform: cisco AIR-AP1810W-B-K9,  Capabilities: Router Trans-Bridge 
Interface: GigabitEthernet1/0/39,  Port ID (outgoing port): GigabitEthernet0
Holdtime : 132 sec

Version :
          Cisco AP Software, ap1g4-k9w8 Version: 8.5.151.0
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 2014-2015 by Cisco Systems, Inc.

advertisement version: 2
Duplex: full
Management address(es): 
  IP address: 172.20.96.130

-------------------------
Device ID: ap-0525-4-4631
Entry address(es): 
  IP address: 172.20.85.138
  IPv6 address: FE80::2EB:D5FF:FE10:D70  (link-local)
Platform: cisco AIR-AP1810W-B-K9,  Capabilities: Router Trans-Bridge 
Interface: GigabitEthernet1/0/41,  Port ID (outgoing port): GigabitEthernet0
Holdtime : 114 sec

Version :
Cisco AP Software, ap1g4-k9w8 Version: 8.5.151.0
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 2014-2015 by Cisco Systems, Inc.

advertisement version: 2
Duplex: full
Management address(es): 
  IP address: 172.20.85.138

-------------------------
Device ID: ap-0525-4-4713
Entry address(es): 
  IP address: 172.20.96.55
  IPv6 address: FE80::B226:80FF:FEDF:6246  (link-local)
Platform: cisco AIR-AP3802I-B-K9,  Capabilities: Router Trans-Bridge 
Interface: GigabitEthernet1/0/44,  Port ID (outgoing port): GigabitEthernet0
Holdtime : 121 sec

Version :
Cisco AP Software, ap3g3-k9w8 Version: 8.5.151.0
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 2014-2015 by Cisco Systems, Inc.

advertisement version: 2
Duplex: full
Management address(es): 
  IP address: 172.20.96.55

-------------------------
Device ID: ap-0525-4-4705
Entry address(es): 
  IP address: 172.20.85.246
  IPv6 address: FE80::5EA6:2DFF:FED7:5132  (link-local)
Platform: cisco AIR-AP2802I-B-K9,  Capabilities: Router Trans-Bridge 
Interface: GigabitEthernet1/0/45,  Port ID (outgoing port): GigabitEthernet0
Holdtime : 153 sec

Version :
Cisco AP Software, ap3g3-k9w8 Version: 8.5.151.0
Technical Support: http://www.cisco.com/techsupport
          Copyright (c) 2014-2015 by Cisco Systems, Inc.

advertisement version: 2
Duplex: full
Management address(es): 
  IP address: 172.20.85.246

-------------------------
Device ID: sx2-525hosp-1408-clinical.net.utah.edu
Entry address(es): 
  IP address: 172.20.64.81
Platform: cisco C9410R,  Capabilities: Switch IGMP 
Interface: TenGigabitEthernet5/0/6,  Port ID (outgoing port): TenGigabitEthernet5/0/2
Holdtime : 134 sec

Version :
Cisco IOS Software [Gibraltar], Catalyst L3 Switch Software (CAT9K_IOSXE), Version 16.12.3a, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2020 by Cisco Systems, Inc.
Compiled Tue 28-Apr-20 09:37 by mcpre

advertisement version: 2
VTP Management Domain: 'vtp-525hosp'
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 172.20.64.81

-------------------------
Device ID: ap-0525-4-4663
Entry address(es): 
  IP address: 172.20.96.188
  IPv6 address: FE80::2616:9DFF:FED9:EB7E  (link-local)
Platform: cisco AIR-AP2802I-B-K9,  Capabilities: Router Trans-Bridge 
Interface: GigabitEthernet1/0/48,  Port ID (outgoing port): GigabitEthernet0
Holdtime : 141 sec

Version :
Cisco AP Software, ap3g3-k9w8 Version: 8.5.151.0
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 2014-2015 by Cisco Systems, Inc.

advertisement version: 2
Duplex: full
Management address(es): 
  IP address: 172.20.96.188

-------------------------
Device ID: ap-0525-4-4416
Entry address(es): 
  IP address: 155.100.196.216
  IPv6 address: FE80::227:90FF:FE48:1F68  (link-local)
Platform: cisco AIR-AP1810W-B-K9,  Capabilities: Router Trans-Bridge 
Interface: GigabitEthernet7/0/5,  Port ID (outgoing port): GigabitEthernet0
Holdtime : 156 sec

Version :
Cisco AP Software, ap1g4-k9w8 Version: 8.5.151.0
Technical Support: http://www.cisco.com/techsupport
          Copyright (c) 2014-2015 by Cisco Systems, Inc.

advertisement version: 2
Duplex: full
Management address(es): 
  IP address: 155.100.196.216

-------------------------
Device ID: sx1-525hosp-1408-clinical.net.utah.edu
Entry address(es): 
  IP address: 172.20.64.80
Platform: cisco C9300-48UXM,  Capabilities: Switch IGMP 
Interface: TenGigabitEthernet5/0/5,  Port ID (outgoing port): TenGigabitEthernet1/1/2
Holdtime : 163 sec

Version :
Cisco IOS Software [Gibraltar], Catalyst L3 Switch Software (CAT9K_IOSXE), Version 16.12.4, RELEASE SOFTWARE (fc5)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2020 by Cisco Systems, Inc.
Compiled Thu 09-Jul-20 21:49 by mcpre

advertisement version: 2
VTP Management Domain: 'vtp-525hosp'
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 172.20.64.80

-------------------------
Device ID: ap-0525-4-4643
Entry address(es): 
  IP address: 172.20.85.229
  IPv6 address: FE80::227:90FF:FE48:1F80  (link-local)
Platform: cisco AIR-AP1810W-B-K9,  Capabilities: Router Trans-Bridge 
Interface: GigabitEthernet1/0/40,  Port ID (outgoing port): GigabitEthernet0
Holdtime : 121 sec

Version :
Cisco AP Software, ap1g4-k9w8 Version: 8.5.151.0
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 2014-2015 by Cisco Systems, Inc.

advertisement version: 2
Duplex: full
Management address(es): 
  IP address: 172.20.85.229

-------------------------
Device ID: sx1-525hosp-5105.net.utah.edu
Entry address(es): 
  IP address: 172.20.64.131
Platform: cisco WS-C4510R+E,  Capabilities: Router Switch IGMP 
Interface: TenGigabitEthernet4/0/13,  Port ID (outgoing port): TenGigabitEthernet5/2
Holdtime : 159 sec

Version :
Cisco IOS Software, Catalyst 4500 L3 Switch Software (cat4500e-UNIVERSALK9-M), Version 15.1(2)SG3, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
          Copyright (c) 1986-2013 by Cisco Systems, Inc.
Compiled Thu 19-Dec-13 14:08 by prod_rel_team

advertisement version: 2
VTP Management Domain: 'sx1-525hosp-5105'
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 172.20.64.131

-------------------------
Device ID: ap-0525-5-5550.net.utah.edu
Entry address(es): 
  IP address: 172.20.85.251
  IPv6 address: FE80::E6AA:5DFF:FE00:12FC  (link-local)
Platform: cisco AIR-CAP3702I-A-K9,  Capabilities: Trans-Bridge Source-Route-Bridge IGMP 
Interface: GigabitEthernet1/0/24,  Port ID (outgoing port): GigabitEthernet0
Holdtime : 161 sec

Version :
Cisco IOS Software, C3700 Software (AP3G2-K9W8-M), Version 15.3(3)JF10, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2019 by Cisco Systems, Inc.
Compiled Thu 13-Jun-19 18:51 by prod_rel_team

advertisement version: 2
Duplex: full
Power drawn: 16.800 Watts
Power request id: 42672, Power management id: 2
Power request levels are:0 0 0 0 0 
Management address(es): 
  IP address: 172.20.85.251

-------------------------
Device ID: sx1-525hosp-3745.net.utah.edu
Entry address(es): 
  IP address: 172.20.64.132
Platform: cisco WS-C4510R+E,  Capabilities: Router Switch IGMP 
Interface: TenGigabitEthernet4/0/7,  Port ID (outgoing port): TenGigabitEthernet5/1
Holdtime : 134 sec

Version :
Cisco IOS Software, IOS-XE Software, Catalyst 4500 L3 Switch Software (cat4500e-UNIVERSALK9-M), Version 03.05.02.E RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2014 by Cisco Systems, Inc.
Compiled Tue 11-Mar-14 16:27 by prod_rel_team

advertisement version: 2
VTP Management Domain: 'sx1-525hosp-3745'
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 172.20.64.132

-------------------------
Device ID: sx1-525hosp-6103.net.utah.edu
Entry address(es): 
  IP address: 172.20.64.10
          Platform: cisco C9410R,  Capabilities: Switch IGMP 
Interface: TenGigabitEthernet4/0/14,  Port ID (outgoing port): TenGigabitEthernet5/0/2
Holdtime : 153 sec

Version :
Cisco IOS Software [Everest], Catalyst L3 Switch Software (CAT9K_IOSXE), Version 16.6.5, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2018 by Cisco Systems, Inc.
Compiled Mon 10-Dec-18 12:52 by mcpre

advertisement version: 2
VTP Management Domain: 'vtp-525hosp'
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 172.20.64.10

-------------------------
Device ID: sx2-525hosp-3745.net.utah.edu
Entry address(es): 
  IP address: 172.20.64.26
Platform: cisco WS-C4510R+E,  Capabilities: Router Switch IGMP 
Interface: TenGigabitEthernet4/0/6,  Port ID (outgoing port): TenGigabitEthernet5/1
Holdtime : 145 sec

Version :
Cisco IOS Software, Catalyst 4500 L3 Switch Software (cat4500e-UNIVERSALK9-M), Version 15.1(2)SG3, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2013 by Cisco Systems, Inc.
Compiled Thu 19-Dec-13 14:08 by prod_rel_team

advertisement version: 2
VTP Management Domain: 'sx2-525hosp-3745'
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 172.20.64.26

-------------------------
Device ID: sx1-525hosp-2411.net.utah.edu
Entry address(es): 
  IP address: 172.20.64.29
Platform: cisco WS-C4510R+E,  Capabilities: Switch IGMP 
Interface: TenGigabitEthernet4/0/16,  Port ID (outgoing port): TenGigabitEthernet5/1
Holdtime : 134 sec

Version :
Cisco IOS Software, Catalyst 4500 L3 Switch Software (cat4500e-UNIVERSALK9-M), Version 15.1(2)SG3, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2013 by Cisco Systems, Inc.
Compiled Thu 19-Dec-13 14:08 by prod_rel_team

advertisement version: 2
VTP Management Domain: 'sx1-525hosp-2411'
Native VLAN: 1
Duplex: full
Management address(es): 
            IP address: 172.20.64.29

-------------------------
Device ID: sx1-525hosp-3306.net.utah.edu
Entry address(es): 
  IP address: 172.20.64.23
Platform: cisco WS-C4510R+E,  Capabilities: Switch IGMP 
Interface: TenGigabitEthernet4/0/8,  Port ID (outgoing port): TenGigabitEthernet5/1
Holdtime : 129 sec

Version :
Cisco IOS Software, Catalyst 4500 L3 Switch Software (cat4500e-UNIVERSALK9-M), Version 15.1(2)SG3, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2013 by Cisco Systems, Inc.
Compiled Thu 19-Dec-13 14:08 by prod_rel_team

advertisement version: 2
VTP Management Domain: 'sx1-525hosp-3306'
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 172.20.64.23

-------------------------
Device ID: sx1-525hosp-1873.net.utah.edu
Entry address(es): 
  IP address: 172.20.64.110
Platform: cisco WS-C4506-E,  Capabilities: Router Switch IGMP 
Interface: TenGigabitEthernet4/0/5,  Port ID (outgoing port): TenGigabitEthernet1/2
Holdtime : 128 sec

Version :
Cisco IOS Software, Catalyst 4500 L3 Switch  Software (cat4500es8-UNIVERSALK9-M), Version 15.2(3)E, RELEASE SOFTWARE (fc4)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2014 by Cisco Systems, Inc.
Compiled Sun 07-Dec-14 17:59 by prod_rel_team

advertisement version: 2
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 172.20.64.110

-------------------------
Device ID: sx1-0525hosp-2673-clinical.net.utah.edu
Entry address(es): 
  IP address: 172.20.64.59
Platform: cisco WS-C3850-48P,  Capabilities: Switch IGMP 
Interface: TenGigabitEthernet4/0/20,  Port ID (outgoing port): TenGigabitEthernet1/1/2
Holdtime : 159 sec

Version :
Cisco IOS Software [Everest], Catalyst L3 Switch Software (CAT3K_CAA-UNIVERSALK9-M), Version 16.6.8, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2020 by Cisco Systems, Inc.
          Compiled Thu 23-Apr-20 17:22 by mcpre

advertisement version: 2
VTP Management Domain: 'vtp-0525hosp'
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 172.20.64.59

-------------------------
Device ID: sx1-0525hosp-2255-clinical.net.utah.edu
Entry address(es): 
  IP address: 172.20.64.46
Platform: cisco C9300-48U,  Capabilities: Switch IGMP 
Interface: TenGigabitEthernet4/0/23,  Port ID (outgoing port): TenGigabitEthernet2/1/1
Holdtime : 172 sec

Version :
Cisco IOS Software [Gibraltar], Catalyst L3 Switch Software (CAT9K_IOSXE), Version 16.12.4, RELEASE SOFTWARE (fc5)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2020 by Cisco Systems, Inc.
Compiled Thu 09-Jul-20 21:49 by mcpre

advertisement version: 2
VTP Management Domain: 'vtp-521som'
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 172.20.64.46

-------------------------
Device ID: r2-clinical-park.net.utah.edu(JPG224500DL)
Entry address(es): 
  IP address: 10.104.213.227
Platform: N77-C7710,  Capabilities: Router Switch IGMP CVTA phone port 
Interface: TenGigabitEthernet5/0/2,  Port ID (outgoing port): Ethernet1/10
Holdtime : 160 sec

Version :
Cisco Nexus Operating System (NX-OS) Software, Version 8.2(2)

advertisement version: 2
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 172.29.1.17

-------------------------
Device ID: sx1-525hosp-1437B-clinical.net.utah.edu
Entry address(es): 
  IP address: 172.20.64.72
Platform: cisco WS-C4510R+E,  Capabilities: Switch IGMP 
Interface: TenGigabitEthernet4/0/22,  Port ID (outgoing port): TenGigabitEthernet5/1
Holdtime : 144 sec

Version :
Cisco IOS Software, Catalyst 4500 L3 Switch  Software (cat4500es8-UNIVERSALK9-M), Version 15.2(3)E, RELEASE SOFTWARE (fc4)
Technical Support: http://www.cisco.com/techsupport
          Copyright (c) 1986-2014 by Cisco Systems, Inc.
Compiled Sun 07-Dec-14 17:59 by prod_rel_team

advertisement version: 2
VTP Management Domain: 'sx1-525hosp-1437B'
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 172.20.64.72

-------------------------
Device ID: sx1-525hosp-a0070-clinical
Entry address(es): 
  IP address: 172.20.64.62
Platform: cisco C9410R,  Capabilities: Switch IGMP 
Interface: TenGigabitEthernet5/0/3,  Port ID (outgoing port): TenGigabitEthernet5/0/2
Holdtime : 145 sec

Version :
Cisco IOS Software [Fuji], Catalyst L3 Switch Software (CAT9K_IOSXE), Version 16.9.4, RELEASE SOFTWARE (fc2)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2019 by Cisco Systems, Inc.
Compiled Thu 22-Aug-19 18:14 by mcpre

advertisement version: 2
VTP Management Domain: 'vtp-525hosp'
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 172.20.64.62

-------------------------
Device ID: sx1-525hosp-b157-clinical.net.utah.edu
Entry address(es): 
  IP address: 172.20.64.50
Platform: cisco C9410R,  Capabilities: Switch IGMP 
Interface: TenGigabitEthernet4/0/2,  Port ID (outgoing port): TenGigabitEthernet5/0/2
Holdtime : 139 sec

Version :
Cisco IOS Software [Gibraltar], Catalyst L3 Switch Software (CAT9K_IOSXE), Version 16.12.4, RELEASE SOFTWARE (fc5)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2020 by Cisco Systems, Inc.
Compiled Thu 09-Jul-20 21:49 by mcpre

advertisement version: 2
VTP Management Domain: 'vtp-525hosp'
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 172.20.64.50

-------------------------
Device ID: sx2-525hosp-a371-clinical.net.utah.edu
Entry address(es): 
  IP address: 172.20.64.17
Platform: cisco C9407R,  Capabilities: Switch IGMP 
Interface: TenGigabitEthernet4/0/9,  Port ID (outgoing port): TenGigabitEthernet3/0/2
Holdtime : 159 sec
          
Version :
Cisco IOS Software [Everest], Catalyst L3 Switch Software (CAT9K_IOSXE), Version 16.6.5, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2018 by Cisco Systems, Inc.
Compiled Mon 10-Dec-18 12:52 by mcpre

advertisement version: 2
VTP Management Domain: 'vtp-525hosp'
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 172.20.64.17

-------------------------
Device ID: r1-clinical-b244.net.utah.edu(JPG22480005)
Entry address(es): 
  IP address: 10.104.213.226
Platform: N77-C7710,  Capabilities: Router Switch IGMP CVTA phone port 
Interface: TenGigabitEthernet5/0/1,  Port ID (outgoing port): Ethernet1/10
Holdtime : 169 sec

Version :
Cisco Nexus Operating System (NX-OS) Software, Version 8.2(2)

advertisement version: 2
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 172.29.1.16

-------------------------
Device ID: sx2-525hosp-a0070-clinical.net.utah.edu
Entry address(es): 
  IP address: 172.20.64.63
Platform: cisco C9410R,  Capabilities: Switch IGMP 
Interface: TenGigabitEthernet5/0/4,  Port ID (outgoing port): TenGigabitEthernet5/0/2
Holdtime : 156 sec

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
  IP address: 172.20.64.63

-------------------------
Device ID: sx1-525hosp-a673.net.utah.edu
Entry address(es): 
  IP address: 172.20.64.48
Platform: cisco WS-C3650-48PQ,  Capabilities: Switch IGMP 
Interface: TenGigabitEthernet4/0/24,  Port ID (outgoing port): TenGigabitEthernet1/1/2
Holdtime : 176 sec
          
Version :
Cisco IOS Software [Denali], Catalyst L3 Switch Software (CAT3K_CAA-UNIVERSALK9-M), Version 16.3.6, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2018 by Cisco Systems, Inc.
Compiled Wed 28-Feb-18 15:23 by mcpre

advertisement version: 2
VTP Management Domain: 'vtp-565eej'
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 172.20.64.48

-------------------------
Device ID: sx1-525hosp-a371.net.utah.edu
Entry address(es): 
  IP address: 172.20.64.45
Platform: cisco WS-C4510R+E,  Capabilities: Switch IGMP 
Interface: TenGigabitEthernet4/0/15,  Port ID (outgoing port): TenGigabitEthernet5/2
Holdtime : 170 sec

Version :
Cisco IOS Software, Catalyst 4500 L3 Switch Software (cat4500e-UNIVERSALK9-M), Version 15.1(2)SG3, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2013 by Cisco Systems, Inc.
Compiled Thu 19-Dec-13 14:08 by prod_rel_team

advertisement version: 2
VTP Management Domain: 'sx1-525hosp-a371'
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 172.20.64.45


Total cdp entries displayed : 39""",
 'show module all':"""^
% Invalid input detected at '^' marker.
""",
 'show module':"""Chassis Type: C9410R              

Mod Ports Card Type                                   Model          Serial No.
---+-----+--------------------------------------+--------------+--------------
1   48   48-Port UPOE 10/100/1000 (RJ-45)            C9400-LC-48U   JAE22280N09
4   24   24-Port 10 Gigabit Ethernet (SFP+)          C9400-LC-24XS  JAE222801VF
5   10   Supervisor 1 Module                         C9400-SUP-1    JAE22270XUG
7   48   48-Port UPOE 10/100/1000 (RJ-45)            C9400-LC-48U   JAE222809MC
8   48   48-Port UPOE 10/100/1000 (RJ-45)            C9400-LC-48U   JAE222805VD

Mod MAC addresses                    Hw   Fw           Sw                 Status
---+--------------------------------+----+------------+------------------+--------
1   BC26.C772.2940 to BC26.C772.296F 1.1  16.6.2r[FC1]  16.06.04a          ok        
4   B08B.CFE2.D598 to B08B.CFE2.D5AF 1.0  16.6.2r[FC1]  16.06.04a          ok        
5   A093.51D2.5C6C to A093.51D2.5C75 2.0  16.6.2r[FC1]  16.06.04a          ok        
7   BC26.C723.66B4 to BC26.C723.66E3 1.1  16.6.2r[FC1]  16.06.04a          ok        
8   BC26.C723.78B4 to BC26.C723.78E3 1.1  16.6.2r[FC1]  16.06.04a          ok        

Mod Redundancy Role     Operating Redundancy Mode Configured Redundancy Mode
---+-------------------+-------------------------+---------------------------
5   Active              active                    sso                       
""",
 'show run | section snmp':"""snmp-server group VoiceRO v3 priv read VoicePhones access 73
snmp-server group VoiceRO v3 auth context vlan- match prefix 
snmp-server group CliNOCGrv3RO v3 priv read CliNOCViewRO access 70
snmp-server group CliNOCGrv3RO v3 auth context vlan- match prefix 
snmp-server group CliNOCGrv3RW v3 priv write CliNOCViewRW access 71
snmp-server view VoicePhones internet included
snmp-server view CliNOCViewRO internet included
snmp-server view CliNOCViewRW internet included
snmp-server location Bldg. 525 Room 4659-new
snmp-server contact BC-509403 Y-334728
snmp-server context vlan-1
snmp-server context vlan-123
snmp-server context vlan-124
snmp-server context vlan-125
snmp-server context vlan-126
snmp-server context vlan-127
snmp-server context vlan-128
snmp-server context vlan-129
snmp-server context vlan-130
snmp-server context vlan-131
snmp-server context vlan-132
snmp-server context vlan-270
snmp-server context vlan-332
snmp-server context vlan-337
snmp-server context vlan-338
snmp-server context vlan-341
snmp-server context vlan-345
snmp-server context vlan-396
snmp-server context vlan-418
snmp-server context vlan-540
snmp-server context vlan-551
snmp-server context vlan-575
snmp-server context vlan-600
snmp-server context vlan-607
snmp-server context vlan-610
snmp-server context vlan-620
snmp-server context vlan-629
snmp-server context vlan-630
snmp-server context vlan-631
snmp-server context vlan-632
snmp-server context vlan-633
snmp-server context vlan-634
snmp-server context vlan-635
snmp-server context vlan-636
snmp-server context vlan-637
snmp-server context vlan-638
snmp-server context vlan-640
snmp-server context vlan-680
snmp-server context vlan-732
snmp-server context vlan-770
snmp-server context vlan-771
snmp-server context vlan-772
snmp-server context vlan-773
snmp-server context vlan-850
snmp-server context vlan-921
snmp-server context vlan-942
snmp-server context vlan-983
snmp-server context vlan-984
snmp-server context vlan-986
          snmp-server context vlan-987
snmp-server context vlan-988
snmp-server context vlan-989
snmp-server context vlan-990
snmp-server context vlan-1037
snmp-server context vlan-1041
snmp-server context vlan-1060
snmp-server context vlan-1075
snmp-server context vlan-1076
snmp-server context vlan-1112
snmp-server context vlan-1209
snmp-server context vlan-1600
snmp-server context vlan-1605
snmp-server context vlan-1616
snmp-server context vlan-1621
snmp-server context vlan-1672
snmp-server context vlan-1700
snmp-server context vlan-1800
snmp-server context vlan-1900
snmp-server context vlan-3000
snmp ifmib ifindex persist""",
 'show run | in snmp':"""snmp-server group VoiceRO v3 priv read VoicePhones access 73
snmp-server group VoiceRO v3 auth context vlan- match prefix 
snmp-server group CliNOCGrv3RO v3 priv read CliNOCViewRO access 70
snmp-server group CliNOCGrv3RO v3 auth context vlan- match prefix 
snmp-server group CliNOCGrv3RW v3 priv write CliNOCViewRW access 71
snmp-server view VoicePhones internet included
snmp-server view CliNOCViewRO internet included
snmp-server view CliNOCViewRW internet included
snmp-server location Bldg. 525 Room 4659-new
snmp-server contact BC-509403 Y-334728
snmp-server context vlan-1
snmp-server context vlan-123
snmp-server context vlan-124
snmp-server context vlan-125
snmp-server context vlan-126
snmp-server context vlan-127
snmp-server context vlan-128
snmp-server context vlan-129
snmp-server context vlan-130
snmp-server context vlan-131
snmp-server context vlan-132
snmp-server context vlan-270
snmp-server context vlan-332
snmp-server context vlan-337
snmp-server context vlan-338
snmp-server context vlan-341
snmp-server context vlan-345
snmp-server context vlan-396
snmp-server context vlan-418
snmp-server context vlan-540
snmp-server context vlan-551
snmp-server context vlan-575
snmp-server context vlan-600
snmp-server context vlan-607
snmp-server context vlan-610
snmp-server context vlan-620
snmp-server context vlan-629
snmp-server context vlan-630
snmp-server context vlan-631
snmp-server context vlan-632
snmp-server context vlan-633
snmp-server context vlan-634
snmp-server context vlan-635
snmp-server context vlan-636
snmp-server context vlan-637
snmp-server context vlan-638
snmp-server context vlan-640
snmp-server context vlan-680
snmp-server context vlan-732
snmp-server context vlan-770
snmp-server context vlan-771
snmp-server context vlan-772
snmp-server context vlan-773
snmp-server context vlan-850
snmp-server context vlan-921
snmp-server context vlan-942
snmp-server context vlan-983
snmp-server context vlan-984
snmp-server context vlan-986
          snmp-server context vlan-987
snmp-server context vlan-988
snmp-server context vlan-989
snmp-server context vlan-990
snmp-server context vlan-1037
snmp-server context vlan-1041
snmp-server context vlan-1060
snmp-server context vlan-1075
snmp-server context vlan-1076
snmp-server context vlan-1112
snmp-server context vlan-1209
snmp-server context vlan-1600
snmp-server context vlan-1605
snmp-server context vlan-1616
snmp-server context vlan-1621
snmp-server context vlan-1672
snmp-server context vlan-1700
snmp-server context vlan-1800
snmp-server context vlan-1900
snmp-server context vlan-3000
snmp ifmib ifindex persist""",
 'show snmp user':"""User name: prognosis
Engine ID: 800000090300A09351D25C4E
storage-type: nonvolatile	 active
Authentication Protocol: MD5
Privacy Protocol: DES
Group-name: VoiceRO

User name: CliNONUserv3RO
Engine ID: 800000090300A09351D25C4E
storage-type: nonvolatile	 active
Authentication Protocol: MD5
Privacy Protocol: DES
Group-name: CliNOCGrv3RW

User name: CliNONUserv3Rw
Engine ID: 800000090300A09351D25C4E
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
    150 permit 10.71.24.17
    140 permit 10.71.24.16
    170 permit 10.71.24.19
    160 permit 10.71.24.18
    20 permit 172.20.150.100
    220 permit 10.71.24.25
    110 permit 10.71.24.13 (11327463 matches)
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
    10 permit tcp 155.98.253.0 0.0.0.255 any eq 22 (74 matches)
    20 permit tcp host 172.20.150.100 any eq 22
    30 permit tcp host 155.100.126.162 any eq 22
              40 permit tcp host 155.100.126.163 any eq 22
    50 permit tcp host 10.64.2.70 any eq 22
    60 permit tcp host 155.99.239.130 any eq 22
    70 permit tcp host 155.97.152.244 any eq 22
    80 permit tcp host 155.100.123.72 any eq 22
    90 permit tcp 155.99.254.128 0.0.0.127 any eq 22 (10 matches)
    100 permit tcp 155.98.164.192 0.0.0.31 any eq 22 (10 matches)
    110 permit tcp host 10.71.24.11 any eq 22
    120 permit tcp host 10.71.24.12 any eq 22
    130 permit tcp host 10.71.24.13 any eq 22 (88 matches)
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
logging host 155.98.204.52
logging host 155.98.253.244
logging host 172.24.29.14
logging host 10.70.24.10""",
 'show run | in logging':"""logging buffered notifications
logging console critical
logging facility local6
logging source-interface Vlan332
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
 All    0180.c200.0021    STATIC      CPU
 All    ffff.ffff.ffff    STATIC      CPU
   1    002f.5cfd.d451    DYNAMIC     Po30
   1    34ed.1bc4.2dec    DYNAMIC     Te4/0/3
   1    34f8.e7a5.793d    DYNAMIC     Po30
 332    0000.0c9f.f14c    DYNAMIC     Po30
 332    000d.5d0a.ebae    DYNAMIC     Po30
 332    003a.9c3f.d7c1    DYNAMIC     Po30
 332    003a.9c40.0dc1    DYNAMIC     Po30
 332    00c0.b729.995b    DYNAMIC     Po30
 332    00c0.b766.84ed    DYNAMIC     Po30
 332    00c0.b768.dab8    DYNAMIC     Po30
 332    00c0.b768.db60    DYNAMIC     Po30
 332    00c0.b76d.680e    DYNAMIC     Gi8/0/48
 332    00c0.b774.55ff    DYNAMIC     Po30
 332    00c0.b794.5f61    DYNAMIC     Po30
 332    00c0.b7b3.9c91    DYNAMIC     Po30
 332    00c0.b7c3.f756    DYNAMIC     Po30
 332    00c0.b7c4.265b    DYNAMIC     Po30
 332    00c0.b7c9.570a    DYNAMIC     Po30
 332    00c0.b7d2.aba8    DYNAMIC     Po30
 332    00c0.b7e1.f27f    DYNAMIC     Po30
 332    00c0.b7e9.b142    DYNAMIC     Po30
 332    00c0.b7eb.4796    DYNAMIC     Po30
 332    00c0.b7f1.17eb    DYNAMIC     Po30
 332    00c0.b7f1.212e    DYNAMIC     Po30
 332    00c0.b7f1.214a    DYNAMIC     Po30
 332    00c0.b7f1.216d    DYNAMIC     Po30
 332    00c0.b7f1.21a0    DYNAMIC     Po30
 332    00c0.b7f1.21a3    DYNAMIC     Po30
 332    00c0.b7fa.064c    DYNAMIC     Po30
 332    00f6.63a7.62c9    DYNAMIC     Po30
 332    2829.8623.8502    DYNAMIC     Po30
 332    34ed.1bc4.2dc5    DYNAMIC     Po30
 332    34ed.1bc4.2dec    DYNAMIC     Po30
           332    3c13.cc26.eec9    DYNAMIC     Po30
 332    502f.a8c9.e285    DYNAMIC     Po30
 332    502f.a8c9.ee45    DYNAMIC     Po30
 332    503d.e583.20bf    DYNAMIC     Po30
 332    503d.e583.2c7f    DYNAMIC     Po30
 332    503d.e583.2cff    DYNAMIC     Po30
 332    503d.e583.2dbf    DYNAMIC     Po30
 332    5475.d019.053f    DYNAMIC     Po30
 332    700f.6add.3e45    DYNAMIC     Po30
 332    7018.a722.fac9    DYNAMIC     Po30
 332    7061.7b23.8605    DYNAMIC     Po30
 332    7079.b3f2.5a45    DYNAMIC     Po30
 332    7079.b3f2.8005    DYNAMIC     Po30
 332    848a.8dfd.f5c9    DYNAMIC     Po30
 332    a093.51d2.5c45    STATIC      Vl332 
 332    a093.51d2.6745    DYNAMIC     Po30
 332    a093.51d2.71c5    DYNAMIC     Po30
 332    a093.51d2.7285    DYNAMIC     Po30
 332    a89d.21bc.d149    DYNAMIC     Po30
 332    bc16.65d2.a03f    DYNAMIC     Po30
 332    c014.fe7c.b5c5    DYNAMIC     Po30
 332    f86b.d9c2.5845    DYNAMIC     Po30
 332    f8a5.c589.81c9    DYNAMIC     Po30
 632    0000.0c9f.f278    DYNAMIC     Po30
 632    0001.2991.d5fd    DYNAMIC     Po30
 632    0005.b7de.e513    DYNAMIC     Po30
 632    0005.b7e2.f43f    DYNAMIC     Po30
 632    0007.326c.c941    DYNAMIC     Po30
 632    0007.3271.1030    DYNAMIC     Gi7/0/6
 632    0007.327c.b418    DYNAMIC     Po30
 632    0007.327c.b5e0    DYNAMIC     Gi8/0/26
 632    0007.327c.b60c    DYNAMIC     Gi7/0/3
 632    0007.327c.b8b0    DYNAMIC     Gi8/0/19
 632    0007.327c.b9b2    DYNAMIC     Po30
 632    0007.327d.1bb1    DYNAMIC     Po30
 632    0007.327d.1e0b    DYNAMIC     Po30
 632    0007.327f.a174    DYNAMIC     Po30
 632    0007.327f.a410    DYNAMIC     Po30
 632    000c.c601.ae48    DYNAMIC     Po30
 632    000c.c601.aeae    DYNAMIC     Po30
 632    000c.c601.aeba    DYNAMIC     Gi8/0/38
 632    000c.c601.b16e    DYNAMIC     Gi7/0/23
 632    000c.c601.b826    DYNAMIC     Po30
 632    000c.c601.b834    DYNAMIC     Gi7/0/14
 632    000c.c601.b844    DYNAMIC     Gi8/0/16
 632    000c.c601.b8ca    DYNAMIC     Po30
 632    000c.c601.b8f6    DYNAMIC     Po30
 632    000c.c601.b912    DYNAMIC     Po30
 632    001a.4b17.af80    DYNAMIC     Po30
 632    0024.dd01.41b3    DYNAMIC     Po30
 632    0024.dd01.4221    DYNAMIC     Gi7/0/32
 632    0025.9092.3d1c    DYNAMIC     Gi8/0/31
 632    0025.9095.3354    DYNAMIC     Gi8/0/3
 632    0027.9048.1f68    DYNAMIC     Gi7/0/5
 632    003a.9c3f.d7c1    DYNAMIC     Po30
 632    003a.9c40.0dc1    DYNAMIC     Po30
 632    003e.e1cd.5267    DYNAMIC     Po30
 632    003e.e1cd.5acb    DYNAMIC     Po30
 632    0040.9d2c.86ff    DYNAMIC     Gi8/0/46
           632    00d0.694c.c8e5    DYNAMIC     Gi7/0/13
 632    0860.6efd.9bfa    DYNAMIC     Po30
 632    0cc4.7a16.c154    DYNAMIC     Gi8/0/24
 632    0cc4.7a16.de00    DYNAMIC     Gi8/0/4
 632    0cc4.7a72.7694    DYNAMIC     Po30
 632    0cc4.7a72.8f53    DYNAMIC     Gi7/0/10
 632    0cc4.7a72.908c    DYNAMIC     Po30
 632    0cc4.7a94.079b    DYNAMIC     Po30
 632    0cc4.7ae3.c929    DYNAMIC     Po30
 632    1062.e519.14f4    DYNAMIC     Po30
 632    1062.e51b.86ca    DYNAMIC     Po30
 632    1062.e598.1f33    DYNAMIC     Gi7/0/42
 632    10e7.c606.1afa    DYNAMIC     Gi7/0/29
 632    10e7.c616.5797    DYNAMIC     Po30
 632    10e7.c616.57f2    DYNAMIC     Gi8/0/36
 632    1860.2421.a05f    DYNAMIC     Po30
 632    1860.2426.ba87    DYNAMIC     Po30
 632    1860.2428.84bc    DYNAMIC     Po30
 632    1860.2484.1584    DYNAMIC     Po30
 632    1860.24b0.9907    DYNAMIC     Po30
 632    3024.a9fa.b234    DYNAMIC     Po30
 632    3c2a.f441.a32c    DYNAMIC     Gi7/0/25
 632    3c52.825f.b165    DYNAMIC     Po30
 632    3cec.ef02.1158    DYNAMIC     Po30
 632    40b0.3418.1d94    DYNAMIC     Po30
 632    40b0.3418.1daa    DYNAMIC     Po30
 632    5cb9.0112.f01e    DYNAMIC     Po30
 632    6805.ca0b.00b2    DYNAMIC     Po30
 632    6879.ed74.a593    DYNAMIC     Po30
 632    68ab.8a82.938c    DYNAMIC     Po30
 632    68ab.8a82.940c    DYNAMIC     Po30
 632    6c2b.59c9.749d    DYNAMIC     Po30
 632    6c2b.59c9.7b41    DYNAMIC     Po30
 632    6c2b.59c9.b33d    DYNAMIC     Po30
 632    6c2b.59c9.b43a    DYNAMIC     Po30
 632    6c2b.59c9.b55e    DYNAMIC     Po30
 632    6c2b.59c9.b6b0    DYNAMIC     Po30
 632    6c2b.59c9.bbf9    DYNAMIC     Po30
 632    6c2b.59c9.bcc9    DYNAMIC     Po30
 632    6c2b.59cc.fcb3    DYNAMIC     Po30
 632    6c2b.59d3.ed09    DYNAMIC     Po30
 632    6c2b.59d4.e4e4    DYNAMIC     Po30
 632    6c2b.59e1.1bd0    DYNAMIC     Po30
 632    6c2b.59eb.4d52    DYNAMIC     Po30
 632    6c2b.59ef.1f1a    DYNAMIC     Gi8/0/28
 632    7018.a722.fab5    DYNAMIC     Po30
 632    705a.0f3c.f6aa    DYNAMIC     Gi7/0/28
 632    787b.8aab.7b61    DYNAMIC     Po30
 632    84a9.3e12.0c43    DYNAMIC     Po30
 632    a042.3f29.e77a    DYNAMIC     Po30
 632    a08c.fdc2.c9d2    DYNAMIC     Po30
 632    a08c.fddc.7572    DYNAMIC     Gi7/0/37
 632    a08c.fdeb.ff0a    DYNAMIC     Gi7/0/22
 632    a0dd.e5fc.950b    DYNAMIC     Gi7/0/16
 632    a4bb.6d4d.374c    DYNAMIC     Po30
 632    a4bb.6d4d.378f    DYNAMIC     Po30
 632    ac1f.6b14.020d    DYNAMIC     Po30
 632    ac1f.6b66.10d1    DYNAMIC     Po30
 632    ace2.d304.50b8    DYNAMIC     Po30
           632    ace2.d304.5174    DYNAMIC     Gi7/0/43
 632    ace2.d308.5082    DYNAMIC     Po30
 632    ace2.d30f.8cc3    DYNAMIC     Po30
 632    b827.ebaa.b933    DYNAMIC     Po30
 632    c0a2.6d00.acbd    DYNAMIC     Po30
 632    c8d3.ffa6.b18c    DYNAMIC     Po30
 632    c8d3.ffb5.431f    DYNAMIC     Po30
 632    c8d9.d209.61f4    DYNAMIC     Gi7/0/18
 632    dc4a.3e76.a787    DYNAMIC     Po30
 632    dc4a.3e7c.ab17    DYNAMIC     Po30
 632    dc4a.3e8a.7a22    DYNAMIC     Po30
 632    dc4a.3e92.7794    DYNAMIC     Po30
 632    dc4a.3e95.b31e    DYNAMIC     Po30
 632    dc4a.3e9b.c3c3    DYNAMIC     Po30
 632    e454.e85c.f2a0    DYNAMIC     Po30
 632    e454.e867.6106    DYNAMIC     Po30
 632    e454.e886.e323    DYNAMIC     Po30
 632    e454.e897.1306    DYNAMIC     Gi7/0/21
 632    e454.e8b5.238b    DYNAMIC     Gi8/0/1
 632    e4b9.7af9.c677    DYNAMIC     Po30
 632    ec8e.b579.8e37    DYNAMIC     Po30
 632    f439.0925.5c9d    DYNAMIC     Po30
 632    f439.0925.60ee    DYNAMIC     Po30
 632    fc3f.db0f.9ac2    DYNAMIC     Po30
 988    0000.0c9f.f3dc    DYNAMIC     Po30
 988    003a.9c3f.d7c1    DYNAMIC     Po30
 988    003a.9c40.0dc1    DYNAMIC     Po30
 988    34ed.1bc4.2dec    DYNAMIC     Po30
 988    a009.ed08.7281    DYNAMIC     Gi8/0/15
 988    a009.ed0b.77c6    DYNAMIC     Gi8/0/18
 988    a009.ed0b.7884    DYNAMIC     Gi7/0/28
 988    a009.ed0b.79f8    DYNAMIC     Gi7/0/27
 988    a009.ed0b.79fb    DYNAMIC     Gi8/0/11
 988    a009.ed0b.7a5b    DYNAMIC     Gi7/0/48
 988    a009.ed0b.7abb    DYNAMIC     Gi8/0/45
 988    a009.ed0b.7ae3    DYNAMIC     Gi7/0/37
 988    a009.ed0b.7af6    DYNAMIC     Gi7/0/17
 988    a009.ed0b.7b0c    DYNAMIC     Gi7/0/21
 988    a009.ed0b.7b10    DYNAMIC     Gi8/0/28
 988    a009.ed0b.7b35    DYNAMIC     Gi7/0/26
 988    a009.ed0b.7b39    DYNAMIC     Gi8/0/12
 988    a009.ed0b.7b3c    DYNAMIC     Gi7/0/45
 988    a009.ed0b.7b3e    DYNAMIC     Gi7/0/4
 988    a009.ed0b.7b42    DYNAMIC     Gi8/0/25
 988    a009.ed0b.7b4c    DYNAMIC     Gi7/0/44
 988    a009.ed0b.7b52    DYNAMIC     Gi8/0/5
 988    a425.1bc2.8cf9    DYNAMIC     Gi8/0/32
 988    b447.5eaa.dfe4    DYNAMIC     Gi8/0/35
 988    b447.5eae.97fb    DYNAMIC     Gi7/0/22
 988    b447.5eae.981b    DYNAMIC     Gi8/0/23
 988    b447.5eae.985a    DYNAMIC     Gi7/0/42
 988    b447.5eae.988d    DYNAMIC     Gi8/0/34
 988    b447.5eb1.104f    DYNAMIC     Gi7/0/18
 988    b447.5eb1.1c1f    DYNAMIC     Gi8/0/33
 988    c81f.ea98.852b    DYNAMIC     Gi8/0/2
 129    0000.0c9f.f081    DYNAMIC     Po30
 129    0005.b7de.e803    DYNAMIC     Gi7/0/2
 129    0025.6441.97b8    DYNAMIC     Gi7/0/45
 129    003a.9c3f.d7c1    DYNAMIC     Po30
           129    003a.9c40.0dc1    DYNAMIC     Po30
 129    00ee.ab3f.7ea8    DYNAMIC     Po30
 129    34ed.1bc4.2dec    DYNAMIC     Po30
 129    6c2b.5944.cbb1    DYNAMIC     Gi8/0/10
 129    6c2b.5944.ccb1    DYNAMIC     Gi7/0/44
 129    6c2b.5944.ccc4    DYNAMIC     Gi8/0/7
 129    6c2b.5946.a7d2    DYNAMIC     Gi7/0/4
 129    6c2b.5946.ed8d    DYNAMIC     Gi8/0/11
 129    6c2b.5947.8f22    DYNAMIC     Gi8/0/22
 129    6c2b.5949.3961    DYNAMIC     Gi8/0/5
 129    6c2b.5949.39c5    DYNAMIC     Gi7/0/26
 129    6c2b.5949.3b19    DYNAMIC     Gi8/0/21
 129    6c2b.5949.3c6a    DYNAMIC     Gi7/0/48
 129    6c2b.594c.287a    DYNAMIC     Gi7/0/27
 129    6c2b.594c.28a5    DYNAMIC     Gi7/0/38
 129    6c2b.594c.3ea3    DYNAMIC     Gi7/0/30
 129    6c2b.594c.b998    DYNAMIC     Gi7/0/19
 129    6c2b.594d.2322    DYNAMIC     Gi8/0/8
 129    6c2b.594d.239c    DYNAMIC     Gi8/0/12
 129    6c2b.594d.23f8    DYNAMIC     Gi8/0/30
 129    6c2b.594d.2461    DYNAMIC     Gi8/0/20
 129    6c2b.5953.af8a    DYNAMIC     Gi7/0/20
 129    6c2b.5954.0dca    DYNAMIC     Gi8/0/25
 129    6c2b.5954.0e2c    DYNAMIC     Gi7/0/46
 129    6c2b.5954.0e31    DYNAMIC     Gi8/0/13
 129    6c2b.5954.0f6f    DYNAMIC     Gi7/0/1
 129    6c2b.5954.12f8    DYNAMIC     Gi8/0/18
 129    6c2b.5954.13a2    DYNAMIC     Gi7/0/47
 129    6c2b.5954.13c8    DYNAMIC     Gi7/0/8
 129    6c2b.5954.13d6    DYNAMIC     Gi8/0/27
 129    6c2b.5954.2d0b    DYNAMIC     Gi7/0/11
 129    6c2b.5954.2d39    DYNAMIC     Gi8/0/45
 129    6c2b.5954.2d3f    DYNAMIC     Gi8/0/15
 129    6c2b.5963.e5e6    DYNAMIC     Gi8/0/9
 129    6c2b.5967.2b72    DYNAMIC     Gi7/0/41
 129    6c2b.5967.2b78    DYNAMIC     Gi7/0/39
 129    6c2b.5967.30a5    DYNAMIC     Gi7/0/40
 129    7018.a722.fab5    DYNAMIC     Po30
 129    70ea.1ae3.8e30    DYNAMIC     Po30
1060    0000.0c9f.f424    DYNAMIC     Po30
1060    0002.c18a.874d    DYNAMIC     Gi7/0/33
1060    0002.c18a.92ec    DYNAMIC     Po30
1060    0002.c18a.a4ee    DYNAMIC     Po30
1060    0002.c18a.a569    DYNAMIC     Po30
1060    0022.4dd9.e2b8    DYNAMIC     Po30
1060    003a.9c3f.d7c1    DYNAMIC     Po30
1060    003a.9c40.0dc1    DYNAMIC     Po30
 732    0000.0c9f.f2dc    DYNAMIC     Po30
 732    0001.0554.1c84    DYNAMIC     Po30
 732    0022.db01.b48a    DYNAMIC     Gi1/0/10
 732    003a.9c3f.d7c1    DYNAMIC     Po30
 732    003a.9c40.0dc1    DYNAMIC     Po30
 732    34ed.1bc4.2dec    DYNAMIC     Po30
 732    7018.a722.fab5    DYNAMIC     Po30
 341    0000.0c9f.f155    DYNAMIC     Po30
 341    0001.0554.1ca2    DYNAMIC     Po30
 341    0001.3e03.7ab7    DYNAMIC     Po30
 341    0001.3e03.7b28    DYNAMIC     Po30
 341    0001.3e03.7c98    DYNAMIC     Po30
           341    0001.3e03.9ca0    DYNAMIC     Po30
 341    0001.f08f.3020    DYNAMIC     Po30
 341    0001.f08f.3036    DYNAMIC     Po30
 341    0001.f091.eed4    DYNAMIC     Po30
 341    0001.f091.f142    DYNAMIC     Gi1/0/17
 341    0020.4afc.4c51    DYNAMIC     Po30
 341    003a.9c3f.d7c1    DYNAMIC     Po30
 341    003a.9c40.0dc1    DYNAMIC     Po30
 341    0040.9d2c.dac5    DYNAMIC     Po30
 341    0040.ae08.4bbc    DYNAMIC     Po30
 341    0040.ae11.7bdc    DYNAMIC     Gi1/0/14
 341    0090.3329.78d5    DYNAMIC     Po30
 341    00d0.c9c1.2fc2    DYNAMIC     Po30
 341    00d0.c9c1.2fce    DYNAMIC     Po30
 341    00d0.c9c1.577e    DYNAMIC     Po30
 341    00d0.c9c7.bba5    DYNAMIC     Po30
 341    1862.e4cd.30c2    DYNAMIC     Po30
 341    88d7.f6c2.bd3d    DYNAMIC     Po30
 341    9070.656a.a15d    DYNAMIC     Po30
 341    9070.65c4.8f88    DYNAMIC     Po30
 341    9070.65d3.a551    DYNAMIC     Po30
 341    c4f3.126d.5cfc    DYNAMIC     Po30
 418    0000.0c9f.f1a2    DYNAMIC     Po30
 418    003a.9c3f.d7c1    DYNAMIC     Po30
 418    003a.9c40.0dc1    DYNAMIC     Po30
 418    502f.a8f3.0d79    DYNAMIC     Gi1/0/18
1112    0000.0c9f.f458    DYNAMIC     Po30
1112    0016.2511.b77e    DYNAMIC     Po30
1112    0016.2511.cfe6    DYNAMIC     Po30
1112    0016.2511.d059    DYNAMIC     Po30
1112    0016.2511.d05f    DYNAMIC     Po30
1112    0016.2511.d061    DYNAMIC     Po30
1112    0016.2511.d080    DYNAMIC     Po30
1112    0016.2511.d716    DYNAMIC     Po30
1112    0016.2511.d72a    DYNAMIC     Gi1/0/20
1112    0016.2511.e36c    DYNAMIC     Po30
1112    0016.2511.e375    DYNAMIC     Po30
1112    0016.2511.e3a6    DYNAMIC     Po30
1112    0016.2511.e478    DYNAMIC     Po30
1112    0016.2511.e5d1    DYNAMIC     Po30
1112    0016.2511.e5e1    DYNAMIC     Po30
1112    0024.dd01.427a    DYNAMIC     Po30
1112    0024.dd01.4287    DYNAMIC     Po30
1112    003a.9c3f.d7c1    DYNAMIC     Po30
1112    003a.9c40.0dc1    DYNAMIC     Po30
1112    34ed.1bc4.2dec    DYNAMIC     Po30
1112    7018.a722.fab5    DYNAMIC     Po30
 396    0000.0c9f.f18c    DYNAMIC     Po30
 396    0007.4d41.af5a    DYNAMIC     Po30
 396    0007.4d41.af5d    DYNAMIC     Po30
 396    0007.4d41.af5e    DYNAMIC     Po30
 396    0007.4d41.b106    DYNAMIC     Po30
 396    0007.4d41.b119    DYNAMIC     Po30
 396    0007.4d42.c727    DYNAMIC     Po30
 396    0007.4d42.d49f    DYNAMIC     Po30
 396    0007.4d42.d4b9    DYNAMIC     Gi1/0/35
 396    0007.4d42.d4c8    DYNAMIC     Po30
 396    0007.4d43.3969    DYNAMIC     Po30
 396    0007.4d43.396c    DYNAMIC     Po30
           396    0007.4d43.e2fc    DYNAMIC     Po30
 396    0007.4d44.ae8c    DYNAMIC     Po30
 396    0007.4d44.af5c    DYNAMIC     Po30
 396    0007.4d44.b9a6    DYNAMIC     Gi1/0/32
 396    0007.4d47.08b1    DYNAMIC     Po30
 396    0007.4d47.2768    DYNAMIC     Po30
 396    0007.4d47.532e    DYNAMIC     Po30
 396    0007.4d47.93a7    DYNAMIC     Po30
 396    0007.4d4a.649e    DYNAMIC     Po30
 396    0007.4d4a.689a    DYNAMIC     Po30
 396    0007.4d4a.6fdc    DYNAMIC     Po30
 396    0007.4d4a.e6e7    DYNAMIC     Po30
 396    0007.4d4a.e749    DYNAMIC     Po30
 396    0007.4d4b.b379    DYNAMIC     Po30
 396    0007.4d4b.b3c5    DYNAMIC     Po30
 396    0007.4d4b.b622    DYNAMIC     Po30
 396    0007.4d4b.b630    DYNAMIC     Po30
 396    0007.4d4b.b637    DYNAMIC     Po30
 396    0007.4d4b.b66f    DYNAMIC     Po30
 396    0007.4d4b.b7ea    DYNAMIC     Po30
 396    0007.4d54.770b    DYNAMIC     Po30
 396    0007.4d54.ba16    DYNAMIC     Po30
 396    0007.4d57.25b3    DYNAMIC     Po30
 396    0007.4d5b.d34b    DYNAMIC     Po30
 396    0007.4d61.ffce    DYNAMIC     Po30
 396    0007.4d62.0311    DYNAMIC     Po30
 396    0007.4d66.3a5b    DYNAMIC     Po30
 396    0007.4d6b.f276    DYNAMIC     Gi1/0/25
 396    0007.4d6b.f69b    DYNAMIC     Po30
 396    0007.4d6c.7da9    DYNAMIC     Po30
 396    0007.4d6e.ee1e    DYNAMIC     Po30
 396    0007.4d6e.f07d    DYNAMIC     Po30
 396    0007.4d73.d969    DYNAMIC     Po30
 396    0007.4d76.144d    DYNAMIC     Po30
 396    0007.4d7a.a849    DYNAMIC     Po30
 396    0007.4d7c.dd91    DYNAMIC     Po30
 396    0007.4d86.6037    DYNAMIC     Po30
 396    0007.4d8e.aa31    DYNAMIC     Po30
 396    0007.4d93.d09b    DYNAMIC     Po30
 396    0007.4d95.0774    DYNAMIC     Po30
 396    0007.4d95.07b2    DYNAMIC     Po30
 396    0007.4d95.3ca9    DYNAMIC     Po30
 396    0007.4d96.689c    DYNAMIC     Po30
 396    0007.4d96.bda4    DYNAMIC     Po30
 396    0007.4d96.dd4c    DYNAMIC     Po30
 396    0007.4da6.5065    DYNAMIC     Po30
 396    0007.4da6.50f6    DYNAMIC     Po30
 396    0007.4da6.6f4f    DYNAMIC     Po30
 396    0007.4da7.e2dc    DYNAMIC     Po30
 396    0007.4dad.e959    DYNAMIC     Po30
 396    000c.c601.aeb8    DYNAMIC     Gi1/0/33
 396    000c.c601.aebc    DYNAMIC     Po30
 396    000c.c601.b16a    DYNAMIC     Po30
 396    000c.c601.b8da    DYNAMIC     Po30
 396    000c.c603.0e0c    DYNAMIC     Po30
 396    000e.7fdf.0953    DYNAMIC     Po30
 396    0011.0af0.065c    DYNAMIC     Po30
 396    0011.0af2.d149    DYNAMIC     Po30
 396    0012.7980.8869    DYNAMIC     Po30
           396    0012.7982.ac16    DYNAMIC     Po30
 396    0013.21be.cf7e    DYNAMIC     Po30
 396    0017.088e.d1d1    DYNAMIC     Po30
 396    0018.fea0.c29d    DYNAMIC     Po30
 396    001a.4b26.2d2c    DYNAMIC     Po30
 396    001b.781d.457d    DYNAMIC     Po30
 396    001b.78e5.5eab    DYNAMIC     Po30
 396    001b.78e6.64fe    DYNAMIC     Po30
 396    001b.78ef.83fc    DYNAMIC     Po30
 396    001e.0b15.fe1f    DYNAMIC     Po30
 396    0021.5a7d.d895    DYNAMIC     Po30
 396    0021.5a7d.d897    DYNAMIC     Po30
 396    0021.5a7d.d8d9    DYNAMIC     Po30
 396    0021.5a7d.d8e8    DYNAMIC     Po30
 396    0021.5a7f.1882    DYNAMIC     Po30
 396    0021.5a7f.41c7    DYNAMIC     Po30
 396    0021.5a8b.4b6c    DYNAMIC     Po30
 396    0021.5a90.111e    DYNAMIC     Po30
 396    0021.5a94.b681    DYNAMIC     Po30
 396    0023.7d84.0b14    DYNAMIC     Po30
 396    0023.7d8c.2531    DYNAMIC     Po30
 396    0023.7d8c.2587    DYNAMIC     Po30
 396    0025.b3eb.438d    DYNAMIC     Po30
 396    0025.b3f6.cd8f    DYNAMIC     Po30
 396    003a.9c3f.d7c1    DYNAMIC     Po30
 396    003a.9c40.0dc1    DYNAMIC     Po30
 396    0040.9d69.6fc4    DYNAMIC     Po30
 396    0068.eb81.1b35    DYNAMIC     Po30
 396    040e.3c0b.eb99    DYNAMIC     Po30
 396    040e.3c6c.3838    DYNAMIC     Po30
 396    040e.3ce8.1fcd    DYNAMIC     Po30
 396    082e.5fb9.3e3f    DYNAMIC     Po30
 396    082e.5fb9.c88d    DYNAMIC     Po30
 396    082e.5fbb.bfe5    DYNAMIC     Po30
 396    082e.5fbc.c3d3    DYNAMIC     Po30
 396    101f.7444.74e8    DYNAMIC     Po30
 396    1060.4b14.2a0c    DYNAMIC     Po30
 396    1060.4b14.2a1f    DYNAMIC     Po30
 396    1458.d03c.c922    DYNAMIC     Po30
 396    18a9.05ff.c3e9    DYNAMIC     Po30
 396    2426.4206.fa83    DYNAMIC     Po30
 396    24be.05e9.0c26    DYNAMIC     Po30
 396    2c27.d711.0bb4    DYNAMIC     Po30
 396    2c44.fd05.30ef    DYNAMIC     Po30
 396    2c44.fd05.30f8    DYNAMIC     Po30
 396    2c44.fd05.c83c    DYNAMIC     Po30
 396    2c44.fd06.9637    DYNAMIC     Po30
 396    2c59.e575.66a4    DYNAMIC     Gi1/0/31
 396    2c59.e5d4.4e0f    DYNAMIC     Po30
 396    2c59.e5d5.533b    DYNAMIC     Po30
 396    2c76.8a3e.08fc    DYNAMIC     Po30
 396    2c76.8a3e.08fe    DYNAMIC     Po30
 396    2c76.8a3e.1801    DYNAMIC     Po30
 396    2c76.8a3e.1802    DYNAMIC     Po30
 396    2c76.8a3e.1806    DYNAMIC     Po30
 396    2c76.8a3e.1f2d    DYNAMIC     Po30
 396    2c76.8a3e.1f30    DYNAMIC     Po30
 396    2c76.8a3e.62e7    DYNAMIC     Po30
 396    2c76.8a3e.bef0    DYNAMIC     Po30
           396    2c76.8a3e.bef6    DYNAMIC     Po30
 396    2c76.8a3e.ce5e    DYNAMIC     Po30
 396    2c76.8a3e.ce62    DYNAMIC     Po30
 396    2c76.8a3e.ce66    DYNAMIC     Po30
 396    2c76.8a3e.ce78    DYNAMIC     Po30
 396    2c76.8a41.df94    DYNAMIC     Po30
 396    3024.a9f7.0207    DYNAMIC     Po30
 396    30e1.713d.c457    DYNAMIC     Po30
 396    30e1.71bd.b001    DYNAMIC     Po30
 396    3464.a968.515c    DYNAMIC     Po30
 396    3464.a96d.3ee6    DYNAMIC     Po30
 396    34ed.1bc4.2dec    DYNAMIC     Po30
 396    3822.e2f8.3953    DYNAMIC     Po30
 396    3822.e2fe.131d    DYNAMIC     Po30
 396    3822.e2ff.0c60    DYNAMIC     Po30
 396    3863.bb04.79b3    DYNAMIC     Po30
 396    3863.bbde.b220    DYNAMIC     Po30
 396    38ea.a76c.7a04    DYNAMIC     Po30
 396    3c4a.9243.9f3b    DYNAMIC     Po30
 396    3c4a.9243.9f41    DYNAMIC     Po30
 396    3c52.82bd.cb4e    DYNAMIC     Po30
 396    3ca8.2a02.2fc7    DYNAMIC     Po30
 396    3ca8.2a06.d2e8    DYNAMIC     Po30
 396    3ca8.2a07.f68d    DYNAMIC     Po30
 396    3ca8.2af5.9c9c    DYNAMIC     Po30
 396    3cd9.2b0e.1f1f    DYNAMIC     Po30
 396    40a8.f0b5.64ac    DYNAMIC     Po30
 396    40b0.3426.8a0c    DYNAMIC     Po30
 396    441e.a132.0361    DYNAMIC     Po30
 396    441e.a133.0486    DYNAMIC     Po30
 396    441e.a135.3d56    DYNAMIC     Po30
 396    441e.a135.3d62    DYNAMIC     Po30
 396    441e.a135.3d6f    DYNAMIC     Po30
 396    441e.a135.3d71    DYNAMIC     Po30
 396    441e.a135.3d81    DYNAMIC     Po30
 396    441e.a135.3dad    DYNAMIC     Po30
 396    480f.cfc8.5c46    DYNAMIC     Po30
 396    480f.cfc8.6c1f    DYNAMIC     Po30
 396    480f.cfe8.71d9    DYNAMIC     Po30
 396    480f.cff9.32ca    DYNAMIC     Po30
 396    503d.e583.2cff    DYNAMIC     Po30
 396    5065.f35a.83d7    DYNAMIC     Po30
 396    5820.b14d.2a0c    DYNAMIC     Po30
 396    5820.b14d.6c58    DYNAMIC     Po30
 396    5820.b150.a32c    DYNAMIC     Po30
 396    5820.b150.c32c    DYNAMIC     Po30
 396    5820.b150.c343    DYNAMIC     Po30
 396    5820.b150.c344    DYNAMIC     Po30
 396    5820.b150.c396    DYNAMIC     Po30
 396    5820.b150.c3ba    DYNAMIC     Po30
 396    5820.b150.daae    DYNAMIC     Po30
 396    5ca6.2d2d.32fc    DYNAMIC     Po30
 396    5cb9.010e.0358    DYNAMIC     Po30
 396    5cb9.0111.bdd5    DYNAMIC     Po30
 396    5cb9.0111.bf85    DYNAMIC     Po30
 396    5cb9.0112.b03a    DYNAMIC     Po30
 396    6451.0624.07f3    DYNAMIC     Po30
 396    68ab.8a82.0ca6    DYNAMIC     Po30
 396    68ab.8a82.6522    DYNAMIC     Po30
           396    68ab.8a82.93e8    DYNAMIC     Po30
 396    6c02.e0f5.e50f    DYNAMIC     Po30
 396    6c2b.5953.a6a4    DYNAMIC     Po30
 396    6c2b.5964.e27d    DYNAMIC     Po30
 396    6c3b.e508.400d    DYNAMIC     Gi1/0/29
 396    6c3b.e508.62c8    DYNAMIC     Po30
 396    6c3b.e508.62cf    DYNAMIC     Po30
 396    6c3b.e509.5045    DYNAMIC     Po30
 396    6cc2.1722.1a3c    DYNAMIC     Po30
 396    7018.a722.fab5    DYNAMIC     Po30
 396    705a.0fa4.2ccb    DYNAMIC     Po30
 396    7446.a04c.d33b    DYNAMIC     Po30
 396    7446.a052.1704    DYNAMIC     Gi1/0/34
 396    7446.a052.177c    DYNAMIC     Gi1/0/36
 396    781c.5a60.2b13    DYNAMIC     Po30
 396    78ac.c082.e3bd    DYNAMIC     Po30
 396    78e3.b5f7.5764    DYNAMIC     Po30
 396    80c1.6e94.4937    DYNAMIC     Po30
 396    80e8.2c7e.2333    DYNAMIC     Po30
 396    842a.fd79.a5db    DYNAMIC     Po30
 396    842a.fd79.b515    DYNAMIC     Po30
 396    8851.fbea.ccb1    DYNAMIC     Po30
 396    8851.fbeb.3fda    DYNAMIC     Po30
 396    8851.fbeb.4f84    DYNAMIC     Po30
 396    8851.fbeb.7fa5    DYNAMIC     Po30
 396    8851.fbec.42d9    DYNAMIC     Po30
 396    8851.fbec.42e3    DYNAMIC     Po30
 396    8cdc.d45d.429d    DYNAMIC     Po30
 396    8cdc.d45d.c496    DYNAMIC     Po30
 396    9457.a515.beef    DYNAMIC     Po30
 396    9457.a5d1.bf45    DYNAMIC     Po30
 396    984b.e13e.0d8c    DYNAMIC     Po30
 396    98e7.f4a3.406d    DYNAMIC     Po30
 396    98e7.f4a3.9755    DYNAMIC     Po30
 396    98e7.f4a6.05f6    DYNAMIC     Po30
 396    98e7.f4a6.f061    DYNAMIC     Po30
 396    9c7b.ef85.8df6    DYNAMIC     Po30
 396    9c8e.9985.4cb6    DYNAMIC     Po30
 396    9cb6.541b.d595    DYNAMIC     Po30
 396    a08c.fd17.2ffb    DYNAMIC     Po30
 396    a08c.fd62.ac41    DYNAMIC     Po30
 396    a08c.fde6.f43f    DYNAMIC     Po30
 396    a0b3.cc9a.a572    DYNAMIC     Po30
 396    a0b3.cc9a.b458    DYNAMIC     Po30
 396    a0b3.cc9a.b4c4    DYNAMIC     Po30
 396    a0b3.cc9a.b4e3    DYNAMIC     Po30
 396    a0b3.cc9a.c41e    DYNAMIC     Po30
 396    a0b3.cc9a.c4db    DYNAMIC     Po30
 396    a0b3.cc9e.b460    DYNAMIC     Po30
 396    a0b3.cc9f.e23a    DYNAMIC     Gi1/0/26
 396    a0d3.c17f.c88a    DYNAMIC     Po30
 396    a0d3.c181.9c7b    DYNAMIC     Po30
 396    ac16.2d39.857e    DYNAMIC     Po30
 396    ace2.d349.6c59    DYNAMIC     Po30
 396    b00c.d1e3.5e38    DYNAMIC     Po30
 396    b05a.dac1.8345    DYNAMIC     Po30
 396    b05a.dac2.c21c    DYNAMIC     Po30
 396    b4b5.2ff7.b9ff    DYNAMIC     Po30
 396    b4b5.2ff8.a375    DYNAMIC     Gi1/0/28
           396    b4b5.2ff8.db8b    DYNAMIC     Po30
 396    b4b6.8604.1551    DYNAMIC     Po30
 396    b4b6.86c4.7b1c    DYNAMIC     Po30
 396    b4b6.86c8.44e0    DYNAMIC     Po30
 396    bce9.2fd1.182a    DYNAMIC     Po30
 396    bce9.2fd1.1836    DYNAMIC     Po30
 396    bce9.2fd1.184a    DYNAMIC     Po30
 396    bce9.2fd1.2b2a    DYNAMIC     Po30
 396    bce9.2fd2.2fff    DYNAMIC     Po30
 396    bce9.2fd2.5fc3    DYNAMIC     Po30
 396    bce9.2fd2.5fd5    DYNAMIC     Po30
 396    bce9.2fd2.5fd7    DYNAMIC     Po30
 396    bce9.2fd2.5fe5    DYNAMIC     Po30
 396    bce9.2fd2.bba0    DYNAMIC     Po30
 396    bce9.2fd2.db2e    DYNAMIC     Po30
 396    bce9.2fd3.8e45    DYNAMIC     Po30
 396    bce9.2fd3.8e47    DYNAMIC     Po30
 396    bce9.2fd4.1676    DYNAMIC     Po30
 396    bce9.2fd4.492b    DYNAMIC     Po30
 396    bce9.2fd4.67b5    DYNAMIC     Po30
 396    bce9.2fd4.86f8    DYNAMIC     Po30
 396    bce9.2fd4.96ba    DYNAMIC     Po30
 396    bce9.2fd4.96ca    DYNAMIC     Po30
 396    bce9.2fd4.96e4    DYNAMIC     Po30
 396    bce9.2fd4.96ec    DYNAMIC     Po30
 396    bce9.2fd4.96ee    DYNAMIC     Po30
 396    bce9.2fd4.96f0    DYNAMIC     Po30
 396    bce9.2fd4.a604    DYNAMIC     Po30
 396    bce9.2fd4.a678    DYNAMIC     Po30
 396    bce9.2fd4.c6a0    DYNAMIC     Po30
 396    bce9.2fd4.d8aa    DYNAMIC     Po30
 396    bce9.2fd4.d8be    DYNAMIC     Po30
 396    bce9.2fd4.d8d8    DYNAMIC     Po30
 396    bce9.2fd4.f806    DYNAMIC     Po30
 396    bce9.2fd7.09b8    DYNAMIC     Po30
 396    bce9.2fd7.09c0    DYNAMIC     Po30
 396    bce9.2fd7.09c6    DYNAMIC     Po30
 396    bce9.2fd7.09c8    DYNAMIC     Po30
 396    bce9.2fd7.09d0    DYNAMIC     Po30
 396    bce9.2fd7.a910    DYNAMIC     Po30
 396    bce9.2fd7.f863    DYNAMIC     Po30
 396    bce9.2fd7.f883    DYNAMIC     Po30
 396    c434.6b1a.a5a8    DYNAMIC     Po30
 396    c8cb.b861.ec36    DYNAMIC     Po30
 396    c8cb.b863.2b9a    DYNAMIC     Gi1/0/27
 396    c8d3.ff0f.d6c6    DYNAMIC     Po30
 396    c8d9.d2cf.77ef    DYNAMIC     Po30
 396    d0bf.9c30.79dc    DYNAMIC     Po30
 396    d0bf.9c36.841a    DYNAMIC     Po30
 396    dc4a.3e69.8f48    DYNAMIC     Po30
 396    dc4a.3eb2.ce7f    DYNAMIC     Po30
 396    dc4a.3eb3.9cd7    DYNAMIC     Gi1/0/30
 396    e839.358d.4df3    DYNAMIC     Po30
 396    e839.358d.81db    DYNAMIC     Po30
 396    e839.358d.f1a6    DYNAMIC     Po30
 396    e839.358e.30f0    DYNAMIC     Po30
 396    e8d8.d196.d68d    DYNAMIC     Po30
 396    e8d8.d1e5.8934    DYNAMIC     Po30
 396    ec8e.b525.79bd    DYNAMIC     Po30
           396    ec8e.b526.793e    DYNAMIC     Po30
 396    ec8e.b5bc.2b13    DYNAMIC     Po30
 396    ecb1.d7f8.0df7    DYNAMIC     Po30
 396    f092.1c61.7307    DYNAMIC     Po30
 396    f092.1c61.730f    DYNAMIC     Po30
 396    f092.1c61.87a2    DYNAMIC     Po30
 396    f092.1c62.ed7e    DYNAMIC     Po30
 396    f092.1c62.ed8a    DYNAMIC     Po30
 396    f092.1c62.ed8d    DYNAMIC     Po30
 396    f092.1c62.ed8e    DYNAMIC     Po30
 396    f092.1c62.fd4d    DYNAMIC     Po30
 396    f430.b971.658a    DYNAMIC     Po30
 396    f430.b973.d281    DYNAMIC     Po30
 396    f80d.acd5.b352    DYNAMIC     Po30
 396    f80d.acd7.5dc5    DYNAMIC     Po30
 396    f80d.acd7.5dcb    DYNAMIC     Po30
 396    f80d.acd7.5dd1    DYNAMIC     Po30
 396    f80d.acd7.5dd9    DYNAMIC     Po30
 396    fc3f.db50.0c1c    DYNAMIC     Po30
 396    fc3f.db51.506a    DYNAMIC     Po30
 396    fc3f.dbbd.1d43    DYNAMIC     Po30
 396    fc3f.dbbe.4bc9    DYNAMIC     Po30
 396    fc3f.dbbe.8f7c    DYNAMIC     Po30
 396    fc3f.dbbf.1fc2    DYNAMIC     Po30
 396    fc3f.dbc3.a733    DYNAMIC     Po30
 607    0000.0c9f.f25f    DYNAMIC     Po30
 607    0024.ae03.4c80    DYNAMIC     Po30
 607    003a.9c3f.d7c1    DYNAMIC     Po30
 607    003a.9c40.0dc1    DYNAMIC     Po30
 607    0050.f900.3caf    DYNAMIC     Po30
 607    0050.f900.8bf4    DYNAMIC     Po30
 607    0050.f900.a503    DYNAMIC     Gi1/0/2
 607    0050.f900.a50b    DYNAMIC     Gi1/0/1
 607    0050.f900.d1eb    DYNAMIC     Po30
 607    0050.f901.5cf7    DYNAMIC     Po30
 607    34ed.1bc4.2dec    DYNAMIC     Po30
 771    0000.0c9f.f303    DYNAMIC     Po30
 771    001d.9722.0350    DYNAMIC     Po30
 771    003a.9c3f.d7c1    DYNAMIC     Po30
 771    003a.9c40.0dc1    DYNAMIC     Po30
 771    10e7.c623.2810    DYNAMIC     Po30
 771    10e7.c630.0675    DYNAMIC     Po30
 771    34ed.1bc4.2dec    DYNAMIC     Po30
 771    40a8.f041.2cf4    DYNAMIC     Po30
 771    40a8.f041.2cf6    DYNAMIC     Po30
 771    40a8.f045.5fb4    DYNAMIC     Po30
 771    40a8.f046.addc    DYNAMIC     Po30
 771    480f.cf4e.3cd5    DYNAMIC     Po30
 771    480f.cf5e.6ef2    DYNAMIC     Po30
 771    6c2b.5954.2d1c    DYNAMIC     Gi1/0/8
 771    6c2b.59d4.23db    DYNAMIC     Po30
 771    6c2b.59d4.dff9    DYNAMIC     Po30
 771    6c2b.59d4.e672    DYNAMIC     Po30
 771    705a.0f48.3bd1    DYNAMIC     Po30
 771    8cdc.d44d.8495    DYNAMIC     Po30
 771    8cec.4bc7.9dc2    DYNAMIC     Po30
 771    9457.a5ec.b9f1    DYNAMIC     Po30
 771    94de.806d.f00b    DYNAMIC     Po30
 771    a08c.fdcb.ea38    DYNAMIC     Po30
           771    a4bb.6dcf.9656    DYNAMIC     Po30
 771    b06e.bf0a.a210    DYNAMIC     Po30
 771    b42e.9969.4676    DYNAMIC     Po30
 771    b42e.99ad.531a    DYNAMIC     Po30
 771    b827.eb72.2776    DYNAMIC     Po30
 771    c434.6b79.b7db    DYNAMIC     Po30
 771    c434.6b79.bc03    DYNAMIC     Po30
 771    c434.6b7a.eedb    DYNAMIC     Po30
 771    c434.6b7a.eede    DYNAMIC     Po30
 771    c434.6b7d.88fd    DYNAMIC     Po30
 771    c8d3.ffb5.44fa    DYNAMIC     Po30
 771    c8d9.d209.6373    DYNAMIC     Po30
 771    dc4a.3e6b.8f8f    DYNAMIC     Po30
 771    dc4a.3e6c.0085    DYNAMIC     Po30
 771    dc4a.3e74.fc9b    DYNAMIC     Po30
 771    dc4a.3e86.97e2    DYNAMIC     Po30
 771    dc4a.3e9b.c3cd    DYNAMIC     Po30
 771    e0d5.5eb5.e975    DYNAMIC     Po30
 771    e0d5.5ed9.e88d    DYNAMIC     Po30
 771    e454.e84e.8120    DYNAMIC     Po30
 771    e454.e84e.b49c    DYNAMIC     Po30
 771    e454.e876.8376    DYNAMIC     Po30
 771    e454.e876.eb0a    DYNAMIC     Po30
 771    e454.e876.eceb    DYNAMIC     Po30
 771    e454.e876.f492    DYNAMIC     Po30
 771    e454.e877.017b    DYNAMIC     Po30
 771    e454.e877.04e4    DYNAMIC     Po30
 771    e454.e89b.930b    DYNAMIC     Po30
 771    e454.e89b.cad7    DYNAMIC     Po30
 771    e454.e8a4.9115    DYNAMIC     Po30
 771    e454.e8a5.af36    DYNAMIC     Po30
 771    e454.e8b2.1424    DYNAMIC     Po30
 771    e454.e8b2.16b3    DYNAMIC     Po30
 771    e454.e8b2.1af7    DYNAMIC     Po30
 771    e454.e8b2.529c    DYNAMIC     Po30
 771    e454.e8bf.b4e8    DYNAMIC     Po30
 771    e454.e8bf.b50a    DYNAMIC     Po30
 771    e454.e8bf.b52a    DYNAMIC     Po30
 771    e454.e8c0.d0e4    DYNAMIC     Po30
 771    e454.e8d9.1ab7    DYNAMIC     Po30
 771    e454.e8da.9e92    DYNAMIC     Po30
 771    e454.e8db.6eff    DYNAMIC     Po30
 771    e454.e8dc.641d    DYNAMIC     Po30
 771    e4b9.7af9.c7ad    DYNAMIC     Po30
 771    f018.98e8.f4e6    DYNAMIC     Po30
 771    f018.98f2.e9b7    DYNAMIC     Po30
1037    0000.0c9f.f40d    DYNAMIC     Po30
1037    000b.86c0.b6fe    DYNAMIC     Po30
1037    000b.86c4.9060    DYNAMIC     Po30
1037    0027.9048.1320    DYNAMIC     Po30
1037    0027.9048.1f80    DYNAMIC     Gi1/0/40
1037    0027.9048.1f90    DYNAMIC     Gi1/0/39
1037    003a.9c3f.d7c1    DYNAMIC     Po30
1037    003a.9c40.0dc1    DYNAMIC     Po30
1037    006b.f125.c708    DYNAMIC     Po30
1037    006b.f125.c7b6    DYNAMIC     Po30
1037    006b.f125.cb8c    DYNAMIC     Po30
1037    006b.f125.cb9a    DYNAMIC     Po30
1037    006b.f125.cc2e    DYNAMIC     Po30
          1037    006b.f125.cf4e    DYNAMIC     Po30
1037    006b.f125.d0aa    DYNAMIC     Po30
1037    006b.f125.d3b4    DYNAMIC     Po30
1037    006b.f125.d3c2    DYNAMIC     Po30
1037    006b.f125.d3da    DYNAMIC     Po30
1037    006b.f125.d3dc    DYNAMIC     Po30
1037    006b.f125.d3fc    DYNAMIC     Po30
1037    006b.f125.d412    DYNAMIC     Po30
1037    006b.f125.d54c    DYNAMIC     Po30
1037    006b.f125.d730    DYNAMIC     Po30
1037    006b.f125.d744    DYNAMIC     Po30
1037    006b.f125.d784    DYNAMIC     Po30
1037    006b.f125.d79e    DYNAMIC     Po30
1037    006b.f125.d882    DYNAMIC     Po30
1037    006b.f125.d8a2    DYNAMIC     Po30
1037    0081.c424.1d04    DYNAMIC     Po30
1037    0081.c467.0fba    DYNAMIC     Po30
1037    0081.c467.1ffe    DYNAMIC     Po30
1037    00d7.8f1e.b5d0    DYNAMIC     Po30
1037    00d7.8f1e.b608    DYNAMIC     Po30
1037    00d7.8f1e.bf38    DYNAMIC     Po30
1037    00d7.8f1e.bf78    DYNAMIC     Po30
1037    00d7.8fa6.e7fc    DYNAMIC     Po30
1037    00d7.8fa6.f336    DYNAMIC     Po30
1037    00d7.8fa6.f3a4    DYNAMIC     Po30
1037    00eb.d510.0d70    DYNAMIC     Gi1/0/41
1037    00eb.d510.5660    DYNAMIC     Gi1/0/43
1037    00ee.ab3f.5498    DYNAMIC     Po30
1037    00ee.ab3f.5ad0    DYNAMIC     Po30
1037    00ee.ab3f.5e38    DYNAMIC     Po30
1037    00ee.ab3f.5e68    DYNAMIC     Po30
1037    00ee.ab3f.5f08    DYNAMIC     Po30
1037    00ee.ab3f.5fb0    DYNAMIC     Po30
1037    00ee.ab3f.6168    DYNAMIC     Po30
1037    00ee.ab3f.6198    DYNAMIC     Po30
1037    00ee.ab3f.61a0    DYNAMIC     Po30
1037    00ee.ab3f.6298    DYNAMIC     Po30
1037    00ee.ab3f.7158    DYNAMIC     Po30
1037    00ee.ab3f.7238    DYNAMIC     Po30
1037    00ee.ab3f.72a8    DYNAMIC     Po30
1037    00ee.ab3f.72e8    DYNAMIC     Po30
1037    00ee.ab3f.7300    DYNAMIC     Po30
1037    00ee.ab3f.7318    DYNAMIC     Po30
1037    00ee.ab3f.7340    DYNAMIC     Po30
1037    00ee.ab3f.7350    DYNAMIC     Po30
1037    00ee.ab3f.7370    DYNAMIC     Po30
1037    00ee.ab3f.73a8    DYNAMIC     Po30
1037    00ee.ab3f.7420    DYNAMIC     Po30
1037    00ee.ab3f.7430    DYNAMIC     Po30
1037    00ee.ab3f.7470    DYNAMIC     Po30
1037    00ee.ab3f.7828    DYNAMIC     Po30
1037    00ee.ab3f.7870    DYNAMIC     Po30
1037    00ee.ab3f.7880    DYNAMIC     Po30
1037    00ee.ab3f.78f8    DYNAMIC     Po30
1037    00ee.ab3f.7908    DYNAMIC     Po30
1037    00ee.ab3f.7928    DYNAMIC     Po30
1037    00ee.ab3f.7ab0    DYNAMIC     Po30
1037    00ee.ab3f.7b68    DYNAMIC     Po30
1037    00ee.ab3f.7bf0    DYNAMIC     Po30
          1037    00ee.ab3f.7c88    DYNAMIC     Po30
1037    00ee.ab3f.7cd8    DYNAMIC     Po30
1037    00ee.ab3f.7cf0    DYNAMIC     Po30
1037    00ee.ab3f.7d08    DYNAMIC     Po30
1037    00ee.ab3f.7d30    DYNAMIC     Po30
1037    00ee.ab3f.7de8    DYNAMIC     Po30
1037    00ee.ab3f.7e08    DYNAMIC     Po30
1037    00ee.ab3f.7e68    DYNAMIC     Po30
1037    00ee.ab3f.7ec0    DYNAMIC     Po30
1037    00ee.ab3f.7f40    DYNAMIC     Po30
1037    00ee.ab3f.7f50    DYNAMIC     Po30
1037    00ee.ab3f.7f58    DYNAMIC     Po30
1037    00ee.ab3f.7f90    DYNAMIC     Po30
1037    00ee.ab3f.7fa8    DYNAMIC     Po30
1037    00ee.ab3f.8008    DYNAMIC     Po30
1037    00ee.ab3f.8090    DYNAMIC     Po30
1037    00ee.ab3f.80c8    DYNAMIC     Po30
1037    00ee.ab3f.80f8    DYNAMIC     Po30
1037    00ee.ab3f.8248    DYNAMIC     Po30
1037    00ee.ab3f.8328    DYNAMIC     Po30
1037    00ee.ab3f.84b8    DYNAMIC     Po30
1037    00ee.ab3f.8510    DYNAMIC     Po30
1037    00ee.ab3f.8558    DYNAMIC     Po30
1037    00ee.ab3f.8578    DYNAMIC     Po30
1037    00ee.ab3f.8580    DYNAMIC     Po30
1037    00ee.ab3f.85d8    DYNAMIC     Po30
1037    00ee.ab3f.8648    DYNAMIC     Po30
1037    00ee.ab3f.86e0    DYNAMIC     Po30
1037    00ee.ab3f.86f8    DYNAMIC     Po30
1037    00ee.ab3f.87b8    DYNAMIC     Po30
1037    00ee.ab3f.88e0    DYNAMIC     Po30
1037    00ee.ab3f.8908    DYNAMIC     Po30
1037    00ee.ab3f.8a38    DYNAMIC     Po30
1037    00ee.ab3f.8ad8    DYNAMIC     Po30
1037    00f6.634a.6020    DYNAMIC     Po30
1037    00f6.634a.69a6    DYNAMIC     Po30
1037    00f6.634a.69b4    DYNAMIC     Po30
1037    00f6.634a.69c4    DYNAMIC     Po30
1037    00f6.634a.69ca    DYNAMIC     Po30
1037    00f6.634a.69ce    DYNAMIC     Po30
1037    00f6.634a.69d8    DYNAMIC     Po30
1037    00f6.634a.69ee    DYNAMIC     Po30
1037    00f6.634a.6a78    DYNAMIC     Po30
1037    00f6.634a.6a84    DYNAMIC     Po30
1037    00f6.634a.6a86    DYNAMIC     Po30
1037    00f6.634a.6a9e    DYNAMIC     Po30
1037    0462.7381.8bd8    DYNAMIC     Po30
1037    0462.7383.5f90    DYNAMIC     Po30
1037    0462.73c7.d38c    DYNAMIC     Po30
1037    0462.73db.5ab4    DYNAMIC     Po30
1037    0462.73e1.f210    DYNAMIC     Po30
1037    0462.73e8.e024    DYNAMIC     Po30
1037    0462.73f0.cef4    DYNAMIC     Po30
1037    0462.73f0.cf60    DYNAMIC     Po30
1037    10b3.d5b0.a014    DYNAMIC     Po30
1037    10b3.d5b0.a2a6    DYNAMIC     Po30
1037    10b3.d5b6.071a    DYNAMIC     Po30
1037    10b3.d5bf.e006    DYNAMIC     Po30
1037    10b3.d5cb.645c    DYNAMIC     Po30
          1037    10b3.d5cb.6636    DYNAMIC     Po30
1037    10b3.d5cb.6642    DYNAMIC     Po30
1037    10b3.d5cb.6a0a    DYNAMIC     Po30
1037    10b3.d5e9.b8cc    DYNAMIC     Po30
1037    10b3.d6b3.a0f8    DYNAMIC     Po30
1037    10b3.d6b3.a10a    DYNAMIC     Po30
1037    10b3.d6b3.a312    DYNAMIC     Po30
1037    1880.902e.4aba    DYNAMIC     Gi1/0/42
1037    1880.902e.5f58    DYNAMIC     Po30
1037    2416.9dd9.eb00    DYNAMIC     Po30
1037    2416.9dd9.eb08    DYNAMIC     Po30
1037    2416.9dd9.eb7e    DYNAMIC     Gi1/0/48
1037    2416.9dd9.ebcc    DYNAMIC     Po30
1037    2416.9dd9.f0a0    DYNAMIC     Po30
1037    2416.9dd9.f0f6    DYNAMIC     Po30
1037    2416.9dd9.f110    DYNAMIC     Po30
1037    2416.9dd9.f126    DYNAMIC     Po30
1037    2416.9dd9.f136    DYNAMIC     Po30
1037    2416.9dd9.f200    DYNAMIC     Po30
1037    2416.9dd9.f2ac    DYNAMIC     Po30
1037    2416.9dd9.f2dc    DYNAMIC     Po30
1037    2416.9df5.09e6    DYNAMIC     Po30
1037    3890.a578.0156    DYNAMIC     Po30
1037    3890.a578.153e    DYNAMIC     Po30
1037    3890.a578.1782    DYNAMIC     Po30
1037    3890.a578.1ae6    DYNAMIC     Po30
1037    3c51.0e3d.e7c8    DYNAMIC     Po30
1037    3c51.0e3d.efa0    DYNAMIC     Po30
1037    3c51.0e3d.efae    DYNAMIC     Po30
1037    3c51.0e3d.efb8    DYNAMIC     Po30
1037    3c51.0e3d.eff0    DYNAMIC     Po30
1037    3c51.0e3d.f404    DYNAMIC     Po30
1037    3c51.0e3d.f414    DYNAMIC     Po30
1037    3c51.0e3d.f428    DYNAMIC     Po30
1037    3c51.0e3d.f430    DYNAMIC     Po30
1037    3c51.0e3d.f434    DYNAMIC     Po30
1037    3c51.0e3d.f436    DYNAMIC     Po30
1037    3c51.0e40.cf46    DYNAMIC     Po30
1037    3c51.0e49.db14    DYNAMIC     Po30
1037    3c51.0e49.e318    DYNAMIC     Po30
1037    3c51.0e60.5526    DYNAMIC     Po30
1037    3c51.0e60.631a    DYNAMIC     Po30
1037    3c51.0efa.5e64    DYNAMIC     Po30
1037    3c51.0efa.686e    DYNAMIC     Po30
1037    3c51.0efa.6880    DYNAMIC     Po30
1037    4c71.0d0f.1dd8    DYNAMIC     Po30
1037    4c71.0d0f.1f28    DYNAMIC     Po30
1037    4c71.0d0f.23d0    DYNAMIC     Po30
1037    4c71.0d0f.2e44    DYNAMIC     Po30
1037    4c71.0d33.8eca    DYNAMIC     Po30
1037    4c71.0d3d.9b2a    DYNAMIC     Po30
1037    4c71.0d3e.db20    DYNAMIC     Po30
1037    4c71.0d3e.db24    DYNAMIC     Po30
1037    4c71.0d3e.db6e    DYNAMIC     Po30
1037    4c71.0d3f.2010    DYNAMIC     Po30
1037    4c71.0d90.4fce    DYNAMIC     Po30
1037    4ce1.76b9.c324    DYNAMIC     Po30
1037    4ce1.76cb.49c0    DYNAMIC     Po30
1037    4ce1.76cb.50fc    DYNAMIC     Po30
          1037    4ce1.76cb.5116    DYNAMIC     Po30
1037    4ce1.76ef.e862    DYNAMIC     Po30
1037    500f.804a.06d4    DYNAMIC     Po30
1037    500f.8098.16a4    DYNAMIC     Po30
1037    500f.8098.1742    DYNAMIC     Po30
1037    502f.a8df.8b18    DYNAMIC     Po30
1037    503d.e583.2cff    DYNAMIC     Po30
1037    5ca6.2d2d.32c8    DYNAMIC     Po30
1037    5ca6.2d2d.32d2    DYNAMIC     Po30
1037    5ca6.2d2d.32dc    DYNAMIC     Po30
1037    5ca6.2d2d.32e2    DYNAMIC     Po30
1037    5ca6.2db6.f820    DYNAMIC     Po30
1037    5ca6.2db6.f882    DYNAMIC     Po30
1037    5ca6.2db6.f886    DYNAMIC     Po30
1037    5ca6.2db6.fbb8    DYNAMIC     Po30
1037    5ca6.2db6.fbca    DYNAMIC     Po30
1037    5ca6.2dd7.50d6    DYNAMIC     Po30
1037    5ca6.2dd7.50e0    DYNAMIC     Po30
1037    5ca6.2dd7.50e6    DYNAMIC     Po30
1037    5ca6.2dd7.50ec    DYNAMIC     Po30
1037    5ca6.2dd7.5132    DYNAMIC     Gi1/0/45
1037    5ca6.2dd7.56f0    DYNAMIC     Po30
1037    5ca6.2dd7.570c    DYNAMIC     Po30
1037    5ca6.2dd7.5714    DYNAMIC     Po30
1037    5ca6.2dd7.574e    DYNAMIC     Po30
1037    5ca6.2de6.3968    DYNAMIC     Po30
1037    5ca6.2de6.3976    DYNAMIC     Po30
1037    5ca6.2de6.397a    DYNAMIC     Gi1/0/46
1037    5ca6.2de6.397e    DYNAMIC     Po30
1037    5ca6.2de6.3984    DYNAMIC     Po30
1037    689e.0b9a.0b6a    DYNAMIC     Po30
1037    6c8b.d313.d40a    DYNAMIC     Po30
1037    7018.a722.fab5    DYNAMIC     Po30
1037    70b3.1713.adf8    DYNAMIC     Po30
1037    70db.981a.1ba4    DYNAMIC     Po30
1037    70df.2fa2.6afc    DYNAMIC     Po30
1037    70ea.1a6a.bd58    DYNAMIC     Po30
1037    70ea.1ae3.7ee0    DYNAMIC     Po30
1037    70ea.1ae3.87a0    DYNAMIC     Po30
1037    70ea.1ae3.87c8    DYNAMIC     Po30
1037    70ea.1ae3.8ab0    DYNAMIC     Po30
1037    70ea.1ae3.8b68    DYNAMIC     Po30
1037    70ea.1ae3.8bd8    DYNAMIC     Po30
1037    70ea.1ae3.8bf8    DYNAMIC     Po30
1037    70ea.1ae3.8d58    DYNAMIC     Po30
1037    70ea.1ae3.8e10    DYNAMIC     Po30
1037    70ea.1ae3.8e48    DYNAMIC     Po30
1037    70ea.1ae3.8fd8    DYNAMIC     Po30
1037    70ea.1ae3.9168    DYNAMIC     Po30
1037    70ea.1ae3.9200    DYNAMIC     Po30
1037    70ea.1ae3.9270    DYNAMIC     Po30
1037    70ea.1ae3.92c0    DYNAMIC     Po30
1037    70ea.1ae3.92e0    DYNAMIC     Po30
1037    70ea.1ae3.92e8    DYNAMIC     Po30
1037    70ea.1ae3.9578    DYNAMIC     Po30
1037    7872.5d1c.2c84    DYNAMIC     Po30
1037    7872.5d62.af70    DYNAMIC     Po30
1037    78ba.f993.483c    DYNAMIC     Po30
1037    80e0.1d3c.7608    DYNAMIC     Po30
          1037    84b2.61b0.4d04    DYNAMIC     Po30
1037    84b2.61b0.4e80    DYNAMIC     Po30
1037    84b2.61b9.80c8    DYNAMIC     Po30
1037    84b2.61bf.ab34    DYNAMIC     Po30
1037    84b8.02a4.6cc0    DYNAMIC     Po30
1037    84b8.02a7.bd94    DYNAMIC     Po30
1037    84b8.02b8.32c8    DYNAMIC     Po30
1037    88f0.3137.db08    DYNAMIC     Po30
1037    a023.9f66.123c    DYNAMIC     Po30
1037    a0b4.395d.85d0    DYNAMIC     Po30
1037    a0b4.395d.87bc    DYNAMIC     Po30
1037    a0b4.395d.8d10    DYNAMIC     Po30
1037    a0b4.3978.c188    DYNAMIC     Po30
1037    a0b4.3978.c1a0    DYNAMIC     Po30
1037    a0b4.3978.c1da    DYNAMIC     Po30
1037    a0b4.3978.c1ee    DYNAMIC     Po30
1037    a0b4.3978.d59c    DYNAMIC     Po30
1037    a0b4.3987.a772    DYNAMIC     Po30
1037    a0b4.3987.aa50    DYNAMIC     Po30
1037    a0b4.3987.b6ee    DYNAMIC     Po30
1037    a0b4.3987.b71a    DYNAMIC     Po30
1037    a0b4.3987.b71e    DYNAMIC     Po30
1037    a0b4.3987.c79c    DYNAMIC     Po30
1037    a0b4.398d.6886    DYNAMIC     Po30
1037    a0b4.398d.7234    DYNAMIC     Po30
1037    a0b4.398d.7266    DYNAMIC     Po30
1037    a0b4.398d.7864    DYNAMIC     Po30
1037    a0b4.398d.788c    DYNAMIC     Po30
1037    a0b4.398d.78b6    DYNAMIC     Po30
1037    a0b4.398d.78ba    DYNAMIC     Po30
1037    a0b4.39c5.79aa    DYNAMIC     Po30
1037    a0b4.39c5.79d4    DYNAMIC     Po30
1037    a0ec.f9fe.48cc    DYNAMIC     Po30
1037    a453.0ec4.1e40    DYNAMIC     Po30
1037    a89d.2155.e2c0    DYNAMIC     Po30
1037    a89d.2155.e350    DYNAMIC     Po30
1037    a89d.2164.2c98    DYNAMIC     Po30
1037    a89d.2169.e744    DYNAMIC     Po30
1037    a89d.2169.e7f0    DYNAMIC     Po30
1037    a89d.2169.e84c    DYNAMIC     Po30
1037    ac3a.673d.730e    DYNAMIC     Po30
1037    ac3a.673d.7380    DYNAMIC     Po30
1037    ac3a.6749.4576    DYNAMIC     Po30
1037    ac3a.6749.459a    DYNAMIC     Po30
1037    ac3a.6749.4bb4    DYNAMIC     Po30
1037    ac3a.6749.4be6    DYNAMIC     Po30
1037    ac3a.6749.4bf4    DYNAMIC     Po30
1037    ac3a.6749.4cd4    DYNAMIC     Po30
1037    ac3a.675e.6238    DYNAMIC     Po30
1037    ac3a.676b.e940    DYNAMIC     Po30
1037    ac3a.676b.ea5a    DYNAMIC     Po30
1037    ac3a.676b.eb08    DYNAMIC     Po30
1037    ac4a.676d.0d3e    DYNAMIC     Po30
1037    ac4a.676d.38f6    DYNAMIC     Po30
1037    ac4a.676d.3bf6    DYNAMIC     Po30
1037    ac4a.676d.3bfe    DYNAMIC     Po30
1037    ac4a.676d.3c1e    DYNAMIC     Po30
1037    ac4a.676d.3ca8    DYNAMIC     Po30
1037    ac7a.562b.7972    DYNAMIC     Po30
          1037    ac7a.562b.7986    DYNAMIC     Po30
1037    ac7a.562b.7cc4    DYNAMIC     Po30
1037    ac7a.562b.7cc8    DYNAMIC     Po30
1037    b026.80df.6246    DYNAMIC     Gi1/0/44
1037    b08b.cfa8.1584    DYNAMIC     Po30
1037    b08b.cfa8.169e    DYNAMIC     Po30
1037    b827.eb27.ddf1    DYNAMIC     Po30
1037    b827.eb28.2bc4    DYNAMIC     Po30
1037    b827.eb6d.fee8    DYNAMIC     Po30
1037    b827.eb93.a06a    DYNAMIC     Po30
1037    b827.ebd3.3ba2    DYNAMIC     Po30
1037    b827.ebef.d1c4    DYNAMIC     Gi1/0/37
1037    b827.ebf0.1ef6    DYNAMIC     Po30
1037    b827.ebfb.524f    DYNAMIC     Po30
1037    cc7f.761e.525e    DYNAMIC     Po30
1037    cc7f.761e.5278    DYNAMIC     Po30
1037    cc7f.7623.4ce6    DYNAMIC     Po30
1037    cc7f.7623.501a    DYNAMIC     Po30
1037    cc7f.7623.5028    DYNAMIC     Po30
1037    d46d.5091.e598    DYNAMIC     Po30
1037    d4c9.3c5a.16a0    DYNAMIC     Po30
1037    d4c9.3ce6.c2b8    DYNAMIC     Po30
1037    e41f.7b8c.1402    DYNAMIC     Po30
1037    e4aa.5d00.12fc    DYNAMIC     Gi1/0/24
1037    e4aa.5d6c.a120    DYNAMIC     Po30
1037    e4aa.5dd2.b500    DYNAMIC     Po30
1037    e4aa.5dd9.5fc0    DYNAMIC     Po30
1037    f4cf.e2ac.333c    DYNAMIC     Po30
1037    f4db.e6bf.e398    DYNAMIC     Po30
1037    f4db.e6bf.e548    DYNAMIC     Po30
1037    f4db.e6f4.a31c    DYNAMIC     Po30
1037    f4db.e6f4.a65a    DYNAMIC     Po30
1037    f4db.e6f4.aa3c    DYNAMIC     Po30
1037    f4db.e6f4.aacc    DYNAMIC     Po30
1037    f4db.e6f4.aad6    DYNAMIC     Po30
1037    f4db.e6f4.aae0    DYNAMIC     Po30
1037    f4db.e6f4.c188    DYNAMIC     Po30
1037    f4db.e6fa.6764    DYNAMIC     Po30
1037    f4db.e6fd.4660    DYNAMIC     Po30
1037    f4db.e6fd.46ac    DYNAMIC     Po30
1037    f4db.e6fd.46ba    DYNAMIC     Po30
1037    f4db.e6fd.46ee    DYNAMIC     Po30
1037    f4db.e6fd.4784    DYNAMIC     Po30
1037    f4db.e6ff.4160    DYNAMIC     Po30
1037    f4db.e6ff.418e    DYNAMIC     Po30
1037    f4db.e6ff.41ce    DYNAMIC     Po30
1037    f4db.e6ff.41da    DYNAMIC     Po30
1037    f4db.e6ff.41ec    DYNAMIC     Po30
1037    f4db.e6ff.41f4    DYNAMIC     Po30
1037    f4db.e6ff.4232    DYNAMIC     Po30
1037    f4db.e6ff.5294    DYNAMIC     Po30
1037    f4db.e6ff.52e6    DYNAMIC     Po30
1037    f4db.e6ff.552a    DYNAMIC     Po30
1037    f80b.cbfd.0d30    DYNAMIC     Po30
1037    f80b.cbfd.0d54    DYNAMIC     Po30
 600    0000.0c9f.f258    DYNAMIC     Po30
 600    0007.327d.187d    DYNAMIC     Po30
 600    003a.9c3f.d7c1    DYNAMIC     Po30
 600    003a.9c40.0dc1    DYNAMIC     Po30
           600    0060.e065.14fa    DYNAMIC     Po30
 600    0060.e065.150d    DYNAMIC     Po30
 600    0060.e065.159e    DYNAMIC     Po30
 600    0060.e065.15d4    DYNAMIC     Po30
 600    0060.e065.15d5    DYNAMIC     Po30
 600    0060.e065.15d7    DYNAMIC     Po30
 600    0060.e065.15da    DYNAMIC     Po30
 600    0060.e065.174c    DYNAMIC     Po30
 600    0060.e065.1750    DYNAMIC     Po30
 600    0060.e065.5f6e    DYNAMIC     Po30
 600    0060.e066.1367    DYNAMIC     Po30
 600    0060.e066.13e2    DYNAMIC     Po30
 600    0060.e066.8775    DYNAMIC     Po30
 600    0060.e066.87d3    DYNAMIC     Po30
 600    0060.e066.f71f    DYNAMIC     Po30
 600    0060.e066.f7e8    DYNAMIC     Po30
 600    0060.e06a.3b5b    DYNAMIC     Po30
 600    0060.e06a.3b5e    DYNAMIC     Gi1/0/16
 600    0cc4.7a91.26f8    DYNAMIC     Po30
 600    0cc4.7a91.2704    DYNAMIC     Po30
 600    0cc4.7a91.36dc    DYNAMIC     Po30
 600    0cc4.7a91.3814    DYNAMIC     Po30
 600    0cc4.7ac7.b960    DYNAMIC     Po30
 600    0cc4.7ac9.d7cc    DYNAMIC     Po30
 600    0cc4.7ac9.d7ce    DYNAMIC     Po30
 600    0cc4.7aca.ad90    DYNAMIC     Po30
 600    0cc4.7aca.ad9c    DYNAMIC     Po30
 600    0cc4.7aca.adae    DYNAMIC     Po30
 600    0cc4.7aca.ae1e    DYNAMIC     Gi1/0/15
 600    0cc4.7aca.ae3a    DYNAMIC     Po30
 600    0cc4.7aca.af8c    DYNAMIC     Po30
 600    503d.e583.2cff    DYNAMIC     Po30
 123    0000.0c9f.f07b    DYNAMIC     Po30
 123    003a.9c3f.d7c1    DYNAMIC     Po30
 123    003a.9c40.0dc1    DYNAMIC     Po30
 123    6c2b.5953.afb6    DYNAMIC     Gi7/0/24
 124    0000.0c9f.f07c    DYNAMIC     Po30
 124    003a.9c3f.d7c1    DYNAMIC     Po30
 125    0000.0c9f.f07d    DYNAMIC     Po30
 125    0020.4afb.fdd2    DYNAMIC     Po30
 125    003a.9c3f.d7c1    DYNAMIC     Po30
 125    003a.9c40.0dc1    DYNAMIC     Po30
 125    bce9.2fd4.a616    DYNAMIC     Po30
 126    0000.0c9f.f07e    DYNAMIC     Po30
 126    003a.9c3f.d7c1    DYNAMIC     Po30
 126    003a.9c40.0dc1    DYNAMIC     Po30
 126    34ed.1bc4.2dec    DYNAMIC     Po30
 126    6c2b.594d.22e6    DYNAMIC     Po30
 126    6c2b.594d.2613    DYNAMIC     Po30
 126    6c2b.594e.352b    DYNAMIC     Po30
 126    6c2b.5954.0d1a    DYNAMIC     Po30
 126    6c2b.5954.0f19    DYNAMIC     Po30
 126    6c2b.5954.12aa    DYNAMIC     Po30
 126    6c2b.5954.2ce7    DYNAMIC     Po30
 126    6c2b.5954.2d83    DYNAMIC     Po30
 126    6c2b.5954.2d8a    DYNAMIC     Po30
 126    6c2b.5962.dfea    DYNAMIC     Po30
 126    6c2b.5963.efcb    DYNAMIC     Po30
 126    6c2b.5963.f065    DYNAMIC     Po30
           126    6c2b.5967.29be    DYNAMIC     Po30
 126    6c2b.5967.2adf    DYNAMIC     Po30
 126    6c2b.5967.9505    DYNAMIC     Po30
 126    6c2b.5973.a807    DYNAMIC     Po30
 127    0000.0c9f.f07f    DYNAMIC     Po30
 127    003a.9c3f.d7c1    DYNAMIC     Po30
 127    003a.9c40.0dc1    DYNAMIC     Po30
 127    34ed.1bc4.2dec    DYNAMIC     Po30
 127    e454.e873.5972    DYNAMIC     Po30
 128    0000.0c9f.f080    DYNAMIC     Po30
 128    003a.9c3f.d7c1    DYNAMIC     Po30
 128    003a.9c40.0dc1    DYNAMIC     Po30
 128    34ed.1bc4.2dec    DYNAMIC     Po30
 130    0000.0c9f.f082    DYNAMIC     Po30
 130    003a.9c3f.d7c1    DYNAMIC     Po30
 130    003a.9c40.0dc1    DYNAMIC     Po30
 130    34ed.1bc4.2dec    DYNAMIC     Po30
 131    0000.0c9f.f083    DYNAMIC     Po30
 131    003a.9c3f.d7c1    DYNAMIC     Po30
 131    003a.9c40.0dc1    DYNAMIC     Po30
 131    34ed.1bc4.2dec    DYNAMIC     Po30
 132    0000.0c9f.f084    DYNAMIC     Po30
 132    003a.9c3f.d7c1    DYNAMIC     Po30
 132    003a.9c40.0dc1    DYNAMIC     Po30
 270    0000.0c9f.f10e    DYNAMIC     Po30
 270    003a.9c3f.d7c1    DYNAMIC     Po30
 270    003a.9c40.0dc1    DYNAMIC     Po30
 270    0040.5803.02c7    DYNAMIC     Gi1/0/12
 270    0040.5803.b1cb    DYNAMIC     Te4/0/5
 270    0040.5809.3c6b    DYNAMIC     Gi1/0/11
 270    0040.5813.7861    DYNAMIC     Po30
 270    0040.5813.789a    DYNAMIC     Po30
 270    0040.5813.af3c    DYNAMIC     Po30
 270    0040.5814.06be    DYNAMIC     Po30
 270    34ed.1bc4.2dec    DYNAMIC     Po30
 270    503d.e583.2cff    DYNAMIC     Po30
 337    0000.0c9f.f151    DYNAMIC     Po30
 337    003a.9c3f.d7c1    DYNAMIC     Po30
 337    003a.9c40.0dc1    DYNAMIC     Po30
 338    0000.0c9f.f152    DYNAMIC     Po30
 338    003a.9c3f.d7c1    DYNAMIC     Po30
 338    003a.9c40.0dc1    DYNAMIC     Po30
 338    0060.0c85.b656    DYNAMIC     Po30
 345    0000.0c9f.f159    DYNAMIC     Po30
 345    003a.9c3f.d7c1    DYNAMIC     Po30
 345    003a.9c40.0dc1    DYNAMIC     Po30
 345    100e.7ef1.dec0    DYNAMIC     Po30
 540    0000.0c9f.f21c    DYNAMIC     Po30
 540    0019.9972.d8f1    DYNAMIC     Po30
 540    001f.2905.d796    DYNAMIC     Po30
 540    003a.9c3f.d7c1    DYNAMIC     Po30
 540    003a.9c40.0dc1    DYNAMIC     Po30
 540    4c52.621a.66f2    DYNAMIC     Po30
 540    901b.0ea7.a9ad    DYNAMIC     Po30
 540    901b.0efe.da35    DYNAMIC     Po30
 540    ecb1.d739.105c    DYNAMIC     Po30
 551    0000.0c9f.f227    DYNAMIC     Po30
 551    0007.3264.a4e4    DYNAMIC     Po30
 551    0007.3264.a598    DYNAMIC     Po30
           551    0007.3264.a7f6    DYNAMIC     Po30
 551    000d.0507.6270    DYNAMIC     Po30
 551    000d.0507.b1e2    DYNAMIC     Po30
 551    000d.0507.b211    DYNAMIC     Po30
 551    000d.0507.b238    DYNAMIC     Po30
 551    000d.0507.b286    DYNAMIC     Po30
 551    000d.0507.b314    DYNAMIC     Po30
 551    003a.9c3f.d7c1    DYNAMIC     Po30
 551    003a.9c40.0dc1    DYNAMIC     Po30
 551    34ed.1bc4.2dec    DYNAMIC     Po30
 551    7018.a722.fab5    DYNAMIC     Po30
 551    785f.4c00.1b95    DYNAMIC     Po30
 551    785f.4c00.1b97    DYNAMIC     Po30
 551    785f.4c00.cf7e    DYNAMIC     Po30
 551    785f.4c00.d6fc    DYNAMIC     Po30
 551    785f.4c00.ddb5    DYNAMIC     Po30
 551    785f.4c00.dde5    DYNAMIC     Po30
 551    7c16.0d05.3485    DYNAMIC     Po30
 551    7c16.0d05.63fb    DYNAMIC     Po30
 551    7c16.0d05.6407    DYNAMIC     Po30
 551    7c16.0d05.9c92    DYNAMIC     Po30
 551    7c16.0d05.a020    DYNAMIC     Po30
 551    7c16.0d05.a085    DYNAMIC     Po30
 551    7c16.0d05.a0a0    DYNAMIC     Po30
 575    0000.0c9f.f23f    DYNAMIC     Po30
 575    003a.9c3f.d7c1    DYNAMIC     Po30
 575    003a.9c40.0dc1    DYNAMIC     Po30
 610    0000.0c9f.f262    DYNAMIC     Te4/0/10
 610    0007.327f.a17a    DYNAMIC     Te4/0/10
 610    003a.9c3f.d7c1    DYNAMIC     Te4/0/10
 610    003a.9c40.0dc1    DYNAMIC     Te4/0/10
 620    0000.0c9f.f26c    DYNAMIC     Po30
 620    003a.9c3f.d7c1    DYNAMIC     Po30
 620    003a.9c40.0dc1    DYNAMIC     Po30
 629    0000.0c9f.f275    DYNAMIC     Po30
 629    003a.9c3f.d7c1    DYNAMIC     Po30
 629    003a.9c40.0dc1    DYNAMIC     Po30
 629    70b5.e82b.1ebc    DYNAMIC     Po30
 629    a08c.fdd1.ac60    DYNAMIC     Po30
 629    b07b.2503.251f    DYNAMIC     Po30
 629    b42e.99fb.c561    DYNAMIC     Po30
 629    d8cb.8ac8.23c3    DYNAMIC     Po30
 630    0000.0c9f.f276    DYNAMIC     Po30
 630    0007.327c.b416    DYNAMIC     Po30
 630    0007.327c.b6dc    DYNAMIC     Po30
 630    0007.327d.18ad    DYNAMIC     Po30
 630    000c.c601.b0fe    DYNAMIC     Po30
 630    000c.c601.b126    DYNAMIC     Po30
 630    000c.c601.b15e    DYNAMIC     Po30
 630    0019.b9bd.fd88    DYNAMIC     Po30
 630    001e.678a.8500    DYNAMIC     Po30
 630    0025.9066.4b48    DYNAMIC     Po30
 630    003a.9c3f.d7c1    DYNAMIC     Po30
 630    003a.9c40.0dc1    DYNAMIC     Po30
 630    0040.8c71.d5e4    DYNAMIC     Po30
 630    0040.9d46.fc8e    DYNAMIC     Po30
 630    006b.f125.d510    DYNAMIC     Po30
 630    0090.333f.83df    DYNAMIC     Po30
 630    1062.e51b.8724    DYNAMIC     Po30
           630    10e7.c606.13a9    DYNAMIC     Po30
 630    10e7.c606.144e    DYNAMIC     Po30
 630    10e7.c606.162c    DYNAMIC     Po30
 630    10e7.c606.16a8    DYNAMIC     Po30
 630    10e7.c606.1ae5    DYNAMIC     Po30
 630    10e7.c606.1bb3    DYNAMIC     Po30
 630    10e7.c616.4f1c    DYNAMIC     Po30
 630    3005.5c93.2b16    DYNAMIC     Po30
 630    3ca8.2af8.01b5    DYNAMIC     Po30
 630    40b0.3418.1d78    DYNAMIC     Po30
 630    6416.7f77.e654    DYNAMIC     Po30
 630    6416.7fb9.fa8d    DYNAMIC     Po30
 630    6c2b.59c9.ad93    DYNAMIC     Po30
 630    6c2b.59d4.dffb    DYNAMIC     Po30
 630    6c2b.59ee.e970    DYNAMIC     Po30
 630    6c2b.59f0.6bc4    DYNAMIC     Po30
 630    98e7.43bd.d85e    DYNAMIC     Po30
 630    a08c.fde6.0bfc    DYNAMIC     Po30
 630    a4bb.6d77.c31c    DYNAMIC     Po30
 630    ace2.d30f.8c5f    DYNAMIC     Po30
 630    b00c.d134.60c9    DYNAMIC     Po30
 630    ec8e.b577.0574    DYNAMIC     Po30
 631    0000.0c9f.f277    DYNAMIC     Po30
 631    0007.327c.b392    DYNAMIC     Po30
 631    0007.327c.b39c    DYNAMIC     Po30
 631    0007.327c.b3a2    DYNAMIC     Po30
 631    000c.c601.b8ae    DYNAMIC     Po30
 631    0024.dd01.428a    DYNAMIC     Po30
 631    0025.9036.de6c    DYNAMIC     Po30
 631    0025.9095.314c    DYNAMIC     Po30
 631    003a.9c3f.d7c1    DYNAMIC     Po30
 631    003a.9c40.0dc1    DYNAMIC     Po30
 631    004e.019c.ee6f    DYNAMIC     Po30
 631    0862.6637.28ac    DYNAMIC     Po30
 631    1062.e517.bf96    DYNAMIC     Po30
 631    10e7.c606.1324    DYNAMIC     Po30
 631    10e7.c606.1624    DYNAMIC     Po30
 631    1860.2421.9f13    DYNAMIC     Po30
 631    1860.2428.8381    DYNAMIC     Po30
 631    1860.2428.b675    DYNAMIC     Po30
 631    305a.3a82.1a1f    DYNAMIC     Po30
 631    48ba.4eec.b52d    DYNAMIC     Po30
 631    5065.f349.2b29    DYNAMIC     Po30
 631    6045.cb89.98f1    DYNAMIC     Po30
 631    68ab.8a82.93dc    DYNAMIC     Po30
 631    6c2b.59c9.5de9    DYNAMIC     Po30
 631    6c2b.59c9.c0dc    DYNAMIC     Po30
 631    6c2b.59cc.9e51    DYNAMIC     Po30
 631    6c2b.59d3.dd90    DYNAMIC     Po30
 631    6c2b.59d5.3dfc    DYNAMIC     Po30
 631    6c2b.59eb.3050    DYNAMIC     Po30
 631    6c2b.59eb.47b1    DYNAMIC     Po30
 631    704d.7b6f.4cda    DYNAMIC     Po30
 631    705a.0f4a.4182    DYNAMIC     Po30
 631    70b5.e804.d21e    DYNAMIC     Po30
 631    70b5.e80b.19e4    DYNAMIC     Po30
 631    781c.5af2.5495    DYNAMIC     Po30
 631    80e8.2cb4.7848    DYNAMIC     Po30
 631    98e7.f4bb.880a    DYNAMIC     Po30
           631    a08c.fddc.533e    DYNAMIC     Po30
 631    a4bb.6d7f.aaaa    DYNAMIC     Po30
 631    a4bb.6db3.4560    DYNAMIC     Po30
 631    ace2.d303.d04f    DYNAMIC     Po30
 631    ace2.d303.d147    DYNAMIC     Po30
 631    ace2.d306.c8c1    DYNAMIC     Po30
 631    ace2.d30f.8ce6    DYNAMIC     Po30
 631    c8d3.ffa1.e05c    DYNAMIC     Po30
 631    c8d3.ffa4.0b19    DYNAMIC     Po30
 631    c8d3.ffb8.bd42    DYNAMIC     Po30
 631    c8d9.d294.5c84    DYNAMIC     Po30
 631    c8d9.d294.60bf    DYNAMIC     Po30
 631    c8d9.d294.bcca    DYNAMIC     Po30
 631    c8d9.d296.7e34    DYNAMIC     Po30
 631    c8f7.50cd.7caf    DYNAMIC     Po30
 631    fc3f.db09.63d6    DYNAMIC     Po30
 633    0000.0c9f.f279    DYNAMIC     Po30
 633    0004.5f73.8f59    DYNAMIC     Po30
 633    0007.327d.199b    DYNAMIC     Po30
 633    0007.327d.19a3    DYNAMIC     Po30
 633    0007.327d.1a15    DYNAMIC     Po30
 633    0007.327d.1b20    DYNAMIC     Po30
 633    0007.327d.1b8f    DYNAMIC     Po30
 633    0007.327f.a1e4    DYNAMIC     Po30
 633    000c.c601.aeb2    DYNAMIC     Po30
 633    000c.c601.b0f6    DYNAMIC     Po30
 633    000c.c601.b156    DYNAMIC     Po30
 633    000c.c601.b900    DYNAMIC     Po30
 633    0015.17cf.3c12    DYNAMIC     Po30
 633    0019.0f28.f429    DYNAMIC     Po30
 633    001d.9722.01f6    DYNAMIC     Po30
 633    001d.9722.034c    DYNAMIC     Po30
 633    0020.4aa0.a21f    DYNAMIC     Po30
 633    0020.4aa2.0fa3    DYNAMIC     Po30
 633    0020.4ab2.efe5    DYNAMIC     Po30
 633    0020.4ab2.f03c    DYNAMIC     Po30
 633    0024.dd01.41c3    DYNAMIC     Po30
 633    003a.9c3f.d7c1    DYNAMIC     Po30
 633    003a.9c40.0dc1    DYNAMIC     Po30
 633    004e.019c.d16d    DYNAMIC     Po30
 633    0059.dcbb.c0e2    DYNAMIC     Po30
 633    00d0.694c.5ea8    DYNAMIC     Po30
 633    00d0.694c.c8e2    DYNAMIC     Po30
 633    00d0.694c.c902    DYNAMIC     Po30
 633    0462.73db.5760    DYNAMIC     Po30
 633    0c9d.9216.6104    DYNAMIC     Po30
 633    0cc4.7a72.63b4    DYNAMIC     Po30
 633    0cc4.7a90.44b2    DYNAMIC     Po30
 633    0cc4.7a9a.93b2    DYNAMIC     Po30
 633    0cc4.7ab3.d8a7    DYNAMIC     Po30
 633    0cc4.7aca.ae14    DYNAMIC     Po30
 633    0cc4.7aca.aeea    DYNAMIC     Po30
 633    1062.e515.e660    DYNAMIC     Po30
 633    1062.e517.f401    DYNAMIC     Po30
 633    1062.e51a.60a3    DYNAMIC     Po30
 633    1062.e51a.60e5    DYNAMIC     Po30
 633    10e7.c606.138f    DYNAMIC     Po30
 633    10e7.c606.1415    DYNAMIC     Po30
 633    10e7.c606.15bc    DYNAMIC     Po30
           633    10e7.c606.1611    DYNAMIC     Po30
 633    10e7.c606.161b    DYNAMIC     Po30
 633    10e7.c606.161f    DYNAMIC     Po30
 633    10e7.c606.1623    DYNAMIC     Po30
 633    10e7.c606.1633    DYNAMIC     Po30
 633    10e7.c606.169a    DYNAMIC     Po30
 633    10e7.c606.1afb    DYNAMIC     Po30
 633    10e7.c606.1dcb    DYNAMIC     Po30
 633    10e7.c606.8e9d    DYNAMIC     Po30
 633    10e7.c608.ca15    DYNAMIC     Po30
 633    10e7.c60c.38f8    DYNAMIC     Po30
 633    10e7.c610.c597    DYNAMIC     Po30
 633    10e7.c610.c7ac    DYNAMIC     Po30
 633    10e7.c616.4f26    DYNAMIC     Po30
 633    10e7.c616.589e    DYNAMIC     Po30
 633    10e7.c62e.6960    DYNAMIC     Po30
 633    10e7.c64b.f866    DYNAMIC     Po30
 633    149d.997a.496a    DYNAMIC     Po30
 633    1860.2421.9f82    DYNAMIC     Po30
 633    1860.2427.55ba    DYNAMIC     Po30
 633    1860.247c.eac2    DYNAMIC     Po30
 633    18b1.69b6.3725    DYNAMIC     Po30
 633    34ed.1bc4.2dec    DYNAMIC     Po30
 633    34f6.2da9.9e98    DYNAMIC     Po30
 633    3c2a.f450.f062    DYNAMIC     Po30
 633    40a8.f045.da8d    DYNAMIC     Po30
 633    40b0.3418.0939    DYNAMIC     Po30
 633    40b0.3418.09aa    DYNAMIC     Po30
 633    5065.8362.8e7f    DYNAMIC     Po30
 633    6c2b.59c9.7bba    DYNAMIC     Po30
 633    6c2b.59c9.aa63    DYNAMIC     Po30
 633    6c2b.59c9.c7ae    DYNAMIC     Po30
 633    6c2b.59cb.fee7    DYNAMIC     Po30
 633    6c2b.59cc.0093    DYNAMIC     Po30
 633    6c2b.59cc.060c    DYNAMIC     Po30
 633    6c2b.59cc.9bee    DYNAMIC     Po30
 633    6c2b.59cc.c0fd    DYNAMIC     Po30
 633    6c2b.59d3.0038    DYNAMIC     Po30
 633    6c2b.59d3.db71    DYNAMIC     Po30
 633    6c2b.59d3.dbbd    DYNAMIC     Po30
 633    6c2b.59d6.6717    DYNAMIC     Po30
 633    6c2b.59e5.4ac5    DYNAMIC     Po30
 633    6c2b.59f7.4d18    DYNAMIC     Po30
 633    704f.5701.1875    DYNAMIC     Po30
 633    705a.0f48.3bc1    DYNAMIC     Po30
 633    884a.eac2.9824    DYNAMIC     Po30
 633    8cec.4bc7.f605    DYNAMIC     Po30
 633    901b.0eba.176a    DYNAMIC     Po30
 633    98e7.f4bc.bdc0    DYNAMIC     Po30
 633    9c7b.ef72.4bbc    DYNAMIC     Po30
 633    a08c.fdc9.7334    DYNAMIC     Po30
 633    a08c.fdc9.797e    DYNAMIC     Po30
 633    a08c.fdd1.abef    DYNAMIC     Po30
 633    a08c.fddc.57e9    DYNAMIC     Po30
 633    a08c.fddc.75c2    DYNAMIC     Po30
 633    a4bb.6d4d.42ad    DYNAMIC     Po30
 633    a4bb.6d4f.7411    DYNAMIC     Po30
 633    a4bb.6d77.98f8    DYNAMIC     Po30
 633    a4bb.6d77.c2be    DYNAMIC     Po30
           633    a4bb.6d7c.4a6f    DYNAMIC     Po30
 633    a4bb.6d7f.aa97    DYNAMIC     Po30
 633    a89d.2140.62c8    DYNAMIC     Po30
 633    ac1f.6b13.765f    DYNAMIC     Po30
 633    ac87.a30b.62ed    DYNAMIC     Po30
 633    ace2.d301.0fe9    DYNAMIC     Po30
 633    ace2.d303.d037    DYNAMIC     Po30
 633    ace2.d303.d042    DYNAMIC     Po30
 633    ace2.d303.d052    DYNAMIC     Po30
 633    ace2.d303.d123    DYNAMIC     Po30
 633    ace2.d303.d128    DYNAMIC     Po30
 633    ace2.d303.d12b    DYNAMIC     Po30
 633    ace2.d303.d12c    DYNAMIC     Po30
 633    ace2.d303.d134    DYNAMIC     Po30
 633    ace2.d304.0199    DYNAMIC     Po30
 633    ace2.d304.50ce    DYNAMIC     Po30
 633    ace2.d306.c874    DYNAMIC     Po30
 633    ace2.d306.c876    DYNAMIC     Po30
 633    ace2.d306.c8b9    DYNAMIC     Po30
 633    ace2.d306.ccb4    DYNAMIC     Po30
 633    ace2.d30f.8cd0    DYNAMIC     Po30
 633    ace2.d312.a055    DYNAMIC     Po30
 633    b05c.da67.6e66    DYNAMIC     Po30
 633    b07b.2597.c296    DYNAMIC     Po30
 633    c025.e943.f068    DYNAMIC     Po30
 633    c03e.ba8f.92a5    DYNAMIC     Po30
 633    c03e.ba9a.584a    DYNAMIC     Po30
 633    c465.16fe.ca56    DYNAMIC     Po30
 633    c8d3.ffa4.1dd9    DYNAMIC     Po30
 633    c8d3.ffa6.ad0e    DYNAMIC     Po30
 633    c8d3.ffa6.b018    DYNAMIC     Po30
 633    c8d3.ffa6.b025    DYNAMIC     Po30
 633    c8d3.ffa6.b394    DYNAMIC     Po30
 633    c8d3.ffa6.b3a5    DYNAMIC     Po30
 633    c8d3.ffa6.b3db    DYNAMIC     Po30
 633    c8d3.ffa6.b3e4    DYNAMIC     Po30
 633    c8d3.ffa6.b3ef    DYNAMIC     Po30
 633    c8d3.ffa6.b40f    DYNAMIC     Po30
 633    c8d3.ffa6.b546    DYNAMIC     Po30
 633    c8d3.ffa6.b55a    DYNAMIC     Po30
 633    c8d3.ffa6.b55d    DYNAMIC     Po30
 633    c8d9.d209.62ea    DYNAMIC     Po30
 633    c8f7.50fe.5696    DYNAMIC     Po30
 633    c8f7.50fe.c152    DYNAMIC     Po30
 633    dc4a.3e69.8f11    DYNAMIC     Po30
 633    dc4a.3e76.8101    DYNAMIC     Po30
 633    dc4a.3e7f.b4cb    DYNAMIC     Po30
 633    dc4a.3e83.b13b    DYNAMIC     Po30
 633    dc4a.3e8f.e149    DYNAMIC     Po30
 633    e454.e858.aa48    DYNAMIC     Po30
 633    e454.e85d.801b    DYNAMIC     Po30
 633    e454.e85d.ca2a    DYNAMIC     Po30
 633    e454.e867.7455    DYNAMIC     Po30
 633    e454.e878.47a5    DYNAMIC     Po30
 633    e454.e89c.0369    DYNAMIC     Po30
 633    e454.e8c8.6a05    DYNAMIC     Po30
 633    e4b9.7af6.af58    DYNAMIC     Po30
 633    e4b9.7af9.c83e    DYNAMIC     Po30
 633    e4b9.7afb.1994    DYNAMIC     Po30
           633    ec8e.b570.6bd5    DYNAMIC     Po30
 633    ecb1.d743.6e48    DYNAMIC     Po30
 633    f44d.3060.a012    DYNAMIC     Po30
 633    f45e.ab34.0392    DYNAMIC     Po30
 634    0000.0c9f.f27a    DYNAMIC     Po30
 634    000c.c601.b08a    DYNAMIC     Po30
 634    000c.c601.b200    DYNAMIC     Po30
 634    000c.c601.b83e    DYNAMIC     Po30
 634    0018.8516.e7bc    DYNAMIC     Po30
 634    001d.9722.01eb    DYNAMIC     Po30
 634    001d.9722.02c9    DYNAMIC     Po30
 634    001d.9722.03d2    DYNAMIC     Po30
 634    0020.4afb.d33e    DYNAMIC     Po30
 634    0020.4afb.d424    DYNAMIC     Po30
 634    0020.4afb.d432    DYNAMIC     Po30
 634    0020.4afb.d4f1    DYNAMIC     Po30
 634    0020.4afb.e41e    DYNAMIC     Po30
 634    0020.4afb.f65f    DYNAMIC     Po30
 634    0020.4afb.fdb3    DYNAMIC     Po30
 634    0020.4afb.fdd5    DYNAMIC     Po30
 634    0020.4afb.fe85    DYNAMIC     Po30
 634    0020.4afc.0049    DYNAMIC     Po30
 634    0020.4afc.006b    DYNAMIC     Po30
 634    0020.4afc.006f    DYNAMIC     Po30
 634    0020.4afc.4c4c    DYNAMIC     Po30
 634    0024.dd01.441f    DYNAMIC     Po30
 634    0025.9066.4caa    DYNAMIC     Po30
 634    0025.9066.d1a0    DYNAMIC     Po30
 634    0025.90c9.77f6    DYNAMIC     Po30
 634    0025.90e1.26d2    DYNAMIC     Po30
 634    0026.b956.7acc    DYNAMIC     Po30
 634    003a.9c3f.d7c1    DYNAMIC     Po30
 634    003a.9c40.0dc1    DYNAMIC     Po30
 634    004e.019b.ba56    DYNAMIC     Po30
 634    0cc4.7a4e.97a4    DYNAMIC     Po30
 634    0cc4.7a70.016e    DYNAMIC     Po30
 634    0cc4.7a72.904a    DYNAMIC     Po30
 634    1062.e517.bf9a    DYNAMIC     Po30
 634    1062.e519.41f3    DYNAMIC     Po30
 634    10e7.c600.d37f    DYNAMIC     Po30
 634    10e7.c606.169e    DYNAMIC     Po30
 634    10e7.c606.1dd9    DYNAMIC     Po30
 634    10e7.c60e.a9e5    DYNAMIC     Po30
 634    10e7.c616.5792    DYNAMIC     Po30
 634    10e7.c641.2057    DYNAMIC     Po30
 634    1860.2428.81c9    DYNAMIC     Po30
 634    1860.2428.84bd    DYNAMIC     Po30
 634    2426.4235.67a5    DYNAMIC     Po30
 634    34ed.1bc4.2dec    DYNAMIC     Po30
 634    40a8.f057.d468    DYNAMIC     Po30
 634    40b0.3418.0996    DYNAMIC     Po30
 634    480f.cfc8.6c21    DYNAMIC     Po30
 634    6400.6a70.9276    DYNAMIC     Po30
 634    6c2b.59cc.0600    DYNAMIC     Po30
 634    6c2b.59cf.b0e2    DYNAMIC     Po30
 634    6c2b.59d3.d8b2    DYNAMIC     Po30
 634    6c2b.59d3.db8c    DYNAMIC     Po30
 634    6c2b.59d4.dd0f    DYNAMIC     Po30
 634    6c2b.59d5.32ee    DYNAMIC     Po30
           634    6c2b.59ea.f83e    DYNAMIC     Po30
 634    6c2b.59eb.00fb    DYNAMIC     Po30
 634    6c2b.59f7.4fa4    DYNAMIC     Po30
 634    705a.0f3c.c89b    DYNAMIC     Po30
 634    781c.5a76.a804    DYNAMIC     Po30
 634    78dd.d9fe.f62c    DYNAMIC     Po30
 634    84b8.02af.cdb8    DYNAMIC     Po30
 634    8c04.baa6.3bab    DYNAMIC     Po30
 634    9c8e.99df.5b6b    DYNAMIC     Po30
 634    9c8e.99df.5bd9    DYNAMIC     Po30
 634    a08c.fdda.5671    DYNAMIC     Po30
 634    a08c.fddd.6bd1    DYNAMIC     Po30
 634    a4bb.6d77.9cb1    DYNAMIC     Po30
 634    a4bb.6d77.a178    DYNAMIC     Po30
 634    a4bb.6d77.c708    DYNAMIC     Po30
 634    a4bb.6d7e.c176    DYNAMIC     Po30
 634    ac1f.6b65.bb0e    DYNAMIC     Po30
 634    ac22.0b29.7219    DYNAMIC     Po30
 634    ace2.d301.6962    DYNAMIC     Po30
 634    ace2.d301.6a21    DYNAMIC     Po30
 634    ace2.d301.6b04    DYNAMIC     Po30
 634    ace2.d306.1eae    DYNAMIC     Po30
 634    ace2.d312.a07c    DYNAMIC     Po30
 634    c8d3.ff9c.a14c    DYNAMIC     Po30
 634    c8d9.d209.6199    DYNAMIC     Po30
 634    c8d9.d209.6259    DYNAMIC     Po30
 634    c8d9.d209.6298    DYNAMIC     Po30
 634    d89e.f333.f54e    DYNAMIC     Po30
 634    dc4a.3e67.1ad2    DYNAMIC     Po30
 634    dc4a.3e6b.85bf    DYNAMIC     Po30
 634    dc4a.3e84.b8f2    DYNAMIC     Po30
 634    dc4a.3e8f.e361    DYNAMIC     Po30
 634    e0d5.5eb6.d2c4    DYNAMIC     Po30
 634    e0d5.5ed9.e842    DYNAMIC     Po30
 634    e454.e85c.f07b    DYNAMIC     Po30
 634    e454.e867.6fba    DYNAMIC     Po30
 634    e454.e893.132c    DYNAMIC     Po30
 634    e454.e8b1.4851    DYNAMIC     Po30
 634    e81a.5800.0d72    DYNAMIC     Po30
 634    e81a.5800.0d94    DYNAMIC     Po30
 634    ec8e.b57a.8301    DYNAMIC     Po30
 634    ec8e.b57a.833b    DYNAMIC     Po30
 634    ec8e.b57a.84f4    DYNAMIC     Po30
 635    0000.0c9f.f27b    DYNAMIC     Po30
 635    0009.fb58.9df9    DYNAMIC     Po30
 635    000c.c601.a374    DYNAMIC     Po30
 635    0019.0f51.2436    DYNAMIC     Po30
 635    0019.0f51.2473    DYNAMIC     Po30
 635    0019.0f51.2477    DYNAMIC     Po30
 635    0020.4a13.6e49    DYNAMIC     Po30
 635    0025.90e6.f34c    DYNAMIC     Po30
 635    003a.9c3f.d7c1    DYNAMIC     Po30
 635    003a.9c40.0dc1    DYNAMIC     Po30
 635    00d0.c9d2.911f    DYNAMIC     Po30
 635    00d0.c9e1.aedd    DYNAMIC     Po30
 635    00e0.f42a.41bc    DYNAMIC     Po30
 635    00e0.f42a.422e    DYNAMIC     Po30
 635    0860.6efc.da78    DYNAMIC     Po30
 635    1062.e515.e6a1    DYNAMIC     Po30
           635    1062.e515.e793    DYNAMIC     Po30
 635    1062.e519.41f9    DYNAMIC     Po30
 635    1062.e519.41fd    DYNAMIC     Po30
 635    10e7.c600.d3aa    DYNAMIC     Po30
 635    10e7.c63b.da27    DYNAMIC     Po30
 635    1860.2421.9fae    DYNAMIC     Po30
 635    1860.24a3.0613    DYNAMIC     Po30
 635    1860.24a8.394c    DYNAMIC     Po30
 635    1860.24ab.be31    DYNAMIC     Po30
 635    1860.24ac.a9d4    DYNAMIC     Po30
 635    1860.24af.942b    DYNAMIC     Po30
 635    3c07.5463.7de5    DYNAMIC     Po30
 635    3c2a.f461.7c98    DYNAMIC     Po30
 635    40a8.f043.5883    DYNAMIC     Po30
 635    40a8.f045.5fce    DYNAMIC     Po30
 635    40a8.f045.dbe1    DYNAMIC     Po30
 635    480f.cf3a.eb0f    DYNAMIC     Po30
 635    480f.cf58.7cc9    DYNAMIC     Po30
 635    6805.ca8b.9a8c    DYNAMIC     Po30
 635    685b.35c3.7704    DYNAMIC     Po30
 635    6c2b.59c9.6100    DYNAMIC     Po30
 635    6c2b.59c9.7959    DYNAMIC     Po30
 635    6c2b.59d1.37a3    DYNAMIC     Po30
 635    6c2b.59d2.f1ef    DYNAMIC     Po30
 635    6c2b.59d4.0c28    DYNAMIC     Po30
 635    6c2b.59d4.1d46    DYNAMIC     Po30
 635    6c2b.59d4.e2fc    DYNAMIC     Po30
 635    6c2b.59d5.238d    DYNAMIC     Po30
 635    6c2b.59e3.e897    DYNAMIC     Po30
 635    6c2b.59eb.1b30    DYNAMIC     Po30
 635    6c2b.59eb.5708    DYNAMIC     Po30
 635    6c2b.59f6.ed36    DYNAMIC     Po30
 635    705a.0f37.a558    DYNAMIC     Po30
 635    7085.c21e.eed9    DYNAMIC     Po30
 635    8c04.baa6.3b63    DYNAMIC     Po30
 635    8cec.4bc7.99f7    DYNAMIC     Po30
 635    901b.0e1b.3aef    DYNAMIC     Po30
 635    a08c.fdeb.88ab    DYNAMIC     Po30
 635    a4bb.6d4d.a3b3    DYNAMIC     Po30
 635    ace2.d306.c85f    DYNAMIC     Po30
 635    ace2.d30f.8cb4    DYNAMIC     Po30
 635    ace2.d311.194b    DYNAMIC     Po30
 635    c400.ad5e.9ef0    DYNAMIC     Po30
 635    c434.6b7d.8833    DYNAMIC     Po30
 635    c8d3.ffb3.eb70    DYNAMIC     Po30
 635    c8d3.ffb3.fc98    DYNAMIC     Po30
 635    c8d9.d209.5dcd    DYNAMIC     Po30
 635    c8d9.d283.5862    DYNAMIC     Po30
 635    c8d9.d294.6039    DYNAMIC     Po30
 635    c8d9.d294.60c3    DYNAMIC     Po30
 635    dc4a.3e6c.043e    DYNAMIC     Po30
 635    dc4a.3e84.e0ab    DYNAMIC     Po30
 635    dc4a.3e89.16ac    DYNAMIC     Po30
 635    e454.e85c.e1a5    DYNAMIC     Po30
 635    e454.e85f.62e8    DYNAMIC     Po30
 635    e454.e867.6699    DYNAMIC     Po30
 635    e454.e876.ff71    DYNAMIC     Po30
 635    e454.e8bf.b687    DYNAMIC     Po30
 635    e454.e8bf.b691    DYNAMIC     Po30
           635    e454.e8bf.b7a2    DYNAMIC     Po30
 635    e454.e8db.6d7a    DYNAMIC     Po30
 635    ecb1.d75f.c4c2    DYNAMIC     Po30
 635    f4db.e6ff.41f2    DYNAMIC     Po30
 636    0000.0c9f.f27c    DYNAMIC     Po30
 636    0007.3276.768b    DYNAMIC     Po30
 636    0007.3276.d063    DYNAMIC     Po30
 636    000c.c601.b914    DYNAMIC     Po30
 636    001d.9722.03cd    DYNAMIC     Po30
 636    001d.9722.03d0    DYNAMIC     Po30
 636    0020.4afb.fe78    DYNAMIC     Po30
 636    0020.4afc.007a    DYNAMIC     Po30
 636    003a.9c3f.d7c1    DYNAMIC     Po30
 636    003a.9c40.0dc1    DYNAMIC     Po30
 636    10e7.c600.d393    DYNAMIC     Po30
 636    10e7.c608.2401    DYNAMIC     Po30
 636    3448.ed84.1e95    DYNAMIC     Po30
 636    40b0.341d.daf8    DYNAMIC     Po30
 636    40b0.3439.a52e    DYNAMIC     Po30
 636    40b0.3439.a539    DYNAMIC     Po30
 636    40b0.343b.ffdb    DYNAMIC     Po30
 636    40b0.343b.ffdd    DYNAMIC     Po30
 636    40b0.343b.ffea    DYNAMIC     Po30
 636    40b0.343e.4b24    DYNAMIC     Po30
 636    40b0.343e.4b25    DYNAMIC     Po30
 636    40b0.343e.687e    DYNAMIC     Po30
 636    40b0.3441.d107    DYNAMIC     Po30
 636    40b0.3443.884d    DYNAMIC     Po30
 636    40b0.3443.8855    DYNAMIC     Po30
 636    40b0.3444.c362    DYNAMIC     Po30
 636    40b0.3444.c366    DYNAMIC     Po30
 636    40b0.3444.c37d    DYNAMIC     Po30
 636    40b0.3444.c37f    DYNAMIC     Po30
 636    40b0.3445.41bf    DYNAMIC     Po30
 636    6c2b.59e3.ec3d    DYNAMIC     Po30
 636    6c2b.59e9.ce2d    DYNAMIC     Po30
 636    6c2b.59e9.d2df    DYNAMIC     Po30
 636    6c2b.59ea.c748    DYNAMIC     Po30
 636    6c2b.59ea.cdb1    DYNAMIC     Po30
 636    6c2b.59eb.25cf    DYNAMIC     Po30
 636    6c2b.59eb.4653    DYNAMIC     Po30
 636    6c2b.59ef.1c30    DYNAMIC     Po30
 636    6c2b.59f1.c101    DYNAMIC     Po30
 636    6c2b.59f4.2f72    DYNAMIC     Po30
 636    6c2b.59f4.aa7d    DYNAMIC     Po30
 636    705a.0f4a.4082    DYNAMIC     Po30
 636    98e7.f42e.46e4    DYNAMIC     Po30
 636    a08c.fdc2.c9d1    DYNAMIC     Po30
 636    a08c.fdd2.70b3    DYNAMIC     Po30
 636    a08c.fdd3.0f02    DYNAMIC     Po30
 636    a08c.fdda.7c63    DYNAMIC     Po30
 636    a08c.fdda.7c66    DYNAMIC     Po30
 636    a08c.fddc.7574    DYNAMIC     Po30
 636    a08c.fddc.f38e    DYNAMIC     Po30
 636    a08c.fddc.f390    DYNAMIC     Po30
 636    a08c.fdde.e6cc    DYNAMIC     Po30
 636    a0c5.f2c0.1368    DYNAMIC     Po30
 636    a4bb.6d4d.0b5e    DYNAMIC     Po30
 636    a4bb.6d4d.163d    DYNAMIC     Po30
           636    a4bb.6d4d.1919    DYNAMIC     Po30
 636    a4bb.6d4d.1c6e    DYNAMIC     Po30
 636    a4bb.6d4d.4abb    DYNAMIC     Po30
 636    a4bb.6d4d.94fb    DYNAMIC     Po30
 636    a4bb.6d4d.9950    DYNAMIC     Po30
 636    a4bb.6d4d.a248    DYNAMIC     Po30
 636    a4bb.6d4d.a324    DYNAMIC     Po30
 636    a4bb.6d4d.a442    DYNAMIC     Po30
 636    a4bb.6d4d.a89b    DYNAMIC     Po30
 636    a4bb.6d4d.a8a5    DYNAMIC     Po30
 636    a4bb.6d4d.c3c5    DYNAMIC     Po30
 636    a4bb.6d4d.c528    DYNAMIC     Po30
 636    a4bb.6d4d.c5b0    DYNAMIC     Po30
 636    a4bb.6d4d.c647    DYNAMIC     Po30
 636    a4bb.6d4d.c648    DYNAMIC     Po30
 636    a4bb.6d4d.d00c    DYNAMIC     Po30
 636    a4bb.6d4d.d020    DYNAMIC     Po30
 636    a4bb.6d4d.d3f8    DYNAMIC     Po30
 636    a4bb.6d4e.bd86    DYNAMIC     Po30
 636    a4bb.6d4e.d66b    DYNAMIC     Po30
 636    a4bb.6d4e.d69b    DYNAMIC     Po30
 636    a4bb.6d4e.d825    DYNAMIC     Po30
 636    a4bb.6d4e.da75    DYNAMIC     Po30
 636    a4bb.6d4e.da87    DYNAMIC     Po30
 636    a4bb.6d4e.db73    DYNAMIC     Po30
 636    a4bb.6d4e.db94    DYNAMIC     Po30
 636    a4bb.6d4e.dcc3    DYNAMIC     Po30
 636    a4bb.6d4e.dcca    DYNAMIC     Po30
 636    a4bb.6d4e.e728    DYNAMIC     Po30
 636    a4bb.6d4e.f0c7    DYNAMIC     Po30
 636    a4bb.6d4f.6d0d    DYNAMIC     Po30
 636    a4bb.6d4f.723e    DYNAMIC     Po30
 636    a4bb.6d4f.7295    DYNAMIC     Po30
 636    a4bb.6d4f.741d    DYNAMIC     Po30
 636    a4bb.6d4f.7b8a    DYNAMIC     Po30
 636    a4bb.6d4f.8570    DYNAMIC     Po30
 636    a4bb.6d4f.8bc8    DYNAMIC     Po30
 636    a4bb.6d4f.90ff    DYNAMIC     Po30
 636    a4bb.6d4f.9290    DYNAMIC     Po30
 636    a4bb.6d4f.9303    DYNAMIC     Po30
 636    ace2.d30f.8d50    DYNAMIC     Po30
 636    b00c.d134.70ce    DYNAMIC     Po30
 636    bce9.2fd4.8680    DYNAMIC     Po30
 636    c03e.baac.fe05    DYNAMIC     Po30
 636    c8d3.ffa1.e16b    DYNAMIC     Po30
 636    c8d3.ffa4.1dd3    DYNAMIC     Po30
 636    c8d3.ffb3.edbe    DYNAMIC     Po30
 636    c8d3.ffb3.ee04    DYNAMIC     Po30
 636    c8d3.ffb3.ee07    DYNAMIC     Po30
 636    c8d3.ffb3.ee0b    DYNAMIC     Po30
 636    c8d3.ffb3.ee10    DYNAMIC     Po30
 636    c8d3.ffb3.ee12    DYNAMIC     Po30
 636    c8d3.ffb7.f6c4    DYNAMIC     Po30
 636    c8d3.ffb8.ba56    DYNAMIC     Po30
 636    c8d3.ffb8.bd3c    DYNAMIC     Po30
 636    c8d3.ffb8.bd47    DYNAMIC     Po30
 636    c8d3.ffbc.424e    DYNAMIC     Po30
 636    c8d9.d209.6e5a    DYNAMIC     Po30
 636    c8f7.50d1.4de3    DYNAMIC     Po30
           636    dc4a.3e77.ecf0    DYNAMIC     Po30
 636    e454.e85c.d5b8    DYNAMIC     Po30
 636    e454.e85c.ddd4    DYNAMIC     Po30
 636    ec8e.b56e.7904    DYNAMIC     Po30
 636    ec8e.b57a.8315    DYNAMIC     Po30
 636    fc3f.db02.949a    DYNAMIC     Po30
 636    fc3f.db06.6563    DYNAMIC     Po30
 637    0000.0c9f.f27d    DYNAMIC     Po30
 637    0001.f092.af7a    DYNAMIC     Po30
 637    000d.0505.a930    DYNAMIC     Po30
 637    000d.0507.631b    DYNAMIC     Po30
 637    000d.0507.6328    DYNAMIC     Po30
 637    000d.0507.6332    DYNAMIC     Po30
 637    000d.0507.b34a    DYNAMIC     Po30
 637    001d.9722.01ef    DYNAMIC     Po30
 637    001d.9722.030b    DYNAMIC     Po30
 637    0024.dd01.4508    DYNAMIC     Po30
 637    003a.9c3f.d7c1    DYNAMIC     Po30
 637    003a.9c40.0dc1    DYNAMIC     Po30
 637    00ee.ab3f.8130    DYNAMIC     Po30
 637    0cc4.7a16.db38    DYNAMIC     Po30
 637    0cc4.7a70.002e    DYNAMIC     Po30
 637    1062.e500.0a0b    DYNAMIC     Po30
 637    1062.e501.6ee9    DYNAMIC     Po30
 637    1062.e501.6f63    DYNAMIC     Po30
 637    1062.e502.16ed    DYNAMIC     Po30
 637    1062.e502.18cc    DYNAMIC     Po30
 637    1062.e502.18f4    DYNAMIC     Po30
 637    1062.e513.3014    DYNAMIC     Po30
 637    1062.e515.e9af    DYNAMIC     Po30
 637    1062.e519.422a    DYNAMIC     Po30
 637    1062.e51a.60ed    DYNAMIC     Po30
 637    1062.e51a.6182    DYNAMIC     Po30
 637    1062.e51a.6298    DYNAMIC     Po30
 637    1062.e51a.6499    DYNAMIC     Po30
 637    1062.e51b.871a    DYNAMIC     Po30
 637    10e7.c606.1621    DYNAMIC     Po30
 637    10e7.c611.3e10    DYNAMIC     Po30
 637    10e7.c640.8d51    DYNAMIC     Po30
 637    1860.2426.ba8f    DYNAMIC     Po30
 637    1860.2426.bd00    DYNAMIC     Po30
 637    1860.2427.5595    DYNAMIC     Po30
 637    1860.2428.b678    DYNAMIC     Po30
 637    1860.249d.6bd8    DYNAMIC     Po30
 637    1860.24ab.be4d    DYNAMIC     Po30
 637    1860.24ab.be4e    DYNAMIC     Po30
 637    1860.24ab.be66    DYNAMIC     Po30
 637    1860.24b0.9914    DYNAMIC     Po30
 637    1860.24b1.136f    DYNAMIC     Po30
 637    1860.24f9.d83e    DYNAMIC     Po30
 637    2426.427c.7ad7    DYNAMIC     Po30
 637    40b0.341b.8706    DYNAMIC     Po30
 637    40b0.343b.e371    DYNAMIC     Po30
 637    40b0.343b.e378    DYNAMIC     Po30
 637    40b0.343e.6a37    DYNAMIC     Po30
 637    480f.cf59.b60e    DYNAMIC     Po30
 637    480f.cfbe.9e74    DYNAMIC     Po30
 637    480f.cfc8.5c47    DYNAMIC     Po30
 637    5065.f34d.95e3    DYNAMIC     Po30
           637    6c2b.59c9.57f7    DYNAMIC     Po30
 637    6c2b.59c9.8026    DYNAMIC     Po30
 637    6c2b.59c9.908b    DYNAMIC     Po30
 637    6c2b.59c9.b3e6    DYNAMIC     Po30
 637    6c2b.59d3.e2aa    DYNAMIC     Po30
 637    6c2b.59d3.e74f    DYNAMIC     Po30
 637    6c2b.59d4.1809    DYNAMIC     Po30
 637    6c2b.59d4.23f1    DYNAMIC     Po30
 637    6c2b.59d5.2225    DYNAMIC     Po30
 637    6c2b.59d5.3748    DYNAMIC     Po30
 637    6c2b.59d5.3f6e    DYNAMIC     Po30
 637    6c2b.59d5.3fb8    DYNAMIC     Po30
 637    6c2b.59d5.447e    DYNAMIC     Po30
 637    6c2b.59ea.ebf2    DYNAMIC     Po30
 637    6c2b.59f8.cc24    DYNAMIC     Po30
 637    705a.0f48.b6d5    DYNAMIC     Po30
 637    74fe.4805.89a0    DYNAMIC     Po30
 637    781c.5af2.5811    DYNAMIC     Po30
 637    785f.4c00.434d    DYNAMIC     Po30
 637    785f.4c00.434e    DYNAMIC     Po30
 637    88d7.f6c2.bb5a    DYNAMIC     Po30
 637    88d7.f6c2.bdcb    DYNAMIC     Po30
 637    88d7.f6c2.be51    DYNAMIC     Po30
 637    a08c.fdda.40a5    DYNAMIC     Po30
 637    a08c.fde6.f44f    DYNAMIC     Po30
 637    a08c.fdeb.feb8    DYNAMIC     Po30
 637    a4bb.6d4d.9746    DYNAMIC     Po30
 637    a4bb.6d4d.a765    DYNAMIC     Po30
 637    a4bb.6d4e.c26b    DYNAMIC     Po30
 637    a4bb.6d7f.ae20    DYNAMIC     Po30
 637    acdb.da4c.daa6    DYNAMIC     Po30
 637    acdb.da4c.dbf2    DYNAMIC     Po30
 637    ace2.d301.0e2a    DYNAMIC     Po30
 637    ace2.d303.d045    DYNAMIC     Po30
 637    ace2.d303.d11f    DYNAMIC     Po30
 637    ace2.d303.d14b    DYNAMIC     Po30
 637    ace2.d303.d14d    DYNAMIC     Po30
 637    c8d3.ffa1.de0a    DYNAMIC     Po30
 637    c8f7.50fe.8f50    DYNAMIC     Po30
 637    dc4a.3e82.21ad    DYNAMIC     Po30
 637    dc4a.3e93.6797    DYNAMIC     Po30
 637    dc4a.3e93.683e    DYNAMIC     Po30
 637    e454.e84f.0d4e    DYNAMIC     Po30
 637    e454.e858.a99d    DYNAMIC     Po30
 637    e454.e85c.c160    DYNAMIC     Po30
 637    e454.e85c.d451    DYNAMIC     Po30
 637    e454.e85c.dd43    DYNAMIC     Po30
 637    e454.e85c.e21c    DYNAMIC     Po30
 637    e454.e85c.e665    DYNAMIC     Po30
 637    e454.e85c.e7df    DYNAMIC     Po30
 637    e454.e85c.e831    DYNAMIC     Po30
 637    e454.e85c.ea5e    DYNAMIC     Po30
 637    e454.e85c.ebae    DYNAMIC     Po30
 637    e454.e85d.4b0b    DYNAMIC     Po30
 637    e454.e85d.5186    DYNAMIC     Po30
 637    e454.e85d.7a5a    DYNAMIC     Po30
 637    e454.e879.d82d    DYNAMIC     Po30
 637    e454.e87f.7ca0    DYNAMIC     Po30
 637    e454.e885.ad4c    DYNAMIC     Po30
           637    e454.e895.9d36    DYNAMIC     Po30
 637    e4aa.5d6e.6ce8    DYNAMIC     Po30
 637    e4b9.7af9.b619    DYNAMIC     Po30
 637    f430.b9d4.0031    DYNAMIC     Po30
 637    f439.0925.62db    DYNAMIC     Po30
 637    f439.0925.62dc    DYNAMIC     Po30
 637    f439.0925.63f0    DYNAMIC     Po30
 637    f4cf.e274.6a78    DYNAMIC     Po30
 638    0000.0c9f.f27e    DYNAMIC     Po30
 638    0009.fb76.e91f    DYNAMIC     Po30
 638    0009.fb76.e923    DYNAMIC     Po30
 638    000c.c601.aeb0    DYNAMIC     Po30
 638    001d.9722.01ed    DYNAMIC     Po30
 638    0023.245a.23db    DYNAMIC     Po30
 638    0023.245a.6ec6    DYNAMIC     Po30
 638    0024.dd01.441b    DYNAMIC     Po30
 638    003a.9c3f.d7c1    DYNAMIC     Po30
 638    003a.9c40.0dc1    DYNAMIC     Po30
 638    004e.019b.bbf8    DYNAMIC     Po30
 638    0860.6efd.973c    DYNAMIC     Po30
 638    1062.e51a.6181    DYNAMIC     Po30
 638    1062.e51b.86cc    DYNAMIC     Po30
 638    1062.e51b.879e    DYNAMIC     Po30
 638    10e7.c608.c9a2    DYNAMIC     Po30
 638    10e7.c60c.38b0    DYNAMIC     Po30
 638    10e7.c60c.38d4    DYNAMIC     Po30
 638    1860.2421.a08e    DYNAMIC     Po30
 638    1860.2428.8313    DYNAMIC     Po30
 638    2426.4235.64e5    DYNAMIC     Po30
 638    2c76.8a04.eb79    DYNAMIC     Po30
 638    4c52.6220.bb1a    DYNAMIC     Po30
 638    5cb9.0112.f0af    DYNAMIC     Po30
 638    6879.ed74.5967    DYNAMIC     Po30
 638    68ab.8a82.a1dc    DYNAMIC     Po30
 638    6c2b.59c9.5579    DYNAMIC     Po30
 638    6c2b.59c9.595c    DYNAMIC     Po30
 638    6c2b.59c9.6f01    DYNAMIC     Po30
 638    6c2b.59d6.6870    DYNAMIC     Po30
 638    6c2b.59ed.f9a0    DYNAMIC     Po30
 638    6c2b.59f7.6a8a    DYNAMIC     Po30
 638    6c2b.59f7.6c18    DYNAMIC     Po30
 638    70df.2fce.1ce7    DYNAMIC     Po30
 638    781c.5aa1.f306    DYNAMIC     Po30
 638    781c.5aa1.f38c    DYNAMIC     Po30
 638    9457.a5ee.40a5    DYNAMIC     Po30
 638    a08c.fdd2.aab0    DYNAMIC     Po30
 638    a08c.fddd.6bd8    DYNAMIC     Po30
 638    a08c.fde6.f463    DYNAMIC     Po30
 638    a4bb.6d6d.18c9    DYNAMIC     Po30
 638    a4bb.6da8.d05c    DYNAMIC     Po30
 638    ace2.d303.fcf8    DYNAMIC     Po30
 638    b00c.d133.6e0c    DYNAMIC     Po30
 638    dc4a.3e67.1844    DYNAMIC     Po30
 638    dc4a.3e6c.4fdd    DYNAMIC     Po30
 638    e454.e85d.3cfd    DYNAMIC     Po30
 638    e454.e8b5.23d3    DYNAMIC     Po30
 638    e4b9.7af6.b6b5    DYNAMIC     Po30
 638    e81a.5800.0d56    DYNAMIC     Po30
 638    e81a.5800.0d95    DYNAMIC     Po30
           638    ecb1.d731.29aa    DYNAMIC     Po30
 638    f8b1.56a3.f835    DYNAMIC     Po30
 640    0000.0c9f.f280    DYNAMIC     Po30
 640    0015.1798.76da    DYNAMIC     Po30
 640    003a.9c3f.d7c1    DYNAMIC     Po30
 640    003a.9c40.0dc1    DYNAMIC     Po30
 640    00e0.81b6.83a4    DYNAMIC     Po30
 640    40b0.341a.8bab    DYNAMIC     Po30
 680    0000.0c9f.f2a8    DYNAMIC     Te4/0/2
 680    001e.c600.0016    DYNAMIC     Te4/0/2
 680    001e.c600.003e    DYNAMIC     Te4/0/2
 680    003a.9c3f.d7c1    DYNAMIC     Te4/0/2
 680    003a.9c40.0dc1    DYNAMIC     Te4/0/2
 770    0000.0c9f.f302    DYNAMIC     Po30
 770    003a.9c3f.d7c1    DYNAMIC     Po30
 770    003a.9c40.0dc1    DYNAMIC     Po30
 770    0040.9d4a.3131    DYNAMIC     Po30
 770    0040.9d50.b858    DYNAMIC     Po30
 772    0000.0c9f.f304    DYNAMIC     Po30
 772    003a.9c3f.d7c1    DYNAMIC     Po30
 772    003a.9c40.0dc1    DYNAMIC     Po30
 773    0000.0c9f.f305    DYNAMIC     Te4/0/13
 773    003a.9c3f.d7c1    DYNAMIC     Te4/0/13
 773    003a.9c40.0dc1    DYNAMIC     Te4/0/13
 850    0000.0c9f.f352    DYNAMIC     Po30
 850    003a.9c3f.d7c1    DYNAMIC     Po30
 850    003a.9c40.0dc1    DYNAMIC     Po30
 850    a46c.2a9f.b817    DYNAMIC     Po30
 921    0000.0c9f.f399    DYNAMIC     Po30
 921    003a.9c3f.d7c1    DYNAMIC     Po30
 921    003a.9c40.0dc1    DYNAMIC     Po30
 921    70db.9822.c6ea    DYNAMIC     Po30
 942    0000.0c9f.f3ae    DYNAMIC     Po30
 942    003a.9c3f.d7c1    DYNAMIC     Po30
 983    0000.0c9f.f3d7    DYNAMIC     Po30
 983    003a.9c3f.d7c1    DYNAMIC     Po30
 983    003a.9c40.0dc1    DYNAMIC     Po30
 983    34ed.1bc4.2dec    DYNAMIC     Po30
 983    6416.7f47.a71d    DYNAMIC     Po30
 983    6416.7fa2.9e0a    DYNAMIC     Po30
 983    6416.7fb8.8f1e    DYNAMIC     Po30
 984    0000.0c9f.f3d8    DYNAMIC     Po30
 984    003a.9c3f.d7c1    DYNAMIC     Po30
 984    003a.9c40.0dc1    DYNAMIC     Po30
 984    10cd.ae67.93b3    DYNAMIC     Po30
 984    34ed.1bc4.2dec    DYNAMIC     Po30
 986    0000.0c9f.f3da    DYNAMIC     Po30
 986    003a.9c3f.d7c1    DYNAMIC     Po30
 986    34ed.1bc4.2dec    DYNAMIC     Po30
 986    6416.7f77.53af    DYNAMIC     Po30
 987    0000.0c9f.f3db    DYNAMIC     Po30
 987    003a.9c3f.d7c1    DYNAMIC     Po30
 987    003a.9c40.0dc1    DYNAMIC     Po30
 987    34ed.1bc4.2dec    DYNAMIC     Po30
 989    0000.0c9f.f3dd    DYNAMIC     Po30
 989    003a.9c3f.d7c1    DYNAMIC     Po30
 989    6416.7f47.8bf8    DYNAMIC     Po30
 990    0000.0c9f.f3de    DYNAMIC     Po30
 990    003a.9c3f.d7c1    DYNAMIC     Po30
           990    003a.9c40.0dc1    DYNAMIC     Po30
1041    0000.0c9f.f411    DYNAMIC     Po30
1041    0010.7fb2.8754    DYNAMIC     Po30
1041    0010.7fb2.8f0a    DYNAMIC     Po30
1041    0010.7fb2.8f2a    DYNAMIC     Po30
1041    0010.7fb2.9313    DYNAMIC     Po30
1041    0010.7fc2.ac66    DYNAMIC     Po30
1041    0010.7fcc.350c    DYNAMIC     Po30
1041    0010.7fcc.355e    DYNAMIC     Po30
1041    0010.7fd4.0aa1    DYNAMIC     Po30
1041    0010.7fd5.5ef6    DYNAMIC     Po30
1041    003a.9c3f.d7c1    DYNAMIC     Po30
1041    003a.9c40.0dc1    DYNAMIC     Po30
1041    34ed.1bc4.2dec    DYNAMIC     Po30
1041    7845.0105.ff99    DYNAMIC     Po30
1041    a0f8.495d.9766    DYNAMIC     Po30
1041    d46a.91d0.1f29    DYNAMIC     Gi1/0/22
1209    0000.0c9f.f4b9    DYNAMIC     Po30
1209    003a.9c3f.d7c1    DYNAMIC     Po30
1209    003a.9c40.0dc1    DYNAMIC     Po30
1209    0050.f964.eeb6    DYNAMIC     Po30
1209    0050.f965.42a4    DYNAMIC     Po30
1600    0000.0c9f.f640    DYNAMIC     Te4/0/15
1600    003a.9c3f.d7c1    DYNAMIC     Te4/0/15
1600    003a.9c40.0dc1    DYNAMIC     Te4/0/15
1600    0040.8cfc.faea    DYNAMIC     Te4/0/15
1600    accc.8e0c.8041    DYNAMIC     Te4/0/15
1600    accc.8e0c.8042    DYNAMIC     Te4/0/15
1600    accc.8e0c.9412    DYNAMIC     Te4/0/15
1600    accc.8e0c.9417    DYNAMIC     Te4/0/15
1600    accc.8e0c.9419    DYNAMIC     Te4/0/15
1600    accc.8e0c.943d    DYNAMIC     Te4/0/15
1600    accc.8e0c.943e    DYNAMIC     Te4/0/15
1600    accc.8e0c.943f    DYNAMIC     Te4/0/15
1600    accc.8e0c.9440    DYNAMIC     Te4/0/15
1600    accc.8e0c.9443    DYNAMIC     Te4/0/15
1600    accc.8e1e.86af    DYNAMIC     Te4/0/15
1600    accc.8e1e.86b0    DYNAMIC     Te4/0/15
1600    accc.8e1e.86c8    DYNAMIC     Te4/0/15
1600    accc.8e1e.86c9    DYNAMIC     Te4/0/15
1600    accc.8e1e.86ca    DYNAMIC     Te4/0/15
1600    accc.8e1e.86d4    DYNAMIC     Te4/0/15
1600    accc.8e1e.86d5    DYNAMIC     Te4/0/15
1600    accc.8e1e.86d6    DYNAMIC     Te4/0/15
1600    accc.8e1e.86d7    DYNAMIC     Te4/0/15
1600    accc.8e1e.8718    DYNAMIC     Te4/0/15
1600    accc.8e1e.8719    DYNAMIC     Te4/0/15
1600    accc.8e1e.871a    DYNAMIC     Te4/0/15
1600    accc.8e1e.871b    DYNAMIC     Te4/0/15
1600    accc.8e1e.8722    DYNAMIC     Te4/0/15
1600    accc.8e1e.8723    DYNAMIC     Te4/0/15
1600    accc.8e1e.8724    DYNAMIC     Te4/0/15
1600    accc.8e1e.8725    DYNAMIC     Te4/0/15
1600    accc.8e1e.8730    DYNAMIC     Te4/0/15
1600    accc.8e1e.8738    DYNAMIC     Te4/0/15
1600    accc.8e1e.873e    DYNAMIC     Te4/0/15
1600    accc.8e1e.873f    DYNAMIC     Te4/0/15
1600    accc.8e1e.874b    DYNAMIC     Te4/0/15
1600    accc.8e1e.874c    DYNAMIC     Te4/0/15
          1600    accc.8e1e.f37e    DYNAMIC     Te4/0/15
1600    accc.8e1e.f3a6    DYNAMIC     Te4/0/15
1605    0000.0c9f.f645    DYNAMIC     Po30
1605    003a.9c3f.d7c1    DYNAMIC     Po30
1605    003a.9c40.0dc1    DYNAMIC     Po30
1605    0040.8cfa.1b44    DYNAMIC     Po30
1605    0040.8cfa.1b48    DYNAMIC     Po30
1605    0040.8cfa.1b4a    DYNAMIC     Po30
1605    0040.8cfa.1ce2    DYNAMIC     Po30
1605    0040.8cfa.5d79    DYNAMIC     Po30
1605    accc.8e5c.c83b    DYNAMIC     Po30
1605    accc.8ea1.e489    DYNAMIC     Po30
1605    accc.8ec1.21fe    DYNAMIC     Po30
1605    accc.8ec1.21ff    DYNAMIC     Po30
1605    accc.8ec1.2203    DYNAMIC     Po30
1605    accc.8ec1.2204    DYNAMIC     Po30
1605    accc.8ec1.2209    DYNAMIC     Po30
1605    accc.8ec1.220d    DYNAMIC     Po30
1605    accc.8ec1.220f    DYNAMIC     Po30
1605    accc.8ec1.2213    DYNAMIC     Po30
1605    accc.8ec1.9171    DYNAMIC     Po30
1616    0000.0c9f.f650    DYNAMIC     Po30
1616    003a.9c3f.d7c1    DYNAMIC     Po30
1616    003a.9c40.0dc1    DYNAMIC     Po30
1616    34ed.1bc4.2dec    DYNAMIC     Po30
1621    0000.0c9f.f640    DYNAMIC     Po30
1621    003a.9c3f.d7c1    DYNAMIC     Po30
1621    003a.9c40.0dc1    DYNAMIC     Po30
1672    0000.0c9f.f688    DYNAMIC     Po30
1672    003a.9c3f.d7c1    DYNAMIC     Po30
1672    003a.9c40.0dc1    DYNAMIC     Po30
1700    0000.0c9f.f6a4    DYNAMIC     Po30
1700    003a.9c3f.d7c1    DYNAMIC     Po30
1700    003a.9c40.0dc1    DYNAMIC     Po30
1900    0000.0c9f.f76c    DYNAMIC     Po30
1900    003a.9c3f.d7c1    DYNAMIC     Po30
1900    003a.9c40.0dc1    DYNAMIC     Po30
1900    e0da.dc03.9923    DYNAMIC     Gi1/0/47
1900    e0da.dc03.994a    DYNAMIC     Gi1/0/47
1900    e0da.dc03.994b    DYNAMIC     Gi1/0/47
1900    e0da.dc03.994f    DYNAMIC     Gi1/0/47
1900    e0da.dc03.9952    DYNAMIC     Gi1/0/47
Total Mac Addresses for this criterion: 2161""",
 'show run | section tacacs':"""aaa group server tacacs+ NOC-TAC
 server name TAC-EBC
 server name TAC-SECONDARY
tacacs server TAC-EBC
 address ipv4 172.31.17.180
 key 7 032D1F0E2F4B246E6E0B0044
tacacs server TAC-SECONDARY
 address ipv4 10.64.32.5
 key 7 07266549674D1C273710124D""",
 'show run | in tacacs':"""aaa group server tacacs+ NOC-TAC
tacacs server TAC-EBC
tacacs server TAC-SECONDARY""",
 'show power inline':"""Available:4505.0(w)  Used:515.6(w)  Remaining:3989.4(w)

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
Gi1/0/11  auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/12  auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/13  auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/14  auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/15  auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/16  auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/17  auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/18  auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/19  auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/20  auto   on         15.4       15.4       Ieee PD             0    
Gi1/0/21  auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/22  auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/23  auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/24  auto   on         16.8       16.8       AIR-CAP3702I-A-K9   4    
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
Gi1/0/35  auto   faulty     0.0        0.0        n/a                 n/a  
Gi1/0/36  auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/37  auto   on         30.0       30.0       Ieee PD             4    
Gi1/0/38  auto   off        0.0        0.0        n/a                 n/a  
Gi1/0/39  auto   on         30.0       30.0       AIR-AP1810W-B-K9    4    
Gi1/0/40  auto   on         30.0       30.0       AIR-AP1810W-B-K9    4    
Gi1/0/41  auto   on         30.0       30.0       AIR-AP1810W-B-K9    4    
Gi1/0/42  auto   on         30.0       30.0       AIR-AP3802I-B-K9    4    
Gi1/0/43  auto   on         30.0       30.0       AIR-AP1810W-B-K9    4    
Gi1/0/44  auto   on         30.0       30.0       AIR-AP3802I-B-K9    4    
Gi1/0/45  auto   on         30.0       30.0       AIR-AP2802I-B-K9    4    
Gi1/0/46  auto   on         30.0       30.0       AIR-AP2802I-B-K9    4    
Gi1/0/47  off    off        0.0        0.0        n/a                 n/a  
Gi1/0/48  auto   on         30.0       30.0       AIR-AP2802I-B-K9    4    
Gi7/0/1   auto   off        0.0        0.0        n/a                 n/a  
Gi7/0/2   auto   off        0.0        0.0        n/a                 n/a  
Gi7/0/3   auto   off        0.0        0.0        n/a                 n/a  
Gi7/0/4   auto   on         4.0        4.0        Ieee PD             1    
          Interface Admin  Oper            Power(Watts)     Device              Class
                            From PS    To Device                    
--------- ------ ---------- ---------- ---------- ------------------- -----

Gi7/0/5   auto   on         30.0       30.0       AIR-AP1810W-B-K9    4    
Gi7/0/6   auto   off        0.0        0.0        n/a                 n/a  
Gi7/0/7   auto   off        0.0        0.0        n/a                 n/a  
Gi7/0/8   auto   off        0.0        0.0        n/a                 n/a  
Gi7/0/9   auto   off        0.0        0.0        n/a                 n/a  
Gi7/0/10  auto   off        0.0        0.0        n/a                 n/a  
Gi7/0/11  auto   off        0.0        0.0        n/a                 n/a  
Gi7/0/12  auto   off        0.0        0.0        n/a                 n/a  
Gi7/0/13  auto   off        0.0        0.0        n/a                 n/a  
Gi7/0/14  auto   off        0.0        0.0        n/a                 n/a  
Gi7/0/15  auto   off        0.0        0.0        n/a                 n/a  
Gi7/0/16  auto   off        0.0        0.0        n/a                 n/a  
Gi7/0/17  auto   on         4.0        4.0        Ieee PD             1    
Gi7/0/18  auto   on         4.0        4.0        Ieee PD             1    
Gi7/0/19  auto   off        0.0        0.0        n/a                 n/a  
Gi7/0/20  auto   off        0.0        0.0        n/a                 n/a  
Gi7/0/21  auto   on         4.0        4.0        Ieee PD             1    
Gi7/0/22  auto   on         4.0        4.0        Ieee PD             1    
Gi7/0/23  auto   off        0.0        0.0        n/a                 n/a  
Gi7/0/24  auto   off        0.0        0.0        n/a                 n/a  
Gi7/0/25  auto   off        0.0        0.0        n/a                 n/a  
Gi7/0/26  auto   on         4.0        4.0        Ieee PD             1    
Gi7/0/27  auto   on         4.0        4.0        Ieee PD             1    
Gi7/0/28  auto   on         15.4       15.4       Ieee PD             3    
Gi7/0/29  auto   off        0.0        0.0        n/a                 n/a  
Gi7/0/30  auto   off        0.0        0.0        n/a                 n/a  
Gi7/0/31  auto   off        0.0        0.0        n/a                 n/a  
Gi7/0/32  auto   on         4.0        4.0        Ieee PD             1    
Gi7/0/33  auto   on         30.0       30.0       Ieee PD             4    
Gi7/0/34  auto   off        0.0        0.0        n/a                 n/a  
Gi7/0/35  auto   off        0.0        0.0        n/a                 n/a  
Gi7/0/36  auto   off        0.0        0.0        n/a                 n/a  
Gi7/0/37  auto   on         4.0        4.0        Ieee PD             1    
Gi7/0/38  auto   off        0.0        0.0        n/a                 n/a  
Gi7/0/39  auto   off        0.0        0.0        n/a                 n/a  
Gi7/0/40  auto   off        0.0        0.0        n/a                 n/a  
Gi7/0/41  auto   off        0.0        0.0        n/a                 n/a  
Gi7/0/42  auto   on         4.0        4.0        Ieee PD             1    
Gi7/0/43  auto   off        0.0        0.0        n/a                 n/a  
Gi7/0/44  auto   on         4.0        4.0        Ieee PD             1    
Gi7/0/45  auto   on         4.0        4.0        Ieee PD             1    
Gi7/0/46  auto   off        0.0        0.0        n/a                 n/a  
Gi7/0/47  auto   off        0.0        0.0        n/a                 n/a  
Gi7/0/48  auto   on         4.0        4.0        Ieee PD             1    
Gi8/0/1   auto   off        0.0        0.0        n/a                 n/a  
Gi8/0/2   auto   on         4.0        4.0        Ieee PD             1    
Gi8/0/3   auto   off        0.0        0.0        n/a                 n/a  
Gi8/0/4   auto   off        0.0        0.0        n/a                 n/a  
Gi8/0/5   auto   on         4.0        4.0        Ieee PD             1    
Gi8/0/6   auto   off        0.0        0.0        n/a                 n/a  
Gi8/0/7   auto   off        0.0        0.0        n/a                 n/a  
Gi8/0/8   auto   off        0.0        0.0        n/a                 n/a  
Gi8/0/9   auto   off        0.0        0.0        n/a                 n/a  
Gi8/0/10  auto   off        0.0        0.0        n/a                 n/a  
Gi8/0/11  auto   on         4.0        4.0        Ieee PD             1    
Gi8/0/12  auto   on         4.0        4.0        Ieee PD             1    
Gi8/0/13  auto   off        0.0        0.0        n/a                 n/a  
Gi8/0/14  auto   off        0.0        0.0        n/a                 n/a  
Gi8/0/15  auto   on         4.0        4.0        Ieee PD             1    
          Interface Admin  Oper            Power(Watts)     Device              Class
                            From PS    To Device                    
--------- ------ ---------- ---------- ---------- ------------------- -----

Gi8/0/16  auto   off        0.0        0.0        n/a                 n/a  
Gi8/0/17  auto   off        0.0        0.0        n/a                 n/a  
Gi8/0/18  auto   on         4.0        4.0        Ieee PD             1    
Gi8/0/19  auto   off        0.0        0.0        n/a                 n/a  
Gi8/0/20  auto   off        0.0        0.0        n/a                 n/a  
Gi8/0/21  auto   off        0.0        0.0        n/a                 n/a  
Gi8/0/22  auto   off        0.0        0.0        n/a                 n/a  
Gi8/0/23  auto   on         4.0        4.0        Ieee PD             1    
Gi8/0/24  auto   off        0.0        0.0        n/a                 n/a  
Gi8/0/25  auto   on         4.0        4.0        Ieee PD             1    
Gi8/0/26  auto   off        0.0        0.0        n/a                 n/a  
Gi8/0/27  auto   off        0.0        0.0        n/a                 n/a  
Gi8/0/28  auto   on         4.0        4.0        Ieee PD             1    
Gi8/0/29  auto   off        0.0        0.0        n/a                 n/a  
Gi8/0/30  auto   off        0.0        0.0        n/a                 n/a  
Gi8/0/31  auto   off        0.0        0.0        n/a                 n/a  
Gi8/0/32  auto   on         4.0        4.0        Ieee PD             1    
Gi8/0/33  auto   on         4.0        4.0        Ieee PD             1    
Gi8/0/34  auto   on         4.0        4.0        Ieee PD             1    
Gi8/0/35  auto   on         4.0        4.0        Ieee PD             1    
Gi8/0/36  auto   off        0.0        0.0        n/a                 n/a  
Gi8/0/37  auto   off        0.0        0.0        n/a                 n/a  
Gi8/0/38  auto   off        0.0        0.0        n/a                 n/a  
Gi8/0/39  auto   off        0.0        0.0        n/a                 n/a  
Gi8/0/40  auto   off        0.0        0.0        n/a                 n/a  
Gi8/0/41  auto   off        0.0        0.0        n/a                 n/a  
Gi8/0/42  auto   off        0.0        0.0        n/a                 n/a  
Gi8/0/43  auto   off        0.0        0.0        n/a                 n/a  
Gi8/0/44  auto   off        0.0        0.0        n/a                 n/a  
Gi8/0/45  auto   on         4.0        4.0        Ieee PD             1    
Gi8/0/46  auto   off        0.0        0.0        n/a                 n/a  
Gi8/0/47  auto   off        0.0        0.0        n/a                 n/a  
Gi8/0/48  auto   off        0.0        0.0        n/a                 n/a  
--------- ------ ---------- ---------- ---------- ------------------- -----

Totals:          42   on    515.6      515.6     
""",
 'show environment all':"""Sensor List:  Environmental Monitoring 
 Sensor           Location          State             Reading
 Temp: Coretemp   R0                Normal            50 Celsius
 Temp: DopplerD   R0                Normal            80 Celsius
 V1: VX1          R0                Normal            871 mV
 V1: VX2          R0                Normal            1495 mV
 V1: VX3          R0                Normal            1055 mV
 V1: VX4          R0                Normal            852 mV
 V1: VX5          R0                Normal            1505 mV
 V1: VX6          R0                Normal            1300 mV
 V1: VX7          R0                Normal            1006 mV
 V1: VX8          R0                Normal            1098 mV
 V1: VX9          R0                Normal            1202 mV
 V1: VX10         R0                Normal            1702 mV
 V1: VX11         R0                Normal            1226 mV
 V1: VX12         R0                Normal            1801 mV
 V1: VX13         R0                Normal            2506 mV
 V1: VX14         R0                Normal            3302 mV
 V1: VX15         R0                Normal            5043 mV
 V1: VX16         R0                Normal            896 mV
 Temp:   outlet   R0                Normal            47 Celsius
 Temp:    inlet   R0                Normal            26 Celsius
 HotSwap: Volts   R0                Normal            53 V DC
 HotSwap: Power   R0                Normal            300 Watts
 V1: VX1          1/0               Normal            998 mV
 V1: VX2          1/0               Normal            1500 mV
 V1: VX3          1/0               Normal            1800 mV
 V1: VX4          1/0               Normal            3294 mV
 V1: VX5          1/0               Normal            3335 mV
 V1: VX6          1/0               Normal            1500 mV
 V1: VX7          1/0               Normal            1028 mV
 V1: VX8          1/0               Normal            3303 mV
 V1: VX9          1/0               Normal            11967 mV
 V1: VX10         1/0               Normal            1000 mV
 V1: VX11         1/0               Normal            1034 mV
 Temp:   Outlet   1/0               Normal            30 Celsius
 Temp:    Inlet   1/0               Normal            24 Celsius
 HotSwap: Volts   1/0               Normal            53 V DC
 HotSwap: Power   1/0               Normal            477 Watts
 V1: VX1          7/0               Normal            1000 mV
 V1: VX2          7/0               Normal            1499 mV
 V1: VX3          7/0               Normal            1795 mV
 V1: VX4          7/0               Normal            3295 mV
 V1: VX5          7/0               Normal            3329 mV
 V1: VX6          7/0               Normal            1499 mV
 V1: VX7          7/0               Normal            1030 mV
 V1: VX8          7/0               Normal            3305 mV
 V1: VX9          7/0               Normal            11999 mV
 V1: VX10         7/0               Normal            998 mV
 V1: VX11         7/0               Normal            1029 mV
 Temp:   Outlet   7/0               Normal            34 Celsius
 Temp:    Inlet   7/0               Normal            27 Celsius
 HotSwap: Volts   7/0               Normal            53 V DC
 HotSwap: Power   7/0               Normal            518 Watts
 V1: VX1          4/0               Normal            1028 mV
 V1: VX2          4/0               Normal            900 mV
 V1: VX3          4/0               Normal            1814 mV
 V1: VX4          4/0               Normal            3303 mV
 V1: VX5          4/0               Normal            3328 mV
           V1: VX6          4/0               Normal            1501 mV
 V1: VX7          4/0               Normal            996 mV
 V1: VX8          4/0               Normal            11939 mV
 V1: VX9          4/0               Normal            1033 mV
 V1: VX10         4/0               Normal            1034 mV
 V1: VX11         4/0               Normal            1038 mV
 V1: VX12         4/0               Normal            1036 mV
 Temp:   Outlet   4/0               Normal            35 Celsius
 Temp:    Inlet   4/0               Normal            32 Celsius
 HotSwap: Volts   4/0               Normal            53 V DC
 HotSwap: Power   4/0               Normal            493 Watts
 V1: VX1          8/0               Normal            1000 mV
 V1: VX2          8/0               Normal            1499 mV
 V1: VX3          8/0               Normal            1800 mV
 V1: VX4          8/0               Normal            3295 mV
 V1: VX5          8/0               Normal            3335 mV
 V1: VX6          8/0               Normal            1501 mV
 V1: VX7          8/0               Normal            1026 mV
 V1: VX8          8/0               Normal            3308 mV
 V1: VX9          8/0               Normal            12063 mV
 V1: VX10         8/0               Normal            1005 mV
 V1: VX11         8/0               Normal            1034 mV
 Temp:   Outlet   8/0               Normal            36 Celsius
 Temp:    Inlet   8/0               Normal            25 Celsius
 HotSwap: Volts   8/0               Normal            53 V DC
 HotSwap: Power   8/0               Normal            514 Watts

""",
}
