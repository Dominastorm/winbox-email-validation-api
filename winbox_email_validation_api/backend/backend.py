from helpers.csv_helpers import csv_to_array, array_to_csv 

from tests.email_regex import email_regex_check, email_international_regex_check
from tests.mx import mx_test
from tests.smtp import smtp_test
from tests.catch_all import catch_all_test
from tests.role_account import role_account_check
from tests.free_email import free_email_check
from tests.disposable_email import disposable_email_check
from tests.temporary_unavalability import temporary_unavailability_check
from tests.yahoo_test import yahoo_test


def email_validation(spreadsheet, output_file):
    
    # ask the user the validations they want to run
    headers_map = {1: 'Regex', 2: 'MX Lookup', 3: 'SMTP', 4: 'Catch All', 5: 'Role Account', 6: 'Free Email', 7: 'Disposable Email', 8: 'Temporary Unavailibility', 9: 'Yahoo Test'}
    validators_map = {1: email_regex_check, 2: mx_test, 3: smtp_test, 4: catch_all_test, 5: role_account_check, 6: free_email_check, 7: disposable_email_check, 8: temporary_unavailability_check, 9: yahoo_test}
    
    choices = eval(input("""Enter the validations you wish to perform in the form of a list:
    1. Email Regex
    2. MX
    3. SMTP
    4. Catch All
    5. Role Account
    6. Free Email
    7. Disposable Email
    8. Temporary Unavailibility Test
    9. Yahoo Test
    10. All
     """))

    if choices == 10:
        choices = list(range(1, 10))

    if type(choices) == int:
        choices = [choices]

    choices.sort()    
    
    # get the emails from the spreadsheet
    emails = csv_to_array(spreadsheet)

    # replace headers with new headers (assuming the csv entered by user has first row as headers)
    headers = ["Email"]
    for i in choices:
        headers.append(headers_map[i])
    emails[0] = headers

    # run the validations
    for row in emails[1:]:
        email = row[0]
        for i in choices:
            row.append(validators_map[i](email))

    print("Validations ran sucessfully!")

    return array_to_csv(emails, output_file)

if __name__ == "__main__":
    # upload spreadsheet
    spreadsheet = "ValidationApp/test_files/test.csv"
    output_file = 'output.csv'
    email_validation(spreadsheet, output_file)
    