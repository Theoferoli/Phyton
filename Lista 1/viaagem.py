distancia = float(input("Distância a percorrer (em km): "))
velocidade = float(input("Velocidade média esperada (em km/h): "))

tempo = distancia / velocidade
print(f"O tempo estimado da viagem é de {tempo:.2f} horas.")
