# OSNC - Open Source Network Controller
**Intent:**
This code Library is a WIP (work in progress) library intended to be consumed by python developers for Networking applications. The library is intended to provide a universal framework,
and dataclass structure for different network equipment from different vendors. This library should serve as the centeral application to control most network applications.

Intergation with Hardware and software:
Most Cisco Catalyst switches
Some Cisco routers
Some Cisco NX-OS switches
Infoblox
Palo Alto Next Gen Firewalls
Palo Alto Panorama

This application can be called as a library from other python libraries, or it can be ran as a standalone web application with GUI. Below is the instructions for Web application:

**Web Application Install:**
```
docker pull python:3.8-slim-bullseye
docker build -t osnc:latest .
docker run osnc:latest -p 8080:8080 -v $(pwd):/opt/OSNC
```

**Python Application:**

- `from Network.L2.Switch import Stack`
- `from Network.L2.Vlan import vlan`
- `from Network.L1.Port import Interface`


An example of the starting entry point for switches would look like: 
```
from Network.L2.Switch import Stack

s = Stack(<ipaddress>)
s.login()
s.getswitchinfo() #SSH into switch, 
s.assignattibutes() #run all get commands and makes Python objects

from Network.L3.Router import Router
r = Router('<ipaddress>')
r.get_started() #SSH into router, run all get commands and makes Python objects
```

