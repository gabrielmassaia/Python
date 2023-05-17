kmsPercorridos = int(input("Quantos kms vc percorreu?: "))
diasAlugado = int(input("Por quantos dias vc alugou o carro?: "))
preco = 60*diasAlugado + 0.15*kmsPercorridos
print("Km {}. Dias {}.". format(kmsPercorridos, diasAlugado))
print("O preço a ser pago é de: {}".format(preco))