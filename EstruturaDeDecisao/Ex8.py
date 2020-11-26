# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato.

preco1 = float(input('Informe o 1º preço: '))
preco2 = float(input('Informe o 2º preço: '))
preco3 = float(input('Informe o 3º preço: '))

mais_barato = preco1

if preco1 < preco2 and preco3:
    mais_barato = preco1
if preco2 < preco1 and preco3:
    mais_barato = preco2
if preco3 < preco1 and preco2:
    mais_barato = preco3

print(mais_barato, 'é o preço mais barato')
