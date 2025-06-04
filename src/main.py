import os, shutil

def main():
    shutil.rmtree("public", True)
    os.mkdir("public")
    static_directories("static")
    
def static_directories(static_dir):
    if os.path.isfile(static_dir):
        return static_dir
    next_level = os.listdir(static_dir)
    new_dir = "public"
    for i in range(len(next_level)):
        if not os.path.isfile(os.path.join(static_dir, next_level[i])):
            new_dir = os.path.join(new_dir, next_level[i])
            os.mkdir(new_dir)
        new_path = static_directories(os.path.join(static_dir, next_level[i]))
        if type(new_path) is not type(None):
            shutil.copy(new_path, new_dir)

main()