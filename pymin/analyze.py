"""
Analyze what type of packages were parsed
Three type of packages:
    - built-in
    - local
    - outside
"""


# NOTE:
# maybe some people don`t like this system of call
# so they can easily change it
# if you know how call them let me know about it
NAME_BUILTIN = "built-in"
NAME_LOCAL = "local"
NAME_OUTSIDE = "outside"


def extract_nested_lists_to_list(nested_lists):
    """
    [["", ""], [""], []] --> ["", "", ""]
    """
    pass

def nested_lists_to_list_or_list_to_list(lst):
    # check list on nesting in it other list(s)
    nested = False
    for i in lst:
        if type(i) == list:
            nested = True
    if nested == True:
        return list(chain(lst))
    if nested == False:
        return lst

lst_ex = [["malina", "brusnika"], ["123", "dsf"]]
print(nested_lists_to_list_or_list_to_list(lst_ex))

def analyze_pkgs(pkgs, files):
    """
    Return dictionary with names of package`s type
    ===================ARGUMENTS==================
    pkgs - list of pkgs
    files - list of files that situated in cwd
    """
    local = []



if __name__ == "__main__":
    pass
    #from find_pkgs import find_pkgs
    #analyze_pkgs(find_pkgs())
