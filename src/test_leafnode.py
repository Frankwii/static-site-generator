import unittest

from leafnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_propstohtml(self):
        node=LeafNode(props={"href": "https://www.google.com", "target": "_blank"},value="Hello")

        self.assertEqual(node.props_to_html()," href=\"https://www.google.com\" target=\"_blank\"")

    def test_selftohtml(self):

        node=LeafNode(tag="p", value="This is a paragraph of text.")

        self.assertEqual(node.to_html(),"<p>This is a paragraph of text.</p>")

    def test_tohtml2(self):
        node=LeafNode(tag="a", value="Click me!", props={"href": "https://www.google.com"})

        self.assertEqual(node.to_html(),"<a href=\"https://www.google.com\">Click me!</a>")


    def test_raisesError(self):
        with self.assertRaises(TypeError):
            LeafNode(value=2)
        
    def test_raisesError2(self):
        with self.assertRaises(TypeError):
            LeafNode(value=None)


if __name__ == "__main__":
    unittest.main()
