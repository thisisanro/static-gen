def markdown_to_blocks(markdown):
    result = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        if not block:
            continue
        block = block.strip()
        result.append(block)
    return result

def block_to_block_type(text):
    if not text:
        raise ValueError("Block of markdown text is required")
    lines = text.split("\n")
    if text.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return "heading"
    if text.startswith("```") and text.endswith("```"):
        return "code"
    if text.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return "paragraph"
        return "quote"
    if text.startswith("* ") or text.startswith("- "):
        for line in lines:
            if not line.startswith(("* ", "- ")):
                return "paragraph"
        return "unordered_list"
    if text.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return "paragraph"
            i += 1
        return "ordered_list"
    return "paragraph"