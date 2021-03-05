from __init__ import find_pkgs

# TODO:
# remake architecture

def print_pkgs(pkgs=find_pkgs()):
    message = "Builtin:\n"
    for i in pkgs["builtin"]:
        message += "  " + i + "\n"
    message += "Local:\n"
    for i in pkgs["local"]:
        message += "  " + i + "\n"
    message += "Outside:\n"
    for i in pkgs["outside"]:
        message += "  " + i + "\n"
    print(message[:-1])

print_pkgs()
