import unittest
from textnode import TextNode, TextType
from markdown_parser import split_nodes_delimiter, extract_markdown_images, extract_markdown_links

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

    def test_extract_links(self):
        input = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        output = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(extract_markdown_links(input), output)

    def test_extract_images(self):
        input = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        output = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(extract_markdown_images(input), output)
    
    def test_extract_links_empty(self):
        self.assertEqual(extract_markdown_links(""), [])
    
    def test_extract_links_no_link(self):
        input = "Text without [link]"
        self.assertEqual(extract_markdown_links(input), [])


if __name__ == "__main__":
    unittest.main()
