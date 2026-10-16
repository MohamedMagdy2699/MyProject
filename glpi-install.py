#!/usr/bin/env python3

# This script automates the installation of the GLPI Agent on a Linux system.
import urllib.request
import os
import subprocess
import shutil

#Variables you can change
agent_url="https://github.com/glpi-project/glpi-agent/releases/download/1.21/glpi-agent-1.21-with-snap-linux-installer.pl"
agent_directory="/tmp/glpi-agent"
glpi_server="http://41.38.193.103:8080/plugins/glpiinventory"

#Download GLPI Agent

filename = os.path.basename(agent_url)
destination = os.path.join(agent_directory, filename)

# functions
def run_command(command):
    result = subprocess.run(command, text=True)
    if result.returncode !=0:
       raise RuntimeError(f"Error occurred while running command: {' '.join(command)}")
    return result

def install_dependencies():
   
    print ("\n ==========Installing dependencies...============")
    run_command(["sudo", "apt-get", "update"])
    if shutil.which("wget") is None:  
       run_command(["sudo", "apt-get", "install", "-y", "wget"])
       print ("\n =========wget installed successfully ====")
    else: print ("wget already installed")

    if shutil.which("python3") is None:  
           run_command(["sudo", "apt-get", "install", "-y", "python3"])
           print ("\n =========python3 installed successfully ====")
    else: print ("python3 already installed")

def create_directory():
    if not os.path.exists(agent_directory):
        os.makedirs(agent_directory)
        print ("Directory created successfully")
    else:
        print ("Directory already exists")

def download_agent():
         if os.path.isfile(destination) and os.path.getsize(destination) > 0:
            print ("File already exists")
            return
        
         print ("Downloading Agent....")
         run_command(["sudo", "wget", "-P", agent_directory, agent_url])

         if not os.path.isfile(destination) or os.path.getsize(destination) == 0:
            raise RuntimeError("Failed to download GLPI agent.")

def install_agent():
    print ("Installing agent...")
    run_command(["sudo", "chmod", "+x", destination])
    result = subprocess.run(["sudo", destination],
                input=(f"{glpi_server}\n"),
                text=True
                )
def configuring_agent():
    config_file = "/etc/glpi-agent/agent.cfg"
    with open(config_file, "r") as file:
        content = file.read()
        if glpi_server in content :
           print ("glpi-agent already configured")
        else:
            print ("Configuring the agent...")
            with open(config_file, "a") as file:
                 file.write(f"\nserver = {glpi_server}\n")
            print ("Agent configured successfully")

#Run Script
def main():
    if os.geteuid() != 0:
        raise PermissionError("This script must be run as root. Please use sudo.")
    print ("========================================")
    print ("     GLPI Agent installation            ")
    print ("========================================")
    if shutil.which("glpi-agent") is None:    
       install_dependencies()
       create_directory()
       download_agent()
       install_agent()
       print("GLPI Agent installed successfully")
    else: 
        print ("glpi-agent already installed")
    configuring_agent()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)
        
