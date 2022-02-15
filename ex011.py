# Faça um programa que leia a largura e a altura
# de uma parede em metros, calcule a sua area e a quantidade
# de tinta necessária para pintá-la. Sabendo que cada litro de tinta
# pinta uma area de 2m²


altura = float(input("Digite a altura da parede: "))
base = float(input("Digite a base da parede: "))

area = altura * base
cont = 0

print("Area: ", area)

if area > 0:

    while area != 0:

        area -= 2
        cont += 1

    print("\n Seram necessarios", cont, "litros de tinta, para pintar a parede!")

else:

    print(area, "com valor insuficiente, para calculo.")






