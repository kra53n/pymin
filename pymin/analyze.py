"""
Analyze what type of packages were parsed
Three type of packages:
    - built-in
    - local
    - outside
"""

from itertools import product
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
    return ver[:ver.find(' ')]

def path_to_builtin(lst=sys_path):
    """
    From list in sys_path it parse path to Python
    where situated his Libs
    """
    res = [i[9:] for i in sys_path if i[9:len(i)-len(py_version())] == 'python']
    return res[0] if res else res

def parse_builtin_from_python_libs():
    """
    Parse built in modules in Python
    """
    path = path_to_builtin()
    if not path:
        return path
    files = [f for f in listdir(path)]

    slice_in_files_extension(files)
    skip = ("pydoc_data", "config", "Tools")
    pkgs = []
    rm = []

    for i in files:
        if '_' not in i[:1]:
            pkgs.append(i)

    for i, j in product(skip, pkgs):
        if i == j:
            rm.append(i)

    for i, j in product(pkgs, skip):
        if j in i:
            pkgs.remove(i)

    return pkgs

def check_builtin(pkgs):
    """
    Find builtin modules in project.
    Check pkgs with builtin Python modules
    """
    return [i for i in pkgs if i in parse_builtin_from_python_libs()]

def parse_local(pkgs, files):
    local = []
    # clean pkgs
    pkgs = [pkg.replace(".", "") if "." in pkg else pkg for pkg in pkgs]

    slice_in_files_extension(files)
    local.extend([file for file in files if file in pkgs])
    for pkg in local:
        files.remove(pkg)

    return local

def parse_outside(pkgs, builtin, local):
    return [pkg for pkg in pkgs if all(map(lambda x: pkg not in x, (builtin, local)))]

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
