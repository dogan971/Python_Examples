print("""**********************************************
Atm Makinesine Hoşgeldiniz

İşlemler:
1. Bakiye Sorgulama

2. Para Yatırma

3. Para Çekme

Programdan çıkmak için 'q' ya basınız.
**********************************************
""")

bakiye = 1000
while True:
    islem = input("İşlemi seçiniz: ")
    if(islem == "q"):
        print("Yine Bekleriz")
        break;
    elif(islem == "1"):
        print(f"Bakiyeniz {bakiye} tl dir...")
    elif(islem == "2"):
        miktar = int(input("Miktarı giriniz: "))
        bakiye += miktar
        print(f"Güncel Bakiyeniz {bakiye}")
    elif(islem == "3"):
        miktar = int(input("Çekilecek miktarı giriniz: "))
        if(bakiye - miktar < 0 ):
            print("Yetersiz Bakiye..")
            continue
        bakiye -= miktar
        print(f"Güncel Bakiyeniz {bakiye}")
    else:
        print("Geçersiz işlem...")








