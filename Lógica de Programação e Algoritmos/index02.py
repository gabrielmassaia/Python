# a) O somatório dos 5 primeiros números inteiros e positivos:
n1 = int(input("Digite o primeiro número inteiro positivo: "))
n2 = int(input("Digite o segundo número inteiro positivo: "))
n3 = int(input("Digite o terceiro número inteiro positivo: "))
n4 = int(input("Digite o quarto número inteiro positivo: "))
n5 = int(input("Digite o quinto número inteiro positivo: "))
res = (n1 + n2 + n3 + n4 + n5)
print("O somatório dos 5 primeiros números inteiros e positivo é: ", res)

# b) A média entre 23,19 e 31
quant = (23 + 19 + 31)
media = (quant / 3)
print("A média entre 23, 19 e 31 é: %.2f" % media)
print(f"A média entre 23, 19 e 31 é: {media:.2f}")

# c) O número de vezes que 73 cabe em 403
quant = (403 / 73)
print(f"O numero 73 cabe {quant:.2f} dentro de 403")

# d) A sobra quando 403 é divido por 73
quant = (403 % 73)
print(f"A sobra quando 403 é divido por 73 é de: {quant:.2f}")

# e) 2 elevado a décima potência
quant = (2 ** 10)
print("O resultado de 2 elevado a décima pontência é de: ", quant)

# f) O valor absoluto da diferença entre 54 e 57
quant = (57 - 54)
print("O valor absoluto da diferença entre 54 e 57 é de: ", quant)

# g) O menor valor entre 34, 29 e 31
quant = min(34,29,31)
print(quant)

