# OSNC - Open Source Network Controller
**Intent:**
This code Library is a WIP (work in progress) library intended to be consumed by developers working on python Networking applications. The library is intended to provide a universal framework for developing integrated APIs with network equipment, and applications. This Library can be imported, and called directly from other applications or it can be run as a standalone web application with a GUI.

The following is supported:
Palo Alto Next Gen Firewalls, and Panorama
Most commands for Cisco L2/L3 switches
Most commands for Cisco Nexus switches
Some Cisco routers
Infoblox 
  -DHCP
  -DNS
  -IPAM
  -Grid

**Install:**
```
docker pull python:3.8-slim-bullseye
docker build -t osnc:latest .
docker run osnc:latest -p 8080:8080 -v $(pwd):/opt/OSNC
```

Intended Consumable Packages are located under the Network Package:

- `from Network.L2.Switch import Stack`
- `from Network.L2.Vlan import vlan`
- `from Network.L1.Port import Interface`


An example of the starting entry point would look like: 
```
from Network.Switch import Stack

s = Stack(<ipaddress>)
s.login()
s.getswitchinfo()
s.assignattibutes()
```

This Will log into the switch and run the following commands:
- `show run`
- `show version`
- `show int status`
- `show run | section interface`
- `show run | in interface`
- `show interface`
- `show inventory`
- `show interface counters`
- `show cdp nei detail`
- `show module all`
- `show module`
- `show run | section snmp`
- `show snmp user`
- `show access-list`
- `show run | section logging`
- `show run | in logging`
- `show mac address-table`
- `show run | section tacacs`
- `show power inline`
- `show environment all`

Using the data from those commands the script than populates the Stack object's properties with the data from the commands
