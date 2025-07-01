from functions.stage_files import stage_files
from functions.generate_page import generate_pages_recursive
import sys

def main():
    if len(sys.argv) == 2:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    
    print(f"base ---- {basepath}")
    content = "./content"
    template = "./template.html"
    public = "./docs"

    dir_path_static = "./static"

    stage_files(dir_path_static, public)
    
    generate_pages_recursive(
        content,
        template,
        public,
        basepath,
    )
    

if __name__ == "__main__":
    main()

 