def tambolenleribulma(sayi):
    tam_bolenler = []
    for i in range(2,sayi):
        if(sayi % i == 0):
            tam_bolenler.append(i)
    return tam_bolenler


while True:
    x = input("Sayı: ")
    if(x == "q"):
        break
    else:
        x = int(x)
        if(tambolenleribulma(x)):
            print("Tam Bölünür")
        else:
            print("Tam Bölünmüyor")