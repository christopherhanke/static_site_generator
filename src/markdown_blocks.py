import re
from htmlnode import HTMLNode, ParentNode, LeafNode

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


def markdown_to_html(markdown):
    md_blocks = markdown_to_blocks(markdown)
    
    # end of recursion, when markdwon is empty

    block_types = []
    for block in md_blocks:
        block_types.append(block_to_block_type(block))
    
    if len(md_blocks) != len(block_types):
        raise Exception("Invalid markdown, count of blocks does not equal count of block_type")
    
    items = []
    print()
    for block, block_type in zip(md_blocks, block_types):
        print(f"Block: {block}")
        if block_type == block_type_quote:
            blockquote_to_html(block)
        elif block_type == block_type_unorderd_list:
            items.append(unordered_list_to_html(block))
        elif block_type == block_type_ordered_list:
            ordered_list_to_html(block)
        elif block_type == block_type_heading:
            header_to_html(block)
        elif block_type == block_type_paragraph:
            LeafNode("p", block)

    pass

def blockquote_to_html(markdown):
    # return LeafNode with type blockquote and and quote-text
    lines = markdown.split("\n")
    new_line = ""
    for i in range(len(lines)):
        new_line += lines[i].lstrip("> ")
        if i < len(lines)-1:
            new_line += "\n"
    return LeafNode("blockquote", new_line)

def unordered_list_to_html(markdown):
    # return ParentNode with type unordered list and list elements in children
    # split lines in markdown to get list items
    lines = markdown.split("\n")
    items = []
    for line in lines:
        items.append(LeafNode("li", line.lstrip("* ")))
    return ParentNode("ul", items)

def ordered_list_to_html(markdown):
    # return ParentNode with type ordered list and list elements in children
    lines = markdown.split("\n")
    items = []
    for line in lines:
        item = re.match(r'\d\. (.*)', line).group(1)
        items.append(LeafNode("li", item))
    return ParentNode("ol", items)

def code_to_html(markdown):
    # return ParentNode with type code and code-text in children
    code_block = (markdown.lstrip("` ")).rstrip("` ")
    return ParentNode("pre", [LeafNode("code", code_block),])

def header_to_html(markdown):
    #return HTMLNode with type h* and header-text
    matches = re.match(r'(#+) (.*)', markdown)
    header = (matches.group(1)).count("#")
    line = matches.group(2)
    return LeafNode(f"h{header}", line)
