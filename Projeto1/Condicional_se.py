venda = float(input("Digite o valor: "))

if venda > 300:
    desconto = venda * 10 / 100
    venda = venda - desconto
print("Novo valor: ", venda)
