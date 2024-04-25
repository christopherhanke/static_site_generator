import unittest

from generate_page import (
    extract_title,
    generate_page,
)

class TestGeneratePage(unittest.TestCase):
    def test_extract_title(self):
        markdown = "# This is a header"
        result = "This is a header"
        self.assertEqual(extract_title(markdown), result)
    
    def test_extract_no_title(self):
        e = Exception("There is no header")
        markdown = "This is no header"
        try:
            extract_title(markdown)
        except Exception as ex:
            self.assertEqual(str(ex), str(e))
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_generate_page(self):
        generate_page("./content/index.md", "./template.html", "./public/index.html")


        