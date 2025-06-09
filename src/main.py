import os, shutil

from markdown_blocks import markdown_to_html_node

def main():
    shutil.rmtree("public", True)
    if not os.path.exists("public"):
        os.mkdir("public")
    copy_directories("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")
    
def copy_directories(orig, dest):
    sub_dir = os.listdir(orig)
    for i in range(len(sub_dir)):
        src_path = os.path.join(orig, sub_dir[i])
        dest_path = os.path.join(dest, sub_dir[i])
        if os.path.isfile(src_path):
            print(f"Copying {src_path} -> {dest_path}")
            shutil.copy(src_path, dest)
        else:
            if not os.path.exists(dest_path):
                os.mkdir(dest_path)
            copy_directories(src_path, dest_path)

def extract_title(markdown):
    heading = markdown.strip()
    if heading.startswith("# "):
        return heading.replace("# ", "", 1)
    return markdown

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown = open(from_path).read() #content/index.md
    template = open(template_path).read() #template.html
    html_node = markdown_to_html_node(markdown).to_html()
    print(html_node)
    """title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", markdown)
    copy_directories(template_path, dest_path)"""

main()