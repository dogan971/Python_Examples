import random
import time

print("""guess the number *****************
guess between 1 and 100

*****************""")

random_value = random.randint(1,100)
quantity = 7
while True:
    value = int(input("Enter the value: "))
    if(value < random_value):
        print("information is being questioned")
        time.sleep(1)
        print("Enter a higher value")
        quantity -= 1
        print(f"{quantity}")
    elif(value > random_value):
        print("information is being questioned")
        time.sleep(1)
        print("Enter a lower value")
        quantity -= 1
        print(f"{quantity}")
    else:
        print("Congratulations")
        time.sleep(1)
        print(value)
        break
    if(quantity == 0 ):
        print("quantity is over")
        print(f"True value = {random_value}")