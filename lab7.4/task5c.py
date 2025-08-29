class StudentRecord:
    def __init__(self, name, id, courses=None):
        self._name = name
        self._id = id
        self._courses = courses if courses is not None else []
    
    @property
    def studentName(self):
        return self._name
    
    @property
    def student_id(self):
        return self._id
    
    @property
    def courses(self):
        return self._courses
    
    def add_course(self, course):
        self._courses.append(course)
    
    def get_summary(self):
        return f"Student: {self._name}, ID: {self._id}, Courses: {', '.join(self._courses)}"

class Department:
    def __init__(self, deptName, students=None):
        self._dept_name = deptName
        self._students = students if students is not None else []
    
    @property
    def dept_name(self):
        return self._dept_name
    
    @property
    def students(self):
        return self._students
    
    def enroll_student(self, student):
        self._students.append(student)
    
    def department_summary(self):
        return f"Department: {self._dept_name}, Total Students: {len(self._students)}"

s1 = StudentRecord("Alice", 101, ["Math", "Science"])
d1 = Department("Computer Science")
d1.enroll_student(s1)
print(s1.get_summary())
print(d1.department_summary())