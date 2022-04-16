# try:
#      a = int("asdcjcjkhg122223")
#      print("Program Burada")

# except:
#     print("Error....")


# try:
#     a = int(input("Sayı1: "))
#     b = int(input("Sayı2: "))
#     print(a/b)
# except ValueError:
#     print("Value Error....")
# except ZeroDivisionError:
#     print("Zero Division Error")


# try:
#     a = int(input("Sayı1: "))
#     b = int(input("Sayı2: "))
#     print(a/b)
# except (ValueError,ZeroDivisionError):
#     print("Value Error.... or ZeroDivisionError") 


# try:
#     a = int(input("Sayı1: "))
#     b = int(input("Sayı2: "))
#     print(a/b)
# except (ValueError,ZeroDivisionError):
#     print("Value Error.... or ZeroDivisionError")
# finally:
#     print("%100 WORKING")


def tersCevir(string):
    if(type(string) != str):
        raise ValueError("that's not string")
    return print(string[::-1])

# tersCevir(123) 
# tersCevir("asdcqwr")

try:
    tersCevir(12)
except ValueError:
    print("ValueError")