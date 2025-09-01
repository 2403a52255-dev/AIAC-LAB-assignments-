def classify_age(age):
    if age < 0:
        print("Invalid Age")
        return
    match age:
        case _ if age <= 12:
            print("Child")
        case _ if age <= 19:
            print("Teenager")
        case _ if age <= 35:
            print("Young Adult")
        case _ if age <= 59:
            print("Adult")
        case _:
            print("Senior Citizen")

# --- Check Output ---
classify_age(5)    # Child
classify_age(16)   # Teenager
classify_age(28)   # Young Adult
classify_age(45)   # Adult
classify_age(70)   # Senior Citizen
classify_age(-3)   # Invalid Age

