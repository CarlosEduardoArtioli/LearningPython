# Faça um programa que leia 5 números e informe o maior número.

count = 0
maior_num = -99999

while count < 5:
    count += 1
    num = float(input('Informe um número: '))
    if num > maior_num:
        maior_num = num

print('O maior número é:', maior_num)
