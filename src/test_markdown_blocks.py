import unittest
from markdown_blocks import (
    markdown_to_blocks,
)

class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        text = "This is **bolded** paragraph\n\n This is another paragraph with *italic* text and `code` here \nThis is the same paragraph on a new line\n\n* This is a list\n* with items"
        text_blocks = [
            "This is **bolded** paragraph",
            "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
            "* This is a list\n* with items",
        ]
        self.assertEqual(markdown_to_blocks(text), text_blocks)