#!/usr/bin/env python
import sys
from pathlib import Path


def correct_name(name):
    i = 0
    name_parts = []
    last = ""
    for char in name:
        c = char
        if char.isupper():
            c = c.lower()
            if i > 0 and last != "_" and not last.isupper():
                c = "_" + c
        name_parts.append(c)
        i += 1
        last = char
    return "".join(name_parts)


def walk(path):
    for p in path.iterdir():
        rename(p)


def rename(path):
    cor_path = path.with_name(correct_name(path.name))
    if cor_path != path:
        print("renaming %s to %s" % (path, cor_path))
        path.rename(cor_path)
    if cor_path.is_dir():
        walk(cor_path)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise TypeError("No directory path passed")
    rename_path = Path(sys.argv[1]).resolve()
    if not rename_path.is_dir():
        raise TypeError("%s is not a directory!" % (rename_path,))
    print("recursivly rename path: %s" % rename_path)
    rename(rename_path)
