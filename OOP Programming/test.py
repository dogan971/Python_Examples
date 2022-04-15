class Yonetici():
    def __init__(self,isim,soyisim,sehir,numara):
        self.isim = isim
        self.soyisim = soyisim
        self.sehir = sehir
        self.numara = numara
    
    def showInfo(self):
        print("Info Gösteriliyor")
        print(f"İsim {self.isim} Soyisim {self.soyisim} Sehir {self.sehir} Numara {self.numara}")



class Calisan(Yonetici):
    def __init__(self,isim,soyisim,sehir,numara,departman):
        super().__init__(isim,soyisim,sehir,numara)
        self.departman = departman
    def showInfo(self):
        print("Info Gösteriliyor")
        print(f" İsim: {self.isim} \n Soyisim: {self.soyisim} \n Sehir: {self.sehir} \n Numara: {self.numara} \n Departman: {self.departman}")


personel = Calisan("Latif","Tplgu","Ankara",543,"Bilişim")
personel.showInfo()