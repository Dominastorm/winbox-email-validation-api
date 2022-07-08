from backend.helpers.mail_helpers import get_domain
from backend.roles_and_domains import free_domains

def free_email_check(email):
    if get_domain(email) in free_domains:
        return True
    else:
        return False