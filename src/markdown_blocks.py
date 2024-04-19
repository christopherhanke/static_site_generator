import re

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unorderd_list = "unordered_list"
block_type_ordered_list = "ordered_list"


def markdown_to_blocks(markdown):
    lines = markdown.splitlines()
    new_lines = []
    for line in lines:
        new_lines.append((line.lstrip(" ")).rstrip(" "))
    
    new_block = ""
    new_blocks = []
    for line in new_lines:
        if line != "":
            if new_block != "":
                new_block += "\n"
            new_block += line
        else:
            if new_block != "":
                new_blocks.append(new_block)
                new_block = ""
    if new_block != "":
        new_blocks.append(new_block)

    return new_blocks


def block_to_block_type(block):
    
    # heading
    
    # code

    # quote

    # unordered list

    # ordered list

    # paragraph (if none of the other)

    pass