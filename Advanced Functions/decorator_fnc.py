
# import time 


# def kare_hesapla(sayilar):
#     sonuc = list()
#     baslama = time.time()
#     for i in sayilar:
#         sonuc.append(i ** 2)
#     bitis = time.time()
#     print("Bu fonksiyon " + str(bitis-baslama) + " saniye sürdü")
#     return sonuc

# def kup_hesapla(sayilar):
#     sonuc = list()
#     baslama = time.time()
#     for i in sayilar:
#         sonuc.append(i**3)
#     bitis = time.time()
#     print("Bu fonksiyon " + str(bitis-baslama) + " saniye sürdü")    
#     return sonuc

# kare_hesapla(range(100000))
# kup_hesapla(range(100000))


# Decorator ile yapımı 

import time

def zaman_hesaplayici(func):
    def wrapper(sayilar):
        baslama = time.time()
        sonuc = func(sayilar)
        bitis = time.time()
        print(func.__name__+ " " + str(baslama-bitis)+" saniye sürdü")
        return sonuc
    return wrapper

@zaman_hesaplayici
def kare_hesapla(sayilar):
    liste = list()
    for i in sayilar:
        liste.append(i ** 2)
    return print(liste)
@zaman_hesaplayici
def kup_hesapla(sayilar):
    liste = list()
    for i in sayilar:
        liste.append(i ** 3)
    return print(liste)

kare_hesapla(range(1000000))
kup_hesapla(range(1000000))