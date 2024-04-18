import re
from htmlnode import HTMLNode, LeafNode, ParentNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, otherNode):
        return (
            self.text == otherNode.text
            and self.text_type == otherNode.text_type
            and self.url == otherNode.url
        )
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node):
    if text_node.text_type == text_type_text:
        return LeafNode(None, text_node.text)
    if text_node.text_type == text_type_bold:
        return LeafNode("b", text_node.text)
    if text_node.text_type == text_type_italic:
        return LeafNode("i", text_node.text)
    if text_node.text_type == text_type_code:
        return LeafNode("code", text_node.text)
    if text_node.text_type == text_type_link:
        return LeafNode("a", text_node.text, {"href=": text_node.url})
    if text_node.text_type == text_type_image:
        return LeafNode("img", "", {"src=": text_node.url, "alt=": text_node.text})
    raise Exception(f"Invalid text type: {text_node.text_type}")


def split_nodes_image(old_nodes):
    image_tup = extract_markdown_images(old_nodes.text)
    if image_tup == []:
        return old_nodes
    
    last_node = old_nodes
    new_nodes = []
    for i in range(len(image_tup)):
        text_split = last_node.text.split(f"![{image_tup[i][0]}]({image_tup[i][1]})", 1)
        if len(text_split[0]) != 0:
            new_nodes.append(TextNode(text_split[0], old_nodes.text_type))
        new_nodes.append(TextNode(image_tup[i][0], text_type_image, image_tup[i][1]))
        if i == len(image_tup)-1:
            if len(text_split[1]) != 0:
                new_nodes.append(TextNode(text_split[1], old_nodes.text_type))
        else:
            last_node = TextNode(text_split[1], old_nodes.text_type)
    
    return new_nodes


def split_nodes_link(old_nodes):
    link_tup = extract_markdown_links(old_nodes.text)
    if link_tup == []:
        return old_nodes
    
    last_node = old_nodes
    new_nodes = []
    for i in range (len(link_tup)):
        text_split = last_node.text.split(f"[{link_tup[i][0]}]({link_tup[i][1]})")
        if len(text_split[0]) != 0:
            new_nodes.append(TextNode(text_split[0], old_nodes.text_type))
        new_nodes.append(TextNode(link_tup[i][0], text_type_link, link_tup[i][1]))
        if i == len(link_tup)-1:
            if (len(text_split[1])) != 0:
                new_nodes.append(TextNode(text_split[1], old_nodes.text_type))
        else:
            last_node = TextNode(text_split[1], old_nodes.text_type)
    
    return new_nodes

    pass


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if not isinstance(node, TextNode):
            new_nodes.append(split_nodes_delimiter(node, delimiter, text_type))
        else:
             line = node.text.split(delimiter)
             for i in range(0, len(line)):
                if i % 2 == 0:
                     new_nodes.append(TextNode(line[i], node.text_type))
                else:             
                    new_nodes.append(TextNode(line[i], text_type))
    return new_nodes 

def extract_markdown_images(text):
    matches = re.findall(r'!\[(.*?)\]\((.*?)\)', text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r'\[(.*?)\]\((.*?)\)', text)
    return matches
