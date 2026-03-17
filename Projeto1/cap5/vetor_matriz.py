# -----------------------------
# EXEMPLO 1 - Preencher a lista
# -----------------------------
lista = []
for cont in range(5):  # vai de 0 a 4
    x = float(input("Digite um número: "))
    lista.append(x)

print("\nLista digitada:")
print(lista)
print("\n" * 2)

# -----------------------------
# EXEMPLO 2 - Imprimir usando índices
# -----------------------------
print("Imprimindo usando índices:")
for i in range(len(lista)):
    print(lista[i])

print("\n" * 2)

# -----------------------------
# EXEMPLO 3 - Imprimir elementos diretamente
# -----------------------------
print("Imprimindo elementos diretamente:")
for elem in lista:
    print(elem)

print("\n" * 2)

# -----------------------------
# EXEMPLO 4 - Somar todos os elementos
# -----------------------------
soma = 0
for elem in lista:
    soma += elem

print(f"Soma = {soma}")
print("\n" * 2)

# -----------------------------
# EXEMPLO 5 - Buscar um elemento na lista
# -----------------------------
achou = False
elem = float(input("Digite o elemento a buscar: "))

for i in range(len(lista)):
    if lista[i] == elem:
        achou = True
        break

if achou:
    print("Elemento encontrado!")
else:
    print("Elemento não encontrado!")