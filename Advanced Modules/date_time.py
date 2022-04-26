
from datetime import datetime
import locale


# print(datetime.now().ctime())
# print(datetime.now().strftime("%A")) # %Y -> year %B -> month  


locale.setlocale(locale.LC_ALL,"") # Dili TR ye çevirdi 
# print(datetime.now().strftime("%A"))
saniye = datetime.timestamp(datetime.now()) # saniye ye çevirme 
# print(saniye)
# print(datetime.fromtimestamp(saniye)) # saniyeyi tarihe çevirme 

# kendi tarihimizi verme

tarih = datetime(2019,12,21)
print(datetime.now() - tarih)