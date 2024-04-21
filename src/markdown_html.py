import re
from inline_markdown import text_to_textnodes
from htmlnode import ParentNode, LeafNode
from textnode import TextNode, text_node_to_html_node
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
    # make list of markdown blocks and list of markdown types
    md_blocks = markdown_to_blocks(markdown)
    md_block_types = []
    for block in md_blocks:
        md_block_types.append(block_to_block_type(block))
    if len(md_blocks) != len(md_block_types):
        raise Exception("Invalid markdown, count of blocks does not equal count of block_type")
    
    # print(f"md_blocks: {md_blocks}\nmd_block_types: {md_block_types}")

    # check block type and put new Node accordingly into list of items
    items = []
    for block, block_type in zip(md_blocks, md_block_types):
        if block_type == block_type_quote:
            items.append(blockquote_to_html(block))
        elif block_type == block_type_unorderd_list:
            items.append(unordered_list_to_html(block))
        elif block_type == block_type_ordered_list:
            items.append(ordered_list_to_html(block))
        elif block_type == block_type_code:
            continue
        elif block_type == block_type_heading:
            continue
        elif block_type == block_type_paragraph:
            items.append(paragraph_to_html(block))
        # print(f"{block}, {block_type}")
        # print(f"items: {items}")
    # print(f"items: {items}")
    return ParentNode("div", items)

def blockquote_to_html(markdown):
    # return Parentnode of type blockquote
    # strip text of leading ">" as markdown for quote
    lines = markdown.split("\n")
    text_nodes = []
    html_nodes = []
    for i in range(len(lines)):
        stripped_text = lines[i].lstrip("> ")
        if i < len(lines)-1:
            stripped_text += "\n"
        text_nodes.extend(text_to_textnodes(stripped_text))
    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))
    return ParentNode("blockquote", html_nodes)

def unordered_list_to_html(markdown):
    # return ParentNode of type unordered list and list elements in children
    # split lines in markdown to get list items
    lines = markdown.split("\n")
    html_nodes = []
    for i in range(len(lines)):
        text_nodes = []
        stripped_text = lines[i].lstrip("*- ")
        text_nodes.extend(text_to_textnodes(stripped_text))
        for j in range(len(text_nodes)):
            html_node = text_node_to_html_node(text_nodes[j])
            if j == 0:
                html_node.tag = "li"
            html_nodes.append(html_node)
    return ParentNode("ul", html_nodes)    

def ordered_list_to_html(markdown):
    # return ParentNode with type ordered list and list elements in children
    # split lines of markdown text
    lines = markdown.split("\n")
    html_nodes = []
    for line in lines:
        text_nodes = []
        # search text after enumartion and make it a Textnode
        stripped_text = re.match(r'\d\. (.*)', line).group(1)
        text_nodes.extend(text_to_textnodes(stripped_text))
        # only first element in line gets "li" type for listing
        for j in range (len(text_nodes)):
            html_node = text_node_to_html_node(text_nodes[j])
            if j == 0:
                html_node.tag = "li"
            html_nodes.append(html_node)
    return ParentNode("ol", html_nodes)

def code_to_html(markdown):
    # return ParentNode with type code and code-text in children
    stripped_text = (markdown.lstrip("` ")).rstrip("` ")
    text_nodes = text_to_textnodes(stripped_text)
    html_nodes = []
    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))
    return ParentNode("pre", [ParentNode("code", html_nodes)])

def header_to_html(markdown):
    #return HTMLNode with type h* and header-text
    matches = re.match(r'(#+) (.*)', markdown)
    header = (matches.group(1)).count("#")
    line = matches.group(2)
    text_nodes = text_to_textnodes(line)
    html_nodes = []
    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))
    return ParentNode(f"h{header}", html_nodes)

def paragraph_to_html(markdown):
    # return Parentnode of type paragraph
    text_nodes = text_to_textnodes(markdown)
    html_nodes = []
    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))
    return ParentNode("p", html_nodes)