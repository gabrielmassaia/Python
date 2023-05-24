precoProduto = float(input("Qual o preço do produto?: "))
percentDesc = float(input("Qual o percentual de desconto? (0-100): "))
desconto = precoProduto * (percentDesc / 100)
precoFinal = precoProduto - desconto
print("O preço do produto é de {}. O desconto será de {}%.".format(precoProduto, percentDesc))
print("O valor calculado de desconto: {}. O valor final do produto é de {}".format(desconto, precoFinal))
