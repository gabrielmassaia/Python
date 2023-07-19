"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input("Digite o seu nome: ")
idade = input("Digite a sua idade: ")
if idade and nome != '':
   print("Seu nome é {}]".format(nome))
   print("Seu nome invertido é {}".format(nome[::-1]))
   print("Seu nome tem {} letras".format(len(nome)))
   print("A primeira letra do seu nome é {}".format(nome[0]))
   print("A última letra do seu nome é {}".format(nome[-1]))
else: 
   print("Desculpe, você deixou campos vazios, retorno e preencha todas as lacunas!")


