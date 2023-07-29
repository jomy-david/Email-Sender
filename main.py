from email.message import EmailMessage
from password import password
import ssl,smtplib


# Sender and Paswword

mail_id = 'jomypythonprojects@gmail.com'
mail_pass = password


# Recievers

mail_reciever = input("Enter Mail id of the reciever >> ")

# Content

subject = input("Enter the subject of the mail >> ")
body = input("Enter the body of the mail >> ")

# content convert to EmailMessage Instance

mail = EmailMessage()
mail['From'] = mail_id
mail['To'] = mail_reciever
mail['Subject'] = subject
mail.set_content(body)

# Create SSL

context = ssl.create_default_context()

# Script to Login and send Message

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as sm:
    sm.login(mail_id,mail_pass)
    sm.sendmail(mail_id,mail_reciever,mail.as_string())