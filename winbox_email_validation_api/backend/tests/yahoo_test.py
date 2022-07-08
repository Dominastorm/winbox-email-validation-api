import smtplib
import time
import imaplib
import email
from email.header import decode_header

username = "testwinbox@gmail.com"
password = "ypsdccdiwccyrkrk"

def send_mails(username, password, emails):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.login(username, password)
    sent_subject = "Test mail"
    sender = "testwinbox@gmail.com"
    sent_body = ("Hey!\n\n"
            "This indeed is a test mail!\n"
            "\n"
            "Cheers,\n"
            "Winbox\n")
    email_text = """\
    From: %s\r\n
    Subject: %s\r\n

    %s
    """ % (sender, sent_subject, sent_body)
    s.sendmail(sender, emails, email_text)
    s.quit()

def clean(text):
    # clean text for creating a folder
    return "".join(c if c.isalnum() else "_" for c in text)

def get_emails(username, password, li):
    # Create an IMAP4 class with SSL
    imap = imaplib.IMAP4_SSL('imap.gmail.com')
    # Login to the IMAP4 server
    imap.login(username, password)

    # Select the INBOX
    status, messages = imap.select('NDR')
    curr_mails = int(messages[0])

    send_mails(username, password, li)

    time.sleep(15)
    # Number of new emails to fetch
    status, message = imap.select('NDR')
    new_mails = int(message[0])
    N = new_mails - curr_mails
    # total number of emails
    messages = int(messages[0])

    all_messages = ""

    # fetch the emails
    for i in range(messages-N, messages):
        # fetch the email message by ID
        res, msg = imap.fetch(str(i), "(RFC822)")
        for response in msg:
            if isinstance(response, tuple):
                # parse a bytes email into a message object
                msg = email.message_from_bytes(response[1])
                # decode the email subject
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    # if it's a bytes, decode to str
                    subject = subject.decode(encoding)
                # decode email sender
                From, encoding = decode_header(msg.get("From"))[0]
                if isinstance(From, bytes):
                    From = From.decode(encoding)
                # if the email message is multipart
                if msg.is_multipart():
                    # iterate over email parts
                    for part in msg.walk():
                        # extract content type of email
                        content_type = part.get_content_type()
                        content_disposition = str(part.get("Content-Disposition"))
                        try:
                            # get the email body
                            body = part.get_payload(decode=True).decode()
                        except:
                            pass
                        if content_type == "text/plain" and "attachment" not in content_disposition:
                            # print text/plain emails and skip attachments
                            all_messages += body
                            
                else:
                    # extract content type of email
                    content_type = msg.get_content_type()
                    # get the email body
                    body = msg.get_payload(decode=True).decode()
                    if content_type == "text/plain":
                        # print only text email parts
                        all_messages += body
    # close the connection and logout
    imap.close()
    imap.logout()
    return all_messages == ""

def yahoo_test(email):
    return get_emails(username, password, [email])