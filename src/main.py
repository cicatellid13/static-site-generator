from functions.stage_files import stage_files
from functions.generate_page import generate_pages_recursive
from dotenv import load_dotenv
import os



def main():
    load_dotenv()
    stage_files()
    content = "./content"
    template = "./template.html"
    public = "./public"
    generate_pages_recursive(
        content,
        template,
        public,
    )
    

if __name__ == "__main__":
    main()

 