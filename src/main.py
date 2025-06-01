import os, shutil

from textnode import TextNode, TextType

def main():
    shutil.rmtree("public", True)
    os.mkdir("public")
    print(os.listdir("static"))

def static_directories(static_dir):
    pass

main()