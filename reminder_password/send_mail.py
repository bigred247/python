import smtplib, ssl

def send_email(usersid):

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "add_email_add@gmail.com"  # Enter your address
    receiver_email = "add_email_add@gmail.com"  # Enter receiver address
    password = "add_password_here"
    message = """\
    Subject: Hi there

    This message is sent from Python. 
    The following users passwords are due to expire. """ + usersid

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
send_email("test123")