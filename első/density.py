olom_suruseg = 11.34  #g/cm^3
rez_suruseg = 8.69  #g/cm^3
olom = 18  #cm^3
rez = 23  #cm^3

olom_nehezseg = olom * olom_suruseg
rez_nehezseg = rez * rez_suruseg

print("Az olom nehézsége: ", olom_nehezseg, "g.")
print("A réz nehézsége: ", rez_nehezseg, "g.")
print("Az ólom nehezebb:", olom_nehezseg > rez_nehezseg)