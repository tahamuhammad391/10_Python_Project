# Password Manager Program........

# What we will used in this project
# 1) Loop
# 2) Conditional Statements
# 3) Dictionary
# 4) File Handiling
# 5) Module (Random Module)

import random as rmd
import string as st

password = {}


# Used File Handling!!!!
try:
    with open("Passwords.txt","r") as file:
        for line in file:
            webs,pwd= line.strip().split(":")
            password[webs]=pwd

except:
    pass

# Making a function which generates random password.
def generate_password():
    char = st.ascii_letters+st.digits+"@#$%&"
    passw = "".join(rmd.choice(char) for _ in range(8))
    return passw

while True:
    print("welcome to Password Manager App!!!!!!\n")

    print("Press 1 to Save The Password")
    print("Press 2 to View The Password")
    print("Press 3 to generate The Password")
    print("Press 4 to Exit")

    choice = int(input("Enter the Choice. = "))

    if choice == 1:
        site = input("Enter the website = ")
        pwd = input("Enter the Password = ")
        password[site]=pwd

        with open("Passwords.txt","a") as file:
            file.write(f"{site}:{pwd}\n")

        print("Password Save Successfully!!!")
    
    elif choice == 2:
        if not password:
            print("No Data")
        else:
            for site,pwd in password.items():
                print(f"{site} : {pwd}\n")
    
    elif choice == 3:
        gen_pwd=generate_password()
        print(gen_pwd)

    elif choice == 4:
        print("Exit Thank You...............")
        break

    else:
        print("Please Enter the Valid Number!!!")
        continue




