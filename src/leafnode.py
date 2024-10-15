from htmlnode import HTMLNode

class LeafNode(HTMLNode):

    def __init__(self,value,tag=None,props=None):
        if not isinstance(value,str):
            raise TypeError("LeafNode is required to have a string value.")
        else:
            super().__init__(tag=tag,value=value,props=props)

    def to_html(self):
        if not isinstance(self.tag,str) or self.tag=="":
            return str(self.value)
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

