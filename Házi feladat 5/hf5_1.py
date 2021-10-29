filepath = "lorem_copy.txt"
fileobject = open(filepath, "r")
lines = fileobject.readlines()
print("A sorok száma: ", len(lines))
fileobject.close()


fileobject = open(filepath, "r")
characters = fileobject.read().replace(" ", "")
len_of_char = len(characters)
print("A karakterek száma: ", len_of_char)
fileobject.close()
