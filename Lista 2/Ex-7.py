import math
area = float(input("Digite o tamanho da área a ser pintada (m²): "))
COBERTURA_POR_LITRO = 3
CAPACIDADE_LATA = 18
PRECO_LATA = 80.00
litros_necessarios = area / COBERTURA_POR_LITRO
quantidade_latas = math.ceil(litros_necessarios / CAPACIDADE_LATA)
preco_total = quantidade_latas * PRECO_LATA
print(f"Área a pintar      : {area:.2f} m²")
print(f"Litros necessários : {litros_necessarios:.2f} L")
print(f"Latas a comprar    : {quantidade_latas}")
print(f"Preço total        : R$ {preco_total:.2f}")


