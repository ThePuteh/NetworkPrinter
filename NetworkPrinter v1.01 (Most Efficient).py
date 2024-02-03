import os
import time
import subprocess

def welcome_header():
    print("Network Printer Installation [Version 1.01]")
    print("(c) The Analyst. All rights reserved.")
    print()

def ricoh_printer_setup():
    os.system("cls")
    print("RICOH Printer Setup...")
    subprocess.run([
        'cscript', 
        '%WINDIR%\\System32\\Printing_Admin_Scripts\\en-US\\Prnport.vbs', 
        '-a', '-r', 'IP_RICOH', '-h', 'RICOH_IP', '-o', 'raw', '-n', '9100'
    ])
    subprocess.run([
        'rundll32', 'printui.dll,PrintUIEntry', '/ii', '/f', 'C:\\Setup\\Printer\\NetPrinter\\Driver\\Ricoh\\oemsetup.inf'
    ])
    time.sleep(2)  # Wait for the dialog to open
    exit()

def canon_printer_setup():
    os.system("cls")
    print("Canon Printer Setup...")
    subprocess.run([
        'cscript', 
        '%WINDIR%\\System32\\Printing_Admin_Scripts\\en-US\\Prnport.vbs', 
        '-a', '-r', 'IP_CANON', '-h', 'CANON_IP', '-o', 'raw', '-n', '9100'
    ])
    subprocess.run([
        'rundll32', 'printui.dll,PrintUIEntry', '/ii', '/f', 'C:\\Setup\\Printer\\NetPrinter\\Driver\\Canon\\CNP60KA64.inf'
    ])
    time.sleep(2)  # Wait for the dialog to open
    exit()

def main():
    welcome_header()
    
    while True:
        print("Choose the Printer Model to proceed...")
        print("1. Canon Printer")
        print("2. Ricoh Printer")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            canon_printer_setup()
        elif choice == "2":
            ricoh_printer_setup()
        elif choice == "3":
            exit()
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
