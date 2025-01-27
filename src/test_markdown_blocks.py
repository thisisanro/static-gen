import unittest
from markdown_blocks import (
    markdown_to_blocks,
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


if __name__ == "__main__":
    unittest.main()