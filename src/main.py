import os, shutil

from markdown_blocks import markdown_to_html_node

def main():
    shutil.rmtree("public", True)
    if not os.path.exists("public"):
        os.mkdir("public")
    copy_directories("static", "public")
    #generate_page("content/index.md", "template.html", "public/index.html")
    generate_pages_recursive("content", "template.html", "public/index.html")
    
def copy_directories(orig, dest):
    if not os.path.isfile(orig):
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
    else:
        print(f"Copying {orig} -> {dest}")
        shutil.copy(orig, dest)

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line.replace("# ", "", 1).strip()
    raise Exception("h1 does not exist")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown = open(from_path).read()
    template = open(template_path).read()
    html_node = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_node)
    copy_directories(template_path, dest_path)
    with open(dest_path, 'w') as f:
        f.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.isfile(dir_path_content):
        sub_dir = os.listdir(dir_path_content)
    else:
        return dir_path_content
    for item in sub_dir:
        if os.path.isfile(os.path.join(dir_path_content, item)):
            generate_page(os.path.join(dir_path_content, item), template_path, dir_path_content.replace("content", "public").replace("md", "html"))
        else:
            generate_pages_recursive(os.path.join(dir_path_content, item), template_path, dest_dir_path)

main()