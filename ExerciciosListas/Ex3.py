# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = []
media = 0

for i in range(4):
    notas.append(float(input('Informe a ' + str(i+1) + 'º nota: ')))
    media = sum(notas) / 4

print('Notas: ', notas)
print('Média: ', media)
