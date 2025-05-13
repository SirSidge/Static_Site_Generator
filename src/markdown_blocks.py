from enum import Enum
from htmlnode import HTMLNode

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
    #Still need the type
    nodes = []
    for block in blocks:
        nodes.append(HTMLNode(markdown_type_to_tag(block_to_block_type(block)), block))
    #print(nodes)
    return nodes

def markdown_type_to_tag(type):
    if type is BlockType.PARAGRAPH:
        return "p"
    if type is BlockType.HEADING:
        return "div"
    if type is BlockType.CODE:
        return "code"
    if type is BlockType.QUOTE:
        return "quote"
    if type is BlockType.ULIST:
        return "ul"
    if type is BlockType.OLIST:
        return "ol"