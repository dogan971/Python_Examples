 
with open("football.txt","r+",encoding="utf-8") as file:
    gs = []
    fb = []
    bjk = []
    for x in file.readlines():
        x = x[:-1]
        liste = x.split(",")
        if(liste[1] == "gs"):
          gs.append(liste[0])
        elif(liste[1] == "bjk"):
          bjk.append(liste[0])
        elif(liste[1] == "fb"):
          fb.append(liste[0])  
    
    with open("gs.txt","w+",encoding="utf-8") as file2:
            for x in gs:
                file2.write(x+"\n")
                print(x)
    with open("fb.txt","w+",encoding="utf-8") as file3:
            for y in fb:
                file3.write(y+"\n")
                print(y)
    with open("bjk.txt","w+",encoding="utf-8") as file4:
            for x in bjk:
                file4.write(x+"\n") 
                print(x)                   


 