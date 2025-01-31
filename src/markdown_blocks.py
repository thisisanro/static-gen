from htmlnode import ParentNode
from markdown_parser import text_to_textnodes
from textnode import text_node_to_html_node


def markdown_to_blocks(markdown):
    result = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        if not block:
            continue
        block = block.strip()
        result.append(block)
    return result

def block_to_block_type(markdown):
    if not markdown:
        raise ValueError("Block of markdown text is required")
    lines = markdown.split("\n")
    if markdown.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return "heading"
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return "code"
    if markdown.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return "paragraph"
        return "quote"
    if markdown.startswith("* ") or markdown.startswith("- "):
        for line in lines:
            if not line.startswith(("* ", "- ")):
                return "paragraph"
        return "unordered_list"
    if markdown.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return "paragraph"
            i += 1
        return "ordered_list"
    return "paragraph"

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        children.append(block_to_html_node(block))
    return ParentNode("div", children)

def block_to_html_node(block):
    type = block_to_block_type(block)
    if type == "paragraph":
        return paragraph_to_html_node(block)
    if type == "heading":
        return heading_to_html_node(block)
    if type == "code":
        return code_to_html_node(block)
    if type == "quote":
        return quote_to_html_node(block)
    if type == "unordered_list":
        return uo_list_to_html_node(block)
    if type == "ordered_list":
        return o_list_to_html_node(block)
    raise ValueError("Invalid block type")

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for node in text_nodes:
        html_node = text_node_to_html_node(node)
        html_nodes.append(html_node)
    return html_nodes

def paragraph_to_html_node(block):
    text = " ".join(block.split("\n"))
    children = text_to_children(text)
    return ParentNode("p", children)

def heading_to_html_node(block):
    heading = block.split()[0]
    index = len(heading) + 1
    tag = f"h{len(heading)}"
    text = block[index:]
    if not text:
        raise ValueError("Heading text is empty")
    children = text_to_children(text)
    return ParentNode(tag, children)

def code_to_html_node(block):
    if not (block.startswith("```") and block.endswith("```")):
        raise ValueError("Invalid code block")
    lines = block.splitlines()
    text = "\n".join(lines[1:-1])
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])
    
def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        new_lines.append(line.lstrip(">").strip())
    text = " ".join(new_lines)
    if not text:
        raise ValueError("Quotes text is empty")
    children = text_to_children(text)
    return ParentNode("blockquote", children)

def uo_list_to_html_node(block):
    lines = block.split("\n")
    items = []
    for line in lines:
        text = line[2:].strip()
        if not text:
            raise ValueError("Invalid unorderdered list")
        children = text_to_children(text)
        items.append(ParentNode("li", children))
    return ParentNode("ul", items)

def o_list_to_html_node(block):
    lines = block.split("\n")
    items = []
    for line in lines:
        text = line[2:].strip()
        if not text:
            raise ValueError("Invalid ordered list")
        children = text_to_children(text)
        items.append(ParentNode("li", children))
    return ParentNode("ol", items)