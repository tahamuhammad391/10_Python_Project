#  Phone MAnagement System using the Python.
# In this project, you will create a simple Phonebook application using Python. 
# This application will allow users to add, search for, delete, and list phonebook entries. 
# The project focuses on reinforcing your understanding of Python's basic concepts, 
# particularly conditional statements, dictionaries, loop and functions.

# Create a empty phone notebook. 
phoneBook={}

# Create a function which adds the name and number of a person.
def phone_add():
    No_of_phones = int(input("Enter how many Phone numbers you want to add? = "))
    for i in range(No_of_phones):
        Name=input("Enter the Name = ").capitalize()
        Number =int(input("Enter the Phone Number = "))
        if Name in phoneBook:
            print("You Entered the same person")
        else:
            phoneBook[Name]=Number
    # print(phoneBook)

def phone_search():
    print("----------------Now Search For Person---------------")
    Name=input("Enter the Name = ").capitalize()
    if Name in phoneBook:
        print(f"{Name}'s Number is: {phoneBook[Name]}")
    else:
        print("Contact not found")


def phone_delete():
    print("----------------Now Delete A Contact---------------")
    Name=input("Enter the Name = ").capitalize()
    if Name in phoneBook:
        popped=phoneBook.pop(Name)
        print(f"The {Name} item is deleted = ",popped)
    else:
        print("This Contact is not Found")
    print(phoneBook)

def phone_view():
    print("----------------View All The Contacts---------------")
    for Name,Number in phoneBook.items():
                print(Name ,"-",Number)

while True:
    phone_add()
    first_choice = int(input("Press 1 For Search Contact\nPress 2 For Delete contact\npress 3 For View All Contacts"))
    if first_choice == 1:
        phone_search()
    elif first_choice == 2:
        phone_delete()
    elif first_choice == 3:
        phone_view()
    second_choice = input("You want to Continue? (YES/NO) = ").upper()
    if second_choice == "YES":
        continue
    else:
        break