n1 = input("Digite um valor: ")
n2 = input("Digite um segundo valor: ")

if n1 < n2:
    print("O segundo valor digitado é maior que o primeiro valor digitado")
else:
    print("O primeiro valor é maior que o segundo")


primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor >= segundo_valor:
    print(
        f'{primeiro_valor=} é maior ou igual '
        f'ao que {segundo_valor=}'
    )
else:
    print(
        f'{segundo_valor=} é maior '
        f'do que {primeiro_valor=}'
    )