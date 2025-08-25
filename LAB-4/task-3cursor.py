def create_student_dict():
    students = {
        's1': {
            'full_name': 'namitha',
            'branch': 'CSE',
            'SGPA': 9.5
        },
        's2': {
            'full_name': 'sangeetha',
            'branch': 'CSE',
            'SGPA': 10
        },
        's3': {
            'full_name': 'arjun',
            'branch': 'ECE',
            'SGPA': 9.2
        }
    }
    s3_info = students['s3']
    return s3_info['full_name'], s3_info['branch'], s3_info['SGPA']

# Example usage:
full_name, branch, sgpa = create_student_dict()
print("Full Name:", full_name)
print("Branch:", branch)
print("SGPA:", sgpa)
