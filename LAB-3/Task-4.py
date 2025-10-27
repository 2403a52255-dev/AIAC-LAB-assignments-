# User Authentication System: Registration and Login Functions

# Dictionary to store user credentials in-memory (username: password)
user_db = {}

def register_user():
    """
    Register a new user by asking for a username and password.
    - Checks if the username already exists.
    - If not, adds the username and password to the user_db.
    """
    username = input("Enter a new username: ").strip()
    if username in user_db:
        print("Username already exists. Please choose a different username.")
        return
    password = input("Enter a new password: ").strip()
    user_db[username] = password
    print(f"User '{username}' registered successfully.")

def login_user():
    """
    Log in an existing user by verifying username and password.
    - Checks if the username exists.
    - Verifies the password.
    """
    username = input("Enter your username: ").strip()
    if username not in user_db:
        print("Username does not exist. Please register first.")
        return
    password = input("Enter your password: ").strip()
    if user_db[username] == password:
        print(f"Login successful. Welcome, {username}!")
    else:
        print("Incorrect password. Please try again.")

# Example usage:
# Uncomment the following lines to test the functions interactively.
while True:
     action = input("Do you want to register or login? (register/login/exit): ").strip().lower()
     if action == "register":
         register_user()
     elif action == "login":
         login_user()
     elif action == "exit":
         break
     else:
         print("Invalid option. Please enter 'register', 'login', or 'exit'.")




