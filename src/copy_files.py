import os, shutil, re


def list_files(current_node, current_path):
    file_list = []
    for node in current_node:
        try:
            if "__pycache__" in node or ".git" in node:
                continue
            file_list.extend(list_files(os.listdir(current_path + "/" + node),current_path + "/" + node))
        except NotADirectoryError:
            file_list.append(current_path + "/" + node)
    return file_list

def copy_content(current_path=".", target_content=None, new_location=None):
    if target_content == None:
        raise Exception("No valid target to copy")
    if new_location == None:
        raise Exception("No valid new location to copy to")
    
    file_list = list_files(os.listdir(current_path), current_path)
    for item in file_list:
        if item.find(target_content) != -1:
            print(f"Target: {target_content} is in directory")
            break
    else:
        print("There seems to be something missing")