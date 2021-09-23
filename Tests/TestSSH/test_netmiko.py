from unittest import TestCase
from SSH.NetmikoConnection import connection
from openpyxl import load_workbook

class Testconnection(TestCase):
    def test_simple_connection(self):
        conn = connection('172.31.132.4',"cisco_ios").connnect()
        print(conn.find_prompt())
        pass


