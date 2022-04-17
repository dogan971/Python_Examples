# open("info.txt","w")

# file = open("C:/Users/es_lo/Desktop/info.txt","w")
# file.close()

# 'a'

# file = open("info.txt","w",encoding="utf-8")
# file.write("Mustafa Murat Çoşkun")
# file.close()

# 'a'
# file = open("info.txt","a",encoding="utf-8")
# file.write("Latif Doğan Toplouğlu")
# file.write("asd")
# file.close()

# file = open("info.txt","a",encoding="utf-8")
# file.write("selam\n") 
# file.close()

# file = open("info.txt","a",encoding="utf-8")
# file.write("Mehmet gençol\n")
# file.close()

# file = open("info.txt","r")
# file.close() 

# try:
#     file = open("info2.txt","r")
# except FileNotFoundError:
#     print("File dont found")

# For:
# file = open("info.txt","r",encoding="utf-8")
# for i in file:
#     print(i,end="")
# file.close() 

# Read:
# file = open("info.txt","r",encoding="utf-8")
# icerik = file.read() # return string 
# print(icerik)
# icerik2 = file.read()
# print(icerik2)
# file.close()

# ReadLine():
# file = open("info.txt","r",encoding="utf-8")
# print(file.readline())
# print(file.readline())
# print(file.readline())
# file.close()

# ReadLines():
# file = open("info.txt","r",encoding="utf-8")
# print(file.readlines())
# file.close()



# with

# with open("info.txt","r",encoding="utf-8") as file:
#     for i in file:
#         print(i)


# tell & seek

# with open("info.txt","r",encoding="utf-8") as file:
#     print(file.tell()) # 0 da şuanda 
#     file.seek(20) # 20.byte a gitti
#     print(file.tell()) #20 de 

# with open("info.txt","r",encoding="utf-8") as file: 
#     file.seek(5)
#     icerik = file.read(10)
#     file.seek(0)
#     print(file.tell())
#     icerik2 = file.read(6)
#     print(icerik)
#     print(icerik2)


# seek() ve write() 'r+'
# with open("info.txt","r+",encoding="utf-8") as file:
#     # file.seek(8)
#     # file.write("selam")
#     print(file.read())

# with open("info.txt","a",encoding="utf-8") as file:
#    file.write("\n2 append added\n")
    
# with open("info.txt","r+",encoding="utf-8") as file:
#     icerik = file.read()
#     icerik = "saaaa\n" + icerik
#     file.seek(0)
#     file.write(icerik)
   
# with open("info.txt","r+",encoding="utf-8") as file:
#     liste = file.readlines()
#     liste.insert(4,"Tahsin Sütcüoğlu \n")
#     file.seek(0)
#     file.writelines(liste)
        