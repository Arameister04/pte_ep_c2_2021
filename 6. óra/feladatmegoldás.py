import random
km_m = 1000
h_s = 3600
try:
    km_hour = float(input("Kérek egy sebességet km/h-ban: "))
    m_sec = km_hour * km_m / h_s
    print(f"A {km_hour} km/h sebesség az {m_sec} m/s-nak felel meg.")
except:
    print("Sajnálom de nemtudom átváltani.")



list1 = []
list2 = []
list3 = []

for i in range(20):
    list1.append(random.randint(0, 1000))

for i in list1:
    if i % 2 == 0:
        list2.append(i)
    else:
        list3.append(i)

print("A lista: ", list1)
print("Páros:", list2)
print("Páratlan:", list3)



