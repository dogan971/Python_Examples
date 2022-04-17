# map:
# array1 = [1,2,3,4,5,6,7,8,9,10]
# array2 = [11,12,13,14,15,16,17,18,19,20]
# array3 = [21,22]
# print(list(map(lambda x,y,z: x * y and y * z,array1,array2,array3)))

# reduce:

# from functools import reduce

# print(reduce(lambda x,y:x+y,[1,2,3,4,5,6,7,8,9,10]))
# Reduce 2 li bir sistemle çalışıyor yani ilk olarak 1 + 2 yapıyor çıkan sonucu 3  ile topluyor 
# print(reduce(lambda x,y:x*y,[1,2,3,4,5])) -> 120
# bu reduce sayesinde uzun faktoriyel işlemleri bile yapabiliriz

# def maximum(x,y):
#     if x>y:
#         return x
#     else:
#         return y
# print(reduce(maximum,[-2,3,-1,5,6]))

# Filter:
# print(list(filter(lambda x : x % 2 == 0,[1,2,3,4,5,6,7,8,9,10]))) # true dönenler geldi [2, 4, 6, 8, 10]
 

# def asal_mi(x):
#     i = 2
#     if(x == 1):
#         return False
#     elif(x == 2):
#         return True
#     else:
#         while (i < x):
#             if x % i == 0:
#                 return False
#             else:
#                 return True

# print(list(filter(asal_mi,[1,2,3,4,5,6,7,8,9,10])))

#Zip:

# liste1 = [1,2,3,4,5]
# liste2 = [6,7,8,9,10,11]
# i = 0
# sonuc = []
# # sonuç = [(1,6),(2,7),(3,8),(4,9),(5,10)]
# while (i<len(liste1) and i<len(liste2)):
#     sonuc.append((liste1[i],liste2[i]))
#     i += 1

# zip ile olan hali ->
# liste1 = [1,2,3,4,5]
# liste2 = [6,7,8,9,10,11]
# print(list(zip(liste1,liste2)))  -> [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]

# liste1= [1,2,3,4,5,6,7,8,9,10]
# liste2= ["JAVA","PYTHON","ECMASCRIPT","C#"]
# liste3= [1996,542,1234,5123,51243,6543,24312,65754,124213]
# print(list(zip(liste1,liste2,liste3))) -> [(1, 'JAVA', 1996), (2, 'PYTHON', 542), (3, 'ECMASCRIPT', 1234), (4, 'C#', 5123)]

# liste1 =[1,2,3,4]
# liste2=["Python","Php","Java","Javascript"]
# for x,j in zip(liste1,liste2):
#     print(x,j)

# x = {"bir":1,"iki":2,"üç":3,"dört":4}
# y = {"Java":999,"JS":954,"py":231,"c#":2315}
# print(dict(zip(x,y)))
# {'bir': 'Java', 'iki': 'JS', 'üç': 'py', 'dört': 'c#'}


# x = {"bir":1,"iki":2,"üç":3,"dört":4}
# y = {"Java":999,"JS":954,"py":231,"c#":2315}
# print(dict(zip(x.values(),y.values())))

# Enumerate:
# liste = ["Elma","Armut","Muz","Kiraz"]
# # sonucu [(0,"Elma"),(1,"Armut"),(2,"Muz"),(3,"Kiraz")]
# i = 0
# list = []
# while i < len(liste):
#     list.append((i,liste[i]))
#     i += 1

# print(list)

# liste = ["Elma","Armut","Muz","Kiraz"]
# print(list(enumerate(liste))) -> sonucu [(0,"Elma"),(1,"Armut"),(2,"Muz"),(3,"Kiraz")]
# for i,j in enumerate(liste):
#     print(i,j)

# liste = ["a","b","c","ç","d","e"]
# for i,j in enumerate(liste):
#     if i % 2 == 0:
#         print(i,j)
    
# All ve Any:
# liste = [True,False,True,False,True,False]
# liste2 = [1,2,3,4,5,6] 
# def icouldntfunctionname(list):
#     for i in list:
#         if not i:
#             return False
#     return True
     

# print(icouldntfunctionname(liste))
# print(icouldntfunctionname(liste2))

# def any(list):
#     for i in list:
#         if i:
#             return True
#     return False

# print(any([True,False,False,True,False,True]))
# print(any([0,0,0,0,0,0,0,0,0]))

# x = all([True,False,False,True,False,True])
# print(x)
# y = any([True,False,False,True,False,True])
# print(y)