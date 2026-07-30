
import random

lista_original = []
PAR = []
IMPAR = []

for i in range(20):
    numero = random.randint(1, 100)
    lista_original.append(numero)

for numero in lista_original:
    if numero % 2 == 0:
        PAR.append(numero)
    else:
        IMPAR.append(numero)

print("Lista Original:", lista_original)
print("Pares:", PAR)
print("Ímpares:", IMPAR)
