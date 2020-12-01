# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no
# vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

nums = []
pares = []
impares = []

for i in range(20):
    nums.append(int(input('Informe o ' + str(i+1) + 'º número inteiro: ')))
    if (nums[i] % 2) == 0:
        pares.append(nums[i])
    else:
        impares.append(nums[i])

print('Todos os números:', nums)
print('Números pares:', pares)
print('Números impares:', impares)
