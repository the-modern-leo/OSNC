import unittest, auth, datetime
from wirelesstools import wirelesstools

class TestWirelessTools(unittest.TestCase):
    def test_get_ap_log_info(self):
        wlo = wirelesstools.WirelessTools(auth.RFSettings.username, 
                auth.RFSettings.password, auth.CASSettings.ldap_user, 
                auth.CASSettings.ldap_pass)
        today = datetime.date.today()
        ap_dict = wlo.get_ap_log_info(482, 5, today)
        self.assertEqual(len(ap_dict.keys()), 24)
        errors = 0
        for hour in ap_dict:
            if len(ap_dict[hour]) < 1:
                errors += 1
        self.assertGreater(errors, 3)
    
    def test_organize_logs_by_hour(self):
        wlo = wirelesstools.WirelessTools(auth.RFSettings.username,
                auth.RFSettings.password, auth.CASSettings.ldap_user,
                auth.CASSettings.ldap_pass)
        logs = [
            "2020-01-01T00:45:00-06:00",
            "2020-01-01T01:45:00-06:00",
            "2020-01-01T02:45:00-06:00",
            "2020-01-01T03:45:00-06:00",
            "2020-01-01T04:45:00-06:00",
            "2020-01-01T05:45:00-06:00",
            "2020-01-01T06:45:00-06:00",
            "2020-01-01T07:45:00-06:00",
            "2020-01-01T08:45:00-06:00",
            "2020-01-01T09:45:00-06:00",
            "2020-01-01T10:45:00-06:00",
            "2020-01-01T11:45:00-06:00",
            "2020-01-01T12:45:00-06:00",
            "2020-01-01T13:45:00-06:00",
            "2020-01-01T14:45:00-06:00",
            "2020-01-01T15:45:00-06:00",
            "2020-01-01T16:45:00-06:00",
            "2020-01-01T17:45:00-06:00",
            "2020-01-01T18:45:00-06:00",
            "2020-01-01T19:45:00-06:00",
            "2020-01-01T20:45:00-06:00",
            "2020-01-01T21:45:00-06:00",
            "2020-01-01T22:45:00-06:00",
            "2020-01-01T23:45:00-06:00"
        ]
        hour_dict = wlo.organize_logs_by_hour(logs)
        for hour in range(1,24):
            self.assertEqual(len(hour_dict[hour]), 1)

    def test_try_ssh_connection(self):
        wlo = wirelesstools.WirelessTools(auth.RFSettings.username,
                auth.RFSettings.password, auth.CASSettings.ldap_user,
                auth.CASSettings.ldap_pass)
        ssh = wlo.try_ssh_connection("nalo", False)
        ssh.disconnect()
        ssh = wlo.try_ssh_connection("dhlo", False)
        ssh.disconnect()

if __name__ == "__main__":
    unittest.main()
