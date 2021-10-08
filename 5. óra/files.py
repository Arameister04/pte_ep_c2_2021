filepath = "lorem_copy.txt"
fileobject = open(filepath, "r+")
max_lenght = 0
max_row = ""
for line in fileobject:
    if len(line) > max_lenght:
        max_row = line
        max_lenght = len(line)
print(max_row)
fileobject.close()


