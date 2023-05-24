#a)
ano = int(input("Qual ano você quer descobrir se foi, é ou será bissexto?: "))
if (ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0):
    print("Pode ser um ano bissexto")
else:
    print("Definitivamente não é um ano bissexto")

#b
Cima = True
Baixo = True
if (Cima == True and Baixo == True):
    print("Decida-se")
else:
    print("Você escolheu um caminho!")