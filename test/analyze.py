from sys import path as sys_path
from sys import version as sys_version
from os import listdir

from find_mds import dir_jogging
from find_mds import check_file

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

def parse_builtin():
    """
    From path_to_builtin it parse files with
    Python extension(only `.py`)
    """
    files = [f for f in dir_jogging(path_to_builtin())[1] if check_file(0, f, 0)]
    return files
    # files_that_suit = []
    # files_in_dir = dir_jogging(parse_builtin())[1]
    # return files_in_dir

if __name__ == "__main__":
    # print(dir_jogging(path_to_builtin())[1])
    print(parse_builtin())
    # print(path_to_builtin())
    # print(py_version("3.12.12312331"))