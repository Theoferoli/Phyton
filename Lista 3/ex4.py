n = int(input("Digite qual termo de Fibonacci você quer descobrir: "))
a, b = 1, 1

# O laço roda (n - 1) vezes para avançar até a posição desejada
for _ in range(n - 1):
    a, b = b, a + b

print(f"O {n}º termo da sequência é: {a}")
