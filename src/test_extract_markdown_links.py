import unittest
from functions.extract_markdown_links import extract_markdown_links, extract_markdown_images



class TestExtractMarkdownLinks(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![picture](https://a-website-dot-com.com) with other text over here"
        )
        self.assertListEqual([("picture", "https://a-website-dot-com.com")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with an [facebook](https://awholefacebook.com) with other text over here"
        )
        self.assertListEqual([("facebook", "https://awholefacebook.com")], matches)
    
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with an [facebook](https://awholefacebook.com) with this too [facebookie](https://awholeotherfacebook.com)"
        )
        self.assertListEqual([("facebook", "https://awholefacebook.com"), ("facebookie", "https://awholeotherfacebook.com")], matches)
