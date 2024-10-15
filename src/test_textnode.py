import unittest

from textnode import TextNode,TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("Now with a url", TextType.TEXT, "https://url")
        node2 = TextNode("Now with a url", TextType.TEXT, "https://url")
        self.assertEqual(node, node2)

    def test_eq3(self):
        node = TextNode("")
        node2 = TextNode("")
        self.assertEqual(node, node2)

    def test_eq4(self):
        node = TextNode("a", url="")
        node2 = TextNode("a", url="")
        self.assertEqual(node, node2)

    def test_noteq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node,node2)

    def test_noteq2(self):
        node = TextNode("", TextType.ITALIC)
        node2 = TextNode("", TextType.BOLD)
        self.assertNotEqual(node,node2)

    def test_noteq3(self):
        node = TextNode("This is a text node",TextType.BOLD, "url1")
        node2 = TextNode("This is a text node",TextType.BOLD, "url2")
        self.assertNotEqual(node,node2)

    def test_noteq4(self):
        node = TextNode("text1", url="")
        node2 = TextNode("text2", url="")
        self.assertNotEqual(node,node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD, "url1")
        self.assertEqual(str(node),"TextNode(This is a text node, bold, url1)")


if __name__ == "__main__":
    unittest.main()
