word = input("Kérek egy szót: ")
if word == word[::-1]:
    print("A szó egy palindrom!")
else:
    print("Ez a szó nem egy palindrom.")