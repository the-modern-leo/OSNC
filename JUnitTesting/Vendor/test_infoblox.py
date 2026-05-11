import unittest
from vendors.infoblox import DNS

class TestRouter(unittest.TestCase):

    def test_login(self):
        rest = DNS()
        rest.get_Network_containers_all(netadd="10.0.0.0/8")

    def test_get_network_contrainer(self):
        rest = DNS()
        result = rest.get_Network_container(netadd="10.24.4.0/22")
        print(result)

    def test_createNetwork(self):
        data = []
        for networks in data:
            rest = DNS()
            result = rest.createNetwork(networks)
            print(result)

    def test_createContainer(self):
        datalist = []
        for data in datalist:
            rest = DNS()
            result = rest.createContainer(data)

    def test_create_networks(self,data,network):
        data = []
        rest = DNS()
        rest.create_multiple_networks("10.70.0.0/16",data)

    def test_create_host_record(self):
        r = DNS()
        records =  [
 ]
        for tvm in records:
            comment = ""
            r.create_host_record(tvm[1],tvm[0])

    def test_find_a_record(self):
        r = DNS()
        r.find_a_record(ipv4addr="10.23.0.4")

    def test_create_host_record(self):
        hostrecords = [
 ]
        r = DNS()
        for recods in hostrecords:
            r.create_host_record(recods[1],recods[0],dns_view="default")