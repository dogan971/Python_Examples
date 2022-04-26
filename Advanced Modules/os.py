from datetime import datetime
import os

# os.chdir("C:/Users/es_lo/Desktop") # Dizini değiştiriyor
# print(os.getcwd()) # Bulunduğu dizini söylüyor.
# print(os.listdir()) # bulunduğumuz konumun dosyalarını listeliyor
# os.mkdir("deneme1") # klasör oluşturuyor
# os.makedirs("deneme1/deneme2/deneme3")
# os.rmdir("deneme1/deneme2/deneme3") # deneme 1 in altındaki 2 ve 3 ü sildi
# os.removedirs ("Deneme2/Deneme3") bütün yazılı klasörleri siliyor
# os.rename("test.txt","test.py") # dosya ismi değiştirme
# print(os.stat("test.py")) # dosyanın özelliklerini gösteriyor
# print(datetime.fromtimestamp(os.stat("test.py").st_atime))  dosyanın özelliklerinin içinden değiştirilme  zamanını alıp şuanki tarih ile arasındaki farkı öğrendik
# for i in os.walk("C:/Users/es_lo/Desktop"): # dosyalar da ve onların alt klasörlerinde geziniyor
#     print(i)

for klasor_yolu,klasor_isimleri,dosya_isimleri in os.walk("C:/Users/es_lo/Desktop"):
    print("Klasör Yolu:",klasor_yolu)
    print("Klasör İsimleri:",klasor_isimleri)
    print("Dosya İsimleri:",dosya_isimleri)