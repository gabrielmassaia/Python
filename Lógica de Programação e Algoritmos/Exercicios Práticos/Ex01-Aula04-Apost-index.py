#CALCULADORA
print("Calculadora em Python")
print("As opções são as seguintes:")
print("+ Adição")
print("- Subtração")
print("* Multiplicação")
print("/ Divisão")
print("Aperte qualquer outra tecla para cancelar.")

op = input("Qual operação deseja fazer?: ")
if op == "+" or op == "-" or op == "*" or op == "/": 
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))

while (op != "s"):
    if (op == "+"):
        res = n1 + n2
        print("Result: {} + {} = {}".format(n1, n2, res))
    elif (op == "-"):
        res = n1 - n2
        print("Result: {} - {} = {}".format(n1, n2, res))
    elif (op == "*"):
        res = n1 * n2
        print("Result: {} * {} = {}".format(n1, n2, res))
    elif (op == "/"):
        res = n1 / n2
        print("Result: {} / {} = {}".format(n1, n2, res))
    else:
        print("Operação inválida")
    
    op = input("Qual operação deseja fazer?: ")
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))

print("Encerrando o software...")