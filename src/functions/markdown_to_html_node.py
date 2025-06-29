from functions.split_nodes_delimiter import markdown_to_blocks, text_to_textnodes
from functions.block_to_block_type import block_to_block_type, BlockType
from functions.text_node_to_html_node import text_node_to_html_node
from htmlnode import ParentNode, LeafNode
import re

def text_to_children(text):
    html_nodes = []
    text_nodes = text_to_textnodes(text)
    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))
    return html_nodes


def markdown_to_html_node(md):
    blocks = markdown_to_blocks(md)
    html_nodes = []
    for block in blocks:
        if not block.strip():
            continue
        block_type = block_to_block_type(block)

        match block_type:
            case BlockType.PARAGRAPH:
                lines = block.split("\n")
                stripped_lines = [line.strip() for line in lines if line.strip() != ""]
                paragraph = " ".join(stripped_lines)
                html_nodes.append(ParentNode("p", children=text_to_children(paragraph)))

            case BlockType.HEADING:
                tag = f"h{block.count("#")}"
                cleaned = block.replace("#", "").lstrip()
                html_nodes.append(ParentNode(tag, children=text_to_children(cleaned)))

            case BlockType.CODE:
                code_content = block.strip()
                if code_content.startswith("```"):
                    code_content = code_content[3:]
                if code_content.endswith("```"):
                    code_content = code_content[:-3]
                
                lines = code_content.split('\n')
                while lines and not lines[0].strip():
                    lines.pop(0)
                while lines and not lines[-1].strip():
                    lines.pop()
                
                min_indent = float('inf')
                for line in lines:
                    if line.strip():
                        indent = len(line) - len(line.lstrip())
                        min_indent = min(min_indent, indent)
                
                if min_indent != float('inf') and min_indent > 0:
                    lines = [line[min_indent:] if line.strip() else line for line in lines]
                
                code_content = '\n'.join(lines) + '\n'
                code_node = LeafNode("code", code_content)
                html_nodes.append(ParentNode("pre", children=[code_node]))
                # if not block.startswith("```") or not block.endswith("```"):
                #     raise ValueError("invalid code block")
                # text = block[4:-3]
                # raw_text_node = TextNode(text, TextType.TEXT)
                # child = text_node_to_html_node(raw_text_node)
                # code = ParentNode("code", [child])
                # html_nodes.append(ParentNode("pre", [code]))

            case BlockType.QUOTE:
                lines = block.split("\n")
                cleaned_lines = []
                for line in lines:
                    if line.startswith("> "):
                        cleaned_lines.append(line[2:])
                    elif line.startswith(">"):
                        cleaned_lines.append(line[1:])
                    else:
                        cleaned_lines.append(line)
                cleaned = "\n".join(cleaned_lines)
                html_nodes.append(ParentNode("blockquote", children=text_to_children(cleaned)))

            case BlockType.UNORDERED_LIST:
                lines = block.split("\n")
                li_nodes = []
                
                for line in lines:
                    if line.startswith("*"):
                        line = line[1:].lstrip() 
                    li_nodes.append(ParentNode("li", children=text_to_children(line)))
                html_nodes.append(ParentNode("ul", children=li_nodes))

            case BlockType.ORDERED_LIST:
                lines = block.split("\n")
                lines_cleaned = [re.sub(r"^\d+\.\s*", "", li).lstrip() for li in lines]
                li_nodes = []
                for line in lines_cleaned:
                    li_nodes.append(ParentNode("li", children=text_to_children(line)))
                html_nodes.append(ParentNode("ol", children=li_nodes))

    # print(html_nodes)
    return ParentNode(tag="div", children=html_nodes)



if __name__ == "__main__":
    markdown_to_html_node()