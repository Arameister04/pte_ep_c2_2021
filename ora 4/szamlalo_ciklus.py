i = 1                           #1 feladat
while i <= 10:
    print(i, end = " ")
    i += 1
print()
for j in range(1, 11):          #1 feladat
    print(j, end = " ")
print()
for j in range(10):             #1 feladat
    print(j + 1, end = " ")
print()
#Innentől második feladat

i = 1
while i <=6:
    print(i * 2 - 1, end = " ")
    i += 1
print()
for j in range(1, 12, 2):
    print(j, end = " ")
print()

#Innentől harmadik feladat

a1 = 0
a2 = 1
print(a1, a2, end = " ")
i = 0
while i < 8:
    an = a1 + a2
    a1 = a2
    a2 = an
    print(an, end = " ")
    i += 1




