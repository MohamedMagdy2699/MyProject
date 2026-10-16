#!/usr/bin/env python3

#libraries
import subprocess

# functions 
def run_command(command):
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running command: {' '.join(command)}")
    return result

# Actions
print("\n" + "="*40)
print("Installing WPS Office 2019 Snap Package")
print("="*40 + "\n")

run_command(["sudo", "apt", "update"])
if run_command(["snap", "list", "wps-2019-snap"]).returncode == 0:
    print("WPS Office 2019 already installed.")
else:
    run_command(["sudo", "snap", "install", "wps-2019-snap"])
    print("WPS Office 2019 installed successfully.")

