# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def tres_argumentos(n1, n2, n3):
    soma = n1 + n2 + n3
    print('A soma dos três números é:', soma)


num1 = float(input('Informe um valor: '))
num2 = float(input('Informe um valor: '))
num3 = float(input('Informe um valor: '))

tres_argumentos(num1, num2, num3)
