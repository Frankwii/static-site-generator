from enum import Enum
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
