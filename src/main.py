import os, shutil

def main():
    shutil.rmtree("public", True)
    os.mkdir("public")
    copy_directories("static", "public")
    print(extract_title("# Heading"))
    
def copy_directories(orig, dest):
    sub_dir = os.listdir(orig)
    for i in range(len(sub_dir)):
        if os.path.isfile(os.path.join(orig, sub_dir[i])):
            print(f"Copying {os.path.join(orig, sub_dir[i])} -> {os.path.join(dest, sub_dir[i])}")
            shutil.copy(os.path.join(orig, sub_dir[i]), dest)
        else:
            if not os.path.exists(os.path.join(dest, sub_dir[i])):
                os.mkdir(os.path.join(dest, sub_dir[i]))
            copy_directories(os.path.join(orig, sub_dir[i]), os.path.join(dest, sub_dir[i]))

def extract_title(markdown):
    heading = markdown.strip() #removes white spaces before and after
    if heading.startswith("# "):
        return heading.replace("# ", "", 1)
    return markdown

main()