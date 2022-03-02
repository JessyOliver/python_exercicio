# escreva um programa que pergunte a quantidade de HM percorridos por um carro
# alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço
# a pagar, sabendo que o carro custa R$ 60.00 por dia e R$ 0.15 por KM rodados.

days = int(input('Informe os dias alugados: '))
km = float(input('Informe os km rodados: '))

print('\n Dias: {}'
      '\n Km rodados {}'
      '\n Valor á pagar R$ {:.2f}'.format(days, km, ((days * 60) + (km * 0.15))))
