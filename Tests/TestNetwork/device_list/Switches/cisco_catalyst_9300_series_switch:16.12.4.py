ip_address = '172.31.6.133'
software = 'software'
hardware = 'hardware'
read_results = {
 'show version':"""Cisco IOS XE Software, Version 16.12.04
Cisco IOS Software [Gibraltar], Catalyst L3 Switch Software (CAT9K_IOSXE), Version 16.12.4, RELEASE SOFTWARE (fc5)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2020 by Cisco Systems, Inc.
Compiled Thu 09-Jul-20 21:49 by mcpre


Cisco IOS-XE software, Copyright (c) 2005-2020 by cisco Systems, Inc.
All rights reserved.  Certain components of Cisco IOS-XE software are
licensed under the GNU General Public License ("GPL") Version 2.0.  The
software code licensed under GPL Version 2.0 is free software that comes
with ABSOLUTELY NO WARRANTY.  You can redistribute and/or modify such
GPL code under the terms of GPL Version 2.0.  For more details, see the
documentation or "License Notice" file accompanying the IOS-XE software,
or the applicable URL provided on the flyer accompanying the IOS-XE
software.


ROM: IOS-XE ROMMON
BOOTLDR: System Bootstrap, Version 16.12.2r, RELEASE SOFTWARE (P)

dx1-874-383colorow-329-ebc uptime is 5 weeks, 18 hours, 5 minutes
Uptime for this control processor is 5 weeks, 18 hours, 6 minutes
System returned to ROM by PowerOn at 22:00:00 MDT Thu May 20 2021
System restarted at 22:10:15 MDT Thu May 20 2021
System image file is "flash:packages.conf"
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

------------------------------------------------------------------------------
Technology-package                                     Technology-package
Current                        Type                       Next reboot  
------------------------------------------------------------------------------
network-essentials  	Smart License                 	 network-essentials  
dna-essentials      	Subscription Smart License    	 dna-essentials                
AIR License Level: AIR DNA Advantage
Next reload AIR license Level: AIR DNA Advantage


Smart Licensing Status: UNREGISTERED/EVAL MODE
          
cisco C9300-48U (X86) processor with 1343576K/6147K bytes of memory.
Processor board ID FCW2210L069
2 Virtual Ethernet interfaces
52 Gigabit Ethernet interfaces
8 Ten Gigabit Ethernet interfaces
2 TwentyFive Gigabit Ethernet interfaces
2 Forty Gigabit Ethernet interfaces
2048K bytes of non-volatile configuration memory.
8388608K bytes of physical memory.
1638400K bytes of Crash Files at crashinfo:.
11264000K bytes of Flash at flash:.
0K bytes of WebUI ODM Files at webui:.

Base Ethernet MAC Address          : 68:2c:7b:d5:44:00
Motherboard Assembly Number        : 73-17957-07
Motherboard Serial Number          : FOC22064LXW
Model Revision Number              : E0
Motherboard Revision Number        : B0
Model Number                       : C9300-48U
System Serial Number               : FCW2210L069


Switch Ports Model              SW Version        SW Image              Mode   
------ ----- -----              ----------        ----------            ----   
*    1 65    C9300-48U          16.12.4           CAT9K_IOSXE           INSTALL


Configuration register is 0x102
""",
 'show run':"""Building configuration...

Current configuration : 21626 bytes
!
! Last configuration change at 22:10:25 MDT Thu May 20 2021
! NVRAM config last updated at 21:32:15 MDT Sun Jun 20 2021 by noc-orionncm
!
version 16.12
no service pad
service timestamps debug datetime msec localtime
service timestamps log datetime msec localtime
service password-encryption
service compress-config
! Call-home is enabled by Smart-Licensing.
service call-home
no platform punt-keepalive disable-kernel-core
!
hostname dx1-874-383colorow-329-ebc
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
enable secret 9 $14$CxsE$KltBzzPeOWCfEE$SMUHmKEAcRvQvNjmsCBpe96pgGelop9jpEEJiSKkyc2
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
boot system switch all flash:packages.conf
clock timezone MST -7 0
          clock summer-time MDT recurring
switch 1 provision c9300-48u
software auto-upgrade enable
!
!
!
!
!
call-home
 ! If contact email address in call-home is configured as sch-smart-licensing@cisco.com
 ! the email address configured in Cisco Smart License Portal will be used as contact email address to send SCH notifications.
 contact-email-addr sch-smart-licensing@cisco.com
 profile "CiscoTAC-1"
  active
  destination transport-method http
  no destination transport-method email
no ip source-route
!
ip name-server 172.20.120.20
ip domain name net.utah.edu
!
!
!
ip dhcp snooping
login on-success log
!
!
!
!
!
vtp domain vtp-874-383colorow
vtp mode transparent
udld aggressive

authentication mac-move permit
no device-tracking logging theft
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
crypto pki trustpoint TP-self-signed-2670762493
 enrollment selfsigned
 subject-name cn=IOS-Self-Signed-Certificate-2670762493
 revocation-check none
 rsakeypair TP-self-signed-2670762493
!
crypto pki trustpoint SLA-TrustPoint
 enrollment pkcs12
 revocation-check crl
!
!
crypto pki certificate chain TP-self-signed-2670762493
 certificate self-signed 01
  30820330 30820218 A0030201 02020101 300D0609 2A864886 F70D0101 05050030 
  31312F30 2D060355 04031326 494F532D 53656C66 2D536967 6E65642D 43657274 
  69666963 6174652D 32363730 37363234 3933301E 170D3138 31313037 31393333 
  32345A17 0D323030 31303130 30303030 305A3031 312F302D 06035504 03132649 
  4F532D53 656C662D 5369676E 65642D43 65727469 66696361 74652D32 36373037 
  36323439 33308201 22300D06 092A8648 86F70D01 01010500 0382010F 00308201 
  0A028201 0100C13D 417EDADB D3B61D12 47378DAB E543AC3B D0F46BF1 8860379C 
  68A44B46 460053C7 D90C90BB 454A4175 481612B5 630961CA C2E152F8 76E78388 
  4899E85E A89604D4 35EB2140 4B35071C C0B5EA74 23100190 6C1DBFD4 93D3996E 
  920A1DA2 2734C344 4B92F616 F76FB968 66B2A7DB FAE66F41 11C80ECB 840E7C17 
  85ACCCBE 8F541A5D BF31F30F 73DA4E1E 1DA5DABC 75B259BE CC0D03B7 A02501D4 
  F27C694C 606CB027 F159C8EE 5547F583 9B34410E C517F981 9929B663 2537E305 
  FB0F4347 5A39B68B E257ACF2 3F7DF7B0 1617FA50 33B3E2C1 6C40CB00 A8C6C37C 
  6049C0FC E1E57641 9D754D49 B6BA4120 30D18ABE 0A998A1C D17E55B0 5685EDDC 
  DCF402C7 99650203 010001A3 53305130 0F060355 1D130101 FF040530 030101FF 
  301F0603 551D2304 18301680 1450F371 F7D4183D 418FB6AB AF602923 4C41AA9C 
  A9301D06 03551D0E 04160414 50F371F7 D4183D41 8FB6ABAF 6029234C 41AA9CA9 
  300D0609 2A864886 F70D0101 05050003 82010100 8CFEFE2F 8D3EA7BE F337CEA3 
  FC51AEC9 E084A8F2 6AD34B93 8C791A6B 747991F8 2D3A91A2 A461D56F CA6F8209 
  CF2994D5 14632BB4 C4675414 8A806CB8 0ECAE5A7 ABF6DF29 65CE8E85 FE93CCD7 
  AF59E87C 6C6BBCEA C4EE41D6 6C48CCCF DDFD8833 7D93DE2E 62A9B01C 21E8BCEF 
  2ACFF822 0E0DF21F D84F6AA5 60188E14 4F6D33E2 C1EDA783 CC456DA5 C2A3B7C9 
  06E3D194 05BF84A9 05D5AF10 ED115CCF 3F7609A1 2F5D5C70 97FE3BDC AC034639 
  FB0D80F5 FDDD2AC8 A6608546 82999DFD 6B71D897 C9F7753C CF159503 9211105C 
  AC71CE06 573783E1 BAAFE77E 846F972D 9665AFFA 37FA946C 3601C54B E9A79151 
  173F3C25 9A080895 6AC878D3 7C6847DA C51910D0
  	quit
crypto pki certificate chain SLA-TrustPoint
 certificate ca 01
  30820321 30820209 A0030201 02020101 300D0609 2A864886 F70D0101 0B050030 
  32310E30 0C060355 040A1305 43697363 6F312030 1E060355 04031317 43697363 
  6F204C69 63656E73 696E6720 526F6F74 20434130 1E170D31 33303533 30313934 
  3834375A 170D3338 30353330 31393438 34375A30 32310E30 0C060355 040A1305 
  43697363 6F312030 1E060355 04031317 43697363 6F204C69 63656E73 696E6720 
  526F6F74 20434130 82012230 0D06092A 864886F7 0D010101 05000382 010F0030 
  82010A02 82010100 A6BCBD96 131E05F7 145EA72C 2CD686E6 17222EA1 F1EFF64D 
  CBB4C798 212AA147 C655D8D7 9471380D 8711441E 1AAF071A 9CAE6388 8A38E520 
  1C394D78 462EF239 C659F715 B98C0A59 5BBB5CBD 0CFEBEA3 700A8BF7 D8F256EE 
  4AA4E80D DB6FD1C9 60B1FD18 FFC69C96 6FA68957 A2617DE7 104FDC5F EA2956AC 
  7390A3EB 2B5436AD C847A2C5 DAB553EB 69A9A535 58E9F3E3 C0BD23CF 58BD7188 
  68E69491 20F320E7 948E71D7 AE3BCC84 F10684C7 4BC8E00F 539BA42B 42C68BB7 
  C7479096 B4CB2D62 EA2F505D C7B062A4 6811D95B E8250FC4 5D5D5FB8 8F27D191 
  C55F0D76 61F9A4CD 3D992327 A8BB03BD 4E6D7069 7CBADF8B DF5F4368 95135E44 
  DFC7C6CF 04DD7FD1 02030100 01A34230 40300E06 03551D0F 0101FF04 04030201 
            06300F06 03551D13 0101FF04 05300301 01FF301D 0603551D 0E041604 1449DC85 
  4B3D31E5 1B3E6A17 606AF333 3D3B4C73 E8300D06 092A8648 86F70D01 010B0500 
  03820101 00507F24 D3932A66 86025D9F E838AE5C 6D4DF6B0 49631C78 240DA905 
  604EDCDE FF4FED2B 77FC460E CD636FDB DD44681E 3A5673AB 9093D3B1 6C9E3D8B 
  D98987BF E40CBD9E 1AECA0C2 2189BB5C 8FA85686 CD98B646 5575B146 8DFC66A8 
  467A3DF4 4D565700 6ADF0F0D CF835015 3C04FF7C 21E878AC 11BA9CD2 55A9232C 
  7CA7B7E6 C1AF74F6 152E99B7 B1FCF9BB E973DE7F 5BDDEB86 C71E3B49 1765308B 
  5FB0DA06 B92AFE7F 494E8A9E 07B85737 F3A58BE1 1A48A229 C37C1E69 39F08678 
  80DDCD16 D6BACECA EEBC7CF9 8428787B 35202CDC 60E4616A B623CDBD 230E3AFB 
  418616A9 4093E049 4D10AB75 27E86F73 932E35B5 8862FDAE 0275156F 719BB2F0 
  D697DF7F 28
  	quit
!
license boot level network-essentials addon dna-essentials
!
!
diagnostic bootup level minimal
!
spanning-tree mode rapid-pvst
spanning-tree extend system-id
spanning-tree vlan 1-4094 priority 16384
memory free low-watermark processor 134344
file prompt quiet
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
errdisable recovery cause storm-control
errdisable recovery cause inline-power
errdisable recovery cause arp-inspection
errdisable recovery cause link-monitor-failure
errdisable recovery cause oam-remote-failure
errdisable recovery cause loopback
errdisable recovery cause psp
!
redundancy
 mode sso
!
!
!
!
!
transceiver type all
 monitoring
!
vlan 31
 name 3rdFloor-data
          !
vlan 33
 name voice
!
vlan 34
 name ebc-874_383colorow-COH
!
vlan 35
 name ebc-874-383colorow-navigen-data
!
vlan 36
 name ebc-874-383colorow-navigen-voice
!
vlan 40
 name ebc-874-COH-printers
!
vlan 330
 name ebc-874_383Colorow_HVAC
!
vlan 623
 name ebc-874_383colorow-ccure
!
vlan 702
 name ebc-874_383colorow-psychresearch
!
vlan 779
 name ebc-874_383Colorow-ehs
!
vlan 845
 name ebc-874_383Colorow-m
!
vlan 1024
 name ebc-874_383colorow-clinical
!
vlan 1034
 name ebc-874_383colorow-PublicAffairs
!
vlan 1045
 name ebc-874-gslc-wkstn
!
vlan 1095
 name ebc-874_383colorow-fm-wyse
!
vlan 1097
 name PATH-future-use
!
vlan 1160
 name ebc-874-383colorow-brainimaging
!
vlan 1603
 name ebc-874colorow-fm-cam
lldp run
!
!
class-map match-any system-cpp-police-ewlc-control
  description EWLC Control 
class-map match-any system-cpp-police-topology-control
  description Topology control
class-map match-any system-cpp-police-sw-forward
            description Sw forwarding, L2 LVX data packets, LOGGING, Transit Traffic
class-map match-any system-cpp-default
  description EWLC Data, Inter FED Traffic 
class-map match-any system-cpp-police-sys-data
  description Openflow, Exception, EGR Exception, NFL Sampled Data, RPF Failed
class-map match-any system-cpp-police-punt-webauth
  description Punt Webauth
class-map match-any system-cpp-police-l2lvx-control
  description L2 LVX control packets
class-map match-any system-cpp-police-forus
  description Forus Address resolution and Forus traffic
class-map match-any system-cpp-police-multicast-end-station
  description MCAST END STATION
class-map match-any system-cpp-police-high-rate-app
  description High Rate Applications 
class-map match-any system-cpp-police-multicast
  description MCAST Data
class-map match-any system-cpp-police-l2-control
  description L2 control
class-map match-any system-cpp-police-dot1x-auth
  description DOT1X Auth
class-map match-any system-cpp-police-data
  description ICMP redirect, ICMP_GEN and BROADCAST
class-map match-any system-cpp-police-stackwise-virt-control
  description Stackwise Virtual OOB
class-map match-any system-cpp-police-control-low-priority
  description General punt
class-map match-any non-client-nrt-class
class-map match-any system-cpp-police-routing-control
  description Routing control and Low Latency
class-map match-any system-cpp-police-protocol-snooping
  description Protocol snooping
class-map match-any system-cpp-police-dhcp-snooping
  description DHCP snooping
class-map match-any system-cpp-police-ios-routing
  description L2 control, Topology control, Routing control, Low Latency
class-map match-any system-cpp-police-system-critical
  description System Critical and Gold Pkt
class-map match-any system-cpp-police-ios-feature
  description ICMPGEN,BROADCAST,ICMP,L2LVXCntrl,ProtoSnoop,PuntWebauth,MCASTData,Transit,DOT1XAuth,Swfwd,LOGGING,L2LVXData,ForusTraffic,ForusARP,McastEndStn,Openflow,Exception,EGRExcption,NflSampled,RpfFailed
!
policy-map system-cpp-policy
 class system-cpp-police-sys-data
  police rate 100 pps
 class system-cpp-police-multicast
  police rate 500 pps
 class system-cpp-police-control-low-priority
  police rate 200 pps
 class system-cpp-police-forus
  police rate 1000 pps
 class system-cpp-default
  police rate 1000 pps
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
 shutdown
 negotiation auto
!
interface GigabitEthernet1/0/1
 description VLAN 702 psychresearch
 switchport access vlan 702
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/2
 description VLAN 702 psychresearch
 switchport access vlan 702
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/3
 description VLAN 702 psychresearch
 switchport access vlan 702
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/4
 description VLAN 702 psychresearch
 switchport access vlan 702
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/5
 description VLAN 702 psychresearch
 switchport access vlan 702
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/6
 description VLAN 702 psychresearch
 switchport access vlan 702
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/7
 description VLAN 702 psychresearch
 switchport access vlan 702
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/8
 description VLAN 702 psychresearch
           switchport access vlan 702
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/9
!
interface GigabitEthernet1/0/10
!
interface GigabitEthernet1/0/11
 description VLAN 1603 FM CAM
 switchport access vlan 1603
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/12
 description VLAN 1603 FM CAM
 switchport access vlan 1603
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/13
 description VLAN 1603 FM CAM
 switchport access vlan 1603
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/14
 description VLAN 1603 FM CAM
 switchport access vlan 1603
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/15
 switchport access vlan 1603
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/16
 switchport access vlan 1603
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/17
 description VLAN 31 Building Data
 switchport access vlan 31
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/18
!
interface GigabitEthernet1/0/19
!
interface GigabitEthernet1/0/20
!
interface GigabitEthernet1/0/21
!
interface GigabitEthernet1/0/22
!
interface GigabitEthernet1/0/23
          !
interface GigabitEthernet1/0/24
!
interface GigabitEthernet1/0/25
 description VLAN 35 Navigen-data
 switchport access vlan 35
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/26
 description VLAN 36 Navigen-VOIP
 switchport access vlan 36
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/27
 switchport access vlan 1603
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/28
 switchport access vlan 1603
 switchport mode access
 spanning-tree portfast
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
!
interface GigabitEthernet1/0/48
!
interface GigabitEthernet1/1/1
!
interface GigabitEthernet1/1/2
!
interface GigabitEthernet1/1/3
!
interface GigabitEthernet1/1/4
!
interface TenGigabitEthernet1/1/1
 description key:t1/1/1:r1-ebc-ebc:e2/19
 switchport mode trunk
 channel-group 30 mode active
 ip dhcp snooping trust
!
interface TenGigabitEthernet1/1/2
 description key:t1/1/2:r2-ebc-park:e2/19
 switchport mode trunk
 channel-group 30 mode active
 ip dhcp snooping trust
!
interface TenGigabitEthernet1/1/3
 description key:t1/1/3:sx1-874-383colorow-177-ebc:t1/1/2
 switchport mode trunk
!
interface TenGigabitEthernet1/1/4
 description #key:t1/1/4:sx2-874-374:t1/1/1
 switchport mode trunk
!
interface TenGigabitEthernet1/1/5
 description key:t1/1/5:sx1-874-383colorow-273-ebc:t1/1/1
 switchport mode trunk
!
interface TenGigabitEthernet1/1/6
!
interface TenGigabitEthernet1/1/7
 description key:t1/1/7:sx1-874-383colorow-374-ebc:t1/1/1
 switchport mode trunk
!
interface TenGigabitEthernet1/1/8
!
interface FortyGigabitEthernet1/1/1
!
interface FortyGigabitEthernet1/1/2
!
interface TwentyFiveGigE1/1/1
!
interface TwentyFiveGigE1/1/2
!
interface AppGigabitEthernet1/0/1
!
interface Vlan1
 no ip address
 shutdown
          !
interface Vlan845
 description ebc-874-383colorow-m
 ip address 172.31.6.133 255.255.255.192
!
ip default-gateway 172.31.6.129
ip forward-protocol nd
no ip http server
no ip http secure-server
ip ssh version 2
!
!
ip sla enable reaction-alerts
logging facility local6
logging source-interface Vlan845
logging host 155.98.253.244
logging host 155.98.204.52
logging host 172.24.29.14
logging host 10.70.24.10
logging host 10.71.24.11
ip access-list standard 70
 10 remark == Update 4-26-2021
 10 remark ======= NOC SNMP RO =======
 10 permit 10.64.2.70
 20 permit 10.71.25.65
 30 permit 155.100.126.163
 40 permit 155.100.126.162
 50 permit 10.71.24.21
 60 permit 10.71.24.20
 70 permit 10.71.24.23
 80 permit 10.71.24.22
 90 permit 10.71.24.17
 100 permit 10.71.24.16
 110 permit 10.71.24.19
 120 permit 10.71.24.18
 130 permit 172.20.150.100
 140 permit 10.71.24.25
 150 permit 10.71.24.13
 160 permit 10.71.24.12
 170 permit 10.71.24.15
 180 permit 10.71.24.14
 190 permit 10.71.24.11
 200 permit 155.100.123.72
 210 permit 10.71.25.164
 220 permit 155.98.164.192 0.0.0.31
 230 permit 155.99.254.128 0.0.0.127
 240 permit 155.98.253.0 0.0.0.255
 250 deny   any log
ip access-list standard 71
 10 remark == Update 4-26-2021
 10 remark ======= NOC SNMP RW =======
 10 permit 10.64.2.70
 20 permit 10.71.25.65
 30 permit 155.100.126.163
 40 permit 155.100.126.162
 50 permit 10.71.24.21
 60 permit 10.71.24.20
 70 permit 10.71.24.23
 80 permit 10.71.24.22
           90 permit 10.71.24.17
 100 permit 10.71.24.16
 110 permit 10.71.24.19
 120 permit 10.71.24.18
 130 permit 172.20.150.100
 140 permit 10.71.24.25
 150 permit 10.71.24.13
 160 permit 10.71.24.12
 170 permit 10.71.24.15
 180 permit 10.71.24.14
 190 permit 10.71.24.11
 200 permit 155.100.123.72
 210 permit 10.71.25.164
 220 permit 155.98.164.192 0.0.0.31
 230 permit 155.99.254.128 0.0.0.127
 240 permit 155.98.253.0 0.0.0.255
 250 deny   any log
ip access-list extended 199
 10 remark == Update 4-26-2021 ==
 10 remark ====== line VTY 0-15 inbound =====
 10 remark ------ NetOpS Workstations-Servers-Pollers --------
 10 permit tcp 155.98.253.0 0.0.0.255 any eq 22
 20 permit tcp host 172.20.150.100 any eq 22
 30 permit tcp host 155.100.126.162 any eq 22
 40 permit tcp host 155.100.126.163 any eq 22
 50 permit tcp host 10.64.2.70 any eq 22
 60 remark ----- door1 & door2 ---------------------------
 60 permit tcp host 155.99.239.130 any eq 22
 70 permit tcp host 155.97.152.244 any eq 22
 80 remark ----- NOC Citrix IP -------------------------
 80 permit tcp host 155.100.123.72 any eq 22
 90 remark ----- Wireless Subnet -------------------------
 90 permit tcp 155.99.254.128 0.0.0.127 any eq 22
 100 remark ------ VPN Connections ------------------------
 100 permit tcp 155.98.164.192 0.0.0.31 any eq 22
 110 remark -----New Orion Address-----------
 110 permit tcp host 10.71.24.11 any eq 22
 120 permit tcp host 10.71.24.12 any eq 22
 130 permit tcp host 10.71.24.13 any eq 22
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
 270 deny   ip any any log
!
snmp-server group CliNOCGrv3RO v3 priv read CliNOCViewRO access 70
snmp-server group CliNOCGrv3RO v3 auth context vlan- match prefix 
snmp-server group CliNOCGrv3RW v3 priv write CliNOCViewRW access 71
snmp-server view CliNOCViewRO internet included
snmp-server view CliNOCViewRW internet included
          snmp-server location Bldg. 874 Room 329
snmp-server contact BC-508870 Y-321300
snmp ifmib ifindex persist
tacacs server TAC-EBC
 address ipv4 172.31.17.180
 key 7 022F405E22420A036C4C1058
tacacs server TAC-SECONDARY
 address ipv4 10.64.32.5
 key 7 143E560E25402F09042A2A74
!
!
!
control-plane
 service-policy input system-cpp-policy
!
privilege exec level 1 show configuration
privilege exec level 1 show
banner login ^C
dx1-874-383colorow-329-ebc

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
 password 7 09795A08110756415F
 login authentication console
 stopbits 1
line vty 0 4
 access-class 199 in
 exec-timeout 30 0
 password 7 053E120E294E0F5A4D
 transport input ssh
line vty 5 15
 access-class 199 in
 exec-timeout 30 0
 password 7 053E120E294E0F5A4D
 transport input ssh
!
ntp server time.utah.edu
!
!
!
!
!
!
end
          """,
 'show int status':"""Port         Name               Status       Vlan       Duplex  Speed Type
Gi1/0/1      VLAN 702 psychrese connected    702        a-full a-1000 10/100/1000BaseTX
Gi1/0/2      VLAN 702 psychrese connected    702        a-full a-1000 10/100/1000BaseTX
Gi1/0/3      VLAN 702 psychrese connected    702        a-full a-1000 10/100/1000BaseTX
Gi1/0/4      VLAN 702 psychrese connected    702        a-full a-1000 10/100/1000BaseTX
Gi1/0/5      VLAN 702 psychrese connected    702        a-full a-1000 10/100/1000BaseTX
Gi1/0/6      VLAN 702 psychrese connected    702        a-full a-1000 10/100/1000BaseTX
Gi1/0/7      VLAN 702 psychrese notconnect   702          auto   auto 10/100/1000BaseTX
Gi1/0/8      VLAN 702 psychrese notconnect   702          auto   auto 10/100/1000BaseTX
Gi1/0/9                         notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/10                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/11     VLAN 1603 FM CAM   connected    1603       a-full  a-100 10/100/1000BaseTX
Gi1/0/12     VLAN 1603 FM CAM   connected    1603       a-full  a-100 10/100/1000BaseTX
Gi1/0/13     VLAN 1603 FM CAM   notconnect   1603         auto   auto 10/100/1000BaseTX
Gi1/0/14     VLAN 1603 FM CAM   notconnect   1603         auto   auto 10/100/1000BaseTX
Gi1/0/15                        notconnect   1603         auto   auto 10/100/1000BaseTX
Gi1/0/16                        notconnect   1603         auto   auto 10/100/1000BaseTX
Gi1/0/17     VLAN 31 Building D connected    31         a-full a-1000 10/100/1000BaseTX
Gi1/0/18                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/19                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/20                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/21                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/22                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/23                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/24                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/25     VLAN 35 Navigen-da notconnect   35           auto   auto 10/100/1000BaseTX
Gi1/0/26     VLAN 36 Navigen-VO notconnect   36           auto   auto 10/100/1000BaseTX
Gi1/0/27                        connected    1603       a-full  a-100 10/100/1000BaseTX
Gi1/0/28                        connected    1603       a-full  a-100 10/100/1000BaseTX
Gi1/0/29                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/30                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/31                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/32                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/33                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/34                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/35                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/36                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/37                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/38                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/39                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/40                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/41                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/42                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/43                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/44                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/45                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/46                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/47                        notconnect   1            auto   auto 10/100/1000BaseTX
Gi1/0/48                        notconnect   1            auto   auto 10/100/1000BaseTX
Te1/1/1      key:t1/1/1:r1-ebc- connected    trunk        full    10G SFP-10GBase-LR
Te1/1/2      key:t1/1/2:r2-ebc- connected    trunk        full    10G SFP-10GBase-LR
Te1/1/3      key:t1/1/3:sx1-874 connected    trunk        full    10G SFP-10GBase-LR
Te1/1/4      #key:t1/1/4:sx2-87 connected    trunk        full    10G SFP-10GBase-LR
Te1/1/5      key:t1/1/5:sx1-874 connected    trunk        full    10G SFP-10GBase-LR
Te1/1/6                         notconnect   1            auto   auto unknown
Te1/1/7      key:t1/1/7:sx1-874 connected    trunk        full    10G SFP-10GBase-LR
Te1/1/8                         notconnect   1            auto   auto unknown
Ap1/0/1                         connected    1          a-full a-1000 App-hosting port
          
Port         Name               Status       Vlan       Duplex  Speed Type
Po30         key:Uplink to dist connected    trunk      a-full  a-10G N/A""",
 'show run | section interface':"""match interface input
 collect interface output
interface Port-channel30
 description key:Uplink to dist nodes
 switchport mode trunk
 ip dhcp snooping trust
interface GigabitEthernet0/0
 vrf forwarding Mgmt-vrf
 no ip address
 shutdown
 negotiation auto
interface GigabitEthernet1/0/1
 description VLAN 702 psychresearch
 switchport access vlan 702
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/2
 description VLAN 702 psychresearch
 switchport access vlan 702
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/3
 description VLAN 702 psychresearch
 switchport access vlan 702
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/4
 description VLAN 702 psychresearch
 switchport access vlan 702
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/5
 description VLAN 702 psychresearch
 switchport access vlan 702
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/6
 description VLAN 702 psychresearch
 switchport access vlan 702
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/7
 description VLAN 702 psychresearch
 switchport access vlan 702
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/8
 description VLAN 702 psychresearch
 switchport access vlan 702
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/9
interface GigabitEthernet1/0/10
interface GigabitEthernet1/0/11
 description VLAN 1603 FM CAM
 switchport access vlan 1603
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/12
           description VLAN 1603 FM CAM
 switchport access vlan 1603
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/13
 description VLAN 1603 FM CAM
 switchport access vlan 1603
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/14
 description VLAN 1603 FM CAM
 switchport access vlan 1603
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/15
 switchport access vlan 1603
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/16
 switchport access vlan 1603
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/17
 description VLAN 31 Building Data
 switchport access vlan 31
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/18
interface GigabitEthernet1/0/19
interface GigabitEthernet1/0/20
interface GigabitEthernet1/0/21
interface GigabitEthernet1/0/22
interface GigabitEthernet1/0/23
interface GigabitEthernet1/0/24
interface GigabitEthernet1/0/25
 description VLAN 35 Navigen-data
 switchport access vlan 35
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/26
 description VLAN 36 Navigen-VOIP
 switchport access vlan 36
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/27
 switchport access vlan 1603
 switchport mode access
 spanning-tree portfast
interface GigabitEthernet1/0/28
 switchport access vlan 1603
 switchport mode access
 spanning-tree portfast
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
interface GigabitEthernet1/1/1
interface GigabitEthernet1/1/2
interface GigabitEthernet1/1/3
interface GigabitEthernet1/1/4
interface TenGigabitEthernet1/1/1
 description key:t1/1/1:r1-ebc-ebc:e2/19
 switchport mode trunk
 channel-group 30 mode active
 ip dhcp snooping trust
interface TenGigabitEthernet1/1/2
 description key:t1/1/2:r2-ebc-park:e2/19
 switchport mode trunk
 channel-group 30 mode active
 ip dhcp snooping trust
interface TenGigabitEthernet1/1/3
 description key:t1/1/3:sx1-874-383colorow-177-ebc:t1/1/2
 switchport mode trunk
interface TenGigabitEthernet1/1/4
 description #key:t1/1/4:sx2-874-374:t1/1/1
 switchport mode trunk
interface TenGigabitEthernet1/1/5
 description key:t1/1/5:sx1-874-383colorow-273-ebc:t1/1/1
 switchport mode trunk
interface TenGigabitEthernet1/1/6
interface TenGigabitEthernet1/1/7
 description key:t1/1/7:sx1-874-383colorow-374-ebc:t1/1/1
 switchport mode trunk
interface TenGigabitEthernet1/1/8
interface FortyGigabitEthernet1/1/1
interface FortyGigabitEthernet1/1/2
interface TwentyFiveGigE1/1/1
interface TwentyFiveGigE1/1/2
interface AppGigabitEthernet1/0/1
interface Vlan1
 no ip address
 shutdown
interface Vlan845
 description ebc-874-383colorow-m
 ip address 172.31.6.133 255.255.255.192
logging source-interface Vlan845""",
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
interface GigabitEthernet1/1/1
interface GigabitEthernet1/1/2
interface GigabitEthernet1/1/3
interface GigabitEthernet1/1/4
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
interface TwentyFiveGigE1/1/1
interface TwentyFiveGigE1/1/2
interface AppGigabitEthernet1/0/1
interface Vlan1
interface Vlan845
logging source-interface Vlan845""",
 'show interface link':"""Port           Name               Down Time      Up Time
Gi1/0/1        VLAN 702 psychrese 00:00:00       5w0d
Gi1/0/2        VLAN 702 psychrese 00:00:00       4w2d
Gi1/0/3        VLAN 702 psychrese 00:00:00       5w0d
Gi1/0/4        VLAN 702 psychrese 00:00:00       5w0d
Gi1/0/5        VLAN 702 psychrese 00:00:00       5w0d
Gi1/0/6        VLAN 702 psychrese 00:00:00       5w0d
Gi1/0/7        VLAN 702 psychrese 5w0d
Gi1/0/8        VLAN 702 psychrese 5w0d
Gi1/0/9                           5w0d
Gi1/0/10                          5w0d
Gi1/0/11       VLAN 1603 FM CAM   00:00:00       2d21h
Gi1/0/12       VLAN 1603 FM CAM   00:00:00       2d21h
Gi1/0/13       VLAN 1603 FM CAM   5w0d
Gi1/0/14       VLAN 1603 FM CAM   5w0d
Gi1/0/15                          5w0d
Gi1/0/16                          5w0d
Gi1/0/17       VLAN 31 Building D 00:00:00       4d04h
Gi1/0/18                          5w0d
Gi1/0/19                          5w0d
Gi1/0/20                          5w0d
Gi1/0/21                          5w0d
Gi1/0/22                          5w0d
Gi1/0/23                          5w0d
Gi1/0/24                          5w0d
Gi1/0/25       VLAN 35 Navigen-da 5w0d
Gi1/0/26       VLAN 36 Navigen-VO 5w0d
Gi1/0/27                          00:00:00       2d21h
Gi1/0/28                          00:00:00       2d21h
Gi1/0/29                          5w0d
Gi1/0/30                          5w0d
Gi1/0/31                          5w0d
Gi1/0/32                          5w0d
Gi1/0/33                          5w0d
Gi1/0/34                          5w0d
Gi1/0/35                          5w0d
Gi1/0/36                          5w0d
Gi1/0/37                          5w0d
Gi1/0/38                          5w0d
Gi1/0/39                          5w0d
Gi1/0/40                          5w0d
Gi1/0/41                          5w0d
Gi1/0/42                          5w0d
Gi1/0/43                          5w0d
Gi1/0/44                          5w0d
Gi1/0/45                          5w0d
Gi1/0/46                          5w0d
Gi1/0/47                          5w0d
Gi1/0/48                          5w0d
Gi1/1/1                           5w0d
Gi1/1/2                           5w0d
Gi1/1/3                           5w0d
Gi1/1/4                           5w0d
Te1/1/1        key:t1/1/1:r1-ebc- 00:00:00       5w0d
Te1/1/2        key:t1/1/2:r2-ebc- 00:00:00       5w0d
Te1/1/3        key:t1/1/3:sx1-874 00:00:00       2w0d
Te1/1/4        #key:t1/1/4:sx2-87 00:00:00       5w0d
Te1/1/5        key:t1/1/5:sx1-874 00:00:00       5w0d
          
Port           Name               Down Time      Up Time
Te1/1/6                           5w0d
Te1/1/7        key:t1/1/7:sx1-874 00:00:00       5w0d
Te1/1/8                           5w0d
Fo1/1/1                           5w0d
Fo1/1/2                           5w0d
Twe1/1/1                          5w0d
Twe1/1/2                          5w0d
Ap1/0/1                           00:00:00       5w0d""",
 'show interface':"""Vlan1 is administratively down, line protocol is down , Autostate Enabled
  Hardware is Ethernet SVI, address is 682c.7bd5.4447 (bia 682c.7bd5.4447)
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
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 packets output, 0 bytes, 0 underruns
     Output 0 broadcasts (0 IP multicasts)
     0 output errors, 1 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
Vlan845 is up, line protocol is up , Autostate Enabled
  Hardware is Ethernet SVI, address is 682c.7bd5.447c (bia 682c.7bd5.447c)
  Description: ebc-874-383colorow-m
  Internet address is 172.31.6.133/26
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output 00:00:00, output hang never
  Last clearing of "" counters never
  Input queue: 1/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 2441000 bits/sec, 496 packets/sec
     2163738 packets input, 263968028 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     1612255235 packets output, 846437052758 bytes, 0 underruns
     Output 0 broadcasts (0 IP multicasts)
     0 output errors, 2 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet0/0 is administratively down, line protocol is down 
  Hardware is RP management port, address is 682c.7bd5.4400 (bia 682c.7bd5.4400)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full Duplex, 1000Mbps, link type is auto, media type is RJ45
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
     12 packets output, 1048 bytes, 0 underruns
     Output 0 broadcasts (0 IP multicasts)
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
     0 carrier transitions
GigabitEthernet1/0/1 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 682c.7bd5.4401 (bia 682c.7bd5.4401)
  Description: VLAN 702 psychresearch
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is on, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 00:00:00, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 1000 bits/sec, 1 packets/sec
  5 minute output rate 2000 bits/sec, 2 packets/sec
     1119438 packets input, 148452439 bytes, 0 no buffer
     Received 2 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     6916026 packets output, 681606293 bytes, 0 underruns
     Output 956159 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/2 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 682c.7bd5.4402 (bia 682c.7bd5.4402)
  Description: VLAN 702 psychresearch
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is on, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 00:00:01, output hang never
            Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 29342
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 1000 bits/sec, 2 packets/sec
     839513 packets input, 544005709 bytes, 0 no buffer
     Received 1935 broadcasts (1883 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 1883 multicast, 0 pause input
     0 input packets with dribble condition detected
     7171269 packets output, 1987658951 bytes, 0 underruns
     Output 956100 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/3 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 682c.7bd5.4403 (bia 682c.7bd5.4403)
  Description: VLAN 702 psychresearch
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 23/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is on, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 00:00:01, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 19570
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 90317000 bits/sec, 8079 packets/sec
  5 minute output rate 4297000 bits/sec, 7800 packets/sec
     1397992295 packets input, 1755035618342 bytes, 0 no buffer
     Received 11269 broadcasts (2563 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 2563 multicast, 0 pause input
     0 input packets with dribble condition detected
     1816185274 packets output, 1012197869207 bytes, 0 underruns
     Output 947458 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/4 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 682c.7bd5.4404 (bia 682c.7bd5.4404)
  Description: VLAN 702 psychresearch
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is on, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
            Last input never, output 00:00:00, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 1000 bits/sec, 2 packets/sec
     270889 packets input, 22717397 bytes, 0 no buffer
     Received 866 broadcasts (842 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 842 multicast, 0 pause input
     0 input packets with dribble condition detected
     6094827 packets output, 570078059 bytes, 0 underruns
     Output 956140 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/5 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 682c.7bd5.4405 (bia 682c.7bd5.4405)
  Description: VLAN 702 psychresearch
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is on, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 00:00:00, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 1000 bits/sec, 2 packets/sec
  5 minute output rate 2000 bits/sec, 4 packets/sec
     1498295 packets input, 131195419 bytes, 0 no buffer
     Received 1 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     7479939 packets output, 681611512 bytes, 0 underruns
     Output 956163 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/6 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 682c.7bd5.4406 (bia 682c.7bd5.4406)
  Description: VLAN 702 psychresearch
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is on, output flow-control is unsupported 
            ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 00:00:00, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 1000 bits/sec, 1 packets/sec
  5 minute output rate 3000 bits/sec, 3 packets/sec
     1914709 packets input, 200678437 bytes, 0 no buffer
     Received 2 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     7941704 packets output, 755849575 bytes, 0 underruns
     Output 956160 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/7 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 682c.7bd5.4407 (bia 682c.7bd5.4407)
  Description: VLAN 702 psychresearch
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is on, output flow-control is unsupported 
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
     Output 0 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/8 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 682c.7bd5.4408 (bia 682c.7bd5.4408)
  Description: VLAN 702 psychresearch
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
            input flow-control is on, output flow-control is unsupported 
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
     Output 0 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/9 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 682c.7bd5.4409 (bia 682c.7bd5.4409)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is on, output flow-control is unsupported 
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
     Output 0 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/10 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 682c.7bd5.440a (bia 682c.7bd5.440a)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is on, output flow-control is unsupported 
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
     Output 0 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/11 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 682c.7bd5.440b (bia 682c.7bd5.440b)
  Description: VLAN 1603 FM CAM
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 2/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is on, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 00:00:00, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 830000 bits/sec, 89 packets/sec
  5 minute output rate 7000 bits/sec, 11 packets/sec
     268811696 packets input, 323247572322 bytes, 0 no buffer
     Received 26 broadcasts (24 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 24 multicast, 0 pause input
     0 input packets with dribble condition detected
     29269628 packets output, 2502567946 bytes, 0 underruns
     Output 124 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/12 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 682c.7bd5.440c (bia 682c.7bd5.440c)
  Description: VLAN 1603 FM CAM
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
            input flow-control is on, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 00:00:00, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 778000 bits/sec, 82 packets/sec
  5 minute output rate 6000 bits/sec, 10 packets/sec
     256594886 packets input, 303937804532 bytes, 0 no buffer
     Received 26 broadcasts (24 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 24 multicast, 0 pause input
     0 input packets with dribble condition detected
     29312643 packets output, 2505550178 bytes, 0 underruns
     Output 124 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/13 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 682c.7bd5.440d (bia 682c.7bd5.440d)
  Description: VLAN 1603 FM CAM
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is on, output flow-control is unsupported 
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
     Output 0 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/14 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 682c.7bd5.440e (bia 682c.7bd5.440e)
  Description: VLAN 1603 FM CAM
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
            Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is on, output flow-control is unsupported 
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
     Output 0 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/15 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 682c.7bd5.440f (bia 682c.7bd5.440f)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is on, output flow-control is unsupported 
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
     Output 0 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/16 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 682c.7bd5.4410 (bia 682c.7bd5.4410)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
            input flow-control is on, output flow-control is unsupported 
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
     Output 0 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/17 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 682c.7bd5.4411 (bia 682c.7bd5.4411)
  Description: VLAN 31 Building Data
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
  input flow-control is on, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 00:00:00, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 1565
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 12000 bits/sec, 9 packets/sec
     46627677 packets input, 49653084625 bytes, 0 no buffer
     Received 71255 broadcasts (57836 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 57836 multicast, 0 pause input
     0 input packets with dribble condition detected
     82685318 packets output, 71674883950 bytes, 0 underruns
     Output 12793861 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/18 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 682c.7bd5.4412 (bia 682c.7bd5.4412)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
            input flow-control is on, output flow-control is unsupported 
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
     Output 0 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/19 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 682c.7bd5.4413 (bia 682c.7bd5.4413)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is on, output flow-control is unsupported 
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
     Output 0 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/20 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 682c.7bd5.4414 (bia 682c.7bd5.4414)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is on, output flow-control is unsupported 
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
     Output 0 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/21 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 682c.7bd5.4415 (bia 682c.7bd5.4415)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is on, output flow-control is unsupported 
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
     Output 0 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/22 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 682c.7bd5.4416 (bia 682c.7bd5.4416)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is on, output flow-control is unsupported 
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
     Output 0 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/23 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 682c.7bd5.4417 (bia 682c.7bd5.4417)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is on, output flow-control is unsupported 
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
     Output 0 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/24 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 682c.7bd5.4418 (bia 682c.7bd5.4418)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is on, output flow-control is unsupported 
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
     Output 0 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/25 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 682c.7bd5.4419 (bia 682c.7bd5.4419)
  Description: VLAN 35 Navigen-data
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is on, output flow-control is unsupported 
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
     Output 0 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/26 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 682c.7bd5.441a (bia 682c.7bd5.441a)
  Description: VLAN 36 Navigen-VOIP
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is on, output flow-control is unsupported 
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
     Output 0 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/27 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 682c.7bd5.441b (bia 682c.7bd5.441b)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 7/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is on, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 00:00:00, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 3074000 bits/sec, 278 packets/sec
  5 minute output rate 14000 bits/sec, 24 packets/sec
     781372529 packets input, 1068677534174 bytes, 0 no buffer
     Received 26 broadcasts (24 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 24 multicast, 0 pause input
     0 input packets with dribble condition detected
     62812940 packets output, 5158622599 bytes, 0 underruns
     Output 124 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/28 is up, line protocol is up (connected) 
  Hardware is Gigabit Ethernet, address is 682c.7bd5.441c (bia 682c.7bd5.441c)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 14/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100/1000BaseTX
  input flow-control is on, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 00:00:00, output hang never
            Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 5776000 bits/sec, 507 packets/sec
  5 minute output rate 14000 bits/sec, 22 packets/sec
     1091672840 packets input, 1511110270476 bytes, 0 no buffer
     Received 26 broadcasts (24 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 24 multicast, 0 pause input
     0 input packets with dribble condition detected
     62483788 packets output, 5136692337 bytes, 0 underruns
     Output 124 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/29 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 682c.7bd5.441d (bia 682c.7bd5.441d)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is on, output flow-control is unsupported 
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
     Output 0 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/30 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 682c.7bd5.441e (bia 682c.7bd5.441e)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is on, output flow-control is unsupported 
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
     Output 0 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/31 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 682c.7bd5.441f (bia 682c.7bd5.441f)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is on, output flow-control is unsupported 
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
     Output 0 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/32 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 682c.7bd5.4420 (bia 682c.7bd5.4420)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is on, output flow-control is unsupported 
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
     Output 0 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/33 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 682c.7bd5.4421 (bia 682c.7bd5.4421)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is on, output flow-control is unsupported 
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
     Output 0 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/34 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 682c.7bd5.4422 (bia 682c.7bd5.4422)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is on, output flow-control is unsupported 
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
     Output 0 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/35 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 682c.7bd5.4423 (bia 682c.7bd5.4423)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is on, output flow-control is unsupported 
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
     Output 0 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/36 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 682c.7bd5.4424 (bia 682c.7bd5.4424)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is on, output flow-control is unsupported 
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
     Output 0 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/37 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 682c.7bd5.4425 (bia 682c.7bd5.4425)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is on, output flow-control is unsupported 
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
     Output 0 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/38 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 682c.7bd5.4426 (bia 682c.7bd5.4426)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is on, output flow-control is unsupported 
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
     Output 0 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/39 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 682c.7bd5.4427 (bia 682c.7bd5.4427)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is on, output flow-control is unsupported 
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
     Output 0 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/40 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 682c.7bd5.4428 (bia 682c.7bd5.4428)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is on, output flow-control is unsupported 
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
     Output 0 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/41 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 682c.7bd5.4429 (bia 682c.7bd5.4429)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is on, output flow-control is unsupported 
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
     Output 0 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/42 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 682c.7bd5.442a (bia 682c.7bd5.442a)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is on, output flow-control is unsupported 
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
     Output 0 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/43 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 682c.7bd5.442b (bia 682c.7bd5.442b)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is on, output flow-control is unsupported 
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
     Output 0 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/44 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 682c.7bd5.442c (bia 682c.7bd5.442c)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is on, output flow-control is unsupported 
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
     Output 0 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/45 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 682c.7bd5.442d (bia 682c.7bd5.442d)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is on, output flow-control is unsupported 
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
     Output 0 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/46 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 682c.7bd5.442e (bia 682c.7bd5.442e)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is on, output flow-control is unsupported 
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
     Output 0 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/47 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 682c.7bd5.442f (bia 682c.7bd5.442f)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is on, output flow-control is unsupported 
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
     Output 0 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/0/48 is down, line protocol is down (notconnect) 
  Hardware is Gigabit Ethernet, address is 682c.7bd5.4430 (bia 682c.7bd5.4430)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is on, output flow-control is unsupported 
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
     Output 0 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/1/1 is down, line protocol is down (notconnect) 
  Hardware is not present
  Hardware is Gigabit Ethernet, address is 682c.7bd5.4431 (bia 682c.7bd5.4431)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
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
     Output 0 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/1/2 is down, line protocol is down (notconnect) 
  Hardware is not present
  Hardware is Gigabit Ethernet, address is 682c.7bd5.4432 (bia 682c.7bd5.4432)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
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
               Output 0 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/1/3 is down, line protocol is down (notconnect) 
  Hardware is not present
  Hardware is Gigabit Ethernet, address is 682c.7bd5.4433 (bia 682c.7bd5.4433)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
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
     Output 0 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet1/1/4 is down, line protocol is down (notconnect) 
  Hardware is not present
  Hardware is Gigabit Ethernet, address is 682c.7bd5.4434 (bia 682c.7bd5.4434)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
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
     Output 0 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
               0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/1/1 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet, address is 682c.7bd5.4435 (bia 682c.7bd5.4435)
  Description: key:t1/1/1:r1-ebc-ebc:e2/19
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 3/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not set
  Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-LR
  input flow-control is on, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output 00:00:04, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 13627000 bits/sec, 9017 packets/sec
  5 minute output rate 123290000 bits/sec, 11483 packets/sec
     5781860345 packets input, 4208384718245 bytes, 0 no buffer
     Received 50385532 broadcasts (47763558 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 47763558 multicast, 0 pause input
     0 input packets with dribble condition detected
     15627415767 packets output, 19306918038392 bytes, 0 underruns
     Output 8680339 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/1/2 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet, address is 682c.7bd5.4436 (bia 682c.7bd5.4436)
  Description: key:t1/1/2:r2-ebc-park:e2/19
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not set
  Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-LR
  input flow-control is on, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:03, output 00:00:00, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 8394000 bits/sec, 1070 packets/sec
  5 minute output rate 23905000 bits/sec, 2748 packets/sec
     5286882376 packets input, 4060824278132 bytes, 0 no buffer
     Received 50289178 broadcasts (47364749 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 47364749 multicast, 0 pause input
     0 input packets with dribble condition detected
     9626191037 packets output, 11411522445917 bytes, 0 underruns
     Output 14267677 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
               0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/1/3 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet, address is 682c.7bd5.4437 (bia 682c.7bd5.4437)
  Description: key:t1/1/3:sx1-874-383colorow-177-ebc:t1/1/2
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not set
  Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-LR
  input flow-control is on, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:05, output 00:00:00, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 22722000 bits/sec, 2368 packets/sec
  5 minute output rate 4513000 bits/sec, 667 packets/sec
     8352361560 packets input, 10203058642860 bytes, 0 no buffer
     Received 8417909 broadcasts (4797521 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 4797521 multicast, 0 pause input
     0 input packets with dribble condition detected
     1608473837 packets output, 747777738671 bytes, 0 underruns
     Output 24771539 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/1/4 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet, address is 682c.7bd5.4438 (bia 682c.7bd5.4438)
  Description: #key:t1/1/4:sx2-874-374:t1/1/1
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not set
  Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-LR
  input flow-control is on, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:01, output 00:00:00, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 8776000 bits/sec, 1210 packets/sec
  5 minute output rate 8094000 bits/sec, 887 packets/sec
     6710134483 packets input, 8302808740716 bytes, 0 no buffer
     Received 12422936 broadcasts (9929991 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 9929991 multicast, 0 pause input
     0 input packets with dribble condition detected
     3588240755 packets output, 2221004671380 bytes, 0 underruns
     Output 25905924 broadcasts (0 multicasts)
               0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/1/5 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet, address is 682c.7bd5.4439 (bia 682c.7bd5.4439)
  Description: key:t1/1/5:sx1-874-383colorow-273-ebc:t1/1/1
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not set
  Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-LR
  input flow-control is on, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output 00:00:00, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 8474000 bits/sec, 949 packets/sec
  5 minute output rate 3560000 bits/sec, 531 packets/sec
     3227843863 packets input, 3543485548319 bytes, 0 no buffer
     Received 23995292 broadcasts (9472200 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 9472200 multicast, 0 pause input
     0 input packets with dribble condition detected
     2016425152 packets output, 1730051205990 bytes, 0 underruns
     Output 13873611 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/1/6 is down, line protocol is down (notconnect) 
  Hardware is Ten Gigabit Ethernet, address is 682c.7bd5.443a (bia 682c.7bd5.443a)
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not set
  Auto-duplex, Auto-speed, link type is auto, media type is unknown
  input flow-control is on, output flow-control is unsupported 
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
     Output 0 broadcasts (0 multicasts)
               0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/1/7 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet, address is 682c.7bd5.443b (bia 682c.7bd5.443b)
  Description: key:t1/1/7:sx1-874-383colorow-374-ebc:t1/1/1
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not set
  Full-duplex, 10Gb/s, link type is auto, media type is SFP-10GBase-LR
  input flow-control is on, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output 00:00:00, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 6305000 bits/sec, 699 packets/sec
  5 minute output rate 1499000 bits/sec, 284 packets/sec
     3215017087 packets input, 3667262051264 bytes, 0 no buffer
     Received 13096507 broadcasts (10806684 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 10806684 multicast, 0 pause input
     0 input packets with dribble condition detected
     2276974211 packets output, 2555240189522 bytes, 0 underruns
     Output 26109040 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/1/8 is down, line protocol is down (notconnect) 
  Hardware is Ten Gigabit Ethernet, address is 682c.7bd5.443c (bia 682c.7bd5.443c)
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not set
  Auto-duplex, Auto-speed, link type is auto, media type is unknown
  input flow-control is on, output flow-control is unsupported 
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
     Output 0 broadcasts (0 multicasts)
               0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
FortyGigabitEthernet1/1/1 is down, line protocol is down (notconnect) 
  Hardware is not present
  Hardware is Forty Gigabit Ethernet, address is 682c.7bd5.443d (bia 682c.7bd5.443d)
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
     Output 0 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
FortyGigabitEthernet1/1/2 is down, line protocol is down (notconnect) 
  Hardware is not present
  Hardware is Forty Gigabit Ethernet, address is 682c.7bd5.443e (bia 682c.7bd5.443e)
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
     Output 0 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
               0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TwentyFiveGigE1/1/1 is down, line protocol is down (notconnect) 
  Hardware is not present
  Hardware is Twenty Five Gigabit Ethernet, address is 682c.7bd5.443f (bia 682c.7bd5.443f)
  MTU 1500 bytes, BW 25000000 Kbit/sec, DLY 10 usec, 
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
     Output 0 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
TwentyFiveGigE1/1/2 is down, line protocol is down (notconnect) 
  Hardware is not present
  Hardware is Twenty Five Gigabit Ethernet, address is 682c.7bd5.4440 (bia 682c.7bd5.4440)
  MTU 1500 bytes, BW 25000000 Kbit/sec, DLY 10 usec, 
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
     Output 0 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
AppGigabitEthernet1/0/1 is up, line protocol is up (connected) 
            Hardware is App-hosting Gigabit Ethernet, address is 682c.7bd5.4441 (bia 682c.7bd5.4441)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, media type is App-hosting port
  input flow-control is on, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 00:00:00, output hang never
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
     2116663 packets output, 195837466 bytes, 0 underruns
     Output 0 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
Port-channel30 is up, line protocol is up (connected) 
  Hardware is EtherChannel, address is 682c.7bd5.4435 (bia 682c.7bd5.4435)
  Description: key:Uplink to dist nodes
  MTU 1500 bytes, BW 20000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 10Gb/s, link type is auto, media type is N/A
  input flow-control is on, output flow-control is unsupported 
  Members in this channel: Te1/1/1 Te1/1/2 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:01, output 00:00:00, output hang never
  Last clearing of "" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 22025000 bits/sec, 10089 packets/sec
  5 minute output rate 147192000 bits/sec, 14229 packets/sec
     11068754262 packets input, 8269214037350 bytes, 0 no buffer
     Received 100674908 broadcasts (95128495 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 95128495 multicast, 0 pause input
     0 input packets with dribble condition detected
     25253646537 packets output, 30718489067157 bytes, 0 underruns
     Output 22948093 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out""",
 'show inventory':"""NAME: "c93xx Stack", DESCR: "c93xx Stack"
PID: C9300-48U         , VID: V01  , SN: FCW2210L069

NAME: "Switch 1", DESCR: "C9300-48U"
PID: C9300-48U         , VID: V01  , SN: FCW2210L069

NAME: "Switch 1 - Power Supply A", DESCR: "Switch 1 - Power Supply A"
PID: PWR-C1-1100WAC    , VID: V02  , SN: LIT21512AYM

NAME: "Switch 1 - Power Supply B", DESCR: "Switch 1 - Power Supply B"
PID: PWR-C1-1100WAC    , VID: V02  , SN: LIT21514AW9

NAME: "Switch 1 FRU Uplink Module 1", DESCR: "8x10G Uplink Module"
PID: C9300-NM-8X       , VID: V01  , SN: FOC22060RQ4

NAME: "Te1/1/1", DESCR: "SFP-10GBase-LR"
PID: SFP-10G-LR          , VID: V02  , SN: FNS17391DJB     

NAME: "Te1/1/2", DESCR: "SFP-10GBase-LR"
PID: SFP-10G-LR          , VID: V02  , SN: USXLR58904      

NAME: "Te1/1/3", DESCR: "SFP-10GBase-LR"
PID: SFP-10G-LR          , VID: V02  , SN: ONT162504ZY     

NAME: "Te1/1/4", DESCR: "SFP-10GBase-LR"
PID: SFP-10G-LR          , VID: V02  , SN: USXLR58902      

NAME: "Te1/1/5", DESCR: "SFP-10GBase-LR"
PID: SFP-10G-LR          , VID: V02  , SN: USXLR75299      

NAME: "Te1/1/7", DESCR: "SFP-10GBase-LR"
PID: SFP-10G-LR          , VID: V02  , SN: USXLR58903      

""",
 'show interface counters':"""Port               InOctets    InUcastPkts    InMcastPkts    InBcastPkts 
Gi1/0/1           148452439        1119436              0              2 
Gi1/0/2           544005709         837578           1883             52 
Gi1/0/3       1755035618342     1397981026           2563           8706 
Gi1/0/4            22717397         270023            842             24 
Gi1/0/5           131195419        1498294              0              1 
Gi1/0/6           200678437        1914707              0              2 
Gi1/0/7                   0              0              0              0 
Gi1/0/8                   0              0              0              0 
Gi1/0/9                   0              0              0              0 
Gi1/0/10                  0              0              0              0 
Gi1/0/11       323247572322      268811670             24              2 
Gi1/0/12       303937804532      256594860             24              2 
Gi1/0/13                  0              0              0              0 
Gi1/0/14                  0              0              0              0 
Gi1/0/15                  0              0              0              0 
Gi1/0/16                  0              0              0              0 
Gi1/0/17        49653084625       46556422          57836          13419 
Gi1/0/18                  0              0              0              0 
Gi1/0/19                  0              0              0              0 
Gi1/0/20                  0              0              0              0 
Gi1/0/21                  0              0              0              0 
Gi1/0/22                  0              0              0              0 
Gi1/0/23                  0              0              0              0 
Gi1/0/24                  0              0              0              0 
Gi1/0/25                  0              0              0              0 
Gi1/0/26                  0              0              0              0 
Gi1/0/27      1068677534174      781372503             24              2 
Gi1/0/28      1511110270476     1091672814             24              2 
Gi1/0/29                  0              0              0              0 
Gi1/0/30                  0              0              0              0 
Gi1/0/31                  0              0              0              0 
Gi1/0/32                  0              0              0              0 
Gi1/0/33                  0              0              0              0 
Gi1/0/34                  0              0              0              0 
Gi1/0/35                  0              0              0              0 
Gi1/0/36                  0              0              0              0 
Gi1/0/37                  0              0              0              0 
Gi1/0/38                  0              0              0              0 
Gi1/0/39                  0              0              0              0 
Gi1/0/40                  0              0              0              0 
Gi1/0/41                  0              0              0              0 
Gi1/0/42                  0              0              0              0 
Gi1/0/43                  0              0              0              0 
Gi1/0/44                  0              0              0              0 
Gi1/0/45                  0              0              0              0 
Gi1/0/46                  0              0              0              0 
Gi1/0/47                  0              0              0              0 
Gi1/0/48                  0              0              0              0 
Te1/1/1       4208389155738     5731483629       47763653        2621977 
Te1/1/2       4060824881612     5236595725       47364842        2924436 
Te1/1/3      10203076153533     8343958408        4797525        3620405 
Te1/1/4       8302815930437     6697717639        9930010        2492954 
Te1/1/5       3543490632060     3203852970        9472225       14523124 
Te1/1/6                   0              0              0              0 
Te1/1/7       3667266659807     3201924471       10806694        2289847 
Te1/1/8                   0              0              0              0 
Ap1/0/1                   0              0              0              0 
          
Port               InOctets    InUcastPkts    InMcastPkts    InBcastPkts 
Po30          8269214037350    10968079354       95128495        5546413 

Port              OutOctets   OutUcastPkts   OutMcastPkts   OutBcastPkts 
Gi1/0/1           681606293        1410594        4549273         956159 
Gi1/0/2          1987658951        1667754        4547415         956100 
Gi1/0/3       1012197869207     1810691090        4546726         947458 
Gi1/0/4           570078059         590244        4548443         956140 
Gi1/0/5           681611512        1974475        4549301         956163 
Gi1/0/6           755849575        2436260        4549284         956160 
Gi1/0/7                   0              0              0              0 
Gi1/0/8                   0              0              0              0 
Gi1/0/9                   0              0              0              0 
Gi1/0/10                  0              0              0              0 
Gi1/0/11         2502567946       24583657        4685847            124 
Gi1/0/12         2505550178       24626632        4685887            124 
Gi1/0/13                  0              0              0              0 
Gi1/0/14                  0              0              0              0 
Gi1/0/15                  0              0              0              0 
Gi1/0/16                  0              0              0              0 
Gi1/0/17        71674883950       50228899       19662558       12793861 
Gi1/0/18                  0              0              0              0 
Gi1/0/19                  0              0              0              0 
Gi1/0/20                  0              0              0              0 
Gi1/0/21                  0              0              0              0 
Gi1/0/22                  0              0              0              0 
Gi1/0/23                  0              0              0              0 
Gi1/0/24                  0              0              0              0 
Gi1/0/25                  0              0              0              0 
Gi1/0/26                  0              0              0              0 
Gi1/0/27         5158622599       58126943        4685873            124 
Gi1/0/28         5136692337       57797775        4685889            124 
Gi1/0/29                  0              0              0              0 
Gi1/0/30                  0              0              0              0 
Gi1/0/31                  0              0              0              0 
Gi1/0/32                  0              0              0              0 
Gi1/0/33                  0              0              0              0 
Gi1/0/34                  0              0              0              0 
Gi1/0/35                  0              0              0              0 
Gi1/0/36                  0              0              0              0 
Gi1/0/37                  0              0              0              0 
Gi1/0/38                  0              0              0              0 
Gi1/0/39                  0              0              0              0 
Gi1/0/40                  0              0              0              0 
Gi1/0/41                  0              0              0              0 
Gi1/0/42                  0              0              0              0 
Gi1/0/43                  0              0              0              0 
Gi1/0/44                  0              0              0              0 
Gi1/0/45                  0              0              0              0 
Gi1/0/46                  0              0              0              0 
Gi1/0/47                  0              0              0              0 
Gi1/0/48                  0              0              0              0 
Te1/1/1      19306949523735    15604770012       13990228        8680363 
Te1/1/2      11411539543422     9600848312       11089892       14267730 
Te1/1/3        747780562322     1490079845       93626280       24771609 
Te1/1/4       2221005443295     3469188764       93147615       25906011 
Te1/1/5       1730052373067     1910496752       92056678       13873675 
Te1/1/6                   0              0              0              0 
Te1/1/7       2555240339350     2158598462       92267618       26109112 
Te1/1/8                   0              0              0              0 
          
Port              OutOctets   OutUcastPkts   OutMcastPkts   OutBcastPkts 
Ap1/0/1           195837658         308900        1807766              0 
Po30         30718489067157    25205618324       25080120       22948093 """,
 'show cdp nei detail':"""-------------------------
Device ID: sx2-874-383colorow-374-ebc
Entry address(es): 
  IP address: 172.31.6.136
Platform: cisco C9300-48U,  Capabilities: Switch IGMP 
Interface: TenGigabitEthernet1/1/4,  Port ID (outgoing port): TenGigabitEthernet1/1/1
Holdtime : 178 sec

Version :
Cisco IOS Software [Fuji], Catalyst L3 Switch Software (CAT9K_IOSXE), Version 16.9.4, RELEASE SOFTWARE (fc2)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2019 by Cisco Systems, Inc.
Compiled Thu 22-Aug-19 18:14 by mcpre

advertisement version: 2
VTP Management Domain: 'vtp-874-383colorow'
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 172.31.6.136

-------------------------
Device ID: r1-ebc-ebc(JPG22470080)
Entry address(es): 
  IP address: 155.98.225.2
Platform: N77-C7710,  Capabilities: Router Switch IGMP CVTA phone port 
Interface: TenGigabitEthernet1/1/1,  Port ID (outgoing port): Ethernet2/19
Holdtime : 160 sec

Version :
Cisco Nexus Operating System (NX-OS) Software, Version 8.2(2)

advertisement version: 2
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 172.29.1.10

-------------------------
Device ID: r2-ebc-park(JPG2249004S)
Entry address(es): 
  IP address: 155.98.225.3
Platform: N77-C7710,  Capabilities: Router Switch IGMP CVTA phone port 
Interface: TenGigabitEthernet1/1/2,  Port ID (outgoing port): Ethernet2/19
Holdtime : 175 sec

Version :
Cisco Nexus Operating System (NX-OS) Software, Version 8.2(2)

advertisement version: 2
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 172.29.1.11

-------------------------
Device ID: sx1-874-383colorow-273-ebc.net.utah.edu
Entry address(es): 
  IP address: 172.31.6.134
          Platform: cisco C9300-48U,  Capabilities: Switch IGMP 
Interface: TenGigabitEthernet1/1/5,  Port ID (outgoing port): TenGigabitEthernet1/1/1
Holdtime : 169 sec

Version :
Cisco IOS Software [Gibraltar], Catalyst L3 Switch Software (CAT9K_IOSXE), Version 16.12.4, RELEASE SOFTWARE (fc5)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2020 by Cisco Systems, Inc.
Compiled Thu 09-Jul-20 21:49 by mcpre

advertisement version: 2
VTP Management Domain: 'vtp-874-383colorow'
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 172.31.6.134

-------------------------
Device ID: sx1-874-383colorow-177-ebc.net.utah.edu
Entry address(es): 
  IP address: 172.31.6.140
Platform: cisco C9300-48U,  Capabilities: Switch IGMP 
Interface: TenGigabitEthernet1/1/3,  Port ID (outgoing port): TenGigabitEthernet1/1/2
Holdtime : 179 sec

Version :
Cisco IOS Software [Gibraltar], Catalyst L3 Switch Software (CAT9K_IOSXE), Version 16.12.4, RELEASE SOFTWARE (fc5)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2020 by Cisco Systems, Inc.
Compiled Thu 09-Jul-20 21:49 by mcpre

advertisement version: 2
VTP Management Domain: 'vtp-874-383colorow'
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 172.31.6.140

-------------------------
Device ID: sx1-874-383colorow-374-ebc.net.utah.edu
Entry address(es): 
  IP address: 172.31.6.135
Platform: cisco C9300-48U,  Capabilities: Switch IGMP 
Interface: TenGigabitEthernet1/1/7,  Port ID (outgoing port): TenGigabitEthernet1/1/1
Holdtime : 147 sec

Version :
Cisco IOS Software [Gibraltar], Catalyst L3 Switch Software (CAT9K_IOSXE), Version 16.12.4, RELEASE SOFTWARE (fc5)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2020 by Cisco Systems, Inc.
Compiled Thu 09-Jul-20 21:49 by mcpre

advertisement version: 2
VTP Management Domain: 'vtp-874-383colorow'
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 172.31.6.135

          
Total cdp entries displayed : 6""",
 'show module all':"""^
% Invalid input detected at '^' marker.
""",
 'show module':"""Switch  Ports    Model                Serial No.   MAC address     Hw Ver.       Sw Ver. 
------  -----   ---------             -----------  --------------  -------       --------
 1       65     C9300-48U             FCW2210L069  682c.7bd5.4400  V01           16.12.4       """,
 'show run | section snmp':"""snmp-server group CliNOCGrv3RO v3 priv read CliNOCViewRO access 70
snmp-server group CliNOCGrv3RO v3 auth context vlan- match prefix 
snmp-server group CliNOCGrv3RW v3 priv write CliNOCViewRW access 71
snmp-server view CliNOCViewRO internet included
snmp-server view CliNOCViewRW internet included
snmp-server location Bldg. 874 Room 329
snmp-server contact BC-508870 Y-321300
snmp ifmib ifindex persist""",
 'show run | in snmp':"""snmp-server group CliNOCGrv3RO v3 priv read CliNOCViewRO access 70
snmp-server group CliNOCGrv3RO v3 auth context vlan- match prefix 
snmp-server group CliNOCGrv3RW v3 priv write CliNOCViewRW access 71
snmp-server view CliNOCViewRO internet included
snmp-server view CliNOCViewRW internet included
snmp-server location Bldg. 874 Room 329
snmp-server contact BC-508870 Y-321300
snmp ifmib ifindex persist""",
 'show snmp user':"""User name: CliNONUserv3RO
Engine ID: 800000090300682C7BD54400
storage-type: nonvolatile	 active
Authentication Protocol: MD5
Privacy Protocol: DES
Group-name: CliNOCGrv3RW

User name: CliNONUserv3Rw
Engine ID: 800000090300682C7BD54400
storage-type: nonvolatile	 active
Authentication Protocol: MD5
Privacy Protocol: DES
Group-name: CliNOCGrv3RW
""",
 'show access-list':"""Standard IP access list 70
    10 permit 10.64.2.70
    20 permit 10.71.25.65
    30 permit 155.100.126.163
    40 permit 155.100.126.162
    50 permit 10.71.24.21
    60 permit 10.71.24.20
    70 permit 10.71.24.23
    80 permit 10.71.24.22
    90 permit 10.71.24.17
    100 permit 10.71.24.16
    110 permit 10.71.24.19
    120 permit 10.71.24.18
    130 permit 172.20.150.100
    140 permit 10.71.24.25
    150 permit 10.71.24.13
    160 permit 10.71.24.12
    170 permit 10.71.24.15
    180 permit 10.71.24.14
    190 permit 10.71.24.11
    200 permit 155.100.123.72
    210 permit 10.71.25.164
    220 permit 155.98.164.192, wildcard bits 0.0.0.31
    230 permit 155.99.254.128, wildcard bits 0.0.0.127
    240 permit 155.98.253.0, wildcard bits 0.0.0.255
    250 deny   any log
Standard IP access list 71
    10 permit 10.64.2.70
    20 permit 10.71.25.65
    30 permit 155.100.126.163
    40 permit 155.100.126.162
    50 permit 10.71.24.21
    60 permit 10.71.24.20 (3903400 matches)
    70 permit 10.71.24.23
    80 permit 10.71.24.22
    90 permit 10.71.24.17
    100 permit 10.71.24.16
    110 permit 10.71.24.19
    120 permit 10.71.24.18
    130 permit 172.20.150.100
    140 permit 10.71.24.25
    150 permit 10.71.24.13
    160 permit 10.71.24.12
    170 permit 10.71.24.15
    180 permit 10.71.24.14
    190 permit 10.71.24.11
    200 permit 155.100.123.72
    210 permit 10.71.25.164
    220 permit 155.98.164.192, wildcard bits 0.0.0.31
    230 permit 155.99.254.128, wildcard bits 0.0.0.127
    240 permit 155.98.253.0, wildcard bits 0.0.0.255
    250 deny   any log
Extended IP access list 199
    10 permit tcp 155.98.253.0 0.0.0.255 any eq 22 (10 matches)
    20 permit tcp host 172.20.150.100 any eq 22
    30 permit tcp host 155.100.126.162 any eq 22
    40 permit tcp host 155.100.126.163 any eq 22
    50 permit tcp host 10.64.2.70 any eq 22
    60 permit tcp host 155.99.239.130 any eq 22
              70 permit tcp host 155.97.152.244 any eq 22
    80 permit tcp host 155.100.123.72 any eq 22
    90 permit tcp 155.99.254.128 0.0.0.127 any eq 22 (80 matches)
    100 permit tcp 155.98.164.192 0.0.0.31 any eq 22 (46 matches)
    110 permit tcp host 10.71.24.11 any eq 22
    120 permit tcp host 10.71.24.12 any eq 22
    130 permit tcp host 10.71.24.13 any eq 22
    140 permit tcp host 10.71.24.14 any eq 22
    150 permit tcp host 10.71.24.15 any eq 22
    160 permit tcp host 10.71.24.16 any eq 22
    170 permit tcp host 10.71.24.17 any eq 22
    180 permit tcp host 10.71.24.18 any eq 22
    190 permit tcp host 10.71.24.19 any eq 22
    200 permit tcp host 10.71.24.20 any eq 22 (52 matches)
    210 permit tcp host 10.71.24.21 any eq 22
    220 permit tcp host 10.71.24.22 any eq 22
    230 permit tcp host 10.71.24.23 any eq 22
    240 permit tcp host 10.71.24.25 any eq 22
    250 permit tcp host 10.71.25.65 any eq 22
    260 permit tcp host 10.71.25.164 any eq 22
    270 deny ip any any log (10 matches)
Extended IP access list IP-Adm-V4-Int-ACL-global
Extended IP access list implicit_deny
    10 deny ip any any
Extended IP access list implicit_permit
    10 permit ip any any
Extended IP access list meraki-fqdn-dns
Extended IP access list preauth_v4
    10 permit udp any any eq domain
    20 permit tcp any any eq domain
    30 permit udp any eq bootps any
    40 permit udp any any eq bootpc
    50 permit udp any eq bootpc any
    60 deny ip any any
IPv6 access list implicit_deny_v6
    deny ipv6 any any sequence 10
IPv6 access list implicit_permit_v6
    permit ipv6 any any sequence 10
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
no device-tracking logging theft
logging facility local6
logging source-interface Vlan845
logging host 155.98.253.244
logging host 155.98.204.52
logging host 172.24.29.14
logging host 10.70.24.10
logging host 10.71.24.11""",
 'show run | in logging':"""logging buffered notifications
logging console critical
no device-tracking logging theft
logging facility local6
logging source-interface Vlan845
logging host 155.98.253.244
logging host 155.98.204.52
logging host 172.24.29.14
logging host 10.70.24.10
logging host 10.71.24.11""",
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
   1    002f.5cfd.d38a    DYNAMIC     Po30
   1    003a.9c3f.ffc1    DYNAMIC     Po30
   1    003a.9c40.5ec1    DYNAMIC     Po30
   1    0087.6451.5bce    DYNAMIC     Po30
   1    682c.7b23.92b5    DYNAMIC     Te1/1/5
   1    682c.7bf8.6c35    DYNAMIC     Te1/1/7
   1    68ca.e436.1eb6    DYNAMIC     Te1/1/3
   1    68ca.e436.85b5    DYNAMIC     Te1/1/4
 845    0000.0c9f.f34d    DYNAMIC     Po30
 845    0026.f36a.0000    DYNAMIC     Po30
 845    003a.9c3f.ffc1    DYNAMIC     Po30
 845    003a.9c40.5ec1    DYNAMIC     Po30
 845    006b.f125.d844    DYNAMIC     Te1/1/3
 845    006b.f125.d862    DYNAMIC     Te1/1/3
 845    00c0.b7eb.4792    DYNAMIC     Te1/1/4
 845    00c0.b7f1.17e8    DYNAMIC     Te1/1/5
 845    00c0.b7f1.1ff5    DYNAMIC     Te1/1/3
 845    0462.73aa.1ae4    DYNAMIC     Te1/1/5
 845    0462.73ab.ea68    DYNAMIC     Te1/1/5
 845    0462.73bd.c0d0    DYNAMIC     Te1/1/5
 845    0462.73bd.c4e8    DYNAMIC     Te1/1/5
 845    0462.73bd.c6b0    DYNAMIC     Te1/1/5
 845    0462.73c2.e650    DYNAMIC     Te1/1/3
 845    0462.73c2.e878    DYNAMIC     Te1/1/5
 845    0462.73c7.dcc8    DYNAMIC     Te1/1/3
 845    2c01.b554.5a7c    DYNAMIC     Te1/1/5
 845    682c.7bd5.447c    STATIC      Vl845 
 845    682c.7bf8.6c7c    DYNAMIC     Te1/1/7
 845    68ca.e436.85fc    DYNAMIC     Te1/1/4
 845    70f0.967f.0cec    DYNAMIC     Te1/1/5
 845    70f0.967f.0d2c    DYNAMIC     Te1/1/3
 845    70f0.967f.3e34    DYNAMIC     Te1/1/4
 845    70f0.967f.3ffc    DYNAMIC     Te1/1/3
           845    70f0.967f.4668    DYNAMIC     Te1/1/4
 845    70f0.967f.47b8    DYNAMIC     Te1/1/3
 845    70f0.967f.48f0    DYNAMIC     Te1/1/5
 845    70f0.967f.4ec4    DYNAMIC     Te1/1/3
 845    70f0.967f.5014    DYNAMIC     Te1/1/4
 845    70f0.967f.50f4    DYNAMIC     Te1/1/4
 845    70f0.967f.5100    DYNAMIC     Te1/1/5
 845    70f0.967f.52ec    DYNAMIC     Te1/1/5
 845    70f0.967f.5350    DYNAMIC     Te1/1/5
 845    70f0.967f.57bc    DYNAMIC     Te1/1/5
 845    70f0.967f.5844    DYNAMIC     Te1/1/3
 845    70f0.967f.58cc    DYNAMIC     Te1/1/4
 845    70f0.967f.5a50    DYNAMIC     Te1/1/3
 845    70f0.967f.5b1c    DYNAMIC     Te1/1/4
 845    70f0.967f.5e10    DYNAMIC     Te1/1/4
 845    70f0.967f.5e70    DYNAMIC     Te1/1/3
 845    70f0.967f.5f7c    DYNAMIC     Te1/1/4
 845    70f0.967f.6010    DYNAMIC     Te1/1/5
 845    70f0.967f.6040    DYNAMIC     Te1/1/5
 845    70f0.967f.6758    DYNAMIC     Te1/1/5
 845    70f0.967f.67c0    DYNAMIC     Te1/1/4
 845    70f0.967f.685c    DYNAMIC     Te1/1/4
 845    70f0.967f.6974    DYNAMIC     Te1/1/3
 845    70f0.967f.69b8    DYNAMIC     Te1/1/4
 845    70f0.967f.6a54    DYNAMIC     Te1/1/4
 845    70f0.967f.6a7c    DYNAMIC     Te1/1/4
 845    70f0.967f.6b74    DYNAMIC     Te1/1/5
 845    70f0.967f.6b88    DYNAMIC     Te1/1/3
 845    70f0.967f.6ba8    DYNAMIC     Te1/1/4
 845    70f0.967f.6c5c    DYNAMIC     Te1/1/4
 845    70f0.967f.6c6c    DYNAMIC     Te1/1/5
 845    70f0.967f.6ca4    DYNAMIC     Te1/1/4
 845    70f0.967f.6cac    DYNAMIC     Te1/1/5
 845    70f0.967f.6d60    DYNAMIC     Te1/1/4
 845    70f0.967f.731c    DYNAMIC     Te1/1/5
 845    70f0.967f.7b68    DYNAMIC     Te1/1/7
 845    70f0.967f.7de4    DYNAMIC     Te1/1/3
 845    70f0.967f.7df8    DYNAMIC     Te1/1/3
 845    70f0.967f.8294    DYNAMIC     Te1/1/3
 845    70f0.967f.8328    DYNAMIC     Te1/1/7
 845    70f0.967f.8e28    DYNAMIC     Te1/1/4
 845    70f0.967f.8fa0    DYNAMIC     Te1/1/4
 845    70f0.967f.9644    DYNAMIC     Te1/1/3
 845    70f0.967f.9650    DYNAMIC     Te1/1/3
 845    70f0.967f.9884    DYNAMIC     Te1/1/4
 845    70f0.967f.9b00    DYNAMIC     Te1/1/5
 845    70f0.967f.9b78    DYNAMIC     Te1/1/4
 845    70f0.967f.9f54    DYNAMIC     Te1/1/7
 845    70f0.967f.9f84    DYNAMIC     Te1/1/4
 845    70f0.967f.9fe8    DYNAMIC     Te1/1/3
 845    70f0.967f.a034    DYNAMIC     Te1/1/3
 845    70f0.967f.a074    DYNAMIC     Te1/1/3
 845    70f0.967f.a0a4    DYNAMIC     Te1/1/4
 845    70f0.967f.a0b8    DYNAMIC     Te1/1/4
 845    70f0.967f.a0fc    DYNAMIC     Te1/1/4
 845    70f0.967f.b068    DYNAMIC     Te1/1/3
 845    70f0.967f.b140    DYNAMIC     Te1/1/4
 845    70f0.967f.b2f0    DYNAMIC     Te1/1/3
 845    70f0.967f.b668    DYNAMIC     Te1/1/4
           845    70f0.967f.b808    DYNAMIC     Te1/1/5
 845    70f0.967f.b918    DYNAMIC     Te1/1/4
 845    70f0.967f.bacc    DYNAMIC     Te1/1/4
 845    70f0.967f.bc94    DYNAMIC     Te1/1/5
 845    70f0.967f.c45c    DYNAMIC     Te1/1/4
 845    70f0.967f.c7f4    DYNAMIC     Te1/1/3
 845    70f0.967f.c844    DYNAMIC     Te1/1/4
 845    70f0.967f.cac4    DYNAMIC     Te1/1/3
 845    70f0.967f.cfcc    DYNAMIC     Te1/1/3
 845    70f0.967f.d480    DYNAMIC     Te1/1/3
 845    70f0.967f.d490    DYNAMIC     Te1/1/5
 845    70f0.967f.de48    DYNAMIC     Te1/1/3
 845    70f0.967f.df74    DYNAMIC     Te1/1/5
 845    70f0.967f.dfac    DYNAMIC     Te1/1/4
 845    70f0.967f.dfc4    DYNAMIC     Te1/1/3
 845    70f0.967f.e060    DYNAMIC     Te1/1/3
 845    70f0.967f.e17c    DYNAMIC     Te1/1/3
 845    70f0.967f.e394    DYNAMIC     Te1/1/4
 845    70f0.967f.e8f8    DYNAMIC     Te1/1/5
 845    70f0.967f.ea38    DYNAMIC     Te1/1/4
 845    70f0.967f.f4f8    DYNAMIC     Te1/1/4
 845    70f0.967f.f6d0    DYNAMIC     Te1/1/3
 845    d0ec.35ad.337c    DYNAMIC     Te1/1/3
  31    0000.0c9f.f01f    DYNAMIC     Po30
  31    0008.9bf8.cebb    DYNAMIC     Te1/1/4
  31    0008.9bf9.1cf3    DYNAMIC     Te1/1/4
  31    0009.6e06.983a    DYNAMIC     Te1/1/3
  31    0009.6e06.a467    DYNAMIC     Te1/1/3
  31    0009.6e06.a469    DYNAMIC     Te1/1/4
  31    0010.1839.4bac    DYNAMIC     Te1/1/4
  31    0011.2471.d866    DYNAMIC     Te1/1/5
  31    0011.32c7.a592    DYNAMIC     Te1/1/7
  31    0012.3f74.82a7    DYNAMIC     Te1/1/5
  31    0014.5162.784c    DYNAMIC     Te1/1/5
  31    001f.5b3c.9c94    DYNAMIC     Gi1/0/17
  31    0024.dd01.41be    DYNAMIC     Te1/1/3
  31    0024.dd01.4201    DYNAMIC     Te1/1/7
  31    0025.64fd.4715    DYNAMIC     Te1/1/5
  31    0025.64fd.471d    DYNAMIC     Te1/1/5
  31    0026.f36a.0000    DYNAMIC     Po30
  31    003a.9c3f.ffc1    DYNAMIC     Po30
  31    003a.9c40.5ec1    DYNAMIC     Po30
  31    003e.e1c7.09b2    DYNAMIC     Te1/1/4
  31    0040.5810.96c5    DYNAMIC     Te1/1/5
  31    040e.3ce8.527f    DYNAMIC     Te1/1/7
  31    082e.5fbc.f7ed    DYNAMIC     Te1/1/3
  31    10bf.48bb.bd14    DYNAMIC     Te1/1/3
  31    10dd.b1ec.c53b    DYNAMIC     Te1/1/4
  31    1803.73ca.1a61    DYNAMIC     Te1/1/4
  31    1803.73ca.ff9a    DYNAMIC     Te1/1/7
  31    1831.bfe0.1dbd    DYNAMIC     Te1/1/7
  31    1860.24c4.c3cd    DYNAMIC     Te1/1/7
  31    1866.da18.7c22    DYNAMIC     Te1/1/7
  31    1866.da3e.f911    DYNAMIC     Te1/1/5
  31    1866.da96.3549    DYNAMIC     Te1/1/4
  31    1866.da96.354d    DYNAMIC     Te1/1/4
  31    245e.be14.6c18    DYNAMIC     Te1/1/4
  31    245e.be29.6a87    DYNAMIC     Te1/1/4
  31    24f5.a209.102c    DYNAMIC     Te1/1/4
            31    28d2.44ac.4b71    DYNAMIC     Te1/1/5
  31    3005.5cf0.9c43    DYNAMIC     Te1/1/5
  31    30e1.71bd.3fe4    DYNAMIC     Te1/1/5
  31    3417.ebcc.1c49    DYNAMIC     Te1/1/3
  31    38c9.8610.64b5    DYNAMIC     Te1/1/7
  31    38c9.8619.2fcd    DYNAMIC     Te1/1/7
  31    38c9.861b.235e    DYNAMIC     Te1/1/4
  31    38c9.861d.8171    DYNAMIC     Te1/1/7
  31    38c9.861e.99a9    DYNAMIC     Te1/1/7
  31    38c9.863c.bcad    DYNAMIC     Te1/1/7
  31    38c9.8641.4a08    DYNAMIC     Te1/1/7
  31    38c9.8650.bac1    DYNAMIC     Te1/1/7
  31    38c9.8651.fddb    DYNAMIC     Te1/1/4
  31    38c9.865a.16a4    DYNAMIC     Te1/1/4
  31    38f9.d30c.962c    DYNAMIC     Te1/1/4
  31    3c2a.f44c.f245    DYNAMIC     Te1/1/3
  31    3c52.822b.ca7f    DYNAMIC     Te1/1/3
  31    402c.f4e9.e4b1    DYNAMIC     Te1/1/7
  31    406c.8fb8.4054    DYNAMIC     Te1/1/7
  31    406c.8fbd.4094    DYNAMIC     Te1/1/4
  31    509a.4c20.5710    DYNAMIC     Te1/1/5
  31    6400.6a63.0049    DYNAMIC     Te1/1/5
  31    6400.6a84.6755    DYNAMIC     Te1/1/7
  31    6400.6a90.f887    DYNAMIC     Te1/1/7
  31    6451.0621.77e6    DYNAMIC     Te1/1/5
  31    685b.35ba.a754    DYNAMIC     Te1/1/4
  31    68fe.f708.7dd8    DYNAMIC     Te1/1/4
  31    6c3b.e514.a49a    DYNAMIC     Te1/1/3
  31    70e2.8413.39e3    DYNAMIC     Te1/1/3
  31    70f3.9504.bdf3    DYNAMIC     Te1/1/3
  31    74d0.2b27.dc3e    DYNAMIC     Te1/1/4
  31    7845.c43e.b13e    DYNAMIC     Te1/1/5
  31    787b.8ab2.f55d    DYNAMIC     Te1/1/7
  31    787b.8ad6.a607    DYNAMIC     Te1/1/3
  31    787b.8ad7.cac5    DYNAMIC     Te1/1/7
  31    787b.8ada.16a9    DYNAMIC     Te1/1/7
  31    7c8b.caf3.3f40    DYNAMIC     Te1/1/3
  31    8cec.4b5a.e9e0    DYNAMIC     Te1/1/5
  31    901b.0e8f.6702    DYNAMIC     Te1/1/3
  31    94c6.9111.bedf    DYNAMIC     Te1/1/5
  31    9890.96e3.92ed    DYNAMIC     Te1/1/3
  31    9c7b.ef82.a291    DYNAMIC     Te1/1/7
  31    a860.b636.21d1    DYNAMIC     Te1/1/4
  31    ac87.a314.cc0f    DYNAMIC     Te1/1/7
  31    b083.fea2.2c37    DYNAMIC     Te1/1/3
  31    c81f.663a.4acf    DYNAMIC     Te1/1/3
  31    c85b.76bc.2897    DYNAMIC     Te1/1/5
  31    c85b.76cd.2f1b    DYNAMIC     Te1/1/5
  31    c85b.76d0.e88c    DYNAMIC     Te1/1/5
  31    d027.88c7.4f53    DYNAMIC     Te1/1/5
  31    d081.7ada.ebda    DYNAMIC     Te1/1/4
  31    d89e.f301.5a1c    DYNAMIC     Te1/1/5
  31    d89e.f331.98c4    DYNAMIC     Te1/1/5
  31    d89e.f334.a768    DYNAMIC     Te1/1/5
  31    d89e.f39e.1e47    DYNAMIC     Te1/1/4
  31    dc4a.3e03.4b41    DYNAMIC     Te1/1/3
  31    ec9a.7435.04c6    DYNAMIC     Te1/1/3
  31    ecf4.bb04.3928    DYNAMIC     Te1/1/4
  31    f018.98eb.6001    DYNAMIC     Te1/1/4
            31    f092.1c60.ed4f    DYNAMIC     Te1/1/7
  31    f430.b973.393e    DYNAMIC     Te1/1/5
  31    f439.0946.24fc    DYNAMIC     Te1/1/5
  31    f481.39c7.2f03    DYNAMIC     Te1/1/4
  31    f48e.38a8.b80d    DYNAMIC     Te1/1/3
  31    f8b1.56a8.03d6    DYNAMIC     Te1/1/4
  31    f8b4.6a82.323c    DYNAMIC     Te1/1/4
  31    f8bc.1274.8bee    DYNAMIC     Te1/1/5
  31    f8d0.2734.7e7c    DYNAMIC     Te1/1/4
  31    fc4d.d43d.fcc9    DYNAMIC     Te1/1/7
 702    0000.0c9f.f2be    DYNAMIC     Po30
 702    0026.f36a.0000    DYNAMIC     Po30
 702    003a.9c3f.ffc1    DYNAMIC     Po30
 702    003a.9c40.5ec1    DYNAMIC     Po30
 702    0cc4.7aad.8ad3    DYNAMIC     Gi1/0/6
 702    0cc4.7aad.9bde    DYNAMIC     Gi1/0/5
 702    0cc4.7ab8.1bb4    DYNAMIC     Gi1/0/1
 702    a036.9f85.9572    DYNAMIC     Gi1/0/2
 702    a036.9f85.96e2    DYNAMIC     Gi1/0/3
 702    a036.9f85.96f0    DYNAMIC     Gi1/0/4
1603    0000.0c9f.f643    DYNAMIC     Po30
1603    0018.8515.f208    DYNAMIC     Te1/1/3
1603    0018.8516.472a    DYNAMIC     Te1/1/5
1603    0018.8516.61b1    DYNAMIC     Te1/1/3
1603    0018.8516.61c6    DYNAMIC     Gi1/0/11
1603    0018.8516.61ec    DYNAMIC     Te1/1/7
1603    0018.8516.6251    DYNAMIC     Te1/1/3
1603    0018.8516.6276    DYNAMIC     Te1/1/3
1603    0018.8516.d1e7    DYNAMIC     Gi1/0/12
1603    0018.8517.0078    DYNAMIC     Te1/1/3
1603    0018.8517.008f    DYNAMIC     Te1/1/7
1603    0018.8517.00a8    DYNAMIC     Te1/1/3
1603    0018.8517.00c4    DYNAMIC     Te1/1/5
1603    0018.8517.00da    DYNAMIC     Te1/1/5
1603    0018.8517.00df    DYNAMIC     Te1/1/5
1603    0018.8517.d02f    DYNAMIC     Te1/1/4
1603    0018.8517.d03a    DYNAMIC     Gi1/0/28
1603    0018.8517.d043    DYNAMIC     Gi1/0/27
1603    0018.8517.d058    DYNAMIC     Te1/1/4
1603    0018.8518.3703    DYNAMIC     Te1/1/3
1603    0018.851b.dd1a    DYNAMIC     Te1/1/3
1603    0026.f36a.0000    DYNAMIC     Po30
1603    003a.9c3f.ffc1    DYNAMIC     Po30
1603    003a.9c40.5ec1    DYNAMIC     Po30
1603    0040.8cea.672a    DYNAMIC     Te1/1/3
1603    0040.8cea.672c    DYNAMIC     Te1/1/3
1603    0040.8cea.6731    DYNAMIC     Te1/1/3
1603    0040.8ceb.e7f6    DYNAMIC     Te1/1/3
  33    0000.0c9f.f021    DYNAMIC     Po30
  33    0004.f258.d9d2    DYNAMIC     Te1/1/7
  33    0004.f270.dbf9    DYNAMIC     Te1/1/7
  33    0004.f273.87a2    DYNAMIC     Te1/1/7
  33    0004.f2cc.5c05    DYNAMIC     Te1/1/7
  33    0004.f2d1.5184    DYNAMIC     Te1/1/7
  33    0004.f2dc.7c19    DYNAMIC     Te1/1/4
  33    0009.6e06.9445    DYNAMIC     Te1/1/3
  33    0009.6e06.971f    DYNAMIC     Te1/1/3
  33    0009.6e06.98df    DYNAMIC     Te1/1/3
  33    0009.6e06.99d7    DYNAMIC     Te1/1/3
            33    001b.4f6c.3610    DYNAMIC     Te1/1/7
  33    001b.4f6c.3fae    DYNAMIC     Te1/1/3
  33    001b.4f6c.4031    DYNAMIC     Te1/1/3
  33    0026.f36a.0000    DYNAMIC     Po30
  33    003a.9c3f.ffc1    DYNAMIC     Po30
  33    003a.9c40.5ec1    DYNAMIC     Po30
  33    00e0.7524.8b85    DYNAMIC     Te1/1/4
  33    00e0.7524.8bbc    DYNAMIC     Te1/1/5
  33    10cd.ae63.983d    DYNAMIC     Te1/1/4
  33    10cd.ae63.ac63    DYNAMIC     Te1/1/7
  33    10cd.ae63.ae19    DYNAMIC     Te1/1/7
  33    10cd.ae63.ae1d    DYNAMIC     Te1/1/7
  33    10cd.ae64.4230    DYNAMIC     Te1/1/4
  33    10cd.ae64.48f4    DYNAMIC     Te1/1/4
  33    10cd.ae64.4c76    DYNAMIC     Te1/1/7
  33    10cd.ae64.4edf    DYNAMIC     Te1/1/7
  33    10cd.ae64.55d5    DYNAMIC     Te1/1/7
  33    10cd.ae64.55f9    DYNAMIC     Te1/1/4
  33    10cd.ae64.55fa    DYNAMIC     Te1/1/7
  33    10cd.ae64.5610    DYNAMIC     Te1/1/4
  33    10cd.ae64.5616    DYNAMIC     Te1/1/7
  33    10cd.ae64.562a    DYNAMIC     Te1/1/4
  33    10cd.ae64.564f    DYNAMIC     Te1/1/4
  33    10cd.ae64.5659    DYNAMIC     Te1/1/7
  33    10cd.ae64.5696    DYNAMIC     Te1/1/4
  33    10cd.ae64.56aa    DYNAMIC     Te1/1/7
  33    10cd.ae65.190a    DYNAMIC     Te1/1/7
  33    10cd.ae66.2815    DYNAMIC     Te1/1/4
  33    10cd.ae67.a838    DYNAMIC     Te1/1/7
  33    24d9.213d.0201    DYNAMIC     Te1/1/7
  33    24d9.213d.0246    DYNAMIC     Te1/1/7
  33    24d9.213d.0332    DYNAMIC     Te1/1/3
  33    24d9.213d.0344    DYNAMIC     Te1/1/5
  33    24d9.213d.037b    DYNAMIC     Te1/1/4
  33    24d9.2148.e82d    DYNAMIC     Te1/1/7
  33    2cf4.c5f7.a9e8    DYNAMIC     Te1/1/7
  33    2cf4.c5f7.aa27    DYNAMIC     Te1/1/4
  33    3475.c7e6.4f78    DYNAMIC     Te1/1/7
  33    3475.c7ea.4f91    DYNAMIC     Te1/1/5
  33    3475.c7eb.9d81    DYNAMIC     Te1/1/4
  33    50cd.22b4.2c26    DYNAMIC     Te1/1/7
  33    50cd.22b4.2c8c    DYNAMIC     Te1/1/7
  33    6416.7f1c.1627    DYNAMIC     Te1/1/4
  33    6416.7f1c.1dd6    DYNAMIC     Te1/1/4
  33    6416.7f1c.e15e    DYNAMIC     Te1/1/7
  33    6416.7f1f.6de1    DYNAMIC     Te1/1/7
  33    6416.7f3e.057b    DYNAMIC     Te1/1/7
  33    6416.7f3e.a658    DYNAMIC     Te1/1/4
  33    6416.7f4e.c1e1    DYNAMIC     Te1/1/7
  33    6416.7f9d.f63a    DYNAMIC     Te1/1/7
  33    6ca8.498f.5707    DYNAMIC     Te1/1/7
  33    6ca8.498f.7923    DYNAMIC     Te1/1/4
  33    6ca8.498f.7b5c    DYNAMIC     Te1/1/4
  33    6ca8.498f.829d    DYNAMIC     Te1/1/7
  33    6ca8.498f.830b    DYNAMIC     Te1/1/4
  33    6ca8.4991.2001    DYNAMIC     Te1/1/3
  33    707c.6901.0feb    DYNAMIC     Te1/1/7
  33    707c.6901.0ffe    DYNAMIC     Te1/1/7
  33    707c.6902.8e3d    DYNAMIC     Te1/1/7
            33    707c.6902.8e55    DYNAMIC     Te1/1/7
  33    8483.7180.44fb    DYNAMIC     Te1/1/4
  33    8483.7187.8cdf    DYNAMIC     Te1/1/5
  33    8483.7187.f181    DYNAMIC     Te1/1/4
  33    a009.ed03.89ed    DYNAMIC     Te1/1/5
  33    a009.ed08.71af    DYNAMIC     Te1/1/5
  33    a009.ed0a.7446    DYNAMIC     Te1/1/7
  33    a009.ed0a.7457    DYNAMIC     Te1/1/7
  33    a009.ed0a.746a    DYNAMIC     Te1/1/4
  33    a009.ed0a.7487    DYNAMIC     Te1/1/7
  33    a009.ed0a.9545    DYNAMIC     Te1/1/4
  33    a425.1bc1.514e    DYNAMIC     Te1/1/4
  33    a425.1bc2.8bf1    DYNAMIC     Te1/1/4
  33    a425.1bc2.8c21    DYNAMIC     Te1/1/4
  33    a425.1bc2.8c46    DYNAMIC     Te1/1/4
  33    a425.1bc2.8c83    DYNAMIC     Te1/1/4
  33    a425.1bc4.b700    DYNAMIC     Te1/1/5
  33    a425.1bc4.b93f    DYNAMIC     Te1/1/5
  33    a425.1bc4.c79e    DYNAMIC     Te1/1/5
  33    a478.86ba.b865    DYNAMIC     Te1/1/5
  33    b447.5ea3.87af    DYNAMIC     Te1/1/3
  33    b447.5ea3.8864    DYNAMIC     Te1/1/7
  33    b447.5ea5.ac07    DYNAMIC     Te1/1/7
  33    b447.5ea7.a10b    DYNAMIC     Te1/1/7
  33    b447.5ea9.0adb    DYNAMIC     Te1/1/4
  33    b447.5ead.f7ed    DYNAMIC     Te1/1/4
  33    b447.5eae.92a4    DYNAMIC     Te1/1/7
  33    b447.5eae.988f    DYNAMIC     Te1/1/7
  33    b447.5eae.fdc8    DYNAMIC     Te1/1/4
  33    b447.5eaf.2232    DYNAMIC     Te1/1/5
  33    b447.5eaf.9651    DYNAMIC     Te1/1/7
  33    b447.5eb0.9fc1    DYNAMIC     Te1/1/5
  33    b447.5eb1.0fce    DYNAMIC     Te1/1/5
  33    b447.5eb2.ac5f    DYNAMIC     Te1/1/5
  33    b447.5eb2.aca4    DYNAMIC     Te1/1/7
  33    b447.5eb2.acaa    DYNAMIC     Te1/1/5
  33    b447.5eb3.4db6    DYNAMIC     Te1/1/7
  33    b4b0.177f.d20b    DYNAMIC     Te1/1/7
  33    c057.bc20.edfb    DYNAMIC     Te1/1/5
  33    c057.bc20.ef01    DYNAMIC     Te1/1/7
  33    c057.bc25.308d    DYNAMIC     Te1/1/4
  33    c057.bc25.3210    DYNAMIC     Te1/1/7
  33    c057.bc29.8e68    DYNAMIC     Te1/1/5
  33    c81f.ea6a.e924    DYNAMIC     Te1/1/7
  33    c81f.ea6a.e934    DYNAMIC     Te1/1/7
  33    c81f.ea6a.e93a    DYNAMIC     Te1/1/7
  33    c81f.ea6b.ba0e    DYNAMIC     Te1/1/4
  33    c81f.ea6b.c2d1    DYNAMIC     Te1/1/4
  33    c81f.ea6b.c334    DYNAMIC     Te1/1/4
  33    c81f.ea6b.c33e    DYNAMIC     Te1/1/4
  33    c81f.ea6b.c353    DYNAMIC     Te1/1/7
  33    c81f.ea6b.c3a3    DYNAMIC     Te1/1/4
  33    ccf9.54aa.41db    DYNAMIC     Te1/1/4
  33    ccf9.54aa.423b    DYNAMIC     Te1/1/4
  33    d478.5605.55ce    DYNAMIC     Te1/1/7
  33    d478.56b1.2208    DYNAMIC     Te1/1/5
  33    d478.56b1.2507    DYNAMIC     Te1/1/5
  33    d478.56b1.2bee    DYNAMIC     Te1/1/5
  33    d478.56b1.2bfa    DYNAMIC     Te1/1/5
            33    d478.56b6.2835    DYNAMIC     Te1/1/7
  33    d478.56b6.2944    DYNAMIC     Te1/1/7
  33    d478.56b6.295e    DYNAMIC     Te1/1/5
  33    d478.56b6.877b    DYNAMIC     Te1/1/4
  33    d478.56b6.cfda    DYNAMIC     Te1/1/7
  33    f873.a2ee.cf91    DYNAMIC     Te1/1/3
  33    f873.a2ef.2129    DYNAMIC     Te1/1/7
  33    f873.a2ef.5778    DYNAMIC     Te1/1/7
  33    f873.a2ef.e858    DYNAMIC     Te1/1/7
  33    f873.a2ef.fe0c    DYNAMIC     Te1/1/7
  34    0000.0c9f.f022    DYNAMIC     Po30
  34    0023.24ec.a2e8    DYNAMIC     Te1/1/5
  34    0023.24ec.a30d    DYNAMIC     Te1/1/5
  34    0023.24ec.a370    DYNAMIC     Te1/1/5
  34    0023.24ec.a386    DYNAMIC     Te1/1/5
  34    0023.24ec.a709    DYNAMIC     Te1/1/5
  34    0026.f36a.0000    DYNAMIC     Po30
  34    003a.9c3f.ffc1    DYNAMIC     Po30
  34    003a.9c40.5ec1    DYNAMIC     Po30
  34    2426.42b4.eb35    DYNAMIC     Te1/1/7
  34    309c.237d.46bd    DYNAMIC     Te1/1/7
  34    40b0.3424.59b5    DYNAMIC     Te1/1/5
  34    4ccc.6ae3.de02    DYNAMIC     Te1/1/7
  34    4ccc.6ae8.c11a    DYNAMIC     Te1/1/7
  34    54e1.ad8b.8cde    DYNAMIC     Te1/1/7
  34    5820.b14c.979d    DYNAMIC     Te1/1/4
  34    8c16.4592.80e0    DYNAMIC     Te1/1/7
  34    8c16.45a2.9c17    DYNAMIC     Te1/1/4
  34    8c16.45b5.e048    DYNAMIC     Te1/1/7
  34    8c16.45e2.9f3c    DYNAMIC     Te1/1/7
  34    d0bf.9c32.88ce    DYNAMIC     Te1/1/7
  35    0000.0c9f.f023    DYNAMIC     Po30
  35    0026.f36a.0000    DYNAMIC     Po30
  35    003a.9c40.5ec1    DYNAMIC     Po30
  36    0000.0c9f.f024    DYNAMIC     Po30
  36    0026.f36a.0000    DYNAMIC     Po30
  36    003a.9c40.5ec1    DYNAMIC     Po30
  40    0000.0c9f.f028    DYNAMIC     Po30
  40    0026.f36a.0000    DYNAMIC     Po30
  40    003a.9c40.5ec1    DYNAMIC     Po30
 330    0000.0c9f.f14a    DYNAMIC     Po30
 330    0001.f089.a498    DYNAMIC     Te1/1/5
 330    0001.f08f.3078    DYNAMIC     Te1/1/3
 330    001e.c605.3847    DYNAMIC     Te1/1/5
 330    001e.c605.3ca2    DYNAMIC     Te1/1/5
 330    0026.f36a.0000    DYNAMIC     Po30
 330    003a.9c3f.ffc1    DYNAMIC     Po30
 330    003a.9c40.5ec1    DYNAMIC     Po30
 330    3045.1185.93d6    DYNAMIC     Te1/1/4
 330    3045.1185.a198    DYNAMIC     Te1/1/3
 330    3045.11a3.f2d9    DYNAMIC     Te1/1/3
 330    3045.11ae.1408    DYNAMIC     Te1/1/5
 623    0000.0c9f.f26f    DYNAMIC     Po30
 623    0026.f36a.0000    DYNAMIC     Po30
 623    003a.9c3f.ffc1    DYNAMIC     Po30
 623    003a.9c40.5ec1    DYNAMIC     Po30
 623    0050.f901.6814    DYNAMIC     Te1/1/3
 623    0050.f901.881a    DYNAMIC     Te1/1/3
 623    0050.f901.88b4    DYNAMIC     Te1/1/7
           623    0050.f901.88b9    DYNAMIC     Te1/1/3
 779    0000.0c9f.f30b    DYNAMIC     Po30
 779    0026.f36a.0000    DYNAMIC     Po30
 779    003a.9c40.5ec1    DYNAMIC     Po30
1024    0000.0c9f.f400    DYNAMIC     Po30
1024    0026.f36a.0000    DYNAMIC     Po30
1024    003a.9c3f.ffc1    DYNAMIC     Po30
1024    003a.9c40.5ec1    DYNAMIC     Po30
1024    10dd.b1b0.c94e    DYNAMIC     Te1/1/3
1024    406c.8f3e.022f    DYNAMIC     Te1/1/3
1024    787b.8ad6.a473    DYNAMIC     Te1/1/3
1024    e0d5.5e43.64ec    DYNAMIC     Te1/1/3
1034    0026.f36a.0000    DYNAMIC     Po30
1045    0026.f36a.0000    DYNAMIC     Po30
1095    0000.0c9f.f447    DYNAMIC     Po30
1095    0026.f36a.0000    DYNAMIC     Po30
1095    003a.9c40.5ec1    DYNAMIC     Po30
1097    0026.f36a.0000    DYNAMIC     Po30
1160    0000.0c9f.f488    DYNAMIC     Po30
1160    0026.f36a.0000    DYNAMIC     Po30
1160    003a.9c3f.ffc1    DYNAMIC     Po30
1160    003a.9c40.5ec1    DYNAMIC     Po30
1160    003e.e1c5.2f7a    DYNAMIC     Te1/1/7
1160    003e.e1c7.138e    DYNAMIC     Te1/1/7
1160    90b1.1c6a.6efa    DYNAMIC     Te1/1/7
Total Mac Addresses for this criterion: 492""",
 'show run | section tacacs':"""aaa group server tacacs+ NOC-TAC
 server name TAC-EBC
 server name TAC-SECONDARY
tacacs server TAC-EBC
 address ipv4 172.31.17.180
 key 7 022F405E22420A036C4C1058
tacacs server TAC-SECONDARY
 address ipv4 10.64.32.5
 key 7 143E560E25402F09042A2A74""",
 'show run | in tacacs':"""aaa group server tacacs+ NOC-TAC
tacacs server TAC-EBC
tacacs server TAC-SECONDARY""",
 'show power inline':"""Module   Available     Used     Remaining
          (Watts)     (Watts)    (Watts) 
------   ---------   --------   ---------
1          1835.0       61.6      1773.4
Interface Admin  Oper       Power   Device              Class Max
                            (Watts)                            
--------- ------ ---------- ------- ------------------- ----- ----
Gi1/0/1   auto   off        0.0     n/a                 n/a   60.0 
Gi1/0/2   auto   off        0.0     n/a                 n/a   60.0 
Gi1/0/3   auto   off        0.0     n/a                 n/a   60.0 
Gi1/0/4   auto   off        0.0     n/a                 n/a   60.0 
Gi1/0/5   auto   off        0.0     n/a                 n/a   60.0 
Gi1/0/6   auto   off        0.0     n/a                 n/a   60.0 
Gi1/0/7   auto   off        0.0     n/a                 n/a   60.0 
Gi1/0/8   auto   off        0.0     n/a                 n/a   60.0 
Gi1/0/9   auto   off        0.0     n/a                 n/a   60.0 
Gi1/0/10  auto   off        0.0     n/a                 n/a   60.0 
Gi1/0/11  auto   on         15.4    Ieee PD             0     60.0 
Gi1/0/12  auto   on         15.4    Ieee PD             0     60.0 
Gi1/0/13  auto   off        0.0     n/a                 n/a   60.0 
Gi1/0/14  auto   off        0.0     n/a                 n/a   60.0 
Gi1/0/15  auto   off        0.0     n/a                 n/a   60.0 
Gi1/0/16  auto   off        0.0     n/a                 n/a   60.0 
Gi1/0/17  auto   off        0.0     n/a                 n/a   60.0 
Gi1/0/18  auto   off        0.0     n/a                 n/a   60.0 
Gi1/0/19  auto   off        0.0     n/a                 n/a   60.0 
Gi1/0/20  auto   off        0.0     n/a                 n/a   60.0 
Gi1/0/21  auto   off        0.0     n/a                 n/a   60.0 
Gi1/0/22  auto   off        0.0     n/a                 n/a   60.0 
Gi1/0/23  auto   off        0.0     n/a                 n/a   60.0 
Gi1/0/24  auto   off        0.0     n/a                 n/a   60.0 
Gi1/0/25  auto   off        0.0     n/a                 n/a   60.0 
Gi1/0/26  auto   off        0.0     n/a                 n/a   60.0 
Gi1/0/27  auto   on         15.4    Ieee PD             3     60.0 
Gi1/0/28  auto   on         15.4    Ieee PD             3     60.0 
Gi1/0/29  auto   off        0.0     n/a                 n/a   60.0 
Gi1/0/30  auto   off        0.0     n/a                 n/a   60.0 
Gi1/0/31  auto   off        0.0     n/a                 n/a   60.0 
Gi1/0/32  auto   off        0.0     n/a                 n/a   60.0 
Gi1/0/33  auto   off        0.0     n/a                 n/a   60.0 
Gi1/0/34  auto   off        0.0     n/a                 n/a   60.0 
Gi1/0/35  auto   off        0.0     n/a                 n/a   60.0 
Gi1/0/36  auto   off        0.0     n/a                 n/a   60.0 
Gi1/0/37  auto   off        0.0     n/a                 n/a   60.0 
Gi1/0/38  auto   off        0.0     n/a                 n/a   60.0 
Gi1/0/39  auto   off        0.0     n/a                 n/a   60.0 
Gi1/0/40  auto   off        0.0     n/a                 n/a   60.0 
Gi1/0/41  auto   off        0.0     n/a                 n/a   60.0 
Gi1/0/42  auto   off        0.0     n/a                 n/a   60.0 
Gi1/0/43  auto   off        0.0     n/a                 n/a   60.0 
Gi1/0/44  auto   off        0.0     n/a                 n/a   60.0 
Gi1/0/45  auto   off        0.0     n/a                 n/a   60.0 
Gi1/0/46  auto   off        0.0     n/a                 n/a   60.0 
Gi1/0/47  auto   off        0.0     n/a                 n/a   60.0 
Gi1/0/48  auto   off        0.0     n/a                 n/a   60.0 """,
 'show environment all':"""Switch	 FAN	 Speed	 State
---------------------------------------------------
  1  	  1	13760 	  OK
  1  	  2	13760 	  OK
  1  	  3	13760 	  OK
FAN PS-1 is OK
FAN PS-2 is OK
Switch 1: SYSTEM TEMPERATURE is OK
Inlet Temperature Value: 23 Degree Celsius
Temperature State: GREEN
Yellow Threshold : 46 Degree Celsius
Red Threshold    : 56 Degree Celsius

Outlet Temperature Value: 32 Degree Celsius
Temperature State: GREEN
Yellow Threshold : 105 Degree Celsius
Red Threshold    : 125 Degree Celsius

Hotspot Temperature Value: 45 Degree Celsius
Temperature State: GREEN
Yellow Threshold : 105 Degree Celsius
Red Threshold    : 125 Degree Celsius
SW  PID                 Serial#     Status           Sys Pwr  PoE Pwr  Watts
--  ------------------  ----------  ---------------  -------  -------  -----
1A  PWR-C1-1100WAC      LIT21512AYM  OK              Good     Good     1100
1B  PWR-C1-1100WAC      LIT21514AW9  OK              Good     Good     1100
""",
}
