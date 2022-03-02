# faça um algoritmo que leia o preço de um
# produto e mostre seu novo preço, com 5% de desconto

nameProduct = str(input("Digite o nome do produto:"))

price = float(input("Digite o preço do produto: "))

print("\n Produto:", nameProduct,
      "\n Valor produto: R$ {:.2f}".format(price),
      "\n Valor com desconto: R$ {:.2f}".format(price - ((5 / 100) * price)))

