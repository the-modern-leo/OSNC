import unittest
from Network.L4.firewall import PaloAlto,adddressobj,GroupObj,Interface

class TestRouter(unittest.TestCase):
    def test_CreateAddressObj(self):
        addr = adddressobj("addr_10.5.0.1","10.5.0.1/32",True)
        result = addr.Create()
        with PaloAlto(ip="10.2.2.2",pano=True) as p:
            p.SendConfigCommands(result)

        pass

    def test_CreateGroupObj(self):
        group = GroupObj("Test",True)
        result = group.Create()
        with PaloAlto(ip="10.2.2.2",pano=True) as p:
            p.SendConfigCommands(result)
        pass

    def test_CreateBatchAddressObj(self):
        for x in range(200,231):
            addr = adddressobj(f"addr_10.2.7.{str(x)}", f"10.2.7.{str(x)}/32", True)
            result = addr.Create()
            with PaloAlto(ip="10.2.2.2", pano=True) as p:
                p.SendConfigCommands(result)
    def test_batchAssocateAddressToGroupObj(self):
        results = []
        for x in range(200,231):
            group = GroupObj("Test", True)
            results.append(group.AddAddressObj(f"addr_10.2.7.{str(x)}")[0])
        with PaloAlto(ip="10.2.2.2", pano=True) as p:
            p.SendConfigCommands(results)
    def test_AssocateAddressToGroupObj(self):
        group = GroupObj("test",True)
        result = group.AddAddressObj("addr_10.5.0.1")
        with PaloAlto(ip="10.2.2.2",pano=True) as p:
            p.SendConfigCommands(result)
        pass

    def test_DeleteAddressObj(self):
        group = GroupObj("test",True)
        result = group.Delete()
        with PaloAlto(ip="10.2.2.2",pano=True) as p:
            p.SendConfigCommands(result)
        pass

    def test_CreateL3SubInterfaceOnAgg(self):
        listOfInterfaces = [
{"IPAddress":"10.72.0.0/24","Vlan":"2656","Location":"TEST1","Router":"FW-test"},
{"IPAddress":"10.72.1.0/24","Vlan":"2706","Location":"TEST1","Router":"FW-test"},
{"IPAddress":"10.72.2.0/24","Vlan":"2756","Location":"TEST1","Router":"FW-test"},
{"IPAddress":"10.72.3.0/24","Vlan":"2806","Location":"TEST1","Router":"FW-test"},
{"IPAddress":"10.72.4.0/24","Vlan":"2856","Location":"TEST1","Router":"FW-test"},
{"IPAddress":"10.72.5.0/24","Vlan":"2906","Location":"TEST1","Router":"FW-test"},
{"IPAddress":"10.72.6.0/24","Vlan":"2956","Location":"TEST1","Router":"FW-test"},
{"IPAddress":"10.72.7.0/24","Vlan":"3006","Location":"TEST1","Router":"FW-test"},
{"IPAddress":"10.72.8.0/24","Vlan":"3056","Location":"TEST1","Router":"FW-test"},
{"IPAddress":"10.72.9.0/24","Vlan":"3106","Location":"TEST1","Router":"FW-test"},
{"IPAddress":"10.72.10.0/24","Vlan":"3156","Location":"TEST1","Router":"FW-test"},
{"IPAddress":"10.72.11.0/24","Vlan":"3206","Location":"TEST1","Router":"FW-test"},
]
        with PaloAlto(ip="10.2.2.2", pano=True,) as p:
            for inter in listOfInterfaces:
                I = Interface("ae2",True,template="FW-test",interfacenumber=inter["Vlan"])
                test = I.Create(inter["IPAddress"],tag="Network",comment=f"{inter['Location']}-Network",VRtoAddTo="Test",AddtoSZ=True,Vsys="vsys1",zone="Network")
                result = p.SendConfigCommands(test)
                pass

    def test_DeleteL3SubInterfaceOnAgg(self):
        listOfInterfaces = [
            "2656",
            "2706",
            "2756",
            "2806",
            "2856",
            "2906",
            "2956",
            "3006",
            "3056",
            "3106",
        ]
        with PaloAlto(ip="10.2.2.2", pano=True) as p:
            for inter in listOfInterfaces:
                I = Interface("ae2", True, template="FW-test", interfacenumber=inter)
                p.SendConfigCommands(I.Delete())
                pass
