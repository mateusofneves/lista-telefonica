tempo_casa = int(input("Digite seu tempo de casa: "))
salario = float(input("Digite seu salario: "))

if tempo_casa < 3:
    aumento = salario * 0.05
else:
    aumento = salario * 0.10

novo_salario = salario + aumento

print("O seu salário foi de:", salario, "Para:", novo_salario)
print(f"O seu salário foi de R${salario:.2f} para R${novo_salario:.2f}")