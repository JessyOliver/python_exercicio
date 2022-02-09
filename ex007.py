# Desenvolva um programa qu leia as duas notas
# de um aluno. Calcule e mostre sua média
nota1 = float(input("Digite a nota 1°: "))
nota2 = float(input("Digite a 2° nota: "))
media = (nota1 + nota2) / 2

print("\n As notas: "
      "\n 1° nota: {} "
      "\n 2° nota: {} "
      "\n Média: {:.2f}".format(nota1, nota2, media))
