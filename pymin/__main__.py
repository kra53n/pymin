from __init__ import return_mds
from os import getcwd


def print_mds(path):
    mds = return_mds(path)
    message = ""
    for moudule_type, values in mds.items():
        message += "\n" + moudule_type.upper() + "\n"
        for value in values:
            message += "\t" + value + "\n"
    print(message[1:])


if __name__ == "__main__":
    path = '../pytouch/pytouch'
    print_mds(path)
