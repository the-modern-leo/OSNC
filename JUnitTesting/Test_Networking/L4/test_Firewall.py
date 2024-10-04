import unittest
from Network.L4.firewall import PaloAlto,adddressobj,GroupObj

class TestRouter(unittest.TestCase):
    def test_CreateAddressObj(self):
        addr = adddressobj("addr_10.5.0.1","10.5.0.1/32",True)
        result = addr.Create()
        with PaloAlto(ip="10.7.17.132",pano=True) as p:
            p.SendConfigCommands(result)

        pass

    def test_CreateGroupObj(self):
        group = GroupObj("test",True)
        result = group.Create()
        with PaloAlto(ip="10.7.17.132",pano=True) as p:
            p.SendConfigCommands(result)
        pass

    def test_AssocateAddressToGroupObj(self):
        group = GroupObj("test",True)
        result = group.AddAddressObj("addr_10.5.0.1")
        with PaloAlto(ip="10.7.17.132",pano=True) as p:
            p.SendConfigCommands(result)
        pass

    def test_DeleteAddressObj(self):
        group = GroupObj("test",True)
        result = group.Delete()
        with PaloAlto(ip="10.7.17.132",pano=True) as p:
            p.SendConfigCommands(result)
        pass
