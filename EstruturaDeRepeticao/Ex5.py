# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
# Valide a entrada e permita repetir a operação.

anos = 0
a = int(input('Informe a primeira população: '))
taxa_a = float(input('Informe a taxa de crescimento da primeira população (ex: 0.05 = 5%): '))
b = int(input('Informe a segunda população: '))
taxa_b = float(input('Informe a taxa de crescimento da segunda população (ex: 0.05 = 5%): '))

while a != b:
    a += a * taxa_a
    b += b * taxa_b
    anos += 1

print('Serão necessários:', anos, 'anos')
