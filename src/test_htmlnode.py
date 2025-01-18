import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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
    
    def test_no_tag(self):
        node = LeafNode(None, "text")
        self.assertEqual(node.to_html(), "text")

    def test_with_tag(self):
        node = LeafNode("tag", "text")
        self.assertEqual(node.to_html(), "<tag>text</tag>")

    def test_with_props(self):
        node = LeafNode("tag", "text", {"href": "link.com"})
        self.assertEqual(node.to_html(), '<tag href="link.com">text</tag>')

    def test_nested_children(self):
        node = ParentNode("tag", [ParentNode("tag2", [LeafNode("tag3", "value")])])
        self.assertEqual(node.to_html(), "<tag><tag2><tag3>value</tag3></tag2></tag>")
    
    def test_multiple_children(self):
        node = ParentNode(
            "tag",
            [
                LeafNode("t", "v"),
                LeafNode("t2","v2"),
                LeafNode("t3","v3")
            ]
        )
        self.assertEqual(node.to_html(), "<tag><t>v</t><t2>v2</t2><t3>v3</t3></tag>")

    def test_no_children(self):
        node = ParentNode("tag", None)
        try:
            node.to_html()
            self.fail("ValueError should be raised")
        except ValueError as e:
            self.assertEqual(str(e), "ParentNode requires children data")

if __name__ == "__main__":
    unittest.main()