"""
Exemplo do Atacado

1.	Entre com o valor unitário do produto (Lembrar que número decimal é feito com ponto e não vírgula);
2.	Entre com a quantidade desse produto;
3.	O programa deve retornar o valor total sem desconto;
4.	O programa deve retornar o valor total após o desconto;
5.	Deve-se utilizar estruturas if, elif e else (EXIGÊNCIA 1 de 1);
6.	Colocar um exemplo de SAIDA DE CONSOLE de compra de mais de 10 und. (para mostrar que o desconto foi aplicado

Até 9	0% na unidade
Entre 10 e 99	5% na unidade
Entre 100 e 999	10% na unidade
De 1000 para mais	15% na unidade


"""

print( " " * 30 + "Bem Vindo ao Atacadista do Gabriel Massaia de Oliveira" + " " * 30)
print(" " * 100 )
print("Segue as informações sobre os descontos abaixo:")
print(" " * 100 )
print("-> Até 9x unidades. Desconto de 0% na unidade.")
print("-> Entre 10x e 99x unidades. Desconto de 5% na unidade.")
print("-> Entre 100x e 999x unidades. Desconto de 10% na unidade.")
print("-> A partir de 1000x unidades. Desconto de 15% na unidade.")
print(" " * 100 )

preco = float(input("Informe o preço do produto: "))
quant = float(input("Informe a quantidade do produto em unidades (uni x1...): "))
compra = preco*quant

if (quant <= 9):
    print("Essa quantidade de itens não da acesso ao desconto, o preço final é de R$ {:.2f}".format(compra))

elif ((quant >= 10) and (quant <=99)):
    valorComDesc = compra - compra*(5/100)
    print("Essa quantidade se enquadra em 5% de desconto na unidade")
    print("O preço sem desconto é de R$ {:.2f}".format(compra))
    print("O preço final, com desconto incluso é de R$ {:.2f}".format(valorComDesc))

elif ((quant >= 100) and (quant <=999)):
    valorComDesc = compra - compra*(10/100)
    print("Essa quantidade se enquadra em 10% de desconto na unidade")
    print("O preço sem desconto é de R$ {:.2f}".format(compra))
    print("O preço final, com desconto incluso é de R$ {:.2f}".format(valorComDesc))

elif (quant >= 1000):
    valorComDesc = compra - compra*(15/100)
    print("Essa quantidade se enquadra em 15% de desconto na unidade")
    print("O preço sem desconto é de R$ {:.2f}".format(compra))
    print("O preço final, com desconto incluso é de R$ {:.2f}".format(valorComDesc))

print( " " * 30 + "Atacadista do Gabriel Massaia de Oliveira agradece sua preferência, volte sempre!" + " " * 30)   






