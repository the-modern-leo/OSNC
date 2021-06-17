from unittest import TestCase
from SSH import NetmikoConnection


class Testconnection(TestCase):
    def test_simple_connection(self):
        conn = NetmikoConnection.connnect('172.31.132.4',"cisco_ios")
        print(conn.find_prompt())
