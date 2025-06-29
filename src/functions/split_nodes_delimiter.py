from textnode import TextType, TextNode
from functions.extract_markdown_links import extract_markdown_links, extract_markdown_images


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_image(old_nodes: list[TextNode]):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        original_text = node.text
        link_data = extract_markdown_images(original_text)

        if len(link_data) == 0:
            new_nodes.append(node)
            continue

        remaining_text = original_text
        for link in link_data:
            before, after = remaining_text.split(f"![{link[0]}]({link[1]})", 1)

            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.IMAGE, link[1]))
            remaining_text = after

        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes



def split_nodes_link(old_nodes: list[TextNode]):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        original_text = node.text
        link_data = extract_markdown_links(original_text)

        if len(link_data) == 0:
            new_nodes.append(node)
            continue

        remaining_text = original_text
        for link in link_data:
            before, after = remaining_text.split(f"[{link[0]}]({link[1]})", 1)

            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            remaining_text = after

        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

def markdown_to_blocks(markdown):
    # lines = markdown.split("\n")
    # blocks = []
    # current_block = []

    # for line in lines:
    #     if line.strip() == "":
    #         # Blank line: close current block
    #         if current_block:
    #             blocks.append("\n".join(current_block))
    #             current_block = []
    #     else:
    #         current_block.append(line)

    # # Add the final block if any
    # if current_block:
    #     blocks.append("\n".join(current_block))

    # return blocks
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block.strip() == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

    


if __name__ == "__main__":
    md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
    print(markdown_to_blocks(md))




