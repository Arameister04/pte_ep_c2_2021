import random

raw_input_data = input("Adj meg egy számot: ")
try:
    number = float(raw_input_data)
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

    number = 7
    if number >=3 and number <17:
        print("Beleesik a [3:17) intervallumba.")
    else:
        print("A szám nem esik bele a [3:17) intervallumba.")

    a, b, c = random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)
    print(a, b, c)
    if a + b > c and a + c > b and b + c > a:
        print("Lehet ezen oldalhosszakkal háromszöget szerkeszteni.")
    else:
        print("Nem lehet ezen oldalhosszakkal háromszöget szerkeszteni.")

    if a >= b and a >= c:
        print("Ez a szám a legnagyobb:", a)
    else:
        if b >= c:
            print("Ez a szám a legnagyobb:", b)
        else:
            print("Ez a szám a legnagyobb:", c)

    if a <= b and a <= c:
        print("Ez a szám a legkisebb:", a)
    if b <= a and b <= c:
        print("Ez a szám a legkisebb:", b)
    if c <= b and c <= a:
        print("Ez a szám a legkisebb:", c)

    charachter = "Á"
    maganhangzok = "aáréiíoóöőuúüűAÁEÉIÍOÓUÚÖŐÜŰ"
    if maganhangzok.find(charachter) >= 0:
        print("Ez a karakter magánhangzó.")
    else:
        print("Ez a karakter nem magánhangzó.")

    number = 15
    if number % 3 == 0 and number % 5 == 0:
        print("Ez a szám osztható hárommal és öttel is.")
    elif number % 3 == 0:
        print("Ez a szám csak hárommal osztható")
    elif number % 5 == 0:
        print("Ez a szám csak öttel osztható")
    else:
        print("Ez a szám nem osztható hárommal sem öttel:")

    jegy = random.randint(1, 5)
    if jegy == 5:
        print("kiváló")
    elif jegy == 4:
        print("jó")
    elif jegy == 3:
        print("közepes")
    elif jegy == 2:
        print("elégséges")
    elif jegy == 1:
        print("elégtelen")
    else:
        print("nem megfelelő érték")

    print(random.random())

except ValueError:
    print("De én egy számot kértem!")

