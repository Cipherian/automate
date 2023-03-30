import os
import sys
import shutil



def create_files(filenames):
    file_dir = os.path.dirname(__file__)
    for filename in filenames:
        path = os.path.join(file_dir, filename)
        with open(path, "w") as f:
            f.write("hello world")
        print(f"created file {path}")


def create_directories(directory_hierarchy):
    path = os.getcwd()
    for directory_name in directory_hierarchy.split('/'):
        path = os.path.join(path, directory_name)
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"created directory {path}")
        else:
            print(f"directory {path} already exists")


if __name__ == "__main__":
    directory_hierarchy = sys.argv[1]
    filenames = sys.argv[1:]
    # create_files(filenames)
    create_directories(directory_hierarchy)