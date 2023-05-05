'''
Program: user's data registration, login, user's data recording in file and loading back to program
Created on 2023/04/29
Created by Peter Oo
'''

db = {}
email_exist = -1
password_exist = -1

def is_pass_existed(password):
    '''Check whether password existed or not and return index if existed or -1'''
    global password_exist
    password_exist = -1
    db_len = len(db)
    for idx in range(db_len):
        if db[idx]["password"] == password:
            password_exist = idx
            break

def is_mail_existed(email):
    '''Check whether Email existed or not and return index if existed or -1'''
    global email_exist
    email_exist = -1
    db_len = len(db)
    for idx in range(db_len):
        if db[idx]["email"] == email:
            email_exist = idx
            break

# def number_input(user_string):
#     '''function to put only numbers and error handle mode included if alphabet is found in stdin'''
#     while True:
#         try:
#             option = int(input(user_string))
#             return option
#         except ValueError:
#             print("Enter only numbers")

def number_input(user_string):
    '''function to put only numbers and error handle mode included if alphabet is found in stdin'''
    number_list = "0123456789"
    while True:
        allow = True
        option = input(user_string)
        for ele in option:
            if ele not in number_list:
                allow = False
                break
        if allow:
            return int(option)
        else:
            print("Enter only numbers")

def registration():
    '''user's registration section to insert user's data and profile'''
    print("             REGISTRATION SECTION\n")
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
                user_phone = number_input("Enter phone no: ")
                user_age = number_input("Enter your age: ")
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
    '''Login section to allow user to check in their account profile and edit if necessary'''
    print("             LOGIN SECTION\n")
    user_email = input("%-10s: " %("Email"))
    user_password = input("%-10s: " %("Password"))
    is_mail_existed(user_email)
    is_pass_existed(user_password)
    if email_exist != -1 and password_exist != -1:
        user_corner(email_exist)
    else:
        if email_exist == -1:
            print("Email Not Found!\nRe-submit\n")
        else:
            print("Password not correct\nRe-submit\n")
        login()

def user_corner(id):
    '''Allow user to check data and update profile if necessary'''
    print("             USER CORNER\n")
    print(f"Welcome {db[id]['name']}\n")
    while True:
        option = input("'profile', 'setting', 'logout', or 'exit': ")
        if option.lower() == 'profile':
            print("%-15s: {}".format(db[id]['email']) %("Email"))
            print("%-15s: {}".format(db[id]['name']) %("Name"))
            print("%-15s: {}".format(db[id]['phone']) %("Ph no:"))
            print("%-15s: {}".format(db[id]["age"]) %("Age"))
        elif option.lower() == 'setting':
            while True:
                choice = number_input("Press 1 to update email, 2 to name, 3 to password, 4 to ph no:, 5 to age & 6 to go back: ")
                if choice == 1:
                    select = input("Update your email: ")
                    db[id]['email'] = select.lower()
                    print("Email updated successfully")
                elif choice == 2:
                    select = input("Update your name: ")
                    db[id]['name'] = select
                    print("name updated successfully")
                elif choice == 3:
                    print("Update your email password")
                    while True:
                        select = input("%-18s: " %("Enter password"))
                        confirm = input("%-18s: "%("Confirm password"))
                        if select == confirm:
                            db[id]['password'] = select
                            print("password updated successfully")
                            break
                        else:
                            print("Passwords not matched\nRe-submit")
                elif choice == 4:
                    select = number_input("Update your phone number: ")
                    db[id]['phone'] = select
                    print("Phone number updated successfully")
                elif choice == 5:
                    select = number_input("Update your age: ")
                    db[id]['age'] = select
                    print("Age updated successfully")
                elif choice == 6:
                    break
                else:
                    print('[-] Wrong Input\nRe-submit')
        elif option.lower() == "exit":
            exit_program()   
        elif option.lower() == "logout":
            break
        else:
            print('Wrong Input\nRe-submit\n')


def main_sector():
    '''Main sector to control all other sections'''
    print("             USER CENTRE\n")
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
    '''If called, database is saved to file and exit from the program'''
    saving_data()
    exit(1)

def saving_data():
    '''Saving data from database to the file'''
    f = open("user_data.txt", "w")
    for idx in db:
        f.write(f"{db[idx]['email']}, {db[idx]['name']}, {db[idx]['password']}, {db[idx]['phone']}, {db[idx]['age']}\n")
    f.close()

def loading_data():
    '''loading data from the file to program database'''
    try:
        f = open("user_data.txt", "r")
        for line in f:
            user_data = line.split(',')
            id = len(db)
            profile = {id: {"email": user_data[0].strip(),
                            "name": user_data[1].strip(),
                            "password": user_data[2].strip(),
                            "phone": user_data[3].strip(),
                            "age": user_data[4].strip()}}
            db.update(profile)
        f.close()
    except FileNotFoundError:
        print("Still No user in DataBase\n")

# Start of Main Program
if __name__ == "__main__":
    loading_data()
    while True:
        main_sector()