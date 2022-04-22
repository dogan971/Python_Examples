# Args: 
# def function(*args):
#     for i in args:
#         print(i)

# function(5,4,3,2,1,5,6,2,3,4,5,6,7,1)

# def function(name,*args):
#     print("Name:",name)
#     print("-----------------------")
#     for i in args:
#         print(i)
# *Args a giden VERİLER BİR TUPLE A DÖNÜŞÜYOR

# function("Latif",1,2,3) 

# -----------------------------------------------------
# Kwargs:

# def function(**kwargs):
#         print(kwargs)

# function(isim = "Latif",numara = 12345)

# def function(**kwargs):
#     for i,j in kwargs.items():
#         print(f"{i},{j}")

# function(isim = "Latif",numara = 123456)

# def function(*args,**kwargs):
#     for i in args:
#         print(i)
#     for i,j in kwargs.items():
#         print(i,j)
# function(1,2,3,4,5,6,6,7,87,isim = "Latif",numara = 123456)


# ----------------------------------------------------------

# def selamla(isim):
#     print("Selam",isim)

# merhaba = selamla
# merhaba("Latif")
# del selamla
# merhaba("Latif")

# def func():    
#     def func2():
#         print("Selam")
#     func2()


# func()

# def func(*args):
#     def func2(args):
#         toplam = 0
#         for i in args:
#             toplam += i
#         print(toplam)
#     func2(args)

# func(1,2,3,4,5,6,7,8,9,10)
 
#--------------------------------------------------------
# def mainFunc(value_type):
#     def sum(*args):
#         toplam = 0
#         for i in args:
#             toplam += i
#         return print(toplam)
#     def çarpım(*args):
#         çarpım = 1
#         for i in args:
#             çarpım *= i
#         return print(çarpım)
#     if(value_type == "sum"):
#         return sum
#     else:
#         return çarpım

# func = mainFunc("sum")
# func(1,2,3,4,5,6,7,8,9,10)
# func = mainFunc("çarpım")
# func(1,2,3,4)

# def toplama(a,b):
#     return a + b
# def çıkarma(a,b):
#     return a-b
# def çarpma(a,b):
#     return a*b
# def bölme(a,b):
#     return a/b

# def mainFunc(func1,func2,func3,func4,islem_adi):
#     if islem_adi == "toplama":
#         print(func1(4,1))
#     elif islem_adi == "çıkarma":
#         print(func2(3,2))
    
#     elif islem_adi == "çarpma":
#         print(func3(3,2))
        
#     elif islem_adi == "bölme":
#         print(func4(4,2))


# mainFunc(toplama,çıkarma,çarpma,bölme,"toplama")
# mainFunc(toplama,çıkarma,çarpma,bölme,"çarpma")
 







