print("Escolha o que deseja comprar")
print("1 - Banana")
print("2 - Laranja")
print("3 - Maçã")
produto = int(input("Qual sua escolha? "))
qtd = int(input("Quantas unidades? "))

if (produto == 1):
    pagar = qtd * 2.3
    print("Você comprou {} bananas. Total a pagar: {}".format(qtd, pagar))
else:
    if (produto == 2):
        pagar = qtd * 3.6
        print("Você comprou {} laranjas. Total a pagar {}".format(qtd, pagar))
    else:
        if (produto == 3):
            pagar = qtd * 1.85
            print("Você comprou {} maçãs. Total a pagar {}".format(qtd, pagar))
        else:
            print("Produto não cadastrado!")