import unittest
from markdown_blocks import (
    markdown_to_blocks,
    block_to_block_type,
    markdown_to_html_node,
)


class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        text = (
            "# This is a heading\n\n"
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n"
            "* This is the first list item in a list block\n"
            "* This is a list item\n"
            "* This is another list item"
        )
        blocks = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n"
            "* This is a list item\n"
            "* This is another list item",
        ]
        self.assertEqual(markdown_to_blocks(text), blocks)

    def test_block_to_block_type_heading(self):
        text = "# This is a heading text"
        self.assertEqual(block_to_block_type(text), "heading")

    def test_block_to_block_type_code(self):
        text = "```\nThis is a code text\n```"
        self.assertEqual(block_to_block_type(text), "code")

    def test_block_to_block_type_quote(self):
        text = (
            "> quote line one\n"
            "> quote line two\n"
            "> quote line three"
        )
        self.assertEqual(block_to_block_type(text), "quote")
    
    def test_block_to_block_type_unordered(self):
        text = (
            "* This is unordered block line\n"
            "* This is unordered block line two\n"
            "* This is unordered block line three"
        )
        self.assertEqual(block_to_block_type(text), "unordered_list")

    def test_block_to_block_type_ordered(self):
        text = (
            "1. first line\n"
            "2. second line\n"
            "3. third line"
        )
        self.assertEqual(block_to_block_type(text), "ordered_list")

    def test_block_to_block_type_paragraph(self):
        text = (
            "This is a pargrapgh\n"
            "and the second line of it"
        )
        self.assertEqual(block_to_block_type(text), "paragraph")

    def test_markdown_to_html_paragraph(self):
        markdown = "This is a paragraph with **bold** text."
        html_node = markdown_to_html_node(markdown)
        self.assertEqual(
            "<div><p>This is a paragraph with <b>bold</b> text.</p></div>",
            html_node.to_html()
        )
    def test_markdown_to_html_heading(self):
        markdown = "## Heading"
        html_node = markdown_to_html_node(markdown)
        self.assertEqual(
            "<div><h2>Heading</h2></div>",
            html_node.to_html()
        )

    def test_markdown_to_html_unordered_list(self):
        markdown = "* Item 1\n* Item 2"
        html_node = markdown_to_html_node(markdown)
        self.assertEqual(
            "<div><ul><li>Item 1</li><li>Item 2</li></ul></div>",
            html_node.to_html()
        )

    def test_markdown_to_html_ordered_list(self):
        markdown = "1. First\n2. Second"
        html_node = markdown_to_html_node(markdown)
        self.assertEqual(
            "<div><ol><li>First</li><li>Second</li></ol></div>",
            html_node.to_html()
        )

    def test_markdown_to_html_code(self):
        markdown = "```\ndef test():\n    pass\n```"
        html_node = markdown_to_html_node(markdown)
        self.assertEqual(
            "<div><pre><code>def test():\n    pass</code></pre></div>",
            html_node.to_html()
        )

    def test_markdown_to_html_quote(self):
        markdown = """
> This is a
> blockquote block

this is paragraph text

""" 
        html_node = markdown_to_html_node(markdown)
        self.assertEqual(
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
            html_node.to_html()
        )


if __name__ == "__main__":
    unittest.main()