import dns.resolver
import smtplib
import socket
from backend.helpers.mail_helpers import get_domain

def smtp_validation(email):
    
    try:
        
        domain = get_domain(email)
        
        # Get the mx record
        mx_record = str(dns.resolver.resolve(domain, 'MX')[0].exchange)
        
        # Get local server hostname
        host = socket.gethostname()
        
        # SMTP lib setup (use debug level for full output)
        server = smtplib.SMTP()
        server.set_debuglevel(0)
        
        # SMTP Conversation
        server.connect(mx_record)      
        server.helo(host)
        server.mail('dchawla228@gmail.com') 
        code, message = server.rcpt(str(email))
        server.quit()

        # Assume 250 as Success
        if code == 250:
            return True
        else:
            return False
    except:
        return False