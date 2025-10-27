# User Authentication System with GUI using tkinter

import tkinter as tk
from tkinter import messagebox

# In-memory user database (username: password)
user_db = {}

# Function to register a new user
def register_user_gui():
    """
    Register a new user via GUI.
    - Checks if the username already exists.
    - If not, adds the username and password to the user_db.
    """
    username = reg_username_entry.get().strip()
    password = reg_password_entry.get().strip()
    if not username or not password:
        messagebox.showwarning("Input Error", "Please enter both username and password.")
        return
    if username in user_db:
        messagebox.showerror("Registration Failed", "Username already exists. Please choose a different username.")
    else:
        user_db[username] = password
        messagebox.showinfo("Registration Successful", f"User '{username}' registered successfully.")

# Function to log in an existing user
def login_user_gui():
    """
    Log in an existing user via GUI.
    - Checks if the username exists.
    - Verifies the password.
    """
    username = login_username_entry.get().strip()
    password = login_password_entry.get().strip()
    if not username or not password:
        messagebox.showwarning("Input Error", "Please enter both username and password.")
        return
    if username not in user_db:
        messagebox.showerror("Login Failed", "Username does not exist. Please register first.")
    elif user_db[username] == password:
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")
    else:
        messagebox.showerror("Login Failed", "Incorrect password. Please try again.")

# Create main window
root = tk.Tk()
root.title("User Authentication System")

# Registration Frame
reg_frame = tk.LabelFrame(root, text="Register", padx=10, pady=10)
reg_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

tk.Label(reg_frame, text="Username:").grid(row=0, column=0, sticky="e")
reg_username_entry = tk.Entry(reg_frame)
reg_username_entry.grid(row=0, column=1)

tk.Label(reg_frame, text="Password:").grid(row=1, column=0, sticky="e")
reg_password_entry = tk.Entry(reg_frame, show="*")
reg_password_entry.grid(row=1, column=1)

reg_button = tk.Button(reg_frame, text="Register", command=register_user_gui)
reg_button.grid(row=2, column=0, columnspan=2, pady=5)

# Login Frame
login_frame = tk.LabelFrame(root, text="Login", padx=10, pady=10)
login_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

tk.Label(login_frame, text="Username:").grid(row=0, column=0, sticky="e")
login_username_entry = tk.Entry(login_frame)
login_username_entry.grid(row=0, column=1)

tk.Label(login_frame, text="Password:").grid(row=1, column=0, sticky="e")
login_password_entry = tk.Entry(login_frame, show="*")
login_password_entry.grid(row=1, column=1)

login_button = tk.Button(login_frame, text="Login", command=login_user_gui)
login_button.grid(row=2, column=0, columnspan=2, pady=5)

# Start the GUI event loop
root.mainloop()
