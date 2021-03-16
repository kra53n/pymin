"""
find_mds - find modules
"""

from os import walk
from os import path as os_path


IGNORE_DIRS = [".git"]


def dir_jogging(path):
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
        for name in IGNORE_DIRS:
            if name in root:
                cont = True
        if cont:
            continue
            
        if files != 0:
            for file in files:
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

def check_file(path, file):
    """
    Check it is Python file or not
    Arguments:
        path - path to file with name of file
        file - name of file
    """
    if file[-3:] == ".py":
        return 1
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
    for i in range(len(data[0])):
        if check_file(path_files[i], files[i]):
            py_path_to_files.append(path_files[i])
    return py_path_to_files

def matrix_to_list(matrix):
    """
    From [[21, 12], [3, 4], [9,0]] function
    return [21, 12, 3, 4, 9, 0]
    """
    lst = []
    for i in matrix:
        lst.extend(i)
    return lst

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
    strings = matrix_to_list(strings)
    strings = remove_unnecessary_items(strings)
    return list(set(strings))

if __name__ == "__main__":
    from os import getcwd
    path = "/home/kra53n/Рабочий стол/getgit"
    md = find_mds(path)
    [print(i) for i in md]