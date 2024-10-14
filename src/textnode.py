class TextNode:
    def __init__(self,text,textType,url=None):
        self.text=text
        self.textType=textType
        self.url=url

    def __eq__(self,other):
        return vars(self)==vars(other)

    def __repr__(self):
        return f"TextNode({self.text}, {self.textType}, {self.url})"
