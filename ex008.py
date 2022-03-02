# Escreva um programa que leia um valor em metros e o
# exiba convertido em centimetros e milimetros

metros = float(input("Informe um distância em metros: \n"))

print("\n A medida de {},\n coresponde á {:.0f}cm \n e {:.0f}mm".format(metros, (metros * 100), (metros * 1000)))