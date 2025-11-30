students = {}

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    students[roll] = {"name": name, "department": dept}
    print("Student Added Successfully!\n")

def view_students():
    if not students:
        print("No records found.\n")
        return
    for roll, info in students.items():
        print(f"Roll: {roll} | Name: {info['name']} | Dept: {info['department']}")
    print()

def delete_student():
    roll = input("Enter Roll Number to delete: ")
    if roll in students:
        del students[roll]
        print("Record Deleted!\n")
    else:
        print("Student not found!\n")

while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")
    
    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        break
    else:
        print("Invalid option!\n")
