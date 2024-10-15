import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("Now with a url", "plain", "https://url")
        node2 = TextNode("Now with a url", "plain", "https://url")
        self.assertEqual(node, node2)

    def test_eq3(self):
        node = TextNode("", "")
        node2 = TextNode("", "")
        self.assertEqual(node, node2)

    def test_eq4(self):
        node = TextNode("a", "","")
        node2 = TextNode("a", "","")
        self.assertEqual(node, node2)

    def test_noteq(self):
        node = TextNode("This is a text node", "italic")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node,node2)

    def test_noteq2(self):
        node = TextNode("", "italic")
        node2 = TextNode("", "bold")
        self.assertNotEqual(node,node2)

    def test_noteq3(self):
        node = TextNode("This is a text node", "bold", "url1")
        node2 = TextNode("This is a text node", "bold", "url2")
        self.assertNotEqual(node,node2)

    def test_noteq4(self):
        node = TextNode("text1", "", "")
        node2 = TextNode("text2", "", "")
        self.assertNotEqual(node,node2)


if __name__ == "__main__":
    unittest.main()
