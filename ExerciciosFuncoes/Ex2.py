# Faça um programa para imprimir:
#     1
#     1   2
#     1   2   3
#     .....
#     1   2   3   ...  n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.

def imprimir_num(num):
    count = 0
    for x in range(num):
        count += 1
        print(count, '', end='')


n = int(input('Informe um valor inteiro: '))

imprimir_num(n)
