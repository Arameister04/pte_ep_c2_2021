from easygui import *


msgbox("Hello There °-°!", title="Hello", ok_button="Hi")


flavour = buttonbox("What is your favourite ice cream flavor?", title="Icecream", choices=['Vanilla[1]', 'Chocolate[2]', 'Strawberry[3]'], default_choice="Vanilla[1]")

msgbox("You picked " + flavour)