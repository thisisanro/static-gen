import unittest
from textnode import TextNode, TextType
from markdown_parser import split_nodes_delimiter

class TestMarkdownParser(unittest.TestCase):
    def test_split_nodes_code(self):
        node = TextNode("This is text with a `code block` word", TextType.NORMAL)
        splitted_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            splitted_nodes,
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.NORMAL),
            ]
        )
    
    def test_split_nodes_bold(self):
        node = TextNode("This is text with a **bold** word", TextType.NORMAL)
        splitted_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            splitted_nodes,
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("bold", TextType.BOLD),
                TextNode(" word", TextType.NORMAL),
            ]
        )

    def test_split_nodes_italic(self):
        node = TextNode("This is text with an *italic* word", TextType.NORMAL)
        splitted_node = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(
            splitted_node,
            [
                TextNode("This is text with an ", TextType.NORMAL),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.NORMAL),
            ]
        )
    
    def test_split_nodes_check_closing_delimiter(self):
        node = TextNode("This is text with an *italic word", TextType.NORMAL)
        with self.assertRaises(ValueError) as context:
            split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(str(context.exception), "Invalid Markdown syntax, closing delimiter is required")

    def test_split_nodes_multiple_delimiters(self):
        node = TextNode("This *is* text with a **bold** word", TextType.NORMAL)
        splitted_node = split_nodes_delimiter([node], "**", TextType.BOLD)
        splitted_node = split_nodes_delimiter(splitted_node, "*", TextType.ITALIC)
        self.assertEqual(
            splitted_node,
            [
                TextNode("This ", TextType.NORMAL),
                TextNode("is", TextType.ITALIC),
                TextNode(" text with a ", TextType.NORMAL),
                TextNode("bold", TextType.BOLD),
                TextNode(" word", TextType.NORMAL),
            ]
        )

if __name__ == "__main__":
    unittest.main()
