km_percorridos = float(input("Quantidade de km percorridos: "))
dias_alugado = int(input("Quantidade de dias de aluguel: "))

preco_dias = dias_alugado * 60.00
preco_km = km_percorridos * 0.15
total_pagar = preco_dias + preco_km

print(f"O total a pagar é: R$ {total_pagar:.2f}")
