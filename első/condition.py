number = 100
number2 = 200
if number < 10:
    print("Ez a szám kisebb, mint 10.")
else:
    print("Ez a szám nagyobb vagy egyenlő 10-zel.")

if number > 100:
    print("Ez a szám nagyobb, mint 100.")
else:
    print("Ez a szám nem nagyobb, mint 100.")

if number % 2 >0:
    print("A szám páratlan.")
else:
    print("A szám páros")


if number % number2 == 0:
    print("A", number2, "osztója a", number, "-nek.")
else:
    if number2 % number ==0:
        print("A", number, "osztója a", number2, "-nek.")

    else:
        print("Egyik sem osztója a másiknak")

string = "A balazs egy alma"
string_first = string[0]
string_last = string[-1]

if string_first == string_last:
    print("A mondat első és utolsó betűje megeggyezik.")
else:
    print("A mondat első és utolsó betűje nem egyezik meg.")

number = -10

if number == 0:
    print("Ez a szám nulla.")
elif number > 0:
    print("Ez a szám pozitív.")
else:
    print("Ez a szám negatív")

if number > 0:
    print("Ez a szám pozitív.")
    if number < 0:
        print("Ez a szám negatív.")
    else:
        print("Ez a szám a nulla")

if string[0].isupper():
    print("Nagybetűvel kezdődik.")
else:
    print("A nem nagybetűvel kezdűdik")

string2 = "almafa"
sting = "almafszár"
if string[0:5] == string2[0:5]:
    print("Az első öt karakter azonos")
else:
    print("Nem azonos az első 5 karakter.")
