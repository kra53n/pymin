"""
Analyze what type of packages were parsed
Three type of packages:
    - built-in
    - local
    - outside
"""

from sys import path as path_to_builtin
from os import listdir

from .find_mds import check_file


# NOTE:
# maybe some people don`t like this system of call
# so they can easily change it
# if you know how call them let me know about it
NAME_BUILTIN = "builtin"
NAME_LOCAL = "local"
NAME_OUTSIDE = "outside"


def slice_in_files_extension(files, extension=".py"):
    """

    """
    l = len(extension)
    for i in range(len(files)):
        if files[i][-l:] == extension:
            files[i] = files[i][:-l]

def parse_builtin_from_python_libs():
    """
    Parse built in modules in Python
    """
    # NOTE:
    # it must be smt like this
    # /usr/lib/pythonX.X
    # if you have difference please give me feedback
    # TODO: find it
    path = path_to_builtin[2]
    files = [f for f in listdir(path)]

    slice_in_files_extension(files)
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

def parse_builtin(pkgs):
    """
    Find builtin modules in project.
    Check pkgs with builtin Python modules
    """
    builtin_py = parse_builtin_from_python_libs()
    return [i for i in pkgs if i in builtin_py]

def parse_local(pkgs, files):
    local = []
    # clean pkgs
    for i in range(len(pkgs)):
        if "." in pkgs[i]:
            pkgs[i] = pkgs[i].replace(".", "")

    slice_in_files_extension(files)
    [local.append(fl) for fl in files if fl in pkgs]
    [files.remove(pkg) for pkg in local]
    return local

def parse_outside(pkgs, builtin, local):
    outside = []
    for pkg in pkgs:
        if (pkg not in builtin) and (pkg not in local):
            outside.append(pkg)
    return outside

def analyze_pkgs(pkgs, files):
    """
    Return dictionary with names of package`s type
    ===================ARGUMENTS==================
    pkgs - list of pkgs
    files - list of files that situated in cwd
    """
    builtin = parse_builtin(pkgs)
    local = parse_local(pkgs, files)
    outside = parse_outside(pkgs, local, builtin)
    return {NAME_BUILTIN: builtin, NAME_LOCAL: local, NAME_OUTSIDE: outside}


if __name__ == "__main__":
    analyze_pkgs(find_mds(), find_files()[1])
    # slice_in_files_extension()