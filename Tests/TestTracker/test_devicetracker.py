import unittest, time
from Tracker import devicetracker
from . import settings

class TestDeviceTracker(unittest.TestCase):
    def test_create_obj(self):
        obj = devicetracker.DeviceTracker(None, None)
        self.assertIsInstance(obj, devicetracker.DeviceTracker)

    def test_updating_a_thread(self):
        obj = devicetracker.DeviceTracker(None, None)
        obj.update(1, "This is a test", None, False)
        self.assertEqual(obj.threads[1]['message'], "This is a test")

    def test_status_error(self):
        obj = devicetracker.DeviceTracker(None, None)
        result = obj.status(1)
        self.assertEqual(result, {
                'error': 'Invalid Thread ID: Thread not found'})
    
    def test_status_removes_error(self):
        obj = devicetracker.DeviceTracker(None, None)
        obj.update(1, "this is an error", None, True)
        obj.status(1)
        self.assertEqual(obj.threads, {})

    def test_status_returns_error(self):
        obj = devicetracker.DeviceTracker(None, None)
        obj.update(1, "this is an error", None, True)
        result = obj.status(1)
        self.assertEqual(result, {'error': 'this is an error'})

    def test_status_removes_done_threads(self):
        obj = devicetracker.DeviceTracker(None, None)
        obj.update(1, None, {'data': 'data'}, False)
        obj.status(1)
        self.assertEqual(obj.threads, {})

    def test_status_returns_done_threads_data(self):
        obj = devicetracker.DeviceTracker(None, None)
        obj.update(1, None, {'data': 'data'}, False)
        result = obj.status(1)
        self.assertEqual(result['result']['data'], {'data': 'data'})

    def test_status_returns_not_done_threads_data(self):
        obj = devicetracker.DeviceTracker(None, None)
        obj.update(1, "Not done yet", {'data': 'data'}, False)
        result = obj.status(1)
        self.assertEqual(result['result']['data'], {'data': 'data'})

    def test_get_mac_results_loop(self):
        mt = settings.TestMacTracker()
        obj = devicetracker.DeviceTracker(mt, None)
        result = obj.get_mac_results(1, "mac", testing=True)
        self.assertIsInstance(result, dict)

    def test_get_mac_results_catches_error(self):
        mt = settings.TestMacTracker()
        obj = devicetracker.DeviceTracker(mt, None)
        result = obj.get_mac_results(1, "error", testing=True)
        self.assertEqual(result, None)

    def test_get_mac_results_updates_error(self):
        mt = settings.TestMacTracker()
        obj = devicetracker.DeviceTracker(mt, None)
        result = obj.get_mac_results(1, "error", testing=True)
        self.assertTrue(obj.threads[1]['error'])

    def test_mac_helper(self):
        obj = devicetracker.DeviceTracker(settings.TestMacTracker(), None)
        result = obj.mac_helper(1, 'mac', testing=True)
        self.assertEqual(result, {'mac':'mac', 'current_ip':'1.1.1.1'})

    def test_mac_helper_invalid(self):
        obj = devicetracker.DeviceTracker(settings.TestMacTracker(), None)
        result = obj.mac_helper(1, 'error', testing=True)
        self.assertIsNone(result)

    def test_get_ip_results(self):
        obj = devicetracker.DeviceTracker(None, settings.TestRouteFinder())
        result = obj.get_rf_results('1', 'ip', testing=True)
        self.assertEqual(result, {'thing': "this works"})

    def test_ip_helper_rejects_correctly(self):
        obj = devicetracker.DeviceTracker(None, settings.TestRouteFinder())
        obj.ip_helper(1, 'this is not an IP', testing=True)
        result2 = obj.ip_helper(2, "155.100.254.246", testing=True)
        result3 = obj.ip_helper(3, "10.104.6.12/26", testing=True)
        self.assertTrue(obj.threads[1]['error'])
        self.assertEqual(result2, {'thing': "this works"})
        self.assertEqual(result3, {'thing': "this works"})

    def test_track_mac_only(self):
        obj = devicetracker.DeviceTracker(settings.TestMacTracker(), None)
        obj.track(1, "mac", mac_only=True, testing=True)
        self.assertTrue(obj.threads[1]['message'] is None and 
                obj.threads[1]['error'] is False)

    def test_track_mac_only_with_bad_mac(self):
        obj = devicetracker.DeviceTracker(settings.TestMacTracker(), None)
        obj.track(1, 'error', mac_only=True, testing=True)
        self.assertTrue(obj.threads[1]['error'])

    def test_track_ip_only(self):
        obj = devicetracker.DeviceTracker(None, settings.TestRouteFinder())
        obj.track(1, "155.100.100.100", ip_only=True, testing=True)
        self.assertTrue(obj.threads[1]['message'] is None and 
                obj.threads[1]['error'] is False)
        obj.track(1, "155.100.3.5/24", ip_only=True, testing=True)
        self.assertTrue(obj.threads[1]['message'] is None and 
                obj.threads[1]['error'] is False)

    def test_track_ip_only_rejects_bad_ips(self):
        obj = devicetracker.DeviceTracker(None, settings.TestRouteFinder())
        obj.track(1, "000.999.8cde.3453", ip_only=True, testing=True)
        self.assertTrue(obj.threads[1]['error'])

    def test_track_both_ip_and_mac(self):
        obj = devicetracker.DeviceTracker(settings.TestMacTracker(),
                                          settings.TestRouteFinder())
        obj.track(1, '1.1.1.1', testing=True)
        self.assertTrue(obj.threads[1]['message'] is None and 
                obj.threads[1]['error'] is False)

    def test_track_both_mac_and_ip(self):
        obj = devicetracker.DeviceTracker(settings.TestMacTracker(),
                                          settings.TestRouteFinder())
        obj.track(1, '0000.0000.0000', testing=True)
        self.assertTrue(obj.threads[1]['message'] is None and 
                obj.threads[1]['error'] is False)

    def test_track_throws_error_on_incorrect_mac(self):
        obj = devicetracker.DeviceTracker(settings.TestMacTracker(),
                                          settings.TestRouteFinder())
        obj.track(1, 'error', testing=True)
        self.assertTrue(obj.threads[1]['error'])

    def test_start_search_with_ip(self):
        obj = devicetracker.DeviceTracker(settings.TestMacTracker(),
                                          settings.TestRouteFinder())
        result = obj.start_search('1.1.1.1', testing=True)
        time.sleep(.1)
        self.assertTrue(result['message'] is None and result['error'] is False)

    def test_start_search_with_mac(self):
        obj = devicetracker.DeviceTracker(settings.TestMacTracker(),
                                          settings.TestRouteFinder())
        result = obj.start_search('0000.0000.0000', testing=True)
        time.sleep(.1)
        self.assertTrue(result['message'] is None and result['error'] is False)

    def test_start_search_with_error(self):
        obj = devicetracker.DeviceTracker(settings.TestMacTracker(),
                                          settings.TestRouteFinder())
        result = obj.start_search('error', testing=True)
        time.sleep(.2)
        self.assertTrue(result['error'])

    def test_start_search_with_ip_get_id(self):
        obj = devicetracker.DeviceTracker(settings.TestMacTracker(),
                                          settings.TestRouteFinder())
        result = obj.start_search('1.1.1.1', testing=True, get_thread=True)
        time.sleep(.2)
        self.assertTrue(obj.threads[result]['message'] is None 
                and obj.threads[result]['error'] is False)

    def test_start_search_with_mac_get_id(self):
        obj = devicetracker.DeviceTracker(settings.TestMacTracker(),
                                          settings.TestRouteFinder())
        result = obj.start_search('0000.0000.0000', testing=True, 
                get_thread=True)
        time.sleep(.2)
        self.assertTrue(obj.threads[result]['message'] is None 
                and obj.threads[result]['error'] is False)

    def test_start_search_with_error_get_id(self):
        obj = devicetracker.DeviceTracker(settings.TestMacTracker(),
                                          settings.TestRouteFinder())
        result = obj.start_search('error', testing=True, get_thread=True)
        time.sleep(.1)
        self.assertTrue(obj.threads[result]['error'])

    def test_multiple_threads_at_once(self):
        obj = devicetracker.DeviceTracker(settings.TestMacTracker(),
                                          settings.TestRouteFinder())
        result_ip = obj.start_search('1.1.1.1', testing=True, 
                get_thread=True)
        time.sleep(.1)
        result_mac = obj.start_search('0000.0000.0000', testing=True, 
                get_thread=True)
        time.sleep(.1)
        result_error = obj.start_search('error', testing=True, get_thread=True)
        time.sleep(.1)
        self.assertTrue(obj.status(result_ip)['result']['data']['rf_result']
                ['mac'] == '0000.0000.0000')
        self.assertTrue(obj.status(result_mac)['result']['data']['mt_result']
                ['current_ip'] == '1.1.1.1')
        self.assertTrue(obj.status(result_error)['error'] is not None)
        

if __name__ == "__main__":
    unittest.main()