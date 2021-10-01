my_list = [1, 2.5, "alma", False]
print("A lista hossza:", len(my_list))
print("A len() függvény visszatérési értékének típusa:", type(len(my_list)))

print("A lista tartalmazza-e a 2.5 értéket:", 2.5 in my_list)
print("Az in operátor eredményének típusa:", type(2.5 in my_list))

print("A lista tartalmazza-e a 2 értéket:", 2 in my_list)
print("Az in operátor eredményének típusa:", type(2 in my_list))

print("A 2.5 érték pozíciója:", my_list.index(2.5))
print("Az index() metódus visszatérési értékének típusa:", type(my_list.index(2.5)))

try:
    print("A 2 érték pozíciója:", my_list.index(2))
    print("Az index() metódus visszatérési értékének típusa:", type(my_list.index(2)))

except ValueError:
    print("hiba")


print("A lista 4. elemének lekérdezése:", my_list[3])
print("A lista 1. értékének típusa:", type(my_list[0]))
print("A lista 2. értékének típusa:", type(my_list[1]))
print("A lista 3. értékének típusa:", type(my_list[2]))
print("A lista 4. értékének típusa:", type(my_list[3]))


print("A fenti részlista típusa:", type(my_list[0:3]))
print("A lista első 3 eleme:", my_list[0:3])

my_list[2] = "körte"
print(my_list)

my_list.append(5)
print(my_list)

my_list.append([1, 2, 3])
print(my_list)


my_list.extend([1, 2, 3])
print(my_list)

my_list.insert(0, "start")
print(my_list)

del(my_list[6])
print(my_list)


while 1 in my_list:
    my_list.remove(1)
print(my_list)


my_list = [4, 7, 1, 4.5, 7, 6]
print(my_list)

my_list.sort()
print("A sort() metódus visszatérési értékének típusa:", type(my_list.sort()))
print(my_list)


my_list.sort(reverse = True)
print(my_list)


my_list.sort()
my_list.reverse()
print(my_list)


my_list2 = sorted(my_list)
print(my_list)
print(my_list2)

