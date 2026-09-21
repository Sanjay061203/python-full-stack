import smtplib
import os
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
From = "sanjay43650@gmail.com"
To = "dineshdinu3026@gmail.com"
Subject = "hi hello welcome"
body = "have a grt day"
attach = "emailattachements.py"
msg = MIMEMultipart()
msg['From']=From
msg['To']=To
msg['Subject']=Subject
msg.attach(MIMEText(body))
part = MIMEBase('application','octet-stream')
print(part)
part.set_payload(open(attach).read())
encoders.encode_base64(part)
part.add_header(f'content-disposition','attachement;filename={os.path.basename(attach)}')
msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("sanjay43650@gmail.com","aohc sxob wwxl lzjy")
server.sendmail(From,To,text)
server.quit()
print("mail sent")

