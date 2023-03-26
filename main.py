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

while True:
    choice = input(" -> Options: View Saved Passwords (view), Generate new password (gen): ").strip()

    if choice == "":
        print(" -> Invalid choice option.")
        continue

    if choice == "view":
        if os.path.isfile('saved_passwords.txt'):
            with open('saved_passwords.txt', 'r') as f:
                print(f.read())
        else:
            print(" -> No passwords saved.")
        input(" -> Press enter to return to the options menu.")
    elif choice == "gen":
        use = input(" -> What is this password going to be used for? (Easier to recognize): ")
        length = int(input(" -> Password Length (Max: 128): "))
        while length > 128:
            print(" -> Error: Password length is too long. Please try again.")
            length = int(input(" -> Password Length (Max: 128): "))
        random_string = ''.join(random.choices(pool, k=length))
        print(" -> You have generated a new password. Your password is: " + random_string)
        with open("saved_passwords.txt", "a") as file:
            file.write(use + " : " + random_string + "\n")
        print(" -> Your generated password has been automatically saved to 'saved_passwords.txt'")
    else:
        print(" -> Invalid choice option.")
