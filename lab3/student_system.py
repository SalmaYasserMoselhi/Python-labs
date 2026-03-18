def create_files():
    students = [
        "1,Salma Yasser",
        "2,Rana Mohamed",
        "3,Shahd Mostafa",
        "4,Ahmed Hussein",
        "5,Tara Emad"
    ]

    grades = [
        "1,Python,90",
        "1,Java,95",
        "2,Python,85",
        "2,Java,88",
        "3,Python,92",
        "3,Java,75",
        "4,Python,80",
        "4,Java,85",
        "5,Python,90",
        "5,Java,95",
    ]

    f = open("students.txt", "w")
    for line in students:
        f.write(line + "\n")
    f.close()
    print("students.txt created successfully.")

    f = open("grades.txt", "w")
    for line in grades:
        f.write(line + "\n")
    f.close()
    print("grades.txt created successfully.")


def display_student_names():
    try:
        f = open("students.txt", "r")
        lines = f.readlines()
        f.close()
    except FileNotFoundError:
        print("Error: students.txt not found.")
        return

    print("Student Names:")
    print("-" * 15)
    for line in lines:
        student_id, name = line.strip().split(",")
        print(name)


def display_python_grades():
    try:
        f = open("grades.txt", "r")
        lines = f.readlines()
        f.close()
    except FileNotFoundError:
        print("Error: grades.txt not found.")
        return

    print("Student grades in Python:")
    print("-" * 25)
    for line in lines:
        student_id, subject, grade = line.strip().split(",")
        if subject == "Python":
            print(f"Student ID: {student_id} | Grade: {grade}")


def display_student_info():
    try:
        students = {}
        f = open("students.txt", "r")
        for line in f:
            student_id, name = line.strip().split(",")
            students[student_id] = name
        f.close()
    except FileNotFoundError:
        print("Error: students.txt not found.")
        return

    try:
        grades = {}
        f = open("grades.txt", "r")
        for line in f:
            student_id, subject, grade = line.strip().split(",")
            if student_id not in grades:
                grades[student_id] = []
            grades[student_id].append((subject, grade))
        f.close()
    except FileNotFoundError:
        print("Error: grades.txt not found.")
        return

    id = input("Enter student ID: ")

    if id in students:
        print(f"Student Name: {students[id]}")
        print("Grades:")
        for subject, grade in grades.get(id, []):
            print(f"\t{subject}: {grade}")
    else:
        print("Student not found")


def display_averages():
    try:
        students = {}
        f = open("students.txt", "r")
        for line in f:
            student_id, name = line.strip().split(",")
            students[student_id] = name
        f.close()
    except FileNotFoundError:
        print("Error: students.txt not found.")
        return

    try:
        grades = {}
        f = open("grades.txt", "r")
        for line in f:
            student_id, subject, grade = line.strip().split(",")
            if student_id not in grades:
                grades[student_id] = []
            grades[student_id].append(int(grade))
        f.close()
    except FileNotFoundError:
        print("Error: grades.txt not found.")
        return

    print("Student Grades Averages:")
    print("-" * 25)
    for id, name in students.items():
        if id in grades:
            avg = sum(grades[id]) / len(grades[id])
            print(f"{name}: {avg}")
