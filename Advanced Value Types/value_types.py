# print(hex(512)) 
# print(bin(4))
# print(abs(-4))
# print(round(3.1))
# print(max(3,45,5,64,3242,3412,312,312,542,6536,236,))
# print(sum([1,2,3,4,5,6,7,8,9,10]))
# pow(2,4)

# -------------------------------------------------------------------------------------------------
# x = "sd"
# print(x.upper())
# print(x.lower())

# x = "ab".replace("a","f")
# print(x)

# x = "Python Programming".split(" ")
# print(x)
# x = "                                                python                                                       ".strip(" ")
# print(x)
# x = "/////////////////////////////////////////////////////////////////////python                                                       ".lstrip("/").rstrip(" ")
# print(x)

# x = ["21","02","2014"]
# print('/'.join(x))

# x = ["T","B","M","M"]
# print('.'.join(x))

# x = "Python".count("P",0)
# print(x)
# -------------------------------------------------------------------------------------------------
# x = {1,2,3}
# print(type(x))
# y = set()
# liste = [1,2,3,4,1,1,2,2,2]
# x = set(liste)
# print(x)

# x = set("Python Programlama Dili")
# print(x)


# x = {"Elma","Armut","Kiraz","Muz"}
# for i in x:
#     print(i)

# x = {1,5,7,8,12,6,7,8,9,10}
# y = {13,52,13,45,57,68,97,658,219,10}
# x.difference_update(y)
# print(x)

# x = {1,5,7,8,12,6,7,8,9,10}
# y = {13,52,13,45,57,68,97,658,219,10}
# x.intersection_update(y)
 
# x = {1,2,3,10,34,100,-2}
# y = {1,2,23,34,-1}
# z = {30,40,50}

# print(x.isdisjoint(z)) 

# x = {1,2,3,10,34,100,-2}
# y = {1,2,23,34,-1}
# x.update(y)
# print(x)
# -------------------------------------------------------------------------------------------------
# list1 = [1,2,3,4,5,6]
# list1.insert(2,"Python")
# print(list1)
# list1 = [1,2,3,4]
# list1.pop()
# print(list1)
# list1.pop(0)
# print(list1)

list1 = [1,2,3,4]
list1.sort(reverse=True)
print(list1)