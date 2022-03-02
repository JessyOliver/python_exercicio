# Faça um programa que leia um numero inteiro
# e exiba na tela sua tabuada

print('\n CRIANDO A TABUADA \n')
numero = int(input("Digite um numero: "))
contador = 0

print("\n TABUADA DO {}".format(numero))
print('_' * 15)
while contador <= 10:
    print('\n {} X {:2} = {}'.format(numero, contador, (contador * numero)))
    contador += 1

print('_' * 15)
