from regex import X


class Dosya():
    def __init__(self):
        self.liste = []
    def siir_satir(self):
       with open("şiir.txt","r+",encoding="utf-8") as file:
            
            for i in file.readlines():
                icerik = i 
                icerik = icerik[:-1]
                self.liste.append(icerik)
            print(self.liste)
    def icouldntfndname(self):
        rastgele_string = ""
        for x in self.liste:
            y = x
            rastgele_string += y[0:1]
        print(rastgele_string)
             


dosya = Dosya()
dosya.siir_satir()
dosya.icouldntfndname()