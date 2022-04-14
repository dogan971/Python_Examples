def asalSayi(x):
    if(x == 1):
        return False
    elif(x == 2):
        return True
    else:
        for y in range(2,x):
             if(x % y == 0):
                return False

        return True
                

while True:
    x = input("Sayı: ")
    if(x == "q"):
        break
    else:
        sayi = int(x)
        if(asalSayi(sayi)):
            print(sayi,"Asaldır")
        else:
            print("Asal Değildir") 