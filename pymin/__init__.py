from find_mds import find_files
from find_mds import find_mds as fp

from analyze import analyze_pkgs


def find_mds():
    return analyze_pkgs(fp(), find_files()[1])
