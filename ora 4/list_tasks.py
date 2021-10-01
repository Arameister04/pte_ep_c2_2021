import random

random.randint(3, 5)
random.random()

list = []
for i in range(20):
    list.append(random.randint(1, 101))

print(list)

list.sort()
print("A list maximum értéke:", list[-1])
print("A list minimum értéke:", list[0])