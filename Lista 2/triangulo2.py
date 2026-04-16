
a = float(input("Informe o lado A: "))
b = float(input("Informe o lado B: "))
c = float(input("Informe o lado C: "))
if (a + b > c) and (a + c > b) and (b + c > a):
    print("Os valores formam um triângulo")
    if a == b == c:
        print("Tipo: Equilátero")
    elif a == b or a == c or b == c:
        print("Tipo: Isósceles")
    else:
        print("Tipo: Escaleno")

else:
    print("Os valores NÃO formam um triângulo")
