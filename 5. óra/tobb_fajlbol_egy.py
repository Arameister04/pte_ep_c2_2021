fileobject1 = open("file1.txt", "r")
fileobject2 = open("file2.txt", "r")
fileobject3 = open("file3.txt", "r")
output_fileobject = open("fajl1_es_fajl2_es_fajl3", "w")
line1 = fileobject1.readline()
line2 = fileobject2.readline()
line3 = fileobject3.readline()
while line1 != "" or line2 != "" or line3 != "":
    output_fileobject.write(line1)
    output_fileobject.write(line2)
    output_fileobject.write(line3)
    line1 = fileobject1.readline()
    line2 = fileobject2.readline()
    line3 = fileobject3.readline()




fileobject1.close()
fileobject2.close()
fileobject3.close()
output_fileobject.close()