import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("tag", "value", None, {"id": "link", "id2": "link2"})
        self.assertEqual(node.props_to_html(), ' id="link" id2="link2"')

    def test_props_to_html_none(self):
        node = HTMLNode("tag", "value", None, None)
        self.assertEqual(node.props_to_html(), "")
    
    def test_repr(self):
        node = HTMLNode("tag", "value", None, {"id": "link", "id2": "link2"})
        self.assertEqual(
            node.__repr__(),
            "HTMLNode\n"
            "tag: tag\n"
            "value: value\n"
            "children: None\n"
            "props: {'id': 'link', 'id2': 'link2'}"
        )

if __name__ == "__main__":
    unittest.main()