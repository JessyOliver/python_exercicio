# Faça um programa que leia um numero inteiro
# e exiba na tela sua tabuada

numero = int(input("Digite um numero: "))
contador = 0

print("\n TABUADA DO {}".format(numero))
while contador <= 10:
    print(contador, ' x ',  numero, '=', contador * 2)
    contador += 1
