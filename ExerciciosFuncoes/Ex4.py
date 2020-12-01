# Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de
# caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.


def retorna(n):
    if n >= 0:
        return 'P'
    else:
        return 'N'


num = float(input('Informe um número: '))

print(retorna(num))
