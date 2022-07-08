import smtplib

username = "dchawla228@gmail.com"
password = "bwgohvehnrojmktq"



def send_mail(username, password, email):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.login(username, password)
    sent_subject = "Test mail"
    sender = "testwinbox@gmail.com"
    sent_body = ("Hey!\n\n"
            "This is a test mail!\n"
            "\n"
            "Cheers,\n"
            "Winbox\n")
    email_text = """\
    From: %s\r\n
    Subject: %s\r\n
    
    %s
    """ % (sender, sent_subject, sent_body)
    print(s.sendmail(sender, email, email_text))
    s.quit()



send_mail(username, password,["testwinbox@gmail.com"])