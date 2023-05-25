#Function
def realce():
    print('|', '_' * 10, "|")
    print('|', '_' * 10, "|")

realce()
print("     MENU")
realce()

#Passando parametros
def realce(s1):
    print('|', '_' * 10, "|")
    print('|', '_' * 10, "|")
    print(s1)
    print('|', '_' * 10, "|")
    print('|', '_' * 10, "|")

realce("     Gabe")

#Mais de um parametro dentro da função
def sub2(x, y):
    res = x-y
    print(res)

sub2(5,7)

#Omitindo parametros
def soma3(x = 0, y = 0, z = 0):
    res = x + y + z
    print(res)

soma3(1,2,3)
soma3(1,2,)
soma3(1)
soma3()

def soma4(x = 0, y = 0, z = 0, w = 0):
    res = x + y + z + w
    print(res)

soma4(1,2,3,4)
soma4(1,2,3)
soma4(1,2)
soma4(1)
soma4()

#Criando borda ao redor da string
def borda(s1):
    tam = len(s1)
    if tam:
        print('+', '-' * tam, '+')
        print('|', s1, '|')
        print('+', '-' * tam, '+')

borda("Olá, Uninter")
borda("Aula 5 de Prog e Algoritmos")
