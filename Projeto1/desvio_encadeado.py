salario = float(input("Qual o seu salario: "))

if salario <= 1900:
    ir = 0
elif salario <= 2800:
    ir = salario * 0.15
else:
    ir = salario * 0.275

sal_liquido = salario - ir

print(f"Seu imposto de renda é: {ir:.2f}")
print(f"Seu salário líquido é: {sal_liquido}")