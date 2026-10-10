#!/usr/bin/env python3

#inserting libraries
import subprocess
import os
import pwd

subprocess.run(["sudo", "apt-get", "update"])

#getting the username from the user
username = input("Enter the username: ")

try:
    #checking if the user already exists
    pwd.getpwnam(username)
    print(f"User {username} already exists.")
except KeyError:
    #add the user to the system
    print("========================================")
    print(f"Adding user {username} to the system...")
    print("========================================")
    subprocess.run(["sudo", "adduser", username])

#adding the user to the groups netdev and lpadmin
subprocess.run(["sudo", "usermod", "-aG", "netdev,lpadmin", username])
print("user added successfully and added to the groups netdev and lpadmin.")