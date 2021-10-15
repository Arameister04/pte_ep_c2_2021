sides = []
side_name = "a"
for i in range(3):
    side = 0
    while side == 0:
        try:
            side = float(input(f"Kérem adja meg a háromszög {side_name} oldalának értékét: "))
            if side > 0:
                if side_name == "a":
                    side_name = "b"
                else:
                    side_name = "c"
                sides.append(side)
            else:
                side = 0
                print("A háromszög csak pozitív valós szám lehet.")
        except ValueError:
            print("A megadott érték nem megfelelő.")

if sides[0] + sides[1] <= sides[2] or sides[1] + sides[2] <= sides[0] or sides[2] + sides[0] <= sides[1]:
    print("Nem háromszög oldalai.")
else:
    k = sides[0] + sides[1] + sides[2]
    d = k/2
    t = (d * ((d - sides[0]) * (d - sides[1]) * (d - sides[2]))) ** 0.5
    print("A háromszög kerülete {}, terület: {}".format(k, t))