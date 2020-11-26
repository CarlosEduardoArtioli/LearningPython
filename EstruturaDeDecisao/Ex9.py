# Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1 = float(input('Informe o 1º número: '))
num2 = float(input('Informe o 2º número: '))
num3 = float(input('Informe o 3º número: '))

if num1 > num2 > num3:
    print('Ordem decrescente:', num1, num2, num3)
if num1 > num3 > num2:
    print('Ordem decrescente:', num1, num3, num2)
if num2 > num1 > num3:
    print('Ordem decrescente:', num2, num1, num3)
if num2 > num3 > num1:
    print('Ordem decrescente:', num2, num3, num1)
if num3 > num2 > num1:
    print('Ordem decrescente:', num3, num2, num1)
if num3 > num1 > num2:
    print('Ordem decrescente:', num3, num1, num2)
if num1 == num2 == num3:
    print('Todos os números são iguais')
