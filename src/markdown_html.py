import re
from htmlnode import ParentNode, LeafNode
from textnode import TextNode
from markdown_blocks import (
    block_type_paragraph,
    block_type_heading,
    block_type_code,
    block_type_quote,
    block_type_unorderd_list,
    block_type_ordered_list,
    markdown_to_blocks,
    block_to_block_type,
)


def markdown_to_html_node(markdown):
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
