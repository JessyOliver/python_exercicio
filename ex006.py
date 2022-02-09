# Crie um algoritmo que leia um número e mostre o seu dobro.
# triplo e raiz quadrada

numero = int(input("Digite um valor: \n"))

print('O bobro de {} ='.format(numero), numero * 2)
print('O triplo de {} ='.format(numero), pow(numero, 3))
print('A raiz quadrada de {} ='.format(numero), pow(numero, 2))