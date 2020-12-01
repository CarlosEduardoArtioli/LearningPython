# Faça um programa para imprimir:
#     1
#     2   2
#     3   3   3
#     .....
#     n   n   n   n   n   n  ... n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

def imprimir_num(num):
    for x in range(num):
        print(num, '', end='')


n = int(input('Informe um valor inteiro: '))

imprimir_num(n)
