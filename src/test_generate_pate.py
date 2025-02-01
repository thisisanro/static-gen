import unittest
from generate_page import(
    extract_title,
)


class TestGeneratePage(unittest.TestCase):
    def test_extract_title(self):
        markdown = (
            "Paragraph text\n\n"
            "# Heading\n\n"
            "## Heding 2"
        )
        self.assertEqual(extract_title(markdown), "Heading")

        markdown = markdown = (
            "  #    Extra spaces  \n\n"
            "Some text here"
        )
        self.assertEqual(extract_title(markdown), "Extra spaces")

        markdown = (
            "Paragraph text\n\n"
            "## Heading 2\n\n"
            "More text"
        )
        with self.assertRaises(ValueError):
            extract_title(markdown)