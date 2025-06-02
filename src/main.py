import os, shutil

def main():
    shutil.rmtree("public", True)
    os.mkdir("public")
    static_directories(os.listdir("static"))
    shutil.copy("static/index.css", "public")
    

def static_directories(static_dir):
    for i in range(len(static_dir)):
        if os.path.isfile(os.path.join("static", {static_dir[i]})):
            print(f"Yes {static_dir[i]} is a file")
        else:
            print(f"No {static_dir[i]} is a directory")
    return static_dir

main()