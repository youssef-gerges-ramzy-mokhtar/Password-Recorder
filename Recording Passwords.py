def addPassword(file, title, user, pas):
    file.write(title + "\n")
    file.write(user + "\n")
    file.write(pas + "\n")
    file.write("\n")

def userInput(file):
    print("Please add your details")
    add = "y"
    while add == "y":
        title = input("Enter the title: ")
        user = input("Enter the Username: ")
        pas = input("Enter the password: ")
        addPassword(file, title, user, pas)

        add = input("please choose do you want to add another one (y/n) ")
        while add != "y" and add != "n":
            print("Invalid input")
            add = input("please choose do you want to add another one (y/n) ")

    file.close()

file = open("Passwords.txt", "a")
userInput(file)