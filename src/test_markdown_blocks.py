import unittest

from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType, markdown_to_html_node
from htmlnode import HTMLNode

class BlockToBlockType(unittest.TestCase):
    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = "- list\n- items"
        self.assertEqual(block_to_block_type(block), BlockType.ULIST)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), BlockType.OLIST)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)


class MarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and _italic_ words inside of it.\n\n- This is the first list item in a list block\n- This is a list item\n- This is another list item"
        self.assertEqual(
            markdown_to_blocks(markdown),
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.",
                "- This is the first list item in a list block\n- This is a list item\n- This is another list item",
            ]
        )
    
    def test_markdown_to_blocks(self):
        md = "This is **bolded** paragraph\n\nThis is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line\n\n- This is a list\n- with items"
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ]
        )

class BlockToHTMLNode(unittest.TestCase):
    def test_block_to_html_node(self):
        md = "This is **bolded** paragraph\ntext in a p\ntag here\n\nThis is another paragraph with _italic_text and 'code' here"
        node = markdown_to_html_node(md)
        self.assertEqual(
            node,
            [
                HTMLNode("p", "This is **bolded** paragraph\ntext in a p\ntag here"),
                HTMLNode("p", "This is another paragraph with _italic_text and 'code' here"),
            ]
        )
        """html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )"""

