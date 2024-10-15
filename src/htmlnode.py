from functools import reduce

class HTMLNode:
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag=tag
        self.value=value
        self.children=children
        self.props=props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None or len(self.props)==0:
            return ""

        stringIterable=map(HTMLNode.__tuple_to_string_htmlformat,self.props.items())

        return reduce(lambda str1,str2:str1+str2,stringIterable)


    @staticmethod
    def __tuple_to_string_htmlformat(item):
        key,value=item
        return f" {str(key)}=\"{str(value)}\""

    def __repr__(self):

        return f"Tag: {self.tag}\nValue: {self.value}\nChildren: {self.children}\nProps: {self.props}"

    def __eq__(self,other):
        return vars(self)==vars(other)

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
