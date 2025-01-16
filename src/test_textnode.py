import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_url_ineq(self):
        node = TextNode("any text", TextType.BOLD, url="http://example1.com")
        node2 = TextNode("any text", TextType.BOLD, url="http://example2.com")
        self.assertNotEqual(node, node2)

    def test_text_ineq(self):
        node = TextNode("first text", TextType.BOLD)
        node2 = TextNode("second text", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_text_types(self):
        node = TextNode("any text", TextType.BOLD)
        node2 = TextNode("any text", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    
    def test_url_none(self):
        node1 = TextNode("any text", TextType.BOLD, url="http://example.com")
        node2 = TextNode("any text", TextType.BOLD)
        self.assertNotEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()