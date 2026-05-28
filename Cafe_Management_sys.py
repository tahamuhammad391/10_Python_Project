#  Cafe Management System in Python.
#  In this project the customer place an order from the list and get the total Bill.

menu={
    'Chai':50,
    'Aloo paratha':110,
    'Chicken paratha':150,
    'Chicken Cheese pyaratha':210,
    'Burger':100,
}

print("Welcome to Python Cafe!....")
print("Chai = Rs50\nAloo Paratha= Rs110\nChicken Paratha = Rs150\nChicken Cheese Paratha = Rs210\nBurger = Rs100")
# This variable is used to add the prices of items and show the total bills.  
Total_price = 0
while True:
    items=input("Enter the item youn want to oreder from list = ").capitalize()

    if items in menu:
        Total_price += menu[items]
        print("Your Total price is = ",Total_price)
    else:
        print(f"This {items} item is not Available in our cafe.....")

    choice = input("Enter the choice if you want order (YES/NO) = ").upper()
    if choice =="YES":
        continue
    else:
        break









# if choice == "YES":
#     second_item=input("Enter the item youn want to oreder from list = ").capitalize()
#     if second_item in menu:
#        Total_price += menu[second_item] 
#     else:
#         print(f"This {second_item} item is not Available in our cafe.....")
# print("Your Total price is = ",Total_price)


