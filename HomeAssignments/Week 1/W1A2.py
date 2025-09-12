def passwordValidation(inputPassword):
    for i in range(1,412) :
        if checkPassword(password):
            break
        else:
            print("Incorrect")
            retryPassword = input(f"Retry {i} : Enter Password - ")
            if checkPassword(retryPassword):
                break

def checkPassword(inputPassword):
    correctPassword = "openAI123"
    if(inputPassword == correctPassword):
        print("Login Successful")
        return True
    else:
         return False

password = input("Enter Password : ")
passwordValidation(password)

