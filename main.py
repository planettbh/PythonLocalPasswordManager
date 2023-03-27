import time
import random
import string
import os
import ctypes
import getpass

new_title = "PasswordManager by GloryDevelopment"
ctypes.windll.kernel32.SetConsoleTitleW(new_title)
pool = string.ascii_letters + string.digits
os.system('cls')
print("   ________                 ____                 __                                 __ ")
print("  / ____/ /___  _______  __/ __ \___ _   _____  / /___  ____  ____ ___  ___  ____  / /_")
print(" / / __/ / __ \/ ___/ / / / / / / _ \ | / / _ \/ / __ \/ __ \/ __ `__ \/ _ \/ __ \/ __/")
print("/ /_/ / / /_/ / /  / /_/ / /_/ /  __/ |/ /  __/ / /_/ / /_/ / / / / / /  __/ / / / /_  ")
print("\____/_/\____/_/   \__, /_____/\___/|___/\___/_/\____/ .___/_/ /_/ /_/\___/_/ /_/\__/  ")
print("                  /____/                            /_/                                ")
print("")
print(" -> Welcome to PasswordManager by Glory Development.")
print("")
print("              Options")
print("")
print("      View saved passwords (1)")
print("      Generate a password (2)")
print("      Import a previous password (3)")
print("      Clear a saved password (4)")
print("      Clear all saved passwords (5)")
print("")

if not os.path.exists('db'):
    os.makedirs('db')

while True:
    choice = input(" -> Choose one of the options: ").strip()

    if choice == "":
        print(" -> Invalid choice option.")
        continue

    if choice == "1":
        if os.path.isfile('db/saved_passwords.txt'):
            with open('db/saved_passwords.txt', 'r') as f:
                print(f.read())
        else:
            print(" -> No passwords saved.")
        input(" -> Press enter to return to the options menu.")
    elif choice == "2":
        use = input(" -> What is this password going to be used for? (Easier to recognize): ")
        length = int(input(" -> Password Length (Max: 128): "))
        while length > 128:
            print(" -> Error: Password length is too long. Please try again.")
            length = int(input(" -> Password Length (Max: 128): "))
        random_string = ''.join(random.choices(pool, k=length))
        print(" -> You have generated a new password. Your password is: " + random_string)
        with open("db/saved_passwords.txt", "a") as file:
            file.write(use + " : " + random_string + "\n")
        print(" -> Your generated password has been automatically saved to 'db/saved_passwords.txt'")
    elif choice == "3":
        use = input(" -> What is this password used for? (Easier to recognize): ")
        imp = input(" -> Enter password you want to import: ")
        while imp == "":
            imp = input(" -> Enter password you want to import: ")
        with open("db/saved_passwords.txt", "a") as file:
            file.write(use + " : " + imp + "\n")
        print(" -> Your imported password has been automatically saved to 'db/saved_passwords.txt'")
    elif choice == "4":
        # ask user which password to delete
        password_to_delete = input(" -> Enter the name of the password you want to delete: ")
        # read all lines into a list
        with open('db/saved_passwords.txt', 'r') as file:
            lines = file.readlines()
        # remove the line containing the password to delete
        new_lines = [line for line in lines if password_to_delete not in line]
        # write the remaining lines back to the file
        with open('db/saved_passwords.txt', 'w') as file:
            for line in new_lines:
                file.write(line)
        print(" -> Password deleted successfully!")
    elif choice == "5":
        # confirm with the user before deleting all passwords
        confirm = input(" -> Are you sure you want to delete all saved passwords? (y/n): ")
        if confirm.lower() == "y":
            with open('db/saved_passwords.txt', 'w') as f:
                f.truncate(0)
            print(" -> All passwords have been deleted successfully!")
        else:
            print(" -> Action cancelled.")
    else:
        print(" -> Invalid choice option.")
