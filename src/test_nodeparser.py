import unittest

from node_parser import split_nodes_delimiter
from textnode import TextType,TextNode

class TestNodeParser(unittest.TestCase):
    def test_splitting_code(self):
        node = TextNode(text="This is text with a `code block` word", textType=TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(new_nodes, [TextNode(text="This is text with a ",textType=TextType.TEXT),
                                     TextNode(text="code block",textType=TextType.CODE),
                                     TextNode(text=" word", textType=TextType.TEXT)])

    def test_splitting_bold(self):
        node = TextNode(text="This is text with a __bold__ word", textType=TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "__", TextType.BOLD)

        self.assertEqual(new_nodes, [TextNode(text="This is text with a ",textType=TextType.TEXT),
                                     TextNode(text="bold",textType=TextType.BOLD),
                                     TextNode(text=" word", textType=TextType.TEXT)])

    def test_splitting_italic(self):
        node = TextNode(text="This is text with *two* words *italic*", textType=TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)

        self.assertEqual(new_nodes, [TextNode(text="This is text with ",textType=TextType.TEXT),
                                     TextNode(text="two",textType=TextType.ITALIC),
                                     TextNode(text=" words "),
                                     TextNode(text="italic", textType=TextType.ITALIC)
                                     ])

    def test_multiple_splittings(self):
        node1 = TextNode(text="This is text with a __bold__ word", textType=TextType.TEXT)
        node2 = TextNode(text="This is text with __bold__ *two* words *italic*", textType=TextType.TEXT)
        old_nodes=[node1,node2]

        new_nodes = split_nodes_delimiter(old_nodes, "__", TextType.BOLD)
        new_new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)

        self.assertEqual(new_new_nodes,
                                    [TextNode(text="This is text with a ",textType=TextType.TEXT),
                                     TextNode(text="bold",textType=TextType.BOLD),
                                     TextNode(text=" word", textType=TextType.TEXT),
                                     TextNode(text="This is text with ",textType=TextType.TEXT),
                                     TextNode(text="bold",textType=TextType.BOLD),
                                     TextNode(text=" "),
                                     TextNode(text="two",textType=TextType.ITALIC),
                                     TextNode(text=" words "),
                                     TextNode(text="italic", textType=TextType.ITALIC)
                                     ])

    def test_invalid_syntax(self):
        with self.assertRaises(SyntaxError):
            node=TextNode(text="This is a text with no closing **bold")
            new_nodes=split_nodes_delimiter([node],"**",TextType.BOLD)

    def test_empty_node(self):
        nodes=[TextNode("")]
        new_nodes=split_nodes_delimiter(nodes,delimiter="*",text_type=TextType.ITALIC)
        self.assertEqual(new_nodes,[])

    # def test_reading_links(self):
    #     node=TextNode("This contains [a link](www.link.com)"),



if __name__=="__main__":
    unittest.main()
