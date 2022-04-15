
class Car():
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        print(x+y+z)

car1 = Car(5,4,3)
print(car1)

class Software():
    def __init__(self,name,lname,phoneNumber,price,languages):
        self.name = name
        self.lname = lname
        self.phoneNumber = phoneNumber
        self.price = price
        self.languages = languages
    
    def zam_yap(self,zam_miktari):
        print("Zam yapılıyor")
        self.price += zam_miktari

    def showInfo(self):
        print(f"""       ***********************************
        Name:{self.name}
        LastName:{self.lname}
        phoneNumber:{self.phoneNumber}
        price:{self.price}
        languages:{self.languages}

        ***********************************""")





person = Software("Latif","Tplgu",54313,9500,["PHP","C#","JAVA","JAVASCRIPT","PYTHON"])
person.zam_yap(500)
person.showInfo()

# Inheritance
class Software2(Software):
    print("Software2")
    def addLanguage(self,newLanguage):
        self.languages.append(newLanguage)



person2 = Software2("Latif","Tplgu",543,9500,["PHP","C#","JAVA","JAVASCRIPT","PYTHON"])
person2.addLanguage("SQL")
person2.showInfo()



# Inheritance Overriding
class Software3(Software):
    print("Software3")
    def __init__(self, name, lname, phoneNumber, price, languages,city):
        super().__init__(name, lname, phoneNumber, price, languages)
        self.city = city    
    def showInfo(self):
        print(f"""       ***********************************
        name:{self.name}
        lastName:{self.lname}
        phoneNumber:{self.phoneNumber}
        price:{self.price}
        languages:{self.languages}
        city:{self.city}

        ***********************************""")
person3 = Software3("Latif","Tplgu",543,9500,["PHP","C#","JAVA","JAVASCRIPT","PYTHON"],"Ankara")
person3.showInfo()
        
 