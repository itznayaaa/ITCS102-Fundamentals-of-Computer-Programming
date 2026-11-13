from getpass import getpass

isLogin = False
loginAttempt = 0

username = "naya"
password = "nini07"

while isLogin == False:
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")

    if username == "naya" and password == "nini07":
        print("Welcome, Naya!")
        print("Total login attempts: ", loginAttempt)
        loginAttempt += 1

    else:
        print("Username and password is incorrect. Please try again.")
        loginAttempt += 1
        isLogin = False