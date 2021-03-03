from find_pkgs import find_files
from find_pkgs import find_pkgs as fp

from analyze import analyze_pkgs


def find_pkgs():
    return analyze_pkgs(fp(), find_files()[1])
