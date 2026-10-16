#!/bin/usr/env python34
import sys
import subprocess


def run_program(program):
    result = subprocess.run([sys.executable, program])
    if result.returncode != 0:
        print(f"Error occurred while running {program}.")
        sys.exit(1)


def main_menu():
    while True:
        print("\n" + "=" * 35)
        print(" Build with one click ")
        print("=" * 35)
        print("1. Install GLPI")
        print("2. Add User")
        print("3. Install GLPI and Add User")
        print("4. Exit")
        print("=" * 35)
        choice = input("chosed the reuired option: 1-4").strip()
        if choice == "1":
            run_program("glpi-install.py")
        elif choice == "2":
            run_program("useradd.py")
        elif choice == "3":
            run_program("glpi-install.py")
            run_program("useradd.py")
        elif choice == "4":
            print("Exiting the program.")
            sys.exit(0)
        else:
            print("Invalid choice. Please select a valid option (1-4).")

if __name__ == "__main__":
    main_menu()