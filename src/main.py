from textnode import TextNode, TextType

def main():
    text_node = TextNode("this is some text", TextType.LINK, "thisisaurl.com")
    print(text_node)


if __name__ == "__main__":
    main()

