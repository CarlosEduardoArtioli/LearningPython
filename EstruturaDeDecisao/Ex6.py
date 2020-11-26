# Faça um Programa que leia três números e mostre o maior deles.

num1 = float(input('Informe o 1º número: '))
num2 = float(input('Informe o 2º número: '))
num3 = float(input('Informe o 3º número: '))

if num1 > num2 and num3:
    print('O maior número é:', num1)
elif num2 > num1 and num3:
    print('O maior número é:', num2)
elif num3 > num1 and num2:
    print('O maior número é:', num3)
else:
    print('Todos os números são iguais')
