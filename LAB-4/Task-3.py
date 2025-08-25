def create_students_dict():
    students = {
        's1': {'full_name': 'namitha', 'branch': 'CSE', 'SGPA': 9.5},
        's2': {'full_name': 'sangeetha', 'branch': 'CSE', 'SGPA': 10},
        's3': {'full_name': 'arjun', 'branch': 'ECE', 'SGPA': 9.2}
    }
    return students

def extract_student_info(students, student_key):
    student = students.get(student_key)
    if student:
        return student['full_name'], student['branch'], student['SGPA']
    else:
        return None

# Example usage:
students = create_students_dict()
s3_info = extract_student_info(students, 's3')
print(s3_info)  # Output: ('arjun', 'ECE', 9.2)