# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas.
# Imprima as consoantes.

caracteres = []
num_consoantes = 0
consoantes = []

for i in range(10):
    caracteres.append(str(input('Informe o ' + str(i + 1) + 'º caractere: ')))
    if caracteres[i] not in ('a', 'e', 'i', 'o', 'u'):
        num_consoantes += 1
        consoantes.append(caracteres[i])

print('Número de consoantes: ', num_consoantes)
print('Consoantes: ', consoantes)
