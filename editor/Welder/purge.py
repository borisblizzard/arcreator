import sys, os, stat, subprocess, shutil, time

purge_exts = [".pyo", ".pyc", ".pyd", ".cpp", ".c"]
purge_names = ["build", "cythonized_source", "__pycache__"]
exclude_names = ["PyXAL", "lib", "Welder.c"]

def scandir(dir):
    print("Scanning: %s" % dir)
    files = []
    for file in os.listdir(dir):
        if file in exclude_names:
            continue
        root, ext = os.path.splitext(file)
        path = os.path.join(dir, file)
        if (os.path.isfile(path) and ext in purge_exts) or (root in purge_names):
            files.append(path)
        elif os.path.isdir(path):
            files.extend(scandir(path))
    return files


print("Beginning Scan:\n")
to_purge = scandir("./src/")

print("\nListing Files:\n")
for name in to_purge:
    print("Will Delete: %s" % name)

answer = input("Delete the listed files? (y/N): ")

flag = False
if "yes" in answer:
    flag = True
if "no" in answer:
    flag = False
if "y" in answer:
    flag = True
if "n" in answer:
    flag = False

if not answer:
    flag = False

if flag:
    print("\nBeginning Purge:\n")
    for name in to_purge:
        print("Deleteing: %s" % name)
        if os.path.isdir(name):
            shutil.rmtree(name)
        else:
            os.remove(name)
print("DONE")
