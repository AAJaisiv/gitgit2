name = input("Enter username:")
passowrd = input("Enter your password:")

def login(name,password):
    if name == "Aryan" and password == "123":
       print("HI {} you have logged in successfully".format(name)) 
    else:
        print("Invalid login")   
login("Aryan","123")