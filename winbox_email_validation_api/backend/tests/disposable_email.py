from backend.helpers.mail_helpers import get_domain
from backend.roles_and_domains import disposable_domains

def disposable_email_check(email):
    if get_domain(email) in disposable_domains:
        return True
    else:
        return False