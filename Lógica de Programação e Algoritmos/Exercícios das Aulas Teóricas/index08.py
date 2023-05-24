#a)
x = 1
while (x <= 5):
    print(x)
    x = x + 1 

#b)
inicial = int(input("Com qual valor deseja iniciar a contagem?: "))
final = int(input("Com qual valor deseja encerrar a contagem?: "))
x = inicial
while (x <= final):
    if (x % 2 == 0):
        print(x)
    x = x + 1

#c)
soma = 0
cont = 1
while (cont <= 5):
    x = float(input("Digite a {} nota: ".format(cont)))
    soma = soma + x
    cont = cont + 1
media = soma / 5
print("Média final: {}".format(media))
    