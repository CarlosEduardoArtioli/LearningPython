# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas,
# dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21,
# 11, 1, 7 e 16

num = str(input('Informe um número menor que 1000: '))

if len(num) == 3:
    print(num, '= ', end='')
    if num[0] == '1':
        print(num[0], 'centena, ', end='')
    else:
        print(num[0], 'centenas, ', end='')
    if num[1] == '1':
        print(num[1], 'dezena e ', end='')
    else:
        print(num[1], 'dezenas e ', end='')
    if num[2] == '1':
        print(num[2], 'unidade', end='')
    else:
        print(num[2], 'unidades', end='')
elif len(num) == 2:
    print(num, '= ', end='')
    if num[0] == '1':
        print(num[0], 'dezena e ', end='')
    else:
        print(num[0], 'dezenas e ', end='')
    if num[1] == '1':
        print(num[1], 'unidade', end='')
    else:
        print(num[1], 'unidades', end='')
elif len(num) == 1:
    print(num, '= ', end='')
    if num[0] == '1':
        print(num[0], 'unidade', end='')
    else:
        print(num[0], 'unidades', end='')
else:
    print('Número informado não atende aos requisitos')
