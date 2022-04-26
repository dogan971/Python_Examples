
from email.mime.multipart import MIMEMultipart # mail yapısını oluşturucak
from email.mime.text import MIMEText # mail deki text
import smtplib #smtp serverına bağlanmak için
import sys # hata mesajı için

mesaj = MIMEMultipart() # önce mail yapısı oluşturduk
mesaj["From"] = "latiftopluogludev2@gmail.com" # gönderilecek yer
mesaj["To"] = "coskun.m.murat@gmail.com"
mesaj["Subject"] = "Smtp Mail Gönderme"

yazi = """
Smtp ile mail gönderimi
Latif Doğan Topluoğlu
Merhaba Hocam
"""

mesajBody = MIMEText(yazi,"plain") 

mesaj.attach(mesajBody) # mesajı attach ledik

try:
    mail = smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo() # smtp serverına bağlandık
    mail.starttls() # giricegimiz kullanıcı adımız ve şifrelerimizi şifreliyoruz.
    mail.login("mail","password")
    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string()) 
    print("Mail Başarıyla Gönderildi....")
    mail.close()
except:
    sys.stderr.write("Bir Sorun Oluştu...")
    sys.stderr.flush()