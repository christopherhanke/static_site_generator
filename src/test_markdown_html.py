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
        result =  ParentNode(
            "div", [
                ParentNode(
                    "p", [
                        LeafNode(None, "This is ", None),
                        LeafNode("b", "bolded", None), 
                        LeafNode(None, " paragraph", None)
                    ], None),
                ParentNode(
                    "p", [
                        LeafNode(None, "This is another paragraph with ", None),
                        LeafNode("i", "italic", None), 
                        LeafNode(None, " text and ", None), 
                        LeafNode("code", "code", None), 
                        LeafNode(None, " here\nThis is the same paragraph on a new line", None)
                    ], None), 
                ParentNode(
                    "ul", [
                        LeafNode("li", "This is a list", None),
                        LeafNode("li", "with items", None)
                    ], None)
                ], None)
        self.assertEqual(str(markdown_to_html_node(text)), str(result))

    def test_unordered_list_to_html(self):
        text = "* This is a **unordered** list\n* with some lines\n* of text to split"
        result = ParentNode("ul", [
            LeafNode("li", "This is a ", None), 
            LeafNode("b", "unordered", None), 
            LeafNode(None, " list", None), 
            LeafNode("li", "with some lines", None),
            LeafNode("li", "of text to split", None)
            ], None)
        self.assertEqual(str(unordered_list_to_html(text)), str(result))
    
    def test_ordered_list_to_html(self):
        text = "1. This is an ordered list\n2. with some lines\n3. of text to split"
        result = ParentNode("ol", [
            LeafNode("li", "This is an ordered list", None),
            LeafNode("li", "with some lines", None), 
            LeafNode("li", "of text to split", None)
            ], None)
        self.assertEqual(str(ordered_list_to_html(text)), str(result))
    
    def test_code_to_html(self):
        text = "```This is a code block. With **some** text.```"
        result = ParentNode("pre", [
            ParentNode("code", [
                LeafNode(None, "This is a code block. With ", None), 
                LeafNode("b", "some", None), 
                LeafNode(None, " text.", None)
                ], None)
            ], None)
        self.assertEqual(str(code_to_html(text)), str(result))
    
    def test_blockquote_to_html(self):
        text = "> This is a quote"
        result = ParentNode("blockquote", [
            LeafNode(None, "This is a quote", None)
            ], None)
        self.assertEqual(str(blockquote_to_html(text)), str(result))

    def test_blockquote_to_html_quotes(self):
        text = "> This is a quote\n> with two lines"
        result = ParentNode("blockquote", [
            LeafNode(None, "This is a quote\n", None),
            LeafNode(None, "with two lines", None)
            ], None)
        self.assertEqual(str(blockquote_to_html(text)), str(result))
    
    def test_header_to_html(self):
        text = "## This is a h2 Header"
        result = ParentNode("h2", [
            LeafNode(None, "This is a h2 Header", None)
            ], None)
        self.assertEqual(str(header_to_html(text)), str(result))
