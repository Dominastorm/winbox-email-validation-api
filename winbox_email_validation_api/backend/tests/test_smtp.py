import unittest
from winbox_email_validation_api.winbox_email_validation_api.settings import ALLOWED_HOSTS
import requests
import pandas as pd

URL = ALLOWED_HOSTS[1]
FILE_NAME = 'test_smtp.csv'

class TestSMTP(unittest.TestCase):
    def test_smtp(self):
        test = 'smtp'
        # read csv file
        df = pd.read_csv(rf'winbox_email_validation_api\backend\tests\{FILE_NAME}')
        # iterate over each row in the csv file
        for index, row in df.iterrows():
            # get email from csv file
            email = row['email']
            # get desired output from csv file
            desired_output = row[f'{test}']
            # make request to api
            response = requests.get(f'https://{URL}/validate/{test}/{email}')
            # get response status code
            status_code = response.status_code
            try:
                # check if status code is 200
                self.assertEqual(status_code, 200)
                # check if response body is equal to correct
                self.assertEqual(eval(response.text)['result'], desired_output)
            except Exception as e:
                raise(AssertionError(str(e) + f'Email: {email}'))
