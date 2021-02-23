from os import getcwd
from os import walk
from os import path


CWD = getcwd()
START_STRING = (
    "from",
    "import"
)


def check_file(path):
    """
    Check python file it is or not
    """
    if path[-3:] == ".py":
        return 1
    if "." not in path:
        # NOTE: it can`t work if file will begin as empty string
        # so if someone will find problem with it
        # he can change it and write me about this
        with open(path) as f:
            line = f.readline()
        if line == "#!/bin/python":
            return 1

def find_files(cwd=CWD):
    """
    Return full path to files in cwd where
    was run script
    """
    # TODO: don`t forget replace cwd
    cwd = "/home/kra53n/Рабочий стол/tetris"
    paths = []
    for address, dirs, files in walk(cwd):
        if files != 0:
            for fl in files:
                pth = path.join(address, fl)
                if check_file(pth):
                    paths.append(pth)
    return paths


if __name__ == "__main__":
    [print(path) for path in find_files()]
