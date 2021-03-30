"""
Analyze what type of packages were parsed
Three type of packages:
    - built-in
    - local
    - outside
"""

from sys import path as sys_path
from sys import version as sys_version
from os import listdir


NAME_BUILTIN = "builtin"
NAME_LOCAL = "local"
NAME_OUTSIDE = "outside"


def slice_in_files_extension(files, extension=".py"):
    l = len(extension)
    for i in range(len(files)):
        if files[i][-l:] == extension:
            files[i] = files[i][:-l]

def py_version(ver=sys_version):
    """
    From sys_version it slice to 2 digits.
    Return result as string
    """
    index = 0
    for i in range(len(ver)):
        if "." in ver[i]:
            index += 1
        if index == 2:
            index = i
            break
    return ver[:index]

def path_to_builtin(lst=sys_path):
    """
    From list in sys_path it parse path to Python
    where situated his Libs
    """
    return [i for i in sys_path if i[9:len(i)-len(py_version())] == "python"][0]

def parse_builtin_from_python_libs():
    """
    Parse built in modules in Python
    """
    path = path_to_builtin()
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

def check_builtin(pkgs):
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

def analyze_mds(mds, files):
    """
    Return dictionary with names of package`s type
    ===================ARGUMENTS==================
    mds - list of mds
    files - list of files that situated in cwd
    """
    builtin = check_builtin(mds)
    local = parse_local(mds, files)
    outside = parse_outside(mds, local, builtin)
    return {NAME_BUILTIN: builtin, NAME_LOCAL: local, NAME_OUTSIDE: outside}
