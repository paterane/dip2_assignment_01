'''
Program: user's data registration, login, user's data recording in file and loading back to program
Created on 2023/04/29
Created by Peter Oo
'''

db = {}
email_exist = -1
password_exist = -1

def is_pass_existed(password):
    global password_exist
    password_exist = -1
    db_len = len(db)
    for idx in range(db_len):
        if db[idx]["password"] == password:
            password_exist = idx
            break

def is_mail_existed(email):
    global email_exist
    email_exist = -1
    db_len = len(db)
    for idx in range(db_len):
        if db[idx]["email"] == email:
            email_exist = idx
            break


def registration():
    print("REGISTRATION SECTION\n")
    user_email = input("Enter your email: ")
    is_mail_existed(user_email)
    if email_exist != -1:
        print("Email already existed.\nTry another\n")
        registration()
    else:
        user_name = input("Enter your username: ")
        while True:
            user_password = input("%-20s: " %("Enter password"))
            confirm_password = input("%-20s: " %("Confirm password"))
            if user_password == confirm_password:
                user_phone = int(input("Enter your phone no: "))
                user_age = int(input("Enter your age: "))
                id = len(db)
                profile = {id: {"email": user_email,
                                "name": user_name,
                                "password": user_password,
                                "phone": user_phone,
                                "age": user_age}}
                db.update(profile)
                print("Registration Completed\n")
                break
            else:
                print("Passwords not matched\nSubmit,again\n")

def login():
    print("LOGIN SECTION\n")
    user_email = input("%-10s: " %("Email"))
    user_password = input("%-10s: " %("Password"))
    is_mail_existed(user_email)
    is_pass_existed(user_password)
    if email_exist != -1 and password_exist != -1:
        print(f"Welcome {db[email_exist]['name']}\n")
        while True:
            option = input("Press '1' to see profile, 'logout', or 'exit': ")
            if option.lower() == '1':
                print("%-15s: {}".format(db[email_exist]['email']) %("Email"))
                print("%-15s: {}".format(db[email_exist]['name']) %("Name"))
                print("%-15s: {}".format(db[email_exist]['phone']) %("Ph no:"))
                print("%-15s: {}".format(db[email_exist]["age"]) %("Age"))
            elif option.lower() == "exit":
                exit_program()   
            elif option.lower() == "logout":
                break
            else:
                print('Wrong Input\nRe-submit\n')
    else:
        if email_exist == -1:
            print("Email Not Found!\nRe-submit\n")
        else:
            print("Password not correct\nRe-submit\n")
        login()

def main_sector():
    print("USER CORNER\n")
    option = input("'register', 'login' or 'exit': ")
    if option.lower() == "register":
        registration()
    elif option.lower() == "login":
        login()
    elif option.lower() == "exit":
        exit_program()
    else:
        print("[-] Wrong Input\n")
        main_sector()

def exit_program():
    saving_data()
    exit(1)

def saving_data():
    f = open("user_data.txt", "w")
    for idx in db:
        f.write(f"{db[idx]['email']}, ")
        f.write(f"{db[idx]['name']}, ")
        f.write(f"{db[idx]['password']}, ")
        f.write(f"{db[idx]['phone']}, ")
        f.write(f"{db[idx]['age']}\n")
    f.close()

def loading_data():
    try:
        f = open("user_data.txt", "r")
        line = f.readline()
        while line:
            user_data = line.split(',')
            id = len(db)
            profile = {id: {"email": user_data[0].strip(),
                            "name": user_data[1].strip(),
                            "password": user_data[2].strip(),
                            "phone": user_data[3].strip(),
                            "age": user_data[4].strip()}}
            db.update(profile)
            line = f.readline()
        f.close()
    except FileNotFoundError:
        print("Still No user in DataBase\n")

# Start of Main Program
if __name__ == "__main__":
    loading_data()
    while True:
        main_sector()