# Faça um Programa que leia três números e mostre o maior e o menor deles.

num1 = float(input('Informe o 1º número: '))
num2 = float(input('Informe o 2º número: '))
num3 = float(input('Informe o 3º número: '))

maior = num1
menor = num1

if maior < num2:
    maior = num2
if maior < num3:
    maior = num3

if menor > num2:
    menor = num2
if menor > num3:
    menor = num3

print('O maior número é:', maior, 'e o menor número é:', menor)
