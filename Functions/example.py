from functools import reduce

# example 1
list1 = [(3,4),(10,3),(5,6),(1,9)]
def icouldntfuncname(tuple):
    return tuple[0] * tuple[1]

print(list(map(icouldntfuncname,list1)))

# example 2
list2 =  [1,2,3,4,5,6,7,8,9,10]
filter = list(filter(lambda z :z % 2 == 0,list2))
print(reduce(lambda x,y:x+y,filter))

# example 3
names = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
lastNames = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]
for i,j in zip(names,lastNames):
    print(i,j)cd