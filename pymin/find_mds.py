"""
find_mds - find modules
"""

from os import walk
from os import path as os_path


IGNORE_DIRS = [".git"]


def dir_jogging(path):
    """
    Give information about directory. For example give
    adress to files, other directories and files
    Return information as dictionary
    """
    data = []
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
                data.append(os_path.join(root, file))
    return data

if __name__ == "__main__":
    from os import getcwd
    path = getcwd()
    [print(i) for i in dir_jogging(path)]