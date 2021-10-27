import random

import easygui

easygui.msgbox("Gondoltam egy számra 1 és 99 között, 6 próbálkozásod van kitalálni.", ok_button="Induljon a játék!")

bot_number = random.randint(1, 99)
tries = 1
tip = ""
try:
    while tries <= 6 and tip != bot_number:
        tip = int(easygui.enterbox("Próbáld kitalálni a számot", title="Próbálkozás: " + str(tries)))
        if tip > bot_number:
            print("Kisebb számra gondoltam.")
        if tip < bot_number:
            print("Nagyobb számra gondoltam.")
        if tip == bot_number:
            easygui.msgbox("Gratulálunk nyertél " + str(tries) + " próbálkozásból!", title="Gratulálunk")
        tries += 1
        if tries == 7:
            easygui.msgbox("Sajnálom vesztettél a keresett érték: " + str(bot_number) + " volt.", title="Lejárt a 6 próbálkozás")
except ValueError:
    easygui.msgbox("Nem megfelelő érték.", title="Hibás")





















