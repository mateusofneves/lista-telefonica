matriz = [[0, 0], [0, 0], [0, 0], [0, 0]]

print("Preencha a matriz... ")
for linha in range(4):
    for coluna in range(2):
        matriz[linha][coluna] = int(input(f"Matriz [{linha}][{coluna}]: "))

print("\nExibindo a matriz... ")
for linha in range(4):
    for coluna in range(2):
        #o \t força que a cada valor exibido ele dá uma tabulação e o end nao deixa ficar pulando as linhas.
        print(f"{matriz[linha][coluna]}\t", end = "")
    print()

soma = 0
for linha in range(4):
    for coluna in range(2):
        soma += matriz[linha][coluna]

print(f"\nSoma da matriz: {soma}")


