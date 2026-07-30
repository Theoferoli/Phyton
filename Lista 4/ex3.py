import random

v1 = []
v2 = []

for i in range(10):
    v1.append(random.randint(1, 100))
    v2.append(random.randint(1, 100))

v3 = []
for i in range(10):
    v3.append(v1[i])
    v3.append(v2[i])

print("Vetor 1:", v1)
print("Vetor 2:", v2)
print("Vetor 3 (Intercalado):", v3)
