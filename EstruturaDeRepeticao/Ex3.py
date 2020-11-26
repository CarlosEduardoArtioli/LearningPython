# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome = ''
idade = -1
salario = -1
sexo = ''
estado_civil = ''

while len(nome) <= 3:
    nome = str(input('Digite um nome que contenha mais de 3 caracteres: '))

while 0 > idade > 150:
    idade = int(input('Digite uma idade entre 0 e 150: '))

while 0 >= salario:
    salario = float(input('Digite um salário maior que 0: '))

while sexo != 'F' and sexo != 'M':
    sexo = str(input('Digite um sexo (M - Masculino ou F - Feminino): ')).upper()

while estado_civil != 'S' and estado_civil != 'C' and estado_civil != 'V' and estado_civil != 'D':
    estado_civil = str(input('Digite um estado civil (S - Solteiro, C - Casado, V - Viúvo, D - Divorciado): ')).upper()

print('Todos os dados estão corretos!')
