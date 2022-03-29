import unittest
from unittest.mock import Mock, patch
from ExternalApps.Outlook import Emailer
import socket

class mock_SMTP():
    def __init__(self, host='', port=0, local_hostname=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT, source_address=None):
        self._host = host
        self.timeout = timeout
        self.esmtp_features = {}
        self.command_encoding = 'ascii'
        self.source_address = source_address

    def starttls(self, keyfile=None, certfile=None, context=None):
         resp = "test"
         reply = "test"
         return (resp, reply)

    def sendmail(self, from_addr, to_addrs, msg, mail_options=(),
                 rcpt_options=()):
         pass

    def quit(self):
         pass


class TestOutlook(unittest.TestCase):
    @patch('ExternalApps.Outlook.SMTP', mock_SMTP)
    def test_send_email(self):
        test_subject = "Testing your Email"
        test_body = """This is a test message intended to get sent to No one. If you are getting this message
Please ignore.
        """
        test_recip = "Test_recip@test.com"
        test_sender = "Test_sender@test.com"
        with Emailer() as E:
            E.send_email(test_subject, test_body, test_recip, test_sender)

