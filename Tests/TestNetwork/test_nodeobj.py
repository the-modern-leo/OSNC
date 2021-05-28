import unittest

from Network.Network import Node

class TestCommandResults(unittest.TestCase):
    def test_node_get_downstream(self):
        nodes = {}

        for key, item in nodes.items():
            n = Node(r1_ipaddress=item['r1'], r2_ipaddress=['r2'])
            n.get_all_downstream()
            n.check_egde_acl()