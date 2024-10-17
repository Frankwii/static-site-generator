import unittest

from node_parser import split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_text_nodes
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

    def test_reading_links(self):
        node=TextNode("This contains [a link](www.link.com)")
        inputs=[node]
        expectedOutput=[TextNode("This contains "),
                        TextNode("a link",url="www.link.com",textType=TextType.LINK)]
        actualOutput=split_nodes_link(inputs)

        self.assertEqual(actualOutput,expectedOutput)

    def test_reading_images(self):
        node1=TextNode("This contains ![an image](www.photo.com) hellow and ![another im](age) wassup")
        node2=TextNode("Some other ![an image](www.photo.com)")
        node3=TextNode("![]() an empty image")
        node4=TextNode("No images *here*")
        inputs=[node1,node2,node3,node4]
        
        expectedOutput=[TextNode("This contains "),
                TextNode("an image",url="www.photo.com",textType=TextType.IMAGE),
                TextNode(" hellow and "),
                TextNode("another im",url="age",textType=TextType.IMAGE),
                TextNode(" wassup"),
                TextNode("Some other "),
                TextNode("an image",url="www.photo.com",textType=TextType.IMAGE),
                TextNode(" an empty image"),
                TextNode("No images *here*")
                ]

        actualOutput=split_nodes_image(inputs)

        self.assertEqual(actualOutput,expectedOutput)

    def test_text_to_textnodes(self):
        testinput="This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

        expectedOutput=[
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                ]

        actualOutput=text_to_text_nodes(testinput)
        self.assertEqual(actualOutput,expectedOutput)


if __name__=="__main__":
    unittest.main()
