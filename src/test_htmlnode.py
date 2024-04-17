import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    node = HTMLNode()
    node_string = "HTMLNode(None, None, None, None)"
    node2 = HTMLNode(None, None, None, {"href": "https://www.google.com", "target": "_blank"})
    node2_props_html = ' href="https://www.google.com" target="_blank"'

    def test_str(self):
        self.assertEqual(str(self.node), self.node_string)
    
    def test_props_to_html(self):
        self.assertEqual(self.node2.props_to_html(), self.node2_props_html)
    
    def test_to_html(self):
        try:
            self.node.to_html()
        except NotImplementedError:
            pass

class TestLeafNode(unittest.TestCase):
    leaf1 = LeafNode("p", "This is a paragraph of text.")
    leaf1_string = "<p>This is a paragraph of text.</p>"
    leaf2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    leaf2_string = '<a href="https://www.google.com">Click me!</a>'

    def test_empty_node(self):
        try:
            leaf_empty = LeafNode()
        except ValueError:
            pass
    
    def test_to_html_1(self):
        self.assertEqual(self.leaf1.to_html(), self.leaf1_string)
    
    def test_to_html_2(self):
        self.assertEqual(self.leaf2.to_html(), self.leaf2_string)

if __name__ == "__main__":
    unittest.main()
