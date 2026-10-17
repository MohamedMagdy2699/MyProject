#!/usr/bin/env python3
import subprocess
import os
import shutil

# installing rustdesk
rustdesk_url="https://github.com/rustdesk/rustdesk/releases/download/1.5.0/rustdesk-1.5.0-x86_64.deb"
rustdesk_directory="/tmp/rustdesk"
filename = os.path.basename(rustdesk_url)

def run_command(command):
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Error occurred while running command: {e}")
def make_directory(path):
    try:
        os.makedirs(path, exist_ok=True)
    except OSError as e:
        raise RuntimeError(f"Error occurred while creating directory {path}: {e}")

def main():
  if shutil.which("rustdesk") is None:
     #Make sure the rustdesk directory exists
     if os.path.isdir(rustdesk_directory):
       print(f"Directory {rustdesk_directory} already exists.")
     else:
       make_directory(rustdesk_directory)
     # Download the rustdesk package
     if not os.path.isfile(f"{rustdesk_directory}/{filename}") or os.path.getsize(f"{rustdesk_directory}/{filename}") == 0:    
       run_command(["wget", "-O", f"{rustdesk_directory}/{filename}", rustdesk_url])
     else:
       print(f"File {filename} already exists and is not empty. Skipping download.")
     if os.path.isfile(f"{rustdesk_directory}/{filename}") and os.path.getsize(f"{rustdesk_directory}/{filename}") > 0:
       run_command(["sudo", "apt", "install", "-y", f"{rustdesk_directory}/{filename}"])
  # Install the rustdesk package
  else:
      print("Rustdesk is already installed. Skipping installation.")


if __name__ == "__main__":
  try: 
      main()
  except Exception as e:
    raise RuntimeError(f"An error occurred: {e}")