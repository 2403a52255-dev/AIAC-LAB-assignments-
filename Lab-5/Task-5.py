def greet_user(name, gender):
    gender = gender.lower()
    if gender == 'male':
        title = "Mr."
    elif gender == 'female':
        title = "Mrs."
    else:
        title = "Mx."
    return f"Hello, {title} {name}! Welcome"

# Take input from user
name = input("Enter your name: ")
gender = input("Enter your gender (male/female/other): ")

print(greet_user(name, gender))