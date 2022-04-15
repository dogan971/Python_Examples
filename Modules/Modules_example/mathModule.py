def factorial(value):
    factorial = 1
    if(value == 0 or value == 1):
        return 1
    else:
        while (value >= 1):
            factorial *= value
            value -= 1
            
    print(factorial)


def calculator ():
    sum = 0
    while True:
        type_of_operation = input("+,-,/,*,for quit 'q',to clear 'c': ")
        if(type_of_operation == "q"):
            break
        if(type_of_operation == "c"):
            sum = 0
            print(f"Sum => {sum}")
            continue
        x = int(input("Enter the value: "))
        y = int(input("Enter the value: "))
        if(type_of_operation == "+"):
            sum += x + y 
            print(f"{sum}")
        elif(type_of_operation == "*"):
            sum += x * y 
            print(f"{sum}")
        elif(type_of_operation == "/"):
            sum += x / y 
            print(f"{sum}")
        elif(type_of_operation == "-"):
            sum += x - y
            print(f"{sum}")
       

    

