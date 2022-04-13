sys_user_name = "darkcookie"
sys_user_password = "12345"
i = 3;

while True:
    user_name = input("Insert the user name: ")
    user_password = input("Insert the password: ")
    if(user_name != sys_user_name and user_password != sys_user_password):
        print("Username and password are incorrect.")
        i -= 1
        print(f"You have {i} attempts left") 
    elif(user_name == sys_user_name and user_password != sys_user_password):
        print("Password wrong...")
        i -= 1
        print(f"You have {i} attempts left")
    elif(user_name != sys_user_name and user_password == sys_user_password):
        print("username wrong...")
        i -= 1
        print(f"You have {i} attempts left")   
    else:
        print("Login successfully")
        break;
    if(i == 0):
            break; 