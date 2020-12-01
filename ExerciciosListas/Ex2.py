# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

numeros = []

for i in range(10):
    numeros.append(float(input('Informe o ' + str(i+1) + 'º número real: ')))

numeros.reverse()
print(numeros)
