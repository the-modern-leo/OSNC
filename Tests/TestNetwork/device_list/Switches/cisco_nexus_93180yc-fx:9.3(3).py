ip_address = '172.30.0.151'
software = 'software'
hardware = 'hardware'
read_results = {
 'show version':"""Cisco Nexus Operating System (NX-OS) Software
TAC support: http://www.cisco.com/tac
Copyright (C) 2002-2019, Cisco and/or its affiliates.
All rights reserved.
The copyrights to certain works contained in this software are
owned by other third parties and used and distributed under their own
licenses, such as open source.  This software is provided "as is," and unless
otherwise stated, there is no warranty, express or implied, including but not
limited to warranties of merchantability and fitness for a particular purpose.
Certain components of this software are licensed under
the GNU General Public License (GPL) version 2.0 or 
GNU General Public License (GPL) version 3.0  or the GNU
Lesser General Public License (LGPL) Version 2.1 or 
Lesser General Public License (LGPL) Version 2.0. 
A copy of each such license is available at
http://www.opensource.org/licenses/gpl-2.0.php and
http://opensource.org/licenses/gpl-3.0.html and
http://www.opensource.org/licenses/lgpl-2.1.php and
http://www.gnu.org/licenses/old-licenses/library.txt.

Software
  BIOS: version 05.40
 NXOS: version 9.3(3)
  BIOS compile time:  01/17/2020
  NXOS image file is: bootflash:///nxos.9.3.3.bin
  NXOS compile time:  12/22/2019 2:00:00 [12/22/2019 07:00:37]


Hardware
  cisco Nexus9000 C93180YC-FX Chassis 
  Intel(R) Xeon(R) CPU D-1528 @ 1.90GHz with 32827212 kB of memory.
  Processor Board ID FDO24250AYL

  Device name: dcx1-079sfebb-server-lib
  bootflash:  115805708 kB
Kernel uptime is 81 day(s), 7 hour(s), 0 minute(s), 25 second(s)

Last reset at 83305 usecs after Mon Apr  5 09:18:33 2021
  Reason: Reset Requested by CLI command reload
  System version: 7.0(3)I7(9)
  Service: 

plugin
  Core Plugin, Ethernet Plugin

Active Package(s):
        """,
 'show run':"""!Command: ning-config
!Running configuration last done at: Tue Jun 22 12:07:56 2021
!Time: Fri Jun 25 16:20:18 2021

version 9.3(3) Bios:version 05.40 
hostname dcx1-079sfebb-server-lib
class-map type network-qos class-fcoe
class-map type network-qos class-all-flood
  match qos-group 2
class-map type network-qos class-ip-multicast
  match qos-group 2
policy-map type network-qos jumbo
  class type network-qos class-default
    mtu 9216
vdc dcx1-079sfebb-server-lib id 1
  limit-resource vlan minimum 16 maximum 4094
  limit-resource vrf minimum 2 maximum 4096
  limit-resource port-channel minimum 0 maximum 511
  limit-resource u4route-mem minimum 248 maximum 248
  limit-resource u6route-mem minimum 96 maximum 96
  limit-resource m4route-mem minimum 58 maximum 58
  limit-resource m6route-mem minimum 8 maximum 8

feature tacacs+
cfs eth distribute
feature udld
feature interface-vlan
feature lacp
feature vpc
feature lldp
clock timezone MST -7 0
clock summer-time MDT 2 Sunday March 02:00 1 Sunday November 02:00 60

logging level feature-mgr 0
username admin password 5 $5$0ZbOSRdS$JuaV8QdS9Ka1jrwLI.EBqDBRPA1nH97.b9/Y5iaLMs9  role network-admin
username networker password 5 $5$zGymEp4g$OekpXR5K52AiqCtVTxUgfnxpKNsHqIS7/UWpdObSed1  role network-admin
username networker passphrase  lifetime 99999 warntime 7
username NXUSERNOC password 5 $5$j6hWTWGH$LYZGq8Ly.ndgPrZfkrCJYUj5mPxoAb0C0fAr/Uu0a52  role network-operator
username NXUSERNOC passphrase  lifetime 99999 warntime 7

banner motd ^
dcx1-079sfebb-server-lib

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

^

ip domain-lookup
ip domain-name net.utah.edu
ip name-server 172.20.120.20
ip host dcx1-079sfebb-server-lib 172.30.0.151
tacacs-server key 7 "L$iN$eW@tb!"
tacacs-server host 172.31.17.180 
tacacs-server host 10.64.32.5 
aaa group server tacacs+ TacServer 
    server 172.31.17.180 
    server 10.64.32.5 
    use-vrf management
aaa group server tacacs+ tacacs 
crypto key generate rsa label dcx1-079sfebb-server-lib modulus 2048
object-group ip address ORION_POLLERS
  10 host 155.98.253.147 
  20 host 155.98.253.149 
  30 host 155.98.253.150 
  40 host 155.98.253.152 
  50 host 155.98.253.155 
  60 host 155.98.253.156 
  70 host 155.98.253.157 
  220 host 10.71.24.11 
  230 host 10.71.24.12 
  240 host 10.71.24.13 
  250 host 10.71.24.14 
  260 host 10.71.24.15 
  270 host 10.71.24.16 
  280 host 10.71.24.17 
  290 host 10.71.24.18 
  300 host 10.71.24.19 
  310 host 10.71.24.20 
  320 host 10.71.24.21 
  330 host 10.71.24.22 
  340 host 10.71.24.23 
  350 host 10.71.24.10 
  360 host 10.71.24.9 
  370 host 10.71.24.8 
  380 host 10.71.24.7 
  390 host 10.71.24.6 
ip access-list SSH_POLICY
  10 permit tcp 155.98.253.0/24 any eq 22 
  15 permit tcp 155.99.254.128/25 any eq 22 
  20 remark VPN Networks
  25 permit tcp 155.98.164.192/27 any eq 22 
  30 permit tcp 155.101.243.0/27 any eq 22 
  31 permit tcp 155.98.164.192/27 any eq 22 
  40 deny tcp 155.100.37.16/32 any eq 22 
  50 deny tcp 155.100.37.31/32 any eq 22 
  60 permit tcp 155.100.37.16/28 any eq 22 
  61 permit tcp 155.99.254.128/25 any eq 22 
  70 remark Door1 & Door2
  80 permit tcp 155.99.239.130/32 any eq 22 
  90 permit tcp 155.97.152.244/32 any eq 22 
  95 permit tcp 155.101.168.124/32 any eq 22 
  99 remark Allow Firemon
  100 remark make 110 for Duc
  120 permit udp addrgroup ORION_POLLERS any eq snmp 
  125 permit udp addrgroup ORION_POLLERS any eq snmptrap 
  130 permit tcp addrgroup ORION_POLLERS any eq 22 
ipv6 access-list VTY-ACL
  10 deny ipv6 any any log 
class-map type qos match-all class-fcoe
system qos
  service-policy type network-qos jumbo
copp profile strict
snmp-server contact TAG:%TAG%-BarCode:%BARCODE%
snmp-server location %BLDG#-RACK#%
snmp-server user admin network-admin auth md5 0x2bf2166822d5f82043bdd1f7076ccfe4 priv 0x2bf2166822d5f82043bdd1f7076ccfe4
 localizedkey
snmp-server user NXUSERNOC network-operator auth md5 0x419fb9d1a1907eb989eab2232cbd0960 priv aes-128 0x419fb9d1a1907eb98
9eab2232cbd0960 localizedkey
snmp-server user networker network-admin auth md5 0x2b41eeed2dde536d78f68149bfc555be priv 0x2b41eeed2dde536d78f68149bfc5
55be localizedkey
snmp-server user admin auth md5 0x1ca4cd1eafaa0407d413582efec4458c priv 0x1ca4cd1eafaa0407d413582efec4458c localizedkey 
engineID 128:0:0:9:3:216:103:217:1:14:0
rmon event 1 log trap public description FATAL(1) owner PMON@FATAL
rmon event 2 log trap public description CRITICAL(2) owner PMON@CRITICAL
rmon event 3 log trap public description ERROR(3) owner PMON@ERROR
rmon event 4 log trap public description WARNING(4) owner PMON@WARNING
rmon event 5 log trap public description INFORMATION(5) owner PMON@INFO
aaa authentication login default group TacServer 
aaa authentication login console local 

vlan 1,2715,2799-2800,2808-2809,2811-2820,2823-2827,2831,2870,2872-2873,2876-2879,2882,2889
vlan 2715
  name BUS-END_USER-3
vlan 2799
  name BUS-SENSITIVE_DATA
vlan 2800
  name BUS_AV
vlan 2808
  name lib-079-BUS-SENSITIVE_DATA2
vlan 2809
  name lib-079-BUS-Fully_Restricted
vlan 2811
  name lib-079-BUS-Services_Public
vlan 2812
  name lib-079-BUS-Services_Public2
vlan 2813
  name lib-079-BUS-Services_Secure2
vlan 2814
  name lib-079-BUS-SENSITIVE_DATA4
vlan 2815
  name lib-079-BUS-STUDENT_NETWORKS2
vlan 2816
  name lib-079-BUS-END_USER2
vlan 2817
  name lib-079-BUS-END_USER3
vlan 2818
  name lib-079-BUS-UNRESTRICTED
vlan 2819
  name lib-079-BUS-Printers
vlan 2820
  name BUS-SERVICES_SECURE
vlan 2823
  name lib-079-BUS-AV2
vlan 2824
  name lib-079-BUS-SENSITIVE_DATA
vlan 2825
  name lib-079-BUS-SENSITIVE_DATA3
vlan 2826
  name BUS-FACILITIES
vlan 2827
  name BUS-END_USER
vlan 2831
  name lib-079-BUS-Services_Secure4
vlan 2870
  name lib-079-BUS-STUDENT_NETWORKS3
vlan 2872
  name BUS-STUDENT_NETWORKS
vlan 2873
  name lib-079-BUS-STUDENT_NETWORKS
vlan 2876
  name lib-079-BUS-Services_Secure5
vlan 2877
  name lib-079-BUS-Services_Secure
vlan 2878
  name lib-079-BUS-END_USER4
vlan 2879
  name BUS-STUDENT_NETWORKS-2
vlan 2882
  name lib-079-BUS-UNRESTRICTED2
vlan 2889
  name lib-079-BUS-Services_Secure3

spanning-tree vlan 1-3967 priority 61440
vrf context management
  ip domain-name net.utah.edu
  ip name-server 172.20.120.20
  ip route 0.0.0.0/0 172.30.0.129


interface Vlan1
  no ip redirects
  no ipv6 redirects

interface port-channel11
  description IBM_Flex_CH1SW2
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 2810-2813,2815-2818,2820,2824-2828,2865,2870,2872-2873,2875,2878-2879,2884-2885,2888-288
9,2903,2905
  no lacp graceful-convergence

interface port-channel12
  description IBM_Flex_CH2SW1
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 2824-2825
  mtu 9216

interface port-channel13
  description IBM_Flex_CH2SW2
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 2810-2813,2815-2818,2820,2824-2828,2865,2870,2872-2873,2875,2878-2879,2884-2885,2888-288
9,2903,2905
[K
interface port-channel16
  description Infortrend Controller A
  switchport
  switchport access vlan 2824
  mtu 9216

interface port-channel20
  description bus-filer02
  switchport
  switchport access vlan 2824

interface port-channel21
  description tegile1
  switchport
  switchport access vlan 2824
  mtu 9216

interface port-channel22
  description tegile2
  switchport
  switchport access vlan 2824
  mtu 9216

interface port-channel23
  description tegile3
  switchport
  switchport access vlan 2824
  mtu 9216

interface port-channel24
  description tegile4
  switchport
  switchport access vlan 2824
  mtu 9216

interface Ethernet1/1

interface Ethernet1/2

interface Ethernet1/3
  description BAD PORT

interface Ethernet1/4

interface Ethernet1/5
  description bus-tegile3-ix2
  switchport
  switchport access vlan 2824
  spanning-tree port type edge
  mtu 9216
  no shutdown

interface Ethernet1/6
  description bus-tegile3-ix3
  switchport
  switchport access vlan 2824
  spanning-tree port type edge
  mtu 9216
  no shutdown

interface Ethernet1/7
  description bus-tegile4-ix2
  switchport
  switchport access vlan 2824
  spanning-tree port type edge
  mtu 9216
  no shutdown

interface Ethernet1/8
  description bus-tegile4-ix3
  switchport
  switchport access vlan 2824
  spanning-tree port type edge
  mtu 9216
  no shutdown

interface Ethernet1/9
  description esxsrv21 Dell R740 vmnic0 -| WPort 2055 |-
  switchport
  switchport access vlan 2824
  spanning-tree port type edge
  mtu 9216
  no shutdown

interface Ethernet1/10
  description esxsrv21 Dell R740 vmnic1 -| WPort 2056 |-
  switchport
  switchport access vlan 2824
  spanning-tree port type edge
  mtu 9216
  no shutdown

interface Ethernet1/11
  description dell esxsrv24
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 2810-2813,2815-2818,2820,2824-2828,2865,2870,2872-2873,2875,2878-2879,2884-2885,2888-288
9
  no shutdown

interface Ethernet1/12
  description BROKEN

interface Ethernet1/13
  description bus-backup
  switchport
  switchport access vlan 2824
  spanning-tree port type normal
  no shutdown

interface Ethernet1/14

interface Ethernet1/15
  description Infortrend ISCSI 1 TEMPORARY
  switchport
  switchport access vlan 2824
  spanning-tree port type edge
  no shutdown

interface Ethernet1/16
  description Infortrend ISCSI 3 TEMPORARY
  switchport
  switchport access vlan 2824
  spanning-tree port type edge
  no shutdown

interface Ethernet1/17
  description Infortrend ISCSI 1 TEMPORARY
  switchport
  switchport access vlan 2824
  spanning-tree port type edge
  no shutdown

interface Ethernet1/18
  description Infortrend ISCSI 1 TEMPORARY
  switchport
  switchport access vlan 2824
  spanning-tree port type edge
  no shutdown

interface Ethernet1/19
  description IBM_Flex_CH2SW2 | TS 5/27/21
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 2810-2813,2815-2818,2820,2824-2828,2865,2870,2872-2873,2875,2878-2879,2884-2885,2888-288
9,2903,2905
  channel-group 11 mode active
  no shutdown

interface Ethernet1/20
  description IBM_Flex_CH2SW2 | TS 5/27/21
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 2810-2813,2815-2818,2820,2824-2828,2865,2870,2872-2873,2875,2878-2879,2884-2885,2888-288
9,2903,2905
  channel-group 11 mode active
  no shutdown

interface Ethernet1/21
  description IBM_Flex_CH2SW1
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 2824-2825
  mtu 9216
  channel-group 12 mode active
  no shutdown

interface Ethernet1/22
  description IBM_Flex_CH2SW1
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 2824-2825
  mtu 9216
  channel-group 12 mode active
  no shutdown

interface Ethernet1/23
  description IBM_Flex_CH2SW2
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 2810-2813,2815-2818,2820,2824-2828,2865,2870,2872-2873,2875,2878-2879,2884-2885,2888-288
9,2903,2905

interface Ethernet1/24
  description IBM_Flex_CH2SW2
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 2810-2813,2815-2818,2820,2824-2828,2865,2870,2872-2873,2875,2878-2879,2884-2885,2888-288
9,2903,2905

interface Ethernet1/25
  description dell esxsrv24
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 2810-2813,2815-2818,2820,2824-2828,2865,2870,2872-2873,2875,2878-2879,2884-2885,2888-288
9
  no shutdown

interface Ethernet1/26

interface Ethernet1/27

interface Ethernet1/28

interface Ethernet1/29

interface Ethernet1/30

interface Ethernet1/31

interface Ethernet1/32

interface Ethernet1/33

interface Ethernet1/34

interface Ethernet1/35

interface Ethernet1/36

interface Ethernet1/37

interface Ethernet1/38

interface Ethernet1/39

interface Ethernet1/40

interface Ethernet1/41

interface Ethernet1/42

interface Ethernet1/43

interface Ethernet1/44
[K
interface Ethernet1/45

interface Ethernet1/46

interface Ethernet1/47

interface Ethernet1/48

interface Ethernet1/49
  switchport
  switchport mode trunk
  mtu 9216
  no shutdown

interface Ethernet1/50

interface Ethernet1/51

interface Ethernet1/52

interface Ethernet1/53

interface Ethernet1/54

interface mgmt0
  description key:dx1-079:g1/0/placeholder
  vrf member management
  ip address 172.30.0.151/25
cli alias name wri copy running-config startup-config
line console
line vty
  exec-timeout 15
  access-class SSH_POLICY in
  ipv6 access-class VTY-ACL in
boot nxos bootflash:/nxos.9.3.3.bin 

logging server 10.71.24.11 7 use-vrf management facility local6
logging server 172.24.29.14 7 use-vrf management facility local6

""",
 'show int status':"""--------------------------------------------------------------------------------
Port          Name               Status    Vlan      Duplex  Speed   Type
--------------------------------------------------------------------------------
mgmt0         key:dx1-079:g1/0/p connected routed    full    1000    --         

--------------------------------------------------------------------------------
Port          Name               Status    Vlan      Duplex  Speed   Type
--------------------------------------------------------------------------------
Eth1/1        --                 xcvrAbsen routed    auto    auto    --         
Eth1/2        --                 xcvrAbsen routed    auto    auto    --         
Eth1/3        BAD PORT           xcvrAbsen routed    auto    auto    --         
Eth1/4        --                 xcvrAbsen routed    auto    auto    --         
Eth1/5        bus-tegile3-ix2    connected 2824      full    10G     SFP-H10GB-ACU10M
Eth1/6        bus-tegile3-ix3    connected 2824      full    10G     SFP-H10GB-ACU10M
Eth1/7        bus-tegile4-ix2    connected 2824      full    10G     SFP-H10GB-ACU10M
Eth1/8        bus-tegile4-ix3    connected 2824      full    10G     SFP-H10GB-ACU10M
Eth1/9        esxsrv21 Dell R740 connected 2824      full    25G     SFP-H25GB-SR
Eth1/10       esxsrv21 Dell R740 connected 2824      full    25G     SFP-H25GB-SR
Eth1/11       dell esxsrv24      connected trunk     full    25G     SFP-H25GB-SR
Eth1/12       BROKEN             disabled  routed    auto    auto    SFP-H25GB-SR
Eth1/13       bus-backup         xcvrAbsen 2824      auto    auto    --         
Eth1/14       --                 xcvrAbsen routed    auto    auto    --         
Eth1/15       Infortrend ISCSI 1 xcvrAbsen 2824      auto    auto    --         
Eth1/16       Infortrend ISCSI 3 xcvrAbsen 2824      auto    auto    --         
Eth1/17       Infortrend ISCSI 1 xcvrAbsen 2824      auto    auto    --         
Eth1/18       Infortrend ISCSI 1 xcvrAbsen 2824      auto    auto    --         
Eth1/19       IBM_Flex_CH2SW2 |  connected trunk     full    10G     SFP-H10GB-CU5M
Eth1/20       IBM_Flex_CH2SW2 |  connected trunk     full    10G     SFP-H10GB-CU5M
Eth1/21       IBM_Flex_CH2SW1    xcvrAbsen trunk     auto    auto    --         
Eth1/22       IBM_Flex_CH2SW1    xcvrAbsen trunk     auto    auto    --         
Eth1/23       IBM_Flex_CH2SW2    xcvrAbsen trunk     auto    auto    --         
Eth1/24       IBM_Flex_CH2SW2    xcvrAbsen trunk     auto    auto    --         
Eth1/25       dell esxsrv24      connected trunk     full    25G     SFP-H25GB-SR
Eth1/26       --                 xcvrAbsen routed    auto    auto    --         
Eth1/27       --                 xcvrAbsen routed    auto    auto    --         
Eth1/28       --                 xcvrAbsen routed    auto    auto    --         
Eth1/29       --                 xcvrAbsen routed    auto    auto    --         
Eth1/30       --                 xcvrAbsen routed    auto    auto    --         
Eth1/31       --                 xcvrAbsen routed    auto    auto    --         
Eth1/32       --                 xcvrAbsen routed    auto    auto    --         
Eth1/33       --                 xcvrAbsen routed    auto    auto    --         
Eth1/34       --                 xcvrAbsen routed    auto    auto    --         
Eth1/35       --                 xcvrAbsen routed    auto    auto    --         
Eth1/36       --                 xcvrAbsen routed    auto    auto    --         
Eth1/37       --                 xcvrAbsen routed    auto    auto    --         
Eth1/38       --                 xcvrAbsen routed    auto    auto    --         
Eth1/39       --                 xcvrAbsen routed    auto    auto    --         
Eth1/40       --                 xcvrAbsen routed    auto    auto    --         
Eth1/41       --                 xcvrAbsen routed    auto    auto    --         
Eth1/42       --                 xcvrAbsen routed    auto    auto    --         
Eth1/43       --                 xcvrAbsen routed    auto    auto    --         
Eth1/44       --                 xcvrAbsen routed    auto    auto    --         
Eth1/45       --                 xcvrAbsen routed    auto    auto    --         
Eth1/46       --                 xcvrAbsen routed    auto    auto    --         
Eth1/47       --                 xcvrAbsen routed    auto    auto    --         
Eth1/48       --                 xcvrAbsen routed    auto    auto    --         
Eth1/49       --                 connected trunk     full    40G     QSFP-40GE-LR4
Eth1/50       --                 xcvrAbsen routed    auto    auto    --         
Eth1/51       --                 xcvrAbsen routed    auto    auto    --         
Eth1/52       --                 xcvrAbsen routed    auto    auto    --         
Eth1/53       --                 xcvrAbsen routed    auto    auto    --         
Eth1/54       --                 xcvrAbsen routed    auto    auto    --         
Po11          IBM_Flex_CH1SW2    connected trunk     full    10G     --         
Po12          IBM_Flex_CH2SW1    noOperMem trunk     auto    auto    --         
Po13          IBM_Flex_CH2SW2    noOperMem 1         auto    auto    --         
Po16          Infortrend Control noOperMem 2824      auto    auto    --         
Po20          bus-filer02        noOperMem 2824      auto    auto    --         
Po21          tegile1            noOperMem 2824      auto    auto    --         
Po22          tegile2            noOperMem 2824      auto    auto    --         
Po23          tegile3            noOperMem 2824      auto    auto    --         
Po24          tegile4            noOperMem 2824      auto    auto    --         
Vlan1         --                 down      routed    auto    auto    --""",
 'show run | section interface':"""feature interface-vlan
interface Vlan1
  no ip redirects
  no ipv6 redirects
interface port-channel11
  description IBM_Flex_CH1SW2
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 2810-2813,2815-2818,2820,2824-2828,2865,2870,2872-2873,2875,2878-2879,2884-2885,2888-288
9,2903,2905
  no lacp graceful-convergence
interface port-channel12
  description IBM_Flex_CH2SW1
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 2824-2825
  mtu 9216
interface port-channel13
  description IBM_Flex_CH2SW2
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 2810-2813,2815-2818,2820,2824-2828,2865,2870,2872-2873,2875,2878-2879,2884-2885,2888-288
9,2903,2905
interface port-channel16
  description Infortrend Controller A
  switchport
  switchport access vlan 2824
  mtu 9216
interface port-channel20
  description bus-filer02
  switchport
  switchport access vlan 2824
interface port-channel21
  description tegile1
  switchport
  switchport access vlan 2824
  mtu 9216
interface port-channel22
  description tegile2
  switchport
  switchport access vlan 2824
  mtu 9216
interface port-channel23
  description tegile3
  switchport
  switchport access vlan 2824
  mtu 9216
interface port-channel24
  description tegile4
  switchport
  switchport access vlan 2824
  mtu 9216
interface Ethernet1/1
interface Ethernet1/2
interface Ethernet1/3
  description BAD PORT
interface Ethernet1/4
interface Ethernet1/5
  description bus-tegile3-ix2
  switchport
  switchport access vlan 2824
  spanning-tree port type edge
  mtu 9216
  no shutdown
interface Ethernet1/6
  description bus-tegile3-ix3
  switchport
  switchport access vlan 2824
  spanning-tree port type edge
  mtu 9216
  no shutdown
interface Ethernet1/7
  description bus-tegile4-ix2
  switchport
  switchport access vlan 2824
  spanning-tree port type edge
  mtu 9216
  no shutdown
interface Ethernet1/8
  description bus-tegile4-ix3
  switchport
  switchport access vlan 2824
  spanning-tree port type edge
  mtu 9216
  no shutdown
interface Ethernet1/9
  description esxsrv21 Dell R740 vmnic0 -| WPort 2055 |-
  switchport
  switchport access vlan 2824
  spanning-tree port type edge
  mtu 9216
  no shutdown
interface Ethernet1/10
  description esxsrv21 Dell R740 vmnic1 -| WPort 2056 |-
  switchport
  switchport access vlan 2824
  spanning-tree port type edge
  mtu 9216
  no shutdown
interface Ethernet1/11
  description dell esxsrv24
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 2810-2813,2815-2818,2820,2824-2828,2865,2870,2872-2873,2875,2878-2879,2884-2885,2888-288
9
  no shutdown
interface Ethernet1/12
  description BROKEN
interface Ethernet1/13
  description bus-backup
  switchport
  switchport access vlan 2824
  spanning-tree port type normal
  no shutdown
interface Ethernet1/14
interface Ethernet1/15
  description Infortrend ISCSI 1 TEMPORARY
  switchport
  switchport access vlan 2824
  spanning-tree port type edge
  no shutdown
interface Ethernet1/16
  description Infortrend ISCSI 3 TEMPORARY
  switchport
  switchport access vlan 2824
  spanning-tree port type edge
  no shutdown
interface Ethernet1/17
  description Infortrend ISCSI 1 TEMPORARY
  switchport
  switchport access vlan 2824
  spanning-tree port type edge
  no shutdown
interface Ethernet1/18
  description Infortrend ISCSI 1 TEMPORARY
  switchport
  switchport access vlan 2824
  spanning-tree port type edge
  no shutdown
interface Ethernet1/19
  description IBM_Flex_CH2SW2 | TS 5/27/21
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 2810-2813,2815-2818,2820,2824-2828,2865,2870,2872-2873,2875,2878-2879,2884-2885,2888-288
9,2903,2905
  channel-group 11 mode active
  no shutdown
interface Ethernet1/20
  description IBM_Flex_CH2SW2 | TS 5/27/21
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 2810-2813,2815-2818,2820,2824-2828,2865,2870,2872-2873,2875,2878-2879,2884-2885,2888-288
9,2903,2905
  channel-group 11 mode active
  no shutdown
interface Ethernet1/21
  description IBM_Flex_CH2SW1
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 2824-2825
  mtu 9216
  channel-group 12 mode active
  no shutdown
interface Ethernet1/22
  description IBM_Flex_CH2SW1
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 2824-2825
  mtu 9216
  channel-group 12 mode active
  no shutdown
interface Ethernet1/23
  description IBM_Flex_CH2SW2
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 2810-2813,2815-2818,2820,2824-2828,2865,2870,2872-2873,2875,2878-2879,2884-2885,2888-288
9,2903,2905
interface Ethernet1/24
  description IBM_Flex_CH2SW2
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 2810-2813,2815-2818,2820,2824-2828,2865,2870,2872-2873,2875,2878-2879,2884-2885,2888-288
9,2903,2905
interface Ethernet1/25
  description dell esxsrv24
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 2810-2813,2815-2818,2820,2824-2828,2865,2870,2872-2873,2875,2878-2879,2884-2885,2888-288
9
  no shutdown
interface Ethernet1/26
interface Ethernet1/27
interface Ethernet1/28
interface Ethernet1/29
interface Ethernet1/30
interface Ethernet1/31
interface Ethernet1/32
interface Ethernet1/33
interface Ethernet1/34
interface Ethernet1/35
interface Ethernet1/36
interface Ethernet1/37
interface Ethernet1/38
interface Ethernet1/39
interface Ethernet1/40
interface Ethernet1/41
interface Ethernet1/42
interface Ethernet1/43
interface Ethernet1/44
interface Ethernet1/45
interface Ethernet1/46
interface Ethernet1/47
interface Ethernet1/48
interface Ethernet1/49
  switchport
  switchport mode trunk
  mtu 9216
  no shutdown
interface Ethernet1/50
interface Ethernet1/51
interface Ethernet1/52
interface Ethernet1/53
interface Ethernet1/54
interface mgmt0
  description key:dx1-079:g1/0/placeholder
  vrf member management
  ip address 172.30.0.151/25""",
 'show run | in interface':"""feature interface-vlan
interface Vlan1
interface port-channel11
interface port-channel12
interface port-channel13
interface port-channel16
interface port-channel20
interface port-channel21
interface port-channel22
interface port-channel23
interface port-channel24
interface Ethernet1/1
interface Ethernet1/2
interface Ethernet1/3
interface Ethernet1/4
interface Ethernet1/5
interface Ethernet1/6
interface Ethernet1/7
interface Ethernet1/8
interface Ethernet1/9
interface Ethernet1/10
interface Ethernet1/11
interface Ethernet1/12
interface Ethernet1/13
interface Ethernet1/14
interface Ethernet1/15
interface Ethernet1/16
interface Ethernet1/17
interface Ethernet1/18
interface Ethernet1/19
interface Ethernet1/20
interface Ethernet1/21
interface Ethernet1/22
interface Ethernet1/23
interface Ethernet1/24
interface Ethernet1/25
interface Ethernet1/26
interface Ethernet1/27
interface Ethernet1/28
interface Ethernet1/29
interface Ethernet1/30
interface Ethernet1/31
interface Ethernet1/32
interface Ethernet1/33
interface Ethernet1/34
interface Ethernet1/35
interface Ethernet1/36
interface Ethernet1/37
interface Ethernet1/38
interface Ethernet1/39
interface Ethernet1/40
interface Ethernet1/41
interface Ethernet1/42
interface Ethernet1/43
interface Ethernet1/44
interface Ethernet1/45
interface Ethernet1/46
interface Ethernet1/47
interface Ethernet1/48
interface Ethernet1/49
interface Ethernet1/50
interface Ethernet1/51
interface Ethernet1/52
interface Ethernet1/53
interface Ethernet1/54
interface mgmt0""",
 'show interface link':"""^
Invalid interface format at '^' marker.""",
 'show interface':"""mgmt0 is up
admin state is up,
  Hardware: GigabitEthernet, address: 9077.ee01.bf00 (bia 9077.ee01.bf00)
  Description: key:dx1-079:g1/0/placeholder
  Internet Address is 172.30.0.151/25
  MTU 1500 bytes, BW 1000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  full-duplex, 1000 Mb/s
  Auto-Negotiation is turned on
  Auto-mdix is turned off
  EtherType is 0x0000 
  1 minute input rate 5936 bits/sec, 4 packets/sec
  1 minute output rate 8272 bits/sec, 2 packets/sec
  Rx
    173092457 input packets 154409439 unicast packets 18538038 multicast packets
    144980 broadcast packets 27285140990 bytes
  Tx
    154523343 output packets 154406273 unicast packets 117063 multicast packets
    7 broadcast packets 33760749674 bytes

Ethernet1/1 is down (XCVR not inserted)
admin state is down, Dedicated Interface
  Hardware: 100/1000/10000/25000 Ethernet, address: 9077.ee01.bf07 (bia 9077.ee01.bf08)
  MTU 1500 bytes, BW 25000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is auto
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 0 bits/sec, 0 packets/sec
    30 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 0 bits/sec, 0 packets/sec
    300 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    4 unicast packets  0 multicast packets  0 broadcast packets
    4 input packets  2452 bytes
    0 jumbo packets  0 storm suppression bytes
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    4 unicast packets  0 multicast packets  0 broadcast packets
    4 output packets  2452 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/2 is down (XCVR not inserted)
admin state is down, Dedicated Interface
  Hardware: 100/1000/10000/25000 Ethernet, address: 9077.ee01.bf07 (bia 9077.ee01.bf09)
  MTU 1500 bytes, BW 25000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is auto
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 0 bits/sec, 0 packets/sec
    30 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 0 bits/sec, 0 packets/sec
    300 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    4 unicast packets  0 multicast packets  0 broadcast packets
    4 input packets  2452 bytes
    0 jumbo packets  0 storm suppression bytes
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    4 unicast packets  0 multicast packets  0 broadcast packets
    4 output packets  2452 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/3 is down (XCVR not inserted)
admin state is down, Dedicated Interface
  Hardware: 100/1000/10000/25000 Ethernet, address: 9077.ee01.bf07 (bia 9077.ee01.bf0a)
  Description: BAD PORT
  MTU 1500 bytes, BW 25000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is auto
  Last link flapped 10week(s) 5day(s)
  Last clearing of "" counters never
  1 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 0 bits/sec, 0 packets/sec
    30 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 0 bits/sec, 0 packets/sec
    300 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    40967750 unicast packets  0 multicast packets  123 broadcast packets
    40967873 input packets  34659725194 bytes
    0 jumbo packets  0 storm suppression bytes
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    37925553 unicast packets  1135944 multicast packets  1892616 broadcast packets
    40954113 output packets  52274621954 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/4 is down (XCVR not inserted)
admin state is down, Dedicated Interface
  Hardware: 100/1000/10000/25000 Ethernet, address: 9077.ee01.bf07 (bia 9077.ee01.bf0b)
  MTU 1500 bytes, BW 25000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is auto
  Last link flapped 6week(s) 5day(s)
  Last clearing of "" counters never
  1 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 0 bits/sec, 0 packets/sec
    30 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 0 bits/sec, 0 packets/sec
    300 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX[K
    6883438 unicast packets  0 multicast packets  19694 broadcast packets
    6903132 input packets  3446657527 bytes
    0 jumbo packets  0 storm suppression bytes
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    6204287 unicast packets  6200267 multicast packets  8923172 broadcast packets
    21327726 output packets  4198639025 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/5 is up
admin state is up, Dedicated Interface
  Hardware: 100/1000/10000/25000 Ethernet, address: 9077.ee01.bf0c (bia 9077.ee01.bf0c)
  Description: bus-tegile3-ix2
  MTU 9216 bytes, BW 10000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is access
  full-duplex, 10 Gb/s, media type is 10G
  Beacon is turned off
  Auto-Negotiation is turned on  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Rate mode is dedicated
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is off
  Last link flapped 3d04h
  Last clearing of "" counters 6w5d
  7 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 496 bits/sec, 0 packets/sec
    30 seconds output rate 4648 bits/sec, 3 packets/sec
    input rate 496 bps, 0 pps; output rate 4.65 Kbps, 3 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 248 bits/sec, 0 packets/sec
    300 seconds output rate 4464 bits/sec, 2 packets/sec
    input rate 248 bps, 0 pps; output rate 4.46 Kbps, 2 pps
  RX
    851526865 unicast packets  0 multicast packets  15897 broadcast packets
    851545459 input packets  1169002348719 bytes
    2697 jumbo packets  0 storm suppression bytes
    0 runts  2697 giants  0 CRC  0 no buffer
    2697 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    35254667 unicast packets  4860559 multicast packets  13666444 broadcast packets
    53781670 output packets  96412445700 bytes
    11010207 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/6 is up
admin state is up, Dedicated Interface
  Hardware: 100/1000/10000/25000 Ethernet, address: 9077.ee01.bf0d (bia 9077.ee01.bf0d)
  Description: bus-tegile3-ix3
  MTU 9216 bytes, BW 10000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is access
  full-duplex, 10 Gb/s, media type is 10G
  Beacon is turned off
  Auto-Negotiation is turned on  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Rate mode is dedicated
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is off
  Last link flapped 3d04h
  Last clearing of "" counters 6w5d
  7 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 720 bits/sec, 1 packets/sec
    30 seconds output rate 3208 bits/sec, 3 packets/sec
    input rate 720 bps, 1 pps; output rate 3.21 Kbps, 3 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 1064 bits/sec, 1 packets/sec
    300 seconds output rate 3504 bits/sec, 1 packets/sec
    input rate 1.06 Kbps, 1 pps; output rate 3.50 Kbps, 1 pps
  RX
    82586624 unicast packets  0 multicast packets  2214 broadcast packets
    82590382 input packets  556350263728 bytes
    65485565 jumbo packets  0 storm suppression bytes
    0 runts  1544 giants  0 CRC  0 no buffer
    1544 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    220291552 unicast packets  4856048 multicast packets  13673899 broadcast packets
    238821650 output packets  284325275419 bytes
    7355320 jumbo packets
    151 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/7 is up
admin state is up, Dedicated Interface
  Hardware: 100/1000/10000/25000 Ethernet, address: 9077.ee01.bf0e (bia 9077.ee01.bf0e)
  Description: bus-tegile4-ix2
  MTU 9216 bytes, BW 10000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is access
  full-duplex, 10 Gb/s, media type is 10G
  Beacon is turned off
  Auto-Negotiation is turned on  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Rate mode is dedicated
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is off
  Last link flapped 3d04h
  Last clearing of "" counters 6w5d
  7 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 0 bits/sec, 0 packets/sec
    30 seconds output rate 3336 bits/sec, 2 packets/sec
    input rate 0 bps, 0 pps; output rate 3.34 Kbps, 2 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 0 bits/sec, 0 packets/sec
    300 seconds output rate 2968 bits/sec, 1 packets/sec
    input rate 0 bps, 0 pps; output rate 2.97 Kbps, 1 pps
  RX
    341579 unicast packets  0 multicast packets  8744 broadcast packets
    350840 input packets  187430748 bytes
    517 jumbo packets  0 storm suppression bytes
    0 runts  517 giants  0 CRC  0 no buffer
    517 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    985579 unicast packets  4859809 multicast packets  13671530 broadcast packets
    19516918 output packets  1599088063 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/8 is up
admin state is up, Dedicated Interface
  Hardware: 100/1000/10000/25000 Ethernet, address: 9077.ee01.bf0f (bia 9077.ee01.bf0f)
  Description: bus-tegile4-ix3
  MTU 9216 bytes, BW 10000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is access
  full-duplex, 10 Gb/s, media type is 10G
  Beacon is turned off
  Auto-Negotiation is turned on  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Rate mode is dedicated
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is off
  Last link flapped 3d04h
  Last clearing of "" counters 6w5d
  8 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 0 bits/sec, 0 packets/sec
    30 seconds output rate 3336 bits/sec, 2 packets/sec
    input rate 0 bps, 0 pps; output rate 3.34 Kbps, 2 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 0 bits/sec, 0 packets/sec
    300 seconds output rate 2984 bits/sec, 1 packets/sec
    input rate 0 bps, 0 pps; output rate 2.98 Kbps, 1 pps
  RX
    125851 unicast packets  0 multicast packets  217 broadcast packets
    126872 input packets  32310322 bytes
    804 jumbo packets  0 storm suppression bytes
    0 runts  804 giants  0 CRC  0 no buffer
    804 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    1028293 unicast packets  4855609 multicast packets  13674942 broadcast packets
    19558844 output packets  1644861175 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/9 is up
admin state is up, Dedicated Interface
  Hardware: 100/1000/10000/25000 Ethernet, address: 9077.ee01.bf10 (bia 9077.ee01.bf10)
  Description: esxsrv21 Dell R740 vmnic0 -| WPort 2055 |-
  MTU 9216 bytes, BW 25000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is access
  full-duplex, 25 Gb/s, media type is 25G
  Beacon is turned off
  Auto-Negotiation is turned off  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Rate mode is dedicated
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is Fc-fec
  Last link flapped 11week(s) 2day(s)
  Last clearing of "" counters never
  5 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 168 bits/sec, 0 packets/sec
    30 seconds output rate 3128 bits/sec, 2 packets/sec
    input rate 168 bps, 0 pps; output rate 3.13 Kbps, 2 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 24 bits/sec, 0 packets/sec
    300 seconds output rate 3016 bits/sec, 1 packets/sec
    input rate 24 bps, 0 pps; output rate 3.02 Kbps, 1 pps
  RX
    12 unicast packets  284660 multicast packets  84 broadcast packets
    284756 input packets  21647143 bytes
    0 jumbo packets  0 storm suppression bytes
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    1129667 unicast packets  14018188 multicast packets  27695246 broadcast packets
    42843101 output packets  3598078387 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/10 is up
admin state is up, Dedicated Interface
  Hardware: 100/1000/10000/25000 Ethernet, address: 9077.ee01.bf11 (bia 9077.ee01.bf11)
  Description: esxsrv21 Dell R740 vmnic1 -| WPort 2056 |-
  MTU 9216 bytes, BW 25000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is access
  full-duplex, 25 Gb/s, media type is 25G
  Beacon is turned off
  Auto-Negotiation is turned off  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Rate mode is dedicated
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is Fc-fec
  Last link flapped 6week(s) 0day(s)
  Last clearing of "" counters never
  6 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 73912 bits/sec, 1 packets/sec
    30 seconds output rate 10600 bits/sec, 5 packets/sec
    input rate 73.91 Kbps, 1 pps; output rate 10.60 Kbps, 5 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 118896 bits/sec, 1 packets/sec
    300 seconds output rate 35192 bits/sec, 3 packets/sec
    input rate 118.90 Kbps, 1 pps; output rate 35.19 Kbps, 3 pps
  RX
    5453610349 unicast packets  284552 multicast packets  154370 broadcast packets
    5454049309 input packets  7381704696456 bytes
    1308738 jumbo packets  0 storm suppression bytes
    0 runts  38 giants  0 CRC  0 no buffer
    38 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    6262073449 unicast packets  14013412 multicast packets  27533240 broadcast packets
    6303620101 output packets  6025815617664 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/11 is up
admin state is up, Dedicated Interface
  Hardware: 100/1000/10000/25000 Ethernet, address: 9077.ee01.bf12 (bia 9077.ee01.bf12)
  Description: dell esxsrv24
  MTU 1500 bytes, BW 25000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is trunk
  full-duplex, 25 Gb/s, media type is 25G
  Beacon is turned off
  Auto-Negotiation is turned off  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Rate mode is dedicated
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is Fc-fec
  Last link flapped 6week(s) 0day(s)
  Last clearing of "" counters never
  5 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 520 bits/sec, 0 packets/sec
    30 seconds output rate 413864 bits/sec, 683 packets/sec
    input rate 520 bps, 0 pps; output rate 413.86 Kbps, 683 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 400 bits/sec, 0 packets/sec
    300 seconds output rate 493344 bits/sec, 747 packets/sec
    input rate 400 bps, 0 pps; output rate 493.34 Kbps, 747 pps
  RX
    8966037801 unicast packets  22066293 multicast packets  6575418 broadcast packets
    8994679512 input packets  11497145516368 bytes
    7279884993 jumbo packets  0 storm suppression bytes
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    13029032088 unicast packets  316876530 multicast packets  514671466 broadcast packets
    13860580084 output packets  11041147099782 bytes
    6680635721 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/12 is down (Administratively down)
admin state is down, Dedicated Interface
  Hardware: 100/1000/10000/25000 Ethernet, address: 9077.ee01.bf07 (bia 9077.ee01.bf13)
  Description: BROKEN
  MTU 1500 bytes, BW 25000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed, media type is 25G
  Beacon is turned off
  Auto-Negotiation is turned off  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Rate mode is dedicated
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is auto
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 0 bits/sec, 0 packets/sec
    30 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 0 bits/sec, 0 packets/sec
    300 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    4 unicast packets  0 multicast packets  0 broadcast packets
    4 input packets  2452 bytes
    0 jumbo packets  0 storm suppression bytes
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    4 unicast packets  0 multicast packets  0 broadcast packets
    4 output packets  2452 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/13 is down (XCVR not inserted)
admin state is up, Dedicated Interface
  Hardware: 100/1000/10000/25000 Ethernet, address: 9077.ee01.bf14 (bia 9077.ee01.bf14)
  Description: bus-backup
  MTU 1500 bytes, BW 25000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is access
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is auto
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 0 bits/sec, 0 packets/sec
    30 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 0 bits/sec, 0 packets/sec
    300 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    4 unicast packets  0 multicast packets  0 broadcast packets
    4 input packets  2452 bytes
    0 jumbo packets  0 storm suppression bytes
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    4 unicast packets  0 multicast packets  0 broadcast packets
    4 output packets  2452 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/14 is down (XCVR not inserted)
admin state is down, Dedicated Interface
  Hardware: 100/1000/10000/25000 Ethernet, address: 9077.ee01.bf07 (bia 9077.ee01.bf15)
  MTU 1500 bytes, BW 25000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is auto
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 0 bits/sec, 0 packets/sec
    30 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 0 bits/sec, 0 packets/sec
    300 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    4 unicast packets  0 multicast packets  0 broadcast packets
    4 input packets  2452 bytes
    0 jumbo packets  0 storm suppression bytes
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    4 unicast packets  0 multicast packets  0 broadcast packets
    4 output packets  2452 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/15 is down (XCVR not inserted)
admin state is up, Dedicated Interface
  Hardware: 100/1000/10000/25000 Ethernet, address: 9077.ee01.bf16 (bia 9077.ee01.bf16)
  Description: Infortrend ISCSI 1 TEMPORARY
  MTU 1500 bytes, BW 25000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is access
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is auto
  Last link flapped 6week(s) 5day(s)
  Last clearing of "" counters never
  1 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 0 bits/sec, 0 packets/sec
    30 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 0 bits/sec, 0 packets/sec
    300 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    965 unicast packets  0 multicast packets  20 broadcast packets
    985 input packets  149198 bytes
    0 jumbo packets  0 storm suppression bytes
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    1876 unicast packets  6004 multicast packets  7969 broadcast packets
    15849 output packets  1301746 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/16 is down (XCVR not inserted)
admin state is up, Dedicated Interface
  Hardware: 100/1000/10000/25000 Ethernet, address: 9077.ee01.bf17 (bia 9077.ee01.bf17)
  Description: Infortrend ISCSI 3 TEMPORARY
  MTU 1500 bytes, BW 25000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is access
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is auto
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 0 bits/sec, 0 packets/sec
    30 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 0 bits/sec, 0 packets/sec
    300 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    4 unicast packets  0 multicast packets  0 broadcast packets
    4 input packets  2452 bytes
    0 jumbo packets  0 storm suppression bytes
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    4 unicast packets  0 multicast packets  0 broadcast packets
    4 output packets  2452 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/17 is down (XCVR not inserted)
admin state is up, Dedicated Interface
  Hardware: 100/1000/10000/25000 Ethernet, address: 9077.ee01.bf18 (bia 9077.ee01.bf18)
  Description: Infortrend ISCSI 1 TEMPORARY
  MTU 1500 bytes, BW 25000000 Kbit , DLY 10 usec
  reliability 246/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is access
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is auto
  Last link flapped 6week(s) 5day(s)
  Last clearing of "" counters never
  2 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 0 bits/sec, 0 packets/sec
    30 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 0 bits/sec, 0 packets/sec
    300 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX[K
    3874 unicast packets  0 multicast packets  11 broadcast packets
    4720 input packets  2351144 bytes
    835 jumbo packets  0 storm suppression bytes
    0 runts  835 giants  0 CRC  0 no buffer
    835 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    5529 unicast packets  5694 multicast packets  7636 broadcast packets
    18855 output packets  1671106 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/18 is down (XCVR not inserted)
admin state is up, Dedicated Interface
  Hardware: 100/1000/10000/25000 Ethernet, address: 9077.ee01.bf19 (bia 9077.ee01.bf19)
  Description: Infortrend ISCSI 1 TEMPORARY
  MTU 1500 bytes, BW 25000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is access
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is auto
  Last link flapped 6week(s) 5day(s)
  Last clearing of "" counters never
  1 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 0 bits/sec, 0 packets/sec
    30 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 0 bits/sec, 0 packets/sec
    300 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    932 unicast packets  0 multicast packets  18 broadcast packets
    956 input packets  156540 bytes
    6 jumbo packets  0 storm suppression bytes
    0 runts  6 giants  0 CRC  0 no buffer
    6 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    1810 unicast packets  5597 multicast packets  7518 broadcast packets
    14921 output packets  1221886 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/19 is up
admin state is up, Dedicated Interface
  Belongs to Po11
  Hardware: 100/1000/10000/25000 Ethernet, address: 9077.ee01.bf1a (bia 9077.ee01.bf1a)
  Description: IBM_Flex_CH2SW2 | TS 5/27/21
  MTU 1500 bytes, BW 10000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is trunk
  full-duplex, 10 Gb/s, media type is 10G
  Beacon is turned off
  Auto-Negotiation is turned on  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Rate mode is dedicated
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is off
  Last link flapped 4week(s) 1day(s)
  Last clearing of "" counters never
  4 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 2488 bits/sec, 3 packets/sec
    30 seconds output rate 249904 bits/sec, 421 packets/sec
    input rate 2.49 Kbps, 3 pps; output rate 249.90 Kbps, 421 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 2336 bits/sec, 3 packets/sec
    300 seconds output rate 330840 bits/sec, 506 packets/sec
    input rate 2.34 Kbps, 3 pps; output rate 330.84 Kbps, 506 pps
  RX
    4656586696 unicast packets  82397988 multicast packets  8337532 broadcast packets
    4747322216 input packets  3996441562327 bytes
    2187606376 jumbo packets  0 storm suppression bytes
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    10397425664 unicast packets  245347165 multicast packets  371873414 broadcast packets
    11014646243 output packets  9113902179885 bytes
    5103711892 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/20 is up
admin state is up, Dedicated Interface
  Belongs to Po11
  Hardware: 100/1000/10000/25000 Ethernet, address: 9077.ee01.bf1b (bia 9077.ee01.bf1b)
  Description: IBM_Flex_CH2SW2 | TS 5/27/21
  MTU 1500 bytes, BW 10000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is trunk
  full-duplex, 10 Gb/s, media type is 10G
  Beacon is turned off
  Auto-Negotiation is turned on  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Rate mode is dedicated
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is off
  Last link flapped 4week(s) 1day(s)
  Last clearing of "" counters never
  5 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 3648 bits/sec, 1 packets/sec
    30 seconds output rate 167304 bits/sec, 259 packets/sec
    input rate 3.65 Kbps, 1 pps; output rate 167.30 Kbps, 259 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 11536 bits/sec, 7 packets/sec
    300 seconds output rate 174528 bits/sec, 199 packets/sec
    input rate 11.54 Kbps, 7 pps; output rate 174.53 Kbps, 199 pps
  RX
    9077969917 unicast packets  4006885 multicast packets  4320320 broadcast packets
    9086297122 input packets  7442914442642 bytes
    3617127476 jumbo packets  0 storm suppression bytes
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    16297922457 unicast packets  99136656 multicast packets  144996958 broadcast packets
    16542056071 output packets  7072057068831 bytes
    3460358953 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/21 is down (XCVR not inserted)
admin state is up, Dedicated Interface
  Belongs to Po12
  Hardware: 100/1000/10000/25000 Ethernet, address: 9077.ee01.bf1c (bia 9077.ee01.bf1c)
  Description: IBM_Flex_CH2SW1
  MTU 9216 bytes, BW 25000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is trunk
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is auto
  Last link flapped 6week(s) 5day(s)
  Last clearing of "" counters 6w5d
  13 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 0 bits/sec, 0 packets/sec
    30 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 0 bits/sec, 0 packets/sec
    300 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    31888 unicast packets  280 multicast packets  129 broadcast packets
    32441 input packets  20499438 bytes
    9990 jumbo packets  0 storm suppression bytes
    0 runts  144 giants  0 CRC  0 no buffer
    144 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    42517 unicast packets  333 multicast packets  206 broadcast packets
    43074 output packets  21991305 bytes
    18 jumbo packets
    18 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/22 is down (XCVR not inserted)
admin state is up, Dedicated Interface
  Belongs to Po12
  Hardware: 100/1000/10000/25000 Ethernet, address: 9077.ee01.bf1d (bia 9077.ee01.bf1d)
  Description: IBM_Flex_CH2SW1
  MTU 9216 bytes, BW 25000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is trunk
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is auto
  Last link flapped 6week(s) 5day(s)
  Last clearing of "" counters 6w5d
  13 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 0 bits/sec, 0 packets/sec
    30 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 0 bits/sec, 0 packets/sec
    300 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    71234 unicast packets  219 multicast packets  111 broadcast packets
    71571 input packets  20034329 bytes
    161 jumbo packets  0 storm suppression bytes
    0 runts  7 giants  0 CRC  0 no buffer
    7 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    61408 unicast packets  747 multicast packets  555 broadcast packets
    62744 output packets  28842848 bytes
    6365 jumbo packets
    34 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/23 is down (XCVR not inserted)
admin state is down, Dedicated Interface
  Hardware: 100/1000/10000/25000 Ethernet, address: 9077.ee01.bf1e (bia 9077.ee01.bf1e)
  Description: IBM_Flex_CH2SW2
  MTU 1500 bytes, BW 25000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is trunk
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is auto
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 0 bits/sec, 0 packets/sec
    30 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 0 bits/sec, 0 packets/sec
    300 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    4 unicast packets  0 multicast packets  0 broadcast packets
    4 input packets  2452 bytes
    0 jumbo packets  0 storm suppression bytes
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    4 unicast packets  0 multicast packets  0 broadcast packets
    4 output packets  2452 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/24 is down (XCVR not inserted)
admin state is down, Dedicated Interface
  Hardware: 100/1000/10000/25000 Ethernet, address: 9077.ee01.bf1f (bia 9077.ee01.bf1f)
  Description: IBM_Flex_CH2SW2
  MTU 1500 bytes, BW 25000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is trunk
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is auto
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 0 bits/sec, 0 packets/sec
    30 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 0 bits/sec, 0 packets/sec
    300 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    4 unicast packets  0 multicast packets  0 broadcast packets
    4 input packets  2452 bytes
    0 jumbo packets  0 storm suppression bytes
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    4 unicast packets  0 multicast packets  0 broadcast packets
    4 output packets  2452 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/25 is up
admin state is up, Dedicated Interface
  Hardware: 100/1000/10000/25000 Ethernet, address: 9077.ee01.bf20 (bia 9077.ee01.bf20)
  Description: dell esxsrv24
  MTU 1500 bytes, BW 25000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is trunk
  full-duplex, 25 Gb/s, media type is 25G
  Beacon is turned off
  Auto-Negotiation is turned off  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Rate mode is dedicated
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is Fc-fec
  Last link flapped 6week(s) 0day(s)
  Last clearing of "" counters never
  4 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 32 bits/sec, 0 packets/sec
    30 seconds output rate 413760 bits/sec, 684 packets/sec
    input rate 32 bps, 0 pps; output rate 413.76 Kbps, 684 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 24 bits/sec, 0 packets/sec
    300 seconds output rate 493080 bits/sec, 746 packets/sec
    input rate 24 bps, 0 pps; output rate 493.08 Kbps, 746 pps
  RX
    283451551 unicast packets  1115104 multicast packets  655570 broadcast packets
    285222225 input packets  86227292284 bytes
    5857435 jumbo packets  0 storm suppression bytes
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    4610257034 unicast packets  339944967 multicast packets  520536171 broadcast packets
    5470738172 output packets  954477441794 bytes
    333667202 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/26 is down (XCVR not inserted)
admin state is down, Dedicated Interface
  Hardware: 100/1000/10000/25000 Ethernet, address: 9077.ee01.bf07 (bia 9077.ee01.bf21)
  MTU 1500 bytes, BW 25000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is auto
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 0 bits/sec, 0 packets/sec
    30 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 0 bits/sec, 0 packets/sec
    300 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    4 unicast packets  0 multicast packets  0 broadcast packets
    4 input packets  2452 bytes
    0 jumbo packets  0 storm suppression bytes
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    4 unicast packets  0 multicast packets  0 broadcast packets
    4 output packets  2452 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/27 is down (XCVR not inserted)
admin state is down, Dedicated Interface
  Hardware: 100/1000/10000/25000 Ethernet, address: 9077.ee01.bf07 (bia 9077.ee01.bf22)
  MTU 1500 bytes, BW 25000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is auto
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 0 bits/sec, 0 packets/sec
    30 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 0 bits/sec, 0 packets/sec
    300 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    4 unicast packets  0 multicast packets  0 broadcast packets
    4 input packets  2452 bytes
    0 jumbo packets  0 storm suppression bytes
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    4 unicast packets  0 multicast packets  0 broadcast packets
    4 output packets  2452 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/28 is down (XCVR not inserted)
admin state is down, Dedicated Interface
  Hardware: 100/1000/10000/25000 Ethernet, address: 9077.ee01.bf07 (bia 9077.ee01.bf23)
  MTU 1500 bytes, BW 25000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is auto
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 0 bits/sec, 0 packets/sec
    30 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 0 bits/sec, 0 packets/sec
    300 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    4 unicast packets  0 multicast packets  0 broadcast packets
    4 input packets  2452 bytes
    0 jumbo packets  0 storm suppression bytes
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    4 unicast packets  0 multicast packets  0 broadcast packets
    4 output packets  2452 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/29 is down (XCVR not inserted)
admin state is down, Dedicated Interface
  Hardware: 100/1000/10000/25000 Ethernet, address: 9077.ee01.bf07 (bia 9077.ee01.bf24)
  MTU 1500 bytes, BW 25000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is auto
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 0 bits/sec, 0 packets/sec
    30 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 0 bits/sec, 0 packets/sec
    300 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 input packets  0 bytes
    0 jumbo packets  0 storm suppression bytes
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 output packets  0 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/30 is down (XCVR not inserted)
admin state is down, Dedicated Interface
  Hardware: 100/1000/10000/25000 Ethernet, address: 9077.ee01.bf07 (bia 9077.ee01.bf25)
  MTU 1500 bytes, BW 25000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is auto
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 0 bits/sec, 0 packets/sec
    30 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 0 bits/sec, 0 packets/sec
    300 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 input packets  0 bytes
    0 jumbo packets  0 storm suppression bytes
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 output packets  0 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/31 is down (XCVR not inserted)
admin state is down, Dedicated Interface
  Hardware: 100/1000/10000/25000 Ethernet, address: 9077.ee01.bf07 (bia 9077.ee01.bf26)
  MTU 1500 bytes, BW 25000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is auto
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 0 bits/sec, 0 packets/sec
    30 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 0 bits/sec, 0 packets/sec
    300 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 input packets  0 bytes
    0 jumbo packets  0 storm suppression bytes
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 output packets  0 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/32 is down (XCVR not inserted)
admin state is down, Dedicated Interface
  Hardware: 100/1000/10000/25000 Ethernet, address: 9077.ee01.bf07 (bia 9077.ee01.bf27)
  MTU 1500 bytes, BW 25000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is auto
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 0 bits/sec, 0 packets/sec
    30 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 0 bits/sec, 0 packets/sec
    300 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 input packets  0 bytes
    0 jumbo packets  0 storm suppression bytes
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 output packets  0 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/33 is down (XCVR not inserted)
admin state is down, Dedicated Interface
  Hardware: 100/1000/10000/25000 Ethernet, address: 9077.ee01.bf07 (bia 9077.ee01.bf28)
  MTU 1500 bytes, BW 25000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is auto
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 0 bits/sec, 0 packets/sec
    30 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 0 bits/sec, 0 packets/sec
    300 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 input packets  0 bytes
    0 jumbo packets  0 storm suppression bytes
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 output packets  0 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/34 is down (XCVR not inserted)
admin state is down, Dedicated Interface
  Hardware: 100/1000/10000/25000 Ethernet, address: 9077.ee01.bf07 (bia 9077.ee01.bf29)
  MTU 1500 bytes, BW 25000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is auto
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 0 bits/sec, 0 packets/sec
    30 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 0 bits/sec, 0 packets/sec
    300 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 input packets  0 bytes
    0 jumbo packets  0 storm suppression bytes
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 output packets  0 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/35 is down (XCVR not inserted)
admin state is down, Dedicated Interface
  Hardware: 100/1000/10000/25000 Ethernet, address: 9077.ee01.bf07 (bia 9077.ee01.bf2a)
  MTU 1500 bytes, BW 25000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is auto
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 0 bits/sec, 0 packets/sec
    30 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 0 bits/sec, 0 packets/sec
    300 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 input packets  0 bytes
    0 jumbo packets  0 storm suppression bytes
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 output packets  0 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/36 is down (XCVR not inserted)
admin state is down, Dedicated Interface
  Hardware: 100/1000/10000/25000 Ethernet, address: 9077.ee01.bf07 (bia 9077.ee01.bf2b)
  MTU 1500 bytes, BW 25000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is auto
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 0 bits/sec, 0 packets/sec
    30 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 0 bits/sec, 0 packets/sec
    300 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 input packets  0 bytes
    0 jumbo packets  0 storm suppression bytes
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 output packets  0 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/37 is down (XCVR not inserted)
admin state is down, Dedicated Interface
  Hardware: 100/1000/10000/25000 Ethernet, address: 9077.ee01.bf07 (bia 9077.ee01.bf2c)
  MTU 1500 bytes, BW 25000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is auto
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 0 bits/sec, 0 packets/sec
    30 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 0 bits/sec, 0 packets/sec
    300 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 input packets  0 bytes
    0 jumbo packets  0 storm suppression bytes
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 output packets  0 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/38 is down (XCVR not inserted)
admin state is down, Dedicated Interface
  Hardware: 100/1000/10000/25000 Ethernet, address: 9077.ee01.bf07 (bia 9077.ee01.bf2d)
  MTU 1500 bytes, BW 25000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is auto
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 0 bits/sec, 0 packets/sec
    30 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 0 bits/sec, 0 packets/sec
    300 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 input packets  0 bytes
    0 jumbo packets  0 storm suppression bytes
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 output packets  0 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/39 is down (XCVR not inserted)
admin state is down, Dedicated Interface
  Hardware: 100/1000/10000/25000 Ethernet, address: 9077.ee01.bf07 (bia 9077.ee01.bf2e)
  MTU 1500 bytes, BW 25000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is auto
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 0 bits/sec, 0 packets/sec
    30 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 0 bits/sec, 0 packets/sec
    300 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 input packets  0 bytes
    0 jumbo packets  0 storm suppression bytes
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 output packets  0 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/40 is down (XCVR not inserted)
admin state is down, Dedicated Interface
  Hardware: 100/1000/10000/25000 Ethernet, address: 9077.ee01.bf07 (bia 9077.ee01.bf2f)
  MTU 1500 bytes, BW 25000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is auto
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 0 bits/sec, 0 packets/sec
    30 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 0 bits/sec, 0 packets/sec
    300 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 input packets  0 bytes
    0 jumbo packets  0 storm suppression bytes
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 output packets  0 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/41 is down (XCVR not inserted)
admin state is down, Dedicated Interface
  Hardware: 100/1000/10000/25000 Ethernet, address: 9077.ee01.bf07 (bia 9077.ee01.bf30)
  MTU 1500 bytes, BW 25000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is auto
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 0 bits/sec, 0 packets/sec
    30 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 0 bits/sec, 0 packets/sec
    300 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 input packets  0 bytes
    0 jumbo packets  0 storm suppression bytes
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 output packets  0 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/42 is down (XCVR not inserted)
admin state is down, Dedicated Interface
  Hardware: 100/1000/10000/25000 Ethernet, address: 9077.ee01.bf07 (bia 9077.ee01.bf31)
  MTU 1500 bytes, BW 25000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is auto
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 0 bits/sec, 0 packets/sec
    30 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 0 bits/sec, 0 packets/sec
    300 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 input packets  0 bytes
    0 jumbo packets  0 storm suppression bytes
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 output packets  0 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/43 is down (XCVR not inserted)
admin state is down, Dedicated Interface
  Hardware: 100/1000/10000/25000 Ethernet, address: 9077.ee01.bf07 (bia 9077.ee01.bf32)
  MTU 1500 bytes, BW 25000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is auto
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 0 bits/sec, 0 packets/sec
    30 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 0 bits/sec, 0 packets/sec
    300 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 input packets  0 bytes
    0 jumbo packets  0 storm suppression bytes
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 output packets  0 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/44 is down (XCVR not inserted)
admin state is down, Dedicated Interface
  Hardware: 100/1000/10000/25000 Ethernet, address: 9077.ee01.bf07 (bia 9077.ee01.bf33)
  MTU 1500 bytes, BW 25000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is auto
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 0 bits/sec, 0 packets/sec
    30 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 0 bits/sec, 0 packets/sec
    300 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 input packets  0 bytes
    0 jumbo packets  0 storm suppression bytes
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 output packets  0 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/45 is down (XCVR not inserted)
admin state is down, Dedicated Interface
  Hardware: 100/1000/10000/25000 Ethernet, address: 9077.ee01.bf07 (bia 9077.ee01.bf34)
  MTU 1500 bytes, BW 25000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is auto
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 0 bits/sec, 0 packets/sec
    30 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 0 bits/sec, 0 packets/sec
    300 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 input packets  0 bytes
    0 jumbo packets  0 storm suppression bytes
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 output packets  0 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/46 is down (XCVR not inserted)
admin state is down, Dedicated Interface
  Hardware: 100/1000/10000/25000 Ethernet, address: 9077.ee01.bf07 (bia 9077.ee01.bf35)
  MTU 1500 bytes, BW 25000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is auto
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 0 bits/sec, 0 packets/sec
    30 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 0 bits/sec, 0 packets/sec
    300 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 input packets  0 bytes
    0 jumbo packets  0 storm suppression bytes
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 output packets  0 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/47 is down (XCVR not inserted)
admin state is down, Dedicated Interface
  Hardware: 100/1000/10000/25000 Ethernet, address: 9077.ee01.bf07 (bia 9077.ee01.bf36)
  MTU 1500 bytes, BW 25000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is auto
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 0 bits/sec, 0 packets/sec
    30 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 0 bits/sec, 0 packets/sec
    300 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 input packets  0 bytes
    0 jumbo packets  0 storm suppression bytes
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 output packets  0 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/48 is down (XCVR not inserted)
admin state is down, Dedicated Interface
  Hardware: 100/1000/10000/25000 Ethernet, address: 9077.ee01.bf07 (bia 9077.ee01.bf37)
  MTU 1500 bytes, BW 25000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is auto
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 0 bits/sec, 0 packets/sec
    30 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 0 bits/sec, 0 packets/sec
    300 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 input packets  0 bytes
    0 jumbo packets  0 storm suppression bytes
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 output packets  0 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/49 is up
admin state is up, Dedicated Interface
  Hardware: 1000/10000/25000/40000/50000/100000 Ethernet, address: 9077.ee01.bf38 (bia 9077.ee01.bf38)
  MTU 9216 bytes, BW 40000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is trunk
  full-duplex, 40 Gb/s, media type is 40G
  Beacon is turned off
  Auto-Negotiation is turned on  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Rate mode is dedicated
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is off
  Last link flapped 11week(s) 4day(s)
  Last clearing of "" counters never
  1 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 777728 bits/sec, 965 packets/sec
    30 seconds output rate 69888 bits/sec, 4 packets/sec
    input rate 777.73 Kbps, 965 pps; output rate 69.89 Kbps, 4 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 894608 bits/sec, 1046 packets/sec
    300 seconds output rate 128440 bits/sec, 1 packets/sec
    input rate 894.61 Kbps, 1.05 Kpps; output rate 128.44 Kbps, 1 pps
  RX
    42041886408 unicast packets  1868773774 multicast packets  869154150 broadcast packets
    44779814332 input packets  33229200854098 bytes
    18880837667 jumbo packets  0 storm suppression bytes
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    28716481914 unicast packets  33977182 multicast packets  20264223 broadcast packets
    28770723319 output packets  31213939785652 bytes
    17856285721 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/50 is down (XCVR not inserted)
admin state is down, Dedicated Interface
  Hardware: 1000/10000/25000/40000/50000/100000 Ethernet, address: 9077.ee01.bf07 (bia 9077.ee01.bf3c)
  MTU 1500 bytes, BW 100000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is auto
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 0 bits/sec, 0 packets/sec
    30 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 0 bits/sec, 0 packets/sec
    300 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 input packets  0 bytes
    0 jumbo packets  0 storm suppression bytes
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 output packets  0 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/51 is down (XCVR not inserted)
admin state is down, Dedicated Interface
  Hardware: 1000/10000/25000/40000/50000/100000 Ethernet, address: 9077.ee01.bf07 (bia 9077.ee01.bf40)
  MTU 1500 bytes, BW 100000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is auto
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 0 bits/sec, 0 packets/sec
    30 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 0 bits/sec, 0 packets/sec
    300 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 input packets  0 bytes
    0 jumbo packets  0 storm suppression bytes
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 output packets  0 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/52 is down (XCVR not inserted)
admin state is down, Dedicated Interface
  Hardware: 1000/10000/25000/40000/50000/100000 Ethernet, address: 9077.ee01.bf07 (bia 9077.ee01.bf44)
  MTU 1500 bytes, BW 100000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is auto
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 0 bits/sec, 0 packets/sec
    30 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 0 bits/sec, 0 packets/sec
    300 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 input packets  0 bytes
    0 jumbo packets  0 storm suppression bytes
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 output packets  0 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/53 is down (XCVR not inserted)
admin state is down, Dedicated Interface
  Hardware: 1000/10000/25000/40000/50000/100000 Ethernet, address: 9077.ee01.bf07 (bia 9077.ee01.bf48)
  MTU 1500 bytes, BW 100000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is auto
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 0 bits/sec, 0 packets/sec
    30 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 0 bits/sec, 0 packets/sec
    300 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 input packets  0 bytes
    0 jumbo packets  0 storm suppression bytes
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 output packets  0 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/54 is down (XCVR not inserted)
admin state is down, Dedicated Interface
  Hardware: 1000/10000/25000/40000/50000/100000 Ethernet, address: 9077.ee01.bf07 (bia 9077.ee01.bf4c)
  MTU 1500 bytes, BW 100000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is auto
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 0 bits/sec, 0 packets/sec
    30 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 0 bits/sec, 0 packets/sec
    300 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 input packets  0 bytes
    0 jumbo packets  0 storm suppression bytes
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 output packets  0 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

port-channel11 is up
admin state is up,
  Hardware: Port-Channel, address: 9077.ee01.bf1a (bia 9077.ee01.bf1a)
  Description: IBM_Flex_CH1SW2
  MTU 1500 bytes, BW 20000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is trunk
  full-duplex, 10 Gb/s
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  Members in this channel: Eth1/19, Eth1/20
  Last clearing of "" counters never
  3 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 5664 bits/sec, 4 packets/sec
    30 seconds output rate 422344 bits/sec, 679 packets/sec
    input rate 5.66 Kbps, 4 pps; output rate 422.34 Kbps, 679 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 13752 bits/sec, 10 packets/sec
    300 seconds output rate 509648 bits/sec, 704 packets/sec
    input rate 13.75 Kbps, 10 pps; output rate 509.65 Kbps, 704 pps
  RX
    13734556614 unicast packets  86404881 multicast packets  12657852 broadcast packets
    13833619347 input packets  11439356005613 bytes
    5804733852 jumbo packets  0 storm suppression bytes
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    26695348943 unicast packets  344483917 multicast packets  516870521 broadcast packets
    27556703381 output packets  16185959338938 bytes
    8564070845 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

port-channel12 is down (No operational members)
admin state is up,
  Hardware: Port-Channel, address: 0000.0000.0000 (bia 0000.0000.0000)
  Description: IBM_Flex_CH2SW1
  MTU 9216 bytes, BW 100000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is trunk
  auto-duplex, auto-speed
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  Members in this channel: Eth1/21, Eth1/22
  Last clearing of "" counters never
  1 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 0 bits/sec, 0 packets/sec
    30 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 0 bits/sec, 0 packets/sec
    300 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    103122 unicast packets  499 multicast packets  240 broadcast packets
    104012 input packets  40533767 bytes
    10151 jumbo packets  0 storm suppression bytes
    0 runts  151 giants  0 CRC  0 no buffer
    151 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    103925 unicast packets  1080 multicast packets  761 broadcast packets
    105818 output packets  50834153 bytes
    6383 jumbo packets
    52 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

port-channel13 is down (No operational members)
admin state is up,
  Hardware: Port-Channel, address: 0000.0000.0000 (bia 0000.0000.0000)
  Description: IBM_Flex_CH2SW2
  MTU 1500 bytes, BW 100000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is trunk
  auto-duplex, auto-speed
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  No members
  Last clearing of "" counters never
  0 interface resets
  Load-Interval #1: 0 seconds
    0 seconds input rate 0 bits/sec, 0 packets/sec
    0 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 0 seconds
    0 seconds input rate 0 bits/sec, 0 packets/sec
    0 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 input packets  0 bytes
    0 jumbo packets  0 storm suppression bytes
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 output packets  0 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

port-channel16 is down (No operational members)
admin state is up,
  Hardware: Port-Channel, address: 0000.0000.0000 (bia 0000.0000.0000)
  Description: Infortrend Controller A
  MTU 9216 bytes, BW 100000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is access
  auto-duplex, auto-speed
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  No members
  Last clearing of "" counters never
  0 interface resets
  Load-Interval #1: 0 seconds
    0 seconds input rate 0 bits/sec, 0 packets/sec
    0 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 0 seconds
    0 seconds input rate 0 bits/sec, 0 packets/sec
    0 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 input packets  0 bytes
    0 jumbo packets  0 storm suppression bytes
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 output packets  0 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

port-channel20 is down (No operational members)
admin state is up,
  Hardware: Port-Channel, address: 0000.0000.0000 (bia 0000.0000.0000)
  Description: bus-filer02
  MTU 1500 bytes, BW 100000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is access
  auto-duplex, auto-speed
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  No members
  Last clearing of "" counters never
  0 interface resets
  Load-Interval #1: 0 seconds
    0 seconds input rate 0 bits/sec, 0 packets/sec
    0 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 0 seconds
    0 seconds input rate 0 bits/sec, 0 packets/sec
    0 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    8 unicast packets  0 multicast packets  0 broadcast packets
    8 input packets  4904 bytes
    0 jumbo packets  0 storm suppression bytes
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    8 unicast packets  0 multicast packets  0 broadcast packets
    8 output packets  4904 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

port-channel21 is down (No operational members)
admin state is up,
  Hardware: Port-Channel, address: 9077.ee01.bf0c (bia 9077.ee01.bf0c)
  Description: tegile1
  MTU 9216 bytes, BW 100000 Kbit , DLY 10 usec
  reliability 251/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is access
  auto-duplex, auto-speed
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  No members
  Last clearing of "" counters never
  0 interface resets
  Load-Interval #1: 0 seconds
    0 seconds input rate 0 bits/sec, 0 packets/sec
    0 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 0 seconds
    0 seconds input rate 0 bits/sec, 0 packets/sec
    0 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    297 unicast packets  0 multicast packets  73 broadcast packets
    380 input packets  49748 bytes
    10 jumbo packets  0 storm suppression bytes
    0 runts  10 giants  0 CRC  0 no buffer
    10 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    0 unicast packets  168 multicast packets  0 broadcast packets
    168 output packets  32496 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

port-channel22 is down (No operational members)
admin state is up,
  Hardware: Port-Channel, address: 9077.ee01.bf0e (bia 9077.ee01.bf0e)
  Description: tegile2
  MTU 9216 bytes, BW 100000 Kbit , DLY 10 usec
  reliability 242/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is access
  auto-duplex, auto-speed
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  No members
  Last clearing of "" counters never
  0 interface resets
  Load-Interval #1: 0 seconds
    0 seconds input rate 0 bits/sec, 0 packets/sec
    0 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 0 seconds
    0 seconds input rate 0 bits/sec, 0 packets/sec
    0 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    135 unicast packets  0 multicast packets  47 broadcast packets
    197 input packets  40064 bytes
    15 jumbo packets  0 storm suppression bytes
    0 runts  15 giants  0 CRC  0 no buffer
    15 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    0 unicast packets  96 multicast packets  0 broadcast packets
    96 output packets  18510 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

port-channel23 is down (No operational members)
admin state is up,
  Hardware: Port-Channel, address: 0000.0000.0000 (bia 0000.0000.0000)
  Description: tegile3
  MTU 9216 bytes, BW 100000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is access
  auto-duplex, auto-speed
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  No members
  Last clearing of "" counters never
  0 interface resets
  Load-Interval #1: 0 seconds
    0 seconds input rate 0 bits/sec, 0 packets/sec
    0 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 0 seconds
    0 seconds input rate 0 bits/sec, 0 packets/sec
    0 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 input packets  0 bytes
    0 jumbo packets  0 storm suppression bytes
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 output packets  0 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

port-channel24 is down (No operational members)
admin state is up,
  Hardware: Port-Channel, address: 0000.0000.0000 (bia 0000.0000.0000)
  Description: tegile4
  MTU 9216 bytes, BW 100000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is access
  auto-duplex, auto-speed
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  No members
  Last clearing of "" counters never
  0 interface resets
  Load-Interval #1: 0 seconds
    0 seconds input rate 0 bits/sec, 0 packets/sec
    0 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 0 seconds
    0 seconds input rate 0 bits/sec, 0 packets/sec
    0 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 input packets  0 bytes
    0 jumbo packets  0 storm suppression bytes
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 output packets  0 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Vlan1 is down (Administratively down), line protocol is down, autostate enabled
  Hardware is EtherSVI, address is  9077.ee01.bf07
  MTU 1500 bytes, BW 1000000 Kbit, DLY 10 usec,
   reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported
  ARP type: ARPA
  Last clearing of "" counters never
  L3 in Switched:
    ucast: 0 pkts, 0 bytes
  L3 out Switched:
    ucast: 0 pkts, 0 bytes



















































[K


""",
 'show inventory':"""NAME: "Chassis",  DESCR: "Nexus9000 C93180YC-FX Chassis"         
PID: N9K-C93180YC-FX     ,  VID: V06 ,  SN: FDO24250AYL          

NAME: "Slot 1",  DESCR: "48x10/25G/32G + 6x40/100G Ethernet/FC Module"
PID: N9K-C93180YC-FX     ,  VID: V06 ,  SN: FDO24250AYL          

NAME: "Power Supply 1",  DESCR: "Nexus9000 C93180YC-FX Chassis Power Supply"
PID: NXA-PAC-500W-PI     ,  VID: V01 ,  SN: LIT24192JNX          

NAME: "Power Supply 2",  DESCR: "Nexus9000 C93180YC-FX Chassis Power Supply"
PID: NXA-PAC-500W-PI     ,  VID: V01 ,  SN: LIT24192KPP          

NAME: "Fan 1",  DESCR: "Nexus9000 C93180YC-FX Chassis Fan Module"
PID: NXA-FAN-30CFM-B     ,  VID: V01 ,  SN: N/A                  

NAME: "Fan 2",  DESCR: "Nexus9000 C93180YC-FX Chassis Fan Module"
PID: NXA-FAN-30CFM-B     ,  VID: V01 ,  SN: N/A                  

NAME: "Fan 3",  DESCR: "Nexus9000 C93180YC-FX Chassis Fan Module"
PID: NXA-FAN-30CFM-B     ,  VID: V01 ,  SN: N/A                  

NAME: "Fan 4",  DESCR: "Nexus9000 C93180YC-FX Chassis Fan Module"
PID: NXA-FAN-30CFM-B     ,  VID: V01 ,  SN: N/A                  
""",
 'show interface counters':"""----------------------------------------------------------------------------------
Port                                     InOctets                      InUcastPkts
----------------------------------------------------------------------------------
mgmt0                                 27285159800                        154409645

----------------------------------------------------------------------------------
Port                                     InOctets                      InUcastPkts
----------------------------------------------------------------------------------
Eth1/1                                       2452                                4
Eth1/2                                       2452                                4
Eth1/3                                34659725194                         40967750
Eth1/4                                 3446657527                          6883438
Eth1/5                              1169002349005                        851526868
Eth1/6                               556350264174                         82586630
Eth1/7                                  187430748                           341579
Eth1/8                                   32310322                           125851
Eth1/9                                   21647143                               12
Eth1/10                             7381704727607                       5453610385
Eth1/11                            11497145516890                       8966037807
Eth1/12                                      2452                                4
Eth1/13                                      2452                                4
Eth1/14                                      2452                                4
Eth1/15                                    149198                              965
Eth1/16                                      2452                                4
Eth1/17                                   2351144                             3874
Eth1/18                                    156540                              932
Eth1/19                             3996441564611                       4656586699
Eth1/20                             7442914443046                       9077969920
Eth1/21                                  20499438                            31888
Eth1/22                                  20034329                            71234
Eth1/23                                      2452                                4
Eth1/24                                      2452                                4
Eth1/25                               86227292284                        283451551
Eth1/26                                      2452                                4
Eth1/27                                      2452                                4
Eth1/28                                      2452                                4
Eth1/29                                         0                                0
Eth1/30                                         0                                0
Eth1/31                                         0                                0
Eth1/32                                         0                                0
Eth1/33                                         0                                0
Eth1/34                                         0                                0
Eth1/35                                         0                                0
Eth1/36                                         0                                0
Eth1/37                                         0                                0
Eth1/38                                         0                                0
Eth1/39                                         0                                0
Eth1/40                                         0                                0
Eth1/41                                         0                                0
Eth1/42                                         0                                0
Eth1/43                                         0                                0
Eth1/44                                         0                                0
Eth1/45                                         0                                0
Eth1/46                                         0                                0
Eth1/47                                         0                                0
Eth1/48                                         0                                0
Eth1/49                            33229201308258                      42041888777
Eth1/50                                         0                                0
Eth1/51                                         0                                0
Eth1/52                                         0                                0
Eth1/53                                         0                                0
Eth1/54                                         0                                0

----------------------------------------------------------------------------------
Port                                     InOctets                      InUcastPkts
----------------------------------------------------------------------------------
Po11                               11439356007721                      13734556620
Po12                                     40533767                           103122
Po13                                            0                                0
Po16                                            0                                0
Po20                                         4904                                8
Po21                                        49748                              297
Po22                                        40064                              135
Po23                                            0                                0
Po24                                            0                                0

----------------------------------------------------------------------------------
Port                                     InOctets                      InUcastPkts
----------------------------------------------------------------------------------
Vlan1                                           0                                0

----------------------------------------------------------------------------------
Port                                  InMcastPkts                      InBcastPkts
----------------------------------------------------------------------------------
mgmt0                                    18538048                           144980

----------------------------------------------------------------------------------
Port                                  InMcastPkts                      InBcastPkts
----------------------------------------------------------------------------------
Eth1/1                                          0                                0
Eth1/2                                          0                                0
Eth1/3                                          0                              123
Eth1/4                                          0                            19694
Eth1/5                                          0                            15897
Eth1/6                                          0                             2214
Eth1/7                                          0                             8744
Eth1/8                                          0                              217
Eth1/9                                     284660                               84
Eth1/10                                    284552                           154370
Eth1/11                                  22066293                          6575418
Eth1/12                                         0                                0
Eth1/13                                         0                                0
Eth1/14                                         0                                0
Eth1/15                                         0                               20
Eth1/16                                         0                                0
Eth1/17                                         0                               11
Eth1/18                                         0                               18
Eth1/19                                  82398014                          8337532
Eth1/20                                   4006885                          4320323
Eth1/21                                       280                              129
Eth1/22                                       219                              111
Eth1/23                                         0                                0
Eth1/24                                         0                                0
Eth1/25                                   1115104                           655570
Eth1/26                                         0                                0
Eth1/27                                         0                                0
Eth1/28                                         0                                0
Eth1/29                                         0                                0
Eth1/30                                         0                                0
Eth1/31                                         0                                0
Eth1/32                                         0                                0
Eth1/33                                         0                                0
Eth1/34                                         0                                0
Eth1/35                                         0                                0
Eth1/36                                         0                                0
Eth1/37                                         0                                0
Eth1/38                                         0                                0
Eth1/39                                         0                                0
Eth1/40                                         0                                0
Eth1/41                                         0                                0
Eth1/42                                         0                                0
Eth1/43                                         0                                0
Eth1/44                                         0                                0
Eth1/45                                         0                                0
Eth1/46                                         0                                0
Eth1/47                                         0                                0
Eth1/48                                         0                                0
Eth1/49                                1868775105                        869154908
Eth1/50                                         0                                0
Eth1/51                                         0                                0
Eth1/52                                         0                                0
Eth1/53                                         0                                0
Eth1/54                                         0                                0

----------------------------------------------------------------------------------
Port                                  InMcastPkts                      InBcastPkts
----------------------------------------------------------------------------------
Po11                                     86404899                         12657855
Po12                                          499                              240
Po13                                            0                                0
Po16                                            0                                0
Po20                                            0                                0
Po21                                            0                               73
Po22                                            0                               47
Po23                                            0                                0
Po24                                            0                                0

----------------------------------------------------------------------------------
Port                                  InMcastPkts                      InBcastPkts
----------------------------------------------------------------------------------
Vlan1                                     --                                --

----------------------------------------------------------------------------------
Port                                    OutOctets                     OutUcastPkts
----------------------------------------------------------------------------------
mgmt0                                 33760941476                        154406696

----------------------------------------------------------------------------------
Port                                    OutOctets                     OutUcastPkts
----------------------------------------------------------------------------------
Eth1/1                                       2452                                4
Eth1/2                                       2452                                4
Eth1/3                                52274621954                         37925553
Eth1/4                                 4198639025                          6204287
Eth1/5                                96412449340                         35254679
Eth1/6                               284325277931                        220291554
Eth1/7                                 1599089947                           985579
Eth1/8                                 1644863059                          1028293
Eth1/9                                 3598080271                          1129667
Eth1/10                             6025815626820                       6262073491
Eth1/11                            11041147459782                      13029035493
Eth1/12                                      2452                                4
Eth1/13                                      2452                                4
Eth1/14                                      2452                                4
Eth1/15                                   1301746                             1876
Eth1/16                                      2452                                4
Eth1/17                                   1671106                             5529
Eth1/18                                   1221886                             1810
Eth1/19                             9113902380530                      10397427874
Eth1/20                             7072057227319                      16297923652
Eth1/21                                  21991305                            42517
Eth1/22                                  28842848                            61408
Eth1/23                                      2452                                4
Eth1/24                                      2452                                4
Eth1/25                              954477800508                       4610260430
Eth1/26                                      2452                                4
Eth1/27                                      2452                                4
Eth1/28                                      2452                                4
Eth1/29                                         0                                0
Eth1/30                                         0                                0
Eth1/31                                         0                                0
Eth1/32                                         0                                0
Eth1/33                                         0                                0
Eth1/34                                         0                                0
Eth1/35                                         0                                0
Eth1/36                                         0                                0
Eth1/37                                         0                                0
Eth1/38                                         0                                0
Eth1/39                                         0                                0
Eth1/40                                         0                                0
Eth1/41                                         0                                0
Eth1/42                                         0                                0
Eth1/43                                         0                                0
Eth1/44                                         0                                0
Eth1/45                                         0                                0
Eth1/46                                         0                                0
Eth1/47                                         0                                0
Eth1/48                                         0                                0
Eth1/49                            31213939815147                      28716481957
Eth1/50                                         0                                0
Eth1/51                                         0                                0
Eth1/52                                         0                                0
Eth1/53                                         0                                0
Eth1/54                                         0                                0

----------------------------------------------------------------------------------
Port                                    OutOctets                     OutUcastPkts
----------------------------------------------------------------------------------
Po11                               16185959614865                      26695351606
Po12                                     50834153                           103925
Po13                                            0                                0
Po16                                            0                                0
Po20                                         4904                                8
Po21                                        32496                                0
Po22                                        18510                                0
Po23                                            0                                0
Po24                                            0                                0

----------------------------------------------------------------------------------
Port                                    OutOctets                     OutUcastPkts
----------------------------------------------------------------------------------
Vlan1                                           0                                0

----------------------------------------------------------------------------------
Port                                 OutMcastPkts                     OutBcastPkts
----------------------------------------------------------------------------------
mgmt0                                      117063                                7

----------------------------------------------------------------------------------
Port                                 OutMcastPkts                     OutBcastPkts
----------------------------------------------------------------------------------
Eth1/1                                          0                                0
Eth1/2                                          0                                0
Eth1/3                                    1135944                          1892616
Eth1/4                                    6200267                          8923172
Eth1/5                                    4860568                         13666459
Eth1/6                                    4856057                         13673914
Eth1/7                                    4859818                         13671545
Eth1/8                                    4855618                         13674957
Eth1/9                                   14018197                         27695261
Eth1/10                                  14013421                         27533255
Eth1/11                                 316876906                        514672113
Eth1/12                                         0                                0
Eth1/13                                         0                                0
Eth1/14                                         0                                0
Eth1/15                                      6004                             7969
Eth1/16                                         0                                0
Eth1/17                                      5694                             7636
Eth1/18                                      5597                             7518
Eth1/19                                 245347355                        371873694
Eth1/20                                  99136840                        144997318
Eth1/21                                       333                              206
Eth1/22                                       747                              555
Eth1/23                                         0                                0
Eth1/24                                         0                                0
Eth1/25                                 339945342                        520536814
Eth1/26                                         0                                0
Eth1/27                                         0                                0
Eth1/28                                         0                                0
Eth1/29                                         0                                0
Eth1/30                                         0                                0
Eth1/31                                         0                                0
Eth1/32                                         0                                0
Eth1/33                                         0                                0
Eth1/34                                         0                                0
Eth1/35                                         0                                0
Eth1/36                                         0                                0
Eth1/37                                         0                                0
Eth1/38                                         0                                0
Eth1/39                                         0                                0
Eth1/40                                         0                                0
Eth1/41                                         0                                0
Eth1/42                                         0                                0
Eth1/43                                         0                                0
Eth1/44                                         0                                0
Eth1/45                                         0                                0
Eth1/46                                         0                                0
Eth1/47                                         0                                0
Eth1/48                                         0                                0
Eth1/49                                  33977182                         20264226
Eth1/50                                         0                                0
Eth1/51                                         0                                0
Eth1/52                                         0                                0
Eth1/53                                         0                                0
Eth1/54                                         0                                0

----------------------------------------------------------------------------------
Port                                 OutMcastPkts                     OutBcastPkts
----------------------------------------------------------------------------------
Po11                                    344484203                        516871037
Po12                                         1080                              761
Po13                                            0                                0
Po16                                            0                                0
Po20                                            0                                0
Po21                                          168                                0
Po22                                           96                                0
Po23                                            0                                0
Po24                                            0                                0

----------------------------------------------------------------------------------
Port                                 OutMcastPkts                     OutBcastPkts
----------------------------------------------------------------------------------
Vlan1                                     --                                --""",
 'show cdp nei detail':"""----------------------------------------
Device ID:sx1-079sfebb-2100k-racka-lib.net.utah.edu
VTP Management Domain Name: vtp-079sfebb

Interface address(es): 1
    IPv4 Address: 172.30.0.154
Platform: cisco C9300-48U, Capabilities: Switch IGMP Filtering 
Interface: mgmt0, Port ID (outgoing port): GigabitEthernet1/0/47
Holdtime: 133 sec

Version:
Cisco IOS Software [Gibraltar], Catalyst L3 Switch Software (CAT9K_IOSXE), Version 16.12.4, RELEASE SOFTWARE (fc5)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2020 by Cisco Systems, Inc.
Compiled Thu 09-Jul-20 21:49 by mcpre

Advertisement Version: 2

Native VLAN: 833
Duplex: full
Mgmt address(es):
    IPv4 Address: 172.30.0.154
Local Interface MAC: 90:77:ee:01:bf:00
Remote Interface MAC: 3c:13:cc:9c:3e:2f
----------------------------------------
Device ID:dx1-0079sfebb-100u-lib.net.utah.edu
VTP Management Domain Name: vtp-0079sfebb

Interface address(es): 1
    IPv4 Address: 172.30.0.132
Platform: cisco C9500-48Y4C, Capabilities: Switch IGMP Filtering 
Interface: Ethernet1/49, Port ID (outgoing port): HundredGigE1/0/51
Holdtime: 120 sec

Version:
Cisco IOS Software [Gibraltar], Catalyst L3 Switch Software (CAT9K_IOSXE), Version 16.12.02, RELEASE SOFTWARE (fc2)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2019 by Cisco Systems, Inc.
Compiled Tue 19-Nov-19 10:04 by mcpre

Advertisement Version: 2

Native VLAN: 1
Duplex: full
Mgmt address(es):
    IPv4 Address: 172.30.0.132
Local Interface MAC: 90:77:ee:01:bf:38
Remote Interface MAC: 4c:e1:75:cc:4a:73""",
 'show module all':"""^
% Invalid parameter detected at '^' marker.""",
 'show module':"""Mod Ports             Module-Type                       Model          Status
--- ----- ------------------------------------- --------------------- ---------
1    54   48x10/25G/32G + 6x40/100G Ethernet/FC N9K-C93180YC-FX       active *  

Mod  Sw                       Hw    Slot
---  ----------------------- ------ ----
1    9.3(3)                   1.2    NA  


Mod  MAC-Address(es)                         Serial-Num
---  --------------------------------------  ----------
1    90-77-ee-01-bf-00 to 90-77-ee-01-bf-5f  FDO24250AYL

Mod  Online Diag Status
---  ------------------
1    Pass

* this terminal session """,
 'show run | section snmp':"""120 permit udp addrgroup ORION_POLLERS any eq snmp 
  125 permit udp addrgroup ORION_POLLERS any eq snmptrap 
snmp-server contact TAG:%TAG%-BarCode:%BARCODE%
snmp-server location %BLDG#-RACK#%
snmp-server user admin network-admin auth md5 0x2bf2166822d5f82043bdd1f7076ccfe4 priv 0x2bf2166822d5f82043bdd1f7076ccfe4
 localizedkey
snmp-server user NXUSERNOC network-operator auth md5 0x419fb9d1a1907eb989eab2232cbd0960 priv aes-128 0x419fb9d1a1907eb98
9eab2232cbd0960 localizedkey
snmp-server user networker network-admin auth md5 0x2b41eeed2dde536d78f68149bfc555be priv 0x2b41eeed2dde536d78f68149bfc5
55be localizedkey
snmp-server user admin auth md5 0x1ca4cd1eafaa0407d413582efec4458c priv 0x1ca4cd1eafaa0407d413582efec4458c localizedkey 
engineID 128:0:0:9:3:216:103:217:1:14:0""",
 'show run | in snmp':"""120 permit udp addrgroup ORION_POLLERS any eq snmp 
  125 permit udp addrgroup ORION_POLLERS any eq snmptrap 
snmp-server contact TAG:%TAG%-BarCode:%BARCODE%
snmp-server location %BLDG#-RACK#%
snmp-server user admin network-admin auth md5 0x2bf2166822d5f82043bdd1f7076ccfe4 priv 0x2bf2166822d5f82043bdd1f7076ccfe4
 localizedkey
snmp-server user NXUSERNOC network-operator auth md5 0x419fb9d1a1907eb989eab2232cbd0960 priv aes-128 0x419fb9d1a1907eb98
9eab2232cbd0960 localizedkey
snmp-server user networker network-admin auth md5 0x2b41eeed2dde536d78f68149bfc555be priv 0x2b41eeed2dde536d78f68149bfc5
55be localizedkey
snmp-server user admin auth md5 0x1ca4cd1eafaa0407d413582efec4458c priv 0x1ca4cd1eafaa0407d413582efec4458c localizedkey 
engineID 128:0:0:9:3:216:103:217:1:14:0""",
 'show snmp user':"""______________________________________________________________
		  SNMP USERS 
______________________________________________________________

User                Auth  Priv(enforce) Groups              acl_filter          
____                ____  _____________ ______              __________          
admin               md5   des(no)       network-admin       
NXUSERNOC           md5   aes-128(no)   network-operator    
networker           md5   des(no)       network-admin       
______________________________________________________________
 NOTIFICATION TARGET USERS (configured  for sending V3 Inform) 
______________________________________________________________

User                          Auth  Priv          
____                          ____  ____          
admin               md5   des           
(EngineID )
128:0:0:9:3:216:103:217:1:14:0
""",
 'show access-list':"""IP access list SSH_POLICY
	10 permit tcp 155.98.253.0/24 any eq 22 
	15 permit tcp 155.99.254.128/25 any eq 22 
	20 remark VPN Networks
	25 permit tcp 155.98.164.192/27 any eq 22 
	30 permit tcp 155.101.243.0/27 any eq 22 
	31 permit tcp 155.98.164.192/27 any eq 22 
	40 deny tcp 155.100.37.16/32 any eq 22 
	50 deny tcp 155.100.37.31/32 any eq 22 
	60 permit tcp 155.100.37.16/28 any eq 22 
	61 permit tcp 155.99.254.128/25 any eq 22 
	70 remark Door1 & Door2
	80 permit tcp 155.99.239.130/32 any eq 22 
	90 permit tcp 155.97.152.244/32 any eq 22 
	95 permit tcp 155.101.168.124/32 any eq 22 
	99 remark Allow Firemon
	100 remark make 110 for Duc
	120 permit udp addrgroup ORION_POLLERS any eq snmp 
	125 permit udp addrgroup ORION_POLLERS any eq snmptrap 
	130 permit tcp addrgroup ORION_POLLERS any eq 22 
IPv6 access list VTY-ACL
	10 deny ipv6 any any log 
IP access list copp-system-p-acl-auto-rp
	10 permit ip any 224.0.1.39/32 
	20 permit ip any 224.0.1.40/32 
IP access list copp-system-p-acl-bgp
	10 permit tcp any gt 1023 any eq bgp 
	20 permit tcp any eq bgp any gt 1023 
IPv6 access list copp-system-p-acl-bgp6
	10 permit tcp any gt 1023 any eq bgp 
	20 permit tcp any eq bgp any gt 1023 
IP access list copp-system-p-acl-dhcp
	10 permit udp any eq bootpc any 
	20 permit udp any neq bootps any eq bootps 
IP access list copp-system-p-acl-dhcp-relay-response
	10 permit udp any eq bootps any 
	20 permit udp any any eq bootpc 
IPv6 access list copp-system-p-acl-dhcp6
	10 permit udp any eq 546 any 
	20 permit udp any any eq 547 
IPv6 access list copp-system-p-acl-dhcp6-relay-response
	10 permit udp any eq 547 any 
	20 permit udp any any eq 546 
IP access list copp-system-p-acl-eigrp
	10 permit eigrp any any 
IPv6 access list copp-system-p-acl-eigrp6
	10 permit eigrp any any 
IP access list copp-system-p-acl-ftp
	10 permit tcp any any eq ftp-data 
	20 permit tcp any any eq ftp 
	30 permit tcp any eq ftp-data any 
	40 permit tcp any eq ftp any 
IP access list copp-system-p-acl-hsrp
	10 permit udp any 224.0.0.0/24 eq 1985 
IPv6 access list copp-system-p-acl-hsrp6
	10 permit udp any ff02::66/128 eq 2029 
IP access list copp-system-p-acl-http
	10 permit tcp any eq www any 
[K	20 permit tcp any any eq www 
IP access list copp-system-p-acl-https
	10 permit tcp any eq 443 any 
	20 permit tcp any any eq 443 
IP access list copp-system-p-acl-icmp
	10 permit icmp any any echo 
	20 permit icmp any any echo-reply 
IPv6 access list copp-system-p-acl-icmp6
	10 permit icmp any any echo-request 
	20 permit icmp any any echo-reply 
IP access list copp-system-p-acl-igmp
	10 permit igmp any 224.0.0.0/3 
MAC access list copp-system-p-acl-mac-cdp-udld-vtp
	10 permit any 0100.0ccc.cccc 0000.0000.0000 
MAC access list copp-system-p-acl-mac-cfsoe
	10 permit any 0180.c200.000e 0000.0000.0000 0x8843 
	20 permit any 0180.c200.000e 0000.0000.0000 
MAC access list copp-system-p-acl-mac-dot1x
	10 permit any 0180.c200.0003 0000.0000.0000 0x888e 
MAC access list copp-system-p-acl-mac-fcoe
	10 permit any any 0x8906 
	20 permit any any 0x8914 
MAC access list copp-system-p-acl-mac-l2-tunnel
	10 permit any any 0x8840 
MAC access list copp-system-p-acl-mac-l3-isis
	10 permit any 0180.c200.0015 0000.0000.0000 
	20 permit any 0180.c200.0014 0000.0000.0000 
	30 permit any 0900.2b00.0005 0000.0000.0000 
	40 permit any 0900.2b00.0004 0000.0000.0000 
MAC access list copp-system-p-acl-mac-lacp
	10 permit any 0180.c200.0002 0000.0000.0000 0x8809 
MAC access list copp-system-p-acl-mac-lldp
	10 permit any 0180.c200.000e 0000.0000.0000 0x88cc 
MAC access list copp-system-p-acl-mac-sdp-srp
	10 permit any 0180.c200.000e 0000.0000.0000 0x3401 
MAC access list copp-system-p-acl-mac-stp
	10 permit any 0100.0ccc.cccd 0000.0000.0000 
	20 permit any 0180.c200.0000 0000.0000.0000 
MAC access list copp-system-p-acl-mac-undesirable
	10 permit any any 
IPv6 access list copp-system-p-acl-mld
	10 permit icmp any any mld-query 
	20 permit icmp any any mld-report 
	30 permit icmp any any mld-reduction 
	40 permit icmp any any mldv2 
IP access list copp-system-p-acl-msdp
	10 permit tcp any gt 1023 any eq 639 
	20 permit tcp any eq 639 any gt 1023 
IPv6 access list copp-system-p-acl-ndp
	10 permit icmp any any router-solicitation 
	20 permit icmp any any router-advertisement 
	30 permit icmp any any nd-ns 
	40 permit icmp any any nd-na 
IP access list copp-system-p-acl-ntp
	10 permit udp any any eq ntp 
	20 permit udp any eq ntp any 
IPv6 access list copp-system-p-acl-ntp6
	10 permit udp any any eq ntp 
	20 permit udp any eq ntp any 
IP access list copp-system-p-acl-openflow
	10 permit tcp any eq 6653 any 
IP access list copp-system-p-acl-ospf
	10 permit ospf any any 
IPv6 access list copp-system-p-acl-ospf6
	10 permit 89 any any 
IP access list copp-system-p-acl-pim
	10 permit pim any 224.0.0.0/24 
	20 permit udp any any eq pim-auto-rp 
	30 permit ip any 224.0.0.13/32 
IP access list copp-system-p-acl-pim-mdt-join
	10 permit udp any 224.0.0.13/32 
IP access list copp-system-p-acl-pim-reg
	10 permit pim any any 
IPv6 access list copp-system-p-acl-pim6
	10 permit pim any ff02::d/128 
	20 permit udp any any eq pim-auto-rp 
IPv6 access list copp-system-p-acl-pim6-reg
	10 permit pim any any 
IP access list copp-system-p-acl-ptp
	10 permit udp any 224.0.1.129/32 eq 319 
	20 permit udp any 224.0.1.129/32 eq 320 
MAC access list copp-system-p-acl-ptp-l2
	10 permit any any 0x88f7 
IP access list copp-system-p-acl-ptp-uc
	10 permit udp any any eq 319 
	20 permit udp any any eq 320 
IP access list copp-system-p-acl-radius
	10 permit udp any any eq 1812 
	20 permit udp any any eq 1813 
	30 permit udp any any eq 1645 
	40 permit udp any any eq 1646 
	50 permit udp any eq 1812 any 
	60 permit udp any eq 1813 any 
	70 permit udp any eq 1645 any 
	80 permit udp any eq 1646 any 
IPv6 access list copp-system-p-acl-radius6
	10 permit udp any any eq 1812 
	20 permit udp any any eq 1813 
	30 permit udp any any eq 1645 
	40 permit udp any any eq 1646 
	50 permit udp any eq 1812 any 
	60 permit udp any eq 1813 any 
	70 permit udp any eq 1645 any 
	80 permit udp any eq 1646 any 
IP access list copp-system-p-acl-rip
	10 permit udp any 224.0.0.0/24 eq rip 
IPv6 access list copp-system-p-acl-rip6
	10 permit udp any ff02::9/64 eq 521 
IP access list copp-system-p-acl-sftp
	10 permit tcp any any eq 115 
	20 permit tcp any eq 115 any 
IP access list copp-system-p-acl-snmp
	10 permit udp any any eq snmp 
	20 permit udp any any eq snmptrap 
	30 permit tcp any any eq 161 
	40 permit tcp any any eq 162 
IPv6 access list copp-system-p-acl-snmp6
	10 permit udp any any eq snmp 
[K	20 permit udp any any eq snmptrap 
	30 permit tcp any any eq 161 
	40 permit tcp any any eq 162 
IP access list copp-system-p-acl-ssh
	10 permit tcp any any eq 22 
	20 permit tcp any eq 22 any 
IPv6 access list copp-system-p-acl-ssh6
	10 permit tcp any any eq 22 
	20 permit tcp any eq 22 any 
IP access list copp-system-p-acl-tacacs
	10 permit tcp any any eq tacacs 
	20 permit tcp any eq tacacs any 
IPv6 access list copp-system-p-acl-tacacs6
	10 permit tcp any any eq tacacs 
	20 permit tcp any eq tacacs any 
IP access list copp-system-p-acl-telnet
	10 permit tcp any any eq telnet 
	20 permit tcp any any eq 107 
	30 permit tcp any eq telnet any 
	40 permit tcp any eq 107 any 
IPv6 access list copp-system-p-acl-telnet6
	10 permit tcp any any eq telnet 
	20 permit tcp any any eq 107 
	30 permit tcp any eq telnet any 
	40 permit tcp any eq 107 any 
IP access list copp-system-p-acl-tftp
	10 permit udp any any eq tftp 
	20 permit udp any any eq 1758 
	30 permit udp any eq tftp any 
	40 permit udp any eq 1758 any 
IPv6 access list copp-system-p-acl-tftp6
	10 permit udp any any eq tftp 
	20 permit udp any any eq 1758 
	30 permit udp any eq tftp any 
	40 permit udp any eq 1758 any 
IP access list copp-system-p-acl-traceroute
	10 permit icmp any any ttl-exceeded 
	20 permit icmp any any port-unreachable 
	30 permit udp any any range 33434 33534 
IP access list copp-system-p-acl-undesirable
	10 permit udp any any eq 1434 
IP access list copp-system-p-acl-vpc
	10 permit udp any any eq 3200 
IP access list copp-system-p-acl-vrrp
	10 permit ip any 224.0.0.18/32 
IPv6 access list copp-system-p-acl-vrrp6
	10 permit ipv6 any ff02::12/128 """,
 'show run | section logging':"""logging level feature-mgr 0
logging server 10.71.24.11 7 use-vrf management facility local6
logging server 172.24.29.14 7 use-vrf management facility local6""",
 'show run | in logging':"""logging level feature-mgr 0
logging server 10.71.24.11 7 use-vrf management facility local6
logging server 172.24.29.14 7 use-vrf management facility local6""",
 'show mac address-table':"""Legend: 
	* - primary entry, G - Gateway MAC, (R) - Routed MAC, O - Overlay MAC
	age - seconds since last seen,+ - primary entry using vPC Peer-Link,
	(T) - True, (F) - False, C - ControlPlane MAC, ~ - vsan
   VLAN     MAC Address      Type      age     Secure NTFY Ports
---------+-----------------+--------+---------+------+----+------------------
*    1     4ce1.75cc.4a73   dynamic  0         F      F    Eth1/49
*    1     80ee.7309.c96b   dynamic  0         F      F    Eth1/49
*    1     80ee.7309.c96c   dynamic  0         F      F    Eth1/49
*    1     8c94.1f18.e335   dynamic  0         F      F    Eth1/49
* 2715     8c94.1f18.e335   dynamic  0         F      F    Eth1/49
* 2799     0000.0c9f.faef   dynamic  0         F      F    Eth1/49
* 2799     8c94.1f18.e335   dynamic  0         F      F    Eth1/49
* 2799     ecce.1389.8582   dynamic  0         F      F    Eth1/49
* 2800     0000.0c9f.faf0   dynamic  0         F      F    Eth1/49
* 2800     0005.a60e.d2ce   dynamic  0         F      F    Eth1/49
* 2800     0005.a614.7d19   dynamic  0         F      F    Eth1/49
* 2800     0005.a614.7d60   dynamic  0         F      F    Eth1/49
* 2800     0005.a614.7d68   dynamic  0         F      F    Eth1/49
* 2800     0005.a614.7d73   dynamic  0         F      F    Eth1/49
* 2800     0005.a614.9907   dynamic  0         F      F    Eth1/49
* 2800     0005.a616.a258   dynamic  0         F      F    Eth1/49
* 2800     0005.a61c.2484   dynamic  0         F      F    Eth1/49
* 2800     0005.a61c.2486   dynamic  0         F      F    Eth1/49
* 2800     0005.a61c.2488   dynamic  0         F      F    Eth1/49
* 2800     0005.a61c.248c   dynamic  0         F      F    Eth1/49
* 2800     0005.a61c.2490   dynamic  0         F      F    Eth1/49
* 2800     0005.a61c.2495   dynamic  0         F      F    Eth1/49
* 2800     0005.a61c.2497   dynamic  0         F      F    Eth1/49
* 2800     0005.a61c.24a1   dynamic  0         F      F    Eth1/49
* 2800     0005.a61c.24a3   dynamic  0         F      F    Eth1/49
* 2800     0005.a61c.24b5   dynamic  0         F      F    Eth1/49
* 2800     0005.a61c.24bc   dynamic  0         F      F    Eth1/49
* 2800     0005.a61c.24c0   dynamic  0         F      F    Eth1/49
* 2800     0005.a61c.24c5   dynamic  0         F      F    Eth1/49
* 2800     0005.a61c.24cd   dynamic  0         F      F    Eth1/49
* 2800     000e.dd51.0704   dynamic  0         F      F    Eth1/49
* 2800     000e.dd51.08b7   dynamic  0         F      F    Eth1/49
* 2800     000e.dd51.093e   dynamic  0         F      F    Eth1/49
* 2800     000e.dd51.0acf   dynamic  0         F      F    Eth1/49
* 2800     000e.dd60.6fe5   dynamic  0         F      F    Eth1/49
* 2800     000e.dd60.7005   dynamic  0         F      F    Eth1/49
* 2800     000e.dd60.704f   dynamic  0         F      F    Eth1/49
* 2800     000e.dd60.7073   dynamic  0         F      F    Eth1/49
* 2800     000e.dd60.7075   dynamic  0         F      F    Eth1/49
* 2800     000e.dd60.7079   dynamic  0         F      F    Eth1/49
* 2800     000e.dd60.708b   dynamic  0         F      F    Eth1/49
* 2800     000e.dd60.7194   dynamic  0         F      F    Eth1/49
* 2800     000e.dd60.7997   dynamic  0         F      F    Eth1/49
* 2800     000e.dd60.799d   dynamic  0         F      F    Eth1/49
* 2800     000e.dd60.79a9   dynamic  0         F      F    Eth1/49
* 2800     000e.dd60.7a01   dynamic  0         F      F    Eth1/49
* 2800     000e.dd60.7a72   dynamic  0         F      F    Eth1/49
* 2800     000e.dd60.7a94   dynamic  0         F      F    Eth1/49
* 2800     000e.dd60.7aa3   dynamic  0         F      F    Eth1/49
* 2800     000e.dd60.7acf   dynamic  0         F      F    Eth1/49
* 2800     000e.dd60.7af3   dynamic  0         F      F    Eth1/49
* 2800     000e.dd60.7bf6   dynamic  0         F      F    Eth1/49
* 2800     000e.dd60.7c42   dynamic  0         F      F    Eth1/49
* 2800     000e.dd60.7c45   dynamic  0         F      F    Eth1/49
* 2800     000e.dd60.7c48   dynamic  0         F      F    Eth1/49
* 2800     000e.dd60.7c64   dynamic  0         F      F    Eth1/49
* 2800     000e.dd60.7c7b   dynamic  0         F      F    Eth1/49
* 2800     000e.dd60.7c7d   dynamic  0         F      F    Eth1/49
* 2800     000e.dd60.7dd4   dynamic  0         F      F    Eth1/49
* 2800     000e.dd60.7dd6   dynamic  0         F      F    Eth1/49
* 2800     000e.dd60.7df3   dynamic  0         F      F    Eth1/49
* 2800     000e.dd60.7df6   dynamic  0         F      F    Eth1/49
* 2800     000e.dd60.7e32   dynamic  0         F      F    Eth1/49
* 2800     000e.dd60.7eba   dynamic  0         F      F    Eth1/49
* 2800     000e.dd60.7eea   dynamic  0         F      F    Eth1/49
* 2800     000e.dd60.7f4c   dynamic  0         F      F    Eth1/49
* 2800     000e.dd60.7f50   dynamic  0         F      F    Eth1/49
* 2800     000e.dd60.7f53   dynamic  0         F      F    Eth1/49
* 2800     000e.dd60.7f57   dynamic  0         F      F    Eth1/49
* 2800     000e.dd60.7f6f   dynamic  0         F      F    Eth1/49
* 2800     000e.dd60.7f95   dynamic  0         F      F    Eth1/49
* 2800     000e.dd60.7fbe   dynamic  0         F      F    Eth1/49
* 2800     000e.dd60.7fed   dynamic  0         F      F    Eth1/49
* 2800     000e.ddf6.6f38   dynamic  0         F      F    Eth1/49
* 2800     000e.ddf6.6f58   dynamic  0         F      F    Eth1/49
* 2800     000e.ddf6.6fa2   dynamic  0         F      F    Eth1/49
* 2800     000e.ddf6.6fc6   dynamic  0         F      F    Eth1/49
* 2800     000e.ddf6.6fc8   dynamic  0         F      F    Eth1/49
* 2800     000e.ddf6.6fcc   dynamic  0         F      F    Eth1/49
* 2800     000e.ddf6.6fde   dynamic  0         F      F    Eth1/49
* 2800     000e.ddf6.70e5   dynamic  0         F      F    Eth1/49
* 2800     000e.ddf6.78e8   dynamic  0         F      F    Eth1/49
* 2800     000e.ddf6.78ee   dynamic  0         F      F    Eth1/49
* 2800     000e.ddf6.78fa   dynamic  0         F      F    Eth1/49
* 2800     000e.ddf6.7952   dynamic  0         F      F    Eth1/49
* 2800     000e.ddf6.79c3   dynamic  0         F      F    Eth1/49
* 2800     000e.ddf6.79e5   dynamic  0         F      F    Eth1/49
* 2800     000e.ddf6.79f4   dynamic  0         F      F    Eth1/49
* 2800     000e.ddf6.7a20   dynamic  0         F      F    Eth1/49
* 2800     000e.ddf6.7a44   dynamic  0         F      F    Eth1/49
* 2800     000e.ddf6.7b47   dynamic  0         F      F    Eth1/49
* 2800     000e.ddf6.7b93   dynamic  0         F      F    Eth1/49
* 2800     000e.ddf6.7b96   dynamic  0         F      F    Eth1/49
* 2800     000e.ddf6.7b99   dynamic  0         F      F    Eth1/49
* 2800     000e.ddf6.7bb5   dynamic  0         F      F    Eth1/49
* 2800     000e.ddf6.7bcc   dynamic  0         F      F    Eth1/49
* 2800     000e.ddf6.7bce   dynamic  0         F      F    Eth1/49
* 2800     000e.ddf6.7d25   dynamic  0         F      F    Eth1/49
* 2800     000e.ddf6.7d27   dynamic  0         F      F    Eth1/49
* 2800     000e.ddf6.7d44   dynamic  0         F      F    Eth1/49
* 2800     000e.ddf6.7d47   dynamic  0         F      F    Eth1/49
* 2800     000e.ddf6.7d83   dynamic  0         F      F    Eth1/49
* 2800     000e.ddf6.7e0b   dynamic  0         F      F    Eth1/49
* 2800     000e.ddf6.7e3b   dynamic  0         F      F    Eth1/49
* 2800     000e.ddf6.7e9d   dynamic  0         F      F    Eth1/49
* 2800     000e.ddf6.7ea1   dynamic  0         F      F    Eth1/49
* 2800     000e.ddf6.7ea4   dynamic  0         F      F    Eth1/49
* 2800     000e.ddf6.7ea8   dynamic  0         F      F    Eth1/49
* 2800     000e.ddf6.7ec0   dynamic  0         F      F    Eth1/49
* 2800     000e.ddf6.7ee6   dynamic  0         F      F    Eth1/49
* 2800     000e.ddf6.7f0f   dynamic  0         F      F    Eth1/49
* 2800     000e.ddf6.7f3e   dynamic  0         F      F    Eth1/49
* 2800     000e.ddfb.908d   dynamic  0         F      F    Eth1/49
* 2800     000e.ddfb.91b5   dynamic  0         F      F    Eth1/49
* 2800     000e.ddfb.9220   dynamic  0         F      F    Eth1/49
* 2800     000e.ddfb.933c   dynamic  0         F      F    Eth1/49
* 2800     000f.d401.767a   dynamic  0         F      F    Eth1/49
* 2800     000f.d401.76b5   dynamic  0         F      F    Eth1/49
* 2800     000f.d40b.b045   dynamic  0         F      F    Eth1/49
* 2800     000f.d40b.b60e   dynamic  0         F      F    Eth1/49
* 2800     0010.7f84.8ed3   dynamic  0         F      F    Eth1/49
* 2800     0010.7f97.82cb   dynamic  0         F      F    Eth1/49
* 2800     0010.7f9b.9feb   dynamic  0         F      F    Eth1/49
* 2800     0010.7f9b.a12b   dynamic  0         F      F    Eth1/49
* 2800     0010.7f9b.a142   dynamic  0         F      F    Eth1/49
* 2800     0010.7f9b.a16d   dynamic  0         F      F    Eth1/49
* 2800     0010.7fa1.bde5   dynamic  0         F      F    Eth1/49
* 2800     0010.7fa6.31b4   dynamic  0         F      F    Eth1/49
* 2800     0010.7fa6.af79   dynamic  0         F      F    Eth1/49
* 2800     0010.7fa6.afd3   dynamic  0         F      F    Eth1/49
* 2800     0010.7fa6.b08c   dynamic  0         F      F    Eth1/49
* 2800     0010.7fa6.b12e   dynamic  0         F      F    Eth1/49
* 2800     0010.7fa6.b17f   dynamic  0         F      F    Eth1/49
* 2800     0010.7fa8.57ea   dynamic  0         F      F    Eth1/49
* 2800     0010.7fa8.7b8f   dynamic  0         F      F    Eth1/49
* 2800     0010.7fa8.7bcc   dynamic  0         F      F    Eth1/49
* 2800     0010.7fa8.7c39   dynamic  0         F      F    Eth1/49
* 2800     0010.7fa8.7c84   dynamic  0         F      F    Eth1/49
* 2800     0010.7fa8.7e54   dynamic  0         F      F    Eth1/49
* 2800     0010.7fa8.8036   dynamic  0         F      F    Eth1/49
* 2800     0010.7fa8.806e   dynamic  0         F      F    Eth1/49
* 2800     0010.7fa8.91f4   dynamic  0         F      F    Eth1/49
* 2800     0010.7fa8.a26e   dynamic  0         F      F    Eth1/49
* 2800     0010.7fa9.31fe   dynamic  0         F      F    Eth1/49
* 2800     0010.7fa9.68a9   dynamic  0         F      F    Eth1/49
* 2800     0010.7fa9.95c9   dynamic  0         F      F    Eth1/49
* 2800     0010.7fa9.9681   dynamic  0         F      F    Eth1/49
* 2800     0010.7fa9.a588   dynamic  0         F      F    Eth1/49
* 2800     0010.7fa9.e29d   dynamic  0         F      F    Eth1/49
* 2800     0010.7fa9.e97c   dynamic  0         F      F    Eth1/49
* 2800     0010.7faa.a72c   dynamic  0         F      F    Eth1/49
* 2800     0010.7fab.10d4   dynamic  0         F      F    Eth1/49
* 2800     0010.7fb0.24f4   dynamic  0         F      F    Eth1/49
* 2800     0010.7fb0.2551   dynamic  0         F      F    Eth1/49
* 2800     0010.7fb0.269d   dynamic  0         F      F    Eth1/49
* 2800     0010.7fb0.279b   dynamic  0         F      F    Eth1/49
* 2800     0010.7fb0.2d08   dynamic  0         F      F    Eth1/49
* 2800     0010.7fb0.36dc   dynamic  0         F      F    Eth1/49
* 2800     0010.7fb0.3a03   dynamic  0         F      F    Eth1/49
* 2800     0010.7fb0.3a13   dynamic  0         F      F    Eth1/49
* 2800     0010.7fb0.3c7c   dynamic  0         F      F    Eth1/49
* 2800     0010.7fb0.3dea   dynamic  0         F      F    Eth1/49
* 2800     0010.7fb0.3dfe   dynamic  0         F      F    Eth1/49
* 2800     0010.7fb0.3f61   dynamic  0         F      F    Eth1/49
* 2800     0010.7fb0.40ad   dynamic  0         F      F    Eth1/49
* 2800     0010.7fb0.41c4   dynamic  0         F      F    Eth1/49
* 2800     0010.7fb0.42a6   dynamic  0         F      F    Eth1/49
* 2800     0010.7fb0.43da   dynamic  0         F      F    Eth1/49
* 2800     0010.7fb0.4427   dynamic  0         F      F    Eth1/49
* 2800     0010.7fb0.444f   dynamic  0         F      F    Eth1/49
* 2800     0010.7fb0.4562   dynamic  0         F      F    Eth1/49
* 2800     0010.7fb2.808a   dynamic  0         F      F    Eth1/49
* 2800     0010.7fb4.cec3   dynamic  0         F      F    Eth1/49
* 2800     0010.7fb4.d2bd   dynamic  0         F      F    Eth1/49
* 2800     0010.7fb4.e2ec   dynamic  0         F      F    Eth1/49
* 2800     0010.7fb7.0356   dynamic  0         F      F    Eth1/49
* 2800     0010.7fb7.2305   dynamic  0         F      F    Eth1/49
* 2800     0010.7fb7.5471   dynamic  0         F      F    Eth1/49
* 2800     0010.7fb7.5c79   dynamic  0         F      F    Eth1/49
* 2800     0010.7fbc.6ebe   dynamic  0         F      F    Eth1/49
* 2800     0010.7fbe.182d   dynamic  0         F      F    Eth1/49
* 2800     0010.7fc6.f909   dynamic  0         F      F    Eth1/49
* 2800     0010.7fc6.f911   dynamic  0         F      F    Eth1/49
* 2800     0010.7fc6.f933   dynamic  0         F      F    Eth1/49
* 2800     0010.7fc6.f95c   dynamic  0         F      F    Eth1/49
* 2800     0010.7fc6.f95d   dynamic  0         F      F    Eth1/49
* 2800     0010.7fc6.f9a1   dynamic  0         F      F    Eth1/49
* 2800     0010.7fc6.f9fa   dynamic  0         F      F    Eth1/49
* 2800     0010.7fc6.fa29   dynamic  0         F      F    Eth1/49
* 2800     0010.7fc6.fa9e   dynamic  0         F      F    Eth1/49
* 2800     0010.7fc6.fb03   dynamic  0         F      F    Eth1/49
* 2800     0010.7fc6.fbc7   dynamic  0         F      F    Eth1/49
* 2800     0010.7fc8.286d   dynamic  0         F      F    Eth1/49
* 2800     0010.7fda.1fac   dynamic  0         F      F    Eth1/49
* 2800     001d.c113.942a   dynamic  0         F      F    Eth1/49
* 2800     001d.c113.9b14   dynamic  0         F      F    Eth1/49
* 2800     001d.c113.9c80   dynamic  0         F      F    Eth1/49
* 2800     001d.c118.f316   dynamic  0         F      F    Eth1/49
* 2800     001d.c151.3434   dynamic  0         F      F    Eth1/49
* 2800     001d.c151.3438   dynamic  0         F      F    Eth1/49
* 2800     001d.c151.3454   dynamic  0         F      F    Eth1/49
* 2800     001d.c151.3455   dynamic  0         F      F    Eth1/49
* 2800     001d.c151.3457   dynamic  0         F      F    Eth1/49
* 2800     001d.c151.3458   dynamic  0         F      F    Eth1/49
* 2800     001d.c151.345a   dynamic  0         F      F    Eth1/49
* 2800     001d.c151.3465   dynamic  0         F      F    Eth1/49
* 2800     001d.c151.3466   dynamic  0         F      F    Eth1/49
* 2800     001d.c191.3b37   dynamic  0         F      F    Eth1/49
* 2800     001d.c191.3b54   dynamic  0         F      F    Eth1/49
* 2800     001d.c191.3b6e   dynamic  0         F      F    Eth1/49
* 2800     001d.c191.3bab   dynamic  0         F      F    Eth1/49
* 2800     001d.c191.3bb3   dynamic  0         F      F    Eth1/49
* 2800     001d.c191.3bbe   dynamic  0         F      F    Eth1/49
* 2800     001d.c191.3bc6   dynamic  0         F      F    Eth1/49
* 2800     001d.c191.3c55   dynamic  0         F      F    Eth1/49
* 2800     001d.c191.3c59   dynamic  0         F      F    Eth1/49
* 2800     001d.c1a0.1768   dynamic  0         F      F    Eth1/49
* 2800     001d.c1a0.1778   dynamic  0         F      F    Eth1/49
* 2800     001d.c1a0.177c   dynamic  0         F      F    Eth1/49
* 2800     001d.c1a0.1788   dynamic  0         F      F    Eth1/49
* 2800     00aa.6e15.65c0   dynamic  0         F      F    Eth1/49
* 2800     247e.12fb.c040   dynamic  0         F      F    Eth1/49
* 2800     501c.b034.13c0   dynamic  0         F      F    Eth1/49
* 2800     501c.b034.25c0   dynamic  0         F      F    Eth1/49
* 2800     501c.b034.31c0   dynamic  0         F      F    Eth1/49
* 2800     501c.b034.6340   dynamic  0         F      F    Eth1/49
* 2800     501c.b034.8cc0   dynamic  0         F      F    Eth1/49
* 2800     501c.b034.8fc0   dynamic  0         F      F    Eth1/49
* 2800     5893.962a.6b00   dynamic  0         F      F    Eth1/49
* 2800     682c.7ba4.86c0   dynamic  0         F      F    Eth1/49
* 2800     682c.7ba4.ed40   dynamic  0         F      F    Eth1/49
* 2800     682c.7ba4.eec0   dynamic  0         F      F    Eth1/49
* 2800     682c.7ba5.0bc0   dynamic  0         F      F    Eth1/49
* 2800     685b.35c3.e186   dynamic  0         F      F    Eth1/49
* 2800     68ca.e46b.ea40   dynamic  0         F      F    Eth1/49
* 2800     68ca.e4b3.82c0   dynamic  0         F      F    Eth1/49
* 2800     68ca.e4b3.9640   dynamic  0         F      F    Eth1/49
* 2800     7001.b508.b640   dynamic  0         F      F    Eth1/49
* 2800     7001.b508.cb40   dynamic  0         F      F    Eth1/49
* 2800     7845.0100.b4e5   dynamic  0         F      F    Eth1/49
* 2800     7845.0100.b4e9   dynamic  0         F      F    Eth1/49
* 2800     7845.0100.ca85   dynamic  0         F      F    Eth1/49
* 2800     7845.0100.d1d8   dynamic  0         F      F    Eth1/49
* 2800     7845.0100.d1e2   dynamic  0         F      F    Eth1/49
* 2800     7845.0100.d2d7   dynamic  0         F      F    Eth1/49
* 2800     7845.0100.d2e6   dynamic  0         F      F    Eth1/49
* 2800     7845.0100.d2ee   dynamic  0         F      F    Eth1/49
* 2800     7845.0100.d2fa   dynamic  0         F      F    Eth1/49
* 2800     7845.0100.d2fe   dynamic  0         F      F    Eth1/49
* 2800     7845.0100.d302   dynamic  0         F      F    Eth1/49
* 2800     7845.0100.d306   dynamic  0         F      F    Eth1/49
* 2800     7845.0100.d47f   dynamic  0         F      F    Eth1/49
* 2800     7845.0100.e5bd   dynamic  0         F      F    Eth1/49
* 2800     7845.0100.e5c3   dynamic  0         F      F    Eth1/49
* 2800     7845.0100.e5ce   dynamic  0         F      F    Eth1/49
* 2800     7845.0100.e5dc   dynamic  0         F      F    Eth1/49
* 2800     7845.0100.e5e5   dynamic  0         F      F    Eth1/49
* 2800     7845.0100.e781   dynamic  0         F      F    Eth1/49
* 2800     7845.0100.e789   dynamic  0         F      F    Eth1/49
* 2800     7845.0100.e79b   dynamic  0         F      F    Eth1/49
* 2800     7845.0100.e7a5   dynamic  0         F      F    Eth1/49
* 2800     7845.0100.eb2d   dynamic  0         F      F    Eth1/49
* 2800     7845.0100.eb39   dynamic  0         F      F    Eth1/49
* 2800     7845.0100.ebec   dynamic  0         F      F    Eth1/49
* 2800     7845.0100.ebf0   dynamic  0         F      F    Eth1/49
* 2800     7845.0100.ebf4   dynamic  0         F      F    Eth1/49
* 2800     7845.0100.ebf8   dynamic  0         F      F    Eth1/49
* 2800     7845.0100.ebfc   dynamic  0         F      F    Eth1/49
* 2800     7845.0100.ec10   dynamic  0         F      F    Eth1/49
* 2800     7845.0100.eda9   dynamic  0         F      F    Eth1/49
* 2800     7845.0100.edc6   dynamic  0         F      F    Eth1/49
* 2800     7845.0100.edcc   dynamic  0         F      F    Eth1/49
* 2800     7845.0102.99bf   dynamic  0         F      F    Eth1/49
* 2800     7845.0109.3d86   dynamic  0         F      F    Eth1/49
* 2800     a01e.0b0d.5baa   dynamic  0         F      F    Eth1/49
* 2800     d4e0.8e11.0669   dynamic  0         F      F    Eth1/49
* 2800     e0d5.5eaf.ff7c   dynamic  0         F      F    Eth1/49
* 2800     ecce.1389.7802   dynamic  0         F      F    Eth1/49
* 2800     ecce.1389.8582   dynamic  0         F      F    Eth1/49
* 2808     0000.0c9f.faf8   dynamic  0         F      F    Eth1/49
* 2808     8c94.1f18.e335   dynamic  0         F      F    Eth1/49
* 2808     ecce.1389.8582   dynamic  0         F      F    Eth1/49
* 2809     0000.0c9f.faf9   dynamic  0         F      F    Eth1/49
* 2809     8c94.1f18.e335   dynamic  0         F      F    Eth1/49
* 2809     ecce.1389.8582   dynamic  0         F      F    Eth1/49
* 2811     0000.0c9f.fafb   dynamic  0         F      F    Eth1/49
* 2811     8c94.1f18.e335   dynamic  0         F      F    Eth1/49
* 2811     ecce.1389.7802   dynamic  0         F      F    Eth1/49
* 2811     ecce.1389.8582   dynamic  0         F      F    Eth1/49
* 2812     0000.0c9f.fafc   dynamic  0         F      F    Eth1/49
* 2812     0015.5d0f.0001   dynamic  0         F      F    Eth1/49
* 2812     0015.5d3e.f615   dynamic  0         F      F    Eth1/49
* 2812     0015.5d3e.f6fa   dynamic  0         F      F    Eth1/49
* 2812     0015.5d48.53ef   dynamic  0         F      F    Eth1/49
* 2812     0015.5d49.42c0   dynamic  0         F      F    Eth1/49
* 2812     0015.5d49.42c1   dynamic  0         F      F    Eth1/49
* 2812     0015.5d49.42d5   dynamic  0         F      F    Eth1/49
* 2812     0015.5d49.9fe6   dynamic  0         F      F    Eth1/49
* 2812     0015.5d49.a801   dynamic  0         F      F    Eth1/49
* 2812     0015.5d49.a802   dynamic  0         F      F    Eth1/49
* 2812     0015.5d49.a806   dynamic  0         F      F    Eth1/49
* 2812     0015.5d49.a82d   dynamic  0         F      F    Eth1/49
* 2812     0015.5d49.a830   dynamic  0         F      F    Eth1/49
* 2812     0015.5d49.a8f6   dynamic  0         F      F    Eth1/49
* 2812     0050.5689.034b   dynamic  0         F      F    Eth1/49
* 2812     0050.5689.0e04   dynamic  0         F      F    Eth1/11
* 2812     0050.5689.1be3   dynamic  0         F      F    Eth1/49
* 2812     0050.5689.2543   dynamic  0         F      F    Eth1/49
* 2812     0050.5689.37b4   dynamic  0         F      F    Eth1/49
* 2812     0050.5689.51f7   dynamic  0         F      F    Eth1/11
* 2812     0050.5689.5aff   dynamic  0         F      F    Eth1/49
* 2812     0050.5689.7d0e   dynamic  0         F      F    Eth1/49
* 2812     0050.5689.89c2   dynamic  0         F      F    Eth1/49
* 2812     0050.5689.9374   dynamic  0         F      F    Eth1/49
* 2812     0050.5689.affc   dynamic  0         F      F    Eth1/49
* 2812     0050.5689.f4cf   dynamic  0         F      F    Eth1/49
* 2812     0050.569c.44ce   dynamic  0         F      F    Eth1/49
* 2812     0050.56a6.4d26   dynamic  0         F      F    Eth1/49
* 2812     0050.56a6.ab7c   dynamic  0         F      F    Eth1/49
* 2812     225d.4072.2933   dynamic  0         F      F    Eth1/49
* 2812     8c94.1f18.e335   dynamic  0         F      F    Eth1/49
* 2812     ecce.1389.7802   dynamic  0         F      F    Eth1/49
* 2812     ecce.1389.8582   dynamic  0         F      F    Eth1/49
* 2813     0000.0c9f.fafd   dynamic  0         F      F    Eth1/49
* 2813     0015.5d3e.8dc5   dynamic  0         F      F    Eth1/49
* 2813     0015.5d3e.f306   dynamic  0         F      F    Eth1/49
* 2813     0015.5d3e.f307   dynamic  0         F      F    Eth1/49
* 2813     0015.5d3e.f610   dynamic  0         F      F    Eth1/49
* 2813     0015.5d3e.f616   dynamic  0         F      F    Eth1/49
* 2813     0015.5d3e.f618   dynamic  0         F      F    Eth1/49
* 2813     0015.5d49.42db   dynamic  0         F      F    Eth1/49
* 2813     0015.5d49.85c0   dynamic  0         F      F    Eth1/49
* 2813     0015.5d49.85c1   dynamic  0         F      F    Eth1/49
* 2813     0015.5d49.9fe7   dynamic  0         F      F    Eth1/49
* 2813     0015.5d49.a807   dynamic  0         F      F    Eth1/49
* 2813     0015.5d49.a827   dynamic  0         F      F    Eth1/49
* 2813     0015.5d49.a82e   dynamic  0         F      F    Eth1/49
* 2813     0015.5d49.a82f   dynamic  0         F      F    Eth1/49
* 2813     0015.5d49.a8ff   dynamic  0         F      F    Eth1/49
* 2813     0025.90d3.3bc3   dynamic  0         F      F    Eth1/49
* 2813     0025.90d3.3c1c   dynamic  0         F      F    Eth1/49
* 2813     0025.90d3.3c1d   dynamic  0         F      F    Eth1/49
* 2813     0025.90fd.c68c   dynamic  0         F      F    Eth1/49
* 2813     0025.90fd.c692   dynamic  0         F      F    Eth1/49
* 2813     0050.5689.16a2   dynamic  0         F      F    Eth1/49
* 2813     0050.5689.308a   dynamic  0         F      F    Eth1/49
* 2813     0050.5689.37d1   dynamic  0         F      F    Eth1/49
* 2813     0050.5689.5a26   dynamic  0         F      F    Eth1/49
* 2813     0050.5689.b0a3   dynamic  0         F      F    Eth1/49
* 2813     0050.5689.d01e   dynamic  0         F      F    Eth1/49
* 2813     0050.5692.181f   dynamic  0         F      F    Eth1/11
* 2813     0050.569c.4d52   dynamic  0         F      F    Eth1/49
* 2813     0050.569c.585b   dynamic  0         F      F    Eth1/49
* 2813     0050.569c.616f   dynamic  0         F      F    Eth1/49
* 2813     0050.569c.6c14   dynamic  0         F      F    Eth1/49
* 2813     0050.569c.7065   dynamic  0         F      F    Eth1/49
* 2813     0050.569c.7efd   dynamic  0         F      F    Po11
* 2813     0050.56a6.48a8   dynamic  0         F      F    Eth1/49
* 2813     00a0.981a.de31   dynamic  0         F      F    Eth1/49
* 2813     00a0.981a.de32   dynamic  0         F      F    Eth1/49
* 2813     00a0.981b.70f7   dynamic  0         F      F    Eth1/49
* 2813     00a0.981b.70f8   dynamic  0         F      F    Eth1/49
* 2813     00d0.2308.3705   dynamic  0         F      F    Eth1/49
* 2813     00e0.ec43.258d   dynamic  0         F      F    Eth1/49
* 2813     00e0.ec43.2721   dynamic  0         F      F    Eth1/49
* 2813     00e0.ec43.2777   dynamic  0         F      F    Eth1/49
* 2813     00e0.ec43.27f3   dynamic  0         F      F    Eth1/49
* 2813     0894.ef4c.ba0e   dynamic  0         F      F    Eth1/49
* 2813     0894.ef4c.ba65   dynamic  0         F      F    Eth1/49
* 2813     0894.ef4c.ba89   dynamic  0         F      F    Eth1/49
* 2813     0894.ef4c.bb3d   dynamic  0         F      F    Eth1/49
* 2813     0894.ef4c.bd55   dynamic  0         F      F    Eth1/49
* 2813     0894.ef4c.bdc1   dynamic  0         F      F    Eth1/49
* 2813     0cc4.7a0d.d238   dynamic  0         F      F    Eth1/49
* 2813     1c72.1dff.386a   dynamic  0         F      F    Eth1/49
* 2813     3448.edec.7f72   dynamic  0         F      F    Eth1/49
* 2813     40f2.e9c0.1420   dynamic  0         F      F    Eth1/49
* 2813     4cd9.8f46.9c1d   dynamic  0         F      F    Eth1/49
* 2813     6cae.8b2b.b670   dynamic  0         F      F    Eth1/49
* 2813     6cae.8b2e.0fc5   dynamic  0         F      F    Eth1/49
* 2813     6cae.8b2e.1581   dynamic  0         F      F    Eth1/49
* 2813     6cae.8b2e.d108   dynamic  0         F      F    Eth1/49
* 2813     6cae.8b2e.d5e0   dynamic  0         F      F    Eth1/49
* 2813     6cae.8b2e.d654   dynamic  0         F      F    Eth1/49
* 2813     6cae.8b2e.d7a9   dynamic  0         F      F    Eth1/49
* 2813     6cae.8b2e.d7c0   dynamic  0         F      F    Eth1/49
* 2813     6cae.8b2e.d908   dynamic  0         F      F    Eth1/49
* 2813     6cae.8b35.25e4   dynamic  0         F      F    Eth1/49
* 2813     7499.75cc.f4fe   dynamic  0         F      F    Eth1/49
* 2813     8c94.1f18.e335   dynamic  0         F      F    Eth1/49
* 2813     98be.9436.7454   dynamic  0         F      F    Eth1/49
* 2813     b07b.25c6.8a40   dynamic  0         F      F    Eth1/49
* 2813     ecce.1389.7802   dynamic  0         F      F    Eth1/49
* 2813     ecce.1389.8582   dynamic  0         F      F    Eth1/49
* 2814     0000.0c9f.fafe   dynamic  0         F      F    Eth1/49
* 2814     8c94.1f18.e335   dynamic  0         F      F    Eth1/49
* 2814     ecce.1389.8582   dynamic  0         F      F    Eth1/49
* 2815     0000.0c9f.faff   dynamic  0         F      F    Eth1/49
* 2815     8c94.1f18.e335   dynamic  0         F      F    Eth1/49
* 2815     ecce.1389.8582   dynamic  0         F      F    Eth1/49
* 2816     0000.0c9f.fb00   dynamic  0         F      F    Eth1/49
* 2816     3417.ebab.8495   dynamic  0         F      F    Eth1/49
* 2816     8c94.1f18.e335   dynamic  0         F      F    Eth1/49
* 2816     ecce.1389.8582   dynamic  0         F      F    Eth1/49
* 2817     0000.0c9f.fb01   dynamic  0         F      F    Eth1/49
* 2817     0001.2e33.fd3a   dynamic  0         F      F    Eth1/49
* 2817     0001.2e39.94a2   dynamic  0         F      F    Eth1/49
* 2817     0001.2e39.94a8   dynamic  0         F      F    Eth1/49
* 2817     0001.2e3c.043d   dynamic  0         F      F    Eth1/49
* 2817     0001.2e4b.c950   dynamic  0         F      F    Eth1/49
* 2817     0001.2e4b.c98b   dynamic  0         F      F    Eth1/49
* 2817     0010.7f8b.c7ee   dynamic  0         F      F    Eth1/49
* 2817     0010.7f8b.db40   dynamic  0         F      F    Eth1/49
* 2817     0010.7f8b.fb7d   dynamic  0         F      F    Eth1/49
* 2817     0010.7f9f.14e9   dynamic  0         F      F    Eth1/49
* 2817     0015.5d0f.0000   dynamic  0         F      F    Eth1/49
* 2817     0015.5d14.cc01   dynamic  0         F      F    Eth1/49
* 2817     0015.5d3e.f32d   dynamic  0         F      F    Eth1/49
* 2817     0015.5d3e.f3c9   dynamic  0         F      F    Eth1/49
* 2817     0015.5d3e.f6e1   dynamic  0         F      F    Eth1/49
* 2817     0015.5d48.5309   dynamic  0         F      F    Eth1/49
* 2817     0015.5d48.53db   dynamic  0         F      F    Eth1/49
* 2817     0015.5d49.88ac   dynamic  0         F      F    Eth1/49
* 2817     0015.5d49.9fdf   dynamic  0         F      F    Eth1/49
* 2817     0022.4d55.4bc6   dynamic  0         F      F    Eth1/49
* 2817     0023.244a.cfea   dynamic  0         F      F    Eth1/49
* 2817     0023.2466.1e83   dynamic  0         F      F    Eth1/49
* 2817     0050.5689.0108   dynamic  0         F      F    Eth1/49
* 2817     0050.5689.0407   dynamic  0         F      F    Eth1/49
* 2817     0050.5689.0422   dynamic  0         F      F    Eth1/49
* 2817     0050.5689.042a   dynamic  0         F      F    Eth1/49
* 2817     0050.5689.084c   dynamic  0         F      F    Eth1/49
* 2817     0050.5689.0ab1   dynamic  0         F      F    Eth1/49
* 2817     0050.5689.0d4a   dynamic  0         F      F    Eth1/49
* 2817     0050.5689.0ddc   dynamic  0         F      F    Eth1/49
* 2817     0050.5689.0e29   dynamic  0         F      F    Eth1/49
* 2817     0050.5689.0f47   dynamic  0         F      F    Eth1/49
* 2817     0050.5689.1006   dynamic  0         F      F    Eth1/49
* 2817     0050.5689.1c1e   dynamic  0         F      F    Eth1/49
* 2817     0050.5689.3011   dynamic  0         F      F    Eth1/49
* 2817     0050.5689.3e89   dynamic  0         F      F    Eth1/49
* 2817     0050.5689.3edb   dynamic  0         F      F    Eth1/49
* 2817     0050.5689.400e   dynamic  0         F      F    Eth1/49
* 2817     0050.5689.4154   dynamic  0         F      F    Eth1/49
* 2817     0050.5689.4173   dynamic  0         F      F    Eth1/49
* 2817     0050.5689.463d   dynamic  0         F      F    Eth1/49
* 2817     0050.5689.4d39   dynamic  0         F      F    Eth1/49
* 2817     0050.5689.4f55   dynamic  0         F      F    Eth1/49
* 2817     0050.5689.5062   dynamic  0         F      F    Eth1/49
* 2817     0050.5689.5519   dynamic  0         F      F    Eth1/49
* 2817     0050.5689.5999   dynamic  0         F      F    Eth1/49
* 2817     0050.5689.5ede   dynamic  0         F      F    Eth1/49
* 2817     0050.5689.600c   dynamic  0         F      F    Eth1/49
* 2817     0050.5689.654c   dynamic  0         F      F    Eth1/49
* 2817     0050.5689.6763   dynamic  0         F      F    Eth1/49
* 2817     0050.5689.6882   dynamic  0         F      F    Eth1/49
* 2817     0050.5689.6a70   dynamic  0         F      F    Eth1/49
* 2817     0050.5689.6e55   dynamic  0         F      F    Eth1/49
* 2817     0050.5689.76a7   dynamic  0         F      F    Eth1/49
* 2817     0050.5689.83f0   dynamic  0         F      F    Eth1/49
* 2817     0050.5689.8803   dynamic  0         F      F    Eth1/49
* 2817     0050.5689.89ac   dynamic  0         F      F    Eth1/49
* 2817     0050.5689.9c03   dynamic  0         F      F    Eth1/49
* 2817     0050.5689.9f28   dynamic  0         F      F    Eth1/49
* 2817     0050.5689.9ff8   dynamic  0         F      F    Eth1/49
* 2817     0050.5689.a433   dynamic  0         F      F    Eth1/49
* 2817     0050.5689.abdf   dynamic  0         F      F    Eth1/49
* 2817     0050.5689.b0ad   dynamic  0         F      F    Eth1/49
* 2817     0050.5689.b326   dynamic  0         F      F    Eth1/49
* 2817     0050.5689.b836   dynamic  0         F      F    Eth1/49
* 2817     0050.5689.c518   dynamic  0         F      F    Eth1/49
* 2817     0050.5689.d0cb   dynamic  0         F      F    Eth1/49
* 2817     0050.5689.d0fd   dynamic  0         F      F    Eth1/49
* 2817     0050.5689.e22d   dynamic  0         F      F    Eth1/49
* 2817     0050.5689.eaba   dynamic  0         F      F    Eth1/49
* 2817     0050.5689.ef45   dynamic  0         F      F    Eth1/49
* 2817     0050.5689.efdb   dynamic  0         F      F    Eth1/49
* 2817     00e0.4c00.0c10   dynamic  0         F      F    Eth1/49
* 2817     00e0.4c08.05ac   dynamic  0         F      F    Eth1/49
* 2817     00e0.4c08.05ad   dynamic  0         F      F    Eth1/49
* 2817     00e0.4c68.02f6   dynamic  0         F      F    Eth1/49
* 2817     00e0.4c68.0808   dynamic  0         F      F    Eth1/49
* 2817     0c4d.e9bd.b90f   dynamic  0         F      F    Eth1/49
* 2817     0c4d.e9c9.202d   dynamic  0         F      F    Eth1/49
* 2817     10dd.b1a3.ce65   dynamic  0         F      F    Eth1/49
* 2817     14fe.b5e0.8f69   dynamic  0         F      F    Eth1/49
* 2817     1803.7322.5255   dynamic  0         F      F    Eth1/49
* 2817     1803.7322.5a59   dynamic  0         F      F    Eth1/49
* 2817     1803.7323.583a   dynamic  0         F      F    Eth1/49
* 2817     1803.7330.fca4   dynamic  0         F      F    Eth1/49
* 2817     1803.7351.374f   dynamic  0         F      F    Eth1/49
* 2817     1803.7351.3aad   dynamic  0         F      F    Eth1/49
* 2817     1803.73d1.90ed   dynamic  0         F      F    Eth1/49
* 2817     1803.73d1.942a   dynamic  0         F      F    Eth1/49
* 2817     1803.73d1.9596   dynamic  0         F      F    Eth1/49
* 2817     1803.73d1.97e2   dynamic  0         F      F    Eth1/49
* 2817     1803.73da.b7bd   dynamic  0         F      F    Eth1/49
* 2817     1803.73da.e588   dynamic  0         F      F    Eth1/49
* 2817     1803.73da.e752   dynamic  0         F      F    Eth1/49
* 2817     1803.73e0.1aa1   dynamic  0         F      F    Eth1/49
* 2817     1866.da16.319d   dynamic  0         F      F    Eth1/49
* 2817     1866.da16.7cc8   dynamic  0         F      F    Eth1/49
* 2817     1866.da1a.a02f   dynamic  0         F      F    Eth1/49
* 2817     1866.da1a.a0d9   dynamic  0         F      F    Eth1/49
* 2817     1866.da1a.a2be   dynamic  0         F      F    Eth1/49
* 2817     1866.da1a.fac9   dynamic  0         F      F    Eth1/49
* 2817     1866.da1a.feb7   dynamic  0         F      F    Eth1/49
* 2817     1866.da1a.ff24   dynamic  0         F      F    Eth1/49
* 2817     1866.da1a.ff6a   dynamic  0         F      F    Eth1/49
* 2817     1866.da3b.5043   dynamic  0         F      F    Eth1/49
* 2817     1866.da41.905a   dynamic  0         F      F    Eth1/49
* 2817     24be.05e9.7922   dynamic  0         F      F    Eth1/49
* 2817     2816.a807.2364   dynamic  0         F      F    Eth1/49
* 2817     309c.23de.8326   dynamic  0         F      F    Eth1/49
* 2817     3417.eb97.826b   dynamic  0         F      F    Eth1/49
* 2817     3417.eba3.38bf   dynamic  0         F      F    Eth1/49
* 2817     3417.ebab.87a2   dynamic  0         F      F    Eth1/49
* 2817     3417.ebab.fa7f   dynamic  0         F      F    Eth1/49
* 2817     3417.ebbf.f854   dynamic  0         F      F    Eth1/49
* 2817     3448.ed90.cecd   dynamic  0         F      F    Eth1/49
* 2817     3473.5ad5.c647   dynamic  0         F      F    Eth1/49
* 2817     38f9.d30f.d2c7   dynamic  0         F      F    Eth1/49
* 2817     38f9.d310.a8ae   dynamic  0         F      F    Eth1/49
* 2817     3c2c.30ca.492d   dynamic  0         F      F    Eth1/49
* 2817     3c7d.0a1a.577e   dynamic  0         F      F    Eth1/49
* 2817     3cdf.1eaf.8e80   dynamic  0         F      F    Eth1/49
* 2817     40cb.c0f1.b283   dynamic  0         F      F    Eth1/49
* 2817     484d.7edb.163d   dynamic  0         F      F    Eth1/49
* 2817     484d.7edb.1648   dynamic  0         F      F    Eth1/49
* 2817     509a.4c03.490d   dynamic  0         F      F    Eth1/49
* 2817     509a.4c03.494c   dynamic  0         F      F    Eth1/49
* 2817     509a.4c04.057a   dynamic  0         F      F    Eth1/49
* 2817     509a.4c04.0a09   dynamic  0         F      F    Eth1/49
* 2817     509a.4c04.0a4e   dynamic  0         F      F    Eth1/49
* 2817     509a.4c04.0a50   dynamic  0         F      F    Eth1/49
* 2817     509a.4c04.0ac7   dynamic  0         F      F    Eth1/49
* 2817     509a.4c04.0b26   dynamic  0         F      F    Eth1/49
* 2817     509a.4c17.bf5d   dynamic  0         F      F    Eth1/49
* 2817     509a.4c54.617e   dynamic  0         F      F    Eth1/49
* 2817     5c26.0a5a.006c   dynamic  0         F      F    Eth1/49
* 2817     6400.6a4a.8949   dynamic  0         F      F    Eth1/49
* 2817     6400.6a4a.8ce2   dynamic  0         F      F    Eth1/49
* 2817     6400.6a5b.a427   dynamic  0         F      F    Eth1/49
* 2817     6400.6a72.ef43   dynamic  0         F      F    Eth1/49
* 2817     6416.7f3e.f7d7   dynamic  0         F      F    Eth1/49
* 2817     685b.35c3.d84e   dynamic  0         F      F    Eth1/49
* 2817     70b5.e80e.15e5   dynamic  0         F      F    Eth1/49
* 2817     70b5.e826.a251   dynamic  0         F      F    Eth1/49
* 2817     70b5.e827.4fc5   dynamic  0         F      F    Eth1/49
* 2817     7824.af9e.b051   dynamic  0         F      F    Eth1/49
* 2817     782b.cbad.c942   dynamic  0         F      F    Eth1/49
* 2817     782b.cbb7.de16   dynamic  0         F      F    Eth1/49
* 2817     782b.cbb7.de7e   dynamic  0         F      F    Eth1/49
* 2817     782b.cbb7.fd57   dynamic  0         F      F    Eth1/49
* 2817     7cd3.0a1c.2e22   dynamic  0         F      F    Eth1/49
* 2817     7cd3.0a1c.3e49   dynamic  0         F      F    Eth1/49
* 2817     7cd3.0a1c.fdce   dynamic  0         F      F    Eth1/49
* 2817     803f.5d08.66a9   dynamic  0         F      F    Eth1/49
* 2817     803f.5d0a.8eb0   dynamic  0         F      F    Eth1/49
* 2817     80ee.7309.cb00   dynamic  0         F      F    Eth1/49
* 2817     8c94.1f18.e335   dynamic  0         F      F    Eth1/49
* 2817     8cec.4b5d.deb3   dynamic  0         F      F    Eth1/49
* 2817     8cec.4b5d.e470   dynamic  0         F      F    Eth1/49
* 2817     8cec.4b5d.e4af   dynamic  0         F      F    Eth1/49
* 2817     8cec.4b6e.ea2d   dynamic  0         F      F    Eth1/49
* 2817     8cec.4b6f.7954   dynamic  0         F      F    Eth1/49
* 2817     8cec.4b6f.796b   dynamic  0         F      F    Eth1/49
* 2817     8cec.4b6f.7a36   dynamic  0         F      F    Eth1/49
* 2817     8cec.4b6f.7a6e   dynamic  0         F      F    Eth1/49
* 2817     8cec.4b6f.9e51   dynamic  0         F      F    Eth1/49
* 2817     8cec.4b6f.9e84   dynamic  0         F      F    Eth1/49
* 2817     8cec.4b70.016f   dynamic  0         F      F    Eth1/49
* 2817     8cec.4b88.8d99   dynamic  0         F      F    Eth1/49
* 2817     8cec.4b89.bcb5   dynamic  0         F      F    Eth1/49
* 2817     8cec.4ba4.b9b7   dynamic  0         F      F    Eth1/49
* 2817     8cec.4ba8.e03c   dynamic  0         F      F    Eth1/49
* 2817     8cec.4ba8.e12d   dynamic  0         F      F    Eth1/49
* 2817     8cec.4ba8.fe22   dynamic  0         F      F    Eth1/49
* 2817     90b1.1c63.8564   dynamic  0         F      F    Eth1/49
* 2817     90b1.1c74.9351   dynamic  0         F      F    Eth1/49
* 2817     9810.e8f3.3e44   dynamic  0         F      F    Eth1/49
* 2817     9890.96a6.06b2   dynamic  0         F      F    Eth1/49
* 2817     9890.96b5.bf7c   dynamic  0         F      F    Eth1/49
* 2817     9890.96cf.b5e7   dynamic  0         F      F    Eth1/49
* 2817     9890.96d1.95d5   dynamic  0         F      F    Eth1/49
* 2817     9890.96d1.9843   dynamic  0         F      F    Eth1/49
* 2817     9890.96d1.9871   dynamic  0         F      F    Eth1/49
* 2817     9890.96d1.9891   dynamic  0         F      F    Eth1/49
* 2817     9890.96d1.9aa4   dynamic  0         F      F    Eth1/49
* 2817     9890.96d1.9b15   dynamic  0         F      F    Eth1/49
* 2817     98e7.43db.df27   dynamic  0         F      F    Eth1/49
* 2817     a01e.0b0d.392b   dynamic  0         F      F    Eth1/49
* 2817     a01e.0b0d.3967   dynamic  0         F      F    Eth1/49
* 2817     a01e.0b0d.397b   dynamic  0         F      F    Eth1/49
* 2817     a01e.0b0d.3c97   dynamic  0         F      F    Eth1/49
* 2817     a01e.0b0d.5a26   dynamic  0         F      F    Eth1/49
* 2817     a0ce.c807.8c44   dynamic  0         F      F    Eth1/49
* 2817     a4bb.6dde.8dea   dynamic  0         F      F    Eth1/49
* 2817     ac87.a307.60ca   dynamic  0         F      F    Eth1/49
* 2817     accc.8e76.1153   dynamic  0         F      F    Eth1/49
* 2817     accc.8e76.115c   dynamic  0         F      F    Eth1/49
* 2817     b07b.250c.e243   dynamic  0         F      F    Eth1/49
* 2817     b07b.250e.1a0e   dynamic  0         F      F    Eth1/49
* 2817     b07b.259b.397a   dynamic  0         F      F    Eth1/49
* 2817     b07b.259b.3aa9   dynamic  0         F      F    Eth1/49
* 2817     b8ca.3a91.434f   dynamic  0         F      F    Eth1/49
* 2817     b8ca.3a9b.1199   dynamic  0         F      F    Eth1/49
* 2817     b8ca.3aa2.3554   dynamic  0         F      F    Eth1/49
* 2817     b8ca.3aa2.9437   dynamic  0         F      F    Eth1/49
* 2817     b8ca.3ab7.df31   dynamic  0         F      F    Eth1/49
* 2817     b8ca.3ab9.d9ef   dynamic  0         F      F    Eth1/49
* 2817     c025.a506.2598   dynamic  0         F      F    Eth1/49
* 2817     c82a.141c.e99a   dynamic  0         F      F    Eth1/49
* 2817     d43d.7ee2.2f78   dynamic  0         F      F    Eth1/49
* 2817     d4be.d998.a3f9   dynamic  0         F      F    Eth1/49
* 2817     d89e.f329.6e6c   dynamic  0         F      F    Eth1/49
* 2817     d8cb.8a18.bc49   dynamic  0         F      F    Eth1/49
* 2817     d8eb.97b6.7f91   dynamic  0         F      F    Eth1/49
* 2817     e03f.49ac.58b0   dynamic  0         F      F    Eth1/49
* 2817     e0d5.5eaf.6c5b   dynamic  0         F      F    Eth1/49
* 2817     e0d5.5eaf.ff7d   dynamic  0         F      F    Eth1/49
* 2817     e454.e89c.5d4a   dynamic  0         F      F    Eth1/49
* 2817     e454.e89c.5e7c   dynamic  0         F      F    Eth1/49
* 2817     e454.e89c.5f96   dynamic  0         F      F    Eth1/49
* 2817     e454.e8d7.949f   dynamic  0         F      F    Eth1/49
* 2817     ecce.1389.7802   dynamic  0         F      F    Eth1/49
* 2817     ecce.1389.8582   dynamic  0         F      F    Eth1/49
* 2817     f018.98ef.7eb4   dynamic  0         F      F    Eth1/49
* 2817     f018.98f3.c877   dynamic  0         F      F    Eth1/49
* 2817     f01d.bc97.6258   dynamic  0         F      F    Eth1/49
* 2817     f04d.a2fc.b333   dynamic  0         F      F    Eth1/49
* 2817     f8b1.56a0.4b1f   dynamic  0         F      F    Eth1/49
* 2817     f8b1.56a0.59cf   dynamic  0         F      F    Eth1/49
* 2817     f8b1.56e3.88eb   dynamic  0         F      F    Eth1/49
* 2818     0000.0c9f.fb02   dynamic  0         F      F    Eth1/49
* 2818     0cc4.7a3a.2771   dynamic  0         F      F    Eth1/49
* 2818     7cd3.0ac6.361a   dynamic  0         F      F    Eth1/49
* 2818     7cd3.0ac6.37d0   dynamic  0         F      F    Eth1/49
* 2818     7cd3.0ac6.38de   dynamic  0         F      F    Eth1/49
* 2818     7cd3.0ac6.3b5a   dynamic  0         F      F    Eth1/49
* 2818     7cd3.0ac6.3db2   dynamic  0         F      F    Eth1/49
* 2818     7cd3.0ac6.3df4   dynamic  0         F      F    Eth1/49
* 2818     7cd3.0ac6.4028   dynamic  0         F      F    Eth1/49
* 2818     7cd3.0ac6.42e6   dynamic  0         F      F    Eth1/49
* 2818     7cd3.0ac6.4484   dynamic  0         F      F    Eth1/49
* 2818     7cd3.0ac7.20e6   dynamic  0         F      F    Eth1/49
* 2818     8c94.1f18.e335   dynamic  0         F      F    Eth1/49
* 2818     ac1f.6b34.e6b5   dynamic  0         F      F    Eth1/49
* 2818     ac1f.6b34.e715   dynamic  0         F      F    Eth1/49
* 2818     e806.88cb.a0f8   dynamic  0         F      F    Eth1/49
* 2818     ecce.1389.7802   dynamic  0         F      F    Eth1/49
* 2818     ecce.1389.8582   dynamic  0         F      F    Eth1/49
* 2819     0000.0c9f.fb03   dynamic  0         F      F    Eth1/49
* 2819     001e.8f4f.79d9   dynamic  0         F      F    Eth1/49
* 2819     001e.8f50.5c16   dynamic  0         F      F    Eth1/49
* 2819     00bb.c1cc.4169   dynamic  0         F      F    Eth1/49
* 2819     00bb.c1cc.458c   dynamic  0         F      F    Eth1/49
* 2819     00bb.c1cc.75cb   dynamic  0         F      F    Eth1/49
* 2819     00bb.c1cc.7b31   dynamic  0         F      F    Eth1/49
* 2819     00bb.c1cc.a85f   dynamic  0         F      F    Eth1/49
* 2819     00bb.c1cc.d440   dynamic  0         F      F    Eth1/49
* 2819     00bb.c1cc.eaf6   dynamic  0         F      F    Eth1/49
* 2819     00bb.c1cd.1729   dynamic  0         F      F    Eth1/49
* 2819     00bb.c1cd.172a   dynamic  0         F      F    Eth1/49
* 2819     00bb.c1cd.25b0   dynamic  0         F      F    Eth1/49
* 2819     101f.7444.99e6   dynamic  0         F      F    Eth1/49
* 2819     180c.aca1.636b   dynamic  0         F      F    Eth1/49
* 2819     48ba.4e37.ecaa   dynamic  0         F      F    Eth1/49
* 2819     48ba.4ee1.632e   dynamic  0         F      F    Eth1/49
* 2819     6012.8bd2.c481   dynamic  0         F      F    Eth1/49
* 2819     705a.0fa8.dc21   dynamic  0         F      F    Eth1/49
* 2819     705a.0fa9.c311   dynamic  0         F      F    Eth1/49
* 2819     705a.0fa9.c313   dynamic  0         F      F    Eth1/49
* 2819     705a.0fa9.c3c7   dynamic  0         F      F    Eth1/49
* 2819     8c94.1f18.e335   dynamic  0         F      F    Eth1/49
* 2819     b4b5.2ff4.ef3a   dynamic  0         F      F    Eth1/49
* 2819     c8d3.ff0e.e273   dynamic  0         F      F    Eth1/49
* 2819     e8d8.d194.e0f0   dynamic  0         F      F    Eth1/49
* 2819     ecce.1389.7802   dynamic  0         F      F    Eth1/49
* 2819     ecce.1389.8582   dynamic  0         F      F    Eth1/49
* 2819     f09f.fc14.b7b2   dynamic  0         F      F    Eth1/49
* 2819     f430.b927.48a5   dynamic  0         F      F    Eth1/49
* 2819     f439.09bd.d2e2   dynamic  0         F      F    Eth1/49
* 2819     f481.39c4.d6b1   dynamic  0         F      F    Eth1/49
* 2819     f481.39c5.785f   dynamic  0         F      F    Eth1/49
* 2819     f481.39c5.fbf4   dynamic  0         F      F    Eth1/49
* 2819     f481.39c6.8c82   dynamic  0         F      F    Eth1/49
* 2819     f481.39c6.95b0   dynamic  0         F      F    Eth1/49
* 2819     f481.39c7.e011   dynamic  0         F      F    Eth1/49
* 2819     f4a9.97ad.d377   dynamic  0         F      F    Eth1/49
* 2819     f4a9.97ad.d378   dynamic  0         F      F    Eth1/49
* 2819     f4a9.97ae.450b   dynamic  0         F      F    Eth1/49
* 2819     f4a9.97b0.fee6   dynamic  0         F      F    Eth1/49
* 2820     0000.0c9f.fb04   dynamic  0         F      F    Eth1/49
* 2820     0015.5d49.a800   dynamic  0         F      F    Eth1/49
* 2820     0050.5689.72f6   dynamic  0         F      F    Eth1/49
* 2820     8c94.1f18.e335   dynamic  0         F      F    Eth1/49
* 2820     ecce.1389.7802   dynamic  0         F      F    Eth1/49
* 2820     ecce.1389.8582   dynamic  0         F      F    Eth1/49
* 2823     0000.0c9f.fb07   dynamic  0         F      F    Eth1/49
* 2823     00c0.b777.1ac7   dynamic  0         F      F    Eth1/49
* 2823     8c94.1f18.e335   dynamic  0         F      F    Eth1/49
* 2823     ecce.1389.8582   dynamic  0         F      F    Eth1/49
* 2824     0000.0c9f.fb08   dynamic  0         F      F    Eth1/49
* 2824     0010.9b27.0246   dynamic  0         F      F    Eth1/49
* 2824     0010.9b27.05b6   dynamic  0         F      F    Eth1/49
* 2824     0010.9b27.12e0   dynamic  0         F      F    Eth1/49
* 2824     0010.9b27.1330   dynamic  0         F      F    Eth1/49
* 2824     0010.9b27.1378   dynamic  0         F      F    Eth1/49
* 2824     0010.9b27.13c0   dynamic  0         F      F    Eth1/49
* 2824     0015.5d3e.f617   dynamic  0         F      F    Eth1/49
* 2824     0015.5d3e.f619   dynamic  0         F      F    Eth1/49
* 2824     0015.5d48.53ed   dynamic  0         F      F    Eth1/49
* 2824     0015.5d48.53ee   dynamic  0         F      F    Eth1/49
* 2824     0015.5d48.53fe   dynamic  0         F      F    Eth1/49
* 2824     0015.5d49.42dc   dynamic  0         F      F    Eth1/49
* 2824     0015.5d49.85c2   dynamic  0         F      F    Eth1/49
* 2824     0015.5d49.a804   dynamic  0         F      F    Eth1/49
* 2824     0050.569c.3808   dynamic  0         F      F    Eth1/49
* 2824     00a0.981d.7f08   dynamic  0         F      F    Eth1/49
* 2824     00a0.981d.7f09   dynamic  0         F      F    Eth1/49
* 2824     00a0.981d.94d7   dynamic  0         F      F    Eth1/49
* 2824     00d0.2368.3705   dynamic  0         F      F    Eth1/49
* 2824     00d0.23a8.3705   dynamic  0         F      F    Eth1/49
* 2824     00d0.23b8.3705   dynamic  0         F      F    Eth1/49
* 2824     00e0.ed1b.f80c   dynamic  0         F      F    Eth1/5
* 2824     00e0.ed1b.f80d   dynamic  0         F      F    Eth1/6
* 2824     00e0.ed31.c6f6   dynamic  0         F      F    Eth1/49
* 2824     00e0.ed31.c6f7   dynamic  0         F      F    Eth1/49
* 2824     00e0.ed41.8e1e   dynamic  0         F      F    Eth1/7
* 2824     00e0.ed41.8e1f   dynamic  0         F      F    Eth1/8
* 2824     00e0.ed42.aaa8   dynamic  0         F      F    Eth1/49
* 2824     02a0.981a.de2c   dynamic  0         F      F    Eth1/49
* 2824     0c42.a1f4.8940   dynamic  0         F      F    Eth1/10
* 2824     40f2.e9c2.13c0   dynamic  0         F      F    Eth1/49
* 2824     6cae.8b2c.a0d0   dynamic  0         F      F    Eth1/49
* 2824     6cae.8b2d.1f48   dynamic  0         F      F    Eth1/49
* 2824     6cae.8b2d.2ac0   dynamic  0         F      F    Eth1/49
* 2824     6cae.8b2f.2c80   dynamic  0         F      F    Eth1/49
* 2824     6cae.8b2f.3630   dynamic  0         F      F    Eth1/49
* 2824     6cae.8b2f.3718   dynamic  0         F      F    Eth1/49
* 2824     6cae.8b2f.39c0   dynamic  0         F      F    Eth1/49
* 2824     6cae.8b2f.39f0   dynamic  0         F      F    Eth1/49
* 2824     6cae.8b2f.3c80   dynamic  0         F      F    Eth1/49
* 2824     6cae.8b33.e498   dynamic  0         F      F    Eth1/49
* 2824     8c94.1f18.e335   dynamic  0         F      F    Eth1/49
* 2824     98be.9437.00f0   dynamic  0         F      F    Eth1/49
* 2824     ecce.1389.7802   dynamic  0         F      F    Eth1/49
* 2824     ecce.1389.8582   dynamic  0         F      F    Eth1/49
* 2824     f4e9.d467.20a0   dynamic  0         F      F    Eth1/49
* 2824     f4e9.d479.9cd5   dynamic  0         F      F    Eth1/49
* 2825     0000.0c9f.fb09   dynamic  0         F      F    Eth1/49
* 2825     002a.6a32.be01   dynamic  0         F      F    Eth1/49
* 2825     7499.75d0.4efe   dynamic  0         F      F    Eth1/49
* 2825     8c94.1f18.e335   dynamic  0         F      F    Eth1/49
* 2825     ecce.1389.7802   dynamic  0         F      F    Eth1/49
* 2825     ecce.1389.8582   dynamic  0         F      F    Eth1/49
* 2826     0000.0c9f.fb0a   dynamic  0         F      F    Eth1/49
* 2826     2829.8604.b567   dynamic  0         F      F    Eth1/49
* 2826     2829.8607.5c3b   dynamic  0         F      F    Eth1/49
* 2826     2829.8607.5c43   dynamic  0         F      F    Eth1/49
* 2826     2829.8607.5c83   dynamic  0         F      F    Eth1/49
* 2826     2829.8607.5c94   dynamic  0         F      F    Eth1/49
* 2826     2829.8607.5c9c   dynamic  0         F      F    Eth1/49
* 2826     2829.8607.5cc7   dynamic  0         F      F    Eth1/49
* 2826     2829.8607.5cde   dynamic  0         F      F    Eth1/49
* 2826     8c94.1f18.e335   dynamic  0         F      F    Eth1/49
* 2826     9884.e3b2.7ac5   dynamic  0         F      F    Eth1/49
* 2826     ecce.1389.8582   dynamic  0         F      F    Eth1/49
* 2827     0000.0c9f.fb0b   dynamic  0         F      F    Eth1/49
* 2827     1065.3036.3917   dynamic  0         F      F    Eth1/49
* 2827     1803.7322.b13b   dynamic  0         F      F    Eth1/49
* 2827     1803.7351.3742   dynamic  0         F      F    Eth1/49
* 2827     1803.73d1.91cb   dynamic  0         F      F    Eth1/49
* 2827     1803.73d1.94bd   dynamic  0         F      F    Eth1/49
* 2827     1803.73d1.97b9   dynamic  0         F      F    Eth1/49
* 2827     1803.73d1.97cc   dynamic  0         F      F    Eth1/49
* 2827     1803.73d1.97fc   dynamic  0         F      F    Eth1/49
* 2827     1803.73d1.9818   dynamic  0         F      F    Eth1/49
* 2827     1803.73d1.989e   dynamic  0         F      F    Eth1/49
* 2827     1803.73da.e591   dynamic  0         F      F    Eth1/49
* 2827     1803.73da.e709   dynamic  0         F      F    Eth1/49
* 2827     1803.73da.e949   dynamic  0         F      F    Eth1/49
* 2827     1860.249d.6bd9   dynamic  0         F      F    Eth1/49
* 2827     1866.da1b.1f72   dynamic  0         F      F    Eth1/49
* 2827     18db.f230.037a   dynamic  0         F      F    Eth1/49
* 2827     2816.a804.7809   dynamic  0         F      F    Eth1/49
* 2827     3417.ebab.8967   dynamic  0         F      F    Eth1/49
* 2827     3417.ebab.8aa0   dynamic  0         F      F    Eth1/49
* 2827     3417.ebac.0d83   dynamic  0         F      F    Eth1/49
* 2827     3417.ebad.f7d3   dynamic  0         F      F    Eth1/49
* 2827     3417.ebd7.9d84   dynamic  0         F      F    Eth1/49
* 2827     3417.ebd7.a9fd   dynamic  0         F      F    Eth1/49
* 2827     34e6.d71a.ffda   dynamic  0         F      F    Eth1/49
* 2827     38f9.d316.5306   dynamic  0         F      F    Eth1/49
* 2827     3ccd.365d.6a6f   dynamic  0         F      F    Eth1/49
* 2827     5cf9.dd6b.240b   dynamic  0         F      F    Eth1/49
* 2827     6400.6a86.3dbf   dynamic  0         F      F    Eth1/49
* 2827     7069.5aec.1b38   dynamic  0         F      F    Eth1/49
* 2827     70b5.e818.e675   dynamic  0         F      F    Eth1/49
* 2827     782b.cba9.24e6   dynamic  0         F      F    Eth1/49
* 2827     7872.5d00.faaa   dynamic  0         F      F    Eth1/49
* 2827     7872.5d09.eb16   dynamic  0         F      F    Eth1/49
* 2827     8c94.1f18.e335   dynamic  0         F      F    Eth1/49
* 2827     8cec.4b8c.3e5f   dynamic  0         F      F    Eth1/49
* 2827     9890.96d1.98a1   dynamic  0         F      F    Eth1/49
* 2827     9890.96d1.9963   dynamic  0         F      F    Eth1/49
* 2827     98e7.43b5.ed64   dynamic  0         F      F    Eth1/49
* 2827     98e7.43e6.fcb8   dynamic  0         F      F    Eth1/49
* 2827     a01e.0b0d.640b   dynamic  0         F      F    Eth1/49
* 2827     a4bb.6dde.a631   dynamic  0         F      F    Eth1/49
* 2827     ac9e.1783.5b3d   dynamic  0         F      F    Eth1/49
* 2827     b07b.2511.1ddd   dynamic  0         F      F    Eth1/49
* 2827     b885.8499.9aee   dynamic  0         F      F    Eth1/49
* 2827     b8ca.3aa2.03de   dynamic  0         F      F    Eth1/49
* 2827     b8ca.3aa2.362c   dynamic  0         F      F    Eth1/49
* 2827     d4be.d99e.7277   dynamic  0         F      F    Eth1/49
* 2827     e454.e89d.3d7e   dynamic  0         F      F    Eth1/49
* 2827     ecce.1389.7802   dynamic  0         F      F    Eth1/49
* 2827     ecce.1389.8582   dynamic  0         F      F    Eth1/49
* 2827     f8b1.56a0.5acd   dynamic  0         F      F    Eth1/49
* 2827     f8b1.56a0.60cf   dynamic  0         F      F    Eth1/49
* 2831     0000.0c9f.fb0f   dynamic  0         F      F    Eth1/49
* 2831     8c94.1f18.e335   dynamic  0         F      F    Eth1/49
* 2831     ecce.1389.8582   dynamic  0         F      F    Eth1/49
* 2870     0000.0c9f.fb36   dynamic  0         F      F    Eth1/49
* 2870     0010.7fcc.2c26   dynamic  0         F      F    Eth1/49
* 2870     0015.5d12.0001   dynamic  0         F      F    Eth1/49
* 2870     0015.5d12.0002   dynamic  0         F      F    Eth1/49
* 2870     0015.5d12.0003   dynamic  0         F      F    Eth1/49
* 2870     0015.5d12.0004   dynamic  0         F      F    Eth1/49
* 2870     0015.5d12.0005   dynamic  0         F      F    Eth1/49
* 2870     0015.5d12.0006   dynamic  0         F      F    Eth1/49
* 2870     0015.5d3e.ab00   dynamic  0         F      F    Eth1/49
* 2870     0015.5d3e.ab01   dynamic  0         F      F    Eth1/49
* 2870     0015.5d3e.ab02   dynamic  0         F      F    Eth1/49
* 2870     0015.5d3e.ab03   dynamic  0         F      F    Eth1/49
* 2870     0015.5d3e.ab04   dynamic  0         F      F    Eth1/49
* 2870     0015.5d3e.ab05   dynamic  0         F      F    Eth1/49
* 2870     0015.5d3e.ab06   dynamic  0         F      F    Eth1/49
* 2870     0015.5d3e.ab07   dynamic  0         F      F    Eth1/49
* 2870     0015.5d3e.ab08   dynamic  0         F      F    Eth1/49
* 2870     0015.5d3e.ab09   dynamic  0         F      F    Eth1/49
* 2870     0015.5d49.a846   dynamic  0         F      F    Eth1/49
* 2870     0015.5d49.a84d   dynamic  0         F      F    Eth1/49
* 2870     0015.5d49.a852   dynamic  0         F      F    Eth1/49
* 2870     0015.5d49.a858   dynamic  0         F      F    Eth1/49
* 2870     0015.5d49.a868   dynamic  0         F      F    Eth1/49
* 2870     0015.5d49.a876   dynamic  0         F      F    Eth1/49
* 2870     0015.5d49.a878   dynamic  0         F      F    Eth1/49
* 2870     0015.5d49.a87b   dynamic  0         F      F    Eth1/49
* 2870     0015.5d49.a87c   dynamic  0         F      F    Eth1/49
* 2870     0015.5d49.a87d   dynamic  0         F      F    Eth1/49
* 2870     0015.5da5.0000   dynamic  0         F      F    Eth1/49
* 2870     0015.5da5.0001   dynamic  0         F      F    Eth1/49
* 2870     0015.5da5.0002   dynamic  0         F      F    Eth1/49
* 2870     0015.5da5.0003   dynamic  0         F      F    Eth1/49
* 2870     0015.5da5.0004   dynamic  0         F      F    Eth1/49
* 2870     0015.5da5.0005   dynamic  0         F      F    Eth1/49
* 2870     0050.5689.a9a6   dynamic  0         F      F    Eth1/49
* 2870     3417.ebc5.f677   dynamic  0         F      F    Eth1/49
* 2870     509a.4c11.f5fc   dynamic  0         F      F    Eth1/49
* 2870     509a.4c1b.0de9   dynamic  0         F      F    Eth1/49
* 2870     7cd3.0a1c.2eb3   dynamic  0         F      F    Eth1/49
* 2870     7cd3.0a1c.58fe   dynamic  0         F      F    Eth1/49
* 2870     7cd3.0a1c.68bb   dynamic  0         F      F    Eth1/49
* 2870     7cd3.0a1c.e9e0   dynamic  0         F      F    Eth1/49
* 2870     8c94.1f18.e335   dynamic  0         F      F    Eth1/49
* 2870     8cec.4b5a.8558   dynamic  0         F      F    Eth1/49
* 2870     8cec.4b5a.8839   dynamic  0         F      F    Eth1/49
* 2870     8cec.4b5a.894a   dynamic  0         F      F    Eth1/49
* 2870     8cec.4b5a.895a   dynamic  0         F      F    Eth1/49
* 2870     8cec.4b5a.899d   dynamic  0         F      F    Eth1/49
* 2870     8cec.4b5a.8ad5   dynamic  0         F      F    Eth1/49
* 2870     8cec.4b5a.8b55   dynamic  0         F      F    Eth1/49
* 2870     8cec.4b5b.820c   dynamic  0         F      F    Eth1/49
* 2870     8cec.4b5b.8210   dynamic  0         F      F    Eth1/49
* 2870     8cec.4b5b.8223   dynamic  0         F      F    Eth1/49
* 2870     8cec.4b5b.8224   dynamic  0         F      F    Eth1/49
* 2870     8cec.4b5b.8279   dynamic  0         F      F    Eth1/49
* 2870     8cec.4b5b.82a6   dynamic  0         F      F    Eth1/49
* 2870     8cec.4b5b.82a8   dynamic  0         F      F    Eth1/49
* 2870     8cec.4b5b.82cf   dynamic  0         F      F    Eth1/49
* 2870     8cec.4b5b.c6a5   dynamic  0         F      F    Eth1/49
* 2870     8cec.4b5b.c6e5   dynamic  0         F      F    Eth1/49
* 2870     8cec.4b5b.c6e6   dynamic  0         F      F    Eth1/49
* 2870     8cec.4b5b.c708   dynamic  0         F      F    Eth1/49
* 2870     8cec.4b5b.c709   dynamic  0         F      F    Eth1/49
* 2870     8cec.4b5b.c730   dynamic  0         F      F    Eth1/49
* 2870     8cec.4b5b.c733   dynamic  0         F      F    Eth1/49
* 2870     8cec.4b5b.c783   dynamic  0         F      F    Eth1/49
* 2870     8cec.4b5b.c84f   dynamic  0         F      F    Eth1/49
* 2870     8cec.4b5b.c8b6   dynamic  0         F      F    Eth1/49
* 2870     8cec.4b5b.c9d8   dynamic  0         F      F    Eth1/49
* 2870     8cec.4b5b.ca37   dynamic  0         F      F    Eth1/49
* 2870     8cec.4b5d.dd1e   dynamic  0         F      F    Eth1/49
* 2870     8cec.4b5d.dda2   dynamic  0         F      F    Eth1/49
* 2870     8cec.4b5d.de0a   dynamic  0         F      F    Eth1/49
* 2870     8cec.4b5d.df39   dynamic  0         F      F    Eth1/49
* 2870     8cec.4b5d.e165   dynamic  0         F      F    Eth1/49
* 2870     8cec.4b5d.e2d5   dynamic  0         F      F    Eth1/49
* 2870     8cec.4b5d.e4ae   dynamic  0         F      F    Eth1/49
* 2870     8cec.4bc2.d7bc   dynamic  0         F      F    Eth1/49
* 2870     8cec.4bc2.d900   dynamic  0         F      F    Eth1/49
* 2870     ecce.1389.7802   dynamic  0         F      F    Eth1/49
* 2870     ecce.1389.8582   dynamic  0         F      F    Eth1/49
* 2872     0000.0c9f.fb38   dynamic  0         F      F    Eth1/49
* 2872     0015.5d3e.f328   dynamic  0         F      F    Eth1/49
* 2872     0015.5d3e.f32a   dynamic  0         F      F    Eth1/49
* 2872     0015.5d3e.f61a   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.85c3   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.85c4   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.9fe8   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.9fe9   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a81e   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a81f   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a820   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a821   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a822   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a823   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a825   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a826   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a828   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a82b   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a82c   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a832   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a834   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a835   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a837   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a838   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a839   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a83a   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a83b   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a83c   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a83d   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a83e   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a83f   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a840   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a841   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a842   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a843   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a844   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a845   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a847   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a848   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a849   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a84a   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a84b   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a850   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a853   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a856   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a859   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a85a   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a85b   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a85d   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a861   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a862   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a863   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a864   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a865   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a866   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a867   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a86a   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a86b   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a86c   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a86d   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a86e   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a86f   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a870   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a871   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a872   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a874   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a875   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a877   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a879   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a87a   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a87e   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a883   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a884   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a885   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a886   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a889   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a88a   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a88b   dynamic  0         F      F    Eth1/49
* 2872     0015.5d49.a88c   dynamic  0         F      F    Eth1/49
* 2872     0015.5da1.0000   dynamic  0         F      F    Eth1/49
* 2872     0015.5da1.0001   dynamic  0         F      F    Eth1/49
* 2872     0015.5da1.0002   dynamic  0         F      F    Eth1/49
* 2872     0015.5da1.0003   dynamic  0         F      F    Eth1/49
* 2872     0015.5da1.0004   dynamic  0         F      F    Eth1/49
* 2872     0015.5da1.0005   dynamic  0         F      F    Eth1/49
* 2872     0015.5da1.0006   dynamic  0         F      F    Eth1/49
* 2872     0015.5da1.0007   dynamic  0         F      F    Eth1/49
* 2872     0015.5da1.0008   dynamic  0         F      F    Eth1/49
* 2872     0015.5da1.0009   dynamic  0         F      F    Eth1/49
* 2872     0015.5da1.000a   dynamic  0         F      F    Eth1/49
* 2872     0015.5da1.000b   dynamic  0         F      F    Eth1/49
* 2872     0015.5da1.000c   dynamic  0         F      F    Eth1/49
* 2872     0015.5da1.000d   dynamic  0         F      F    Eth1/49
* 2872     0015.5da1.000e   dynamic  0         F      F    Eth1/49
* 2872     0015.5da1.000f   dynamic  0         F      F    Eth1/49
* 2872     0015.5da1.0010   dynamic  0         F      F    Eth1/49
* 2872     0015.5da1.0011   dynamic  0         F      F    Eth1/49
* 2872     0015.5da1.0012   dynamic  0         F      F    Eth1/49
* 2872     0015.5da1.0013   dynamic  0         F      F    Eth1/49
* 2872     0015.5da1.0014   dynamic  0         F      F    Eth1/49
* 2872     0015.5da1.0015   dynamic  0         F      F    Eth1/49
* 2872     0015.5da1.0016   dynamic  0         F      F    Eth1/49
* 2872     0015.5da1.0017   dynamic  0         F      F    Eth1/49
* 2872     0015.5da1.0018   dynamic  0         F      F    Eth1/49
* 2872     0015.5da1.0019   dynamic  0         F      F    Eth1/49
* 2872     0015.5da1.001a   dynamic  0         F      F    Eth1/49
* 2872     0015.5da1.001b   dynamic  0         F      F    Eth1/49
* 2872     0015.5da1.001c   dynamic  0         F      F    Eth1/49
* 2872     0015.5da1.001d   dynamic  0         F      F    Eth1/49
* 2872     0015.5da1.001e   dynamic  0         F      F    Eth1/49
* 2872     0015.5da1.001f   dynamic  0         F      F    Eth1/49
* 2872     0015.5da1.0020   dynamic  0         F      F    Eth1/49
* 2872     0015.5da1.0021   dynamic  0         F      F    Eth1/49
* 2872     0015.5da1.0022   dynamic  0         F      F    Eth1/49
* 2872     0015.5da1.0023   dynamic  0         F      F    Eth1/49
* 2872     0015.5da1.0024   dynamic  0         F      F    Eth1/49
* 2872     0015.5da1.0025   dynamic  0         F      F    Eth1/49
* 2872     0015.5da1.0026   dynamic  0         F      F    Eth1/49
* 2872     0015.5da1.0027   dynamic  0         F      F    Eth1/49
* 2872     0015.5da1.0028   dynamic  0         F      F    Eth1/49
* 2872     0015.5da1.0029   dynamic  0         F      F    Eth1/49
* 2872     0015.5da1.002a   dynamic  0         F      F    Eth1/49
* 2872     0015.5da1.002b   dynamic  0         F      F    Eth1/49
* 2872     0015.5da1.002c   dynamic  0         F      F    Eth1/49
* 2872     0015.5da1.002d   dynamic  0         F      F    Eth1/49
* 2872     0015.5da1.002e   dynamic  0         F      F    Eth1/49
* 2872     0015.5da1.002f   dynamic  0         F      F    Eth1/49
* 2872     0015.5da1.0030   dynamic  0         F      F    Eth1/49
* 2872     0015.5da1.0031   dynamic  0         F      F    Eth1/49
* 2872     0015.5da2.0000   dynamic  0         F      F    Eth1/49
* 2872     0015.5da2.0001   dynamic  0         F      F    Eth1/49
* 2872     0015.5da2.0002   dynamic  0         F      F    Eth1/49
* 2872     0015.5da2.0003   dynamic  0         F      F    Eth1/49
* 2872     0015.5da2.0004   dynamic  0         F      F    Eth1/49
* 2872     0015.5da2.0005   dynamic  0         F      F    Eth1/49
* 2872     0015.5da2.0006   dynamic  0         F      F    Eth1/49
* 2872     0015.5da2.0007   dynamic  0         F      F    Eth1/49
* 2872     0015.5da2.0008   dynamic  0         F      F    Eth1/49
* 2872     0015.5da2.0009   dynamic  0         F      F    Eth1/49
* 2872     0015.5da2.000a   dynamic  0         F      F    Eth1/49
* 2872     0015.5da2.000b   dynamic  0         F      F    Eth1/49
* 2872     0015.5da2.000c   dynamic  0         F      F    Eth1/49
* 2872     0015.5da2.000d   dynamic  0         F      F    Eth1/49
* 2872     0015.5da2.000e   dynamic  0         F      F    Eth1/49
* 2872     0015.5da2.000f   dynamic  0         F      F    Eth1/49
* 2872     0015.5da2.0010   dynamic  0         F      F    Eth1/49
* 2872     0015.5da2.0011   dynamic  0         F      F    Eth1/49
* 2872     0015.5da2.0012   dynamic  0         F      F    Eth1/49
* 2872     0015.5da2.0013   dynamic  0         F      F    Eth1/49
* 2872     0015.5da2.0014   dynamic  0         F      F    Eth1/49
* 2872     0015.5da2.0015   dynamic  0         F      F    Eth1/49
* 2872     0015.5da2.0016   dynamic  0         F      F    Eth1/49
* 2872     0015.5da2.0017   dynamic  0         F      F    Eth1/49
* 2872     0015.5da2.0018   dynamic  0         F      F    Eth1/49
* 2872     0015.5da2.0019   dynamic  0         F      F    Eth1/49
* 2872     0015.5da2.001a   dynamic  0         F      F    Eth1/49
* 2872     0015.5da2.001b   dynamic  0         F      F    Eth1/49
* 2872     0015.5da2.001c   dynamic  0         F      F    Eth1/49
* 2872     0015.5da2.001d   dynamic  0         F      F    Eth1/49
* 2872     0015.5da2.001e   dynamic  0         F      F    Eth1/49
* 2872     0015.5da2.001f   dynamic  0         F      F    Eth1/49
* 2872     0015.5da2.0020   dynamic  0         F      F    Eth1/49
* 2872     0015.5da2.0021   dynamic  0         F      F    Eth1/49
* 2872     0015.5da2.0022   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.0000   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.0001   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.0002   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.0003   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.0004   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.0005   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.0006   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.0007   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.0008   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.0009   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.000a   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.000b   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.000c   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.000d   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.000e   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.000f   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.0010   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.0011   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.0012   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.0013   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.0014   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.0015   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.0016   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.0017   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.0018   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.0019   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.001a   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.001b   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.001c   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.001d   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.001e   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.001f   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.0020   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.0021   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.0022   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.0023   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.0024   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.0025   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.0026   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.0027   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.0028   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.0029   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.002a   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.002b   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.002c   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.002d   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.002e   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.002f   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.0030   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.0031   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.0032   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.0033   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.0034   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.0035   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.0036   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.0037   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.0038   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.0039   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.003a   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.003b   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.003c   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.003d   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.003e   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.003f   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.0040   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.0041   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.0042   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.0043   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.0044   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.0045   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.0046   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.0047   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.0048   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.0049   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.004a   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.004b   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.004c   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.004d   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.004e   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.004f   dynamic  0         F      F    Eth1/49
* 2872     0015.5da3.0050   dynamic  0         F      F    Eth1/49
* 2872     0015.5da4.0000   dynamic  0         F      F    Eth1/49
* 2872     0015.5da4.0001   dynamic  0         F      F    Eth1/49
* 2872     0015.5da4.0002   dynamic  0         F      F    Eth1/49
* 2872     0015.5da4.0003   dynamic  0         F      F    Eth1/49
* 2872     0015.5da4.0004   dynamic  0         F      F    Eth1/49
* 2872     0015.5da4.0005   dynamic  0         F      F    Eth1/49
* 2872     0015.5da4.0006   dynamic  0         F      F    Eth1/49
* 2872     0015.5da4.0007   dynamic  0         F      F    Eth1/49
* 2872     0015.5da4.0008   dynamic  0         F      F    Eth1/49
* 2872     0015.5da4.0009   dynamic  0         F      F    Eth1/49
* 2872     0015.5da4.000a   dynamic  0         F      F    Eth1/49
* 2872     0015.5da4.000b   dynamic  0         F      F    Eth1/49
* 2872     0015.5da4.000c   dynamic  0         F      F    Eth1/49
* 2872     0015.5da4.000d   dynamic  0         F      F    Eth1/49
* 2872     0015.5da4.000e   dynamic  0         F      F    Eth1/49
* 2872     0015.5da4.000f   dynamic  0         F      F    Eth1/49
* 2872     0015.5da4.0010   dynamic  0         F      F    Eth1/49
* 2872     0015.5da4.0011   dynamic  0         F      F    Eth1/49
* 2872     0015.5da4.0012   dynamic  0         F      F    Eth1/49
* 2872     0015.5da4.0013   dynamic  0         F      F    Eth1/49
* 2872     0015.5da4.0014   dynamic  0         F      F    Eth1/49
* 2872     0015.5da4.0015   dynamic  0         F      F    Eth1/49
* 2872     0015.5da4.0016   dynamic  0         F      F    Eth1/49
* 2872     0015.5da4.0017   dynamic  0         F      F    Eth1/49
* 2872     0015.5da4.0018   dynamic  0         F      F    Eth1/49
* 2872     0015.5da4.0019   dynamic  0         F      F    Eth1/49
* 2872     0015.5da4.001a   dynamic  0         F      F    Eth1/49
* 2872     008c.fad1.052c   dynamic  0         F      F    Eth1/49
* 2872     008c.fad1.0559   dynamic  0         F      F    Eth1/49
* 2872     008c.fad1.05dc   dynamic  0         F      F    Eth1/49
* 2872     008c.fad1.1563   dynamic  0         F      F    Eth1/49
* 2872     008c.fad1.15a3   dynamic  0         F      F    Eth1/49
* 2872     008c.fad1.3504   dynamic  0         F      F    Eth1/49
* 2872     008c.fad1.35ae   dynamic  0         F      F    Eth1/49
* 2872     008c.fad1.4547   dynamic  0         F      F    Eth1/49
* 2872     008c.fad1.75ee   dynamic  0         F      F    Eth1/49
* 2872     008c.fad1.a477   dynamic  0         F      F    Eth1/49
* 2872     008c.fad1.a495   dynamic  0         F      F    Eth1/49
* 2872     008c.fad1.a4d1   dynamic  0         F      F    Eth1/49
* 2872     008c.fad1.b207   dynamic  0         F      F    Eth1/49
* 2872     008c.fad1.b427   dynamic  0         F      F    Eth1/49
* 2872     008c.fad1.f4a1   dynamic  0         F      F    Eth1/49
* 2872     008c.fad1.f4ec   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a12.2e23   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a13.203c   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a15.0c6e   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a16.5559   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a16.558c   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a16.55b2   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a16.6513   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a16.65ba   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a16.7570   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a16.75a6   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a16.75c1   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a16.75c4   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a16.75e7   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a16.75f3   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a16.8516   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a16.8527   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a16.852b   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a16.852d   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a16.8549   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a16.8553   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a16.8569   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a16.857c   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a16.85bb   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a16.951f   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a16.954c   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a16.957f   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a16.9581   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a16.9582   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a16.9591   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a16.959d   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a16.95b3   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a16.a502   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a16.a504   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a16.a51b   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a16.b5ff   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a16.c539   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a16.c5a9   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a16.c5bf   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.02f9   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.2938   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.2ca4   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.2e0b   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.2e47   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.2e4b   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.2e52   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.2e5c   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.2e61   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.32cd   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.32ec   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.3913   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.3964   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.3e00   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.3e04   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.3e08   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.3e22   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.3e29   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.3e2b   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.3e32   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.3e3b   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.3e43   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.4208   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.4222   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.42e3   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.5258   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.5286   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.58c2   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.6213   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.62b1   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.6820   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.684e   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.68b0   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.68cb   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.6e6f   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.6eaf   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.7208   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.7233   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.7271   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.7275   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.7813   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.7898   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.78b7   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.8e0c   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.8e8e   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.8eb2   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.8edb   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.8ee0   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.8ef3   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.9e18   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.9e1a   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.9e53   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.9e64   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.9e67   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.9ee0   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.a756   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.be1a   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.be2e   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.bedd   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.bedf   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.ce00   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.ce61   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.ce63   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.cec8   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.cee4   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.d996   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.d9c8   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.d9cd   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.d9d7   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.d9e0   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.d9f5   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.e953   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.e967   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.e96e   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.e975   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.e994   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.e9c8   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.e9f2   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.e9f4   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.f893   dynamic  0         F      F    Eth1/49
* 2872     7cd3.0a1c.f96f   dynamic  0         F      F    Eth1/49
* 2872     8c94.1f18.e335   dynamic  0         F      F    Eth1/49
* 2872     8cec.4b5b.c73b   dynamic  0         F      F    Eth1/49
* 2872     ecce.1389.7802   dynamic  0         F      F    Eth1/49
* 2872     ecce.1389.8582   dynamic  0         F      F    Eth1/49
* 2873     0000.0c9f.fb39   dynamic  0         F      F    Eth1/49
* 2873     8c94.1f18.e335   dynamic  0         F      F    Eth1/49
* 2873     ecce.1389.7802   dynamic  0         F      F    Eth1/49
* 2873     ecce.1389.8582   dynamic  0         F      F    Eth1/49
* 2876     0000.0c9f.fb3c   dynamic  0         F      F    Eth1/49
* 2876     8c94.1f18.e335   dynamic  0         F      F    Eth1/49
* 2876     accc.8e98.4e56   dynamic  0         F      F    Eth1/49
* 2876     ecce.1389.8582   dynamic  0         F      F    Eth1/49
* 2877     0000.0c9f.fb3d   dynamic  0         F      F    Eth1/49
* 2877     8c94.1f18.e335   dynamic  0         F      F    Eth1/49
* 2877     ecce.1389.8582   dynamic  0         F      F    Eth1/49
* 2878     0000.0c9f.fb3e   dynamic  0         F      F    Eth1/49
* 2878     0050.5689.c0d1   dynamic  0         F      F    Eth1/49
* 2878     3814.2830.8902   dynamic  0         F      F    Eth1/49
* 2878     6400.6a96.3339   dynamic  0         F      F    Eth1/49
* 2878     8c94.1f18.e335   dynamic  0         F      F    Eth1/49
* 2878     8cec.4b5a.89b0   dynamic  0         F      F    Eth1/49
* 2878     8cec.4bc3.d425   dynamic  0         F      F    Eth1/49
* 2878     c8cb.b82c.4c6a   dynamic  0         F      F    Eth1/49
* 2878     cc48.3a5b.9a15   dynamic  0         F      F    Eth1/49
* 2878     ecce.1389.7802   dynamic  0         F      F    Eth1/49
* 2878     ecce.1389.8582   dynamic  0         F      F    Eth1/49
* 2879     0000.0c9f.fb3f   dynamic  0         F      F    Eth1/49
* 2879     8c94.1f18.e335   dynamic  0         F      F    Eth1/49
* 2879     8cec.4b5b.820e   dynamic  0         F      F    Eth1/49
* 2879     8cec.4b5b.82d9   dynamic  0         F      F    Eth1/49
* 2879     8cec.4b5b.c6a8   dynamic  0         F      F    Eth1/49
* 2879     8cec.4b5b.c6c6   dynamic  0         F      F    Eth1/49
* 2879     8cec.4b5b.c6ed   dynamic  0         F      F    Eth1/49
* 2879     8cec.4b5b.c717   dynamic  0         F      F    Eth1/49
* 2879     ecce.1389.7802   dynamic  0         F      F    Eth1/49
* 2879     ecce.1389.8582   dynamic  0         F      F    Eth1/49
* 2882     0000.0c9f.fb42   dynamic  0         F      F    Eth1/49
* 2882     8c94.1f18.e335   dynamic  0         F      F    Eth1/49
* 2882     ecce.1389.8582   dynamic  0         F      F    Eth1/49
* 2889     0000.0c9f.fb49   dynamic  0         F      F    Eth1/49
* 2889     0001.2e39.94bb   dynamic  0         F      F    Eth1/49
* 2889     000d.ad02.356a   dynamic  0         F      F    Eth1/49
* 2889     5c85.7e48.005a   dynamic  0         F      F    Eth1/49
* 2889     8c94.1f18.e335   dynamic  0         F      F    Eth1/49
* 2889     94c6.911c.7b98   dynamic  0         F      F    Eth1/49
* 2889     94c6.911d.68ac   dynamic  0         F      F    Eth1/49
* 2889     94c6.911d.69d0   dynamic  0         F      F    Eth1/49
* 2889     94c6.911d.6b0a   dynamic  0         F      F    Eth1/49
* 2889     94c6.911d.6e57   dynamic  0         F      F    Eth1/49
* 2889     a01e.0b0d.3936   dynamic  0         F      F    Eth1/49
* 2889     a01e.0b0d.39c6   dynamic  0         F      F    Eth1/49
* 2889     a01e.0b0d.587d   dynamic  0         F      F    Eth1/49
* 2889     ecce.1389.7802   dynamic  0         F      F    Eth1/49
* 2889     ecce.1389.8582   dynamic  0         F      F    Eth1/49
G    -     9077.ee01.bf07   static   -         F      F    sup-eth1(R)""",
 'show run | section tacacs':"""feature tacacs+
tacacs-server key 7 "L$iN$eW@tb!"
tacacs-server host 172.31.17.180 
tacacs-server host 10.64.32.5 
aaa group server tacacs+ TacServer 
    server 172.31.17.180 
    server 10.64.32.5 
    use-vrf management
aaa group server tacacs+ tacacs """,
 'show run | in tacacs':"""feature tacacs+
tacacs-server key 7 "L$iN$eW@tb!"
tacacs-server host 172.31.17.180 
tacacs-server host 10.64.32.5 
aaa group server tacacs+ TacServer 
aaa group server tacacs+ tacacs """,
