import re
from itertools import chain
from textnode import TextType,TextNode

def split_node_textual_types(node,delimiter,text_type):
    # TextNode -> [TextNode]
    if node.textType != TextType.TEXT:
        return [node]

    splitted_text=node.text.split(delimiter)
    # Text pieces in odd positions (starting to count from 1) correspond to TEXT nodes
    # Those in even positions should be casted into text_type nodes
    
    n_nodes=len(splitted_text)

    if n_nodes%2==0:
        raise SyntaxError("Some markdown delimiter was not closed.")

    text_elements=map(lambda string:TextNode(text=string,textType=TextType.TEXT),splitted_text[::2])

    typed_elements=map(lambda string:TextNode(text=string,textType=text_type),splitted_text[1::2])

    # Now we zip those together, but we would be missing the last text element
    reordered_without_last=chain.from_iterable(zip(text_elements,typed_elements))
    nodes=chain(reordered_without_last,[TextNode(text=splitted_text[-1],textType=TextType.TEXT)]) 

    return filter(lambda node: node.text!="",nodes)

def split_nodes_delimiter(old_nodes,delimiter,text_type):
    match text_type:
        case TextType.BOLD:
            if not (delimiter=="**" or delimiter=="__"):
                raise ValueError("Wrong delimiter for bold text")
        case TextType.ITALIC:
            if not (delimiter=="*" or delimiter=="_"):
                raise ValueError("Wrong delimiter for italic text")
        case TextType.CODE:
            if not (delimiter=="`" or delimiter=="``"):
                raise ValueError("Wrong delimiter for code text")

    split_nodes=map(lambda node: split_node_textual_types(node,delimiter,text_type),old_nodes)

    return list(chain.from_iterable(split_nodes))

def extract_markdown_images(text):
    regex=r"!\[(.*?)\]\((.*?)\)"

    return re.findall(regex,text)

def extract_markdown_links(text):
    regex=r"(?<!!)\[(.*?)\]\((.*?)\)"

    return re.findall(regex,text)

def split_nodes_image(old_nodes):
    
    pass

def split_node_image_type(node):

    images=extract_markdown_images(node.text)


def split_nodes_link(old_nodes):
    pass
