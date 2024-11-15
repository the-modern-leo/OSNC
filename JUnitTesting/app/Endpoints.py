import unittest
from app.Endpoints import ScanNetworkForEndPoints,updateEndpoints


class MyTestCase(unittest.TestCase):
    def test_something(self):
        updateEndpoints()
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
