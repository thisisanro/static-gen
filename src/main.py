import shutil
import os

from copystatic import copy_files_recursive
from generate_page import generate_page


src = "./static"
dst = "./public"


def main():
    if os.path.exists(dst):
        print("Deleting public directory...")
        shutil.rmtree(dst)
    print("Copying files to public directory...")
    copy_files_recursive(src, dst)

    generate_page("content/index.md", "./template.html", "public/index.html")

if __name__ == "__main__":
    main()