import unittest
from vendors.infoblox import restapi

class TestRouter(unittest.TestCase):

    def test_login(self):
        rest = restapi()
        rest.get_Network_containers_all(netadd="10.0.0.0/8")
    def test_get_network_contrainer(self):
        rest = restapi()
        result = rest.get_Network_container(netadd="10.23.16.0/20")
        print(result)

    def test_createNetwork(self):
        data = []
        for networks in data:
            rest = restapi()
            result = rest.createNetwork(networks)
            print(result)
    def test_createContainer(self):
        datalist = []
        for data in datalist:
            rest = restapi()
            result = rest.createContainer(data)

    def test_create_networks(self,data,network):
        data = []
        rest = restapi()
        rest.create_multiple_networks("10.70.0.0/16",data)

    def test_create_host_record(self):
        r = restapi()
        records = []
        for tvm in records:
            comment = ""
            r.create_host_record(tvm[2],tvm[0] + "",comment=comment,nextavailable=None,ipad=tvm[1])

    def test_get_host_record(self):
        r = restapi()
        r.get_host_record("10.23.0.4")

    def test_sort(self):
        List_1 = []
        List_2 = []
        try:
            for item in List_1:
                for item_2 in List_2:
                    if item[3].lower() == item_2[1].lower():
                        print(f"{item_2[0]},{item_2[1]},{item_2[2]},{item_2[3]},{item_2[4]},{item_2[5]},{item[6]},,{item[9]},{item[7]},{item_2[9]}")
                        break
                    elif item[3].lower() != item_2[1].lower():
                        pass
        except Exception as e:
            print(e)
            pass