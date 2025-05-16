preco = int(input("Insira o valor do produto:"))

desconto = int(input("Insira o desconto:"))

valor_final = preco - (preco * desconto / 100)
print(f"\nO preço do celular com {desconto}% de desconto é R$ {valor_final} ")