import unittest

from markdown_parser import BlockType, block_to_blocktype, markdown_to_blocks

class TestMarkdownParser(unittest.TestCase):

    def test_markdown_to_blocks1(self):
        markdown=\
        "# This is a heading\n"+\
        "\n"+\
        "This is a paragraph of text. It has some **bold** and *italic* words inside of it.\n"+\
        "\n"+\
        "* This is the first list item in a list block\n"+\
        "* This is a list item\n"+\
        "* This is another list item"

        actualOutput=markdown_to_blocks(markdown)

        expectedOutput=[
                        "# This is a heading",
                        "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                        "* This is the first list item in a list block\n"+
                        "* This is a list item\n"+
                        "* This is another list item"
                        ]
        
        self.assertEqual(actualOutput,expectedOutput)

    def test_markdown_to_blocks2(self):
        markdown=\
        "# This is a heading\n"+\
        "\n"+\
        "This is a paragraph of text. It has some **bold** and *italic* words inside of it.\n"+\
        "\n"+\
        "\n"+\
        "* This is the first list item in a list block\n"+\
        "* This is a list item\n"+\
        "* This is another list item"

        actualOutput=markdown_to_blocks(markdown)

        expectedOutput=[
                        "# This is a heading",
                        "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                        "* This is the first list item in a list block\n"+
                        "* This is a list item\n"+
                        "* This is another list item"
                        ]
        
        self.assertEqual(actualOutput,expectedOutput)

    def test_markdown_to_blocks3(self):
        markdown=\
        "   # This is a heading\n"+\
        "\n   "+\
        "  This is a paragraph of text. It has some **bold** and *italic* words inside of it.   \n"+\
        "\n"+\
        "\n   "+\
        "   * This is the first list item in a list block\n"+\
        "* This is a list item\n"+\
        "* This is another list item    "

        actualOutput=markdown_to_blocks(markdown)

        expectedOutput=[
                        "# This is a heading",
                        "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                        "* This is the first list item in a list block\n"+
                        "* This is a list item\n"+
                        "* This is another list item"
                        ]
        
        self.assertEqual(actualOutput,expectedOutput)
    
    def test_markdown_to_blocks4(self):
        markdown="      \n           \n \n \n   \n \n"

        self.assertEqual(markdown_to_blocks(markdown),[])

    def test_blocktype1(self):
        markdown=\
        "# This is a heading\n"+\
        "\n"+\
        "This is a paragraph of text. It has some **bold** and *italic* words inside of it.\n"+\
        "\n"+\
        "* This is the first list item in a list block\n"+\
        "* This is a list item\n"+\
        "* This is another list item"

        actualOutput=list(map(block_to_blocktype,markdown_to_blocks(markdown)))

        expectedOutput=[
                        BlockType.HEADING,
                        BlockType.PARAGRAPH,
                        BlockType.UNORDERED_LIST
                        ]
        self.assertEqual(actualOutput,expectedOutput)

    def test_blocktype_orderedlist(self):
        markdown=\
        "# This is a heading\n"+\
        "\n"+\
        "This is a paragraph of text. It has some **bold** and *italic* words inside of it.\n"+\
        "\n"+\
        "1. This is the first list item in a list block\n"+\
        "2. This is a list item\n"+\
        "3. This is another list item"

        actualOutput=list(map(block_to_blocktype,markdown_to_blocks(markdown)))

        expectedOutput=[
                        BlockType.HEADING,
                        BlockType.PARAGRAPH,
                        BlockType.ORDERED_LIST
                        ]
        self.assertEqual(actualOutput,expectedOutput)

    def test_blocktype_orderedlist2(self):
        markdown=\
        "# This is a heading\n"+\
        "\n"+\
        "This is a paragraph of text. It has some **bold** and *italic* words inside of it.\n"+\
        "\n"+\
        "0. This is the first list item in a list block\n"+\
        "2. This is a list item\n"+\
        "3. This is another list item"

        actualOutput=list(map(block_to_blocktype,markdown_to_blocks(markdown)))

        expectedOutput=[
                        BlockType.HEADING,
                        BlockType.PARAGRAPH,
                        BlockType.PARAGRAPH
                        ]

        self.assertEqual(actualOutput,expectedOutput)

    def test_blocktype_orderedlist3(self):
        markdown=\
        "# This is a heading\n"+\
        "\n"+\
        "This is a paragraph of text. It has some **bold** and *italic* words inside of it.\n"+\
        "\n"+\
        "1. This is the first list item in a list block\n"+\
        "3. This is a list item\n"+\
        "2. This is another list item"

        actualOutput=list(map(block_to_blocktype,markdown_to_blocks(markdown)))

        expectedOutput=[
                        BlockType.HEADING,
                        BlockType.PARAGRAPH,
                        BlockType.PARAGRAPH
                        ]
        self.assertEqual(actualOutput,expectedOutput)

if __name__=="__main__":
    unittest.main()
