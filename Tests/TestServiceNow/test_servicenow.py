import unittest
from servicenow import servicenow
from auth import ServiceNowAPI


class TestServiceNow(unittest.TestCase):
    def test_attach_to_ticket(self):
        snow = servicenow.ServiceNow(
                ServiceNowAPI.user, ServiceNowAPI.pwd, ServiceNowAPI.url)
        snow.add_txt_attachment(
                "TASK0262904", "test file contents...".encode(), "testfile")
        snow.remove_txt_attachment("TASK0262904", "testfile.txt")

    def test_get_incident_info(self):
        snow = servicenow.ServiceNow(
            ServiceNowAPI.user, ServiceNowAPI.pwd, ServiceNowAPI.url)
        inc_dict = snow.get_incident_info("INC0794745")
        self.assertEqual(inc_dict["number"], "INC0794745")
        self.assertEqual(inc_dict["short_description"],
                "Ticket for Testing TOAST")
        self.assertEqual(inc_dict["created_on"], "2020-07-01 21:02:40")
        self.assertEqual(inc_dict["sys_id"],
                "e22495b4db7954d00771ff441d96198d")

    def test_get_ticket(self):
        snow = servicenow.ServiceNow(
                ServiceNowAPI.user, ServiceNowAPI.pwd, ServiceNowAPI.url)
        result = snow.check_ticket("INC0794745")
        self.assertFalse(result)
        result = snow.check_ticket("RITM0219615")
        self.assertFalse(result)
        result = snow.check_ticket("TASK0262904")
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
