# OSNC - Open Source Network Controller
**Intent:**
This code Library is a WIP (work in progress) library intended to be consumed by other developers working on 
by other python developers working on Networking applications. The library is intended to provide a universal framework,
and dataclass structure for developing applications in real time by scraping data using SSH. 
The 

Application is currently working on being deployed on a single server directly from the server at the moment. 
Support is only on Mac, Linux. 
Future improvements will be running the service as a single docker container for support on all platforms. 
Possible improvements will also see the application 

**Install:**
`pip install onsc`

Intended Consumable Packages are located under the Network Package:

`from Network.L2.Switch import Stack`
`from Network.L2.Vlan import vlan`
`from Network.L1.Port import Interface`


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
