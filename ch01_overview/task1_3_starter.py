"""

      task1_3_starter.py   -   Sorting, sequences, and file size sorter utility

      This script will prompt for a path (and/or) pattern to search.
      It should display a list of files matching that path in order of largest
      to smallest


      Additional tips:

      1. Prompt for a path to search.  Example: ../resources or . or /temp

      2. Perform a os.listdir(path) search which returns a list of strings of items within the directory

      3. Create a list to store new results.  Iterate over os.listdir() list of strings,
         check each result to see if it is a file.  Hint: use os.path.isfile(filename)

      4. For each file, get the file size.  append() the filename AND the file size as a tuple into the new list
         that you created in step 3.  Sub-directories should not be appended into the list.  (e.g., you are creating
         a list of tuples that contain a filename and file size for each tuple added to the new list.

      5. Sort the list according to file size.  Hint: use the list.sort() or sorted(), create a function or lambda
         that will work with the key= argument for sort.

      6. Display the sorted list results.

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

"""import os
path = input('Path relative or absolute directory to search: ')        # example: ../resources
dir_contents = os.listdir(path)
files = []
for file_item in dir_contents:
    fullpath = os.path.join(path, file_item)
    if os.path.isfile(fullpath):
        print("file_item is" ,file_item)
        file_tuple = (file_item, os.stat(fullpath).st_size)
        print("file_tuple is = " , file_tuple)
        files.append((file_item, os.stat(fullpath).st_size))
        #is a list of tuples..   [("myfile.txt",42), ("yourfile.txt",132) .... }
print("files = " , files)
files.sort(key=lambda name_size: name_size[1], reverse=True)
print("files = " , files)
for name, size in files:
    print('{name:<30}{size:10}'.format(name=name, size=size))"""
