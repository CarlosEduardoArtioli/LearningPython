# Altere o programa anterior para mostrar no final a soma dos números.

num1 = int(input('Informe o 1º número inteiro: '))
num2 = int(input('Informe o 2º número inteiro: '))

soma = 0

for i in range(num1 + 1, num2):
    print(i)
    soma += i

for i in range(num2 + 1, num1):
    print(i)
    soma += i

print('A soma dos números é:', soma)
