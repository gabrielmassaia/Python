#Infos básicas
print('Olá, mundo!')
print(2 + 3)
print('2 + 3')
print("2" + "3")
print("Olá,","mundo")
print("O resultado de dois mais tres é:", 2 + 3)

#Atribuição
a = 1
b = 5
resposta = a == b
print(resposta)
resposta = a != b
print(resposta)

# Buscando informações
frase = "Olá, mundo"
print(frase)
print(frase[0])
print(frase[2])

#Concatenação
s1 = "Lógica de Programação"
s1 = s1 + " e Algoritmos"
print(s1)

#Repetindo strings na concatenação
s1 = "A" + '-' * 10 + "B"
print(s1)

#Composição
nota = 9
s1 = "Voce tirou %f na disciplina de Algoritmos" % nota
print(s1)

nota = 8.5
s1 = "Voce tirou %.2f na disciplina de Algoritmos" % nota
print(s1)

#Várias variáveis
nota = 8.5
disciplina = "Algoritmos"
s1 = "Você tirou %.2f na disciplina de %s" % (nota, disciplina)
print(s1)

#Composição moderna
nota = 8.7
disciplina = "Algoritmos"
s1 = "Você tirou {} na disciplina de {}" .format(nota, disciplina)
print(s1)

#Fatiamento
s1 = "Lógica de programação e Algoritmos"
print(s1[0:6])
s1 = "Lógica de programação e Algoritmos"
print(s1[24:34])
s1 = "Lógica de programação e Algoritmos"
print(s1[:6])

#length
s1 = "Lógica de programação e Algoritmos"
tamanho = len(s1)
print(tamanho)

#Funções de entrada
idade = int(input("Qual sua idade?: "))
print(idade)
print(idade + 1)

#Exercicio
n1 = int(input("Digite um numero?: "))
n2 = int(input("Digite um segundo numero?: "))
print(n1 + n2)