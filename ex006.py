# Crie um algoritmo que leia um número e mostre o seu dobro.
# triplo e raiz quadrada

numero = int(input("Digite um valor: \n"))

print('\n O bobro de {} vale: {}'.format(numero, (numero * 2)),
      '\n O triplo de {} vale: {}'.format(numero, (numero * 3)),
      '\n A raiz quadrada de {} vale: {:.2f}'.format(numero, pow(numero, 1/2)))
