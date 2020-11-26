# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a
# ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é
# vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a
# serem compradas e o preço total.

t_m_2 = float(input('Informe o tamanho em metros quadrados da área a ser pintada: '))

litros = t_m_2 / 3
latas = litros / 18
valor = latas * 80

print('Você precisa comprar', latas,'de tinta e o valor_latas total é: R$', valor)
