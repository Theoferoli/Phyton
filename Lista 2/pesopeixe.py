peso=float(input("digite o peso dos peixes em kg: "))
limite=50
valor_multa_kg=4.00
if peso>limite:
    excesso= peso-limite
    multa=excesso*valor_multa_kg
else:
    excesso = 0
    multa = 0.0

print(f"Peso total: {peso:.2f} kg")
print(f"Excesso: {excesso:.2f} kg")
print(f"Valor da Multa: R$ {multa:.2f}")
