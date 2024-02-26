import imaplib
import smtplib
import ssl

password = ""


def sendEmail(receiver):
    myemail = "stephen_robot_1984@fastmail.com"
    port = 465
    smtp_server = "smtp.fastmail.com"
    message = f"""From: {myemail}
To: {receiver}

Yes I am still alive"""
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.set_debuglevel(1)
        server.login(myemail, password)
        server.sendmail(myemail, receiver, message)


def checkEmail():
    # My details
    myemail = "stephen_robot_1984@fastmail.com"
    print("Checking for new mail...")
    mail = imaplib.IMAP4_SSL('imap.fastmail.com')
    mail.login(myemail, password)
    mail.select('inbox')
    status, messages = mail.search(None, 'UNSEEN')
    message_ids = messages[0].split()
    for id in message_ids:
        status, msg_data = mail.fetch(id, '(RFC822)')
        msg = str(msg_data[0][1])
        receiver = str(msg[16:].split(">")[0])
        if "alive" in msg.lower():
            print("Sending email to: '" + receiver + "'")
            sendEmail(receiver)
    mail.close()
    mail.logout()


checkEmail()
quit()