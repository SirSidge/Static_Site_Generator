from textnode import TextNode, TextType

def main():
    node = TextNode.__repr__(TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev"))
    print(node)

main()