from textnode import TextNode, TextType


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

        