# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro
# Escreva um algoritmo que leia o número de litros vendidos,
# o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser
# pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

litros = float(input('Informe a quantidade de litros: '))
combustivel = str(input('Informe o tipo de combustível (A-álcool, G-gasolina): ').upper())

valor = 0
gasolina = 2.5
alcool = 1.9

if combustivel == 'A':
    if litros <= 20:
        valor = litros * (alcool - (alcool * 0.03))
    else:
        valor = litros * (alcool - (alcool * 0.05))
    print('Valor: ', valor)

elif combustivel == 'G':
    if litros <= 20:
        valor = litros * (alcool - (alcool * 0.04))
    else:
        valor = litros * (alcool - (alcool * 0.06))
    print('Valor: ', valor)
else:
    print('O tipo de combustível informado não existe!')
