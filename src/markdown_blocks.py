from enum import Enum
import re

from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType
from htmlnode import HTMLNode, ParentNode, LeafNode

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
    html_nodes = []
    blocks = markdown_to_blocks(markdown)
    for i in range(len(blocks)):
        block = blocks[i]
        if block_to_block_type(block) == BlockType.PARAGRAPH:
            block = replace_newline(block)
            child_nodes = text_to_textnodes(block)
            for r in range(len(child_nodes)):
                child_nodes[r] = text_node_to_html_node(child_nodes[r])
            html_nodes.append(HTMLNode("p", "", child_nodes))
        if block_to_block_type(block) == BlockType.HEADING:
            block = replace_newline(block)
            new_nodes = text_to_textnodes(block)
            new_text = ""
            for i in range(len(new_nodes)):
                new_text += text_node_to_html_node(new_nodes[i]).to_html()
            header_counter = new_text.index(" ",0, 7)
            html_nodes.append(HTMLNode(f"h{header_counter}", new_text[(header_counter + 1):]))
        if block_to_block_type(block) == BlockType.CODE:
            block = re.search(r"\`\`\`(.*?)\`\`\`", block, re.S).group(1)
            if block.startswith("\n"):
                block = block[1:]
            html_nodes.append(HTMLNode("pre", "", [LeafNode("code", block)]))
        if block_to_block_type(block) == BlockType.QUOTE:
            block = replace_newline(block)
            block = block.replace(">", "")
            child_nodes = text_to_textnodes(block)
            for r in range(len(child_nodes)):
                child_nodes[r] = text_node_to_html_node(child_nodes[r])
            html_nodes.append(HTMLNode("blockquote", "", child_nodes))
        if block_to_block_type(block) == BlockType.ULIST:
            block = block.replace("- ", "")
            child_nodes = block.split("\n")
            for r in range(len(child_nodes)):
                child_nodes[r] = LeafNode("li", child_nodes[r])
            html_nodes.append(HTMLNode("ul", "", child_nodes))
        if block_to_block_type(block) == BlockType.OLIST:
            pass
    return ParentNode("div", html_nodes)

def replace_newline(block):
    if "\n" in block:
        return block.replace("\n", " ")
    return block