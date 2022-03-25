# OSNC
Open Source Network Controller

This code Library is a work in progress library intended to be consumed by other developers working on 
front end applications for Networking purposes. The library is being developed with the intended use as 
part of a Devops environment. 

Application is currently working on being deployed on a single server directly from the server at the moment. 
Support is only on Mac, Linux. 
Future improvements will be running the service as a single docker container for support on all platforms. 
Possible improvements will also see the application 

Install:
pip install onsc

Intended Consumable Packages are located under the Network Package:

from Network.L2.Switch import Stack
from Network.L2.Vlan import vlan
from Network.L1.Port import Interface
