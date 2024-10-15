import unittest

from textnode import TextNode,TextType
from htmlnode import LeafNode

class TestTextNodeToHTML(unittest.TestCase):

    def test_text_type(self):

        textnode=TextNode(textType=TextType.TEXT,text="hello")
        leafnode=LeafNode(value="hello")

        self.assertEqual(textnode.to_html_node(),leafnode)

    def test_bold_type(self):

        textnode=TextNode(textType=TextType.BOLD,text="hello")
        leafnode=LeafNode(tag="b",value="hello")

        self.assertEqual(textnode.to_html_node(),leafnode)

    def test_code_type(self):
        textnode=TextNode(textType=TextType.CODE,text="hello")

        self.assertEqual(textnode.to_html_node().to_html(),
                         "<code>hello</code>")

    def test_link_type(self):
        textnode=TextNode(textType=TextType.LINK,text="que viene LINK",url="www.link.com")

        self.assertEqual(textnode.to_html_node().to_html(),
                         "<a href=\"www.link.com\">que viene LINK</a>")

    def test_image_type(self):
        textnode=TextNode(textType=TextType.IMAGE,text="A photo of a bird",url="www.bird.com")

        self.assertEqual(textnode.to_html_node().to_html(),
                         "<img src=\"www.bird.com\" alt=\"A photo of a bird\"></img>")

if __name__ == "__main__":
    unittest.main()
