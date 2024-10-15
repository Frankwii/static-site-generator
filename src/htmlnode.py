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
