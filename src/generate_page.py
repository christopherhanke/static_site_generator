import os, re
from markdown_html import (
    markdown_to_html_node,
)

def extract_title(markdown_text):
    lines = markdown_text.split("\n")
    header = ""
    for line in lines:
        if re.match(r'# (.+)', line) and line.startswith("# "):
            header = re.match(r'# (.+)', line).group(1)
            break
    if header == "":
        raise Exception("There is no header")
    return header


def generate_page(from_path, template_path, dest_path):
    if not os.path.isfile(from_path):
        raise FileNotFoundError("Invalid path to copy from")
    if not os.path.isfile(template_path):
        raise FileNotFoundError(f"Invalid template path")
    
    
    print(f"Generating page from '{from_path}' to '{dest_path}' using '{template_path}'.")

    read_data = None
    with open(from_path) as file:
        read_data = file.read()
    
    html_data = markdown_to_html_node(read_data).to_html()
    title = extract_title(read_data)

    with open(template_path) as file:
        html_template = file.read()
    
    html_template = html_template.replace("{{ Title }}", title)
    html_template = html_template.replace("{{ Content }}", html_data)

    if not os.path.isdir(os.path.dirname(dest_path)):
        print(f"Destionation path didn't exsit.\nCreating destination...\n")
        os.makedirs(os.path.dirname(dest_path))
        print(f"'{dest_path}' created")
    
    if not os.path.isfile(dest_path):
        with open(dest_path, mode="x") as new_file:
            new_file.write(html_template)
    else:
        print(f"\nFile at {dest_path} already exists.\n")
    pass