import dns.resolver
from backend.helpers.mail_helpers import get_domain
# from codecs import encode

def mx_test(email): 
    
    # domain = get_domain(encode(email,'idna'))
    # print("domain",domain)
    try:
        # res = dns.resolver.resolve('xn--'+domain.strip('-'), 'MX')
        # print("res",res)
        domain = get_domain(email)
        dns.resolver.resolve(domain, 'MX')
        return True
    except:
        return False