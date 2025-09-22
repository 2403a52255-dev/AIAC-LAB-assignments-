def welcome_student(student):
    print("Welcome", student)

def welcome_students(students):
    for student in students:
        welcome_student(student)

students = ["Alice", "Bob", "Charlie"]
welcome_students(students)
