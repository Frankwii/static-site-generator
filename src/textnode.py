from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT="text"
    BOLD="bold"
    ITALIC="italic"
    CODE="code"
    LINK="link"
    IMAGE="image"

class TextNode:
    def __init__(self,text,textType=TextType.TEXT,url=None):
        self.text=text
        if not isinstance(textType,TextType):
            raise TypeError("Invalid text type")
        self.textType=textType
        self.url=url

    def __eq__(self,other):
        return vars(self)==vars(other)

    def __repr__(self):
        return f"TextNode({self.text}, {self.textType.value}, {self.url})"

    def to_html_node(self):
        match self.textType:
            case TextType.TEXT:
                return LeafNode(value=self.text)
            case TextType.BOLD:
                return LeafNode(tag="b",value=self.text)
            case TextType.ITALIC:
                return LeafNode(tag="i",value=self.text)
            case TextType.CODE:
                return LeafNode(tag="code",value=self.text)
            case TextType.LINK:
                return LeafNode(tag="a",value=self.text,props={"href":self.url})
            case TextType.IMAGE:
                return LeafNode(tag="img",value="",props={"src":self.url,"alt":self.text})


