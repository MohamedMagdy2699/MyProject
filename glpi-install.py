#!/usr/bin/env python3

#Modules
import urllib.request
import os
import subprocess
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
       print ("command error")
       exit(1)
def install_dependencies():
    print ("Installing dependencies...")
    run_command(["sudo", "apt-get", "update"])
    run_command(["sudo", "apt-get", "install", "-y", "wget", "python3", "python3-pip"])
    print ("Dependencies installed successfully")
def create_directory():
    if not os.path.exists(agent_directory):
        os.makedirs(agent_directory)
        print ("Directory created successfully")
    else:
        print ("Directory already exists")
def download_agent():
     if os.path.exists(destination):
        print ("File already exists")
     else:
         print ("Downloading Agent....")
         subprocess.run(
         ["sudo", "wget", "-P", agent_directory, agent_url]
         )
         print ("GLPI agent downloaded successfully")

def install_agent():
    print ("Installing agent...")
    run_command(["sudo", "chmod", "+x", destination])
    result = subprocess.run(["sudo", destination],
                            input=(f"{glpi_server}\n"),
                            text=True
                             )
def configuring_agent():
    print ("Configuring the agent...")
    config_file = "/etc/glpi-agent/agent.cfg"
    with open(config_file, "a") as file:
         file.write(f"\nserver = {glpi_server}\n")
    print ("Agent configured successfully")
#Run Script
print ("========================================")
print ("     GLPI Agent Automation              ")
print ("========================================")
install_dependencies()
create_directory()
download_agent()
install_agent()
configuring_agent()
