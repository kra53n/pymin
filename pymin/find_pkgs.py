from os import getcwd, walk, path


PATH = getcwd()
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

def find_files(PATH=PATH):
    """
    Return full path to files as list in PATH where
    was run script
    """
    # TODO: USE HERE find_files_full_information
    paths = []
    py_files = []
    for address, dirs, files in walk(PATH):
        if files != 0:
            for fl in files:
                pth = path.join(address, fl)
                if check_file(pth):
                    paths.append(pth)
                    py_files.append(fl)
    return paths, py_files, dirs

def find_pkgs_in_file(path):
    pkgs = []
    with open(path) as f:
        lines = f.readlines()
    for line in lines:
        if START_STRING[0] in line:
            words = line.rstrip().split()
            # sometimes you can find `from` in documentations
            # and etc. For solve this probem script check
            # in what order does it stand
            # NOTE: but it is not full solving of problem
            # and once it can be fixed
            if START_STRING[0] == words[0]:
                pkgs.append(words[1])
        if START_STRING[1] in line[:7]:
            pkgs.append(line.rstrip()[7:])
    return pkgs

def find_pkgs(PATH=PATH):
    pkgs = []
    paths = find_files(PATH)[0]
    for path in paths:
        pkgs.extend(find_pkgs_in_file(path))
    return list(set(pkgs))


if __name__ == "__main__":
    [print(i) for i in find_pkgs()]
    [print(i) for i in find_files()[1]]