"""

      task1_3.py   -   Sorting, sequences, and file size sorter utility (solution)

      This script will prompt for a path (and/or) pattern to search.
      It displays the list of files in order of largest to smallest

"""
import os

path = input('Path relative or absolute directory to search: ')        # example: ../resources
dir_contents = os.listdir(path)
files = []
for file_item in dir_contents:
    fullpath = os.path.join(path, file_item)
    if os.path.isfile(fullpath):
        files.append((file_item, os.stat(fullpath).st_size))

files.sort(key=lambda name_size: name_size[1], reverse=True)

for name, size in files:
    print('{name:<30}{size:10}'.format(name=name, size=size))
