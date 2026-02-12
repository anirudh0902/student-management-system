import os

FILE_NAME = "students.txt"

# Function to add student
def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{roll},{name},{age},{course}\n")

    print("✅ Student Added Successfully!\n")


# Function to view all students
def view_students():
    if not os.path.exists(FILE_NAME):
        print("No records found!\n")
        return

    with open(FILE_NAME, "r") as file:
        students = file.readlines()

        if not students:
            print("No records found!\n")
            return

        print("\n--- Student List ---")
        for student in students:
            roll, name, age, course = student.strip().split(",")
            print(f"Roll: {roll}, Name: {name}, Age: {age}, Course: {course}")
        print()


# Function to search student
def search_student():
    search_roll = input("Enter Roll Number to Search: ")

    if not os.path.exists(FILE_NAME):
        print("No records found!\n")
        return

    with open(FILE_NAME, "r") as file:
        students = file.readlines()
        found = False

        for student in students:
            roll, name, age, course = student.strip().split(",")
            if roll == search_roll:
                print(f"\n🎯 Student Found:")
                print(f"Roll: {roll}, Name: {name}, Age: {age}, Course: {course}\n")
                found = True
                break

        if not found:
            print("❌ Student not found!\n")


# Function to delete student
def delete_student():
    delete_roll = input("Enter Roll Number to Delete: ")

    if not os.path.exists(FILE_NAME):
        print("No records found!\n")
        return

    with open(FILE_NAME, "r") as file:
        students = file.readlines()

    with open(FILE_NAME, "w") as file:
        found = False
        for student in students:
            roll, name, age, course = student.strip().split(",")
            if roll != delete_roll:
                file.write(student)
            else:
                found = True

    if found:
        print("🗑 Student Deleted Successfully!\n")
    else:
        print("❌ Student not found!\n")


# Main menu
while True:
    print("===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting Program...")
        break
    else:
        print("Invalid Choice! Try Again.\n")
