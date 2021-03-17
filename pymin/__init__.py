from find_mds import find_mds
from find_mds import dir_jogging
from analyze import analyze_mds


def return_mds(path):
    return analyze_mds(find_mds(path), dir_jogging(path)[1])