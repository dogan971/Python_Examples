class Dosya():
    def __init__(self):
        self.kelime_sozluk = dict()
        with open("metin.txt","r+",encoding="utf-8") as file:
            icerik = file.read()
            kelimeler = icerik.split()
            self.sade_kelimeler = list()
            for i in kelimeler:
                i = i.strip("\n")
                i = i.strip(" ")
                i = i.strip(".")
                i = i.strip(",")
                self.sade_kelimeler.append(i)
    def tum_kelimeler(self):
        kelimeler_kumesi = set()
        for i in self.sade_kelimeler:
            kelimeler_kumesi.add(i)
        print("Tüm kelimeler..............")
        for i in kelimeler_kumesi:
            print(i)
            print("*********************************")
    def kelime_frekansı(self):
        for i in self.sade_kelimeler:
            if i in self.kelime_sozluk:
                self.kelime_sozluk[i] += 1
            else:
                self.kelime_sozluk[i] = 1
        for  i,j in self.kelime_sozluk.items():
            print(f"{i} Kelimesi {j} Defa Geçiyor....")
            print("----------------------------------------------")
    def kelime_bul(self,kelime):
        bulunan_kelime = dict()
        x = 0
        for i in self.sade_kelimeler:
            if kelime == i:
                x += 1
                bulunan_kelime[i] = x
        if(bulunan_kelime):
            print(f"Bulunan kelime '{kelime}' ve {bulunan_kelime[kelime]} tane mevcut")
        else:
            print("Bulunamadı")
      
                        
dosya = Dosya()
dosya.kelime_bul("Raskolnikov")
    