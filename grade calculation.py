vize1 = int(input("1.Vize: "))
vize2 = int(input("2.Vize: "))
final = int(input("Final: "))
total = int(vize1)*(3/10) + int(vize2)*(3/10) + int(final)*(4/10)
if(total >= 90):
    print("AA")
elif(total >= 85):
    print("BA")
elif(total >=80):
    print("BB")
elif(total >=75):
    print("CB")
elif(total >=70):
    print("CC")
elif(total >=65):
    print("DC")
elif(total >=60):
    print("DD")
elif(total >=55):
    print("FD")
elif(total >=50):
    print("FF")