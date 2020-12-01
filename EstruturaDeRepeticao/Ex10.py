# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no
# intervalo compreendido por eles.

num1 = int(input('Informe o 1º número inteiro: '))
num2 = int(input('Informe o 2º número inteiro: '))

for i in range(num1 + 1, num2):
    print(i)

for i in range(num2 + 1, num1):
    print(i)
