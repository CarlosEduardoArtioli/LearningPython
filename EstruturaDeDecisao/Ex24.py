# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja
# realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.

num1 = int(input('Informe um número: '))
num2 = float(input('Informe outro número: '))
acao = str(input('Informe a ação que deseja tomar (+, -, *, /): '))

if acao == '+':
    print('O resultado é: ' + str(num1 + num2))
    if ((num1 + num2) % 2) == 0:
        print('O valor é par')
    else:
        print('O valor é impar')

    if (num1 + num2) >= 0:
        print('O valor é positivo')
    else:
        print('O valor é negativo')

    if (num1 + num2) == round((num1 + num2)):
        print('O número é inteiro')
    else:
        print('O número é decimal')

elif acao == '-':
    print('O resultado é: ' + str(num1 - num2))
    if ((num1 - num2) % 2) == 0:
        print('O valor é par')
    else:
        print('O valor é impar')

    if (num1 - num2) >= 0:
        print('O valor é positivo')
    else:
        print('O valor é negativo')

    if (num1 - num2) == round((num1 - num2)):
        print('O número é inteiro')
    else:
        print('O número é decimal')

elif acao == '*':
    print('O resultado é: ' + str(num1 * num2))
    if ((num1 * num2) % 2) == 0:
        print('O valor é par')
    else:
        print('O valor é impar')

    if (num1 * num2) >= 0:
        print('O valor é positivo')
    else:
        print('O valor é negativo')

    if (num1 * num2) == round((num1 * num2)):
        print('O número é inteiro')
    else:
        print('O número é decimal')

elif acao == '/':
    print('O resultado é: ' + str(num1 / num2))
    if ((num1 / num2) % 2) == 0:
        print('O valor é par')
    else:
        print('O valor é impar')

    if (num1 / num2) >= 0:
        print('O valor é positivo')
    else:
        print('O valor é negativo')

    if (num1 / num2) == round((num1 / num2)):
        print('O número é inteiro')
    else:
        print('O número é decimal')

else:
    print('Operação incorreta!')
