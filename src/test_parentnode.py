import unittest

from htmlnode import LeafNode,ParentNode

class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode(
            tag="p",
            children=[
                LeafNode(tag="b", value="Bold text"),
                LeafNode(value="Normal text"),
                LeafNode(tag="i", value="italic text"),
                LeafNode(value="Normal text"),
            ],
        )
        self.assertEqual(node.to_html(),"<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_to_html2(self):
        node=ParentNode(tag="a",
                       children=[LeafNode(value="Val"),
                                 ParentNode(tag="c",
                                            children=[LeafNode(value="Val2"),
                                                      LeafNode(tag="b",value="Val3")],
                                            props={"tag3":"prop3"}
                                            )
                                 ],
                        props={"tag1":"prop1","tag2":"prop2"},
                       )
        self.assertEqual(node.to_html(),
                         "<a tag1=\"prop1\" tag2=\"prop2\">Val<c tag3=\"prop3\">Val2<b>Val3</b></c></a>"
        )
    def test_empty_parent(self):
        with self.assertRaises(ValueError):
            ParentNode(tag="a",
                       children=[]
                       )

    def test_tree_types(self):
        with self.assertRaises(TypeError):
            ParentNode(tag="a",
                       children=[2,LeafNode(value="Val")]
                       )

    def test_tree_types2(self):
        with self.assertRaises(TypeError):
            ParentNode(tag="a",
                       children=[LeafNode(value="Val"),
                                 ParentNode(tag="b",
                                            children=[LeafNode(value="Val2"),1]
                                            )
                                 ]
                       )

    def test_notag_tohtml(self):
        with self.assertRaises(TypeError):
            ParentNode(
                       children=[LeafNode(value="Val"),
                                 ParentNode(tag="b",
                                            children=[LeafNode(value="Val2"),1]
                                            )
                                 ]
                      ).to_html()

    def test_notag_tohtml2(self):
        with self.assertRaises(TypeError):
            ParentNode(
                       children=[LeafNode(value="Val"),
                                 ParentNode(tag="b",
                                            children=[LeafNode(value="Val2")]
                                            )
                                 ]
                      ).to_html()

    def test_badtypetag_tohtml(self):
        with self.assertRaises(TypeError):
            ParentNode(tag=2,
                       children=[LeafNode(value="Val"),
                                 ParentNode(tag="b",
                                            children=[LeafNode(value="Val2"),1]
                                            )
                                 ]
                      ).to_html()



if __name__ == "__main__":
    unittest.main()
