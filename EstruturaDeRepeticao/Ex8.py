# Faça um programa que leia 5 números e informe a soma e a média dos números.

count = 0
soma = 0
media = 0

while count < 5:
    num = float(input('Informe um número: '))
    soma += num
    media = soma / 5
    count += 1

print('Soma dos números:', soma)
print('Média dos números:', media)
