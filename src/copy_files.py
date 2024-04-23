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
    # check target_content and new_location raising exceptions when None given
    if target_content == None:
        raise Exception("No valid target to copy")
    if new_location == None:
        raise Exception("No valid new location to copy to")
    
    #getting list of files
    file_list = list_files(os.listdir(current_path), current_path)
    
    target_list = []
    for item in file_list:
        if item.find(target_content) != -1:
            target_list.append(item)
    else:
        if target_list == []:
            raise Exception("There is no target")

    if os.path.isdir(new_location):
        shutil.rmtree(new_location)
        os.mkdir(new_location)
    else:
        os.mkdir(new_location)

    new_list = []
    for item in target_list:
        if not os.path.isfile(item):
            target_list.remove(item)
            continue
        new_list.append(shutil.copy(item, new_location))
    return new_list
    
