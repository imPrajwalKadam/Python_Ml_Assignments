#smtpTesting@123
import smtplib
from email.message import EmailMessage

def send_mail(sender,app_password,receiver,subject,body):
    #step 1: Create email object
    msg = EmailMessage()

    #step 2: set email headers
    msg["From"] = sender
    msg["to"] = receiver
    msg["subject"] = subject


    #step 3 : add mail body
    msg.set_content(body)

    #step 4 : create SMTP SSL connection manually 
    smtp = smtplib.SMTP_SSL("smtp.gmail.com",465)

    # step 5 : Login using gmail + app password
    smtp.login(sender,app_password)

    # step 6 : send the email
    smtp.send_message(msg)

    #step 7: Close connection manully

    smtp.quit()

def main():
    sender_email = "prajwalsmtptesting03@gmail.com"
    app_password = "lzzp kssk utju nfrb"

    # reciver_email = "atharvak3.2000@gmail.com"
    reciver_email = "marvellousinfosystem@gmail.com"
    subject = "Test mail from Python script"
    body = "Jay Ganesh ," \
    "This is test mail sent using marvellous Python ." \
    "Regards" \
    "Marvellous Python"
    print(body)
    send_mail(sender_email,app_password,reciver_email,subject,body)
    print("mail sent successfully")


if __name__ == "__main__":
    main()