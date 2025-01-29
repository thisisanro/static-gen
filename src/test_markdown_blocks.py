import unittest
from markdown_blocks import (
    markdown_to_blocks,
    block_to_block_type,
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
        text = "```This is a code text```"
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


if __name__ == "__main__":
    unittest.main()