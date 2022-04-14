def factorial(value):
    """
    Description **************************
    *************************************
    """
    print("That function is mine")
    factorial = 1
    if(value == 0 or value == 1):
        return 1
    else:
        while(value >= 1):
            factorial *= value
            value -= 1
        
    print(factorial)

programming_languages = ["PHP","C#","ECMASCRIPT","JAVA"]
