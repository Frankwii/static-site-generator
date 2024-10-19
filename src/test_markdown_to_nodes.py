import unittest
from htmlnode import ParentNode, LeafNode
from markdown_parser import block_to_htmlnode

class TestMarkdownToNodes(unittest.TestCase):
    def test_block_to_nodes_paragraph(self):
        inputblock="This is a *text* containing **italic** and __bold__"
        actualOutput=block_to_htmlnode(inputblock)

        expectedOutput=ParentNode(tag="p",
                                  children=[LeafNode("This is a "),
                                            LeafNode(tag="i", value="text"),
                                            LeafNode(" containing "),
                                            LeafNode(tag="b", value="italic"),
                                            LeafNode(" and "),
                                            LeafNode(tag="b", value="bold")]
                                  )

        self.assertEqual(actualOutput,expectedOutput)

    def test_block_to_nodes_code(self):
        inputblock="```for i in range(10):\n\tprint(i)```"
        actualOutput=block_to_htmlnode(inputblock)

        expectedOutput=ParentNode(tag="pre", children=[LeafNode(tag="code", value="for i in range(10):\n\tprint(i)")])

        self.assertEqual(actualOutput,expectedOutput)

    def test_block_to_nodes_header1(self):
        inputblock="# Title"
        actualOutput=block_to_htmlnode(inputblock)

        expectedOutput=ParentNode(tag="h1", children=[LeafNode(value="Title")])

        self.assertEqual(actualOutput,expectedOutput)

    def test_block_to_nodes_header3(self):
        inputblock="### Title smaller #"
        actualOutput=block_to_htmlnode(inputblock)

        expectedOutput=ParentNode(tag="h3", children=[LeafNode(value="Title smaller #")])

        self.assertEqual(actualOutput,expectedOutput)

    def test_block_to_nodes_quote(self):
        inputblock="> This is a quote\n> From me"
        actualOutput=block_to_htmlnode(inputblock)

        expectedOutput=ParentNode(tag="blockquote", children=[LeafNode(tag="p", value="This is a quote\nFrom me")])

        self.assertEqual(actualOutput,expectedOutput)

    def test_block_to_nodes_unordered_list(self):
        inputblock="* A listylist\n* Second item"
        actualOutput=block_to_htmlnode(inputblock)

        expectedOutput=ParentNode(tag="ul", children=[LeafNode(tag="li", value="A listylist"), LeafNode(tag="li", value="Second item")])

        self.assertEqual(actualOutput,expectedOutput)

    def test_block_to_nodes_ordered_list(self):
        inputblock="1. A listylist\n2. Second item"
        actualOutput=block_to_htmlnode(inputblock)

        expectedOutput=ParentNode(tag="ol", children=[LeafNode(tag="li", value="A listylist"), LeafNode(tag="li", value="Second item")])

        self.assertEqual(actualOutput,expectedOutput)

if __name__=="__main__":
    unittest.main()