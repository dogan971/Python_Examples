import time
import random
class Kumanda():
    def __init__(self,tv_durum = "Kapalı",tv_ses = 0,kanal_listesi = ["Trt"],kanal = "Trt"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal

    def tv_ac(self):
        if(self.tv_durum == "Açık"):
            print("Zaten Açık")
        else:
            print("Açılıyor....")
            self.tv_durum = "Açık"
    def tv_kapat(self):
        if(self.tv_durum == "Kapalı"):
            print("Zaten Kapalı")
        else:
            print("Kapatılıyor....")
            self.tv_durum = "Kapalı"
    def ses_ayarları(self):
        while True:
            cevap = input("+/-/q: ")
            if(cevap == "-"):
                if(self.tv_ses != 0):
                  self.tv_ses -= 1
                  print("Ses:",self.tv_ses)
            elif(cevap == "+"):
                if(self.tv_ses != 100):
                    self.tv_ses += 1
                    print("Ses:",self.tv_ses)
            else:
                print("Ses Güncellendi:",self.tv_ses)
                break
    def kanal_ekle(self,kanalIsmi):
        if kanalIsmi not in self.kanal_listesi:
             print("Ekleniyor....")
             self.kanal_listesi.append(kanalIsmi)
             time.sleep(1)
             print(f"Güncel Kanal Listesi:{self.kanal_listesi}")
        else:
            print("Bu kanal zaten mevcut")


    def kanal_sil(self,kanalIsmi):
       if kanalIsmi in self.kanal_listesi:
             print("Siliniyor....")
             self.kanal_listesi.remove(kanalIsmi)
             time.sleep(1)
             print(f"Güncel Kanal Listesi:{self.kanal_listesi}")
       else:
            print("Böyle bir kanal mevcut değil")        
             
    def kanal_gosterme(self):
        print("Şuanda Bulunduğunuz Kanal:",self.kanal)
    
    def kanal_degistirme(self,yeni_kanal):
        if(self.kanal != yeni_kanal):
            if yeni_kanal in self.kanal_listesi:
                print("Kanal degiştiriliyor...")
                self.kanal = yeni_kanal
                time.sleep(1)
                print(f"Güncel Kanal {self.kanal}")
            else:
                print(f"Böyle bir kanal mevcut değil. Mevcut Kanallar {self.kanal_listesi}")
        else:
            print("Zaten şu anda bu kanaldasınız")
    def kanal_listesi_goster(self):
        print(self.kanal_listesi)
    
    def rastgele_kanal(self):
        rastgele = random.randint(0,len(self.kanal_listesi) -1)
        self.kanal = self.kanal_listesi[rastgele]
        print("Şu anki Kanal: ",self.kanal)

    def __len__(self):
        return print(len(self.kanal_listesi))

    def __str__(self):
        return print(f"Tv Durumu :{self.tv_durum}\nTv Ses: {self.tv_ses}\n Kanal Listesi: {self.kanal_listesi}\n Şu anki Kanal: {self.kanal}")    

print("""
Televizyon Uygulaması

1. Tv Aç

2. Tv Kapat

3. Ses Ayarları

4. Kanal Ekle

5. Kanal Sil

6. Şu anki Kanalı Öğren

7. Kanal Listesini Öğren

8. Kanal Değiştir

9. Kanal Listesi Sayısı Öğren

Çıkmak için 'q' ya basınız.
""")

kumanda  = Kumanda()
while True:
    islem = int(input("İşlem Seçiniz: "))
    if(islem == "q"):
        print("Program Sonlandırılıyor...")
        break
    elif(islem == 1):
        kumanda.tv_ac()
    elif(islem == 2):
        kumanda.tv_kapat()
    elif(islem == 3):
        kumanda.ses_ayarları()
    elif(islem == 4):
        yeni_kanal = input("Yeni Kanal İsmi: ")
        kumanda.kanal_ekle(yeni_kanal)
    elif(islem == 5):
        silinecek_kanal = input("Silinecek Kanal İsmi: ")
        kumanda.kanal_sil(silinecek_kanal)
    elif(islem == 6):
        kumanda.kanal_gosterme()
    elif(islem == 7):
        kumanda.kanal_listesi_goster()
    elif(islem == 8):
        degisecek_kanal = input("Geçilecek Kanal İsmi: ")
        kumanda.kanal_degistirme(degisecek_kanal)
    elif(islem == 9):
        len(kumanda)
    else: 
        print("Geçersiz İşlem.......")