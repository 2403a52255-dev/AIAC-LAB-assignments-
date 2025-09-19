def grade(score):
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score <= 89:
        return 'B'
    elif 70 <= score <= 79:
        return 'C'
    elif 60 <= score <= 69:
        return 'D'
    elif 0 <= score < 60:
        return 'F'
    else:
        raise ValueError("Score must be between 0 and 100")
    
# test case-1:
print(grade(85))  # Output: B
#test case-2
print(grade(95))  # Expected output: A
#test case-3
print(grade(45))  # Expected output: F