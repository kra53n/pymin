"""
Analyze what type of packages were parsed
Three type of packages:
    - built-in
    - local
    - outside
"""

from find_pkgs import find_files
from find_pkgs import find_pkgs


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

    # check local files
    slice_in_files_extension(files)
    for fl in files:
        if fl in pkgs:
            local.append(fl)
            files.remove(fl)
    print(files, local)


if __name__ == "__main__":
    analyze_pkgs(find_pkgs(), find_files()[1])
