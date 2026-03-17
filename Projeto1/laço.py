#EXEMPLO 1 de while com S e N
#opcao = input("Digite S para sim ou N para não. ")

#while opcao != 'S' and opcao != 'N' and opcao != 's' and opcao != 'n':
#    print(f"Vc digitou {opcao}. Digite 'S' ou 'N' apenas.")
#    opcao = input("Digite S para sim ou N para não. ")

#print(f"Vc digitou {opcao}.")




#EXEMPLO 2 soma os números até que venha um negativo e depois mostra a soma
#soma = 0

#while True:
#    num = int(input("Digite um número. "))
#    if num > 0:
#        soma = soma + num
#    else:
#        break

#print(f"Soma: {soma}")


num = int(input("Digite 5 números. "))
menor = num
for cont in range(1, 5, 1):
    num = int(input())
    if num < menor:
        menor = num

print(f"Menor número: {menor}")


