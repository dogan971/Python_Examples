import sqlite3

connect = sqlite3.connect("library.db") # connect
cursor = connect.cursor() # işlemler için imlece ihtiyacımız var 
# def create_table():
#     cursor.execute("CREATE TABLE IF NOT EXISTS Books(Name TEXT,Writer TEXT,Publisher TEXT,Page INT)") # SQL sorgusu için Execute
#     connect.commit() # Bu sorgunun çalışması için commit ediyoruz
# create_table()

# def addValueToDB():
#     cursor.execute("INSERT INTO Books values('Harry Potter','J.K Rowling','Idontknow',620)")
#     connect.commit()
# addValueToDB()

# def addValueToDB(name,writer,publisher,page):
#     if(name and writer and publisher and page):
#         cursor.execute("INSERT INTO Books values(?,?,?,?)",(name,writer,publisher,page)) # input dan alıyoruz
#         connect.commit()
#     else: return print("Errorr......")


# name = input("Book Name: ")
# writer = input("Writer Name: ")
# publisher = input("Publisher Name: ")
# page = int(input("Page: "))

# addValueToDB(name,writer,publisher,page)

# def getDataFromDB():
#     cursor.execute("SELECT * FROM Books")
#     liste = cursor.fetchall()
#     print(liste)

# getDataFromDB()
# connect.close() 


# Filter:
# def getDataFromDB(name):
#     # cursor.execute("Select Name,Writer From Books")
#     # cursor.execute("Select Name From Books Where Name = 'Harry Potter'")
#     cursor.execute("Select Name From Books Where Name = ?",(name,)) # Virgül Önemli !!
#     list = cursor.fetchall()
#     print(list)

# name = input("Book Name: ")
# getDataFromDB(name)
# connect.close()

# def updateData(oldName,newName):
#     # cursor.execute("Update Books set Name = 'Harry P.' Where Name = 'Harry Potter'")
#     cursor.execute("Update Books set Writer = ? Where Writer = ?",(newName,oldName))
#     connect.commit()
 

 
# updateData("Harryyyyyyyy","JK Rowling")
# def deleteData(name):
#     cursor.execute("Delete From Books Where Name = ?",(name,))
#     connect.commit()
# name = input("Name: ")
# deleteData(name)
# connect.close()