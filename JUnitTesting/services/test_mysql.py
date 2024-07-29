import unittest
from Services.SQL.Mysql import DB
class TestDB(unittest.TestCase):

    def test_createDB(self):
        with DB() as conn:
            conn.create_database("Networkdb")
        pass

    def test_connection(self):
        with DB() as conn:
            conn.create_table("Networkdb")
        pass

    def test_UpdateData(self):
        with DB() as conn:
            conn.UpdateData("Networkdb","Routers")
        pass
