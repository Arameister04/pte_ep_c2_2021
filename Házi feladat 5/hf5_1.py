filepath = "lorem_copy.txt"
fileobject = open(filepath, "r")
lines = fileobject.readlines()
characters = fileobject.read()
print("A sorok száma: ", len(lines))
print("A karakterek száma: ", len(characters))
fileobject.close()
