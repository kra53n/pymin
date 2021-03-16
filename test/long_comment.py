def find_string_in_file(path, find):
    long_comment = False
    with open(path) as f:
        lines = f.readlines()

    suits = []
    for line in lines:
        # avoid comments
        # if "//" in line:
        #     continue
        # # NOTE: with condition that situated under can be problems
        # if (find[0] in line[0]) and (find[1] not in line[1]):
        #     continue
        # if ("'" == line[0]) and ("'" == line[-1]):
        #     continue
        # if ('"' == line[0]) and ('"' == line[-1]):
        #     continue
        # if (line.count("'''") == 2) or (line.count('"""') == 2):
        #     continue
        if (line.count("'''") == 1) or (line.count('"""') == 1):
            print(line.count('"""'))
            if long_comment:
                print("Yeah312")
                long_comment = False
            elif not long_comment:
                print("Yeah123")
                long_comment = True
        if (long_comment == False) and (find in line):
            suits.append(line.replace("\n", ""))
    return suits


if __name__ == "__main__":
    path = "/home/kra53n/Рабочий стол/pymin/test/help.py"
    res = find_string_in_file(path, "print")
    print(res)