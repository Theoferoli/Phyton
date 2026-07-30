import random

lista = []
for i in range(10):
    numero = random.randint(1, 100)
    lista.append(numero)

maior = lista[0]
menor = lista[0]

for num in lista:
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print("Lista:", lista)
print("Maior:", maior)
print("Menor:", menor)
