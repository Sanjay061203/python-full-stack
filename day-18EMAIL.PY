"""
SMTP module
email.message

import smtplib
import ssl
from email.message import Emailmessage
sender_email="sanjay43650@gmail.com"
password="giyhpiocqpjsfbdo"

receiver_email="gsbabu1232@gmail.com"
message=Emailmessage()
messagr["From"]=sender_email
message["To"]=receiver_email
message["Subject"]="welcome Mail"
message.set_content("welcome to rockys world")

context=ssl.create_default_context()
with smtplib.SMTP("smtp.gmail.com",port=587)as smtp:
    smtp.ehlo()
    smtp.starttls(context=context)
    smtp.ehlo()
    smtp.login(sanjay43650@gmail.com,rocky@1228)
    smtp.send_message(message)
    smtp.quit()
"""
""" SMTP Module
email.message
"""
import smtplib
import ssl
from email.message import EmailMessage
sender_email ="sanjay43650@gmail.com"
password="zwyjunwuajtjjepe"

receiver_email ="gsbabu1232@gmail.com"
message = EmailMessage()
message["From"]=sender_email
message["To"]=receiver_email
message["Subject"]="Welcome Mail"
message.set_content("Welcome to the Codegnan")

context = ssl.create_default_context()

with smtplib.SMTP("smtp.gmail.com",port=587)as smtp:
    smtp.ehlo()
    smtp.starttls(context=context)
    smtp.ehlo()
    smtp.login(sender_email,password)
    smtp.send_message(message)
