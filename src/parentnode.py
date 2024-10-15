from htmlnode import HTMLNode
from leafnode import LeafNode
from functools import reduce


class ParentNode(HTMLNode):
    def __init__(self,children,tag=None,props=None):
        ParentNode.__check_valid_children_tree(children)

        super().__init__(children=children,tag=tag,props=props)

    @staticmethod
    def __check_valid_children_tree(children):
        if not isinstance(children,list):
            raise TypeError("ParentNode attribute for children is not an array")
        elif len(children)==0:
            raise ValueError("ParentNode must have at least one children")
        
        childrenHaveCorrectTypes=map(lambda child:isinstance(child,ParentNode) or isinstance(child,LeafNode),children)

        if not reduce(lambda bool1,bool2: bool1 and bool2,childrenHaveCorrectTypes):
            raise TypeError("ParentNode children must be either other parent nodes or leaf nodes")
        

    def to_html(self):
        if not isinstance(self.tag,str):
            raise TypeError("Translating ParentNode to HTML requires a tag of type string")
        elif self.tag=="":
            raise ValueError("Empty tags are not allowed for ParentNodes")

        htmlStringIterable=map(lambda child:child.to_html(),self.children)
        
        concatted=reduce(lambda str1,str2:str1+str2,htmlStringIterable)

        return f"<{self.tag}{self.props_to_html()}>{concatted}</{self.tag}>"
