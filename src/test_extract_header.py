import unittest

from functions.extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def text_extract_title_with_header(self):
        md = """
# this is the header
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

    """
        self.assertEqual(extract_title(md), "this is the header")
    
    def text_extract_no_title(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

    """
        self.assertEqual(extract_title(md), "no title")
    
    def text_extract_multiple_headings(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

# this is the title
## this is not

This is another paragraph with _italic_ text and `code` here

    """
        self.assertEqual(extract_title(md), "this is the title")