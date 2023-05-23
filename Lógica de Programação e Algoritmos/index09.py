#Validação de dados
x = int(input("Digite um valor maior do que zero: "))
while (x <= 0):
    x = int(input("Digite um valor maior do que zero: "))
print("Vc digitou {}. Encerrando o software...".format(x))

#Instrução break
print("Escreva uma mensagem para repetição: ")
print("Caso queira encerrar, digite 'sair'.")
while True:
    texto = input("")
    print(texto)
    if texto == "sair":
        break
print("Encarrando software...")

#Continue
while True:
    nome = input("Qual o seu nome?: ")
    if (nome != "Gabriel"):
        continue
    senha = input("Qual a sua senha?: ")
    if (senha == "Massaia"):
        break
print("Acesso concedido.")

#Truthy and Falsey
nome = ""
while not nome:
    nome = input("Digite seu nome: ")
valor = int(input("Digite um número qualquer: "))
if valor:
    print("Vc digitou um valor diferente de zero")
else:
    print("Vc digitou zero")


