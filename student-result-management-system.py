import os
DATA_FILE = "students.txt"
def add_student():
    print("\nEnter Student Details")
    name = input("Enter Name: ")
    roll = input("Enter Roll Number: ")
    subjects = ['Maths', 'Science', 'English']
    marks = {}
    for subject in subjects:
        while True:
            try:
                mark = float(input(f"Enter marks for {subject} (out of 100): "))
                if 0 <= mark <= 100:
                    marks[subject] = mark
                    break
                else:
                    print("Marks must be between 0 and 100.")
            except ValueError:
                print("Invalid input! Enter numeric value.")
    total = sum(marks.values())
    percentage = total / len(subjects)
    status = "Pass" if all(m >= 33 for m in marks.values()) else "Fail"
    student = {
        'Name': name,
        'Roll No': roll,
        'Marks': marks,
        'Total': total,
        'Percentage': percentage,
        'Status': status
    }
    save_to_file(student)
    print("Student record added successfully!\n")
def display_results():
    print("\nStudent Result Records:\n")
    if not os.path.exists(DATA_FILE):
        print("No records found!")
        return
    with open(DATA_FILE, 'r') as f:
        data = f.readlines()
        if not data:
            print("No records to show.")
            return
        for record in data:
            student = eval(record.strip())  # Converting string back to dict
            print("-" * 50)
            print(f"Name      : {student['Name']}")
            print(f"Roll No   : {student['Roll No']}")
            for subject, mark in student['Marks'].items():
                print(f"{subject:<10}: {mark}")
            print(f"Total     : {student['Total']}")
            print(f"Percentage: {student['Percentage']:.2f}%")
            print(f"Status    : {student['Status']}")
            print("-" * 50)
def delete_student():
    print("\n Delete Student Record")
    roll_to_delete = input("Enter Roll Number of student to delete: ")
    if not os.path.exists(DATA_FILE):
        print("No records found!")
        return
    found = False
    updated_records = []
    with open(DATA_FILE, 'r') as f:
        records = f.readlines()
    for record in records:
        student = eval(record.strip())
        if student['Roll No'] == roll_to_delete:
            found = True
            print(f"Deleting record for: {student['Name']} (Roll No: {roll_to_delete})")
        else:
            updated_records.append(record)
    if found:
        with open(DATA_FILE, 'w') as f:
            f.writelines(updated_records)
        print("Record deleted successfully.")
    else:
        print("No student found with that Roll Number.")
def save_to_file(student_data):
    with open(DATA_FILE, 'a') as f:
        f.write(str(student_data) + '\n')
def menu():
    while True:
        print("\n====== 📚 Student Result Management System ======")
        print("1. Add Student")
        print("2. Display Results")
        print("3. Delete Student")
        choice = input("Enter your choice (1-3): ")
        if choice == '1':
            add_student()
        elif choice == '2':
            display_results()
        elif choice == '3':
            delete_student()
if __name__ == "__main__":
    menu()
