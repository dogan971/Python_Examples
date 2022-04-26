import sys

# sys.exit()
# a = int(input("a:"))
# b = int(input("b:"))
# sys.exit() # Python ı sonlandırıyor yani altındaki hiç bir komut çalışmıyor
# c = int(input("c:"))

# stdin stderr ve stdout:

# sys.stderr.write("Bu bir hata mesajıdır\n")
# sys.stderr.flush() #oto çalışır yazmak zorunda değiliz ama dosya büyükse eğer flush ı kullanırsak hemen print alabiliriz
# sys.stdout.write("Bu normal bir mesajdır\n")

# argv:

# for i in sys.argv:
#     print(i)

# example:

def kok_bulma(a,b,c):
    delta = b ** 2 - 4 * a * c 
    if(delta < 0 ):
        print("Real kök yok ")
    else:
        x1 = (-b -delta ** 0.5) / (2*a)
        x2 = (-b +delta ** 0.5) / (2*a)
        return (x1,x2)
if(len(sys.argv) == 4):
    print("Kök Bulma:",kok_bulma(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])))
else:
    sys.stderr.write("Hata....")
    sys.stderr.flush()

