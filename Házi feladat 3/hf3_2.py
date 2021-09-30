price_of_item = input ("Kérem irja be a tárgy árát: ")

try:
    number = int(price_of_item)

    price_of_item_under_10k = number * 0.9
    price_of_item_over_10k = number * 0.8

    if number < 10000:
        print("A tárgy leárazott ára: ", price_of_item_under_10k, "Ft.")
    else:
     print("A tárgy leárazott ára: ", price_of_item_over_10k, "Ft.")

except ValueError:
    print("De én egy számot kértem!")