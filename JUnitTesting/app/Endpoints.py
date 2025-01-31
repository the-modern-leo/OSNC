import unittest

import app.Endpoints
from app.Endpoints import ScanNetworkForEndPoints,updateEndpoints,gatherVlansForRouters
from Services.SQL.Mysql import DB


class MyTestCase(unittest.TestCase):
    def test_something(self):
        updateEndpoints()
        self.assertEqual(True, False)  # add assertion here
    def test_GetVlanInformationFromRouter(self):
        gatherVlansForRouters()
        self.assertEqual(True, False)  # add assertion here
    def test_make_table(self):
        with DB() as conn:
            conn.create_tables()
    def testL2_security(self):
        pass
    def test_GetPathToDHCPFromEdge(self):

        pass
if __name__ == '__main__':
    unittest.main()
