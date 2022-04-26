# def kareleri_al():
#     sonuç = []
#     for i in range(1,6):
#         sonuç.append(i ** 2)
#     return sonuç

# print(kareleri_al())

# def kareleri_al():
#     for i in range(1,6):
#         yield i ** 2 # Değerleri almak için yield kullanmamız lazım
        
# yield anahtar kelimesi değere ulaşmak istenilmedigi sürece çalışmıyor. yani bu func çalıştıgında yield kelimesinde tıkanıyor 
# bizim next bir sonraki adıma geçirmemiz lazım
# generator = kareleri_al()
# iterator = iter(generator)
# print(next(iterator)) 

 
# ---------------------------

# liste = [i * 3 for i in range(5)]
# print(liste) 

# generator = (i * 3 for i in range(1,5)) 
# iterator = iter(generator)
# print(next(generator))

# def carpimtablosu():
#     for i in range(1,11):
#         for j in range(1,11):
#            yield(f"{i} {j} = {i*j}")

# for i in carpimtablosu():
#     print(i)