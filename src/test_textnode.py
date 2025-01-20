import unittest
from textnode import TextNode, TextType, text_node_to_html_node

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

    def test_text_to_html_normal(self):
        text_node = TextNode("text", TextType.NORMAL)
        html_node = text_node_to_html_node(text_node)
        assert html_node.tag is None
        assert html_node.value == "text"
        assert html_node.props is None

    def test_text_to_html_link(self):
        text_node = TextNode("text", TextType.LINK, url="google.com")
        html_node = text_node_to_html_node(text_node)
        assert html_node.tag == "a"
        assert html_node.value == "text"
        assert html_node.props == {"href": "google.com"}

    def test_text_to_html_image(self):
        text_node = TextNode("text", TextType.IMAGE, url="image.com")
        html_node = text_node_to_html_node(text_node)
        assert html_node.tag == "img"
        assert html_node.value == ""
        assert html_node.props == {"src": "image.com", "alt": "text"}

if __name__ == "__main__":
    unittest.main()