valorh=float(input("quanto você ganha por hora em R$?: "))
horas=float(input("quantas você trabalhou no mês?: "))
salario_bruto=valorh*horas
ir=salario_bruto*0.11
inss=salario_bruto*0.08
sindicato=salario_bruto*0.05
salario_liquido=salario_bruto - (ir+ inss + sindicato)
print(f"+ Salário Bruto   : R$ {salario_bruto:.2f}")
print(f"- IR (11%)        : R$ {ir:.2f}")
print(f"- INSS (8%)       : R$ {inss:.2f}")
print(f"- Sindicato (5%)  : R$ {sindicato:.2f}")
print(f"= Salário Líquido : R$ {salario_liquido:.2f}")
