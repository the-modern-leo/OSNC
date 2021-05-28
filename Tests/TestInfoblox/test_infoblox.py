import unittest, time, auth
from Infoblox.infoblox import Infoblox
from Tests.TestInfoblox.settings import *

ib_obj = None
test_subnet = '10.64.3.0/24'
test_container = '10.0.8.0/22'

class TestInfoblox(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global ib_obj
        ib_obj = Infoblox(auth.InfobloxAPI.url,
                auth.InfobloxAPI.username, auth.InfobloxAPI.password,
                rf_obj, verify=auth.InfobloxAPI.cert)

    #@classmethod
    #def tearDownClass(cls):

    def test_add_network(self):
        return
        result = ib_obj.add_network('10.0.8.250/30')
        self.assertIsInstance(result, str)
        ib_obj._delete_obj(result)

    def test_next_avail_subnets(self):
        result = ib_obj.next_avail_subnets(test_container, '29', quantity=1)
        self.assertIsInstance(result, dict)
        for k in result['success'].keys():
            self.assertIn('10.0.8.', k)

        to_clean = ib_obj.object_query('network', '10\.0\.8\.*')
        for n in range(len(to_clean)):
            ib_obj._delete_obj(to_clean[n]['_ref'])
        to_clean = ib_obj.object_query('AllZone', '10\.0\.8\.*')
        for rz in range(len(to_clean)):
            ib_obj._delete_obj(to_clean[rz]['_ref'])

    def test_next_avail_ips(self):
        with self.assertRaises(Infoblox.InfobloxObjectError):
            ib_obj.next_avail_ips('192.168.254.250/30')
        #with self.assertRaises(Infoblox.InfobloxRoutefinderError):
        #    ib_obj.next_avail_in_network(test_subnet)
        result = ib_obj.next_avail_ips(test_subnet)
        self.assertIsInstance(result, dict)
        self.assertIn('10.64.3.', result['valid'][0])

    def test_next_avail_ips_w_range(self):
        return
        result = ib_obj.next_avail_ips(test_subnet, quantity=1,
                use_range=True)
        self.assertIsInstance(result, dict)
        self.assertIn('10.64.3.', result['valid'][0])

    def test_next_avail_ips_multi(self):
        result = ib_obj.next_avail_ips(test_subnet, quantity=3)
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result['valid']), 3)

#if __name__ == "__main__":
#    unittest.main()
