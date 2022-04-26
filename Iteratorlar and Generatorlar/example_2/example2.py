def asal_kontrol(sayi):
    i = 2
    while i < sayi:
        if sayi % i == 0:
            return False
        i += 1
    return True

def asal_generator():
    i = 2
    while True:
        if(asal_kontrol(i)):
            yield i
        i += 1


for i in asal_generator():
    if(i > 10000):
        break
    print(i)

