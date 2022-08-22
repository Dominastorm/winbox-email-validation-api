import re

def email_regex_check(email): 
    regex = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(regex, email):
        return True
    else:
        return False

def email_international_regex_check(email):
    regex = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    from codecs import encode
    email = str(encode(email, 'idna')).strip("b").strip("'")
    if re.match(regex, email):
        return True
    else:
        return False