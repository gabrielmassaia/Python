nome = input("Digite um nome: ")
idade = int(input("Qual a idade?: "))
if (nome == "Vinicius"):
    print("Olá Vinicius")
elif (nome != "Vinicius" and idade < 18):
    print("Essa pessoa não se chama Vinicius e é menor de idade")
elif (nome != "Vinicius" and idade > 100):
    print("Essa pessoa possivelmente não existe")

