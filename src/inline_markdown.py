from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    return matches

def split_nodes_image(old_nodes):
    pass

def split_nodes_link(old_nodes):
    new_string = []
    og_string = old_nodes[0].text
    print(og_string)
    delimiter = extract_markdown_links(old_nodes[0].text)
    print(delimiter)
    #new_string = og_string.split(delimiter[0][0], 1)
    new_string = re.split(r"\[.*?\)", og_string)
    print(new_string)
    """new_nodes = []
    extracted_links = []
    for old_node in old_nodes:
        extracted_links = extract_markdown_links(old_node.text)
        for i in range(len(extracted_links)):
            extracted_links[i] = TextNode(extracted_links[i][0], TextType.LINK,)
        new_nodes.extend(extracted_links)
    print(new_nodes)"""
    pass

# Ok so I am on to something here. I just need to find a way to ignore the empty list item. It might not always be the last one, maybe .remove("").