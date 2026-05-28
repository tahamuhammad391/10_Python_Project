# Student Result Management System ....................

# We are using 
# 1) Conditional Statements. 
# 2) Loops.
# 3) Dictionaries. 

student ={}

while True:
    print("welcome to Student Result App!!!!!!\n")

    print("Press 1 to Add The Student")
    print("Press 2 to View All Student")
    print("Press 3 to Check the Result")
    print("Press 4 to delete the student")
    print("Press 5 to Exit")

    choice = int(input("Enter the Number between 1 to 5 = "))

    if choice == 1:
        name = input("Enter the Name of student = ")
        marks = int(input("Enter the Marks of Student = "))
        student[name]=marks
        print(f"The Student {name} is Succesfully Added.")

    elif choice == 2:
        if not student:
            print("There is no Student Name !!!!")
        else:
            # print(student)
            for name,marks in student.items():
                print(name ,"-",marks) # Agar hamay dictionaries ki key and value ko dictionaries 
                # say nikalna hai to hamay for ka loop lagana hoga. 
    elif choice == 3:
        if not student:
            print("There is no Students Marks")
        else:
            name = input("Enter the Name of student for checking the marks = ")

            if name in student:
                Marks=student[name]

                if Marks >= 40:
                    print(f"{name} is Pass and obtain {Marks} Marks congratulation !!")
                else:
                    print(f"Sorry {name} got Fail!!")
    elif choice == 4:
        if not student:
            print("There is no student for deleting.......")
        else:
            name = input("Enter the Name of student for deleting....... ")
            if name in student:
                student.pop(name,"Not Found")
                print(f"The student {name} is remove....")
    elif choice == 5:
        print("Exit Thank You...............")
        break

    else:
        print("Plese Enter the valid input......")
        break

