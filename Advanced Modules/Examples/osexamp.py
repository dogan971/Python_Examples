import os
os.chdir("C:/Users/es_lo/Desktop/udemy_ydek/Git - Github")
for i in os.listdir():
    if(i.endswith(".txt")):
        os.chdir("C:/Users/es_lo/Desktop/Python Examples/Advanced Modules/Examples")
        with open("txt.txt","r+",encoding="utf-8") as file:            
            file.write(i+"\n")
    else:
        os.chdir("C:/Users/es_lo/Desktop")



       

        

