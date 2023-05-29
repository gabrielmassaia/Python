#Criando Tupla

def soma(*num):
    soma = 0
    print("Tupla: {}".format(num))
    for i in num:
        soma += i
    return soma

print("Resultado: {}\n".format(soma(1,2)))
print("Resultado: {}\n".format(soma(1,2,3,4,5,6,7,8,9)))

#Criando lista
item = []
mercado = []

for i in range(3):
    item.append(input("Digite o nome do item: "))
    item.append(int(input("Digite a quantidade: ")))
    item.append(float(input("Digite o valor: ")))
    mercado.append(item[:])
    item.clear()
print(mercado)

soma = 0
print("Lista de compras: ")
print("-" * 20)
print("Item | Quantidade | Valor unitário | Total do item")
for item in mercado:
    print("{} | {} | {} | {}".format(item[0], item[1], item[2], item[1] * item[2]))
    soma += item[1] * item[2]
print("-" * 20)
print("Total a ser pago: {}".format(soma))

# Outra Maneira
market = []

for i in range(3):
    nome = input("Digite o nome do item: ")
    qtd = int(input("Digite a quantidade: "))
    valor = float(input("Digite o valor: "))
    market.append([nome, qtd, valor])
print(market)

soma = 0
print("Lista de compras: ")
print("-" * 20)
print("Item | Quantidade | Valor unitário | Total do item")
for item in market:
    print("{} | {} | {} | {}".format(item[0], item[1], item[2], item[1] * item[2]))
    soma += item[1] * item[2]
print("-" * 20)
print("Total a ser pago: {}".format(soma))