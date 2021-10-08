number = 5
number2 = number * 2
print("A number változó értéke az nem más mint:", number, "\b. Ha ezt megszorzom kettővel, akkor:", number2, "\b-t kapok.")
print("A number változó értéke az nem más mint: ", number, ". Ha ezt megszorzom kettővel, akkor: ", number2, "-t kapok." , sep="")
print(f"A number változó értéke az nem más mint: {number}. Ha ezt megszorzom kettővel, akkor: {number2}-t kapok.")
print("A number változó értéke az nem más mint: {}. Ha ezt megszorzom kettővel, akkor: {}-t kapok.".format(number, number2))


# Igazítasok
print(f"A number változó értéke az nem más mint: {number:<3}. Ha ezt megszorzom kettővel, akkor: {number2:>5}-t kapok.")
print("A number változó értéke az nem más mint: {:^3}. Ha ezt megszorzom kettővel, akkor: {:^5}-t kapok.".format(number, number2))

# Számformátumok
number = 125
print(f"A szám lineáris alakja: {number:b}, az oktális alakja: {number:o}, a decimális alakja: {number:d}, a hexadecimális alakja: {number:x} és {number:X}")
print("A szám lineáris alakja: {:b}, az oktális alakja: {:o}, a decimális alakja: {:d}, a hexadecimális alakja: {:x} és {:X}".format(number, number, number, number, number))


number = 65
print(f"{number:c}")
print("{:c}".format(number))


number = 100.12345
print(f"Tudományos: {number:e} vagy {number:E}")
print(f"Valós szám: {number:f}")
print(f"3 tizedesjegy pontosság: {number:.3f}")
print(f"15 karakteren: {number:15f}")
print(f"15 karakteren 3 tizedesjegy pontossággal: {number:15.3f}")
print(f"3 tizedesjegy pontosság: {number:.3%}")
print(f"15 karakteren: {number:15%}")
print(f"15 karakteren 3 tizedesjegy pontossággal: {number:15.3%}")
