import unittest
from Services.SQL.Mysql import DB
class TestDB(unittest.TestCase):

    def test_createDB(self):
        with DB() as conn:
            conn.create_database("Networkdb")
        pass

    def test_connection(self):
        with DB() as conn:
            conn.create_tables()
        pass

    def test_UpdateData(self):
        with DB() as conn:
            conn.UpdateData("Networkdb","Routers")
        pass

    def test_insert(self):
        SQL = "networkdevice (devicetype,hostname,ipaddress) VALUES (%s, %s, %s)"
        value = ('192.168.100.201', 'Router','ciscorouter9605')
        with DB() as conn:
            conn._insert_record(SQL,value)
        pass

    def test_delete(self):
        SQL = "networkdevice WHERE ipaddress = '192.168.100.201'"
        with DB() as conn:
            conn._delete_record(SQL)
        pass

    def test_update(self):
        SQLCreate = "networkdevice (ipaddress, devicetype,hostname) VALUES (%s, %s, %s)"
        valueCreate = ('192.168.100.201', 'Router','ciscorouter9605')
        SQL = "networkdevice SET dnsname = 'ciscorouter9605.dns' WHERE ipaddress = '192.168.100.201'"
        SQLdelete = "networkdevice WHERE dnsname = 'ciscorouter9605.dns'"
        with DB() as conn:
            conn._insert_record(SQLCreate, valueCreate)
            conn._update_record(SQL)
            conn._delete_record(SQLdelete)
        pass