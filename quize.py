import os

USER_FILE = "users.txt"

# ---------------- REGISTER ----------------
def register():
    print("\n--- Registration ---")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    email = input("Enter Email: ")

    # check user already exists
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as f:
            for line in f:
                if username == line.split(",")[0]:
                    print("Username already exists!\n")
                    return

    with open(USER_FILE, "a") as f:
        f.write(username + "," + password + "," + email + "\n")

    print("Registration Successful!\n")


# ---------------- LOGIN ----------------
def login():
    print("\n--- Login ---")
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if not os.path.exists(USER_FILE):
        print("No users registered yet.\n")
        return False

    with open(USER_FILE, "r") as f:
        for line in f:
            user, pwd, email = line.strip().split(",")
            if username == user and password == pwd:
                print("Login Successful!\n")
                quiz(username)
                return True

    print("Login Failed!\n")
    return False


# ---------------- QUIZ ----------------
def quiz(username):
    print(f"\nWelcome {username} to Quiz Game!")
    score = 0

    print("\nQ1: What is 2 + 2?")
    print("1) 3")
    print("2) 4")
    print("3) 5")
    ans = input("Choose option: ")
    if ans == "2":
        score += 1

    print("\nQ2: Python is?")
    print("1) Snake")
    print("2) Programming Language")
    print("3) Car")
    ans = input("Choose option: ")
    if ans == "2":
        score += 1

    print("\nYour Final Score:", score, "/ 2\n")


# ---------------- MAIN MENU ----------------

    while True:
        print("===== QUIZ APP =====")
        print("1. Registration")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Thank You!")
            break
        else:
            print("Invalid Choice!\n")


# Run Program
  


def update_user():
    username = input("Enter username to update: ")

    if not os.path.exists(USER_FILE):
        print("No users found.\n")
        return

    updated = False
    lines = []

    with open(USER_FILE, "r") as f:
        for line in f:
            user, pwd, email = line.strip().split(",")

            if user == username:
                print("User found! Enter new details:")
                new_password = input("New Password: ")
                new_email = input("New Email: ")
                lines.append(user + "," + new_password + "," + new_email + "\n")
                updated = True
            else:
                lines.append(line)

    if updated:
        with open(USER_FILE, "w") as f:
            f.writelines(lines)
        print("User Updated Successfully!\n")
    else:
        print("User not found!\n")



def delete_user():
    username = input("Enter username to delete: ")

    if not os.path.exists(USER_FILE):
        print("No users found.\n")
        return

    deleted = False
    lines = []

    with open(USER_FILE, "r") as f:
        for line in f:
            user = line.strip().split(",")[0]

            if user == username:
                deleted = True
                continue
            lines.append(line)

    if deleted:
        with open(USER_FILE, "w") as f:
            f.writelines(lines)
        print("User Deleted Successfully!\n")
    else:
        print("User not found!\n")


def main():
    while True:
        print("===== QUIZ APP =====")
        print("1. Registration (Create)")
        print("2. Login")
        print("3. View Users (Read)")
        print("4. Update User")
        print("5. Delete User")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            register()
        elif choice =="2":
            login()
        
        elif choice == "4":
            update_user()
        elif choice == "5":
            delete_user()
        elif choice == "6":
            print("Thank You!")
            break
        else:
            print("Invalid Choice!\n")
