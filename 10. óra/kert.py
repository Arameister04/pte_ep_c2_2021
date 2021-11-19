def menu_opciok():
    print("Kérem válasszon az alábbi menüpontok közül:\n\t0 - Kilépés\n\t1 - Új fa regisztrálása\n\t2 - Adott koordinátán lévő fafajta kiiratás"
          "\n\t3 - Fák és koordináták listázása\n\t4 - Fafajták listázása\n\t6 - Fafajta alapján koordináták listázása")

def egesz_szam_bekerese(koordinata: str) -> int:
    szam = ""
    while szam == "":
        try:
            szam = int(input(f"Kérem adja meg {koordinata} koordinátát"))
        except ValueError:
            print("Nem pozitív egész számot adott meg.")
    return szam

def fa_regisztralasa(fak: dict):
    x = egesz_szam_bekerese("x")
    y = egesz_szam_bekerese("y")
    hely = (x, y)
    if hely not in fak:
        fafajta = input("Kérem adja meg a fa fajtáját: ")
        fak[(x, y)] = fafajta
        print("Sikeres regisztráció.")
    else:
        print("Itt már áll egy fa, nem regisztálhat új fát ide.")

def fafajta_lekerdezese():
    x = egesz_szam_bekerese("x")
    y = egesz_szam_bekerese("y")
    hely = (x, y)
    if hely in fak:
        print("Ezen a koordinátán {} fajta fa áll.".format(fak[hely]))
    else:
        print("Ezen koordinátákon nem áll fa.")



def fafajtak_kiiratása(fak: dict):
    fajtak = []
    for i in fak:
        if fak[i] not in fajtak:
            print(fak[i])
            fajtak.append(fak[i])





def fafajta_koordinatai(fak: dict):
    fajta = input("Milyen fafajta koordinátákra kiváncsi: ")
    koordinatak = ""
    for i in fak:
        if fak[i] == fajta:
            koordinatak += str(i)
    if koordinatak == "":
        print("Nincs ilyen fafajta a kertben.")
    else:
        print("Ezen koordinátákon vannak {} fák: {}".format(fajta, koordinatak))


menu = ""
fak = {}
while menu != "0":
    menu_opciok()
    menu = input()
    if menu == "1":
        fa_regisztralasa(fak)
    elif menu == "2":
        fafajta_lekerdezese()
    elif menu == "3":
        print(fak)
    elif menu == "4":
        fafajtak_kiiratása(fak)
    elif menu == "6":
        fafajta_koordinatai(fak)
