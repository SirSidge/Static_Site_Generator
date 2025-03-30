from enum import Enum

from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "Text"
    BOLD = "Bold"
    ITALIC = "Italic"
    CODE = "Code"
    LINK = "Link"
    IMAGE = "Image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def text_node_to_html_node(text_node):
    if text_node.text_type not in TextType:
        raise Exception("Type Error: This type does not exist")
    if text_node.text_type is TextType.TEXT:
        return LeafNode(None, text_node.text)
    if text_node.text_type is TextType.BOLD:
        return LeafNode("b", text_node.text)
    if text_node.text_type is TextType.ITALIC:
        return LeafNode("i", text_node.text)
    if text_node.text_type is TextType.CODE:
        return LeafNode("code", text_node.text)
    if text_node.text_type is TextType.LINK:
        return LeafNode("a", text_node.text, text_node.url)
    if text_node.text_type is TextType.IMAGE:
        return LeafNode("img", "", text_node.url)