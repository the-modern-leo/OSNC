import unittest
from Network.L2.Switch import Stack
import re
from netaddr import mac_cisco


class TestStack(unittest.TestCase):

    def test_stack(self):
        s = Stack("10.45.150.129")
        s.login()
        s.conn.enable_cisco()
        s.getSwitchInfo()
        s.assignattributes()
