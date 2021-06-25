ip_address = '172.28.65.102'
software = 'software'
hardware = 'hardware'
read_results = {
 'show version':"""Cisco Nexus Operating System (NX-OS) Software
TAC support: http://www.cisco.com/tac
Copyright (C) 2002-2015, Cisco and/or its affiliates.
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
  BIOS: version 07.17
  NXOS: version 7.0(3)I1(2)
  BIOS compile time:  09/10/2014
  NXOS image file is: bootflash:///n9000-dk9.7.0.3.I1.2.bin
  NXOS compile time:  5/16/2015 12:00:00 [05/16/2015 13:07:58]


Hardware
  cisco Nexus9000 C9332PQ chassis 
  Intel(R) Core(TM) i3-3227U C with 16402540 kB of memory.
  Processor Board ID SAL1934MZPC

  Device name: dcx2-ddc-m3
  bootflash:   51496280 kB
Kernel uptime is 2095 day(s), 2 hour(s), 15 minute(s), 57 second(s)

Last reset 
  Reason: Unknown
  System version: 7.0(3)I1(2)
  Service: 

plugin
  Core Plugin, Ethernet Plugin

Active Packages:""",
 'show run':"""!Command: ning-config
!Time: Fri Jun 25 16:24:30 2021

version 7.0(3)I1(2)
hostname dcx2-ddc-m3
class-map type network-qos class-fcoe
policy-map type network-qos jumbo
  class type network-qos class-fcoe
    mtu 2158
  class type network-qos class-default
    mtu 9216
vdc dcx2-ddc-m3 id 1
  limit-resource vlan minimum 16 maximum 4094
  limit-resource vrf minimum 2 maximum 4096
  limit-resource port-channel minimum 0 maximum 511
  limit-resource u4route-mem minimum 248 maximum 248
  limit-resource u6route-mem minimum 96 maximum 96
  limit-resource m4route-mem minimum 58 maximum 58
  limit-resource m6route-mem minimum 8 maximum 8

feature nxapi
feature bash-shell
feature tacacs+
cfs eth distribute
feature udld
feature interface-vlan
feature lacp
feature vpc
feature lldp

username admin password 5 $1$NhJRvJj/$SivMUD1YLO5bgW7sleN1P.  role network-admin

banner motd Z

                   __  __     _____  __
                  / / / /__  / _/ / / /
                 / /_/ / _ / _/ /_/ /
                 ____/___/_/ ____/

 dcx2-ddc-m3


 This device is part of the University of Utah Campus network.
 Unauthorized or improper use of this device may result in
 administrative disciplinary action and civil and criminal
 penalties. All commands issued on this device are monitored
 and recorded. By continuing to use this system you indicate
 your awareness of and consent to these terms and conditions
 of use. See the University of Utah Information Resource Policy
 for more information at http://www.admin.utah.edu/ppmanual/1/1-15.html



 Problems with the University of Utah network should be reported
 to the Campus Help Desk at 581-4000 or via email at helpdesk@Tah.edu.



               !!!!! DO NOT LOGIN !!!!!

 if you are not authorized by the Office of Information Technology at
 the University of Utah (http://www.it.utah.edu/index_fl.html).

Z

ip domain-lookup
ip domain-name net.utah.edu
ip name-server 172.20.120.20
tacacs-server key 7 "L$iN$eW@tb!"
tacacs-server host 172.31.17.180 
tacacs-server host 10.64.32.5 
aaa group server tacacs+ TacServer 
    server 172.31.17.180 
    server 10.64.32.5 
    use-vrf management
interface breakout module 1 port 10,18,20,25-26 map 10g-4x
ip access-list 199
ip access-list MonitorTeam_SNMP_RO_POLICY
  10 remark Monitor Team SNMP Read Only ACL
  20 permit udp 155.100.122.25/32 any eq snmp 
  30 permit udp 155.100.122.28/32 any eq snmp 
  40 permit udp 155.100.122.50/32 any eq snmp 
  50 permit udp 155.100.122.200/32 any eq snmp 
ip access-list NOC_MGMT_OUT
ip access-list NOC_SNMP_RO_POLICY
  10 remark Netops SNMP Read Only ACL
  20 remark NOC MGMT NEt
  30 permit udp 155.98.253.0/24 any eq snmp 
  40 remark INMON Tool
  50 permit udp 155.100.122.113/32 any eq snmp 
  60 remark Neebula Tool Test
  70 permit udp 155.100.240.123/32 any eq snmp 
  100 permit udp 155.101.168.124/32 any eq snmp 
  110 permit udp 10.71.24.10/32 any eq snmp 
  120 permit udp 10.71.24.11/32 any eq snmp 
  130 permit udp 10.71.24.12/32 any eq snmp 
  140 permit udp 10.71.24.13/32 any eq snmp 
  150 permit udp 10.71.24.14/32 any eq snmp 
  160 permit udp 10.71.24.15/32 any eq snmp 
  170 permit udp 10.71.24.16/32 any eq snmp 
  180 permit udp 10.71.24.17/32 any eq snmp 
  190 permit udp 10.71.24.18/32 any eq snmp 
  200 permit udp 10.71.24.19/32 any eq snmp 
  210 permit udp 10.71.24.20/32 any eq snmp 
  220 permit udp 10.71.24.21/32 any eq snmp 
  230 permit udp 10.71.24.22/32 any eq snmp 
  240 permit udp 10.71.24.23/32 any eq snmp 
ip access-list NOC_SNMP_RW_POLICY
  10 remark NOC MGMT NET
  20 permit udp 155.98.253.0/24 any eq snmp 
  30 permit udp 10.71.24.10/32 any eq snmp 
  40 permit udp 10.71.24.11/32 any eq snmp 
  50 permit udp 10.71.24.12/32 any eq snmp 
  60 permit udp 10.71.24.13/32 any eq snmp 
  70 permit udp 10.71.24.14/32 any eq snmp 
  80 permit udp 10.71.24.15/32 any eq snmp 
  90 permit udp 10.71.24.16/32 any eq snmp 
  100 permit udp 10.71.24.17/32 any eq snmp 
  110 permit udp 10.71.24.18/32 any eq snmp 
  120 permit udp 10.71.24.19/32 any eq snmp 
  130 permit udp 10.71.24.20/32 any eq snmp 
  140 permit udp 10.71.24.21/32 any eq snmp 
  150 permit udp 10.71.24.22/32 any eq snmp 
  160 permit udp 10.71.24.23/32 any eq snmp 
ip access-list SSH_POLICY
  10 permit tcp 155.98.253.0/24 any eq 22 
  15 permit tcp 155.99.254.128/25 any eq 22 
  20 remark VPN Networks
  30 permit tcp 155.101.243.0/27 any eq 22 
  31 permit tcp 155.98.164.192/27 any eq 22 
  40 deny tcp 155.100.37.16/32 any eq 22 
  50 deny tcp 155.100.37.31/32 any eq 22 
  60 permit tcp 155.100.37.16/28 any eq 22 
  70 remark Door1 & Door2
  80 permit tcp 155.99.239.130/32 any eq 22 
  90 permit tcp 155.97.152.244/32 any eq 22 
system qos
  service-policy type network-qos jumbo
copp profile strict
snmp-server contact TAG:305156-BarCode:503203
snmp-server location West Temple DC Row a4
snmp-server globalEnforcePriv
snmp-server user admin network-admin auth md5 0xa42b896412551126921a6581c604347c priv 0xa42b896412551126921a6581c604347c
 localizedkey
rmon event 1 log trap public description FATAL(1) owner PMON@FATAL
rmon event 2 log trap public description CRITICAL(2) owner PMON@CRITICAL
rmon event 3 log trap public description ERROR(3) owner PMON@ERROR
rmon event 4 log trap public description WARNING(4) owner PMON@WARNING
rmon event 5 log trap public description INFORMATION(5) owner PMON@INFO
snmp-server community 99U#u#U!x group network-operator
snmp-server community 1xR$bluE group network-operator
snmp-server community 99U#u#U!x use-acl NOC_SNMP_RO_POLICY
snmp-server community 1xR$bluE use-acl MonitorTeam_SNMP_RO_POLICY
ntp server 155.97.154.154 use-vrf management
ntp server 155.97.159.10 use-vrf management
aaa authentication login default group TacServer 
aaa authentication login console local 

vlan 1,520,3520-3521
vlan 520
  name dc-892-libsstaf-in
vlan 3520
  name sv-storage
vlan 3521
  name sv-fed

vrf context management
  ip domain-name net.utah.edu
  ip name-server 155.101.115.10 155.101.201.10
  ip route 0.0.0.0/0 172.28.65.1

interface Vlan1

interface port-channel31
  description ddr1-ddc-i13 and ddr2-ddc-j13
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 520,3520-3521
  mtu 9216

interface Ethernet1/1
  description mlib-vm2019-Node1-Eth1
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 520,3520-3521
  spanning-tree port type edge
  mtu 9216
  no shutdown

interface Ethernet1/2
  description mlib-vm2019-Node2-Eth1
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 520,3520-3521
  spanning-tree port type edge
  mtu 9216
  no shutdown

interface Ethernet1/3
  description qc1
  switchport
  switchport access vlan 520
  no shutdown

interface Ethernet1/4
  description qc2
  switchport
  switchport access vlan 520
  no shutdown

interface Ethernet1/5
  description qc3
  switchport
  switchport access vlan 520
  no shutdown

interface Ethernet1/6
  description qc4
  switchport
  switchport access vlan 520
  no shutdown

interface Ethernet1/7

interface Ethernet1/8

interface Ethernet1/9

interface Ethernet1/10/1
  description SV-VMKM1
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 520,3520-3521
  spanning-tree port type edge
  mtu 9216
  no shutdown

interface Ethernet1/10/2
  description SV-VMKM2
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 520,3520-3521
  spanning-tree port type edge
  mtu 9216
  no shutdown

interface Ethernet1/10/3
  description bu-commed2
  switchport
  switchport access vlan 520
  spanning-tree port type edge
  no shutdown

interface Ethernet1/10/4
  description appdev-ml_eth0
  switchport
  switchport access vlan 520
  no shutdown

interface Ethernet1/11
  description Qumulo-5-eth1
  switchport
  switchport access vlan 520
  spanning-tree port type edge
  no shutdown

interface Ethernet1/12
  description Qumulo-6-eth1
  switchport
  switchport access vlan 520
  spanning-tree port type edge
  no shutdown

interface Ethernet1/13
  description Qumulo-7-eth1
  switchport
  switchport access vlan 520
  spanning-tree port type edge
  no shutdown

interface Ethernet1/14
  description Qumulo-8-eth1
  switchport
  switchport access vlan 520
  spanning-tree port type edge
  no shutdown

interface Ethernet1/15

interface Ethernet1/16
  description BAD_PORT

interface Ethernet1/17
  description Qumulo-9-eth1
  switchport
  switchport access vlan 520
  spanning-tree port type edge
  no shutdown

interface Ethernet1/18/1

interface Ethernet1/18/2

interface Ethernet1/18/3

interface Ethernet1/18/4

interface Ethernet1/19

interface Ethernet1/20/1
  description mlib-vm2019-2-wan
  switchport
  switchport access vlan 520
  spanning-tree port type edge
  no shutdown

interface Ethernet1/20/2
  description mlib-vm2019-2-stor
  switchport
  switchport access vlan 520
  spanning-tree port type edge
  no shutdown

interface Ethernet1/20/3
  description mlib-ns1-b0
  switchport
  switchport access vlan 520
  spanning-tree port type edge
  mtu 9216
  no shutdown

interface Ethernet1/20/4
  description mlib-ns1-b1
  switchport
  switchport access vlan 520
  spanning-tree port type edge
  mtu 9216
  no shutdown

interface Ethernet1/21

interface Ethernet1/22

interface Ethernet1/23
  description Mlib Test
  switchport
  switchport access vlan 520
  spanning-tree port type edge
  no shutdown

interface Ethernet1/24

interface Ethernet1/25/1
  description #e1/25/1:ddr1-ddc-i13:1/14
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 520,3520-3521
  mtu 9216
  channel-group 31 mode active
  no shutdown

interface Ethernet1/25/2

interface Ethernet1/25/3

interface Ethernet1/25/4

interface Ethernet1/26/1
  description #e1/26/1:ddr2-ddc-j13:1/14
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 520,3520-3521
  mtu 9216
  channel-group 31 mode active
  no shutdown

interface Ethernet1/26/2

interface Ethernet1/26/3

interface Ethernet1/26/4

interface Ethernet1/27

interface Ethernet1/28

interface Ethernet1/29

interface Ethernet1/30

interface Ethernet1/31
  no shutdown

interface Ethernet1/32
  no shutdown

interface mgmt0
  description key:dx2-3574ddc-i11-mgmt:Gig1/0/30
  vrf member management
  ip address 172.28.65.102/24
clock timezone MST -7 0
clock summer-time MDT 1 Sunday March 02:00 5 Sunday November 02:00 60
cli alias name wri copy running-config startup-config
line console
line vty
  exec-timeout 15
  access-class SSH_POLICY in
boot nxos bootflash:/n9000-dk9.7.0.3.I1.2.bin 
monitor session 1 
monitor session 2 type erspan-source
  source interface Ethernet1/3 both
logging server 155.98.204.52 6 use-vrf management facility local6
logging server 155.98.253.244 6 use-vrf management facility local6
logging console 0

""",
 'show int status':"""--------------------------------------------------------------------------------
Port          Name               Status    Vlan      Duplex  Speed   Type
--------------------------------------------------------------------------------
mgmt0         key:dx2-3574ddc-i1 connected routed    full    1000    --         
Eth1/1        mlib-vm2019-Node1- connected trunk     full    40G     QSFP-40G-SR-BD
Eth1/2        mlib-vm2019-Node2- connected trunk     full    40G     QSFP-40G-SR-BD
Eth1/3        qc1                xcvrAbsen 520       auto    auto    --         
Eth1/4        qc2                xcvrAbsen 520       auto    auto    --         
Eth1/5        qc3                xcvrAbsen 520       auto    auto    --         
Eth1/6        qc4                xcvrAbsen 520       auto    auto    --         
Eth1/7        --                 xcvrAbsen routed    auto    auto    --         
Eth1/8        --                 xcvrAbsen routed    auto    auto    --         
Eth1/9        --                 xcvrAbsen routed    auto    auto    --         
Eth1/10/1     SV-VMKM1           connected trunk     full    10G     QSFP-40G-CR4
Eth1/10/2     SV-VMKM2           connected trunk     full    10G     QSFP-40G-CR4
Eth1/10/3     bu-commed2         connected 520       full    10G     QSFP-40G-CR4
Eth1/10/4     appdev-ml_eth0     connected 520       full    10G     QSFP-40G-CR4
Eth1/11       Qumulo-5-eth1      connected 520       full    40G     QSFP-40G-CR4
Eth1/12       Qumulo-6-eth1      connected 520       full    40G     QSFP-40G-CR4
Eth1/13       Qumulo-7-eth1      connected 520       full    40G     QSFP-40G-CR4
Eth1/14       Qumulo-8-eth1      connected 520       full    40G     QSFP-40G-CR4
Eth1/15       --                 xcvrAbsen routed    auto    auto    --         
Eth1/16       BAD_PORT           xcvrAbsen routed    auto    auto    --         
Eth1/17       Qumulo-9-eth1      connected 520       full    40G     QSFP-40G-CR4
Eth1/18/1     --                 xcvrAbsen routed    auto    auto    --         
Eth1/18/2     --                 xcvrAbsen routed    auto    auto    --         
Eth1/18/3     --                 xcvrAbsen routed    auto    auto    --         
Eth1/18/4     --                 xcvrAbsen routed    auto    auto    --         
Eth1/19       --                 xcvrAbsen routed    auto    auto    --         
Eth1/20/1     mlib-vm2019-2-wan  notconnec 520       auto    auto    QSFP-H40G-AOC15M
Eth1/20/2     mlib-vm2019-2-stor notconnec 520       auto    auto    QSFP-H40G-AOC15M
Eth1/20/3     mlib-ns1-b0        connected 520       full    10G     QSFP-H40G-AOC15M
Eth1/20/4     mlib-ns1-b1        connected 520       full    10G     QSFP-H40G-AOC15M
Eth1/21       --                 xcvrAbsen routed    auto    auto    --         
Eth1/22       --                 xcvrAbsen routed    auto    auto    --         
Eth1/23       Mlib Test          xcvrAbsen 520       auto    auto    --         
Eth1/24       --                 xcvrAbsen routed    auto    auto    --         
Eth1/25/1     #e1/25/1:ddr1-ddc- connected trunk     full    10G     QSFP-40G-SR4
Eth1/25/2     --                 disabled  routed    auto    auto    QSFP-40G-SR4
Eth1/25/3     --                 disabled  routed    auto    auto    QSFP-40G-SR4
Eth1/25/4     --                 disabled  routed    auto    auto    QSFP-40G-SR4
Eth1/26/1     #e1/26/1:ddr2-ddc- connected trunk     full    10G     QSFP-40G-SR4
Eth1/26/2     --                 disabled  routed    auto    auto    QSFP-40G-SR4
Eth1/26/3     --                 disabled  routed    auto    auto    QSFP-40G-SR4
Eth1/26/4     --                 disabled  routed    auto    auto    QSFP-40G-SR4
Eth1/27       --                 xcvrAbsen routed    auto    auto    --         
Eth1/28       --                 xcvrAbsen routed    auto    auto    --         
Eth1/29       --                 xcvrAbsen routed    auto    auto    --         
Eth1/30       --                 xcvrAbsen routed    auto    auto    --         
Eth1/31       --                 connected routed    full    40G     QSFP-40G-SR-BD
Eth1/32       --                 connected routed    full    40G     QSFP-40G-SR-BD
Po31          ddr1-ddc-i13 and d connected trunk     full    10G     --         
Vlan1         --                 down      routed    auto    auto    --""",
 'show run | section interface':"""feature interface-vlan
interface breakout module 1 port 10,18,20,25-26 map 10g-4x
interface Vlan1
interface port-channel31
  description ddr1-ddc-i13 and ddr2-ddc-j13
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 520,3520-3521
  mtu 9216
interface Ethernet1/1
  description mlib-vm2019-Node1-Eth1
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 520,3520-3521
  spanning-tree port type edge
  mtu 9216
  no shutdown
interface Ethernet1/2
  description mlib-vm2019-Node2-Eth1
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 520,3520-3521
  spanning-tree port type edge
  mtu 9216
  no shutdown
interface Ethernet1/3
  description qc1
  switchport
  switchport access vlan 520
  no shutdown
interface Ethernet1/4
  description qc2
  switchport
  switchport access vlan 520
  no shutdown
interface Ethernet1/5
  description qc3
  switchport
  switchport access vlan 520
  no shutdown
interface Ethernet1/6
  description qc4
  switchport
  switchport access vlan 520
  no shutdown
interface Ethernet1/7
interface Ethernet1/8
interface Ethernet1/9
interface Ethernet1/10/1
  description SV-VMKM1
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 520,3520-3521
  spanning-tree port type edge
  mtu 9216
  no shutdown
interface Ethernet1/10/2
  description SV-VMKM2
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 520,3520-3521
  spanning-tree port type edge
  mtu 9216
  no shutdown
interface Ethernet1/10/3
  description bu-commed2
  switchport
  switchport access vlan 520
  spanning-tree port type edge
  no shutdown
interface Ethernet1/10/4
  description appdev-ml_eth0
  switchport
  switchport access vlan 520
  no shutdown
interface Ethernet1/11
  description Qumulo-5-eth1
  switchport
  switchport access vlan 520
  spanning-tree port type edge
  no shutdown
interface Ethernet1/12
  description Qumulo-6-eth1
  switchport
  switchport access vlan 520
  spanning-tree port type edge
  no shutdown
interface Ethernet1/13
  description Qumulo-7-eth1
  switchport
  switchport access vlan 520
  spanning-tree port type edge
  no shutdown
interface Ethernet1/14
  description Qumulo-8-eth1
  switchport
  switchport access vlan 520
  spanning-tree port type edge
  no shutdown
interface Ethernet1/15
interface Ethernet1/16
  description BAD_PORT
interface Ethernet1/17
  description Qumulo-9-eth1
  switchport
  switchport access vlan 520
  spanning-tree port type edge
  no shutdown
interface Ethernet1/18/1
interface Ethernet1/18/2
interface Ethernet1/18/3
interface Ethernet1/18/4
interface Ethernet1/19
interface Ethernet1/20/1
  description mlib-vm2019-2-wan
  switchport
  switchport access vlan 520
  spanning-tree port type edge
  no shutdown
interface Ethernet1/20/2
  description mlib-vm2019-2-stor
  switchport
  switchport access vlan 520
  spanning-tree port type edge
  no shutdown
interface Ethernet1/20/3
  description mlib-ns1-b0
  switchport
  switchport access vlan 520
  spanning-tree port type edge
  mtu 9216
  no shutdown
interface Ethernet1/20/4
  description mlib-ns1-b1
  switchport
  switchport access vlan 520
  spanning-tree port type edge
  mtu 9216
  no shutdown
interface Ethernet1/21
interface Ethernet1/22
interface Ethernet1/23
  description Mlib Test
  switchport
  switchport access vlan 520
  spanning-tree port type edge
  no shutdown
interface Ethernet1/24
interface Ethernet1/25/1
  description #e1/25/1:ddr1-ddc-i13:1/14
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 520,3520-3521
  mtu 9216
  channel-group 31 mode active
  no shutdown
interface Ethernet1/25/2
interface Ethernet1/25/3
interface Ethernet1/25/4
interface Ethernet1/26/1
  description #e1/26/1:ddr2-ddc-j13:1/14
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 520,3520-3521
  mtu 9216
  channel-group 31 mode active
  no shutdown
interface Ethernet1/26/2
interface Ethernet1/26/3
interface Ethernet1/26/4
interface Ethernet1/27
interface Ethernet1/28
interface Ethernet1/29
interface Ethernet1/30
interface Ethernet1/31
  no shutdown
interface Ethernet1/32
  no shutdown
interface mgmt0
  description key:dx2-3574ddc-i11-mgmt:Gig1/0/30
  vrf member management
  ip address 172.28.65.102/24
  source interface Ethernet1/3 both""",
 'show run | in interface':"""feature interface-vlan
interface breakout module 1 port 10,18,20,25-26 map 10g-4x
interface Vlan1
interface port-channel31
interface Ethernet1/1
interface Ethernet1/2
interface Ethernet1/3
interface Ethernet1/4
interface Ethernet1/5
interface Ethernet1/6
interface Ethernet1/7
interface Ethernet1/8
interface Ethernet1/9
interface Ethernet1/10/1
interface Ethernet1/10/2
interface Ethernet1/10/3
interface Ethernet1/10/4
interface Ethernet1/11
interface Ethernet1/12
interface Ethernet1/13
interface Ethernet1/14
interface Ethernet1/15
interface Ethernet1/16
interface Ethernet1/17
interface Ethernet1/18/1
interface Ethernet1/18/2
interface Ethernet1/18/3
interface Ethernet1/18/4
interface Ethernet1/19
interface Ethernet1/20/1
interface Ethernet1/20/2
interface Ethernet1/20/3
interface Ethernet1/20/4
interface Ethernet1/21
interface Ethernet1/22
interface Ethernet1/23
interface Ethernet1/24
interface Ethernet1/25/1
interface Ethernet1/25/2
interface Ethernet1/25/3
interface Ethernet1/25/4
interface Ethernet1/26/1
interface Ethernet1/26/2
interface Ethernet1/26/3
interface Ethernet1/26/4
interface Ethernet1/27
interface Ethernet1/28
interface Ethernet1/29
interface Ethernet1/30
interface Ethernet1/31
interface Ethernet1/32
interface mgmt0
  source interface Ethernet1/3 both""",
 'show interface link':"""^
Invalid interface format at '^' marker.""",
 'show interface':"""mgmt0 is up
admin state is up,
  Hardware: GigabitEthernet, address: ecbd.1dea.5bd8 (bia ecbd.1dea.5bd8)
  Description: key:dx2-3574ddc-i11-mgmt:Gig1/0/30
  Internet Address is 172.28.65.102/24
  MTU 1500 bytes, BW 1000000 Kbit, DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  full-duplex, 1000 Mb/s
  Auto-Negotiation is turned on
  Auto-mdix is turned off
  EtherType is 0x0000 
  1 minute input rate 2168 bits/sec, 2 packets/sec
  1 minute output rate 2224 bits/sec, 1 packets/sec
  Rx
    2073578616 input packets 115902643 unicast packets 1930360300 multicast packets
    27315673 broadcast packets 184079741303 bytes
  Tx
    125361401 output packets 116314488 unicast packets 9041968 multicast packets
    4945 broadcast packets 26085809107 bytes

Ethernet1/1 is up
admin state is up, Dedicated Interface
  Hardware: 10000/40000 Ethernet, address: ecbd.1dea.5be0 (bia ecbd.1dea.5be0)
  Description: mlib-vm2019-Node1-Eth1
  MTU 9216 bytes, BW 40000000 Kbit, DLY 10 usec
  reliability 255/255, txload 7/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is trunk
  full-duplex, 40 Gb/s, media type is 40G
  Beacon is turned off
  Auto-Negotiation is turned on
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Rate mode is dedicated
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
  Last link flapped 39week(s) 0day(s)
  Last clearing of "" counters never
  49 interface resets
  30 seconds input rate 37518400 bits/sec, 8008 packets/sec
  30 seconds output rate 1223631024 bits/sec, 18395 packets/sec
  Load-Interval #2: 5 minute (300 seconds)
    input rate 33.69 Mbps, 6.42 Kpps; output rate 970.66 Mbps, 14.60 Kpps
  RX
    65719371430 unicast packets  1427959 multicast packets  48469 broadcast packets
    65720847858 input packets  154390998109614 bytes
    27236450508 jumbo packets  0 storm suppression packets
    0 runts  0 giants  2 CRC  0 no buffer
    2 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    3786 Rx pause
  TX
    214265558646 unicast packets  147103721 multicast packets  247161036 broadcast packets
    214659823403 output packets  817341559722988 bytes
    198260776269 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  51855 output discard
    0 Tx pause

Ethernet1/2 is up
admin state is up, Dedicated Interface
  Hardware: 10000/40000 Ethernet, address: ecbd.1dea.5be4 (bia ecbd.1dea.5be4)
  Description: mlib-vm2019-Node2-Eth1
  MTU 9216 bytes, BW 40000000 Kbit, DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is trunk
  full-duplex, 40 Gb/s, media type is 40G
  Beacon is turned off
  Auto-Negotiation is turned on
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Rate mode is dedicated
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
  Last link flapped 39week(s) 0day(s)
  Last clearing of "" counters never
  69 interface resets
  30 seconds input rate 55574312 bits/sec, 964 packets/sec
  30 seconds output rate 5914960 bits/sec, 502 packets/sec
  Load-Interval #2: 5 minute (300 seconds)
    input rate 23.31 Mbps, 433 pps; output rate 4.23 Mbps, 322 pps
  RX
    110568701521 unicast packets  1427984 multicast packets  1431019 broadcast packets
    110571560524 input packets  217677677428847 bytes
    69853852666 jumbo packets  0 storm suppression packets
    0 runts  0 giants  1 CRC  0 no buffer
    1 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    9388 Rx pause
  TX
    234894447928 unicast packets  147534739 multicast packets  246678551 broadcast packets
    235288661218 output packets  780058463208636 bytes
    213666796599 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  34743 output discard
    0 Tx pause

Ethernet1/3 is down (XCVR not inserted)
admin state is up, Dedicated Interface
  Hardware: 10000/40000 Ethernet, address: ecbd.1dea.5be8 (bia ecbd.1dea.5be8)
  Description: qc1
  MTU 1500 bytes, BW 40000000 Kbit, DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is access
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
  Last link flapped 202week(s) 0day(s)
  Last clearing of "" counters never
  36 interface resets
  30 seconds input rate 0 bits/sec, 0 packets/sec
  30 seconds output rate 0 bits/sec, 0 packets/sec
  Load-Interval #2: 5 minute (300 seconds)
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    1011902103044 unicast packets  1110889 multicast packets  15544 broadcast packets
    1011903229477 input packets  1417928811034977 bytes
    362 jumbo packets  0 storm suppression packets
    0 runts  362 giants  0 CRC  0 no buffer
    362 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    977556 Rx pause
  TX
    617502588657 unicast packets  88920107 multicast packets  387571423 broadcast packets
    617979080187 output packets  741831163176969 bytes
    1 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  600555 output discard
    0 Tx pause

Ethernet1/4 is down (XCVR not inserted)
admin state is up, Dedicated Interface
  Hardware: 10000/40000 Ethernet, address: ecbd.1dea.5bec (bia ecbd.1dea.5bec)
  Description: qc2
  MTU 1500 bytes, BW 40000000 Kbit, DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is access
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
  Last link flapped 202week(s) 0day(s)
  Last clearing of "" counters never
  41 interface resets
  30 seconds input rate 0 bits/sec, 0 packets/sec
  30 seconds output rate 0 bits/sec, 0 packets/sec
  Load-Interval #2: 5 minute (300 seconds)
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    1362320403863 unicast packets  1139399 multicast packets  15585 broadcast packets
    1362321558847 input packets  1818944967118135 bytes
    0 jumbo packets  0 storm suppression packets
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    668514 Rx pause
  TX
    1072701654391 unicast packets  88881720 multicast packets  387494492 broadcast packets
    1073178030603 output packets  1285196166013035 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  108401 output discard
    0 Tx pause

Ethernet1/5 is down (XCVR not inserted)
admin state is up, Dedicated Interface
  Hardware: 10000/40000 Ethernet, address: ecbd.1dea.5bf0 (bia ecbd.1dea.5bf0)
  Description: qc3
  MTU 1500 bytes, BW 40000000 Kbit, DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is access
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
  Last link flapped 202week(s) 0day(s)
  Last clearing of "" counters never
  37 interface resets
  30 seconds input rate 0 bits/sec, 0 packets/sec
  30 seconds output rate 0 bits/sec, 0 packets/sec
  Load-Interval #2: 5 minute (300 seconds)
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    1625028499960 unicast packets  1111232 multicast packets  15796 broadcast packets
    1625029626988 input packets  2259832433746887 bytes
    131 jumbo packets  0 storm suppression packets
    0 runts  131 giants  0 CRC  0 no buffer
    131 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    604246 Rx pause
  TX
    1032449179892 unicast packets  88919951 multicast packets  387571713 broadcast packets
    1032925671556 output packets  1218771222206653 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  206826 output discard
    0 Tx pause

Ethernet1/6 is down (XCVR not inserted)
admin state is up, Dedicated Interface
  Hardware: 10000/40000 Ethernet, address: ecbd.1dea.5bf4 (bia ecbd.1dea.5bf4)
  Description: qc4
  MTU 1500 bytes, BW 40000000 Kbit, DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is access
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
  Last link flapped 202week(s) 0day(s)
  Last clearing of "" counters never
  38 interface resets
  30 seconds input rate 0 bits/sec, 0 packets/sec
  30 seconds output rate 0 bits/sec, 0 packets/sec
  Load-Interval #2: 5 minute (300 seconds)
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    1942932061727 unicast packets  1110456 multicast packets  15953 broadcast packets
    1942933188136 input packets  2605144547194288 bytes
    95708 jumbo packets  0 storm suppression packets
    0 runts  95707 giants  0 CRC  0 no buffer
    95707 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    917332 Rx pause
  TX
    1486720793773 unicast packets  88911374 multicast packets  387562599 broadcast packets
    1487197267746 output packets  1747947087892581 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  934475 output discard
    0 Tx pause

Ethernet1/7 is down (XCVR not inserted)
admin state is down, Dedicated Interface
  Hardware: 10000/40000 Ethernet, address: ecbd.1dea.5bdf (bia ecbd.1dea.5bf8)
  MTU 1500 bytes, BW 40000000 Kbit, DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  30 seconds input rate 0 bits/sec, 0 packets/sec
  30 seconds output rate 0 bits/sec, 0 packets/sec
  Load-Interval #2: 5 minute (300 seconds)
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    402248 unicast packets  0 multicast packets  0 broadcast packets
    402248 input packets  566365184 bytes
    0 jumbo packets  0 storm suppression packets
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    402248 unicast packets  0 multicast packets  0 broadcast packets
    402248 output packets  566365184 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/8 is down (XCVR not inserted)
admin state is down, Dedicated Interface
  Hardware: 10000/40000 Ethernet, address: ecbd.1dea.5bdf (bia ecbd.1dea.5bfc)
  MTU 1500 bytes, BW 40000000 Kbit, DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  30 seconds input rate 0 bits/sec, 0 packets/sec
  30 seconds output rate 0 bits/sec, 0 packets/sec
  Load-Interval #2: 5 minute (300 seconds)
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    402248 unicast packets  0 multicast packets  0 broadcast packets
    402248 input packets  566365184 bytes
    0 jumbo packets  0 storm suppression packets
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    402248 unicast packets  0 multicast packets  0 broadcast packets
    402248 output packets  566365184 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/9 is down (XCVR not inserted)
admin state is down, Dedicated Interface
  Hardware: 10000/40000 Ethernet, address: ecbd.1dea.5bdf (bia ecbd.1dea.5c00)
  MTU 1500 bytes, BW 40000000 Kbit, DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  30 seconds input rate 0 bits/sec, 0 packets/sec
  30 seconds output rate 0 bits/sec, 0 packets/sec
  Load-Interval #2: 5 minute (300 seconds)
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    402248 unicast packets  0 multicast packets  0 broadcast packets
    402248 input packets  566365184 bytes
    0 jumbo packets  0 storm suppression packets
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    402248 unicast packets  0 multicast packets  0 broadcast packets
    402248 output packets  566365184 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/10/1 is up
admin state is up, Dedicated Interface
  Hardware: 10000/40000 Ethernet, address: ecbd.1dea.5c04 (bia ecbd.1dea.5c04)
  Description: SV-VMKM1
  MTU 9216 bytes, BW 10000000 Kbit, DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is trunk
  full-duplex, 10 Gb/s, media type is 40G
  Beacon is turned off
  Auto-Negotiation is turned on
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Rate mode is dedicated
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
  Last link flapped 82week(s) 2day(s)
  Last clearing of "" counters 253w4d
  13 interface resets
  30 seconds input rate 30816 bits/sec, 9 packets/sec
  30 seconds output rate 51128 bits/sec, 17 packets/sec
  Load-Interval #2: 5 minute (300 seconds)
    input rate 25.45 Kbps, 2 pps; output rate 31.76 Kbps, 15 pps
  RX
    3413242975380 unicast packets  13900354 multicast packets  16326354 broadcast packets
    3413273202088 input packets  4892610328807184 bytes
    2799397488015 jumbo packets  0 storm suppression packets
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    330 Rx pause
  TX
    3583829907982 unicast packets  630319354 multicast packets  1198463733 broadcast packets
    3585658691069 output packets  4657546551918308 bytes
    2645820793615 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  140542308 output discard
    0 Tx pause

Ethernet1/10/2 is up
admin state is up, Dedicated Interface
  Hardware: 10000/40000 Ethernet, address: ecbd.1dea.5c05 (bia ecbd.1dea.5c05)
  Description: SV-VMKM2
  MTU 9216 bytes, BW 10000000 Kbit, DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is trunk
  full-duplex, 10 Gb/s, media type is 40G
  Beacon is turned off
  Auto-Negotiation is turned on
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Rate mode is dedicated
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
  Last link flapped 82week(s) 1day(s)
  Last clearing of "" counters 253w4d
  45 interface resets
  30 seconds input rate 144 bits/sec, 0 packets/sec
  30 seconds output rate 10520 bits/sec, 13 packets/sec
  Load-Interval #2: 5 minute (300 seconds)
    input rate 624 bps, 0 pps; output rate 10.82 Kbps, 9 pps
  RX
    3229086870188 unicast packets  10496906 multicast packets  6020632 broadcast packets
    3229103387726 input packets  4270049599503722 bytes
    2570655734879 jumbo packets  0 storm suppression packets
    1 runts  0 giants  4 CRC  0 no buffer
    5 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    3156405763462 unicast packets  633308523 multicast packets  1208862603 broadcast packets
    3158247934588 output packets  4312518541635564 bytes
    2164932696756 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  241613359 output discard
    0 Tx pause

Ethernet1/10/3 is up
admin state is up, Dedicated Interface
  Hardware: 10000/40000 Ethernet, address: ecbd.1dea.5c06 (bia ecbd.1dea.5c06)
  Description: bu-commed2
  MTU 1500 bytes, BW 10000000 Kbit, DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is access
  full-duplex, 10 Gb/s, media type is 40G
  Beacon is turned off
  Auto-Negotiation is turned on
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Rate mode is dedicated
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
  Last link flapped 55week(s) 2day(s)
  Last clearing of "" counters never
  572 interface resets
  30 seconds input rate 0 bits/sec, 0 packets/sec
  30 seconds output rate 8864 bits/sec, 10 packets/sec
  Load-Interval #2: 5 minute (300 seconds)
    input rate 0 bps, 0 pps; output rate 8.12 Kbps, 8 pps
  RX
    4463428716952 unicast packets  5102731 multicast packets  3906269 broadcast packets
    4463437725952 input packets  2715951812754497 bytes
    0 jumbo packets  0 storm suppression packets
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    33494036 Rx pause
  TX
    5493199553026 unicast packets  359652696 multicast packets  1363805791 broadcast packets
    5494923011513 output packets  7927459853706472 bytes
    1 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  69479076 output discard
    0 Tx pause

Ethernet1/10/4 is up
admin state is up, Dedicated Interface
  Hardware: 10000/40000 Ethernet, address: ecbd.1dea.5c07 (bia ecbd.1dea.5c07)
  Description: appdev-ml_eth0
  MTU 1500 bytes, BW 10000000 Kbit, DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is access
  full-duplex, 10 Gb/s, media type is 40G
  Beacon is turned off
  Auto-Negotiation is turned on
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Rate mode is dedicated
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
  Last link flapped 83week(s) 0day(s)
  Last clearing of "" counters never
  5 interface resets
  30 seconds input rate 160 bits/sec, 0 packets/sec
  30 seconds output rate 9032 bits/sec, 10 packets/sec
  Load-Interval #2: 5 minute (300 seconds)
    input rate 128 bps, 0 pps; output rate 8.52 Kbps, 8 pps
  RX
    3669246156 unicast packets  2224016 multicast packets  9975 broadcast packets
    3671480147 input packets  5496779292556 bytes
    0 jumbo packets  0 storm suppression packets
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    597122145 unicast packets  102310504 multicast packets  325643271 broadcast packets
    1025075920 output packets  202732637866 bytes
    1 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  18179 output discard
    0 Tx pause

Ethernet1/11 is up
admin state is up, Dedicated Interface
  Hardware: 10000/40000 Ethernet, address: ecbd.1dea.5c08 (bia ecbd.1dea.5c08)
  Description: Qumulo-5-eth1
  MTU 1500 bytes, BW 40000000 Kbit, DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is access
  full-duplex, 40 Gb/s, media type is 40G
  Beacon is turned off
  Auto-Negotiation is turned on
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Rate mode is dedicated
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
  Last link flapped 13week(s) 1day(s)
  Last clearing of "" counters never
  94 interface resets
  30 seconds input rate 11765744 bits/sec, 1146 packets/sec
  30 seconds output rate 1490288 bits/sec, 355 packets/sec
  Load-Interval #2: 5 minute (300 seconds)
    input rate 20.04 Mbps, 1.77 Kpps; output rate 772.30 Kbps, 281 pps
  RX
    3513247264927 unicast packets  10396685 multicast packets  8726 broadcast packets
    3513257670338 input packets  4996306507349792 bytes
    0 jumbo packets  0 storm suppression packets
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    15971181 Rx pause
  TX
    1286366549696 unicast packets  321652068 multicast packets  1077924618 broadcast packets
    1287766126382 output packets  1557031649493141 bytes
    1 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  161348424 output discard
    0 Tx pause

Ethernet1/12 is up
admin state is up, Dedicated Interface
  Hardware: 10000/40000 Ethernet, address: ecbd.1dea.5c0c (bia ecbd.1dea.5c0c)
  Description: Qumulo-6-eth1
  MTU 1500 bytes, BW 40000000 Kbit, DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is access
  full-duplex, 40 Gb/s, media type is 40G
  Beacon is turned off
  Auto-Negotiation is turned on
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Rate mode is dedicated
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
  Last link flapped 13week(s) 1day(s)
  Last clearing of "" counters never
  102 interface resets
  30 seconds input rate 56757776 bits/sec, 5301 packets/sec
  30 seconds output rate 45906872 bits/sec, 6150 packets/sec
  Load-Interval #2: 5 minute (300 seconds)
    input rate 91.73 Mbps, 8.71 Kpps; output rate 80.43 Mbps, 9.89 Kpps
  RX
    6352273428933 unicast packets  10402326 multicast packets  9708 broadcast packets
    6352283840967 input packets  8756469040010149 bytes
    0 jumbo packets  0 storm suppression packets
    0 runts  0 giants  2 CRC  0 no buffer
    2 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    31704198 Rx pause
  TX
    4175521789289 unicast packets  321471250 multicast packets  1077667057 broadcast packets
    4176920927596 output packets  5013632091233527 bytes
    1 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  532792557 output discard
    0 Tx pause

Ethernet1/13 is up
admin state is up, Dedicated Interface
  Hardware: 10000/40000 Ethernet, address: ecbd.1dea.5c10 (bia ecbd.1dea.5c10)
  Description: Qumulo-7-eth1
  MTU 1500 bytes, BW 40000000 Kbit, DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is access
  full-duplex, 40 Gb/s, media type is 40G
  Beacon is turned off
  Auto-Negotiation is turned on
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Rate mode is dedicated
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
  Last link flapped 4week(s) 2day(s)
  Last clearing of "" counters never
  98 interface resets
  30 seconds input rate 13955288 bits/sec, 1300 packets/sec
  30 seconds output rate 681144 bits/sec, 278 packets/sec
  Load-Interval #2: 5 minute (300 seconds)
    input rate 21.18 Mbps, 1.84 Kpps; output rate 672.86 Kbps, 238 pps
  RX
    3987023267033 unicast packets  10397120 multicast packets  9314 broadcast packets
    3987033673467 input packets  5753179171311864 bytes
    0 jumbo packets  0 storm suppression packets
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    22874961 Rx pause
  TX
    1529995769546 unicast packets  321645364 multicast packets  1077901522 broadcast packets
    1531395316432 output packets  1850822989718800 bytes
    1 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  156598971 output discard
    0 Tx pause

Ethernet1/14 is up
admin state is up, Dedicated Interface
  Hardware: 10000/40000 Ethernet, address: ecbd.1dea.5c11 (bia ecbd.1dea.5c11)
  Description: Qumulo-8-eth1
  MTU 1500 bytes, BW 40000000 Kbit, DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is access
  full-duplex, 40 Gb/s, media type is 40G
  Beacon is turned off
  Auto-Negotiation is turned on
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Rate mode is dedicated
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
  Last link flapped 13week(s) 1day(s)
  Last clearing of "" counters never
  104 interface resets
  30 seconds input rate 16475568 bits/sec, 1523 packets/sec
  30 seconds output rate 1952376 bits/sec, 426 packets/sec
  Load-Interval #2: 5 minute (300 seconds)
    input rate 22.25 Mbps, 1.89 Kpps; output rate 887.95 Kbps, 218 pps
  RX
    2499046543026 unicast packets  9941484 multicast packets  7865 broadcast packets
    2499056492375 input packets  3547558176480519 bytes
    0 jumbo packets  0 storm suppression packets
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    60961065 Rx pause
  TX
    1376757202660 unicast packets  321680822 multicast packets  1077985519 broadcast packets
    1378156869001 output packets  1730315479778035 bytes
    1 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/15 is down (XCVR not inserted)
admin state is down, Dedicated Interface
  Hardware: 10000/40000 Ethernet, address: ecbd.1dea.5bdf (bia ecbd.1dea.5c12)
  MTU 1500 bytes, BW 40000000 Kbit, DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
  Last link flapped 83week(s) 1day(s)
  Last clearing of "" counters never
  51 interface resets
  30 seconds input rate 0 bits/sec, 0 packets/sec
  30 seconds output rate 0 bits/sec, 0 packets/sec
  Load-Interval #2: 5 minute (300 seconds)
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    39167144 unicast packets  73363 multicast packets  682 broadcast packets
    39241189 input packets  9541251657 bytes
    0 jumbo packets  0 storm suppression packets
    0 runts  0 giants  7 CRC  0 no buffer
    10 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    30 Rx pause
  TX
    55931387 unicast packets  7269369 multicast packets  15221341 broadcast packets
    78422097 output packets  41080879323 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/16 is down (XCVR not inserted)
admin state is down, Dedicated Interface
  Hardware: 10000/40000 Ethernet, address: ecbd.1dea.5bdf (bia ecbd.1dea.5c16)
  Description: BAD_PORT
  MTU 1500 bytes, BW 40000000 Kbit, DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
  Last link flapped 202week(s) 0day(s)
  Last clearing of "" counters 84w2d
  0 interface resets
  30 seconds input rate 0 bits/sec, 0 packets/sec
  30 seconds output rate 0 bits/sec, 0 packets/sec
  Load-Interval #2: 5 minute (300 seconds)
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    86425 unicast packets  0 multicast packets  0 broadcast packets
    86425 input packets  121690844 bytes
    0 jumbo packets  0 storm suppression packets
    0 runts  0 giants  7 CRC  0 no buffer
    7 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    86432 unicast packets  0 multicast packets  0 broadcast packets
    86432 output packets  121696256 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/17 is up
admin state is up, Dedicated Interface
  Hardware: 10000/40000 Ethernet, address: ecbd.1dea.5c1a (bia ecbd.1dea.5c1a)
  Description: Qumulo-9-eth1
  MTU 1500 bytes, BW 40000000 Kbit, DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is access
  full-duplex, 40 Gb/s, media type is 40G
  Beacon is turned off
  Auto-Negotiation is turned on
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Rate mode is dedicated
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
  Last link flapped 13week(s) 1day(s)
  Last clearing of "" counters never
  94 interface resets
  30 seconds input rate 15249104 bits/sec, 1460 packets/sec
  30 seconds output rate 5167768 bits/sec, 634 packets/sec
  Load-Interval #2: 5 minute (300 seconds)
    input rate 22.12 Mbps, 2.01 Kpps; output rate 3.84 Mbps, 561 pps
  RX
    9571510561422 unicast packets  10332210 multicast packets  5696 broadcast packets
    9571520899328 input packets  13344389955782387 bytes
    0 jumbo packets  0 storm suppression packets
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    152997324 Rx pause
  TX
    7960990937609 unicast packets  320707758 multicast packets  1072538592 broadcast packets
    7962384183959 output packets  10032745539923951 bytes
    1 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/18/1 is down (XCVR not inserted)
admin state is down, Dedicated Interface
  Hardware: 10000/40000 Ethernet, address: ecbd.1dea.5bdf (bia ecbd.1dea.5c1e)
  MTU 1500 bytes, BW 10000000 Kbit, DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  30 seconds input rate 0 bits/sec, 0 packets/sec
  30 seconds output rate 0 bits/sec, 0 packets/sec
  Load-Interval #2: 5 minute (300 seconds)
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    402248 unicast packets  0 multicast packets  0 broadcast packets
    402248 input packets  566365184 bytes
    0 jumbo packets  0 storm suppression packets
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    402248 unicast packets  0 multicast packets  0 broadcast packets
    402248 output packets  566365184 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/18/2 is down (XCVR not inserted)
admin state is down, Dedicated Interface
  Hardware: 10000/40000 Ethernet, address: ecbd.1dea.5bdf (bia ecbd.1dea.5c1f)
  MTU 1500 bytes, BW 10000000 Kbit, DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  30 seconds input rate 0 bits/sec, 0 packets/sec
  30 seconds output rate 0 bits/sec, 0 packets/sec
  Load-Interval #2: 5 minute (300 seconds)
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    130792 unicast packets  0 multicast packets  0 broadcast packets
    130792 input packets  184155136 bytes
    0 jumbo packets  0 storm suppression packets
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    130792 unicast packets  0 multicast packets  0 broadcast packets
    130792 output packets  184155136 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/18/3 is down (XCVR not inserted)
admin state is down, Dedicated Interface
  Hardware: 10000/40000 Ethernet, address: ecbd.1dea.5bdf (bia ecbd.1dea.5c20)
  MTU 1500 bytes, BW 10000000 Kbit, DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  30 seconds input rate 0 bits/sec, 0 packets/sec
  30 seconds output rate 0 bits/sec, 0 packets/sec
  Load-Interval #2: 5 minute (300 seconds)
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    130792 unicast packets  0 multicast packets  0 broadcast packets
    130792 input packets  184155136 bytes
    0 jumbo packets  0 storm suppression packets
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    130792 unicast packets  0 multicast packets  0 broadcast packets
    130792 output packets  184155136 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/18/4 is down (XCVR not inserted)
admin state is down, Dedicated Interface
  Hardware: 10000/40000 Ethernet, address: ecbd.1dea.5bdf (bia ecbd.1dea.5c21)
  MTU 1500 bytes, BW 10000000 Kbit, DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  30 seconds input rate 0 bits/sec, 0 packets/sec
  30 seconds output rate 0 bits/sec, 0 packets/sec
  Load-Interval #2: 5 minute (300 seconds)
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    130792 unicast packets  0 multicast packets  0 broadcast packets
    130792 input packets  184155136 bytes
    0 jumbo packets  0 storm suppression packets
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    130792 unicast packets  0 multicast packets  0 broadcast packets
    130792 output packets  184155136 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/19 is down (XCVR not inserted)
admin state is down, Dedicated Interface
  Hardware: 10000/40000 Ethernet, address: ecbd.1dea.5bdf (bia ecbd.1dea.5c22)
  MTU 1500 bytes, BW 40000000 Kbit, DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  30 seconds input rate 0 bits/sec, 0 packets/sec
  30 seconds output rate 0 bits/sec, 0 packets/sec
  Load-Interval #2: 5 minute (300 seconds)
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    402248 unicast packets  0 multicast packets  0 broadcast packets
    402248 input packets  566365184 bytes
    0 jumbo packets  0 storm suppression packets
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    402248 unicast packets  0 multicast packets  0 broadcast packets
    402248 output packets  566365184 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  838568 output discard
    0 Tx pause

Ethernet1/20/1 is down (Link not connected)
admin state is up, Dedicated Interface
  Hardware: 10000/40000 Ethernet, address: ecbd.1dea.5c26 (bia ecbd.1dea.5c26)
  Description: mlib-vm2019-2-wan
  MTU 1500 bytes, BW 10000000 Kbit, DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is access
  auto-duplex, auto-speed, media type is 40G
  Beacon is turned off
  Auto-Negotiation is turned on
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Rate mode is dedicated
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  30 seconds input rate 0 bits/sec, 0 packets/sec
  30 seconds output rate 0 bits/sec, 0 packets/sec
  Load-Interval #2: 5 minute (300 seconds)
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    254932 unicast packets  0 multicast packets  0 broadcast packets
    254932 input packets  358944256 bytes
    0 jumbo packets  0 storm suppression packets
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    254932 unicast packets  0 multicast packets  0 broadcast packets
    254932 output packets  358944256 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/20/2 is down (Link not connected)
admin state is up, Dedicated Interface
  Hardware: 10000/40000 Ethernet, address: ecbd.1dea.5c27 (bia ecbd.1dea.5c27)
  Description: mlib-vm2019-2-stor
  MTU 1500 bytes, BW 10000000 Kbit, DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is access
  auto-duplex, auto-speed, media type is 40G
  Beacon is turned off
  Auto-Negotiation is turned on
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Rate mode is dedicated
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  30 seconds input rate 0 bits/sec, 0 packets/sec
  30 seconds output rate 0 bits/sec, 0 packets/sec
  Load-Interval #2: 5 minute (300 seconds)
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    134172 unicast packets  0 multicast packets  0 broadcast packets
    134172 input packets  188914176 bytes
    0 jumbo packets  0 storm suppression packets
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    134172 unicast packets  0 multicast packets  0 broadcast packets
    134172 output packets  188914176 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/20/3 is up
admin state is up, Dedicated Interface
  Hardware: 10000/40000 Ethernet, address: ecbd.1dea.5c28 (bia ecbd.1dea.5c28)
  Description: mlib-ns1-b0
  MTU 9216 bytes, BW 10000000 Kbit, DLY 10 usec
  reliability 255/255, txload 1/255, rxload 15/255
  Encapsulation ARPA, medium is broadcast
  Port mode is access
  full-duplex, 10 Gb/s, media type is 40G
  Beacon is turned off
  Auto-Negotiation is turned on
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Rate mode is dedicated
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
  Last link flapped 38week(s) 1day(s)
  Last clearing of "" counters never
  31 interface resets
  30 seconds input rate 615353072 bits/sec, 9453 packets/sec
  30 seconds output rate 46559896 bits/sec, 4479 packets/sec
  Load-Interval #2: 5 minute (300 seconds)
    input rate 488.42 Mbps, 7.47 Kpps; output rate 28.13 Mbps, 3.43 Kpps
  RX
    68802761110 unicast packets  769079 multicast packets  2104088 broadcast packets
    68805634277 input packets  494737765109181 bytes
    56773514306 jumbo packets  0 storm suppression packets
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    2 Rx pause
  TX
    40309170698 unicast packets  97620165 multicast packets  282240154 broadcast packets
    40689031017 output packets  112010493517761 bytes
    14335829627 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  937 output discard
    0 Tx pause

Ethernet1/20/4 is up
admin state is up, Dedicated Interface
  Hardware: 10000/40000 Ethernet, address: ecbd.1dea.5c29 (bia ecbd.1dea.5c29)
  Description: mlib-ns1-b1
  MTU 9216 bytes, BW 10000000 Kbit, DLY 10 usec
  reliability 255/255, txload 1/255, rxload 15/255
  Encapsulation ARPA, medium is broadcast
  Port mode is access
  full-duplex, 10 Gb/s, media type is 40G
  Beacon is turned off
  Auto-Negotiation is turned on
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Rate mode is dedicated
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
  Last link flapped 38week(s) 1day(s)
  Last clearing of "" counters never
  26 interface resets
  30 seconds input rate 613742624 bits/sec, 9417 packets/sec
  30 seconds output rate 46219992 bits/sec, 4464 packets/sec
  Load-Interval #2: 5 minute (300 seconds)
    input rate 486.15 Mbps, 7.44 Kpps; output rate 28.68 Mbps, 3.42 Kpps
  RX
    70095074369 unicast packets  769084 multicast packets  740524 broadcast packets
    70096583977 input packets  499508068312875 bytes
    57131919777 jumbo packets  0 storm suppression packets
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    2 Rx pause
  TX
    40610172149 unicast packets  97620259 multicast packets  283603845 broadcast packets
    40991396253 output packets  113394725140475 bytes
    14517819917 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  937 output discard
    0 Tx pause

Ethernet1/21 is down (XCVR not inserted)
admin state is down, Dedicated Interface
  Hardware: 10000/40000 Ethernet, address: ecbd.1dea.5bdf (bia ecbd.1dea.5c2a)
  MTU 1500 bytes, BW 40000000 Kbit, DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  30 seconds input rate 0 bits/sec, 0 packets/sec
  30 seconds output rate 0 bits/sec, 0 packets/sec
  Load-Interval #2: 5 minute (300 seconds)
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    402248 unicast packets  0 multicast packets  0 broadcast packets
    402248 input packets  566365184 bytes
    0 jumbo packets  0 storm suppression packets
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    402248 unicast packets  0 multicast packets  0 broadcast packets
    402248 output packets  566365184 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/22 is down (XCVR not inserted)
admin state is down, Dedicated Interface
  Hardware: 10000/40000 Ethernet, address: ecbd.1dea.5bdf (bia ecbd.1dea.5c2e)
  MTU 1500 bytes, BW 40000000 Kbit, DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  30 seconds input rate 0 bits/sec, 0 packets/sec
  30 seconds output rate 0 bits/sec, 0 packets/sec
  Load-Interval #2: 5 minute (300 seconds)
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    402248 unicast packets  0 multicast packets  0 broadcast packets
    402248 input packets  566365184 bytes
    0 jumbo packets  0 storm suppression packets
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    402248 unicast packets  0 multicast packets  0 broadcast packets
    402248 output packets  566365184 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/23 is down (XCVR not inserted)
admin state is up, Dedicated Interface
  Hardware: 10000/40000 Ethernet, address: ecbd.1dea.5c32 (bia ecbd.1dea.5c32)
  Description: Mlib Test
  MTU 1500 bytes, BW 40000000 Kbit, DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is access
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
  Last link flapped 21week(s) 4day(s)
  Last clearing of "" counters never
  2 interface resets
  30 seconds input rate 0 bits/sec, 0 packets/sec
  30 seconds output rate 0 bits/sec, 0 packets/sec
  Load-Interval #2: 5 minute (300 seconds)
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    3379184 unicast packets  25 multicast packets  65 broadcast packets
    3379274 input packets  4457117516 bytes
    0 jumbo packets  0 storm suppression packets
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    190 Rx pause
  TX
    3457722 unicast packets  218 multicast packets  715 broadcast packets
    3458655 output packets  4616607143 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/24 is down (XCVR not inserted)
admin state is down, Dedicated Interface
  Hardware: 10000/40000 Ethernet, address: ecbd.1dea.5bdf (bia ecbd.1dea.5c36)
  MTU 1500 bytes, BW 40000000 Kbit, DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  30 seconds input rate 0 bits/sec, 0 packets/sec
  30 seconds output rate 0 bits/sec, 0 packets/sec
  Load-Interval #2: 5 minute (300 seconds)
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    402248 unicast packets  0 multicast packets  0 broadcast packets
    402248 input packets  566365184 bytes
    0 jumbo packets  0 storm suppression packets
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    402248 unicast packets  0 multicast packets  0 broadcast packets
    402248 output packets  566365184 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/25/1 is up
admin state is up, Dedicated Interface
  Belongs to Po31
  Hardware: 10000/40000 Ethernet, address: ecbd.1dea.5c3a (bia ecbd.1dea.5c3a)
  Description: #e1/25/1:ddr1-ddc-i13:1/14
  MTU 9216 bytes, BW 10000000 Kbit, DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is trunk
  full-duplex, 10 Gb/s, media type is 40G
  Beacon is turned off
  Auto-Negotiation is turned on
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Rate mode is dedicated
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
  Last link flapped 6week(s) 2day(s)
  Last clearing of "" counters 203w2d
  9 interface resets
  30 seconds input rate 1443752 bits/sec, 2318 packets/sec
  30 seconds output rate 6480672 bits/sec, 617 packets/sec
  Load-Interval #2: 5 minute (300 seconds)
    input rate 1.91 Mbps, 2.90 Kpps; output rate 3.96 Mbps, 604 pps
  RX
    2917429763193 unicast packets  272077178 multicast packets  234196679 broadcast packets
    2917936037050 input packets  2888878122627352 bytes
    1677752326374 jumbo packets  0 storm suppression packets
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    6408936112148 unicast packets  61311464 multicast packets  17987014 broadcast packets
    6409015410626 output packets  8777710532783848 bytes
    3713307327143 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  2 output discard
    0 Tx pause

Ethernet1/25/2 is down (Administratively down)
admin state is down, Dedicated Interface
  Hardware: 10000/40000 Ethernet, address: ecbd.1dea.5bdf (bia ecbd.1dea.5c3b)
  MTU 1500 bytes, BW 10000000 Kbit, DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed, media type is 40G
  Beacon is turned off
  Auto-Negotiation is turned on
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Rate mode is dedicated
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  30 seconds input rate 0 bits/sec, 0 packets/sec
  30 seconds output rate 0 bits/sec, 0 packets/sec
  Load-Interval #2: 5 minute (300 seconds)
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    400544 unicast packets  0 multicast packets  0 broadcast packets
    400544 input packets  563965952 bytes
    0 jumbo packets  0 storm suppression packets
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    400544 unicast packets  0 multicast packets  0 broadcast packets
    400544 output packets  563965952 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/25/3 is down (Administratively down)
admin state is down, Dedicated Interface
  Hardware: 10000/40000 Ethernet, address: ecbd.1dea.5bdf (bia ecbd.1dea.5c3c)
  MTU 1500 bytes, BW 10000000 Kbit, DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed, media type is 40G
  Beacon is turned off
  Auto-Negotiation is turned on
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Rate mode is dedicated
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  30 seconds input rate 0 bits/sec, 0 packets/sec
  30 seconds output rate 0 bits/sec, 0 packets/sec
  Load-Interval #2: 5 minute (300 seconds)
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    400544 unicast packets  0 multicast packets  0 broadcast packets
    400544 input packets  563965952 bytes
    0 jumbo packets  0 storm suppression packets
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    400544 unicast packets  0 multicast packets  0 broadcast packets
    400544 output packets  563965952 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/25/4 is down (Administratively down)
admin state is down, Dedicated Interface
  Hardware: 10000/40000 Ethernet, address: ecbd.1dea.5bdf (bia ecbd.1dea.5c3d)
  MTU 1500 bytes, BW 10000000 Kbit, DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed, media type is 40G
  Beacon is turned off
  Auto-Negotiation is turned on
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Rate mode is dedicated
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  30 seconds input rate 0 bits/sec, 0 packets/sec
  30 seconds output rate 0 bits/sec, 0 packets/sec
  Load-Interval #2: 5 minute (300 seconds)
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    400544 unicast packets  0 multicast packets  0 broadcast packets
    400544 input packets  563965952 bytes
    0 jumbo packets  0 storm suppression packets
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    400544 unicast packets  0 multicast packets  0 broadcast packets
    400544 output packets  563965952 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/26/1 is up
admin state is up, Dedicated Interface
  Belongs to Po31
  Hardware: 10000/40000 Ethernet, address: ecbd.1dea.5c3e (bia ecbd.1dea.5c3e)
  Description: #e1/26/1:ddr2-ddc-j13:1/14
  MTU 9216 bytes, BW 10000000 Kbit, DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is trunk
  full-duplex, 10 Gb/s, media type is 40G
  Beacon is turned off
  Auto-Negotiation is turned on
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Rate mode is dedicated
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
  Last link flapped 159week(s) 1day(s)
  Last clearing of "" counters 203w2d
  4 interface resets
  30 seconds input rate 218664 bits/sec, 126 packets/sec
  30 seconds output rate 54448240 bits/sec, 4801 packets/sec
  Load-Interval #2: 5 minute (300 seconds)
    input rate 639.94 Kbps, 327 pps; output rate 89.53 Mbps, 7.73 Kpps
  RX
    2154330007610 unicast packets  194861437 multicast packets  735028611 broadcast packets
    2155259897658 input packets  2755652494550865 bytes
    1656299053924 jumbo packets  0 storm suppression packets
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    7043073988020 unicast packets  24588276 multicast packets  9479902 broadcast packets
    7043108056198 output packets  9690191083776036 bytes
    5633488649250 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  281 output discard
    0 Tx pause

Ethernet1/26/2 is down (Administratively down)
admin state is down, Dedicated Interface
  Hardware: 10000/40000 Ethernet, address: ecbd.1dea.5bdf (bia ecbd.1dea.5c3f)
  MTU 1500 bytes, BW 10000000 Kbit, DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed, media type is 40G
  Beacon is turned off
  Auto-Negotiation is turned on
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Rate mode is dedicated
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  30 seconds input rate 0 bits/sec, 0 packets/sec
  30 seconds output rate 0 bits/sec, 0 packets/sec
  Load-Interval #2: 5 minute (300 seconds)
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    281484 unicast packets  0 multicast packets  0 broadcast packets
    281484 input packets  396329472 bytes
    0 jumbo packets  0 storm suppression packets
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    281484 unicast packets  0 multicast packets  0 broadcast packets
    281484 output packets  396329472 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/26/3 is down (Administratively down)
admin state is down, Dedicated Interface
  Hardware: 10000/40000 Ethernet, address: ecbd.1dea.5bdf (bia ecbd.1dea.5c40)
  MTU 1500 bytes, BW 10000000 Kbit, DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed, media type is 40G
  Beacon is turned off
  Auto-Negotiation is turned on
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Rate mode is dedicated
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  30 seconds input rate 0 bits/sec, 0 packets/sec
  30 seconds output rate 0 bits/sec, 0 packets/sec
  Load-Interval #2: 5 minute (300 seconds)
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX[K
    281484 unicast packets  0 multicast packets  0 broadcast packets
    281484 input packets  396329472 bytes
    0 jumbo packets  0 storm suppression packets
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    281484 unicast packets  0 multicast packets  0 broadcast packets
    281484 output packets  396329472 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/26/4 is down (Administratively down)
admin state is down, Dedicated Interface
  Hardware: 10000/40000 Ethernet, address: ecbd.1dea.5bdf (bia ecbd.1dea.5c41)
  MTU 1500 bytes, BW 10000000 Kbit, DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed, media type is 40G
  Beacon is turned off
  Auto-Negotiation is turned on
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Rate mode is dedicated
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  30 seconds input rate 0 bits/sec, 0 packets/sec
  30 seconds output rate 0 bits/sec, 0 packets/sec
  Load-Interval #2: 5 minute (300 seconds)
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    281484 unicast packets  0 multicast packets  0 broadcast packets
    281484 input packets  396329472 bytes
    0 jumbo packets  0 storm suppression packets
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    281484 unicast packets  0 multicast packets  0 broadcast packets
    281484 output packets  396329472 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/27 is down (XCVR not inserted)
admin state is down, Dedicated Interface
  Hardware: 10000/40000 Ethernet, address: ecbd.1dea.5bdf (bia ecbd.1dea.5c42)
  MTU 1500 bytes, BW 40000000 Kbit, DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  30 seconds input rate 0 bits/sec, 0 packets/sec
  30 seconds output rate 0 bits/sec, 0 packets/sec
  Load-Interval #2: 5 minute (300 seconds)
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 input packets  0 bytes
    0 jumbo packets  0 storm suppression packets
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

Ethernet1/28 is down (XCVR not inserted)
admin state is down, Dedicated Interface
  Hardware: 10000/40000 Ethernet, address: ecbd.1dea.5bdf (bia ecbd.1dea.5c43)
  MTU 1500 bytes, BW 40000000 Kbit, DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  30 seconds input rate 0 bits/sec, 0 packets/sec
  30 seconds output rate 0 bits/sec, 0 packets/sec
  Load-Interval #2: 5 minute (300 seconds)
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 input packets  0 bytes
    0 jumbo packets  0 storm suppression packets
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

Ethernet1/29 is down (XCVR not inserted)
admin state is down, Dedicated Interface
  Hardware: 10000/40000 Ethernet, address: ecbd.1dea.5bdf (bia ecbd.1dea.5c44)
  MTU 1500 bytes, BW 40000000 Kbit, DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  30 seconds input rate 0 bits/sec, 0 packets/sec
  30 seconds output rate 0 bits/sec, 0 packets/sec
  Load-Interval #2: 5 minute (300 seconds)
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 input packets  0 bytes
    0 jumbo packets  0 storm suppression packets
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
  Hardware: 10000/40000 Ethernet, address: ecbd.1dea.5bdf (bia ecbd.1dea.5c45)
  MTU 1500 bytes, BW 40000000 Kbit, DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
  Last link flapped never
  Last clearing of "" counters never
  0 interface resets
  30 seconds input rate 0 bits/sec, 0 packets/sec
  30 seconds output rate 0 bits/sec, 0 packets/sec
  Load-Interval #2: 5 minute (300 seconds)
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 input packets  0 bytes
    0 jumbo packets  0 storm suppression packets
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

Ethernet1/31 is up
admin state is up, Dedicated Interface
  Hardware: 10000/40000 Ethernet, address: ecbd.1dea.5bdf (bia ecbd.1dea.5c46)
  MTU 1500 bytes, BW 40000000 Kbit, DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  full-duplex, 40 Gb/s, media type is 40G
  Beacon is turned off
  Auto-Negotiation is turned on
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Rate mode is dedicated
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
  Last link flapped 205week(s) 2day(s)
  Last clearing of "" counters never
  1 interface resets
  30 seconds input rate 208 bits/sec, 0 packets/sec
  30 seconds output rate 200 bits/sec, 0 packets/sec
  Load-Interval #2: 5 minute (300 seconds)
    input rate 192 bps, 0 pps; output rate 192 bps, 0 pps
  RX
    0 unicast packets  14483728 multicast packets  0 broadcast packets
    14483728 input packets  3050397785 bytes
    0 jumbo packets  0 storm suppression packets
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    0 unicast packets  14483674 multicast packets  0 broadcast packets
    14483674 output packets  3050382748 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

Ethernet1/32 is up
admin state is up, Dedicated Interface
  Hardware: 10000/40000 Ethernet, address: ecbd.1dea.5bdf (bia ecbd.1dea.5c47)
  MTU 1500 bytes, BW 40000000 Kbit, DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  full-duplex, 40 Gb/s, media type is 40G
  Beacon is turned off
  Auto-Negotiation is turned on
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Rate mode is dedicated
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
  Last link flapped 205week(s) 2day(s)
  Last clearing of "" counters never
  1 interface resets
  30 seconds input rate 224 bits/sec, 0 packets/sec
  30 seconds output rate 224 bits/sec, 0 packets/sec
  Load-Interval #2: 5 minute (300 seconds)
    input rate 192 bps, 0 pps; output rate 192 bps, 0 pps
  RX
    0 unicast packets  14483719 multicast packets  0 broadcast packets
    14483719 input packets  3050395979 bytes
    0 jumbo packets  0 storm suppression packets
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    0 unicast packets  14483667 multicast packets  0 broadcast packets
    14483667 output packets  3050381210 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause

port-channel31 is up
admin state is up,
  Hardware: Port-Channel, address: ecbd.1dea.5c3e (bia ecbd.1dea.5c3e)
  Description: ddr1-ddc-i13 and ddr2-ddc-j13
  MTU 9216 bytes, BW 20000000 Kbit, DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is trunk
  full-duplex, 10 Gb/s
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off 
  EtherType is 0x8100 
  Members in this channel: Eth1/25/1, Eth1/26/1
  Last clearing of "" counters never
  3 interface resets
  30 seconds input rate 1662416 bits/sec, 2444 packets/sec
  30 seconds output rate 60928912 bits/sec, 5418 packets/sec
  Load-Interval #2: 5 minute (300 seconds)
    input rate 2.55 Mbps, 3.23 Kpps; output rate 93.49 Mbps, 8.33 Kpps
  RX
    5071759770803 unicast packets  466938615 multicast packets  969225290 broadcast packets
    5073195934708 input packets  5644530617178217 bytes
    3334051380298 jumbo packets  0 storm suppression packets
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    13452010100168 unicast packets  85899740 multicast packets  27466916 broadcast packets
    13452123466824 output packets  18467901616559884 bytes
    9346795976393 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  283 output discard
    0 Tx pause

Vlan1 is down (Administratively down), line protocol is down
  Hardware is EtherSVI, address is  ecbd.1dea.5bdf
  MTU 1500 bytes, BW 1000000 Kbit, DLY 10 usec,
   reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported
  ARP type: ARPA
  Last clearing of "" counters never
  L3 in Switched:
    ucast: 0 pkts, 0 bytes
""",
 'show inventory':"""NAME: "Chassis",  DESCR: "Nexus9000 C9332PQ chassis"             
PID: N9K-C9332PQ         ,  VID: V02 ,  SN: SAL1934MZPC          

NAME: "Slot 1",  DESCR: "32p 40G Ethernet Module"               
PID: N9K-C9332PQ         ,  VID: V02 ,  SN: SAL1934MZPC          

NAME: "Power Supply 1",  DESCR: "Nexus9000 C9332PQ chassis Power Supply"
PID: N9K-PAC-650W-B      ,  VID: V01 ,  SN: DCB1936Y0Z3          

NAME: "Power Supply 2",  DESCR: "Nexus9000 C9332PQ chassis Power Supply"
PID: N9K-PAC-650W-B      ,  VID: V01 ,  SN: DCB1936Y0WE          

NAME: "Fan 1",  DESCR: "Nexus9000 C9332PQ chassis Fan Module"  
PID: NXA-FAN-30CFM-F     ,  VID: V01 ,  SN: N/A                  

NAME: "Fan 2",  DESCR: "Nexus9000 C9332PQ chassis Fan Module"  
PID: NXA-FAN-30CFM-F     ,  VID: V01 ,  SN: N/A                  

NAME: "Fan 3",  DESCR: "Nexus9000 C9332PQ chassis Fan Module"  
PID: NXA-FAN-30CFM-F     ,  VID: V01 ,  SN: N/A                  

NAME: "Fan 4",  DESCR: "Nexus9000 C9332PQ chassis Fan Module"  
PID: NXA-FAN-30CFM-F     ,  VID: V01 ,  SN: N/A                  
""",
 'show interface counters':"""--------------------------------------------------------------------------------
Port                                 InOctets                      InUcastPkts
--------------------------------------------------------------------------------
mgmt0                            184079754719                        115902802
Eth1/1                        154391014517783                      65719386908
Eth1/2                        217677682807403                     110568702561
Eth1/3                       1417928811034977                    1011902103044
Eth1/4                       1818944967118135                    1362320403863
Eth1/5                       2259832433746887                    1625028499960
Eth1/6                       2605144547194288                    1942932061727
Eth1/7                              566365184                           402248
Eth1/8                              566365184                           402248
Eth1/9                              566365184                           402248
Eth1/10/1                    4892610328816816                    3413242975416
Eth1/10/2                    4270049599503790                    3229086870188
Eth1/10/3                    2715951812754497                    4463428716952
Eth1/10/4                       5496779292684                       3669246158
Eth1/11                      4996306511976222                    3513247268427
Eth1/12                      8756469062503908                    6352273445664
Eth1/13                      5753179176780857                    3987023270886
Eth1/14                      3547558180031655                    2499046545595
Eth1/15                            9541251657                         39167144
Eth1/16                             121690844                            86425
Eth1/17                     13344389963848572                    9571510567505
Eth1/18/1                           566365184                           402248
Eth1/18/2                           184155136                           130792
Eth1/18/3                           184155136                           130792
Eth1/18/4                           184155136                           130792
Eth1/19                             566365184                           402248
Eth1/20/1                           358944256                           254932
Eth1/20/2                           188914176                           134172
Eth1/20/3                     494737895410099                      68802777731
Eth1/20/4                     499508200153481                      70095091157
Eth1/21                             566365184                           402248
Eth1/22                             566365184                           402248
Eth1/23                            4457117516                          3379184
Eth1/24                             566365184                           402248
Eth1/25/1                    2888878123246650                    2917429771207
Eth1/25/2                           563965952                           400544
Eth1/25/3                           563965952                           400544
Eth1/25/4                           563965952                           400544
Eth1/26/1                    2755652494568935                    2154330007679
Eth1/26/2                           396329472                           281484
Eth1/26/3                           396329472                           281484
Eth1/26/4                           396329472                           281484
Eth1/27                                     0                                0
Eth1/28                                     0                                0
Eth1/29                                     0                                0
Eth1/30                                     0                                0
Eth1/31                            3050397785                                0
Eth1/32                            3050395979                                0
Po31                         5644530617815585                    5071759778886
Vlan1                                     --                                 0

--------------------------------------------------------------------------------
Port                              InMcastPkts                      InBcastPkts
--------------------------------------------------------------------------------
mgmt0                              1930360306                         27315673
Eth1/1                                1427959                            48469
Eth1/2                                1427984                          1431019
Eth1/3                                1110889                            15544
Eth1/4                                1139399                            15585
Eth1/5                                1111232                            15796
Eth1/6                                1110456                            15953
Eth1/7                                      0                                0
Eth1/8                                      0                                0
Eth1/9                                      0                                0
Eth1/10/1                            13900355                         16326357
Eth1/10/2                            10496906                          6020634
Eth1/10/3                             5102731                          3906269
Eth1/10/4                             2224016                             9975
Eth1/11                              10396685                             8726
Eth1/12                              10402326                             9708
Eth1/13                              10397120                             9314
Eth1/14                               9941484                             7865
Eth1/15                                 73363                              682
Eth1/16                                     0                                0
Eth1/17                              10332210                             5696
Eth1/18/1                                   0                                0
Eth1/18/2                                   0                                0
Eth1/18/3                                   0                                0
Eth1/18/4                                   0                                0
Eth1/19                                     0                                0
Eth1/20/1                                   0                                0
Eth1/20/2                                   0                                0
Eth1/20/3                              769080                          2104088
Eth1/20/4                              769085                           740524
Eth1/21                                     0                                0
Eth1/22                                     0                                0
Eth1/23                                    25                               65
Eth1/24                                     0                                0
Eth1/25/1                           272077187                        234196679
Eth1/25/2                                   0                                0
Eth1/25/3                                   0                                0
Eth1/25/4                                   0                                0
Eth1/26/1                           194861452                        735028660
Eth1/26/2                                   0                                0
Eth1/26/3                                   0                                0
Eth1/26/4                                   0                                0
Eth1/27                                     0                                0
Eth1/28                                     0                                0
Eth1/29                                     0                                0
Eth1/30                                     0                                0
Eth1/31                              14483728                                0
Eth1/32                              14483719                                0
Po31                                466938639                        969225339
Vlan1                                     --                                --

--------------------------------------------------------------------------------
Port                                OutOctets                     OutUcastPkts
--------------------------------------------------------------------------------
mgmt0                             26085941385                        116314789
Eth1/1                        817342061027246                     214265620073
Eth1/2                        780058466102857                     234894449439
Eth1/3                        741831163176969                     617502588657
Eth1/4                       1285196166013035                    1072701654391
Eth1/5                       1218771222206653                    1032449179892
Eth1/6                       1747947087892581                    1486720793773
Eth1/7                              566365184                           402248
Eth1/8                              566365184                           402248
Eth1/9                              566365184                           402248
Eth1/10/1                    4657546551930628                    3583829907997
Eth1/10/2                    4312518541641077                    3156405763463
Eth1/10/3                    7927459853710873                    5493199553026
Eth1/10/4                        202732642331                        597122146
Eth1/11                      1557031649716556                    1286366550770
Eth1/12                      5013632116350688                    4175521816480
Eth1/13                      1850822989939425                    1529995770296
Eth1/14                      1730315479993326                    1376757203453
Eth1/15                           41080879323                         55931387
Eth1/16                             121696256                            86432
Eth1/17                     10032745544447259                    7960990941581
Eth1/18/1                           566365184                           402248
Eth1/18/2                           184155136                           130792
Eth1/18/3                           184155136                           130792
Eth1/18/4                           184155136                           130792
Eth1/19                             566365184                           402248
Eth1/20/1                           358944256                           254932
Eth1/20/2                           188914176                           134172
Eth1/20/3                     112010509168053                      40309185465
Eth1/20/4                     113394741395866                      40610186947
Eth1/21                             566365184                           402248
Eth1/22                             566365184                           402248
Eth1/23                            4616607143                          3457722
Eth1/24                             566365184                           402248
Eth1/25/1                    8777710537164431                    6408936115272
Eth1/25/2                           563965952                           400544
Eth1/25/3                           563965952                           400544
Eth1/25/4                           563965952                           400544
Eth1/26/1                    9690191117013152                    7043074011621
Eth1/26/2                           396329472                           281484
Eth1/26/3                           396329472                           281484
Eth1/26/4                           396329472                           281484
Eth1/27                                     0                                0
Eth1/28                                     0                                0
Eth1/29                                     0                                0
Eth1/30                                     0                                0
Eth1/31                            3050382906                                0
Eth1/32                            3050381210                                0
Po31                        18467901654177583                   13452010126893
Vlan1                                     --                                --

--------------------------------------------------------------------------------
Port                             OutMcastPkts                     OutBcastPkts
--------------------------------------------------------------------------------
mgmt0                                 9041968                             4945
Eth1/1                              147103746                        247161096
Eth1/2                              147534763                        246678611
Eth1/3                               88920107                        387571423
Eth1/4                               88881720                        387494492
Eth1/5                               88919951                        387571713
Eth1/6                               88911374                        387562599
Eth1/7                                      0                                0
Eth1/8                                      0                                0
Eth1/9                                      0                                0
Eth1/10/1                           630319378                       1198463790
Eth1/10/2                           633308547                       1208862661
Eth1/10/3                           359652712                       1363805846
Eth1/10/4                           102310520                        325643326
Eth1/11                             321652084                       1077924673
Eth1/12                             321471266                       1077667112
Eth1/13                             321645380                       1077901577
Eth1/14                             321680840                       1077985590
Eth1/15                               7269369                         15221341
Eth1/16                                     0                                0
Eth1/17                             320707776                       1072538663
Eth1/18/1                                   0                                0
Eth1/18/2                                   0                                0
Eth1/18/3                                   0                                0
Eth1/18/4                                   0                                0
Eth1/19                                     0                                0
Eth1/20/1                                   0                                0
Eth1/20/2                                   0                                0
Eth1/20/3                            97620183                        282240225
Eth1/20/4                            97620277                        283603916
Eth1/21                                     0                                0
Eth1/22                                     0                                0
Eth1/23                                   218                              715
Eth1/24                                     0                                0
Eth1/25/1                            61311466                         17987016
Eth1/25/2                                   0                                0
Eth1/25/3                                   0                                0
Eth1/25/4                                   0                                0
Eth1/26/1                            24588278                          9479905
Eth1/26/2                                   0                                0
Eth1/26/3                                   0                                0
Eth1/26/4                                   0                                0
Eth1/27                                     0                                0
Eth1/28                                     0                                0
Eth1/29                                     0                                0
Eth1/30                                     0                                0
Eth1/31                              14483675                                0
Eth1/32                              14483667                                0
Po31                                 85899744                         27466921
Vlan1                                     --                                --""",
 'show cdp nei detail':"""----------------------------------------
Device ID:dx2-3574ddc-i11-mgmt.net.utah.edu
VTP Management Domain Name: vtp-3574ddc

Interface address(es):
    IPv4 Address: 172.28.65.10
Platform: cisco C9300-48U, Capabilities: Switch IGMP Filtering 
Interface: mgmt0, Port ID (outgoing port): GigabitEthernet2/0/32
Holdtime: 126 sec

Version:
Cisco IOS Software [Everest], Catalyst L3 Switch Software (CAT9K_IOSXE), Version 16.6.5, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2018 by Cisco Systems, Inc.
Compiled Mon 10-Dec-18 12:52 by mcpre

Advertisement Version: 2

Native VLAN: 669
Duplex: full
Mgmt address(es):
    IPv4 Address: 172.28.65.10
----------------------------------------
Device ID:dcx1-ddc-m3.net.utah.edu(SAL1934MZQP)
System Name: dcx1-ddc-m3

Interface address(es):
    IPv4 Address: 172.28.65.101
Platform: N9K-C9332PQ, Capabilities: Router Switch Supports-STP-Dispute
Interface: Ethernet1/31, Port ID (outgoing port): Ethernet1/31
Holdtime: 146 sec

Version:
Cisco Nexus Operating System (NX-OS) Software, Version 7.0(3)I1(2)

Advertisement Version: 2
Duplex: full

MTU: 1500
Physical Location: West Temple DC Row a4
Mgmt address(es):
    IPv4 Address: 172.28.65.101
----------------------------------------
Device ID:dcx1-ddc-m3.net.utah.edu(SAL1934MZQP)
System Name: dcx1-ddc-m3

Interface address(es):
    IPv4 Address: 172.28.65.101
Platform: N9K-C9332PQ, Capabilities: Router Switch Supports-STP-Dispute
Interface: Ethernet1/32, Port ID (outgoing port): Ethernet1/32
Holdtime: 146 sec

Version:
Cisco Nexus Operating System (NX-OS) Software, Version 7.0(3)I1(2)

Advertisement Version: 2
Duplex: full

MTU: 1500
Physical Location: West Temple DC Row a4
Mgmt address(es):
    IPv4 Address: 172.28.65.101
----------------------------------------
Device ID:ddr1-ddc-i13.net.utah.edu(TBM12368112)
System Name: ddr1-ddc-i13

Interface address(es):
    IPv4 Address: 155.97.133.98
Platform: N7K-C7010, Capabilities: Router Switch IGMP Filtering Supports-STP-Dispute
Interface: Ethernet1/25/1, Port ID (outgoing port): Ethernet1/14
Holdtime: 142 sec

Version:
Cisco Nexus Operating System (NX-OS) Software, Version 6.2(16)

Advertisement Version: 2

Native VLAN: 1
Duplex: full

MTU: 9216
Physical Location: DD DC Row i13
Mgmt address(es):
    IPv4 Address: 172.29.1.22
----------------------------------------
Device ID:ddr2-ddc-j13.net.utah.edu(TBM13312176)
System Name: ddr2-ddc-j13

Interface address(es):
    IPv4 Address: 155.97.133.99
Platform: N7K-C7010, Capabilities: Router Switch IGMP Filtering Supports-STP-Dispute
Interface: Ethernet1/26/1, Port ID (outgoing port): Ethernet1/14
Holdtime: 159 sec

Version:
Cisco Nexus Operating System (NX-OS) Software, Version 6.2(16)

Advertisement Version: 2

Native VLAN: 1
Duplex: full

MTU: 9216
Physical Location: DDC Row j13
Mgmt address(es):
    IPv4 Address: 172.29.1.23""",
 'show module all':"""^
% Invalid parameter detected at '^' marker.""",
 'show module':"""Mod  Ports  Module-Type                           Model            Status
---  -----  ------------------------------------- ---------------- ----------
1    32     32p 40G Ethernet Module               N9K-C9332PQ      active *

Mod  Sw                Hw     Slot
---  ----------------  ------ ----
1    7.0(3)I1(2)       2.0    NA  


Mod  MAC-Address(es)                         Serial-Num
---  --------------------------------------  ----------
1    ec-bd-1d-ea-5b-d8 to ec-bd-1d-ea-5c-4d  SAL1934MZPC

Mod  Online Diag Status
---  ------------------
1    Pass

* this terminal session """,
 'show run | section snmp':"""20 permit udp 155.100.122.25/32 any eq snmp 
  30 permit udp 155.100.122.28/32 any eq snmp 
  40 permit udp 155.100.122.50/32 any eq snmp 
  50 permit udp 155.100.122.200/32 any eq snmp 
  30 permit udp 155.98.253.0/24 any eq snmp 
  50 permit udp 155.100.122.113/32 any eq snmp 
  70 permit udp 155.100.240.123/32 any eq snmp 
  100 permit udp 155.101.168.124/32 any eq snmp 
  110 permit udp 10.71.24.10/32 any eq snmp 
  120 permit udp 10.71.24.11/32 any eq snmp 
  130 permit udp 10.71.24.12/32 any eq snmp 
  140 permit udp 10.71.24.13/32 any eq snmp 
  150 permit udp 10.71.24.14/32 any eq snmp 
  160 permit udp 10.71.24.15/32 any eq snmp 
  170 permit udp 10.71.24.16/32 any eq snmp 
  180 permit udp 10.71.24.17/32 any eq snmp 
  190 permit udp 10.71.24.18/32 any eq snmp 
  200 permit udp 10.71.24.19/32 any eq snmp 
  210 permit udp 10.71.24.20/32 any eq snmp 
  220 permit udp 10.71.24.21/32 any eq snmp 
  230 permit udp 10.71.24.22/32 any eq snmp 
  240 permit udp 10.71.24.23/32 any eq snmp 
  20 permit udp 155.98.253.0/24 any eq snmp 
  30 permit udp 10.71.24.10/32 any eq snmp 
  40 permit udp 10.71.24.11/32 any eq snmp 
  50 permit udp 10.71.24.12/32 any eq snmp 
  60 permit udp 10.71.24.13/32 any eq snmp 
  70 permit udp 10.71.24.14/32 any eq snmp 
  80 permit udp 10.71.24.15/32 any eq snmp 
  90 permit udp 10.71.24.16/32 any eq snmp 
  100 permit udp 10.71.24.17/32 any eq snmp 
  110 permit udp 10.71.24.18/32 any eq snmp 
  120 permit udp 10.71.24.19/32 any eq snmp 
  130 permit udp 10.71.24.20/32 any eq snmp 
  140 permit udp 10.71.24.21/32 any eq snmp 
  150 permit udp 10.71.24.22/32 any eq snmp 
  160 permit udp 10.71.24.23/32 any eq snmp 
snmp-server contact TAG:305156-BarCode:503203
snmp-server location West Temple DC Row a4
snmp-server globalEnforcePriv
snmp-server user admin network-admin auth md5 0xa42b896412551126921a6581c604347c priv 0xa42b896412551126921a6581c604347c
 localizedkey
snmp-server community 99U#u#U!x group network-operator
snmp-server community 1xR$bluE group network-operator
snmp-server community 99U#u#U!x use-acl NOC_SNMP_RO_POLICY
snmp-server community 1xR$bluE use-acl MonitorTeam_SNMP_RO_POLICY""",
 'show run | in snmp':"""20 permit udp 155.100.122.25/32 any eq snmp 
  30 permit udp 155.100.122.28/32 any eq snmp 
  40 permit udp 155.100.122.50/32 any eq snmp 
  50 permit udp 155.100.122.200/32 any eq snmp 
  30 permit udp 155.98.253.0/24 any eq snmp 
  50 permit udp 155.100.122.113/32 any eq snmp 
  70 permit udp 155.100.240.123/32 any eq snmp 
  100 permit udp 155.101.168.124/32 any eq snmp 
  110 permit udp 10.71.24.10/32 any eq snmp 
  120 permit udp 10.71.24.11/32 any eq snmp 
  130 permit udp 10.71.24.12/32 any eq snmp 
  140 permit udp 10.71.24.13/32 any eq snmp 
  150 permit udp 10.71.24.14/32 any eq snmp 
  160 permit udp 10.71.24.15/32 any eq snmp 
  170 permit udp 10.71.24.16/32 any eq snmp 
  180 permit udp 10.71.24.17/32 any eq snmp 
  190 permit udp 10.71.24.18/32 any eq snmp 
  200 permit udp 10.71.24.19/32 any eq snmp 
  210 permit udp 10.71.24.20/32 any eq snmp 
  220 permit udp 10.71.24.21/32 any eq snmp 
  230 permit udp 10.71.24.22/32 any eq snmp 
  240 permit udp 10.71.24.23/32 any eq snmp 
  20 permit udp 155.98.253.0/24 any eq snmp 
  30 permit udp 10.71.24.10/32 any eq snmp 
  40 permit udp 10.71.24.11/32 any eq snmp 
  50 permit udp 10.71.24.12/32 any eq snmp 
  60 permit udp 10.71.24.13/32 any eq snmp 
  70 permit udp 10.71.24.14/32 any eq snmp 
  80 permit udp 10.71.24.15/32 any eq snmp 
  90 permit udp 10.71.24.16/32 any eq snmp 
  100 permit udp 10.71.24.17/32 any eq snmp 
  110 permit udp 10.71.24.18/32 any eq snmp 
  120 permit udp 10.71.24.19/32 any eq snmp 
  130 permit udp 10.71.24.20/32 any eq snmp 
  140 permit udp 10.71.24.21/32 any eq snmp 
  150 permit udp 10.71.24.22/32 any eq snmp 
  160 permit udp 10.71.24.23/32 any eq snmp 
snmp-server contact TAG:305156-BarCode:503203
snmp-server location West Temple DC Row a4
snmp-server globalEnforcePriv
snmp-server user admin network-admin auth md5 0xa42b896412551126921a6581c604347c priv 0xa42b896412551126921a6581c604347c
 localizedkey
snmp-server community 99U#u#U!x group network-operator
snmp-server community 1xR$bluE group network-operator
snmp-server community 99U#u#U!x use-acl NOC_SNMP_RO_POLICY
snmp-server community 1xR$bluE use-acl MonitorTeam_SNMP_RO_POLICY""",
 'show snmp user':"""______________________________________________________________
                  SNMP USERS [global privacy flag enabled]
______________________________________________________________

User                          Auth  Priv(enforce) Groups                        
____                          ____  _____________ ______                        
admin                         md5   des(yes)      network-admin                 

____________________________ __________________________________
 NOTIFICATION TARGET USERS (configured  for sending V3 Inform) 
___________________________ ___________________________________

User                          Auth  Priv 
____                          ____  ____ """,
 'show access-list':"""IP access list 199
IP access list MonitorTeam_SNMP_RO_POLICY
        10 remark Monitor Team SNMP Read Only ACL
        20 permit udp 155.100.122.25/32 any eq snmp 
        30 permit udp 155.100.122.28/32 any eq snmp 
        40 permit udp 155.100.122.50/32 any eq snmp 
        50 permit udp 155.100.122.200/32 any eq snmp 
IP access list NOC_MGMT_OUT
IP access list NOC_SNMP_RO_POLICY
        10 remark Netops SNMP Read Only ACL
        20 remark NOC MGMT NEt
        30 permit udp 155.98.253.0/24 any eq snmp 
        40 remark INMON Tool
        50 permit udp 155.100.122.113/32 any eq snmp 
        60 remark Neebula Tool Test
        70 permit udp 155.100.240.123/32 any eq snmp 
        100 permit udp 155.101.168.124/32 any eq snmp 
        110 permit udp 10.71.24.10/32 any eq snmp 
        120 permit udp 10.71.24.11/32 any eq snmp 
        130 permit udp 10.71.24.12/32 any eq snmp 
        140 permit udp 10.71.24.13/32 any eq snmp 
        150 permit udp 10.71.24.14/32 any eq snmp 
        160 permit udp 10.71.24.15/32 any eq snmp 
        170 permit udp 10.71.24.16/32 any eq snmp 
        180 permit udp 10.71.24.17/32 any eq snmp 
        190 permit udp 10.71.24.18/32 any eq snmp 
        200 permit udp 10.71.24.19/32 any eq snmp 
        210 permit udp 10.71.24.20/32 any eq snmp 
        220 permit udp 10.71.24.21/32 any eq snmp 
        230 permit udp 10.71.24.22/32 any eq snmp 
        240 permit udp 10.71.24.23/32 any eq snmp 
IP access list NOC_SNMP_RW_POLICY
        10 remark NOC MGMT NET
        20 permit udp 155.98.253.0/24 any eq snmp 
        30 permit udp 10.71.24.10/32 any eq snmp 
        40 permit udp 10.71.24.11/32 any eq snmp 
        50 permit udp 10.71.24.12/32 any eq snmp 
        60 permit udp 10.71.24.13/32 any eq snmp 
        70 permit udp 10.71.24.14/32 any eq snmp 
        80 permit udp 10.71.24.15/32 any eq snmp 
        90 permit udp 10.71.24.16/32 any eq snmp 
        100 permit udp 10.71.24.17/32 any eq snmp 
        110 permit udp 10.71.24.18/32 any eq snmp 
        120 permit udp 10.71.24.19/32 any eq snmp 
        130 permit udp 10.71.24.20/32 any eq snmp 
        140 permit udp 10.71.24.21/32 any eq snmp 
        150 permit udp 10.71.24.22/32 any eq snmp 
        160 permit udp 10.71.24.23/32 any eq snmp 
IP access list SSH_POLICY
        10 permit tcp 155.98.253.0/24 any eq 22 
        15 permit tcp 155.99.254.128/25 any eq 22 
        20 remark VPN Networks
        30 permit tcp 155.101.243.0/27 any eq 22 
        31 permit tcp 155.98.164.192/27 any eq 22 
        40 deny tcp 155.100.37.16/32 any eq 22 
        50 deny tcp 155.100.37.31/32 any eq 22 
        60 permit tcp 155.100.37.16/28 any eq 22 
        70 remark Door1 & Door2
        80 permit tcp 155.99.239.130/32 any eq 22 
        90 permit tcp 155.97.152.244/32 any eq 22 
IP access list copp-system-p-acl-auto-rp
        10 permit ip any 224.0.1.39/32 
        20 permit ip any 224.0.1.40/32 
IP access list copp-system-p-acl-bgp
        10 permit tcp any gt 1024 any eq bgp 
        20 permit tcp any eq bgp any gt 1024 
IPv6 access list copp-system-p-acl-bgp6
        10 permit tcp any gt 1024 any eq bgp 
        20 permit tcp any eq bgp any gt 1024 
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
IP access list copp-system-p-acl-icmp
        10 permit icmp any any echo 
        20 permit icmp any any echo-reply 
IPv6 access list copp-system-p-acl-icmp6
        10 permit icmp any any echo-request 
        20 permit icmp any any echo-reply 
IPv6 access list copp-system-p-acl-icmp6-msgs
        10 permit icmp any any router-advertisement 
        20 permit icmp any any router-solicitation 
        30 permit icmp any any nd-na 
        40 permit icmp any any nd-ns 
        50 permit icmp any any mld-query 
        60 permit icmp any any mld-report 
        70 permit icmp any any mld-reduction 
        80 permit icmp any any mldv2 
IP access list copp-system-p-acl-igmp
        10 permit igmp any 224.0.0.0/3 
MAC access list copp-system-p-acl-mac-cdp-udld-vtp
        10 permit any 0100.0ccc.cccc 0000.0000.0000 
MAC access list copp-system-p-acl-mac-cfsoe
        10 permit any 0180.c200.000e 0000.0000.0000 0x8843 
        20 permit any 0180.c200.000e 0000.0000.0000 
MAC access list copp-system-p-acl-mac-dot1x
        10 permit any 0180.c200.0003 0000.0000.0000 0x888e 
MAC access list copp-system-p-acl-mac-l2-tunnel
        10 permit any any 0x8840 
MAC access list copp-system-p-acl-mac-l3-isis
        10 permit any 0180.c200.0015 0000.0000.0000 
        20 permit any 0180.c200.0014 0000.0000.0000 
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
IP access list copp-system-p-acl-msdp
        10 permit tcp any gt 1024 any eq 639 
        20 permit tcp any eq 639 any gt 1024 
IP access list copp-system-p-acl-ntp
        10 permit udp any any eq ntp 
        20 permit udp any eq ntp any 
IPv6 access list copp-system-p-acl-ntp6
        10 permit udp any any eq ntp 
        20 permit udp any eq ntp any 
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
 'show run | section logging':"""logging server 155.98.204.52 6 use-vrf management facility local6
logging server 155.98.253.244 6 use-vrf management facility local6
logging console 0""",
 'show run | in logging':"""logging server 155.98.204.52 6 use-vrf management facility local6
logging server 155.98.253.244 6 use-vrf management facility local6
logging console 0""",
 'show mac address-table':"""Legend: 
        * - primary entry, G - Gateway MAC, (R) - Routed MAC, O - Overlay MAC
        age - seconds since last seen,+ - primary entry using vPC Peer-Link,
        (T) - True, (F) - False
   VLAN     MAC Address      Type      age     Secure NTFY Ports
---------+-----------------+--------+---------+------+----+------------------
*  520     0002.c94d.6ada   dynamic  0         F      F    Po31
*  520     0002.c94f.a10c   dynamic  0         F      F    Po31
*  520     0002.c953.0088   dynamic  0         F      F    Po31
*  520     0002.c953.0740   dynamic  0         F      F    Po31
*  520     0002.c957.14ca   dynamic  0         F      F    Po31
*  520     001b.21ab.33e8   dynamic  0         F      F    Po31
*  520     0022.bdf8.19ff   dynamic  0         F      F    Po31
*  520     0024.36f4.d22c   dynamic  0         F      F    Po31
*  520     0050.566a.f8b5   dynamic  0         F      F    Eth1/10/1
*  520     0050.566f.337f   dynamic  0         F      F    Po31
*  520     0050.5692.04db   dynamic  0         F      F    Po31
*  520     0050.5692.0bf7   dynamic  0         F      F    Po31
*  520     0050.5692.0d00   dynamic  0         F      F    Po31
*  520     0050.5692.0d7c   dynamic  0         F      F    Po31
*  520     0050.5692.0ec9   dynamic  0         F      F    Po31
*  520     0050.5692.1408   dynamic  0         F      F    Po31
*  520     0050.5692.1621   dynamic  0         F      F    Po31
*  520     0050.5692.1b7f   dynamic  0         F      F    Po31
*  520     0050.5692.1cd4   dynamic  0         F      F    Po31
*  520     0050.5692.22b8   dynamic  0         F      F    Po31
*  520     0050.5692.257b   dynamic  0         F      F    Po31
*  520     0050.5692.2aec   dynamic  0         F      F    Po31
*  520     0050.5692.2e18   dynamic  0         F      F    Po31
*  520     0050.5692.2e6f   dynamic  0         F      F    Po31
*  520     0050.5692.34a1   dynamic  0         F      F    Po31
*  520     0050.5692.3858   dynamic  0         F      F    Po31
*  520     0050.5692.39b9   dynamic  0         F      F    Po31
*  520     0050.5692.3fae   dynamic  0         F      F    Po31
*  520     0050.5692.4256   dynamic  0         F      F    Po31
*  520     0050.5692.42bb   dynamic  0         F      F    Po31
*  520     0050.5692.456e   dynamic  0         F      F    Po31
*  520     0050.5692.46d7   dynamic  0         F      F    Po31
*  520     0050.5692.4753   dynamic  0         F      F    Po31
*  520     0050.5692.4b32   dynamic  0         F      F    Po31
*  520     0050.5692.4be0   dynamic  0         F      F    Po31
*  520     0050.5692.50e2   dynamic  0         F      F    Po31
*  520     0050.5692.5120   dynamic  0         F      F    Po31
*  520     0050.5692.543a   dynamic  0         F      F    Po31
*  520     0050.5692.5818   dynamic  0         F      F    Po31
*  520     0050.5692.5a17   dynamic  0         F      F    Po31
*  520     0050.5692.5d81   dynamic  0         F      F    Po31
*  520     0050.5692.5fdd   dynamic  0         F      F    Po31
*  520     0050.5692.6126   dynamic  0         F      F    Po31
*  520     0050.5692.61ce   dynamic  0         F      F    Po31
*  520     0050.5692.685b   dynamic  0         F      F    Po31
*  520     0050.5692.6de1   dynamic  0         F      F    Po31
*  520     0050.5692.6e38   dynamic  0         F      F    Po31
*  520     0050.5692.7389   dynamic  0         F      F    Po31
*  520     0050.5692.7f4c   dynamic  0         F      F    Po31
*  520     0050.5692.7f67   dynamic  0         F      F    Po31
*  520     0050.56b7.00d2   dynamic  0         F      F    Po31
*  520     0050.56b7.031f   dynamic  0         F      F    Po31
*  520     0050.56b7.04d0   dynamic  0         F      F    Po31
*  520     0050.56b7.04fb   dynamic  0         F      F    Po31
*  520     0050.56b7.070c   dynamic  0         F      F    Po31
*  520     0050.56b7.074c   dynamic  0         F      F    Po31
*  520     0050.56b7.0aff   dynamic  0         F      F    Po31
*  520     0050.56b7.0c92   dynamic  0         F      F    Po31
*  520     0050.56b7.0d69   dynamic  0         F      F    Po31
*  520     0050.56b7.0f4a   dynamic  0         F      F    Po31
*  520     0050.56b7.1094   dynamic  0         F      F    Eth1/10/2
*  520     0050.56b7.13fd   dynamic  0         F      F    Po31
*  520     0050.56b7.15a0   dynamic  0         F      F    Po31
*  520     0050.56b7.17c5   dynamic  0         F      F    Po31
*  520     0050.56b7.183a   dynamic  0         F      F    Po31
*  520     0050.56b7.218f   dynamic  0         F      F    Po31
*  520     0050.56b7.22e4   dynamic  0         F      F    Po31
*  520     0050.56b7.25ed   dynamic  0         F      F    Po31
*  520     0050.56b7.29b7   dynamic  0         F      F    Po31
*  520     0050.56b7.2b40   dynamic  0         F      F    Po31
*  520     0050.56b7.2dfb   dynamic  0         F      F    Po31
*  520     0050.56b7.2f83   dynamic  0         F      F    Po31
*  520     0050.56b7.38be   dynamic  0         F      F    Po31
*  520     0050.56b7.38e5   dynamic  0         F      F    Po31
*  520     0050.56b7.3a1e   dynamic  0         F      F    Po31
*  520     0050.56b7.3d95   dynamic  0         F      F    Po31
*  520     0050.56b7.3ec2   dynamic  0         F      F    Po31
*  520     0050.56b7.45f6   dynamic  0         F      F    Po31
*  520     0050.56b7.46a0   dynamic  0         F      F    Po31
*  520     0050.56b7.46b9   dynamic  0         F      F    Po31
*  520     0050.56b7.4bd7   dynamic  0         F      F    Po31
*  520     0050.56b7.50c7   dynamic  0         F      F    Po31
*  520     0050.56b7.57db   dynamic  0         F      F    Po31
*  520     0050.56b7.5a7f   dynamic  0         F      F    Po31
*  520     0050.56b7.5ba2   dynamic  0         F      F    Po31
*  520     0050.56b7.5d4d   dynamic  0         F      F    Po31
*  520     0050.56b7.61af   dynamic  0         F      F    Po31
*  520     0050.56b7.66e6   dynamic  0         F      F    Po31
*  520     0050.56b7.69be   dynamic  0         F      F    Po31
*  520     0050.56b7.6ce0   dynamic  0         F      F    Po31
*  520     0050.56b7.7064   dynamic  0         F      F    Po31
*  520     0050.56b7.762c   dynamic  0         F      F    Po31
*  520     0050.56b7.76fb   dynamic  0         F      F    Po31
*  520     0050.56b7.7aff   dynamic  0         F      F    Po31
*  520     0050.56b7.7be1   dynamic  0         F      F    Po31
*  520     0050.56b7.7e09   dynamic  0         F      F    Po31
*  520     0050.56b7.7f4c   dynamic  0         F      F    Po31
*  520     00e0.ed95.2146   dynamic  0         F      F    Eth1/20/3
*  520     00e0.ed95.2147   dynamic  0         F      F    Eth1/20/4
*  520     00e0.ed95.7668   dynamic  0         F      F    Po31
*  520     00e0.ed95.7669   dynamic  0         F      F    Po31
*  520     0cc4.7a50.aa34   dynamic  0         F      F    Po31
*  520     0cc4.7a5a.1dd0   dynamic  0         F      F    Po31
*  520     4cd9.8f9c.5430   dynamic  0         F      F    Po31
*  520     782b.cb2a.1084   dynamic  0         F      F    Po31
*  520     9803.9bb0.6b72   dynamic  0         F      F    Po31
*  520     a4bf.0144.a843   dynamic  0         F      F    Po31
*  520     a820.6600.ef01   dynamic  0         F      F    Po31
*  520     ac1f.6b3a.7db4   dynamic  0         F      F    Po31
*  520     ac1f.6bb1.1f5e   dynamic  0         F      F    Po31
*  520     d4e8.8047.7c8d   dynamic  0         F      F    Po31
*  520     d4e8.8047.9b55   dynamic  0         F      F    Po31
*  520     d4e8.80a5.fde7   dynamic  0         F      F    Eth1/2
*  520     d4e8.80a6.4fa7   dynamic  0         F      F    Eth1/1
*  520     e41d.2d17.4450   dynamic  0         F      F    Eth1/12
*  520     e41d.2d17.5960   dynamic  0         F      F    Eth1/13
*  520     e41d.2d17.5b00   dynamic  0         F      F    Eth1/11
*  520     e41d.2d28.d151   dynamic  0         F      F    Po31
*  520     e41d.2d74.45d0   dynamic  0         F      F    Eth1/14
*  520     e41d.2db5.bfa0   dynamic  0         F      F    Eth1/17
*  520     e443.4b60.5954   dynamic  0         F      F    Eth1/10/4
* 3520     0050.5661.88dc   dynamic  0         F      F    Eth1/10/2
* 3520     0050.566d.1d78   dynamic  0         F      F    Eth1/10/1
G    -     ecbd.1dea.5bdf   static   -         F      F    sup-eth1(R)""",
 'show run | section tacacs':"""feature tacacs+
tacacs-server key 7 "L$iN$eW@tb!"
tacacs-server host 172.31.17.180 
tacacs-server host 10.64.32.5 
aaa group server tacacs+ TacServer 
    server 172.31.17.180 
    server 10.64.32.5 
    use-vrf management""",
 'show run | in tacacs':"""feature tacacs+
tacacs-server key 7 "L$iN$eW@tb!"
tacacs-server host 172.31.17.180 
tacacs-server host 10.64.32.5 
aaa group server tacacs+ TacServer """,
 'show power inline':"""^
% Invalid command at '^' marker.""",
 'show environment all':"""^
% Invalid command at '^' marker.""",
}
