dias = int(input("Quantidade de dias: "))
horas = int(input("Quantidade de horas: "))
minutos = int(input("Quantidade de minutos: "))
segundos = int(input("Quantidade de segundos: "))

total_segundos = (dias * 24 * 3600) + (horas * 3600) + (minutos * 60) + segundos
print(f"O total em segundos é: {total_segundos}")
