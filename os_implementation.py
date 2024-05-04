import os

# if u want to check the current directory
current_dir = os.getcwd()

# create new directory
path = r"C:\Users\gtush\Desktop\os"

# new folder name
name_of_new_folder = "New folder"

# Path of the new folder (combination of existing folder path and new folder name)
new_folder = os.path.join(path, name_of_new_folder)
if os.path.exists(new_folder):
    print("folder exits")
else:
    pass

# create multiple folder
# '''
# for i in range(11, 100):
#     name_of_new_folders = f"New folder {i}"
#     new_folder = os.path.join(path, name_of_new_folders)
#     if not os.path.exists(name_of_new_folders):
#         os.mkdir(new_folder)
#
#
# new_path = r"C:\Users\gtush\Desktop\ostut 11"
# for i in range(11, 100):
#     name_of_new_folders = f"New folder {i}"
#     current_name = os.path.join(new_path, name_of_new_folders)
#     new_name = os.path.join(new_path, f"tut_{i + 1}")
#
#     # Check if the directory exists before renaming
#     if os.path.exists(current_name):
#         os.rename(current_name, new_name)
#     else:
#         print(f"Directory '{current_name}' does not exist.")
# '''

new_path = r"C:\Users\gtush\Desktop\ostut 11"
content = os.listdir(new_path)
print("content")
for i in content:
    new_dir = new_path + rf"\tut_{i}"
    print(os.listdir(f"C:/Users/gtush/Desktop/ostut 11/{i}"))
