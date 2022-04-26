from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
import smtplib 
import sys 

body = MIMEMultipart()
text = """
    sa
"""
textBody = MIMEText(text,"plain")

with open("mail.txt","r+",encoding="utf-8") as file:
    for i in file.readlines():
        i = i[:-1]
        list = i.split(",")
        body["From"] = "latiftopluogludev2@gmail.com"
        body["To"] = list[1]
        subject = input("Konu gir: ")
        body["Subject"] = subject
        body.attach(textBody)
        try:
            mail = smtplib.SMTP("smtp.gmail.com",587)
            mail.ehlo()
            mail.starttls()
            mail.login("email","password")
            mail.sendmail(body["From"],body["To"],body.as_string())
            mail.close()
        except:
            sys.stderr.write("Errorr.....")
            sys.stderr.flush()


 