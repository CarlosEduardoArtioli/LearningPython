# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram
# para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
# baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salario_antigo = float(input('Informe o salário: '))

percentual = 0
aumento = 0
salario_novo = 0

if salario_antigo <= 280:
    percentual = 0.2
    aumento = salario_antigo * percentual
    salario_novo = salario_antigo + aumento
elif 280 < salario_antigo >= 700:
    percentual = 0.15
    aumento = salario_antigo * percentual
    salario_novo = salario_antigo + aumento
elif 700 < salario_antigo >= 1_500:
    percentual = 0.1
    aumento = salario_antigo * percentual
    salario_novo = salario_antigo + aumento
elif salario_antigo > 1_500:
    percentual = 0.05
    aumento = salario_antigo * percentual
    salario_novo = salario_antigo + aumento

print('Salário antes do reajuste:', salario_antigo)
print('Percentual de aumento aplicado:', percentual)
print('Valor do aumento:', aumento)
print('Novo salário:', salario_novo)
