## Cap Management System Using function, nested if, loops and data types.

print("Welcome to your portal Cap Management System")

print("User Portal")
users=[]
credential ={}
service=[]
amount=[]
def user():
    user_name=input("Enter the Name: ").lower()
    password=int(input("Enter the password: "))
    users.append(user_name)
    users.append(password)
    credential["User"]=users
    return credential

def facility():
    caps=int(input("What type of cap you want to book \n 1) Outside City Destination Ride \n 2) City Destination Ride : "))
    if caps == 2:
        Des_Ride = input("What type of cap you want to book \n 1) Ac Car \n 2) Non Ac Car \n 3) Bike :  ")    
        if Des_Ride == "Ac Car":
            print("You Enjoy Our AC Car Service")
        elif Des_Ride == "Non Ac Car":
            print("You Enjoy Our Non Ac Car Service")
        elif Des_Ride == "Bike":
            print("You Enjoy Our Bike Service")
        else:
            print("No service is Available !!! ")
        service.append(Des_Ride)
        credential["Services"]=service
        return credential
    
    if caps == 1:
        Des_Ride = input("What type of cap you want to book \n 1) Ac Car \n 2) Non Ac Car : ")    
        if Des_Ride == "Ac Car":
            print("You Enjoy Our AC Car Service")
        elif Des_Ride == "Non Ac Car":
            print("You Enjoy Our Non Ac Car Service")
        else:
            print("No service is Available !!!")
        service.append(Des_Ride)
        credential["Services"]=service
        return credential


def fare():
    count = int(input("Enter The Amount of Fare!!!: "))
    amount.append(count)
    credential["Fare"]=amount
    return credential


while True:
    persons = user()
    print(persons)
    facti = facility()
    print(facti)
    rupees = fare()
    print(rupees) 
    process = credential.get("Services")
    paisay = credential.get("Fare")
    for i,j in zip(process,paisay):
        if i == "Ac Car" and j > 1000:
            print(f"You may enjoy your {i} with {j} Amount!")
        elif i=="Non Ac Car":
            if j<=1000 and j>=500:
                print(f"You may enjoy your {i} with {j} Amount!")
        elif i=="Bike":
            if j<=500 and j>=250:
                print(f"You may enjoy your {i} with {j} Amount!") 
        else:
            print("Not Found")


    # for i in range(len(process)):
    #     if process[i] == "Ac Car" and paisay[i]> 1000:
    #         print("Good Job")
    #     else:
    #         print("Not Found")

    rerun= input("If you want to continue than press yes otherwise no : ").lower()
    if rerun == "yes":
        continue
    else:
        break




