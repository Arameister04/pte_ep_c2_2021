import easygui

year_str = easygui.enterbox("Kérem adjon meg egy évszámot", title="Adatbekérés")

try:
    year = int(year_str)
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 ==0:
                easygui.msgbox("A megadott év osztható négyszázzal maradék nélkül tehát szökőév.", title="Szökőév")
            else:
                easygui.msgbox("A megadott év nem osztható négyszázzal, osztható százzal ezél nem szökőév .", title="Nem szökőév.")
        else:
            easygui.msgbox("Ez az év szökőév mert 4-gyel osztható, de 100-al nem.",title="Szökőév.")
    else:
        easygui.msgbox("Ez az év nem szökőév, mert nem osztható 4-gyel", title="Nem szökőév.")

except ValueError:
    easygui.msgbox("Nem megfelelő évszám", title="Hiba")

