import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    node = TextNode("This is a text node", "bold")
    node2 = TextNode("This is a text node", "bold")
    node3 = TextNode("This is another text node", "bold", "https://boot.dev")

    def test_eq(self):
        self.assertEqual(self.node, self.node2)
    
    def test_not_eq(self):
        self.assertNotEqual(self.node, self.node3)
    
    def test_url_none(self):
        self.assertEqual(self.node.url, None)
    
    def test_url_not_none(self):
        self.assertNotEqual(self.node3.url, None)
        

if __name__ == "__main__":
    unittest.main()
