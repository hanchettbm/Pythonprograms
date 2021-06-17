
repeat = True
while repeat == True:
    user_exist = input("Do you have a username? Type yes or no: ")

    if user_exist == "no":
        username = input(str("Input username here: "))
        password = input (str("Input password: "))
        authentication = {"username":username, "password":password}

        check_username = input(str("What is your username?: "))
        check_password = input (str("What is your password?: "))

        if check_username in authentication.values() and check_password in authentication.values():
            print("you are authenticated.")
            repeat = False
        else:
            print("Invalid credentials")
            repeat = True

    else: 
        print("Thanks for Checking!")
        repeat = False  