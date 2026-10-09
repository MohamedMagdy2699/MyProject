#!/usr/bin/env python3

#Modules
import urllib.request
import os
import subprocess
#Variables
agent_url="https://github.com/glpi-project/glpi-agent/releases/download/1.21/glpi-agent-1.21-with-snap-linux-installer.pl"
agent_directory="/tmp/glpi-agent"
#Download GLPI Agent

filename = os.path.basename(agent_url)
destination = os.path.join(agent_directory, filename)

# functions
def download_agent():
     print ("Downloading Agent....")
     subprocess.run(
      ["sudo", "wget", "-p", "agent_directory=", agent_url]
     )
     print ("GLPI agent downloaded successfully")
download_agent()
