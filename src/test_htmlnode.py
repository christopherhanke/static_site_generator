import unittest

from htmlnode import HTMLNode

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

if __name__ == "__main__":
    unittest.main()
