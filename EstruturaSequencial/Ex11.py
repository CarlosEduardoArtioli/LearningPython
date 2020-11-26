# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

num1 = int(input('Informe um número inteiro: '))
num2 = int(input('Informe outro número inteiro: '))
num3 = float(input('Informe um número real: '))

p = (num1 * 2) * (num2 / 2)
s = (num1 * 3) + num3
e = num3 ** 3

print('O produto do dobro do primeiro com metade do segundo: ', p)
print()
print('A soma do triplo do primeiro com o terceiro: ', s)
print()
print('O terceiro elevado ao cubo: ', e)