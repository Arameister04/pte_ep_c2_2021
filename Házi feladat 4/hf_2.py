a1 = int(input("Kérem adja meg egy mértani sorozat első elemét: "))
a2 = int(input("Kérem adja meg egy mértani sorozat második elemét: "))

q = a2 / a1

n = int(input("Kérem adja meg a sorozat n. tetszőleges elemét: "))
i = 1
q2 = a2 / a1
while i < n - 1:
    q2 = q2 * q
    i += 1
n_final = a1 * (q2)

print("A sorozat tetszőleges eleme nem más mint: ", n_final)