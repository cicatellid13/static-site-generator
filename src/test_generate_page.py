import unittest

from functions.generate_page import generate_page

class TestGeneratePage(unittest.TestCase):
    def test_generate_page_find_html(self):
        f_path = "./content/index.md"
        t_path = "./template.html"
        d_path = "./"
        page = generate_page(f_path, t_path, d_path)

        self.assertIn("html", page)
    
    def test_generate_page_find_header(self):
        f_path = "./content/index.md"
        t_path = "./template.html"
        d_path = "./"
        page = generate_page(f_path, t_path, d_path)

        self.assertIn("<h1>Tolkien Fan Club</h1>", page)
    
    def test_generate_page_find_list(self):
        f_path = "./content/index.md"
        t_path = "./template.html"
        d_path = "./"
        page = generate_page(f_path, t_path, d_path)

        self.assertIn("<li>Gandalf</li>", page)