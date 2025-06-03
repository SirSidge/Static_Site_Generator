import os, shutil

def main():
    shutil.rmtree("public", True)
    os.mkdir("public")
    static_directories("static")
    
def static_directories(static_dir):
    if os.path.isfile(static_dir):
        return static_dir
    next_level = os.listdir(static_dir)
    for i in range(len(next_level)):
        new_path = static_directories(os.path.join(static_dir, next_level[i]))
        if type(new_path) is not type(None):
            shutil.copy(new_path, "public")

main()