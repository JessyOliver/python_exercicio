# Crie um programa qu eleia o quanto dinheiro que uma pessoa tem
# e mostre quantos dolares ela pode comprar
# comsidere US$ 1.00 = R$ 3.27

money = float(input("Digite o valor em reais: R$ "))
cont = 0

print('Com R$ {}'.format(money))
if money >= 3.27:
    while money > 3.27:
        money -= 3.27
        cont += 1
    print("Você pode comprar :"
          "\n $: {:.2f} ".format(cont))
else:
    print("O valor de R$ {:.2f} é insuficiente para comprar, dolares".format(money))
