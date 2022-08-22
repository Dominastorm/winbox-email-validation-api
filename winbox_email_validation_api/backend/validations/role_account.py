from backend.roles_and_domains import roles

def get_username(email):
    return email.split('@')[0]

def role_account_check(email):
    username = get_username(email)
    if username in roles:
        return True
    else:
        return False