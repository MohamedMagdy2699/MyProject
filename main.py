#!/bin/usr/env python34
import sys
import subprocess


def run_program(program):
    result = subprocess.run([sys.executable, program])
    if result.returncode != 0:
        raise RuntimeError(f"Error occurred while running {program}.")


def main_menu():
    while True:
        print("\n" + "=" * 35)
        print(" Build with one click ")
        print("=" * 35)
        print("1. Install GLPI")
        print("2. Add User")
        print("3. install WPS")
        print("4. run all at once")
        print("5. Exit")
        print("=" * 35)
        choice = input("chose the required option: 1-5:  ").strip()
        if choice == "1":
            run_program("glpi-install.py")
        elif choice == "2":
            run_program("useradd.py")
        elif choice == "3":
            run_program("wps-install.py")
        elif choice == "4":
            run_program("glpi-install.py")
            run_program("wps-install.py")
            choice = input("Do you want to add a user? (y/n): ").strip().lower()
            if choice == "y":
               run_program("useradd.py")
            else:
                print("User addition skipped.")
        elif choice == "5":
            print("Exiting the program.")
            sys.exit(0)
        else:
            print("Invalid choice. Please select a valid option (1-4).")

if __name__ == "__main__":
    try:
        main_menu()
    except (subprocess.CalledProcessError, FileNotFoundError, RuntimeError) as error:
        print(f"An error occurred: {error}")
        sys.exit(1)