def markdown_to_blocks(markdown):
    result = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        if not block:
            continue
        block = block.strip()
        result.append(block)
    return result
