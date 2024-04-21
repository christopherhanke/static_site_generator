import unittest
from htmlnode import (
    ParentNode,
    LeafNode
)
from markdown_html import (
    markdown_to_html_node,
    blockquote_to_html,
    unordered_list_to_html,
    ordered_list_to_html,
    code_to_html,
    header_to_html,
)


class TestMarkdownHTML(unittest.TestCase):
    def test_markdown_to_html_node(self):
        text = "This is **bolded** paragraph\n\n This is another paragraph with *italic* text and `code` here \nThis is the same paragraph on a new line\n\n\n* This is a list\n* with items"
        result =  None
        markdown_to_html_node(text)
        

    def test_unordered_list_to_html(self):
        text = "* This is a unordered list\n* with some lines\n* of text to split"
        result = ParentNode("ul", [LeafNode("li", "This is a unordered list", None), LeafNode("li", "with some lines", None), LeafNode("li", "of text to split", None)], None)
        self.assertEqual(str(unordered_list_to_html(text)), str(result))
    
    def test_ordered_list_to_html(self):
        text = "1. This is an ordered list\n2. with some lines\n3. of text to split"
        result = ParentNode("ol", [LeafNode("li", "This is an ordered list", None), LeafNode("li", "with some lines", None), LeafNode("li", "of text to split", None)], None)
        self.assertEqual(str(ordered_list_to_html(text)), str(result))
    
    def test_code_to_html(self):
        text = "```This is a code block.```"
        result = ParentNode("pre", [LeafNode("code", "This is a code block.", None)], None)
        self.assertEqual(str(code_to_html(text)), str(result))
    
    def test_blockquote_to_html(self):
        text = "> This is a quote"
        result = LeafNode("blockquote", "This is a quote")
        self.assertEqual(str(blockquote_to_html(text)), str(result))

    def test_blockquote_to_html_quotes(self):
        text = "> This is a quote\n> with two lines"
        result = LeafNode("blockquote", "This is a quote\nwith two lines")
        self.assertEqual(str(blockquote_to_html(text)), str(result))
    
    def test_header_to_html(self):
        text = "## This is a h2 Header"
        result = LeafNode("h2", "This is a h2 Header", None)
        self.assertEqual(str(header_to_html(text)), str(result))
