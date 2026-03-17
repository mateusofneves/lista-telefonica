def nota_valida(nota):
    return 0 < nota < 10

nota1 = float(input("Digite a primeira nota: "))
if nota_valida(nota1):
    nota2 = float(input("Digite a segunda nota: "))
    if nota_valida(nota2):
        media = (nota1 + nota2) / 2
        print(f"A média dos valores é: {media}")
    else:
        print(f"A nota {nota2} é inválida.")
else:
    print(f"A nota {nota1} é inválida.")

