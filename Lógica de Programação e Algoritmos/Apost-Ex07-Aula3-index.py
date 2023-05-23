#Exercício do Triângulo

A = int(input("Digite o 1 lado do triângulo: "))
B = int(input("Digite o 2 lado do triângulo: "))
C = int(input("Digite o 3 lado do triângulo: "))

if (A > 0) and (B > 0) and (C > 0):
    if (A + B > C) and ( A + C > B) and (B + C > A):
    #Se chegou até aqui, o triangulo é válido!
        if A != B and A != C and B != C:
            print("Triangulo escaleno!")
        else:
            if A == B and A == C and B == C:
                print("Triangulo equilátero!")
            else:
                print("Triangulo isósceles!")
    else:
        print("Pelo menos um dos lados está com valor incorreto para a formação de um triângulo")
else:
    print("Pelo menos um dos lados está com valor incorreto para a formação de um triângulo")
