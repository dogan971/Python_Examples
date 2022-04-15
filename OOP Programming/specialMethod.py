# class Book():
#     pass

# book = Book() ## __init__ method 
# print(book) ## __str__ method
# len(book) ## __len__ method
# del book # __del__ method
class Book():
    def __init__(self,name,writer,page,type_of_book):
        print("init function")
        self.name =name
        self.writer = writer
        self.page = page
        self.type_of_book = type_of_book
    def __str__(self): # return ile bir string döndürmesi gerekiyor
        return f"İsim: {self.name}\nYazar: {self.writer}\nSayfa Sayısı: {self.page}\nKitap Türü: {self.type_of_book}"
    def __len__(self):
        return self.page
    def __del__(self):
        print("Siliniyor....... ")
book = Book("İstanbul Hatırası","Ahmet Ümit",561,"Detective")
print(book)
print(len(book))
del book
