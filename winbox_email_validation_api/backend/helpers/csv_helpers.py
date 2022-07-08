import csv

# read spreadsheet
def find_column_number(spreadsheet, column_name):
    with open(spreadsheet, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if column_name in row:
                return row.index(column_name)
        else:
            raise Exception('Column not found')

# take a spreadsheet as input and return an array of emails (as arrays)
def csv_to_array(spreadsheet):
    # find the column number of email
    email_col = find_column_number(spreadsheet, 'email')
    # read all the emails and return list of emails
    with open(spreadsheet, 'r') as f:
        reader = csv.reader(f)
        emails = [["email"]]
        reader.__next__()
        for row in reader:
            email = row[email_col]
            emails.append([email])
        return emails

def array_to_csv(array, filename='output.csv'):
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(array)