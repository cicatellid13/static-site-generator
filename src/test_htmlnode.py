import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        node = HTMLNode(
            tag="p",
            value="this is paragraph text",
            children=[
                HTMLNode(tag="p", value="more text"),
                HTMLNode(tag="p", value="even more text")
            ],
            props={
                "href": "https://www.google.com",
                "target": "_blank",
            }
        )
        result = node.props_to_html()
        self.assertEqual(result, " href=\"https://www.google.com\" target=\"_blank\"")
    

    def test_props_to_html_empty(self):
        node = HTMLNode(props={})
        result = node.props_to_html()
        self.assertEqual(result, "") 
    

    def test_no_children(self):
        node = HTMLNode(tag="p", value="just text")
        self.assertIsNone(node.children)
    

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    
    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(tag=p, value=What a strange world, children=None, props={'class': 'primary'})",
        )


if __name__ == "__main__":
    unittest.main()

