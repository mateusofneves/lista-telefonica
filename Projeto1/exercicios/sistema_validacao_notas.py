def nota_valida(nota):
    return 0 <= nota <= 10

print("Sistema de Validação de notas. \n")

while True:
    nota1 = float(input("Digite a primeira nota: "))
    while not nota_valida(nota1):
        print("Nota inválida, digite novamente.")
        nota1 = float(input("Digite a primeira nota: "))

    nota2 = float(input("Digite a segunda nota: "))
    while not nota_valida(nota2):
        print("Nota inválida, digite novamente.")
        nota2 = float(input("Digite a segunda nota: "))
        print()

    media = (nota1 + nota2) / 2
    print()
    print(f"A nota {nota1} e {nota2} dão a média: {media}.")

    print()
    continuar = str(input("Deseja continuar? [S/N] ")).upper()
    print()
    if continuar != "S":
        print("Encerrado.")
        break