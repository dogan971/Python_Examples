import sqlite3
import time

from sqlalchemy import null

class Kitap():
    def __init__(self,isim,yazar,yayınevi,tür,baskı):
        self.isim = isim
        self.yazar = yazar
        self.yayınevi = yayınevi
        self.tür = tür
        self.baskı = baskı
    def __str__(self):
        return f"Kitap İsmi:{self.isim}\n Yazar İsmi:{self.yazar}\n Yayınevi:{self.yayınevi}\n Tür:{self.tür}\n Baskı:{self.baskı}"


class Kütüphane():
    def __init__(self) -> None:
        self.baglanti_olustur()
    
    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("kitaplar.db")
        self.cursor = self.baglanti.cursor()
        sorgu = "Create Table if not exists kitaplık(isim TEXT,yazar TEXT,yayınevi TEXT,tür TEXT,baskı INT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()
    def baglantiyi_kes(self):
        self.baglanti.close()
    def kitaplari_goster(self):
        sorgu = "Select * From kitaplık"
        self.cursor.execute(sorgu)
        icerik = self.cursor.fetchall()
        if(len(icerik) != 0):
            for i in icerik:
                kitap = Kitap(i[0],i[1],i[2],i[3],i[4])
                print("Kitap :",kitap)
        else:
            print("Kitap Bulunmuyor")
    def kitap_sorgula(self,isim):
        if(isim):
            self.cursor.execute("Select * From kitaplık Where isim = ?",(isim,))
            icerik = self.cursor.fetchall()
            if(len(icerik) == 0):
                print("Kitap Bulunamadı")
            else:
                for i in icerik:
                    kitap = Kitap(i[0],i[1],i[2],i[3],i[4])
                print(kitap)
        else:
            print("Boş Veri...")
    def kitap_ekle(self):
        isim = input("İsim: ")
        yazar = input("Yazar: ")
        yayınevi = input("Yayınevi: ")
        tür = input("Tür: ")
        baskı = int(input("Baskı: "))
        if(isim and yazar and yayınevi  and tür  and baskı):
            self.cursor.execute("insert into kitaplık values(?,?,?,?,?)",(isim,yazar,yayınevi,tür,baskı))
            self.baglanti.commit()

        else:
            print("Bütün verileri giriniz....")
    def kitap_sil(self,isim):
        if(isim):
            self.cursor.execute("Delete From kitaplık where isim = ?",(isim,))
            self.baglanti.commit()

        else:
            print("Veri Giriniz....")
    def baskı_yükselt(self,isim):
        if(isim):
            self.cursor.execute("Select * from kitaplık where isim = ?",(isim,))
            icerik = self.cursor.fetchall()
            if(len(icerik) == 0):
                print("Kitap Bulunamadı")
            else:
                baskı = icerik[0][4]
                baskı += 1
                self.cursor.execute("Update kitaplık set baskı  = ? where isim = ?",(baskı,isim))
                self.baglanti.commit()
        else:
            print("Bir Değer Giriniz...!")

    
 


