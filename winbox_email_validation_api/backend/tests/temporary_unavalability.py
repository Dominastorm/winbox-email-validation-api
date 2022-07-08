import smtplib
import dns.resolver
import socket
import time

from helpers.mail_helpers import get_domain

def smtp_mail(email, host, server):
    server.helo(host)
    server.mail('dchawla228@gmail.com') 
    code, message = server.rcpt(str(email))
    return code, message


def temporary_unavailability_check(email, count=0):
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
        code, message = smtp_mail(email, host, server)
    
        if code == 250:
            return  "Success"
        elif code == 503:
            if count == 0:
                time.sleep(5)
                code, message = smtp_mail(email, host, server)
                count += 1
            elif count == 1:
                time.sleep(120) 
                code, message = smtp_mail(email, host, server)
                count += 1
            elif count == 2:
                time.sleep(300)
                code, message = smtp_mail(email, host, server)
                count += 1
            else:
                server.quit()
                return "Unavailable"
        else:
            server.quit()
            return "Failure"
        server.quit()
        return "Failure"
    except:
        return "Failure"
