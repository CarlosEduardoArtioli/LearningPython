# Faça um Programa que peça dois números e imprima o maior deles.

num1 = float(input('Informe o primeiro número: '))
num2 = float(input('Informe o segundo número: '))

if num1 > num2:
    print('O maior número é:', num1)
elif num2 > num1:
    print('O maior número é:', num2)
else:
    print('Os dois números são iguais')
