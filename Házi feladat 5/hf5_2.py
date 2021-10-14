fileobject = open("hazi feladat 2.txt", "w")

x = 1
while (x <= 10):
    row = ""
    y = 1
    while (y <= 10):
        row += format(x * y, ">4")
        y += 1
    fileobject.write(row)
    print(row)
    x += 1


fileobject.close()
