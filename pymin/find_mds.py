"""
find_mds - find modules
"""

from os import walk
from os import path as os_path


IGNORE_DIRS = [".git"]
IGNORE_FILES = ["LICENSE"]


def dir_jogging(path, ignore_dirs=IGNORE_DIRS, ignore_files=IGNORE_FILES):
    """
    Argument path is path to directory.
    Function return:
        0) files that recieves from directory recursively.
        1) name of file from 0 point
    """
    pth = []
    file_names = []
    for root, dirs, files in walk(path):
        # skip directory with names in IGNORE_DIRS
        cont = False
        for name in ignore_dirs:
            if name in root:
                cont = True
        if cont:
            continue
            
        if files != 0:
            for file in files:
                if file in ignore_files:
                    continue
                pth.append(os_path.join(root, file))
                file_names.append(file)
    return pth, file_names

def find_string_in_file(path, find):
    """
    Arguments:
        0) path - path to file
        1) find - string that will be searched.
        Searching avoid various comments
    Return line that have `find` value
    """
    # help avoid long comments
    long_comment = False
    with open(path) as f:
        lines = f.readlines()

    suits = []
    for line in lines:
        # avoid comments
        if "//" in line:
            continue
        # NOTE: with condition that situated under can be problems
        if (find[0] in line[0]) and (find[1] not in line[1]):
            continue
        if ("'" == line[0]) and ("'" == line[-1]):
            continue
        if ('"' == line[0]) and ('"' == line[-1]):
            continue
        if (line.count("'''") == 2) or (line.count('"""') == 2):
            continue
        if (line.count("'''") == 1) or (line.count('"""') == 1):
            if long_comment:
                long_comment = False
            elif not long_comment:
                long_comment = True
        if (long_comment == False) and (find in line):
            suits.append(line.replace("\n", ""))
    return suits

def check_file(path, file, find_without_ext=True):
    """
    Check it is Python file or not
    Arguments:
        path - path to file with name of file
        file - name of file
        find_without_ext - find Python files without extension or not
    """
    if file[-3:] == ".py":
        return 1
    if find_without_ext == True:
        if "." not in file:
            if find_string_in_file(path, "#!/bin/python"):
                return 1

def get_py_files(path):
    """
    Argument:
        path - path to directory
    Return list of paths with Python files
    """
    py_path_to_files = []
    data = dir_jogging(path)
    path_files, files = data[0], data[1]
    for idx, path_file in enumerate(path_files):
        if check_file(path_file, files[idx]):
            py_path_to_files.append(path_file)
    return py_path_to_files

def deal_with_from_in_string(string):
    string = string[5:]
    first_space_index = 0
    for i in range(len(string)):
        if string[i] == " ":
            first_space_index = i
            break
    string = string[:first_space_index]
    return string

def remove_unnecessary_items(strings):
    for i in range(len(strings)):
        # remove spaces at the begining of string
        strings[i] = strings[i].lstrip()
        if "from" in strings[i]:
            strings[i] = deal_with_from_in_string(strings[i])
    return strings

def find_mds(path):
    """
    Argument path - path to directory
    """
    paths = get_py_files(path)
    strings = [find_string_in_file(p, "import") for p in paths]
    strings = list(itertools.chain.from_iterable(strings))
    strings = remove_unnecessary_items(strings)
    return list(set(strings))
