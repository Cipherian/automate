import shelve
import shutil
import os.path
import os
import glob
import sys
from pathlib import Path

data = {"name": "John", "age": 30, "email": "john@example.com"}
data2 = {"name": "Jane", "age": 25, "email": "jane@example.com"}

# Get the path to the script that's currently running
script_dir = os.path.dirname(__file__)

with shelve.open("data.db") as db:
    db["data"] = data


new_file_path = os.path.join(script_dir, "shelve_quiz.txt")


with open(new_file_path, "w") as f:
    f.write(str(data))

# shutil.copyfile("data.db", os.path.join(script_dir, "data2.db")) # copies file

files = os.listdir(script_dir)

files_2 = glob.glob(os.path.join(script_dir, "*.txt")) # finds all txt files in the directory and prints the route

p = Path(".")