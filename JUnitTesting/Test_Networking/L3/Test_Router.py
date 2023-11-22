import unittest
from Network.L3.Router import Router


class TestRouter(unittest.TestCase):

    def test_upper(self):
        r = Router("192.168.100.201")
        r.get_started()
        self.assertEqual()
    def test_port_finder(self):
        r = router("192.168.100.202")
        r.get_started()