import unittest
from textnode import TextNode, TextType
from markdown_parser import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes,
)

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

    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.NORMAL,
        )
        result = [
            TextNode("This is text with a link ", TextType.NORMAL),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.NORMAL),
            TextNode(
                "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
            ),
        ]
        self.assertEqual(split_nodes_link([node]), result)

    def test_split_nodes_image(self):
        node = TextNode(
            "This is text with a link ![image](https://www.image.dev) and ![image2](https://www.image2.dev)",
            TextType.NORMAL,
        )
        result = [
            TextNode("This is text with a link ", TextType.NORMAL),
            TextNode("image", TextType.IMAGE, "https://www.image.dev"),
            TextNode(" and ", TextType.NORMAL),
            TextNode(
                "image2", TextType.IMAGE, "https://www.image2.dev"
            ),
        ]
        self.assertEqual(split_nodes_image([node]), result)

    def test_split_nodes_single_image(self):
        node = TextNode("![image](https://image.com)", TextType.NORMAL)
        result = [
            TextNode("image", TextType.IMAGE, "https://image.com")
        ]
        self.assertListEqual(split_nodes_image([node]), result)
    
    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        self.assertEqual(
            text_to_textnodes(text),
            [
                TextNode("This is ", TextType.NORMAL),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.NORMAL),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.NORMAL),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.NORMAL),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.NORMAL),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ]
        )
        

if __name__ == "__main__":
    unittest.main()
