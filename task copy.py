import os
import requests
import shutil
from datetime import datetime

# Creating directory named after my first and last name
first_name = "catherine"  
last_name = "gyamfi"    
directory_name = f"{first_name}_{last_name}"
os.makedirs(directory_name, exist_ok=True)

directory_name = "catherine_gyamfi"
if os.path.exists(directory_name):
    try:
        shutil.rmtree(directory_name)
        print(f"Directory '{directory_name}' has been removed successfully.")
    except Exception as e:
        print(f"Error: {e}")
#Downloading file from github
download_folder = "catherine gyamfi"
if not os.path.exists(download_folder):
    os.makedirs(download_folder)
    print(f"Directory '{download_folder}' created.")

local_file_path = os.path.join(download_folder, "catherine_gyamfi.txt")

url = "https://raw.githubusercontent.com/sdg000/pydevops_intro_lab/main/change_me.txt"
response = requests.get(url)

if response.status_code == 200:
    print("File successfully downloaded.")
    with open(local_file_path, 'wb') as file:
        file.write(response.content)
    print("File saved successfully.")
else:
    print(f"Failed to download file. Status code: {response.status_code}")

#user input and timestamp
user_input = input("Describe what you have learned so far in a sentence: ")
now = datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")

with open(local_file_path, "w") as file:
    file.write(user_input + "\n")
    file.write(f"Last modified on: {current_time}\n")
print("File successfully modified.")

with open(local_file_path, "r") as file:  
    content = file.read()
print("\nYou Entered:")  
print(content)
