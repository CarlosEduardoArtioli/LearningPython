# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
# O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas
# seguintes situações:
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve
# fazer pedir os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

import math

a = float(input('Informe o valor de "a": '))
b = 0
c = 0

if a != 0:
    b = float(input('Informe o valor de "b": '))
    c = float(input('Informe o valor de "c": '))
    delta = b**2 - (4 * a * c)
    if delta > 0:
        delta = math.sqrt(delta)
        x1 = (-b + delta) / (2 * a)
        x2 = (-b - delta) / (2 * a)
        print(x1, x2)
    elif delta == 0:
        x = -b / (2 * a)
        print(x)
    else:
        print('O delta calculado é negativo, a equação não possui raizes reais')
else:
    print('A equação não é do segundo grau!')
