students = {}

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")
    students[roll] = {"Name": name, "Marks": marks}
    print("Student Added Successfully!\n")

def view_students():
    if not students:
        print("No records found.\n")
        return
    for roll, details in students.items():
        print(f"Roll: {roll}, Name: {details['Name']}, Marks: {details['Marks']}")
    print()

def delete_student():
    roll = input("Enter Roll Number to delete: ")
    if roll in students:
        del students[roll]
        print("Student Deleted Successfully!\n")
    else:
        print("Student Not Found.\n")

while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        delete_student()
    elif choice == '4':
        break
    else:
        print("Invalid Choice\n")Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")
    students[roll] = {"Name": name, "Marks": marks}
    print("Student Added Successfully!\n")

def view_students():
    if not students:
        print("No records found.\n")
        return
    for roll, details in students.items():
        print(f"Roll: {roll}, Name: {details['Name']}, Marks: {details['Marks']}")
    print()

def delete_student():
    roll = input("Enter Roll Number to delete: ")
    if roll in students:
        del students[roll]
        print("Student Deleted Successfully!\n")
    else:
        print("Student Not Found.\n")

while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        delete_student()
    elif choice == '4':
     