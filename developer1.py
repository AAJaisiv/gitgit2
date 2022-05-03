name = input("Enter username:")
passowrd = input("Enter your password:")

def login(name,password):
    if name == "Aryan" and password == "123":
       print("HI",name, "you have logged in successfully") 
    else:
        print("Invalid login")   
login("Aryan","123")