from markdown_blocks import (
    block_to_block_type,
    markdown_to_blocks,
    markdown_to_html_node,
)

from copystatic import copy_files_recursive

import os
from pathlib import Path
import shutil


def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block_to_block_type(block) == "heading" and block.startswith("# "):
            return block[2:].strip()
    raise ValueError("Markdown has no h1 header")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown = ""
    with open(from_path) as file:
        markdown= file.read()
    template = ""
    with open(template_path) as file:
        template = file.read()
    html_node = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    html_page = template.replace("{{ Title }}", title)
    html_page = html_page.replace("{{ Content }}", html_node)
    with open(dest_path, "w") as file:
        file.write(html_page)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for item in os.listdir(dir_path_content):
        src_path = os.path.join(dir_path_content, item)
        dst_path = os.path.join(dest_dir_path, item)
        if os.path.isfile(src_path) and src_path.endswith(".md"):
            dst_path = Path(dst_path).with_suffix(".html")
            generate_page(src_path, template_path, dst_path)
        if os.path.isdir(src_path):
            if not os.path.exists(dst_path):
                print(f"Creating directory: {dst_path}")
                os.mkdir(dst_path)
            generate_pages_recursive(src_path, template_path, dst_path)
