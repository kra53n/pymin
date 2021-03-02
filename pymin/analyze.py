"""
Analyze what type of packages were parsed
Three type of packages:
    - built-in
    - local
    - outside
"""

from find_pkgs import find_files
from find_pkgs import find_pkgs

from sys import path as path_to_builtin
from os import listdir


# NOTE:
# maybe some people don`t like this system of call
# so they can easily change it
# if you know how call them let me know about it
NAME_BUILTIN = "built-in"
NAME_LOCAL = "local"
NAME_OUTSIDE = "outside"


def slice_in_files_extension(files, extension=".py"):
    l = len(extension)
    for i in range(len(files)):
        if files[i][-l:] == extension:
            files[i] = files[i][:-l]

def parse_builtin():
    """
    Parse built in modules in Python
    """
    # NOTE:
    # it must be smt like this
    # /usr/lib/pythonX.X
    # if you have difference please give me feedback
    path = path_to_builtin[2]
    files = [f for f in listdir(path)]

    slice_in_files_extension(files)
    #print([print(i) for i in files])
    # what names it must skip
    skip = ("pydoc_data", "config", "Tools")
    pkgs = []
    rm = []
    [pkgs.append(i) for i in files if "_" not in i[:1]]
    for i in skip:
        for j in pkgs:
            if i in j:
                rm.append(i)
    for i in pkgs:
        for j in skip:
            if j in i:
                pkgs.remove(i)
    return pkgs

# TODO: check working of this
#def parse_local(pkgs, files):
#    local = []
#    slice_in_files_extension(files)
#    [local.append(fl) for fl in files if fl in pkgs]
#    [files.remove(pkg) for pkg in local]
#    return local
    

def analyze_pkgs(pkgs, files):
    """
    Return dictionary with names of package`s type
    ===================ARGUMENTS==================
    pkgs - list of pkgs
    files - list of files that situated in cwd
    """
    builtin = parse_builtin()
    local = []
    outside = []

    # Try to find local pkgs
    slice_in_files_extension(files)
    [local.append(fl) for fl in files if fl in pkgs]
    [files.remove(pkg) for pkg in local]


if __name__ == "__main__":
    #parse_builtin()
    analyze_pkgs(find_pkgs(), find_files())
