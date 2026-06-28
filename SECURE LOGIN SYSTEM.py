SECURE LOGIN SYSTEM : 

Source Code :


import sqlite3
import hashlib

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")
conn.commit()

current_user = None

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register():
    username = input("Enter Username: ").strip()
    password = input("Enter Password: ")

    if len(username) < 3:
        print("Username must be at least 3 characters.\n")
        return

    if len(password) < 6:
        print("Password must be at least 6 characters.\n")
        return

    hashed = hash_password(password)

    try:
        cursor.execute(
            "INSERT INTO users(username,password) VALUES(?,?)",
            (username, hashed)
        )
        conn.commit()
        print("Registration Successful!\n")

    except sqlite3.IntegrityError:
        print("Username already exists.\n")

def login():
    global current_user

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    hashed = hash_password(password)

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, hashed)
    )

    user = cursor.fetchone()

    if user:
        current_user = username
        print(f"\nWelcome {username}!\n")
    else:
        print("Invalid Username or Password.\n")

def logout():
    global current_user

    if current_user:
        print(f"{current_user} Logged Out Successfully.\n")
        current_user = None
    else:
        print("No user is logged in.\n")

while True:

    print("====== Secure Login System ======")

    if current_user:
        print("Logged in as:", current_user)

    print("1. Register")
    print("2. Login")
    print("3. Logout")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        register()

    elif choice == "2":
        login()

    elif choice == "3":
        logout()

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice\n")

conn.close()


Output :

====== Secure Login System ======
1. Register
2. Login
3. Logout
4. Exit
Enter Choice: 1

Enter Username: prem
Enter Password: prem123
Registration Successful!

====== Secure Login System ======
1. Register
2. Login
3. Logout
4. Exit
Enter Choice: 2

Enter Username: prem
Enter Password: prem123

Welcome prem!

====== Secure Login System ======
Logged in as: prem
1. Register
2. Login
3. Logout
4. Exit
Enter Choice: 3

prem Logged Out Successfully.