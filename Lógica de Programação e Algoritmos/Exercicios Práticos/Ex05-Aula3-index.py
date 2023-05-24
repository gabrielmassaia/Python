#a)
idade = int(input("Digite uma idade "))
if (idade > 60):
    print("Você tem direito aos benefícios")

#b)
dano = int(input("Qual o dano sofrido?: "))
escudo = int(input("Quantos pts de escudo você tem?: "))
if (dano > 10 and escudo == 0):
    print("You're dead!")

#c)
norte = True
sul = False
leste = False
oeste = False
if (norte == True or sul == True or leste == True or oeste == True):
    print("Você escapou!")
