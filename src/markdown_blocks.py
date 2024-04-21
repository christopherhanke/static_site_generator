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
    if re.match(r'#+ (.+)', block):
        return block_type_heading
    
    # code
    elif re.match(r'```(.+)', block):
        return block_type_code
    
    # quote
    elif re.match(r'> (.+)', block):
        if not "\n" in block:
            return block_type_quote
        else:
            for line in block.split("\n"):
                if re.match(r'>(.+)', line):
                    continue
                else:
                    break
            else:
                return block_type_quote

    # unordered list
    elif re.match(r'\* (.*)', block) or re.match(r'- (.*)', block):
        if not "\n" in block:
            return block_type_unorderd_list
        else:
            for line in block.split("\n"):
                if re.match(r'\* (.*)', line) or re.match(r'- (.*)', line):
                    continue
                else:
                    break
            else:
                return block_type_unorderd_list

    # ordered list
    elif re.match(r'\d\. (.*)', block):
        if not "\n" in block:
            return block_type_ordered_list
        else:
            i = 1
            for line in block.split("\n"):
                if i == int((re.match(r'(\d)\. .*', line)).group(1)):
                    i +=1
                    continue
                break
            else:
                return block_type_ordered_list
            
    # paragraph (if none of the other)
    return block_type_paragraph
