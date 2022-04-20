class Dosya():
    def __init__(self) -> None:
        
        with open("mail.txt","r+",encoding="utf-8") as file :
            self.list = []
   
            for x in file.readlines():
                x = x[:-1]
                self.list.append(x)
            for i in self.list:
                string = i
                if "@gmail.com" in string:
                    print(string)   

        


dosya = Dosya()