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
    og_string = old_nodes[0].text
    extracted_images = extract_markdown_images(old_nodes[0].text)
    new_string = re.split(r"!\[.*?\]|\(.*?\)", og_string)
    counter = 0
    for i in range(len(new_string)):
        if i % 2 == 0:
            new_string[i] = TextNode(new_string[i], TextType.TEXT)
        else:
            new_string[i] = TextNode(extracted_images[counter][0], TextType.IMAGE, extracted_images[counter][1])
            counter += 1
    new_string.pop((len(new_string) - 1))
    return new_string

def split_nodes_link(old_nodes):
    og_string = old_nodes[0].text
    extracted_links = extract_markdown_links(old_nodes[0].text)
    new_string = re.split(r"\[.*?\]|\(.*?\)", og_string)
    counter = 0
    for i in range(len(new_string)):
        if i % 2 == 0:
            new_string[i] = TextNode(new_string[i], TextType.TEXT)
        else:
            new_string[i] = TextNode(extracted_links[counter][0], TextType.LINK, extracted_links[counter][1])
            counter += 1
    new_string.pop((len(new_string) - 1))
    return new_string