'''
import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
print(server)
server.starttls()
server.login("sanjay43650@gmail.com","pymv ozfd gmny fpgs")
msg = "we are glad that you cracked the highest package of the decade so we want to congragulate you and your family"
server.sendmail("sanjay43650@gamil.com","knsknsk10@gmail.com",msg)
server.quit()
print("mail sent")
'''
import math
import random
import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
otp = random.randint(0000,9999)
server.login("sanjay43650@gmail.com","pymv ozfd gmny fpgs")
msg = f"we are glad that you cracked the highest package of the decade so we want to congragulate you and your family {otp}"
server.sendmail("sanjay43650@gamil.com",["knsknsk10@gmail.com","sanjay43650@gmail.com"],msg)
server.quit()
print("mail sent")
if(otp == int(input("enter validation code: "))):
    print("yes")
else:
    print("sorry")
