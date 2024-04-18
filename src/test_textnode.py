import unittest
import textnode

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    node = TextNode("This is a text node", "bold")
    node_string = "TextNode(This is a text node, bold, None)"
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
    
    def test_repr(self):
        self.assertEqual(str(self.node), self.node_string)
        
    def test_split_nodes_delimiter(self):
        node = TextNode("This is text with a `code block` word", textnode.text_type_text)
        new_nodes = textnode.split_nodes_delimiter([node], "`", textnode.text_type_code)
        result = [

            TextNode("This is text with a ", textnode.text_type_text),
            TextNode("code block", textnode.text_type_code),
            TextNode(" word", textnode.text_type_text),
        ]
        self.assertEqual(new_nodes, result)
    
    def test_extrakt_markdown_images(self):
        test_text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        matches = [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")]
        self.assertEqual(textnode.extract_markdown_images(test_text), matches)
        
    def test_extrakt_markdown_links(self):
        test_text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        matches = [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]
        self.assertEqual(textnode.extract_markdown_links(test_text), matches)


if __name__ == "__main__":
    unittest.main()
