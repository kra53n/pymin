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
    ffs = find_files(path)
    files = ffs[1]
    dirs = ffs[2]
    del ffs

    slice_in_files_extension(files)
    pkgs = files + dirs
    del files, dirs
    print(pkgs)
    # what names it must skip
    skip = ()
    

def analyze_pkgs(pkgs, files):
    """
    Return dictionary with names of package`s type
    ===================ARGUMENTS==================
    pkgs - list of pkgs
    files - list of files that situated in cwd
    """
    builtin = []
    local = []
    outside = []

    # Try to find local pkgs
    slice_in_files_extension(files)
    [local.append(fl) for fl in files if fl in pkgs]
    [files.remove(pkg) for pkg in local]


if __name__ == "__main__":
    #analyze_pkgs(find_pkgs(), find_files()[1])
    parse_builtin()
