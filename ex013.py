# Faça um programa que leia o salário de um funcionário e mostre
# seu novo salário, com 15% de aumento

wage = float(input("Digite o salário do funcionário: R$"))

grossSalary = float(0)

grossSalary = wage + ((15 / 100) * wage)

print("\n Salário final do funcionário: \n R$ {:.2f}".format(grossSalary))