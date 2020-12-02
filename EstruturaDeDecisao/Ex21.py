# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e
# depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1,
# 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve
# se preocupar com a quantidade de notas existentes na máquina.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50,
# uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50,
# quatro notas de 10, uma nota de 5 e quatro notas de 1.

saque = float(input('Informe o valor do saque (Entre 10 reais e 600 reais): '))

if 10 <= saque <= 600:
    notas_100 = int((saque - (saque % 100)) / 100)
    notas_50 = int((saque % 100) / 50)
    notas_10 = int(((saque % 50) / 10))
    notas_1 = saque % 10

    if notas_100 == 1:
        print(notas_100, 'nota de R$100')
    elif notas_100 > 1:
        print(notas_100, 'notas de R$100')
    if notas_50 == 1:
        print(notas_50, 'nota de R$50')
    elif notas_50 > 1:
        print(notas_50, 'notas de R$50')
    if notas_10 == 1:
        print(notas_10, 'nota de R$10')
    elif notas_10 > 1:
        print(notas_10, 'notas de R$10')
    if notas_1 == 1:
        print(notas_1, 'nota de R$1')
    elif notas_1 > 1:
        print(notas_1, 'notas de R$1')

else:
    print('Valor incorreto')
