

def extract_title(md: str):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line.replace("#", "").lstrip()
    # raise Exception(f"No h1 header in provided markdown: {md}")
    return "no title"