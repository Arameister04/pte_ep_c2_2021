list1 = []
while len(list1) == 0 or list1[len(list1) - 1] != "":
    list1.append(input())
list1.remove("")
print(list1)

