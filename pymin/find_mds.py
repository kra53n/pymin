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

def check_file(path, file):
    """
    Check it is Python file or not
    Arguments:
        path - path to file with name of file
        file - file
    """
    if file[-3:] == ".py":
        return 1
    if "." not in file:
        py_file = False
        py_string = "#!/bin/python"
        long_comment = False
        with open(path) as f:
            lines = f.readlines()

        for line in lines:
            # avoid comments
            if "//" in line:
                continue
            # NOTE: with condition that situated under can be problems
            if (py_string[0] in line[0]) and (py_string[1] not in line[1]):
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
                if not long_comment:
                    long_comment = True
            if (long_comment == False) and (py_string in line):
                return 1


if __name__ == "__main__":
    from os import getcwd
    path = getcwd()
    data = dir_jogging(path)
    # [print(data[0][i], "\t"*3, data[1][i]) for i in range(len(data[0]))]
    path_file, file = data[0][4], data[1][4]
    print(path_file, file)
    print(check_file(path_file, file))