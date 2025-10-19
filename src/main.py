import os, shutil, sys

from markdown_blocks import markdown_to_html_node

def main():
    basepath = ""
    if len(sys.argv) < 2:
        basepath = "/"
    else:
        basepath = sys.argv[1]
    shutil.rmtree("docs", True)
    if not os.path.exists("docs"):
        os.mkdir("docs")
    copy_directories("static", "docs")
    generate_pages_recursive("content", "template.html", "docs/index.html", basepath)
    
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

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown = open(from_path).read()
    template = open(template_path).read()
    html_node = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_node)
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')
    with open(dest_path, 'w') as f:
        f.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    if not os.path.isfile(dir_path_content):
        sub_dir = os.listdir(dir_path_content)
    else:
        return dir_path_content
    for item in sub_dir:
        new_dir_path = os.path.join(dir_path_content, item)
        if os.path.isfile(new_dir_path):
            temp_dir = os.path.join("docs", new_dir_path[8:]).replace("md", "html")
            os.makedirs(os.path.dirname(temp_dir), exist_ok=True)
            generate_page(new_dir_path, template_path, temp_dir, basepath)
        else:
            generate_pages_recursive(os.path.join(dir_path_content, item), template_path, dest_dir_path, basepath)

main()