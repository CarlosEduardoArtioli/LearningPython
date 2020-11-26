# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

h = float(input('Informe sua altura: '))

phomem = (72.7 * h) - 58
pmulher = (62.1 * h) - 44.7

print('Caso seja homem, seu peso ideal é: ', phomem)
print()
print('Caso seja mulher, seu peso ideal é: ', pmulher)
