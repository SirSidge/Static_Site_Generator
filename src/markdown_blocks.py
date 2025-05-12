def markdown_to_blocks(markdown):
    blocks = markdown.strip().split("\n\n")
    for block in blocks:
        if block == "":
            blocks.remove(block)
    return blocks