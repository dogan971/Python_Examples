
def yeni_ozellik(func):
    def wrapper(sayilar):
        ciftler_toplamı = 0
        cift_sayilar = 0
        tekler_toplami = 0
        tek_sayilar = 0
        for i in sayilar:
            if i % 2 == 0:
                ciftler_toplamı += i
                cift_sayilar += 1
            else:
                tekler_toplami += i
                tek_sayilar += 1
        func(sayilar)
        return print(f"Teklerin Ortalaması:{tekler_toplami / tek_sayilar},Çiftlerin Ortalaması:{ciftler_toplamı/cift_sayilar}")
    return wrapper
@yeni_ozellik
def ortalamabul(sayilar):
    toplam = 0
    for i in sayilar:
        toplam += i
    print("Genel Ortalama:",toplam/len(sayilar))

ortalamabul(range(100500))

for i in range(100):
    print(i)