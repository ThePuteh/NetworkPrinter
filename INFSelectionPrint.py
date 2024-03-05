import subprocess
import time
import os
import socket
from tkinter import Tk, filedialog
import hashlib
import getpass
import sys

def validate_ipv4(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
        return True
    except (socket.error, AttributeError):
        try:
            socket.inet_aton(address)
            return True
        except socket.error:
            return False

def clear_console():
    os.system('cls')  # For Windows

def browse_file():
    root = Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(
        title="Select INF File",
        filetypes=(("INF Files", "*.inf"), ("All Files", "*.*"))
    )

    root.destroy()

    return file_path

def hash_password(password):
    # Use SHA-256 for hashing
    sha256 = hashlib.sha256()
    sha256.update(password.encode())
    return sha256.hexdigest()

def get_masked_password():
    return getpass.getpass("Enter password to proceed: ")

def handle_subprocess(command):
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing subprocess: {e}")
        # Handle the error gracefully, possibly logging it or prompting the user for appropriate action
        sys.exit(1)

def choose_printer():
    while True:
        clear_console()
        print("Network Printer Installation [Version 1.00]")
        print("(c) Printer Batch Installation. All rights reserved.")

        # Prompt user for password
        password = get_masked_password()

        # Hash the entered password for comparison
        hashed_password = hash_password(password)

        # Replace the stored hashed password with the actual hashed password
        stored_hashed_password = hash_password("P@55w0rd_")

        # Compare the hashed passwords
        if hashed_password == stored_hashed_password:
            print("Password accepted. Please continue.")
        else:
            print("Incorrect password. Try again.")
            time.sleep(2)
            continue  # Restart the loop if the password is incorrect

        print("")
        print("Existing Printer:")
        print("")
        print("1. Canon PCL6 Driver")
        print("2. HP Universal Printing PCL 6")
        print("")
        var_choice = input("Select your Printer Driver: ")

        if var_choice == "1":
            var_brand = "Canon Printer"
            while True:
                var_ip = input(f"IP address for {var_brand}: ")
                if var_ip.strip() and validate_ipv4(var_ip):
                    break
                else:
                    print("Invalid IPv4 format. Please enter a valid IP Address.")
            clear_console()
            var_driver = "Canon PCL6 Driver"
            var_inf_path = browse_file()
            confirm_installation(var_choice, var_brand, var_driver, var_ip, var_inf_path)
            break
        elif var_choice == "2":
            var_brand = "HP Printer"
            while True:
                var_ip = input(f"IP address for {var_brand}: ")
                if var_ip.strip() and validate_ipv4(var_ip):
                    break
                else:
                    print("Invalid IPv4 format. Please enter a valid IP Address.")
            clear_console()
            var_driver = "HP Universal Printing PCL 6 Driver"
            var_inf_path = browse_file()
            confirm_installation(var_choice, var_brand, var_driver, var_ip, var_inf_path)
            break
        else:
            print("Invalid Selection. Please try again.")
            time.sleep(2)

def confirm_installation(var_choice, var_brand, var_driver, var_ip, var_inf_path):
    clear_console()
    print(f"Printer selected : {var_brand}")
    print(f"Printer Driver : {var_driver}")
    print(f"IP address : {var_ip}")
    print(f"Driver Path Selected (INF Files) : {var_inf_path}")
    print("")
    
    while True:
        print("Proceed with this setup? (Yes/No/Restart)")
        print("Enter y/n or r for restart")
        var_confirm = input().upper()

        if var_confirm in ["YES", "NO", "RESTART", "Y", "N", "R"]:
            if var_confirm == "YES" or var_confirm == "Y":
                print("Installation starting in 5 seconds...")
                time.sleep(5)
                
                rundll32_path = os.path.join(os.environ['SYSTEMROOT'], 'System32', 'rundll32.exe')
                
                if os.path.exists(rundll32_path):
                    handle_subprocess([rundll32_path, "printui.dll,PrintUIEntry", "/ia", "/f", var_inf_path, "/h", "x64"])
                    handle_subprocess([rundll32_path, "printui.dll,PrintUIEntry", "/if", "/b", "Network Printer", "/f", var_inf_path, "/r", var_ip, "/m", var_driver])
                    print("Installation Finished. Goodbye!")
                    time.sleep(3)
                    sys.exit()
                else:
                    print("Error: rundll32 not found. Installation cannot proceed.")
                    sys.exit(1)
            elif var_confirm == "NO" or var_confirm == "N":
                print("Exiting the script. Goodbye!")
                sys.exit()
            elif var_confirm == "RESTART" or var_confirm == "R":
                print("Restarting printer selection...")
                time.sleep(2)
                choose_printer()
                break
        else:
            clear_console()
            print("Invalid Input Option!")
            time.sleep(3)
            clear_console()
            print("Your setting is :")
            print(f"Printer selected : {var_brand}")
            print(f"Printer Driver : {var_driver}")
            print(f"IP address : {var_ip}")
            print(f"INF file path : {var_inf_path}")
            print("")

if __name__ == "__main__":
    choose_printer()
