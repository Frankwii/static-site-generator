import re
from itertools import chain
from functools import reduce
from enum import Enum

from htmlnode import ParentNode, LeafNode
from node_parser import text_to_text_nodes

def split_strings_by_singular_delimiter_one(strings,delimiter):

    return chain.from_iterable(map(lambda string: string.split(delimiter,1), strings))

def split_strings_by_delimiters_one_by_one(strings,delimiters):

    # We're recursively applying split_strings_by_singular_delimiter to the (cumulative) split iterable
    # until the "delimiters" iterable is empty
    return reduce(split_strings_by_singular_delimiter_one, delimiters, strings)

def markdown_to_blocks(markdown):
    regex=r"[ \t]*\n[ \t\n]*\n+[ \t]*"

    blocksplitters=re.findall(regex,markdown)

    blocks_crude=split_strings_by_delimiters_one_by_one([markdown],blocksplitters)

    blocks_stripped=map(lambda string: string.strip(" \t\n"),blocks_crude)

    return list(filter(lambda string: string!="",blocks_stripped))

class BlockType(Enum):
    PARAGRAPH="paragraph"
    HEADING="heading"
    CODE="code"
    QUOTE="quote"
    UNORDERED_LIST="unordered list"
    ORDERED_LIST="ordered list"

def block_to_blocktype(block):
    firstword=block.split(" ",1)[0]

    if firstword in ["#","##","###","####","#####","######"]:
        return BlockType.HEADING
    
    split_code=block.split("```")
    if len(split_code)>2 and split_code[0]==split_code[-1]=="":
        return BlockType.CODE

    lines=block.splitlines()
    first_words_of_lines=list(map(lambda line: line.split(" ",1)[0], lines))

    lines_startby_quotes=map(lambda string: string==">", first_words_of_lines)

    if reduce(lambda bool1, bool2: bool1 and bool2, lines_startby_quotes):
        return BlockType.QUOTE

    lines_startby_bulletpoints=map(lambda string: string=="*" or string=="-", first_words_of_lines)

    if reduce(lambda bool1, bool2: bool1 and bool2, lines_startby_bulletpoints):
        return BlockType.UNORDERED_LIST
    
    def is_formatted_number(string):
        splitted=string.split(".",1)
        return splitted[-1]=="" and splitted[0].isdigit()

    lines_startby_formattednumbers=map(is_formatted_number,first_words_of_lines)

    if reduce(lambda bool1, bool2: bool1 and bool2, lines_startby_formattednumbers):
        numbers=list(
                map(int,
                    map(lambda string: string.split(".",1)[0], first_words_of_lines))
                )
        if len(numbers)>0 and numbers[0]==1:
            numbers_copy_without_one=numbers.copy()[1:]
            def difference_is_one(integer_tuple):
                num1, num2=integer_tuple
                return num2==num1+1

            differences_are_one=map(difference_is_one,zip(numbers,numbers_copy_without_one))
            if reduce(lambda bool1, bool2: bool1 and bool2, differences_are_one):
                return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH
    
def block_to_htmlnode(block):
    blocktype=block_to_blocktype(block)
    match blocktype:
        case BlockType.PARAGRAPH:
            textnodes=text_to_text_nodes(block)
            childnodes=list(map(lambda textnode: textnode.to_html_node(), textnodes))

            return ParentNode(tag="p", children=childnodes)
            
        case BlockType.CODE:
            text=block.split("```")[1]
            return ParentNode(tag="pre",
                              children=[LeafNode(tag="code", value=text)]
                              )

        case BlockType.HEADING:
            hashes, heading=block.split(" ",1)
            return ParentNode(tag=f"h{str(len(hashes))}",
                              children=[LeafNode(value=heading)]
                              )

        case BlockType.UNORDERED_LIST:
            listcontents=map(lambda line: line.split(" ")[1], block.splitlines())
            return ParentNode(tag="ul",
                              children=list(map(lambda string: LeafNode(tag="li", value=string), listcontents))
                              )

        case BlockType.ORDERED_LIST:
            listcontents=map(lambda line: line.split(" ")[1], block.splitlines())
            return ParentNode(tag="ol",
                              children=list(map(lambda string: LeafNode(tag="li", value=string), listcontents))
                              )

        case BlockType.QUOTE:
            quotelines=map(lambda line: line.split(" ")[1], block.splitlines())
            quote=reduce(lambda string1, string2: string1+"\n"+string2, quotelines)

            return ParentNode(tag="blockquote",
                              children=[LeafNode(value=quote)]
                              )

# def markdown_to_htmlnode(markdown):
#     pass


    

