from unittest import TestCase
from SSH import NetmikoConnection
from openpyxl import load_workbook





class Testconnection(TestCase):
    def test_simple_connection(self):
        conn = NetmikoConnection.connnect('172.31.132.4',"cisco_ios")
        print(conn.find_prompt())

    def test_Switch(self):
        conn = NetmikoConnection.connnect('172.31.132.4',"cisco_ios")
        print(conn.find_prompt())

if __name__=="__main__":
    Testconnection().test_simple_connection()

