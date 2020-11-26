# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a
# ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é
# vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre
# arredonde os valores para cima, isto é, considere latas cheias.

t_m_2 = float(input('Informe o tamanho em metros quadrados da área a ser pintada: '))

litros = t_m_2 / 6

# Latas
if t_m_2 % 108 == 0:
    latas = litros / 18

else:
    latas = int(litros / 18) + 1

# Galões
if t_m_2 % 21.6 == 0:
    galoes = litros / 3.6

else:
    galoes = int(litros / 3.6) + 1

valor_latas = latas * 80
valor_galoes = galoes * 25

print('Você precisa comprar', latas,'latas de tinta e o valor total é: R$', valor_latas)
print('Você precisa comprar', galoes,'galões de tinta e o valor total é: R$', valor_galoes)
