# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de
# cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

count = 0

for i in range(10):
    notas = []
    media = 0
    for x in range(4):
        notas.append(float(input('Informe a ' + str(x + 1) + 'ª nota: ')))
    for n in notas:
        media += n
    if (media / 4) >= 7:
        count += 1

print('Número de alunos com média maior ou igual a 7:', count)
