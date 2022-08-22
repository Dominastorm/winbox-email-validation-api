import random
import string
import math

from backend.helpers.mail_helpers import get_domain
from backend.validations.smtp import smtp_validation

def catch_all_validation(email):
    # performing catch-all detection by performing smtp test on randomly generated emails
    domain = get_domain(email)
    result = [0]*5    
    for i in range(5):
        random_email = ''.join(random.choice(string.ascii_lowercase) for _ in range(20)) + '@' + domain
        result[i] = smtp_validation(email=random_email)
    # In the case of a catch-all server, result will be [1, 1, 1, 1, 1], in all other cases, it is not a catch-all server
    return bool(math.prod(result))