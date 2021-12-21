### Local Imports ###
from Network.Routing import Router

#testing Frameworks
import unittest

### Test Imports ###


### global imports ###



class TestRouterObject(unittest.TestCase):
    """
    This is for Testing compatibility of router objects across multiple platforms
    """
    def test_Catalyst_C9606R(self):
        iplist = []
        for ip in iplist:
            r = Router(ip)
            r.login()
            r.getSwitchInfo()
            r.assignattributes()

            for vlan in r.vlansints:
                public_subnet = []
                private_subnet = []
                for subnet in vlan.subnets:
                    if '155.' in subnet.with_prefixlen:
                        public_subnet.append(subnet.with_prefixlen)
                    if '172.' in subnet.with_prefixlen:
                        private_subnet.append(subnet.with_prefixlen)
                print(f"{vlan.number},{'-'.join(public_subnet)},{'-'.join(private_subnet)},Park")


