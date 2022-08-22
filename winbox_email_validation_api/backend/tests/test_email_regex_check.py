import unittest
from backend.validations.email_regex import email_international_regex_check, email_regex_check

class TestEmailRegex(unittest.TestCase):
    def test_email_regex_check(self):
        self.assertTrue(email_regex_check("dchawla228@gmail.com"))
        self.assertFalse(email_regex_check("invalid"))
        
    def test_email_international_regex_check(self):
        self.assertTrue(email_international_regex_check("dchawla228@gmail.com"))
        self.assertFalse(email_international_regex_check("invalid"))

