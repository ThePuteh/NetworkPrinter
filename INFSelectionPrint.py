import subprocess
import time
import os
import socket  # Library for IP address validation
from tkinter import Tk, filedialog

def validate_ipv4(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
        return True
    except AttributeError:  # For systems without inet_pton function
        try:
            socket.inet_aton(address)
            return True
        except socket.error:
            return False
    except socket.error:
        return False

def clear_console():
    os.system('cls')  # For Windows

def browse_file():
    root = Tk()
    root.withdraw()  # Hide the root window

    file_path = filedialog.askopenfilename(
        title="Select INF File",
        filetypes=(("INF Files", "*.inf"), ("All Files", "*.*"))
    )

    root.destroy()  # Destroy the root window after file selection

    return file_path

def choose_printer():
    while True:
        clear_console()
        print("Network Printer Installation [Version 1.00]")
        print("(c) Printer Batch Installation. All rights reserved.")
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
            clear_console()  # Clears the console after IP input
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
            clear_console()  # Clears the console after IP input
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
                    subprocess.run([rundll32_path, "printui.dll,PrintUIEntry", "/ia", "/f", var_inf_path, "/h", "x64"], shell=True)
                    subprocess.run([rundll32_path, "printui.dll,PrintUIEntry", "/if", "/b", "Network Printer", "/f", var_inf_path, "/r", var_ip, "/m", var_driver], shell=True)
                    print("Installation Finished. Goodbye!")
                    time.sleep(3)
                else:
                    print("Warning: rundll32 not found. Installation cannot proceed.")
                exit()  # Exit the script after successful installation
            elif var_confirm == "NO" or var_confirm == "N":
                print("Exiting the script. Goodbye!")
                exit()  # Exit the script
            elif var_confirm == "RESTART" or var_confirm == "R":
                print("Restarting printer selection...")
                time.sleep(2)
                choose_printer()
                break  # Exit loop if 'Restart' is entered
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
