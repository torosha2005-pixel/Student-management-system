students = []


def calculate_grade(avg):
    if avg >= 80:
        return "A+"
    elif avg >= 70:
        return "A"
    elif avg >= 60:
        return "A-"
    elif avg >= 50:
        return "B"
    elif avg >= 40:
        return "C"
    else:
        return "F"


def add_student():
    name = input("Enter name: ")
    roll = input("Enter roll: ")

    marks = []
    for i in range(3):
        m = float(input(f"Enter marks for subject {i+1}: "))
        marks.append(m)

    student = {
        "name": name,
        "roll": roll,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully!\n")


def show_students():
    if not students:
        print("No data found!\n")
        return

    for s in students:
        avg = sum(s["marks"]) / 3
        grade = calculate_grade(avg)

        print("\n----- Student Info -----")
        print("Name:", s["name"])
        print("Roll:", s["roll"])
        print("Marks:", s["marks"])
        print("Average:", round(avg, 2))
        print("Grade:", grade)


def modify_marks():
    roll = input("Enter roll to modify: ")

    for s in students:
        if s["roll"] == roll:
            print("Current marks:", s["marks"])

            for i in range(3):
                s["marks"][i] = float(input(f"Enter new marks for subject {i+1}: "))

            print("Marks updated!\n")
            return

    print("Student not found!\n")


def highest_student():
    if not students:
        print("No data found!\n")
        return

    top = students[0]
    max_avg = sum(top["marks"]) / 3

    for s in students:
        avg = sum(s["marks"]) / 3
        if avg > max_avg:
            max_avg = avg
            top = s

    print("\nTop Student:")
    print("Name:", top["name"])
    print("Roll:", top["roll"])
    print("Average:", round(max_avg, 2))
    print("Grade:", calculate_grade(max_avg))


while True:
    print("\n==== Student Management System ====")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Modify Marks")
    print("4. Highest Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        show_students()
    elif choice == "3":
        modify_marks()
    elif choice == "4":
        highest_student()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")