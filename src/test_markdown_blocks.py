import unittest
from markdown_blocks import (
    markdown_to_blocks,
    block_to_block_type,
    block_type_paragraph,
    block_type_heading,
    block_type_code,
    block_type_quote,
    block_type_unorderd_list,
    block_type_ordered_list,
    markdown_to_html,
    unordered_list_to_html
)
from htmlnode import (
    HTMLNode,
    LeafNode,
    ParentNode
)


class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        text = "This is **bolded** paragraph\n\n This is another paragraph with *italic* text and `code` here \nThis is the same paragraph on a new line\n\n\n* This is a list\n* with items"
        text_blocks = [
            "This is **bolded** paragraph",
            "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
            "* This is a list\n* with items",
        ]
        self.assertEqual(markdown_to_blocks(text), text_blocks)
    
    def test_block_to_blocktype_header(self):
        block = "## Test case header"
        self.assertEqual(block_to_block_type(block), block_type_heading)
    
    def test_block_to_blocktype_code(self):
        block = "```This is a code block```"
        self.assertEqual(block_to_block_type(block), block_type_code)
    
    def test_block_to_blocktype_quote(self):
        block = ">This is a quote line"
        self.assertEqual(block_to_block_type(block), block_type_quote)
    
    def test_block_to_blocktype_quotelines(self):
        block = ">This is a quote line\n>over two lines"
        self.assertEqual(block_to_block_type(block), block_type_quote)
    
    def test_block_to_blocktype_unordered(self):
        block = "* This a list\n* with some lines\n* of text"
        self.assertEqual(block_to_block_type(block), block_type_unorderd_list)
    
    def test_block_to_blocktype_ordered(self):
        block = "1. This an ordered list\n2. With some lines\n3. to check them"
        self.assertEqual(block_to_block_type(block), block_type_ordered_list)
    
    def test_block_to_blocktype_ordered_false(self):
        block = "1. This is an not so ordered list\n2. with some lines correct\n5. and some false"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

    
    def test_markdown_to_html(self):
        text = "This is **bolded** paragraph\n\n This is another paragraph with *italic* text and `code` here \nThis is the same paragraph on a new line\n\n\n* This is a list\n* with items"
        result =  None
        markdown_to_html(text)
        

    def test_unordered_list_to_html(self):
        text = "* This is a unordered list\n* with some lines\n* of text to split"
        result = ParentNode("ul", [LeafNode("li", "This is a unordered list", None), LeafNode("li", "with some lines", None), LeafNode("li", "of text to split", None)], None)
        
        self.assertEqual(str(unordered_list_to_html(text)), str(result))
    