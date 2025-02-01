import shutil
import os


def copy_files_recursive(src, dst):
    if not os.path.exists(dst):
        os.mkdir(dst)
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)
        if os.path.isfile(src_path):
            print(f"Copying file: {src_path} to {dst_path}")
            shutil.copy(src_path, dst_path)
        if os.path.isdir(src_path):
            print(f"Creating directory: {dst_path}")
            os.mkdir(dst_path)
            copy_files_recursive(src_path, dst_path)
