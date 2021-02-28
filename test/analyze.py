def slice_in_files_extension(files, extension=".py"):
    l = len(extension)
    for i in range(len(files)):
        if files[i][-l:] == extension:
            files[i] = files[i][:-l]

local = []
pkgs = ["june", "april", "may"]
files = ["mart", "may", "april"]

[local.append(fl) for fl in files if fl in pkgs]
[files.remove(pkg) for pkg in local]
print(files, local)
