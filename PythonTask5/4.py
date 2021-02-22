user = "ayushi"
password = "agrawal"
if input("Enter username:") == user:
    for i in range(0,3):
        pass1 = input("Enter passowrd: ")
        if pass1 == password:
            print("Correct user and password")
            break
        else:
            print("Password incorrect please retype again")
            pass