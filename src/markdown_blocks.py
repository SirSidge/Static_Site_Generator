from enum import Enum

from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"

def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.OLIST
    return BlockType.PARAGRAPH

def markdown_to_blocks(markdown):
    blocks = markdown.strip().split("\n\n")
    for block in blocks:
        if block == "":
            blocks.remove(block)
    return blocks

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    print(blocks)
    new_text_nodes = []
    new_leaf_nodes = []
    for block in blocks:
        if BlockType.PARAGRAPH == block_to_block_type(block):
            new_text_nodes.extend(text_to_textnodes(block))
        if BlockType.HEADING == block_to_block_type(block):
            print("********FOUND A HEADING*************")
        if BlockType.CODE == block_to_block_type(block):
            print("********FOUND A CODE*************")
        if BlockType.QUOTE == block_to_block_type(block):
            print("********FOUND A QUOTE*************")
        if BlockType.ULIST == block_to_block_type(block):
            print("********FOUND A ULIST*************")
        if BlockType.OLIST == block_to_block_type(block):
            print("********FOUND A OLIST*************")
        #maybe raise an error if none of the above
    print(new_text_nodes)
    for text_node in new_text_nodes:
        new_leaf_nodes.append(text_node_to_html_node(text_node).to_html())
    new_value = ""
    for i in new_leaf_nodes:
        new_value += i
    html_node = ParentNode("div", f"<p>{new_value}</p>")
    print("----------------------------")
    print(html_node)
    print("----------------------------")
    pass
