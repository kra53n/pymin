from os import getcwd

from find_mds import find_mds, dir_jogging
from analyze import analyze_mds


def return_mds(path):
    return analyze_mds(find_mds(path), dir_jogging(path)[1])


def print_mds(path):
    mds = return_mds(path)
    sep = '\n\t'
    message = '\n'.join([f"{module_type.upper()}\n\t{sep.join((v for v in values))}"
                         for module_type, values in mds.items()])
    print(message)


if __name__ == "__main__":
    path = getcwd()
    print_mds(path)
