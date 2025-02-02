import shutil
import os

from copystatic import copy_files_recursive
from generate_page import generate_pages_recursive


static = "./static"
content = "./content"
public = "./public"
template = "./template.html"


def main():
    if os.path.exists(public):
        print("Deleting public directory...")
        shutil.rmtree(public)
    print("Copying files to public directory...")
    copy_files_recursive(static, public)

    print("Generating site...")
    generate_pages_recursive(content, template, public)


if __name__ == "__main__":
    main()