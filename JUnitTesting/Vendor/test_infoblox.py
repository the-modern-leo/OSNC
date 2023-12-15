import unittest
from vendors.infoblox import restapi

class TestRouter(unittest.TestCase):

    def test_login(self):
        rest = restapi()
        rest.get_Network_containers_all(netadd="10.0.0.0/8")
    def test_get_network_contrainer(self):
        rest = restapi()
        rest.get_Network_container(netadd="10.24.4.0/22")
    def test_create_multiple_networks(self):
        data = [
            {"location": "FW-Untrust", "size": 29, "router": "FLHQBCI9600 / MB3BCI9600", "vlan": "1220"},
            {"location": "FW-Trust", "size": 29, "router": "FLHQBCI9600 / MB3BCI9600", "vlan": "1221"},
            {"location": "Mt. Ogden Addition", "size": 28, "router": "OG1ACI3850", "vlan": "1222"},
            {"location": "Mt. Timp.", "size": 27, "router": "ProvoTIC-CI3850", "vlan": "1223"},
            {"location": "OGX", "size": 27, "router": "	MB3-B-OGX-BRT-CI9300 / OGD-BRT-CI9300", "vlan": "1224"},
            {"location": "Intermodal", "size": 28, "router": "CustFirstCI3850-12", "vlan": "1225"},
            {"location": "FLHQ", "size": 28, "router": "FLHQ3850", "vlan": "1226"},
            {"location": "Jordan River", "size": 28, "router": "JRSCACI3850X", "vlan": "1227"},
            {"location": "DDTC", "size": 27, "router": "DDTC3ACI9300", "vlan": "1228"},
            {"location": "TRAX N", "size": 27, "router": "BilboFLHQ", "vlan": "1229"},
            {"location": "CRN", "size": 27, "router": "BilboFLHQ", "vlan": "1230"},
            {"location": "Murray Police", "size": 28, "router": "UPDASA2110", "vlan": "1231"},
            {"location": "Ogden Transit Center", "size": 28, "router": "OGTC-B-CI3850", "vlan": "1232"},
            {"location": "TRAX S", "size": 27, "router": "FrodoMB3", "vlan": "1233"},
            {"location": "UVX", "size": 26, "router": "UVX-Samwise-CI3850.", "vlan": "1234"},
            {"location": "CRS", "size": 27, "router": "BilboFLHQ", "vlan": "1235"},
            {"location": "Mbk 1", "size": 28, "router": "MB1ACI3850-Distro", "vlan": "1236"},
            {"location": "Mbk 3", "size": 28, "router": "MB3BCI3850", "vlan": "1237"},
            {"location": "Mbk 7", "size": 28, "router": "MB7CI3850-12", "vlan": "1238"},
            {"location": "Mbk 8", "size": 28, "router": "MB8C-CI3850-12", "vlan": "1239"},
            {"location": "Riverside", "size": 28, "router": "RS1A-C3850-12", "vlan": "1240"}
        ]
        rest = restapi()
        rest.create_multiple_networks("10.24.4.0/22",data)