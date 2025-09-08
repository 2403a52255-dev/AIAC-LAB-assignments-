import hashlib
import getpass

# Simple in-memory user database with hashed passwords
users_db = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, password):
    if username in users_db:
        print("Username already exists.")
        return False
    users_db[username] = hash_password(password)
    print("Registration successful.")
    return True

def login(username, password):
    hashed = hash_password(password)
    if users_db.get(username) == hashed:
        print("Login successful.")
        return True
    else:
        print("Invalid username or password.")
        return False

def main():
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")
            register(username, password)
        elif choice == '2':
            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")
            login(username, password)
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()