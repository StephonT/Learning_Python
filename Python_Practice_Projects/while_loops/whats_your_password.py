correct_password = "abcd1234"
password = ""

while password != correct_password:
    password = input("What is your password?")
    if password.lower() == correct_password:
        print("You have successfully unlocked your account!")
        break
    else:
        print("Wrong password. Please try again")
