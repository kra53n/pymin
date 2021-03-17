from __init__ import return_mds
from os import getcwd


def print_mds(path):
    mds = return_mds(path)
    keys = mds.keys()
    message = ""
    for key in keys:
        message += "\n" + key.upper() + "\n"
        for i in range(len(mds[key])):
            message += "\t" + mds[key][i]
            if i != len(mds[key])-1:
                message += "\n"
    print(message[1:])


if __name__ == "__main__":
    print_mds(getcwd())