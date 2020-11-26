# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e
# continue pedindo até que o usuário informe um valor válido.

nota = -1

while 0 > nota or nota > 10:
    nota = int(input('Informe uma nota entre 0 e 10: '))

    if 0 > nota or nota > 10:
        print('Valor inválido!')
