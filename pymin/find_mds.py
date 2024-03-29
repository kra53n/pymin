from itertools import chain
from os import walk
from os import path as os_path

from constants import IGNORE_DIRS, IGNORE_FILES


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
        for name in ignore_dirs:
            if name not in root:
                break
        else:
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
    Return line that have `find` substring

    Arguments:
        0) path - path to file
        1) find - string that help find strings with find substring.
    """
    # help avoid long comments
    with open(path) as f:
        lines = [ls for line in f.readlines() if (ls := line.lstrip()) != '']

    # avoid comments
    suits = []
    long_comment = False
    for line in lines:
        if any(map(lambda x: x == 1, (line.count("'''"), line.count('"""')))):
            long_comment = False if long_comment else True
        if long_comment:
            continue

        if "//" in line or \
            "'import'" in line or \
            '"import"' in line or \
                (find[0] in line[0]) and (find[1] not in line[1]) or \
                ("'" == line[0]) and ("'" == line[-1]) or \
                ('"' == line[0]) and ('"' == line[-1]) or \
                any(map(lambda x: x == 2, (line.count("'''"), line.count('"""')))):
            continue
        if find in line:
            suits.append(line.replace("\n", ""))
    return suits


def check_file(path: str, file: str, find_without_ext: bool = True):
    """
    Check it is Python file or not
    Arguments:
        path - path to file with name of file
        file - name of file
        find_without_ext - find Python files without extension or not
    """
    if file[-3:] == ".py":
        return 1
    if find_without_ext:
        if "." not in file and find_string_in_file(path, "#!/bin/python"):
            return 1


def get_py_files(path):
    """
    Argument:
        path - path to directory
    Return list of paths with Python files
    """
    path_files, files = dir_jogging(path)
    py_paths = [path_file for idx, path_file in enumerate(path_files) if check_file(path_file, files[idx])]
    return py_paths


def deal_with_from_in_string(string):
    string = string[len("from "):]
    string = string[:string.index(" ")]
    return string


def remove_unnecessary_items(strings):
    for idx, val in enumerate(strings):
        strings[idx] = val.lstrip()
        if 'from' in val:
            strings[idx] = deal_with_from_in_string(val)
    return strings


def find_mds(path):
    """
    Argument path - path to directory
    """
    paths = get_py_files(path)
    strings = [find_string_in_file(p, "import") for p in paths]
    strings = list(chain.from_iterable(strings))
    strings = remove_unnecessary_items(strings)
    return list(set(strings))
