nome = input("Qual o seu nome?: ")
altura = float(input("Qual a sua altura (em cm)?: "))
altura_metros = altura / 100
peso = float(input("Qual o seu peso (em kg)?: "))
imc = peso / (altura_metros**2)

#Formatação de string
linha_1 = f"{nome} tem {altura:.2f} de altura"
linha_2 = f"pesa {peso} kg e seu IMC é de {imc:.2f}"
linha_3 = f"IMC = {imc:.3f}"
print(linha_1)
print(linha_2)
print(linha_3)


""" print(nome, "tem", altura, "de altura")
print("pesa", peso, "quilos e seu IMC é de", imc) """