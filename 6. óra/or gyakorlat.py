a, b = 2, 4
if a == 4 or b != 4:
    print("Nyert")
if a == 4 or b == 4:
    print("Majdnem nyert")


number = int(input("Kérek egy számot: "))
if number != 2:
    print("vesztett")
elif number == 3:
    print("kis türelmet kérek")
else:
    print("Nyert")