x = input("Şekil İsmi: ")
if(x == "Dörtgen"):
    kenar1 = int(input("Kenar1: "))
    kenar2 = int(input("Kenar2: "))
    kenar3 = int(input("Kenar3: "))
    kenar4 = int(input("Kenar4: "))
    if (kenar1 == kenar2 and kenar1 == kenar3 and kenar1 == kenar4):
        print("Kare")
    elif (kenar1 == kenar3 and kenar2 == kenar4):
        print("Dikdörtgen")
    else:
        print("Dörtgen")
elif (x == "Üçgen"):
    a = int(input("Kenar-1:"))
    b = int(input("Kenar-2:"))
    c = int(input("Kenar-3:"))
    if ( abs(a+b) > c and abs(a+c) > b and abs(b+c) > a):
        if (a == b and a == c ):
            print("Eşkenar Üçgen...")
        elif ((a == b and a != c) or (a == c and a != b) or (b == c and b != a)):
            print("İkizkenar Üçgen....")
        else:
            print("Çeşitkenar Üçgen...")
    else:
        print("Üçgen belirtmiyor...")
        
else:
    print("Geçersiz Şekil...")