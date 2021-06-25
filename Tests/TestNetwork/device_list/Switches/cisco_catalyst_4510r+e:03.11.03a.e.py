ip_address = '172.31.128.133'
software = 'software'
hardware = 'hardware'
read_results = {
 'show version':"""Cisco IOS Software, IOS-XE Software, Catalyst 4500 L3 Switch  Software (cat4500e-UNIVERSALK9-M), Version 03.11.03a.E RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2020 by Cisco Systems, Inc.
Compiled Fri 18-Sep-20 17:04 by prod_rel_team



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



ROM: 15.0(1r)SG5
sx1-112mrsc-2 uptime is 15 weeks, 1 day, 16 hours, 55 minutes
Uptime for this control processor is 15 weeks, 1 day, 16 hours, 57 minutes
System returned to ROM by reload
System restarted at 22:31:48 MST Wed Mar 10 2021
System image file is "bootflash:cat4500e-universalk9.SPA.03.11.03a.E.152-7.E3a.bin"
Jawa Revision 7, Snowtrooper Revision 0x0.0x1C

Last reload reason: reason IOS UPgrade



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


License Information for 'WS-X45-SUP7-E'
    License Level: lanbase   Type: Permanent
    Next reboot license Level: lanbase

cisco WS-C4510R+E (MPC8572) processor (revision 10) with 2097152K bytes of physical memory.
Processor board ID FOX1619GMW9
MPC8572 CPU at 1.5GHz, Supervisor 7
Last reset from Reload
2 Virtual Ethernet interfaces
336 Gigabit Ethernet interfaces
          4 Ten Gigabit Ethernet interfaces
511K bytes of non-volatile configuration memory.

Configuration register is 0x2102
""",
 'show run':"""Building configuration...

Current configuration : 65531 bytes
!
! Last configuration change at 11:40:33 MDT Mon Apr 26 2021 by noc-orionncm
! NVRAM config last updated at 21:06:13 MDT Sun Jun 20 2021 by noc-orionncm
!
version 15.2
no service pad
service timestamps debug datetime msec localtime
service timestamps log datetime msec localtime
service password-encryption
service compress-config
!
hostname sx1-112mrsc-2
!
boot-start-marker
boot system flash bootflash:cat4500e-universalk9.SPA.03.11.03a.E.152-7.E3a.bin
boot-end-marker
!
!
vrf definition mgmtVrf
 !
 address-family ipv4
 exit-address-family
 !
 address-family ipv6
 exit-address-family
!
logging buffered notifications
logging console critical
enable secret 4 AxX6fbAku8l9zKY4O7ZcdfBJJY.70T3owqL/RFJ.JEU
!
aaa new-model
!
!
aaa group server tacacs+ NOC-TAC
 server name TAC-EBC
 server name TAC-SECONDARY
!
aaa authentication login default group NOC-TAC line enable none
aaa authentication login console line enable
aaa authentication enable default group NOC-TAC enable
aaa authorization config-commands
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
vtp mode transparent
!
crypto pki trustpoint CISCO_IDEVID_SUDI
 revocation-check none
 rsakeypair CISCO_IDEVID_SUDI
!
crypto pki trustpoint CISCO_IDEVID_SUDI0
 revocation-check none
!
!
crypto pki certificate chain CISCO_IDEVID_SUDI
 certificate 7F68E77D00000005E00F
  30820452 3082033A A0030201 02020A7F 68E77D00 000005E0 0F300D06 092A8648 
  86F70D01 01050500 30393116 30140603 55040A13 0D436973 636F2053 79737465 
  6D73311F 301D0603 55040313 16436973 636F204D 616E7566 61637475 72696E67 
  20434130 1E170D31 32303530 37323135 3234395A 170D3232 30353037 32323032 
  34395A30 50312930 27060355 04051320 5049443A 57532D58 34352D53 5550372D 
  4520534E 3A434154 31363137 4C355358 31233021 06035504 03131A57 532D5834 
  352D5355 50372D45 2D303032 35383462 32373531 32308201 22300D06 092A8648 
  86F70D01 01010500 0382010F 00308201 0A028201 0100B764 CE91675E CF92D3AB 
  190E2E54 49820C16 8717C265 1BDC3477 5D31A4DA A132B7A2 C53F0FBE 0535A820 
  61782EB7 5FB88AFE B72FEDA6 78111726 7835AA1C 989EE3A0 88E47D7E E8A3E999 
  AE99536C 5A02FC7F EA6F2024 EFA2C4EE 1F08E2C8 CFAE9CC1 5325FF36 03640702 
  4D2DA9B8 F77E2992 7692ECF8 8405F53B E5B04249 BD4AD6E5 567D4F10 0CDDAA85 
  66E9241D 64B88793 D6653D77 E0C5584F B987BA04 29C2E27E D4789424 0FE9829B 
  E5829C51 A9E73961 5BDB090A 6C7C0C27 D0D16E5C 7BC678FF 654958B3 B7C8B862 
  F460B1AA 07A37388 9BF1937D 5D1C7E69 382DBF15 4571721B 242B556F 8C72D769 
  B0B88398 26D50F91 73B7E6FD 4AFEC177 F399D553 A0930203 010001A3 82014330 
  82013F30 0E060355 1D0F0101 FF040403 0204F030 1D060355 1D250416 30140608 
  2B060105 05070301 06082B06 01050507 0302301D 0603551D 0E041604 14028D32 
  693A1D3A 8DACD7EE CC67AA01 3D2A949F 70301F06 03551D23 04183016 8014D0C5 
  2226AB4F 4660ECAE 0591C7DC 5AD1B047 F76C303F 0603551D 1F043830 363034A0 
  32A03086 2E687474 703A2F2F 7777772E 63697363 6F2E636F 6D2F7365 63757269 
  74792F70 6B692F63 726C2F63 6D63612E 63726C30 4C06082B 06010505 07010104 
  40303E30 3C06082B 06010505 07300286 30687474 703A2F2F 7777772E 63697363 
  6F2E636F 6D2F7365 63757269 74792F70 6B692F63 65727473 2F636D63 612E6365 
  72303F06 092B0601 04018237 14020432 1E300049 00500053 00450043 0049006E 
  00740065 0072006D 00650064 00690061 00740065 004F0066 0066006C 0069006E 
  0065300D 06092A86 4886F70D 01010505 00038201 0100993A CA82643D 17FC7D87 
  A04B8080 CA605719 BAEA63A5 3078172A D65AACEE 2F36AE95 211BB5D9 848B6300 
  AF558BAB 3E7798C4 17C3E57F 0424E25B C489D32B CB30555A 6F56F5D9 A90D49FC 
  24E5D4F7 3786581F 108A58EA 17B62AEC 40ADD852 772E7467 E13F8B9E 4E9F44F0 
  288B820A F9DCDB50 221B0A2C 91787237 863640D4 44420DA7 885A5801 2FD5DEA5 
  FE2AA666 6BA96D32 4A4D8022 3BD2A5F9 CA836E4C D98414BA CBC34DFB 8CC32DB9 
  596DA079 783F80DE 8D8C8562 278EB7F1 DB6A5BE6 C0065C78 BD043630 C6E2D508 
  0AC44CDA DE0FBB03 38D45CB2 CF765C8D EE117ABC 3F815FD3 58ACD0CB 69AFF228 
            450CA590 84BFE3E9 AFB184DD 58C20221 34C15ED9 3B3E
  	quit
 certificate ca 6A6967B3000000000003
  308204D9 308203C1 A0030201 02020A6A 6967B300 00000000 03300D06 092A8648 
  86F70D01 01050500 30353116 30140603 55040A13 0D436973 636F2053 79737465 
  6D73311B 30190603 55040313 12436973 636F2052 6F6F7420 43412032 30343830 
  1E170D30 35303631 30323231 3630315A 170D3239 30353134 32303235 34325A30 
  39311630 14060355 040A130D 43697363 6F205379 7374656D 73311F30 1D060355 
  04031316 43697363 6F204D61 6E756661 63747572 696E6720 43413082 0120300D 
  06092A86 4886F70D 01010105 00038201 0D003082 01080282 010100A0 C5F7DC96 
  943515F1 F4994EBB 9B41E17D DB791691 BBF354F2 414A9432 6262C923 F79AE7BB 
  9B79E807 294E30F5 AE1BC521 5646B0F8 F4E68E81 B816CCA8 9B85D242 81DB7CCB 
  94A91161 121C5CEA 33201C9A 16A77DDB 99066AE2 36AFECF8 0AFF9867 07F430EE 
  A5F8881A AAE8C73C 1CCEEE48 FDCD5C37 F186939E 3D71757D 34EE4B14 A9C0297B 
  0510EF87 9E693130 F548363F D8ABCE15 E2E8589F 3E627104 8726A415 620125AA 
  D5DFC9C9 5BB8C9A1 077BBE68 92939320 A86CBD15 75D3445D 454BECA8 DA60C7D8 
  C8D5C8ED 41E1F55F 578E5332 9349D5D9 0FF836AA 07C43241 C5A7AF1D 19FFF673 
  99395A73 67621334 0D1F5E95 70526417 06EC535C 5CDB6AEA 35004102 0103A382 
  01E73082 01E33012 0603551D 130101FF 04083006 0101FF02 0100301D 0603551D 
  0E041604 14D0C522 26AB4F46 60ECAE05 91C7DC5A D1B047F7 6C300B06 03551D0F 
  04040302 01863010 06092B06 01040182 37150104 03020100 30190609 2B060104 
  01823714 02040C1E 0A005300 75006200 43004130 1F060355 1D230418 30168014 
  27F3C815 1E6E9A02 0916AD2B A089605F DA7B2FAA 30430603 551D1F04 3C303A30 
  38A036A0 34863268 7474703A 2F2F7777 772E6369 73636F2E 636F6D2F 73656375 
  72697479 2F706B69 2F63726C 2F637263 61323034 382E6372 6C305006 082B0601 
  05050701 01044430 42304006 082B0601 05050730 02863468 7474703A 2F2F7777 
  772E6369 73636F2E 636F6D2F 73656375 72697479 2F706B69 2F636572 74732F63 
  72636132 3034382E 63657230 5C060355 1D200455 30533051 060A2B06 01040109 
  15010200 30433041 06082B06 01050507 02011635 68747470 3A2F2F77 77772E63 
  6973636F 2E636F6D 2F736563 75726974 792F706B 692F706F 6C696369 65732F69 
  6E646578 2E68746D 6C305E06 03551D25 04573055 06082B06 01050507 03010608 
  2B060105 05070302 06082B06 01050507 03050608 2B060105 05070306 06082B06 
  01050507 0307060A 2B060104 0182370A 0301060A 2B060104 01823714 02010609 
  2B060104 01823715 06300D06 092A8648 86F70D01 01050500 03820101 0030F330 
  2D8CF2CA 374A6499 24290AF2 86AA42D5 23E8A2EA 2B6F6923 7A828E1C 4C09CFA4 
  4FAB842F 37E96560 D19AC6D8 F30BF5DE D027005C 6F1D91BD D14E5851 1DC9E3F7 
  38E7D30B D168BE8E 22A54B06 E1E6A4AA 337D1A75 BA26F370 C66100A5 C379265B 
  A719D193 8DAB9B10 11291FA1 82FDFD3C 4B6E65DC 934505E9 AF336B67 23070686 
  22DAEBDC 87CF5921 421AE9CF 707588E0 243D5D7D 4E963880 97D56FF0 9B71D8BA 
  6019A5B0 6186ADDD 6566F6B9 27A2EE2F 619BBAA1 3061FDBE AC3514F9 B82D9706 
  AFC3EF6D CC3D3CEB 95E981D3 8A5EB6CE FA79A46B D7A25764 C43F4CC9 DBE882EC 
  0166D410 88A256E5 3C57EDE9 02A84891 6307AB61 264B1A13 9FE4DCDA 5F
  	quit
crypto pki certificate chain CISCO_IDEVID_SUDI0
 certificate ca 5FF87B282B54DC8D42A315B568C9ADFF
  30820343 3082022B A0030201 0202105F F87B282B 54DC8D42 A315B568 C9ADFF30 
  0D06092A 864886F7 0D010105 05003035 31163014 06035504 0A130D43 6973636F 
  20537973 74656D73 311B3019 06035504 03131243 6973636F 20526F6F 74204341 
  20323034 38301E17 0D303430 35313432 30313731 325A170D 32393035 31343230 
  32353432 5A303531 16301406 0355040A 130D4369 73636F20 53797374 656D7331 
  1B301906 03550403 13124369 73636F20 526F6F74 20434120 32303438 30820120 
  300D0609 2A864886 F70D0101 01050003 82010D00 30820108 02820101 00B09AB9 
  ABA7AF0A 77A7E271 B6B46662 94788847 C6625584 4032BFC0 AB2EA51C 71D6BC6E 
  7BA8AABA 6ED21588 48459DA2 FC83D0CC B98CE026 68704A78 DF21179E F46105C9 
  15C8CF16 DA356189 9443A884 A8319878 9BB94E6F 2C53126C CD1DAD2B 24BB31C4 
  2BFF8344 6FB63D24 7709EABF 2AA81F6A 56F6200F 11549781 75A725CE 596A8265 
  EFB7EAE7 E28D758B 6EF2DD4F A65E629C CF100A64 D04E6DCE 2BCC5BF5 60A52747 
  8D69F47F CE1B70DE 701B20D6 6ECDA601 A83C12D2 A93FA06B 5EBB8E20 8B7A91E3 
  B568EEA0 E7C40174 A8530B2B 4A9A0F65 120E824D 8E63FDEF EB9B1ADB 53A61360 
            AFC27DD7 C76C1725 D473FB47 64508180 944CE1BF AE4B1CDF 92ED2E05 DF020103 
  A351304F 300B0603 551D0F04 04030201 86300F06 03551D13 0101FF04 05300301 
  01FF301D 0603551D 0E041604 1427F3C8 151E6E9A 020916AD 2BA08960 5FDA7B2F 
  AA301006 092B0601 04018237 15010403 02010030 0D06092A 864886F7 0D010105 
  05000382 0101009D 9D8484A3 41A97C77 0CB753CA 4E445062 EF547CD3 75171CE8 
  E0C6484B B6FE4C3A 198156B0 56EE1996 62AA5AA3 64C1F64E 5433C677 FEC51CBA 
  E55D25CA F5F0939A 83112EE6 CBF87445 FEE705B8 ABE7DFCB 4BE13784 DAB98B97 
  701EF0E2 8BD7B0D8 0E9DB169 D62A917B A9494F7E E68E95D8 83273CD5 68490ED4 
  9DF62EEB A7BEEB30 A4AC1F44 FC95AB33 06FB7D60 0ADEB48A 63B09CA9 F2A4B953 
  0187D068 A4277FAB FFE9FAC9 40388867 B439C684 6F57C953 DBBA8EEE C043B2F8 
  09836EFF 66CF3EEF 17B35818 2509345E E3CBD614 B6ECF292 6F74E42F 812AD592 
  91E0E097 3C326805 854BD1F7 57E2521D 931A549F 0570C04A 71601E43 0B601EFE 
  A3CE8119 E10B35
  	quit
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
errdisable recovery cause unicast-flood
errdisable recovery cause vmps
errdisable recovery cause storm-control
errdisable recovery cause inline-power
errdisable recovery cause arp-inspection
errdisable recovery cause link-monitor-failure
errdisable recovery cause oam-remote-failure
errdisable recovery cause psp
power redundancy-mode combined
file prompt quiet
!
spanning-tree mode rapid-pvst
spanning-tree extend system-id
!
redundancy
 mode rpr
!
vlan internal allocation policy ascending
!
vlan 120
 name fort-112mrsc-laundry
!
vlan 170
 name fort-orl-admin
!
vlan 202
 name fort-112honorshousing-voip 
!
vlan 365
 name fort-112mrsc-ca-wired
          !
vlan 460
 name 0112Marriott-Honors-Red-Print
!
vlan 479
 name fort-112mrsc-wifi
!
vlan 504
 name fort-honors
!
vlan 505
 name fort-815vlgc-foodserv
!
vlan 520
 name fort-112mrsc-TLT-AirMedia
!
vlan 601
 name fort-112dgmr-ccure
!
vlan 611
 name fort-112mrsc-id
!
vlan 646
 name fort-112mrsc-blackboard
!
vlan 656
 name fort-112mrsc-fm
!
vlan 772
 name fort-112mrsc-ehs
!
vlan 874
 name fort-112mrsc-m
!
vlan 1103
 name fort-112-kronos
!
vlan 1133
 name fort-112-BoostPOS
!
vlan 1624
 name fort-112honors-res-camera
lldp run
!
!
!
!
!
!
!
interface FastEthernet1
 vrf forwarding mgmtVrf
 no ip address
 shutdown
 speed auto
 duplex auto
!
interface GigabitEthernet1/1
 description ACCESS POINT
           switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet1/2
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet1/3
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet1/4
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet1/5
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet1/6
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet1/7
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet1/8
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet1/9
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet1/10
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet1/11
           description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet1/12
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet1/13
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet1/14
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet1/15
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet1/16
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet1/17
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet1/18
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet1/19
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet1/20
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
!
          interface GigabitEthernet1/21
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet1/22
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet1/23
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet1/24
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet1/25
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
 spanning-tree portfast edge
!
interface GigabitEthernet1/26
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet1/27
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet1/28
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet1/29
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet1/30
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
           spanning-tree portfast edge
!
interface GigabitEthernet1/31
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet1/32
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet1/33
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet1/34
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet1/35
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet1/36
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet1/37
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet1/38
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
 spanning-tree portfast edge
!
interface GigabitEthernet1/39
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet1/40
           switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet1/41
 switchport access vlan 170
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet1/42
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet1/43
 description red-print-kiosk
 switchport access vlan 460
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet1/44
 switchport access vlan 601
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet1/45
 switchport access vlan 601
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet1/46
 switchport access vlan 601
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet1/47
 switchport access vlan 601
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet1/48
 switchport access vlan 611
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet2/1
 switchport access vlan 170
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet2/2
 switchport access vlan 170
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet2/3
           switchport access vlan 170
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet2/4
 switchport access vlan 170
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet2/5
 switchport access vlan 170
 switchport mode access
 switchport voice vlan 202
 spanning-tree portfast edge
!
interface GigabitEthernet2/6
 switchport access vlan 170
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet2/7
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet2/8
 switchport access vlan 170
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet2/9
 switchport access vlan 170
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet2/10
 switchport access vlan 170
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet2/11
 switchport access vlan 170
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet2/12
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
!
interface GigabitEthernet2/13
 switchport access vlan 170
 switchport mode access
 switchport voice vlan 202
 spanning-tree portfast edge
!
interface GigabitEthernet2/14
 switchport access vlan 170
           switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet2/15
 switchport access vlan 1103
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet2/16
 switchport access vlan 504
 switchport mode access
 switchport voice vlan 202
 spanning-tree portfast edge
!
interface GigabitEthernet2/17
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
!
interface GigabitEthernet2/18
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
!
interface GigabitEthernet2/19
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
 spanning-tree portfast edge
!
interface GigabitEthernet2/20
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
!
interface GigabitEthernet2/21
 switchport access vlan 505
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet2/22
 switchport access vlan 365
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet2/23
 switchport access vlan 170
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet2/24
 switchport access vlan 646
 switchport mode access
 spanning-tree portfast edge
!
          interface GigabitEthernet2/25
 switchport access vlan 504
 switchport mode access
 switchport voice vlan 202
 spanning-tree portfast edge
!
interface GigabitEthernet2/26
 switchport access vlan 504
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet2/27
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
!
interface GigabitEthernet2/28
 switchport access vlan 504
 switchport mode access
 switchport voice vlan 202
 spanning-tree portfast edge
!
interface GigabitEthernet2/29
 switchport access vlan 504
 switchport mode access
 switchport voice vlan 202
 spanning-tree portfast edge
!
interface GigabitEthernet2/30
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
!
interface GigabitEthernet2/31
 description CAM
 switchport access vlan 1624
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet2/32
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
!
interface GigabitEthernet2/33
 description CAM
 switchport access vlan 1624
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet2/34
 description CAM
 switchport access vlan 1624
 switchport mode access
 spanning-tree portfast edge
!
          interface GigabitEthernet2/35
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet2/36
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet2/37
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet2/38
 switchport access vlan 365
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet2/39
 switchport access vlan 505
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet2/40
 switchport access vlan 505
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet2/41
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
!
interface GigabitEthernet2/42
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet2/43
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet2/44
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet2/45
           switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet2/46
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet2/47
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet2/48
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet3/1
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet3/2
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
!
interface GigabitEthernet3/3
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet3/4
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet3/5
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet3/6
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
           switchport mode trunk
!
interface GigabitEthernet3/7
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet3/8
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet3/9
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet3/10
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet3/11
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet3/12
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet3/13
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet3/14
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
!
interface GigabitEthernet3/15
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet3/16
 switchport access vlan 170
 switchport mode access
           switchport voice vlan 202
 spanning-tree portfast edge
!
interface GigabitEthernet3/17
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet3/18
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet3/19
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet3/20
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet3/21
 switchport access vlan 170
 switchport mode access
 switchport voice vlan 202
 spanning-tree portfast edge
!
interface GigabitEthernet3/22
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet3/23
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
!
interface GigabitEthernet3/24
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet3/25
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet3/26
 switchport access vlan 365
           switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet3/27
 switchport access vlan 520
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet3/28
 switchport access vlan 520
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet3/29
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet3/30
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet3/31
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet3/32
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet3/33
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet3/34
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet3/35
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet3/36
 switchport access vlan 365
 switchport mode access
           ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet3/37
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet3/38
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet3/39
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet3/40
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet3/41
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet3/42
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet3/43
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet3/44
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet3/45
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet3/46
 switchport access vlan 365
           switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet3/47
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet3/48
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet4/1
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet4/2
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet4/3
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet4/4
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet4/5
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet4/6
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet4/7
 switchport access vlan 365
 switchport mode access
           ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet4/8
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet4/9
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet4/10
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
!
interface GigabitEthernet4/11
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet4/12
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet4/13
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet4/14
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet4/15
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet4/16
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
!
          interface GigabitEthernet4/17
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet4/18
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet4/19
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet4/20
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
!
interface GigabitEthernet4/21
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet4/22
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet4/23
 description SHUT FOR COPYRIGHT INFRIG(IM-418509)
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 shutdown
 spanning-tree portfast edge
!
interface GigabitEthernet4/24
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet4/25
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
!
interface GigabitEthernet4/26
 switchport access vlan 365
 switchport mode access
           ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet4/27
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet4/28
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet4/29
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
!
interface GigabitEthernet4/30
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet4/31
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet4/32
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet4/33
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet4/34
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
!
interface GigabitEthernet4/35
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet4/36
           switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet4/37
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
!
interface GigabitEthernet4/38
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet4/39
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
!
interface GigabitEthernet4/40
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet4/41
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet4/42
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
!
interface GigabitEthernet4/43
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet4/44
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet4/45
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
          interface GigabitEthernet4/46
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet4/47
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet4/48
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
!
interface TenGigabitEthernet5/1
 description key:Te5/1:dx1-112mrsc:G1/3
 switchport mode trunk
!
interface TenGigabitEthernet5/2
!
interface TenGigabitEthernet5/3
!
interface TenGigabitEthernet5/4
!
interface GigabitEthernet8/1
 switchport access vlan 1624
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet8/2
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
!
interface GigabitEthernet8/3
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet8/4
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet8/5
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet8/6
           switchport access vlan 520
 switchport mode access
 spanning-tree portfast edge
!
interface GigabitEthernet8/7
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
!
interface GigabitEthernet8/8
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
!
interface GigabitEthernet8/9
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet8/10
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet8/11
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet8/12
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet8/13
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet8/14
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet8/15
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet8/16
           switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet8/17
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet8/18
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet8/19
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet8/20
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
!
interface GigabitEthernet8/21
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet8/22
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet8/23
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet8/24
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet8/25
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
!
          interface GigabitEthernet8/26
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet8/27
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet8/28
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet8/29
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet8/30
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet8/31
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet8/32
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
!
interface GigabitEthernet8/33
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
!
interface GigabitEthernet8/34
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet8/35
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
          !
interface GigabitEthernet8/36
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet8/37
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet8/38
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
!
interface GigabitEthernet8/39
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet8/40
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet8/41
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet8/42
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet8/43
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet8/44
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
!
interface GigabitEthernet8/45
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
           spanning-tree portfast edge
!
interface GigabitEthernet8/46
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet8/47
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet8/48
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet9/1
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet9/2
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet9/3
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet9/4
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet9/5
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet9/6
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet9/7
 switchport access vlan 365
 switchport mode access
           ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet9/8
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet9/9
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet9/10
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet9/11
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
!
interface GigabitEthernet9/12
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
!
interface GigabitEthernet9/13
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet9/14
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet9/15
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet9/16
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
!
interface GigabitEthernet9/17
 description ACCESS POINT
           switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
!
interface GigabitEthernet9/18
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet9/19
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet9/20
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet9/21
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet9/22
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet9/23
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
 spanning-tree portfast edge
!
interface GigabitEthernet9/24
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet9/25
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet9/26
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
           spanning-tree portfast edge
!
interface GigabitEthernet9/27
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet9/28
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet9/29
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet9/30
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet9/31
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet9/32
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet9/33
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet9/34
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet9/35
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet9/36
 switchport access vlan 365
 switchport mode access
           ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet9/37
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet9/38
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet9/39
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet9/40
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet9/41
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet9/42
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet9/43
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet9/44
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet9/45
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet9/46
 switchport access vlan 365
           switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet9/47
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet9/48
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet10/1
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet10/2
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
 spanning-tree portfast edge
!
interface GigabitEthernet10/3
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet10/4
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet10/5
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet10/6
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet10/7
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
!
          interface GigabitEthernet10/8
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet10/9
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet10/10
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
!
interface GigabitEthernet10/11
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet10/12
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet10/13
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet10/14
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet10/15
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet10/16
 switchport access vlan 1133
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet10/17
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
          !
interface GigabitEthernet10/18
 switchport access vlan 1133
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet10/19
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet10/20
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
!
interface GigabitEthernet10/21
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet10/22
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet10/23
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet10/24
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet10/25
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet10/26
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
!
interface GigabitEthernet10/27
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
           spanning-tree portfast edge
!
interface GigabitEthernet10/28
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet10/29
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet10/30
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet10/31
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet10/32
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet10/33
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet10/34
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet10/35
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet10/36
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet10/37
 switchport access vlan 365
 switchport mode access
           ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet10/38
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet10/39
 switchport access vlan 504
 switchport mode access
 switchport voice vlan 202
 spanning-tree portfast edge
!
interface GigabitEthernet10/40
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet10/41
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet10/42
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet10/43
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet10/44
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
!
interface GigabitEthernet10/45
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface GigabitEthernet10/46
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
!
interface GigabitEthernet10/47
 description ACCESS POINT
           switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
!
interface GigabitEthernet10/48
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
!
interface Vlan1
 no ip address
 no ip route-cache
 shutdown
!
interface Vlan874
 description #fort-112mrsc-m  
 ip address 172.31.128.133 255.255.255.128
 no ip route-cache
!
ip default-gateway 172.31.128.129
ip forward-protocol nd
no ip http server
no ip http secure-server
ip tftp blocksize 8192
ip route 0.0.0.0 0.0.0.0 172.31.128.129
ip ssh time-out 30
ip ssh version 2
!
!
logging facility local6
logging source-interface Vlan874
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
!
!
snmp-server engineID local 000000090200000628362780
snmp-server community We5U=#9vahev RW 71
snmp-server community fortNs!$q~5r9 RW 71
snmp-server community fort$NmP! RO 70
snmp-server community 99U#u#U!x RO 70
snmp-server community Pru-7abr9fat RW 71
snmp-server community fa!4epre RW 71
snmp-server community Yx5XdagKRsmD3Oi RO 70
snmp-server contact TAG:310221-BARCODE:xxxxxx
snmp-server enable traps snmp authentication linkdown linkup coldstart
snmp-server enable traps config
snmp-server enable traps syslog
snmp-server host 155.98.253.152 version 2c 99U#u#U!x 
snmp-server host 155.98.253.148 v2c 
snmp-server host 155.98.253.149 v2c 
no snmp mib flash cache
tacacs-server host 155.97.160.52
tacacs-server host 155.98.253.200
tacacs-server key 7 1551212C072178200560203252
tacacs server TAC-DDC
 key 7 041821260C2A1F4A244A100753
tacacs server TAC-PARK
 key 7 064525014F455A1D2844071B4D
tacacs server TAC-EBC
 address ipv4 172.31.17.180
 key 7 11205D003E560E2E24283265
tacacs server TAC-SECONDARY
 address ipv4 10.64.32.5
 key 7 10674D1C2C5317292C06336A
!
!
privilege exec level 1 show configuration
privilege exec level 1 show
banner login ^CC

sx1-112mrsc-2



University of Utah Network: All use of this device must comply

with the University of Utah policies and procedures. Any use of
          
this device, whether deliberate or indeliberate will be held legally

responsible. See the University of Utah Policies and Procedures

1-15 Information Resource Policy for more detail.

(www.admin.utah.edu/ppmanual/1/1-15.html)



Problems within the University of Utah's network should be reported

by calling the Campus Helpdesk at 581-4000, or via e-mail at

helpdesk@utah.edu



                        DO NOT LOGIN

if you are not authorized by NetCom at the University of Utah.



^C
!
line con 0
 exec-timeout 5 0
 password 7 10485118254F511E0F
 stopbits 1
line vty 0 4
 access-class 199 in
 exec-timeout 5 0
 password 7 045A1E421D2019030F
 transport input ssh
line vty 5 15
 access-class 199 in
 exec-timeout 5 0
 password 7 1416074F1E057F6622
 transport input ssh
!
ntp server 155.97.159.10
ntp server time.utah.edu
end
""",
 'show int status':"""Port      Name               Status       Vlan       Duplex  Speed Type 
Gi1/1     ACCESS POINT       connected    479        a-full a-1000 10/100/1000-TX
Gi1/2     ACCESS POINT       connected    479        a-full a-1000 10/100/1000-TX
Gi1/3     ACCESS POINT       connected    479        a-full a-1000 10/100/1000-TX
Gi1/4     ACCESS POINT       connected    479        a-full a-1000 10/100/1000-TX
Gi1/5     ACCESS POINT       connected    479        a-full a-1000 10/100/1000-TX
Gi1/6     ACCESS POINT       connected    479        a-full a-1000 10/100/1000-TX
Gi1/7     ACCESS POINT       connected    479        a-full a-1000 10/100/1000-TX
Gi1/8     ACCESS POINT       connected    479        a-full a-1000 10/100/1000-TX
Gi1/9     ACCESS POINT       connected    479        a-full a-1000 10/100/1000-TX
Gi1/10    ACCESS POINT       connected    479        a-full a-1000 10/100/1000-TX
Gi1/11    ACCESS POINT       connected    479        a-full a-1000 10/100/1000-TX
Gi1/12    ACCESS POINT       connected    479        a-full a-1000 10/100/1000-TX
Gi1/13    ACCESS POINT       connected    479        a-full a-1000 10/100/1000-TX
Gi1/14    ACCESS POINT       connected    479        a-full a-1000 10/100/1000-TX
Gi1/15    ACCESS POINT       connected    479        a-full a-1000 10/100/1000-TX
Gi1/16    ACCESS POINT       connected    479        a-full a-1000 10/100/1000-TX
Gi1/17    ACCESS POINT       connected    479        a-full a-1000 10/100/1000-TX
Gi1/18    ACCESS POINT       connected    479        a-full a-1000 10/100/1000-TX
Gi1/19    ACCESS POINT       connected    479        a-full a-1000 10/100/1000-TX
Gi1/20    ACCESS POINT       connected    479        a-full a-1000 10/100/1000-TX
Gi1/21    ACCESS POINT       connected    479        a-full a-1000 10/100/1000-TX
Gi1/22    ACCESS POINT       connected    479        a-full a-1000 10/100/1000-TX
Gi1/23    ACCESS POINT       connected    479        a-full a-1000 10/100/1000-TX
Gi1/24    ACCESS POINT       connected    479        a-full a-1000 10/100/1000-TX
Gi1/25    ACCESS POINT       connected    trunk      a-full a-1000 10/100/1000-TX
Gi1/26    ACCESS POINT       connected    479        a-full a-1000 10/100/1000-TX
Gi1/27    ACCESS POINT       connected    479        a-full a-1000 10/100/1000-TX
Gi1/28    ACCESS POINT       connected    479        a-full a-1000 10/100/1000-TX
Gi1/29    ACCESS POINT       connected    479        a-full a-1000 10/100/1000-TX
Gi1/30    ACCESS POINT       connected    479        a-full a-1000 10/100/1000-TX
Gi1/31    ACCESS POINT       connected    479        a-full a-1000 10/100/1000-TX
Gi1/32    ACCESS POINT       connected    479        a-full a-1000 10/100/1000-TX
Gi1/33    ACCESS POINT       connected    479        a-full a-1000 10/100/1000-TX
Gi1/34    ACCESS POINT       connected    479        a-full a-1000 10/100/1000-TX
Gi1/35    ACCESS POINT       connected    479        a-full a-1000 10/100/1000-TX
Gi1/36    ACCESS POINT       connected    479        a-full a-1000 10/100/1000-TX
Gi1/37    ACCESS POINT       connected    479        a-full a-1000 10/100/1000-TX
Gi1/38    ACCESS POINT       connected    trunk      a-full a-1000 10/100/1000-TX
Gi1/39    ACCESS POINT       connected    479        a-full a-1000 10/100/1000-TX
Gi1/40                       notconnect   365          auto   auto 10/100/1000-TX
Gi1/41                       connected    170        a-full  a-100 10/100/1000-TX
Gi1/42                       notconnect   365          auto   auto 10/100/1000-TX
Gi1/43    red-print-kiosk    connected    460        a-full a-1000 10/100/1000-TX
Gi1/44                       notconnect   601          auto   auto 10/100/1000-TX
Gi1/45                       notconnect   601          auto   auto 10/100/1000-TX
Gi1/46                       connected    601        a-full  a-100 10/100/1000-TX
Gi1/47                       connected    601        a-full  a-100 10/100/1000-TX
Gi1/48                       connected    611        a-half   a-10 10/100/1000-TX
Gi2/1                        connected    170        a-full a-1000 10/100/1000-TX
Gi2/2                        connected    170        a-full a-1000 10/100/1000-TX
Gi2/3                        connected    170        a-full a-1000 10/100/1000-TX
Gi2/4                        connected    170        a-full a-1000 10/100/1000-TX
Gi2/5                        connected    170        a-full a-1000 10/100/1000-TX
Gi2/6                        notconnect   170          auto   auto 10/100/1000-TX
Gi2/7     ACCESS POINT       connected    479        a-full a-1000 10/100/1000-TX
Gi2/8                        connected    170        a-full a-1000 10/100/1000-TX
Gi2/9                        notconnect   170          auto   auto 10/100/1000-TX
          
Port      Name               Status       Vlan       Duplex  Speed Type 
Gi2/10                       notconnect   170          auto   auto 10/100/1000-TX
Gi2/11                       notconnect   170          auto   auto 10/100/1000-TX
Gi2/12    ACCESS POINT       connected    479        a-full a-1000 10/100/1000-TX
Gi2/13                       connected    170        a-full a-1000 10/100/1000-TX
Gi2/14                       notconnect   170          auto   auto 10/100/1000-TX
Gi2/15                       connected    1103       a-full  a-100 10/100/1000-TX
Gi2/16                       connected    504        a-full a-1000 10/100/1000-TX
Gi2/17    ACCESS POINT       connected    trunk      a-full a-1000 10/100/1000-TX
Gi2/18    ACCESS POINT       connected    trunk      a-full a-1000 10/100/1000-TX
Gi2/19    ACCESS POINT       connected    trunk      a-full a-1000 10/100/1000-TX
Gi2/20    ACCESS POINT       connected    trunk      a-full a-1000 10/100/1000-TX
Gi2/21                       notconnect   505          auto   auto 10/100/1000-TX
Gi2/22                       notconnect   365          auto   auto 10/100/1000-TX
Gi2/23                       connected    170        a-full a-1000 10/100/1000-TX
Gi2/24                       connected    646        a-full a-1000 10/100/1000-TX
Gi2/25                       notconnect   504          auto   auto 10/100/1000-TX
Gi2/26                       notconnect   504          auto   auto 10/100/1000-TX
Gi2/27    ACCESS POINT       connected    trunk      a-full a-1000 10/100/1000-TX
Gi2/28                       notconnect   504          auto   auto 10/100/1000-TX
Gi2/29                       connected    504        a-full a-1000 10/100/1000-TX
Gi2/30    ACCESS POINT       connected    trunk      a-full a-1000 10/100/1000-TX
Gi2/31    CAM                connected    1624       a-full  a-100 10/100/1000-TX
Gi2/32    ACCESS POINT       connected    trunk      a-full a-1000 10/100/1000-TX
Gi2/33    CAM                connected    1624       a-full  a-100 10/100/1000-TX
Gi2/34    CAM                connected    1624       a-full  a-100 10/100/1000-TX
Gi2/35    ACCESS POINT       connected    479        a-full a-1000 10/100/1000-TX
Gi2/36                       notconnect   365          auto   auto 10/100/1000-TX
Gi2/37    ACCESS POINT       connected    479        a-full a-1000 10/100/1000-TX
Gi2/38                       notconnect   365          auto   auto 10/100/1000-TX
Gi2/39                       notconnect   505          auto   auto 10/100/1000-TX
Gi2/40                       notconnect   505          auto   auto 10/100/1000-TX
Gi2/41    ACCESS POINT       connected    479        a-full a-1000 10/100/1000-TX
Gi2/42                       notconnect   365          auto   auto 10/100/1000-TX
Gi2/43    ACCESS POINT       connected    479        a-full a-1000 10/100/1000-TX
Gi2/44                       notconnect   365          auto   auto 10/100/1000-TX
Gi2/45                       notconnect   365          auto   auto 10/100/1000-TX
Gi2/46    ACCESS POINT       connected    trunk      a-full a-1000 10/100/1000-TX
Gi2/47                       notconnect   365          auto   auto 10/100/1000-TX
Gi2/48                       notconnect   365          auto   auto 10/100/1000-TX
Gi3/1                        connected    365        a-full  a-100 10/100/1000-TX
Gi3/2     ACCESS POINT       connected    trunk      a-full a-1000 10/100/1000-TX
Gi3/3                        notconnect   365          auto   auto 10/100/1000-TX
Gi3/4                        notconnect   365          auto   auto 10/100/1000-TX
Gi3/5                        notconnect   365          auto   auto 10/100/1000-TX
Gi3/6     ACCESS POINT       connected    trunk      a-full a-1000 10/100/1000-TX
Gi3/7                        notconnect   365          auto   auto 10/100/1000-TX
Gi3/8                        notconnect   365          auto   auto 10/100/1000-TX
Gi3/9                        notconnect   365          auto   auto 10/100/1000-TX
Gi3/10                       notconnect   365          auto   auto 10/100/1000-TX
Gi3/11                       notconnect   365          auto   auto 10/100/1000-TX
Gi3/12                       notconnect   365          auto   auto 10/100/1000-TX
Gi3/13                       notconnect   365          auto   auto 10/100/1000-TX
Gi3/14    ACCESS POINT       connected    trunk      a-full a-1000 10/100/1000-TX
Gi3/15                       notconnect   365          auto   auto 10/100/1000-TX
Gi3/16                       notconnect   170          auto   auto 10/100/1000-TX
Gi3/17                       notconnect   365          auto   auto 10/100/1000-TX
Gi3/18                       notconnect   365          auto   auto 10/100/1000-TX
Gi3/19                       notconnect   365          auto   auto 10/100/1000-TX
Gi3/20                       notconnect   365          auto   auto 10/100/1000-TX
          
Port      Name               Status       Vlan       Duplex  Speed Type 
Gi3/21                       connected    170        a-full a-1000 10/100/1000-TX
Gi3/22                       notconnect   365          auto   auto 10/100/1000-TX
Gi3/23    ACCESS POINT       connected    trunk      a-full a-1000 10/100/1000-TX
Gi3/24                       notconnect   365          auto   auto 10/100/1000-TX
Gi3/25                       notconnect   365          auto   auto 10/100/1000-TX
Gi3/26                       notconnect   365          auto   auto 10/100/1000-TX
Gi3/27                       connected    520        a-full  a-100 10/100/1000-TX
Gi3/28                       connected    520        a-full  a-100 10/100/1000-TX
Gi3/29                       notconnect   365          auto   auto 10/100/1000-TX
Gi3/30                       notconnect   365          auto   auto 10/100/1000-TX
Gi3/31                       notconnect   365          auto   auto 10/100/1000-TX
Gi3/32                       notconnect   365          auto   auto 10/100/1000-TX
Gi3/33                       notconnect   365          auto   auto 10/100/1000-TX
Gi3/34                       notconnect   365          auto   auto 10/100/1000-TX
Gi3/35                       notconnect   365          auto   auto 10/100/1000-TX
Gi3/36                       notconnect   365          auto   auto 10/100/1000-TX
Gi3/37                       notconnect   365          auto   auto 10/100/1000-TX
Gi3/38                       notconnect   365          auto   auto 10/100/1000-TX
Gi3/39                       notconnect   365          auto   auto 10/100/1000-TX
Gi3/40                       notconnect   365          auto   auto 10/100/1000-TX
Gi3/41                       notconnect   365          auto   auto 10/100/1000-TX
Gi3/42                       notconnect   365          auto   auto 10/100/1000-TX
Gi3/43                       connected    365        a-full a-1000 10/100/1000-TX
Gi3/44                       notconnect   365          auto   auto 10/100/1000-TX
Gi3/45                       notconnect   365          auto   auto 10/100/1000-TX
Gi3/46                       notconnect   365          auto   auto 10/100/1000-TX
Gi3/47                       notconnect   365          auto   auto 10/100/1000-TX
Gi3/48                       notconnect   365          auto   auto 10/100/1000-TX
Gi4/1                        notconnect   365          auto   auto 10/100/1000-TX
Gi4/2     ACCESS POINT       connected    trunk      a-full a-1000 10/100/1000-TX
Gi4/3                        notconnect   365          auto   auto 10/100/1000-TX
Gi4/4     ACCESS POINT       connected    trunk      a-full a-1000 10/100/1000-TX
Gi4/5                        notconnect   365          auto   auto 10/100/1000-TX
Gi4/6                        notconnect   365          auto   auto 10/100/1000-TX
Gi4/7                        notconnect   365          auto   auto 10/100/1000-TX
Gi4/8                        notconnect   365          auto   auto 10/100/1000-TX
Gi4/9                        notconnect   365          auto   auto 10/100/1000-TX
Gi4/10    ACCESS POINT       connected    trunk      a-full a-1000 10/100/1000-TX
Gi4/11                       notconnect   365          auto   auto 10/100/1000-TX
Gi4/12                       notconnect   365          auto   auto 10/100/1000-TX
Gi4/13                       notconnect   365          auto   auto 10/100/1000-TX
Gi4/14                       notconnect   365          auto   auto 10/100/1000-TX
Gi4/15    ACCESS POINT       connected    trunk      a-full a-1000 10/100/1000-TX
Gi4/16    ACCESS POINT       connected    trunk      a-full a-1000 10/100/1000-TX
Gi4/17                       notconnect   365          auto   auto 10/100/1000-TX
Gi4/18                       notconnect   365          auto   auto 10/100/1000-TX
Gi4/19                       notconnect   365          auto   auto 10/100/1000-TX
Gi4/20    ACCESS POINT       connected    trunk      a-full a-1000 10/100/1000-TX
Gi4/21                       notconnect   365          auto   auto 10/100/1000-TX
Gi4/22                       notconnect   365          auto   auto 10/100/1000-TX
Gi4/23    SHUT FOR COPYRIGHT disabled     365          auto   auto 10/100/1000-TX
Gi4/24                       notconnect   365          auto   auto 10/100/1000-TX
Gi4/25    ACCESS POINT       connected    trunk      a-full a-1000 10/100/1000-TX
Gi4/26                       notconnect   365          auto   auto 10/100/1000-TX
Gi4/27                       notconnect   365          auto   auto 10/100/1000-TX
Gi4/28    ACCESS POINT       notconnect   479          auto   auto 10/100/1000-TX
Gi4/29    ACCESS POINT       connected    trunk      a-full a-1000 10/100/1000-TX
Gi4/30                       notconnect   365          auto   auto 10/100/1000-TX
Gi4/31                       notconnect   365          auto   auto 10/100/1000-TX
          
Port      Name               Status       Vlan       Duplex  Speed Type 
Gi4/32                       notconnect   365          auto   auto 10/100/1000-TX
Gi4/33                       notconnect   365          auto   auto 10/100/1000-TX
Gi4/34    ACCESS POINT       connected    trunk      a-full a-1000 10/100/1000-TX
Gi4/35                       notconnect   365          auto   auto 10/100/1000-TX
Gi4/36                       notconnect   365          auto   auto 10/100/1000-TX
Gi4/37    ACCESS POINT       connected    trunk      a-full a-1000 10/100/1000-TX
Gi4/38                       notconnect   365          auto   auto 10/100/1000-TX
Gi4/39    ACCESS POINT       connected    trunk      a-full a-1000 10/100/1000-TX
Gi4/40                       notconnect   365          auto   auto 10/100/1000-TX
Gi4/41                       notconnect   365          auto   auto 10/100/1000-TX
Gi4/42    ACCESS POINT       connected    trunk      a-full a-1000 10/100/1000-TX
Gi4/43                       notconnect   365          auto   auto 10/100/1000-TX
Gi4/44                       notconnect   365          auto   auto 10/100/1000-TX
Gi4/45                       notconnect   365          auto   auto 10/100/1000-TX
Gi4/46    ACCESS POINT       connected    trunk      a-full a-1000 10/100/1000-TX
Gi4/47                       notconnect   365          auto   auto 10/100/1000-TX
Gi4/48    ACCESS POINT       connected    trunk      a-full a-1000 10/100/1000-TX
Te5/1     key:Te5/1:dx1-112m connected    trunk        full a-1000 1000BaseSX
Te5/2                        notconnect   1            full   auto No XCVR
Te5/3                        notconnect   1            full   auto No XCVR
Te5/4                        notconnect   1            full   auto No XCVR
Gi8/1                        connected    1624       a-full  a-100 10/100/1000-TX
Gi8/2     ACCESS POINT       notconnect   479          auto   auto 10/100/1000-TX
Gi8/3                        notconnect   365          auto   auto 10/100/1000-TX
Gi8/4                        notconnect   365          auto   auto 10/100/1000-TX
Gi8/5                        notconnect   365          auto   auto 10/100/1000-TX
Gi8/6                        connected    520        a-full  a-100 10/100/1000-TX
Gi8/7     ACCESS POINT       connected    trunk      a-full a-1000 10/100/1000-TX
Gi8/8     ACCESS POINT       connected    trunk      a-full a-1000 10/100/1000-TX
Gi8/9                        notconnect   365          auto   auto 10/100/1000-TX
Gi8/10                       notconnect   365          auto   auto 10/100/1000-TX
Gi8/11                       notconnect   365          auto   auto 10/100/1000-TX
Gi8/12                       notconnect   365          auto   auto 10/100/1000-TX
Gi8/13                       notconnect   365          auto   auto 10/100/1000-TX
Gi8/14                       notconnect   365          auto   auto 10/100/1000-TX
Gi8/15                       notconnect   365          auto   auto 10/100/1000-TX
Gi8/16                       notconnect   365          auto   auto 10/100/1000-TX
Gi8/17                       notconnect   365          auto   auto 10/100/1000-TX
Gi8/18                       notconnect   365          auto   auto 10/100/1000-TX
Gi8/19                       notconnect   365          auto   auto 10/100/1000-TX
Gi8/20    ACCESS POINT       connected    trunk      a-full a-1000 10/100/1000-TX
Gi8/21                       notconnect   365          auto   auto 10/100/1000-TX
Gi8/22                       notconnect   365          auto   auto 10/100/1000-TX
Gi8/23                       notconnect   365          auto   auto 10/100/1000-TX
Gi8/24                       notconnect   365          auto   auto 10/100/1000-TX
Gi8/25    ACCESS POINT       connected    trunk      a-full a-1000 10/100/1000-TX
Gi8/26                       notconnect   365          auto   auto 10/100/1000-TX
Gi8/27                       notconnect   365          auto   auto 10/100/1000-TX
Gi8/28                       notconnect   365          auto   auto 10/100/1000-TX
Gi8/29                       notconnect   365          auto   auto 10/100/1000-TX
Gi8/30                       notconnect   365          auto   auto 10/100/1000-TX
Gi8/31                       notconnect   365          auto   auto 10/100/1000-TX
Gi8/32    ACCESS POINT       connected    trunk      a-full a-1000 10/100/1000-TX
Gi8/33    ACCESS POINT       connected    trunk      a-full a-1000 10/100/1000-TX
Gi8/34                       notconnect   365          auto   auto 10/100/1000-TX
Gi8/35                       notconnect   365          auto   auto 10/100/1000-TX
Gi8/36                       notconnect   365          auto   auto 10/100/1000-TX
Gi8/37                       notconnect   365          auto   auto 10/100/1000-TX
Gi8/38    ACCESS POINT       connected    trunk      a-full a-1000 10/100/1000-TX
          
Port      Name               Status       Vlan       Duplex  Speed Type 
Gi8/39                       notconnect   365          auto   auto 10/100/1000-TX
Gi8/40                       notconnect   365          auto   auto 10/100/1000-TX
Gi8/41                       notconnect   365          auto   auto 10/100/1000-TX
Gi8/42                       notconnect   365          auto   auto 10/100/1000-TX
Gi8/43                       notconnect   365          auto   auto 10/100/1000-TX
Gi8/44    ACCESS POINT       connected    trunk      a-full a-1000 10/100/1000-TX
Gi8/45                       notconnect   365          auto   auto 10/100/1000-TX
Gi8/46                       notconnect   365          auto   auto 10/100/1000-TX
Gi8/47                       notconnect   365          auto   auto 10/100/1000-TX
Gi8/48                       notconnect   365          auto   auto 10/100/1000-TX
Gi9/1                        notconnect   365          auto   auto 10/100/1000-TX
Gi9/2                        notconnect   365          auto   auto 10/100/1000-TX
Gi9/3                        connected    365        a-full a-1000 10/100/1000-TX
Gi9/4                        notconnect   365          auto   auto 10/100/1000-TX
Gi9/5                        notconnect   365          auto   auto 10/100/1000-TX
Gi9/6                        notconnect   365          auto   auto 10/100/1000-TX
Gi9/7                        notconnect   365          auto   auto 10/100/1000-TX
Gi9/8                        notconnect   365          auto   auto 10/100/1000-TX
Gi9/9                        notconnect   365          auto   auto 10/100/1000-TX
Gi9/10                       notconnect   365          auto   auto 10/100/1000-TX
Gi9/11    ACCESS POINT       connected    trunk      a-full a-1000 10/100/1000-TX
Gi9/12    ACCESS POINT       connected    trunk      a-full a-1000 10/100/1000-TX
Gi9/13                       notconnect   365          auto   auto 10/100/1000-TX
Gi9/14                       notconnect   365          auto   auto 10/100/1000-TX
Gi9/15                       notconnect   365          auto   auto 10/100/1000-TX
Gi9/16    ACCESS POINT       connected    trunk      a-full a-1000 10/100/1000-TX
Gi9/17    ACCESS POINT       connected    trunk      a-full a-1000 10/100/1000-TX
Gi9/18                       notconnect   365          auto   auto 10/100/1000-TX
Gi9/19                       notconnect   365          auto   auto 10/100/1000-TX
Gi9/20                       notconnect   365          auto   auto 10/100/1000-TX
Gi9/21                       notconnect   365          auto   auto 10/100/1000-TX
Gi9/22    ACCESS POINT       connected    trunk      a-full a-1000 10/100/1000-TX
Gi9/23    ACCESS POINT       connected    trunk      a-full a-1000 10/100/1000-TX
Gi9/24                       notconnect   365          auto   auto 10/100/1000-TX
Gi9/25                       notconnect   365          auto   auto 10/100/1000-TX
Gi9/26                       notconnect   365          auto   auto 10/100/1000-TX
Gi9/27                       notconnect   365          auto   auto 10/100/1000-TX
Gi9/28                       notconnect   365          auto   auto 10/100/1000-TX
Gi9/29                       notconnect   365          auto   auto 10/100/1000-TX
Gi9/30                       notconnect   365          auto   auto 10/100/1000-TX
Gi9/31                       notconnect   365          auto   auto 10/100/1000-TX
Gi9/32                       notconnect   365          auto   auto 10/100/1000-TX
Gi9/33                       connected    365        a-full a-1000 10/100/1000-TX
Gi9/34                       notconnect   365          auto   auto 10/100/1000-TX
Gi9/35                       notconnect   365          auto   auto 10/100/1000-TX
Gi9/36                       notconnect   365          auto   auto 10/100/1000-TX
Gi9/37                       notconnect   365          auto   auto 10/100/1000-TX
Gi9/38                       notconnect   365          auto   auto 10/100/1000-TX
Gi9/39                       notconnect   365          auto   auto 10/100/1000-TX
Gi9/40                       connected    365        a-full a-1000 10/100/1000-TX
Gi9/41                       notconnect   365          auto   auto 10/100/1000-TX
Gi9/42                       notconnect   365          auto   auto 10/100/1000-TX
Gi9/43                       notconnect   365          auto   auto 10/100/1000-TX
Gi9/44                       notconnect   365          auto   auto 10/100/1000-TX
Gi9/45                       notconnect   365          auto   auto 10/100/1000-TX
Gi9/46                       notconnect   365          auto   auto 10/100/1000-TX
Gi9/47                       notconnect   365          auto   auto 10/100/1000-TX
Gi9/48                       notconnect   365          auto   auto 10/100/1000-TX
Gi10/1                       notconnect   365          auto   auto 10/100/1000-TX
          
Port      Name               Status       Vlan       Duplex  Speed Type 
Gi10/2    ACCESS POINT       connected    trunk      a-full a-1000 10/100/1000-TX
Gi10/3                       notconnect   365          auto   auto 10/100/1000-TX
Gi10/4                       notconnect   365          auto   auto 10/100/1000-TX
Gi10/5                       notconnect   365          auto   auto 10/100/1000-TX
Gi10/6                       notconnect   365          auto   auto 10/100/1000-TX
Gi10/7    ACCESS POINT       connected    trunk      a-full a-1000 10/100/1000-TX
Gi10/8                       notconnect   365          auto   auto 10/100/1000-TX
Gi10/9                       notconnect   365          auto   auto 10/100/1000-TX
Gi10/10   ACCESS POINT       connected    trunk      a-full a-1000 10/100/1000-TX
Gi10/11                      notconnect   365          auto   auto 10/100/1000-TX
Gi10/12                      notconnect   365          auto   auto 10/100/1000-TX
Gi10/13                      notconnect   365          auto   auto 10/100/1000-TX
Gi10/14                      notconnect   365          auto   auto 10/100/1000-TX
Gi10/15                      notconnect   365          auto   auto 10/100/1000-TX
Gi10/16                      notconnect   1133         auto   auto 10/100/1000-TX
Gi10/17                      notconnect   365          auto   auto 10/100/1000-TX
Gi10/18                      notconnect   1133         auto   auto 10/100/1000-TX
Gi10/19                      notconnect   365          auto   auto 10/100/1000-TX
Gi10/20   ACCESS POINT       connected    trunk      a-full a-1000 10/100/1000-TX
Gi10/21                      notconnect   365          auto   auto 10/100/1000-TX
Gi10/22                      notconnect   365          auto   auto 10/100/1000-TX
Gi10/23                      notconnect   365          auto   auto 10/100/1000-TX
Gi10/24                      notconnect   365          auto   auto 10/100/1000-TX
Gi10/25                      notconnect   365          auto   auto 10/100/1000-TX
Gi10/26   ACCESS POINT       connected    trunk      a-full a-1000 10/100/1000-TX
Gi10/27                      notconnect   365          auto   auto 10/100/1000-TX
Gi10/28                      notconnect   365          auto   auto 10/100/1000-TX
Gi10/29                      notconnect   365          auto   auto 10/100/1000-TX
Gi10/30                      notconnect   365          auto   auto 10/100/1000-TX
Gi10/31                      notconnect   365          auto   auto 10/100/1000-TX
Gi10/32                      notconnect   365          auto   auto 10/100/1000-TX
Gi10/33                      notconnect   365          auto   auto 10/100/1000-TX
Gi10/34                      notconnect   365          auto   auto 10/100/1000-TX
Gi10/35                      notconnect   365          auto   auto 10/100/1000-TX
Gi10/36                      notconnect   365          auto   auto 10/100/1000-TX
Gi10/37                      notconnect   365          auto   auto 10/100/1000-TX
Gi10/38                      notconnect   365          auto   auto 10/100/1000-TX
Gi10/39                      connected    504        a-full a-1000 10/100/1000-TX
Gi10/40                      notconnect   365          auto   auto 10/100/1000-TX
Gi10/41                      notconnect   365          auto   auto 10/100/1000-TX
Gi10/42                      notconnect   365          auto   auto 10/100/1000-TX
Gi10/43                      notconnect   365          auto   auto 10/100/1000-TX
Gi10/44   ACCESS POINT       connected    trunk      a-full a-1000 10/100/1000-TX
Gi10/45                      notconnect   365          auto   auto 10/100/1000-TX
Gi10/46   ACCESS POINT       connected    trunk      a-full a-1000 10/100/1000-TX
Gi10/47   ACCESS POINT       connected    trunk      a-full a-1000 10/100/1000-TX
Gi10/48                      notconnect   365          auto   auto 10/100/1000-TX""",
 'show run | section interface':"""interface FastEthernet1
 vrf forwarding mgmtVrf
 no ip address
 shutdown
 speed auto
 duplex auto
interface GigabitEthernet1/1
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet1/2
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet1/3
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet1/4
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet1/5
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet1/6
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet1/7
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet1/8
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet1/9
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet1/10
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet1/11
 description ACCESS POINT
 switchport access vlan 479
           switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet1/12
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet1/13
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet1/14
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet1/15
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet1/16
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet1/17
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet1/18
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet1/19
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet1/20
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet1/21
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet1/22
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet1/23
 description ACCESS POINT
           switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet1/24
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet1/25
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
 spanning-tree portfast edge
interface GigabitEthernet1/26
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet1/27
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet1/28
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet1/29
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet1/30
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet1/31
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet1/32
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet1/33
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet1/34
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
          interface GigabitEthernet1/35
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet1/36
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet1/37
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet1/38
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
 spanning-tree portfast edge
interface GigabitEthernet1/39
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet1/40
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet1/41
 switchport access vlan 170
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet1/42
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet1/43
 description red-print-kiosk
 switchport access vlan 460
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet1/44
 switchport access vlan 601
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet1/45
 switchport access vlan 601
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet1/46
 switchport access vlan 601
 switchport mode access
 spanning-tree portfast edge
          interface GigabitEthernet1/47
 switchport access vlan 601
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet1/48
 switchport access vlan 611
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet2/1
 switchport access vlan 170
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet2/2
 switchport access vlan 170
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet2/3
 switchport access vlan 170
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet2/4
 switchport access vlan 170
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet2/5
 switchport access vlan 170
 switchport mode access
 switchport voice vlan 202
 spanning-tree portfast edge
interface GigabitEthernet2/6
 switchport access vlan 170
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet2/7
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet2/8
 switchport access vlan 170
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet2/9
 switchport access vlan 170
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet2/10
 switchport access vlan 170
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet2/11
 switchport access vlan 170
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet2/12
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
interface GigabitEthernet2/13
           switchport access vlan 170
 switchport mode access
 switchport voice vlan 202
 spanning-tree portfast edge
interface GigabitEthernet2/14
 switchport access vlan 170
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet2/15
 switchport access vlan 1103
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet2/16
 switchport access vlan 504
 switchport mode access
 switchport voice vlan 202
 spanning-tree portfast edge
interface GigabitEthernet2/17
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
interface GigabitEthernet2/18
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
interface GigabitEthernet2/19
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
 spanning-tree portfast edge
interface GigabitEthernet2/20
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
interface GigabitEthernet2/21
 switchport access vlan 505
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet2/22
 switchport access vlan 365
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet2/23
 switchport access vlan 170
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet2/24
 switchport access vlan 646
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet2/25
 switchport access vlan 504
 switchport mode access
 switchport voice vlan 202
 spanning-tree portfast edge
          interface GigabitEthernet2/26
 switchport access vlan 504
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet2/27
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
interface GigabitEthernet2/28
 switchport access vlan 504
 switchport mode access
 switchport voice vlan 202
 spanning-tree portfast edge
interface GigabitEthernet2/29
 switchport access vlan 504
 switchport mode access
 switchport voice vlan 202
 spanning-tree portfast edge
interface GigabitEthernet2/30
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
interface GigabitEthernet2/31
 description CAM
 switchport access vlan 1624
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet2/32
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
interface GigabitEthernet2/33
 description CAM
 switchport access vlan 1624
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet2/34
 description CAM
 switchport access vlan 1624
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet2/35
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet2/36
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet2/37
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
           ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet2/38
 switchport access vlan 365
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet2/39
 switchport access vlan 505
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet2/40
 switchport access vlan 505
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet2/41
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
interface GigabitEthernet2/42
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet2/43
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet2/44
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet2/45
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet2/46
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet2/47
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet2/48
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet3/1
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
           spanning-tree portfast edge
interface GigabitEthernet3/2
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
interface GigabitEthernet3/3
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet3/4
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet3/5
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet3/6
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
interface GigabitEthernet3/7
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet3/8
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet3/9
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet3/10
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet3/11
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet3/12
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet3/13
 switchport access vlan 365
 switchport mode access
           ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet3/14
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
interface GigabitEthernet3/15
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet3/16
 switchport access vlan 170
 switchport mode access
 switchport voice vlan 202
 spanning-tree portfast edge
interface GigabitEthernet3/17
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet3/18
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet3/19
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet3/20
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet3/21
 switchport access vlan 170
 switchport mode access
 switchport voice vlan 202
 spanning-tree portfast edge
interface GigabitEthernet3/22
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet3/23
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
interface GigabitEthernet3/24
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet3/25
 switchport access vlan 365
           switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet3/26
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet3/27
 switchport access vlan 520
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet3/28
 switchport access vlan 520
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet3/29
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet3/30
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet3/31
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet3/32
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet3/33
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet3/34
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet3/35
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet3/36
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet3/37
 switchport access vlan 365
 switchport mode access
           ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet3/38
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet3/39
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet3/40
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet3/41
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet3/42
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet3/43
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet3/44
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet3/45
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet3/46
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet3/47
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet3/48
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet4/1
 switchport access vlan 365
           switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet4/2
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet4/3
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet4/4
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet4/5
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet4/6
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet4/7
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet4/8
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet4/9
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet4/10
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
interface GigabitEthernet4/11
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet4/12
 switchport access vlan 365
           switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet4/13
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet4/14
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet4/15
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet4/16
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
interface GigabitEthernet4/17
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet4/18
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet4/19
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet4/20
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
interface GigabitEthernet4/21
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet4/22
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet4/23
 description SHUT FOR COPYRIGHT INFRIG(IM-418509)
 switchport access vlan 365
 switchport mode access
           ip access-group 101 in
 shutdown
 spanning-tree portfast edge
interface GigabitEthernet4/24
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet4/25
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
interface GigabitEthernet4/26
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet4/27
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet4/28
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet4/29
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
interface GigabitEthernet4/30
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet4/31
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet4/32
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet4/33
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet4/34
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
          interface GigabitEthernet4/35
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet4/36
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet4/37
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
interface GigabitEthernet4/38
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet4/39
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
interface GigabitEthernet4/40
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet4/41
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet4/42
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
interface GigabitEthernet4/43
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet4/44
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet4/45
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet4/46
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
           switchport mode trunk
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet4/47
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet4/48
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
interface TenGigabitEthernet5/1
 description key:Te5/1:dx1-112mrsc:G1/3
 switchport mode trunk
interface TenGigabitEthernet5/2
interface TenGigabitEthernet5/3
interface TenGigabitEthernet5/4
interface GigabitEthernet8/1
 switchport access vlan 1624
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet8/2
 description ACCESS POINT
 switchport access vlan 479
 switchport mode access
interface GigabitEthernet8/3
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet8/4
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet8/5
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet8/6
 switchport access vlan 520
 switchport mode access
 spanning-tree portfast edge
interface GigabitEthernet8/7
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
interface GigabitEthernet8/8
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
interface GigabitEthernet8/9
 switchport access vlan 365
 switchport mode access
           ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet8/10
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet8/11
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet8/12
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet8/13
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet8/14
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet8/15
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet8/16
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet8/17
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet8/18
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet8/19
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet8/20
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
interface GigabitEthernet8/21
 switchport access vlan 365
           switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet8/22
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet8/23
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet8/24
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet8/25
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
interface GigabitEthernet8/26
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet8/27
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet8/28
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet8/29
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet8/30
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet8/31
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet8/32
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
interface GigabitEthernet8/33
           description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
interface GigabitEthernet8/34
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet8/35
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet8/36
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet8/37
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet8/38
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
interface GigabitEthernet8/39
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet8/40
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet8/41
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet8/42
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet8/43
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet8/44
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
          interface GigabitEthernet8/45
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet8/46
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet8/47
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet8/48
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet9/1
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet9/2
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet9/3
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet9/4
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet9/5
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet9/6
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet9/7
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet9/8
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
           spanning-tree portfast edge
interface GigabitEthernet9/9
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet9/10
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet9/11
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
interface GigabitEthernet9/12
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
interface GigabitEthernet9/13
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet9/14
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet9/15
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet9/16
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
interface GigabitEthernet9/17
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
interface GigabitEthernet9/18
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet9/19
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet9/20
 switchport access vlan 365
 switchport mode access
           ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet9/21
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet9/22
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet9/23
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
 spanning-tree portfast edge
interface GigabitEthernet9/24
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet9/25
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet9/26
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet9/27
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet9/28
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet9/29
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet9/30
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet9/31
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
           spanning-tree portfast edge
interface GigabitEthernet9/32
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet9/33
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet9/34
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet9/35
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet9/36
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet9/37
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet9/38
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet9/39
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet9/40
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet9/41
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet9/42
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet9/43
 switchport access vlan 365
 switchport mode access
           ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet9/44
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet9/45
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet9/46
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet9/47
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet9/48
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet10/1
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet10/2
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
 spanning-tree portfast edge
interface GigabitEthernet10/3
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet10/4
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet10/5
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet10/6
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet10/7
           description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
interface GigabitEthernet10/8
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet10/9
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet10/10
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
interface GigabitEthernet10/11
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet10/12
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet10/13
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet10/14
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet10/15
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet10/16
 switchport access vlan 1133
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet10/17
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet10/18
 switchport access vlan 1133
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
          interface GigabitEthernet10/19
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet10/20
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
interface GigabitEthernet10/21
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet10/22
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet10/23
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet10/24
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet10/25
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet10/26
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
interface GigabitEthernet10/27
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet10/28
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet10/29
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet10/30
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
           spanning-tree portfast edge
interface GigabitEthernet10/31
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet10/32
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet10/33
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet10/34
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet10/35
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet10/36
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet10/37
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet10/38
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet10/39
 switchport access vlan 504
 switchport mode access
 switchport voice vlan 202
 spanning-tree portfast edge
interface GigabitEthernet10/40
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet10/41
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet10/42
 switchport access vlan 365
 switchport mode access
           ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet10/43
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet10/44
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
interface GigabitEthernet10/45
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface GigabitEthernet10/46
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
interface GigabitEthernet10/47
 description ACCESS POINT
 switchport trunk allowed vlan 365,479
 switchport trunk native vlan 479
 switchport mode trunk
interface GigabitEthernet10/48
 switchport access vlan 365
 switchport mode access
 ip access-group 101 in
 spanning-tree portfast edge
interface Vlan1
 no ip address
 no ip route-cache
 shutdown
interface Vlan874
 description #fort-112mrsc-m  
 ip address 172.31.128.133 255.255.255.128
 no ip route-cache
logging source-interface Vlan874""",
 'show run | in interface':"""interface FastEthernet1
interface GigabitEthernet1/1
interface GigabitEthernet1/2
interface GigabitEthernet1/3
interface GigabitEthernet1/4
interface GigabitEthernet1/5
interface GigabitEthernet1/6
interface GigabitEthernet1/7
interface GigabitEthernet1/8
interface GigabitEthernet1/9
interface GigabitEthernet1/10
interface GigabitEthernet1/11
interface GigabitEthernet1/12
interface GigabitEthernet1/13
interface GigabitEthernet1/14
interface GigabitEthernet1/15
interface GigabitEthernet1/16
interface GigabitEthernet1/17
interface GigabitEthernet1/18
interface GigabitEthernet1/19
interface GigabitEthernet1/20
interface GigabitEthernet1/21
interface GigabitEthernet1/22
interface GigabitEthernet1/23
interface GigabitEthernet1/24
interface GigabitEthernet1/25
interface GigabitEthernet1/26
interface GigabitEthernet1/27
interface GigabitEthernet1/28
interface GigabitEthernet1/29
interface GigabitEthernet1/30
interface GigabitEthernet1/31
interface GigabitEthernet1/32
interface GigabitEthernet1/33
interface GigabitEthernet1/34
interface GigabitEthernet1/35
interface GigabitEthernet1/36
interface GigabitEthernet1/37
interface GigabitEthernet1/38
interface GigabitEthernet1/39
interface GigabitEthernet1/40
interface GigabitEthernet1/41
interface GigabitEthernet1/42
interface GigabitEthernet1/43
interface GigabitEthernet1/44
interface GigabitEthernet1/45
interface GigabitEthernet1/46
interface GigabitEthernet1/47
interface GigabitEthernet1/48
interface GigabitEthernet2/1
interface GigabitEthernet2/2
interface GigabitEthernet2/3
interface GigabitEthernet2/4
interface GigabitEthernet2/5
interface GigabitEthernet2/6
interface GigabitEthernet2/7
interface GigabitEthernet2/8
interface GigabitEthernet2/9
interface GigabitEthernet2/10
          interface GigabitEthernet2/11
interface GigabitEthernet2/12
interface GigabitEthernet2/13
interface GigabitEthernet2/14
interface GigabitEthernet2/15
interface GigabitEthernet2/16
interface GigabitEthernet2/17
interface GigabitEthernet2/18
interface GigabitEthernet2/19
interface GigabitEthernet2/20
interface GigabitEthernet2/21
interface GigabitEthernet2/22
interface GigabitEthernet2/23
interface GigabitEthernet2/24
interface GigabitEthernet2/25
interface GigabitEthernet2/26
interface GigabitEthernet2/27
interface GigabitEthernet2/28
interface GigabitEthernet2/29
interface GigabitEthernet2/30
interface GigabitEthernet2/31
interface GigabitEthernet2/32
interface GigabitEthernet2/33
interface GigabitEthernet2/34
interface GigabitEthernet2/35
interface GigabitEthernet2/36
interface GigabitEthernet2/37
interface GigabitEthernet2/38
interface GigabitEthernet2/39
interface GigabitEthernet2/40
interface GigabitEthernet2/41
interface GigabitEthernet2/42
interface GigabitEthernet2/43
interface GigabitEthernet2/44
interface GigabitEthernet2/45
interface GigabitEthernet2/46
interface GigabitEthernet2/47
interface GigabitEthernet2/48
interface GigabitEthernet3/1
interface GigabitEthernet3/2
interface GigabitEthernet3/3
interface GigabitEthernet3/4
interface GigabitEthernet3/5
interface GigabitEthernet3/6
interface GigabitEthernet3/7
interface GigabitEthernet3/8
interface GigabitEthernet3/9
interface GigabitEthernet3/10
interface GigabitEthernet3/11
interface GigabitEthernet3/12
interface GigabitEthernet3/13
interface GigabitEthernet3/14
interface GigabitEthernet3/15
interface GigabitEthernet3/16
interface GigabitEthernet3/17
interface GigabitEthernet3/18
interface GigabitEthernet3/19
interface GigabitEthernet3/20
interface GigabitEthernet3/21
          interface GigabitEthernet3/22
interface GigabitEthernet3/23
interface GigabitEthernet3/24
interface GigabitEthernet3/25
interface GigabitEthernet3/26
interface GigabitEthernet3/27
interface GigabitEthernet3/28
interface GigabitEthernet3/29
interface GigabitEthernet3/30
interface GigabitEthernet3/31
interface GigabitEthernet3/32
interface GigabitEthernet3/33
interface GigabitEthernet3/34
interface GigabitEthernet3/35
interface GigabitEthernet3/36
interface GigabitEthernet3/37
interface GigabitEthernet3/38
interface GigabitEthernet3/39
interface GigabitEthernet3/40
interface GigabitEthernet3/41
interface GigabitEthernet3/42
interface GigabitEthernet3/43
interface GigabitEthernet3/44
interface GigabitEthernet3/45
interface GigabitEthernet3/46
interface GigabitEthernet3/47
interface GigabitEthernet3/48
interface GigabitEthernet4/1
interface GigabitEthernet4/2
interface GigabitEthernet4/3
interface GigabitEthernet4/4
interface GigabitEthernet4/5
interface GigabitEthernet4/6
interface GigabitEthernet4/7
interface GigabitEthernet4/8
interface GigabitEthernet4/9
interface GigabitEthernet4/10
interface GigabitEthernet4/11
interface GigabitEthernet4/12
interface GigabitEthernet4/13
interface GigabitEthernet4/14
interface GigabitEthernet4/15
interface GigabitEthernet4/16
interface GigabitEthernet4/17
interface GigabitEthernet4/18
interface GigabitEthernet4/19
interface GigabitEthernet4/20
interface GigabitEthernet4/21
interface GigabitEthernet4/22
interface GigabitEthernet4/23
interface GigabitEthernet4/24
interface GigabitEthernet4/25
interface GigabitEthernet4/26
interface GigabitEthernet4/27
interface GigabitEthernet4/28
interface GigabitEthernet4/29
interface GigabitEthernet4/30
interface GigabitEthernet4/31
interface GigabitEthernet4/32
          interface GigabitEthernet4/33
interface GigabitEthernet4/34
interface GigabitEthernet4/35
interface GigabitEthernet4/36
interface GigabitEthernet4/37
interface GigabitEthernet4/38
interface GigabitEthernet4/39
interface GigabitEthernet4/40
interface GigabitEthernet4/41
interface GigabitEthernet4/42
interface GigabitEthernet4/43
interface GigabitEthernet4/44
interface GigabitEthernet4/45
interface GigabitEthernet4/46
interface GigabitEthernet4/47
interface GigabitEthernet4/48
interface TenGigabitEthernet5/1
interface TenGigabitEthernet5/2
interface TenGigabitEthernet5/3
interface TenGigabitEthernet5/4
interface GigabitEthernet8/1
interface GigabitEthernet8/2
interface GigabitEthernet8/3
interface GigabitEthernet8/4
interface GigabitEthernet8/5
interface GigabitEthernet8/6
interface GigabitEthernet8/7
interface GigabitEthernet8/8
interface GigabitEthernet8/9
interface GigabitEthernet8/10
interface GigabitEthernet8/11
interface GigabitEthernet8/12
interface GigabitEthernet8/13
interface GigabitEthernet8/14
interface GigabitEthernet8/15
interface GigabitEthernet8/16
interface GigabitEthernet8/17
interface GigabitEthernet8/18
interface GigabitEthernet8/19
interface GigabitEthernet8/20
interface GigabitEthernet8/21
interface GigabitEthernet8/22
interface GigabitEthernet8/23
interface GigabitEthernet8/24
interface GigabitEthernet8/25
interface GigabitEthernet8/26
interface GigabitEthernet8/27
interface GigabitEthernet8/28
interface GigabitEthernet8/29
interface GigabitEthernet8/30
interface GigabitEthernet8/31
interface GigabitEthernet8/32
interface GigabitEthernet8/33
interface GigabitEthernet8/34
interface GigabitEthernet8/35
interface GigabitEthernet8/36
interface GigabitEthernet8/37
interface GigabitEthernet8/38
interface GigabitEthernet8/39
          interface GigabitEthernet8/40
interface GigabitEthernet8/41
interface GigabitEthernet8/42
interface GigabitEthernet8/43
interface GigabitEthernet8/44
interface GigabitEthernet8/45
interface GigabitEthernet8/46
interface GigabitEthernet8/47
interface GigabitEthernet8/48
interface GigabitEthernet9/1
interface GigabitEthernet9/2
interface GigabitEthernet9/3
interface GigabitEthernet9/4
interface GigabitEthernet9/5
interface GigabitEthernet9/6
interface GigabitEthernet9/7
interface GigabitEthernet9/8
interface GigabitEthernet9/9
interface GigabitEthernet9/10
interface GigabitEthernet9/11
interface GigabitEthernet9/12
interface GigabitEthernet9/13
interface GigabitEthernet9/14
interface GigabitEthernet9/15
interface GigabitEthernet9/16
interface GigabitEthernet9/17
interface GigabitEthernet9/18
interface GigabitEthernet9/19
interface GigabitEthernet9/20
interface GigabitEthernet9/21
interface GigabitEthernet9/22
interface GigabitEthernet9/23
interface GigabitEthernet9/24
interface GigabitEthernet9/25
interface GigabitEthernet9/26
interface GigabitEthernet9/27
interface GigabitEthernet9/28
interface GigabitEthernet9/29
interface GigabitEthernet9/30
interface GigabitEthernet9/31
interface GigabitEthernet9/32
interface GigabitEthernet9/33
interface GigabitEthernet9/34
interface GigabitEthernet9/35
interface GigabitEthernet9/36
interface GigabitEthernet9/37
interface GigabitEthernet9/38
interface GigabitEthernet9/39
interface GigabitEthernet9/40
interface GigabitEthernet9/41
interface GigabitEthernet9/42
interface GigabitEthernet9/43
interface GigabitEthernet9/44
interface GigabitEthernet9/45
interface GigabitEthernet9/46
interface GigabitEthernet9/47
interface GigabitEthernet9/48
interface GigabitEthernet10/1
interface GigabitEthernet10/2
          interface GigabitEthernet10/3
interface GigabitEthernet10/4
interface GigabitEthernet10/5
interface GigabitEthernet10/6
interface GigabitEthernet10/7
interface GigabitEthernet10/8
interface GigabitEthernet10/9
interface GigabitEthernet10/10
interface GigabitEthernet10/11
interface GigabitEthernet10/12
interface GigabitEthernet10/13
interface GigabitEthernet10/14
interface GigabitEthernet10/15
interface GigabitEthernet10/16
interface GigabitEthernet10/17
interface GigabitEthernet10/18
interface GigabitEthernet10/19
interface GigabitEthernet10/20
interface GigabitEthernet10/21
interface GigabitEthernet10/22
interface GigabitEthernet10/23
interface GigabitEthernet10/24
interface GigabitEthernet10/25
interface GigabitEthernet10/26
interface GigabitEthernet10/27
interface GigabitEthernet10/28
interface GigabitEthernet10/29
interface GigabitEthernet10/30
interface GigabitEthernet10/31
interface GigabitEthernet10/32
interface GigabitEthernet10/33
interface GigabitEthernet10/34
interface GigabitEthernet10/35
interface GigabitEthernet10/36
interface GigabitEthernet10/37
interface GigabitEthernet10/38
interface GigabitEthernet10/39
interface GigabitEthernet10/40
interface GigabitEthernet10/41
interface GigabitEthernet10/42
interface GigabitEthernet10/43
interface GigabitEthernet10/44
interface GigabitEthernet10/45
interface GigabitEthernet10/46
interface GigabitEthernet10/47
interface GigabitEthernet10/48
interface Vlan1
interface Vlan874
logging source-interface Vlan874""",
 'show interface link':"""Port    Name               Down Time        Down Since
Gi1/1    ACCESS POINT      00 secs 
Gi1/2    ACCESS POINT      00 secs 
Gi1/3    ACCESS POINT      00 secs 
Gi1/4    ACCESS POINT      00 secs 
Gi1/5    ACCESS POINT      00 secs 
Gi1/6    ACCESS POINT      00 secs 
Gi1/7    ACCESS POINT      00 secs 
Gi1/8    ACCESS POINT      00 secs 
Gi1/9    ACCESS POINT      00 secs 
Gi1/10   ACCESS POINT      00 secs 
Gi1/11   ACCESS POINT      00 secs 
Gi1/12   ACCESS POINT      00 secs 
Gi1/13   ACCESS POINT      00 secs 
Gi1/14   ACCESS POINT      00 secs 
Gi1/15   ACCESS POINT      00 secs 
Gi1/16   ACCESS POINT      00 secs 
Gi1/17   ACCESS POINT      00 secs 
Gi1/18   ACCESS POINT      00 secs 
Gi1/19   ACCESS POINT      00 secs 
Gi1/20   ACCESS POINT      00 secs 
Gi1/21   ACCESS POINT      00 secs 
Gi1/22   ACCESS POINT      00 secs 
Gi1/23   ACCESS POINT      00 secs 
Gi1/24   ACCESS POINT      00 secs 
Gi1/25   ACCESS POINT      00 secs 
Gi1/26   ACCESS POINT      00 secs 
Gi1/27   ACCESS POINT      00 secs 
Gi1/28   ACCESS POINT      00 secs 
Gi1/29   ACCESS POINT      00 secs 
Gi1/30   ACCESS POINT      00 secs 
Gi1/31   ACCESS POINT      00 secs 
Gi1/32   ACCESS POINT      00 secs 
Gi1/33   ACCESS POINT      00 secs 
Gi1/34   ACCESS POINT      00 secs 
Gi1/35   ACCESS POINT      00 secs 
Gi1/36   ACCESS POINT      00 secs 
Gi1/37   ACCESS POINT      00 secs 
Gi1/38   ACCESS POINT      00 secs 
Gi1/39   ACCESS POINT      00 secs 
Gi1/40                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi1/41                     00 secs 
Gi1/42                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi1/43   red-print-kiosk   00 secs 
Gi1/44                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi1/45                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi1/46                     00 secs 
Gi1/47                     00 secs 
Gi1/48                     00 secs 
Gi2/1                      00 secs 
Gi2/2                      00 secs 
Gi2/3                      00 secs 
Gi2/4                      00 secs 
Gi2/5                      00 secs 
Gi2/6                      15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi2/7    ACCESS POINT      00 secs 
Gi2/8                      00 secs 
Gi2/9                      15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
          
Port    Name               Down Time        Down Since
Gi2/10                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi2/11                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi2/12   ACCESS POINT      00 secs 
Gi2/13                     00 secs 
Gi2/14                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi2/15                     00 secs 
Gi2/16                     00 secs 
Gi2/17   ACCESS POINT      00 secs 
Gi2/18   ACCESS POINT      00 secs 
Gi2/19   ACCESS POINT      00 secs 
Gi2/20   ACCESS POINT      00 secs 
Gi2/21                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi2/22                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi2/23                     00 secs 
Gi2/24                     00 secs 
Gi2/25                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi2/26                     3 days, 3 hours, 38 minutes 23 secs      18:49:27  Tue Jun 22 2021
Gi2/27   ACCESS POINT      00 secs 
Gi2/28                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi2/29                     00 secs 
Gi2/30   ACCESS POINT      00 secs 
Gi2/31   CAM               00 secs 
Gi2/32   ACCESS POINT      00 secs 
Gi2/33   CAM               00 secs 
Gi2/34   CAM               00 secs 
Gi2/35   ACCESS POINT      00 secs 
Gi2/36                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi2/37   ACCESS POINT      00 secs 
Gi2/38                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi2/39                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi2/40                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi2/41   ACCESS POINT      00 secs 
Gi2/42                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi2/43   ACCESS POINT      00 secs 
Gi2/44                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi2/45                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi2/46   ACCESS POINT      00 secs 
Gi2/47                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi2/48                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi3/1                      00 secs 
Gi3/2    ACCESS POINT      00 secs 
Gi3/3                      15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi3/4                      15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi3/5                      15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi3/6    ACCESS POINT      00 secs 
Gi3/7                      15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi3/8                      15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi3/9                      15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi3/10                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi3/11                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi3/12                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi3/13                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi3/14   ACCESS POINT      00 secs 
Gi3/15                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi3/16                     12 weeks, 7 hours, 24 minutes 33 secs      15:03:17  Fri Apr 2 2021
Gi3/17                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi3/18                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi3/19                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi3/20                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
          
Port    Name               Down Time        Down Since
Gi3/21                     00 secs 
Gi3/22                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi3/23   ACCESS POINT      00 secs 
Gi3/24                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi3/25                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi3/26                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi3/27                     00 secs 
Gi3/28                     00 secs 
Gi3/29                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi3/30                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi3/31                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi3/32                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi3/33                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi3/34                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi3/35                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi3/36                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi3/37                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi3/38                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi3/39                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi3/40                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi3/41                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi3/42                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi3/43                     00 secs 
Gi3/44                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi3/45                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi3/46                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi3/47                     8 weeks, 3 days, 17 hours, 2 minutes 33 secs      05:25:17  Tue Apr 27 2021
Gi3/48                     4 weeks, 3 days, 4 hours, 18 minutes 01 sec      18:09:49  Tue May 25 2021
Gi4/1                      15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi4/2    ACCESS POINT      00 secs 
Gi4/3                      15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi4/4    ACCESS POINT      00 secs 
Gi4/5                      15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi4/6                      15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi4/7                      15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi4/8                      15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi4/9                      15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi4/10   ACCESS POINT      00 secs 
Gi4/11                     8 weeks, 15 hours, 13 minutes 12 secs      07:14:38  Fri Apr 30 2021
Gi4/12                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi4/13                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi4/14                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi4/15   ACCESS POINT      00 secs 
Gi4/16   ACCESS POINT      00 secs 
Gi4/17                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi4/18                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi4/19                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi4/20   ACCESS POINT      00 secs 
Gi4/21                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi4/22                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi4/23   SHUT FOR COPYRIGHT15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi4/24                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi4/25   ACCESS POINT      00 secs 
Gi4/26                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi4/27                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi4/28   ACCESS POINT      15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi4/29   ACCESS POINT      00 secs 
Gi4/30                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi4/31                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
          
Port    Name               Down Time        Down Since
Gi4/32                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi4/33                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi4/34   ACCESS POINT      00 secs 
Gi4/35                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi4/36                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi4/37   ACCESS POINT      00 secs 
Gi4/38                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi4/39   ACCESS POINT      00 secs 
Gi4/40                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi4/41                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi4/42   ACCESS POINT      00 secs 
Gi4/43                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi4/44                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi4/45                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi4/46   ACCESS POINT      00 secs 
Gi4/47                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi4/48   ACCESS POINT      00 secs 
Te5/1    key:Te5/1:dx1-112m00 secs 
Te5/2                      15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Te5/3                      15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Te5/4                      15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi8/1                      00 secs 
Gi8/2    ACCESS POINT      15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi8/3                      15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi8/4                      15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi8/5                      15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi8/6                      00 secs 
Gi8/7    ACCESS POINT      00 secs 
Gi8/8    ACCESS POINT      00 secs 
Gi8/9                      15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi8/10                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi8/11                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi8/12                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi8/13                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi8/14                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi8/15                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi8/16                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi8/17                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi8/18                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi8/19                     6 weeks, 6 days, 20 hours, 10 minutes 47 secs      02:17:03  Sat May 8 2021
Gi8/20   ACCESS POINT      00 secs 
Gi8/21                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi8/22                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi8/23                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi8/24                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi8/25   ACCESS POINT      00 secs 
Gi8/26                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi8/27                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi8/28                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi8/29                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi8/30                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi8/31                     7 weeks, 3 days, 1 hour, 22 minutes 58 secs      21:04:52  Tue May 4 2021
Gi8/32   ACCESS POINT      00 secs 
Gi8/33   ACCESS POINT      00 secs 
Gi8/34                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi8/35                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi8/36                     11 weeks, 6 days, 8 hours, 56 minutes 34 secs      13:31:16  Sat Apr 3 2021
Gi8/37                     15 weeks, 1 day, 17 hours, 12 secs      04:44:42  Mon May 18 1925
Gi8/38   ACCESS POINT      00 secs 
          
Port    Name               Down Time        Down Since
Gi8/39                     15 weeks, 1 day, 17 hours, 12 secs      04:44:43  Mon May 18 1925
Gi8/40                     6 weeks, 5 days, 21 hours, 7 minutes 48 secs      01:20:03  Sun May 9 2021
Gi8/41                     15 weeks, 1 day, 17 hours, 12 secs      04:44:43  Mon May 18 1925
Gi8/42                     6 weeks, 5 days, 21 hours, 20 minutes 06 secs      01:07:45  Sun May 9 2021
Gi8/43                     15 weeks, 1 day, 17 hours, 12 secs      04:44:43  Mon May 18 1925
Gi8/44   ACCESS POINT      00 secs 
Gi8/45                     6 weeks, 5 days, 9 hours, 30 minutes 18 secs      12:57:33  Sun May 9 2021
Gi8/46                     15 weeks, 1 day, 17 hours, 12 secs      04:44:43  Mon May 18 1925
Gi8/47                     15 weeks, 1 day, 17 hours, 12 secs      04:44:43  Mon May 18 1925
Gi8/48                     15 weeks, 1 day, 17 hours, 12 secs      04:44:43  Mon May 18 1925
Gi9/1                      15 weeks, 1 day, 17 hours, 12 secs      04:44:43  Mon May 18 1925
Gi9/2                      15 weeks, 1 day, 17 hours, 12 secs      04:44:43  Mon May 18 1925
Gi9/3                      00 secs 
Gi9/4                      15 weeks, 1 day, 17 hours, 12 secs      04:44:43  Mon May 18 1925
Gi9/5                      15 weeks, 1 day, 17 hours, 12 secs      04:44:43  Mon May 18 1925
Gi9/6                      15 weeks, 1 day, 17 hours, 12 secs      04:44:43  Mon May 18 1925
Gi9/7                      15 weeks, 1 day, 17 hours, 12 secs      04:44:43  Mon May 18 1925
Gi9/8                      15 weeks, 1 day, 17 hours, 12 secs      04:44:43  Mon May 18 1925
Gi9/9                      15 weeks, 1 day, 17 hours, 12 secs      04:44:43  Mon May 18 1925
Gi9/10                     15 weeks, 1 day, 17 hours, 12 secs      04:44:43  Mon May 18 1925
Gi9/11   ACCESS POINT      00 secs 
Gi9/12   ACCESS POINT      00 secs 
Gi9/13                     15 weeks, 1 day, 17 hours, 12 secs      04:44:43  Mon May 18 1925
Gi9/14                     15 weeks, 1 day, 17 hours, 12 secs      04:44:43  Mon May 18 1925
Gi9/15                     15 weeks, 1 day, 17 hours, 12 secs      04:44:43  Mon May 18 1925
Gi9/16   ACCESS POINT      00 secs 
Gi9/17   ACCESS POINT      00 secs 
Gi9/18                     15 weeks, 1 day, 17 hours, 12 secs      04:44:43  Mon May 18 1925
Gi9/19                     7 weeks, 3 days, 14 hours, 15 minutes 49 secs      08:12:02  Tue May 4 2021
Gi9/20                     12 weeks, 2 days, 4 hours, 58 minutes 59 secs      17:28:52  Wed Mar 31 2021
Gi9/21                     15 weeks, 1 day, 17 hours, 12 secs      04:44:43  Mon May 18 1925
Gi9/22   ACCESS POINT      00 secs 
Gi9/23   ACCESS POINT      00 secs 
Gi9/24                     15 weeks, 1 day, 17 hours, 12 secs      04:44:43  Mon May 18 1925
Gi9/25                     15 weeks, 1 day, 17 hours, 12 secs      04:44:43  Mon May 18 1925
Gi9/26                     15 weeks, 1 day, 17 hours, 12 secs      04:44:43  Mon May 18 1925
Gi9/27                     8 weeks, 6 days, 20 hours, 12 minutes 08 secs      02:15:43  Sat Apr 24 2021
Gi9/28                     15 weeks, 1 day, 17 hours, 12 secs      04:44:43  Mon May 18 1925
Gi9/29                     15 weeks, 1 day, 17 hours, 12 secs      04:44:43  Mon May 18 1925
Gi9/30                     7 weeks, 3 days, 1 hour, 23 minutes 21 secs      21:04:30  Tue May 4 2021
Gi9/31                     12 weeks, 7 hours, 22 minutes 12 secs      15:05:39  Fri Apr 2 2021
Gi9/32                     15 weeks, 1 day, 17 hours, 12 secs      04:44:43  Mon May 18 1925
Gi9/33                     00 secs 
Gi9/34                     15 weeks, 1 day, 17 hours, 12 secs      04:44:43  Mon May 18 1925
Gi9/35                     15 weeks, 1 day, 17 hours, 12 secs      04:44:43  Mon May 18 1925
Gi9/36                     7 weeks, 2 days, 6 hours, 21 minutes 12 secs      16:06:39  Wed May 5 2021
Gi9/37                     7 weeks, 5 days, 17 hours, 58 minutes 55 secs      04:28:56  Sun May 2 2021
Gi9/38                     15 weeks, 1 day, 17 hours, 12 secs      04:44:43  Mon May 18 1925
Gi9/39                     15 weeks, 1 day, 17 hours, 12 secs      04:44:43  Mon May 18 1925
Gi9/40                     00 secs 
Gi9/41                     15 weeks, 1 day, 17 hours, 12 secs      04:44:43  Mon May 18 1925
Gi9/42                     15 weeks, 1 day, 17 hours, 12 secs      04:44:43  Mon May 18 1925
Gi9/43                     7 weeks, 6 hours, 4 minutes 23 secs      16:23:28  Fri May 7 2021
Gi9/44                     15 weeks, 1 day, 17 hours, 12 secs      04:44:43  Mon May 18 1925
Gi9/45                     15 weeks, 1 day, 17 hours, 12 secs      04:44:43  Mon May 18 1925
Gi9/46                     15 weeks, 1 day, 17 hours, 12 secs      04:44:43  Mon May 18 1925
Gi9/47                     15 weeks, 1 day, 17 hours, 12 secs      04:44:43  Mon May 18 1925
Gi9/48                     15 weeks, 1 day, 17 hours, 12 secs      04:44:43  Mon May 18 1925
Gi10/1                     15 weeks, 1 day, 17 hours, 12 secs      04:44:43  Mon May 18 1925
          
Port    Name               Down Time        Down Since
Gi10/2   ACCESS POINT      00 secs 
Gi10/3                     15 weeks, 1 day, 17 hours, 13 secs      04:44:42  Mon May 18 1925
Gi10/4                     15 weeks, 1 day, 17 hours, 13 secs      04:44:42  Mon May 18 1925
Gi10/5                     15 weeks, 1 day, 17 hours, 13 secs      04:44:42  Mon May 18 1925
Gi10/6                     15 weeks, 1 day, 17 hours, 13 secs      04:44:42  Mon May 18 1925
Gi10/7   ACCESS POINT      00 secs 
Gi10/8                     15 weeks, 1 day, 17 hours, 13 secs      04:44:42  Mon May 18 1925
Gi10/9                     15 weeks, 1 day, 17 hours, 13 secs      04:44:42  Mon May 18 1925
Gi10/10  ACCESS POINT      00 secs 
Gi10/11                    15 weeks, 1 day, 17 hours, 13 secs      04:44:42  Mon May 18 1925
Gi10/12                    15 weeks, 1 day, 17 hours, 13 secs      04:44:42  Mon May 18 1925
Gi10/13                    15 weeks, 1 day, 17 hours, 13 secs      04:44:42  Mon May 18 1925
Gi10/14                    15 weeks, 1 day, 17 hours, 13 secs      04:44:42  Mon May 18 1925
Gi10/15                    15 weeks, 1 day, 17 hours, 13 secs      04:44:42  Mon May 18 1925
Gi10/16                    15 weeks, 1 day, 17 hours, 13 secs      04:44:42  Mon May 18 1925
Gi10/17                    15 weeks, 1 day, 17 hours, 13 secs      04:44:42  Mon May 18 1925
Gi10/18                    15 weeks, 1 day, 17 hours, 13 secs      04:44:42  Mon May 18 1925
Gi10/19                    15 weeks, 1 day, 17 hours, 13 secs      04:44:42  Mon May 18 1925
Gi10/20  ACCESS POINT      00 secs 
Gi10/21                    15 weeks, 1 day, 17 hours, 13 secs      04:44:42  Mon May 18 1925
Gi10/22                    15 weeks, 1 day, 17 hours, 13 secs      04:44:42  Mon May 18 1925
Gi10/23                    15 weeks, 1 day, 17 hours, 13 secs      04:44:42  Mon May 18 1925
Gi10/24                    15 weeks, 1 day, 17 hours, 13 secs      04:44:42  Mon May 18 1925
Gi10/25                    15 weeks, 1 day, 17 hours, 13 secs      04:44:42  Mon May 18 1925
Gi10/26  ACCESS POINT      00 secs 
Gi10/27                    15 weeks, 1 day, 17 hours, 13 secs      04:44:42  Mon May 18 1925
Gi10/28                    15 weeks, 1 day, 17 hours, 13 secs      04:44:42  Mon May 18 1925
Gi10/29                    15 weeks, 1 day, 17 hours, 13 secs      04:44:42  Mon May 18 1925
Gi10/30                    15 weeks, 1 day, 17 hours, 13 secs      04:44:42  Mon May 18 1925
Gi10/31                    15 weeks, 1 day, 17 hours, 13 secs      04:44:42  Mon May 18 1925
Gi10/32                    15 weeks, 1 day, 17 hours, 13 secs      04:44:42  Mon May 18 1925
Gi10/33                    15 weeks, 1 day, 17 hours, 13 secs      04:44:42  Mon May 18 1925
Gi10/34                    15 weeks, 1 day, 17 hours, 13 secs      04:44:42  Mon May 18 1925
Gi10/35                    15 weeks, 1 day, 17 hours, 13 secs      04:44:42  Mon May 18 1925
Gi10/36                    15 weeks, 1 day, 17 hours, 13 secs      04:44:42  Mon May 18 1925
Gi10/37                    15 weeks, 1 day, 17 hours, 13 secs      04:44:42  Mon May 18 1925
Gi10/38                    15 weeks, 1 day, 17 hours, 13 secs      04:44:42  Mon May 18 1925
Gi10/39                    00 secs 
Gi10/40                    15 weeks, 1 day, 17 hours, 13 secs      04:44:42  Mon May 18 1925
Gi10/41                    6 weeks, 6 days, 5 hours, 13 minutes 31 secs      17:14:20  Sat May 8 2021
Gi10/42                    15 weeks, 1 day, 17 hours, 13 secs      04:44:42  Mon May 18 1925
Gi10/43                    15 weeks, 1 day, 17 hours, 13 secs      04:44:42  Mon May 18 1925
Gi10/44  ACCESS POINT      00 secs 
Gi10/45                    15 weeks, 1 day, 17 hours, 13 secs      04:44:42  Mon May 18 1925
Gi10/46  ACCESS POINT      00 secs 
Gi10/47  ACCESS POINT      00 secs 
Gi10/48                    15 weeks, 1 day, 17 hours, 13 secs      04:44:42  Mon May 18 1925""",
