import unittest
import os
from copy_files import (
    list_files,
    copy_content,
)

class TestMain(unittest.TestCase):
    def test_list_files(self):
        current_path = "./"
        result = [
            './public/styles.css', './public/index.html', 
            './src/main.py', './src/copy_files.py', './src/inline_markdown.py', 
            './src/textnode.py', './src/test_copy_files.py', './src/test_htmlnode.py', 
            './src/test_markdown_blocks.py', './src/htmlnode.py', './src/test_textnode.py', 
            './src/test_markdown_html.py', './src/markdown_html.py', './src/test_inline_markdown.py', 
            './src/markdown_blocks.py', 
            './static/index.css', './static/images/FT4GU4M.png', 
            './server.py', 
            './test.sh', 
            './main.sh', 
            './README.md']
        self.assertEqual(list_files(os.listdir(current_path), current_path.rstrip("/")), result)

    def test_copy_content_target_error(self):
        try:
            copy_content(new_location="./public")
        except Exception as e:
            self.assertEqual(str(e), "No valid target to copy")
        else:
            raise Exception("Target shouldn't be valid")
        
    def test_copy_content_new_error(self):
        try:
            copy_content(target_content="./aaa")
        except Exception as e:
            self.assertEqual(str(e), "No valid new location to copy to")
        else:
            raise Exception("New location shouldn't be valid")
    
    def test_copy_target_missing(self):
        copy_content(target_content="./aaa", new_location="./public")

    def test_copy_content(self):
        copy_content(target_content="./static", new_location="./public")
