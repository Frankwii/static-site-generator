import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node=HTMLNode(props={"href": "https://www.google.com", "target": "_blank",})

        self.assertEqual(node.props_to_html()," href=\"https://www.google.com\" target=\"_blank\"")

    def test_eq2(self):
        node=HTMLNode(props={})

        self.assertEqual(node.props_to_html(),"")

    def test_eq3(self):
        node=HTMLNode()

        self.assertEqual(node.props_to_html(),"")

if __name__ == "__main__":
    unittest.main()
