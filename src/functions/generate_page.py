from functions.markdown_to_html_node import markdown_to_html_node
from functions.extract_title import extract_title
import os

def generate_page(from_path, template_path, dest_path):
    print(f"generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        md = f.read()
    with open(template_path) as template:
        temp = template.read()

    html_node = markdown_to_html_node(md)
    html_string = html_node.to_html()

    title = extract_title(html_string)
    html_string = html_string.replace(title, "")
    filled_template = temp.replace("{{ Title }}", title).replace("{{ Content }}", html_string)

    with open(dest_path + "/public/index.html", "w") as html_page:
        html_page.write(filled_template)
        return filled_template

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    with open(template_path) as t:
        template = t.read()
    
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        relative_path = os.path.relpath(from_path, start=dir_path_content)
        final_path = os.path.join(dest_dir_path, relative_path)

        # print(f" ------ from path {from_path}")
        # print(f" ------ final path {final_path}")


        if os.path.isfile(from_path) and from_path.endswith(".md"):
            with open(from_path) as f:
                md = f.read()
                html_node = markdown_to_html_node(md)
                html_string = html_node.to_html()
                title = extract_title(html_string)
                html_string = html_string.replace(title, "")

                filled_template = template.replace("{{ Title }}", title).replace("{{ Content }}", html_string)
                
                final_path = os.path.splitext(final_path)[0] + ".html"

                os.makedirs(os.path.dirname(final_path), exist_ok=True)

                with open(final_path, "w") as html_page:
                    html_page.write(filled_template)
                    
        elif os.path.isdir(from_path):
            print(f"recursively calling function with this dir path -> {from_path}")
            from_path = os.path.join(dir_path_content, filename)

            generate_pages_recursive(from_path, template_path, os.path.join(dest_dir_path, filename))


if __name__ == "__main__":
    content = "./content"
    template = "./template.html"
    public = "./public"


    generate_pages_recursive(content, template, public)

