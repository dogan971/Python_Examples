toplam = 0
while True:
    sayi = input("Sayi: ")
    if(sayi == "q"):
        print("Çıkış yapılıyor..")
        break
    else:
        sayi = int(sayi)
        toplam += sayi
        print(toplam)
