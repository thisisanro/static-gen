from textnode import TextNode, TextType
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    split_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            split_nodes.append(node)
            continue
        parts = node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise ValueError("Invalid Markdown syntax, closing delimiter is required")
        for i in range(len(parts)):
            if parts[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(parts[i], TextType.NORMAL))
            else:
                split_nodes.append(TextNode(parts[i], text_type))
    return split_nodes

def split_nodes_image(old_nodes):
    result = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            result.append(node)
            continue
        node_text = node.text
        images = extract_markdown_images(node_text)
        if len(images) == 0:
            result.append(node)
            continue
        for image in images:
            parts = node_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(parts) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if parts[0] != "":
                result.append(TextNode(parts[0], TextType.NORMAL))
            result.append(TextNode(image[0], TextType.IMAGE, image[1]))
            node_text = parts[1]
        if node_text != "":
            result.append(TextNode(node_text, TextType.NORMAL))
    return result

def split_nodes_link(old_nodes):
    result = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            result.append(node)
            continue
        node_text = node.text
        links = extract_markdown_links(node_text)
        if len(links) == 0:
            result.append(node)
            continue
        for alt, url in links:
            parts = node_text.split(f"[{alt}]({url})", 1)
            if len(parts) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if parts[0] != "":
                result.append(TextNode(parts[0], TextType.NORMAL))
            result.append(TextNode(alt, TextType.LINK, url))
            node_text = parts[1]
        if node_text != "":
            result.append(TextNode(node_text, TextType.NORMAL))
    return result
            

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches
        