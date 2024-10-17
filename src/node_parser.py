import re
from itertools import chain
from functools import reduce
from textnode import TextType,TextNode

def split_nodes_delimiter(old_nodes,delimiter,text_type):

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
    
        return filter(lambda node: not node.is_empty(),nodes)

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

### This code is quite complex
def split_strings_by_singular_delimiter(strings,delimiter):
    """
    Take an iterable of strings and a delimiter
    return another iterable yielding the strings splitted by the delimiter, in the original order
    """

    return chain.from_iterable(map(lambda string: string.split(delimiter),strings))

def split_strings_by_delimiters(strings,delimiters):
    """
    Take an iterable of strings and an iterable of delimiters
    return another iterable yielding the strings splitted by (all) delimiters, in the original order
    """

    # We're recursively applying split_strings_by_singular_delimiter to the (cumulative) split iterable
    # until the "delimiters" iterable is empty
    return reduce(split_strings_by_singular_delimiter, delimiters, strings)
### End of complex code

def split_nodes_image(old_nodes):
    def split_singular_node_image(node):
        text=node.text

        def extract_markdown_images(text):
            regex=r"!\[(.*?)\]\((.*?)\)"
        
            return re.findall(regex,text)

        image_tuples=extract_markdown_images(text)
    
        def construct_delimiter(image_tuple):
            alt,link=image_tuple
            return f"![{alt}]({link})"
    
        delimiters=map(construct_delimiter,image_tuples)
    
        intermediateTexts=list(split_strings_by_delimiters([text],delimiters))
    
        textNodes=map(lambda text:TextNode(text=text,textType=TextType.TEXT),intermediateTexts)
    
        def create_image_node(image_tuple):
            alt,link=image_tuple
            return TextNode(text=alt,url=link,textType=TextType.IMAGE)
    
        imageNodes=map(create_image_node,image_tuples)
    
        # Now we zip those together, but we would be missing the last text element
        reordered_without_last=chain.from_iterable(zip(textNodes,imageNodes))
        nodes=chain(reordered_without_last,[TextNode(text=intermediateTexts[-1],textType=TextType.TEXT)]) 
    
        return filter(lambda node: not node.is_empty(),nodes)

    return list(chain.from_iterable(map(split_singular_node_image,old_nodes)))


def split_nodes_link(old_nodes):
    def split_singular_node_link(node):
        text=node.text

        def extract_markdown_links(text):
            regex=r"(?<!!)\[(.*?)\]\((.*?)\)"
        
            return re.findall(regex,text)

        link_tuples=extract_markdown_links(text)
    
        def construct_delimiter(link_tuple):
            text,link=link_tuple
            return f"![{text}]({link})"
    
        delimiters=map(construct_delimiter,link_tuples)
    
        intermediateTexts=list(split_strings_by_delimiters([text],delimiters))
    
        textNodes=map(lambda text:TextNode(text=text,textType=TextType.TEXT),intermediateTexts)
    
        def create_link_node(image_tuple):
            text,link=image_tuple
            return TextNode(text=text,url=link,textType=TextType.LINK)
    
        link_nodes=map(create_link_node,link_tuples)
    
        # Now we zip those together, but we would be missing the last text element
        reordered_without_last=chain.from_iterable(zip(textNodes,link_nodes))
        nodes=chain(reordered_without_last,[TextNode(text=intermediateTexts[-1],textType=TextType.TEXT)]) 
    
        return filter(lambda node: not node.is_empty(),nodes)

    return list(chain.from_iterable(map(split_singular_node_link,old_nodes)))
