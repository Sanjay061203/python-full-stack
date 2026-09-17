import email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
From = "sanjay43650@gmail.com"
To = "dineshdinu3026@gmail.com"
subject = "you have a grt future"
msg = MIMEMultipart()
#print(msg)
#print(type(msg))
msg['From'] = From
msg['To'] = To
msg['subject'] = subject
text = "hey hello what are doing..! let's catch up to dinner"
msg.attach(MIMEText(msg['body'],'plain'))
text=msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(From,"kjmb rodd geli jkqq")
#msg = "we are so glad that your here tq sir..."
server.sendmail(From,To,text)
server.quit()
print("mail sent")
