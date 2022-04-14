def faktoriyel(sayi):
    faktoriyel = 1
    if(sayi == 0 or sayi == 1):
        print("Faktoriyel ",faktoriyel)
    else:
        while (sayi >= 1):
            faktoriyel *= sayi
            sayi -= 1
        print("Faktoriyel",faktoriyel)

faktoriyel(5)

def ikiylecarp(a):
    return a * 2

toplam = ikiylecarp(5)
print(toplam)


def showInfo(ad = "bilgi yok",soyad = "bilgi yok",numara = "bilgi yok"):
    print(f"İsim {ad} Soyad {soyad} Numara {numara}")

showInfo(soyad = "Tplgu",numara=15)



def toplama (*a):
    total = 0
    for i in a:
        total += i
        print(total)
   


toplama(1,2,3,4,5,6,7,8,9,10)