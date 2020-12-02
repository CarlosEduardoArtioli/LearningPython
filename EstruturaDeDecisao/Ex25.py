# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da
# pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

print('Responda com S(sim) ou N(não)')
pergunta_1 = str(input('Telefonou para a vítima? ').upper())
pergunta_2 = str(input('Esteve no local do crime? ').upper())
pergunta_3 = str(input('Mora perto da vítima? ').upper())
pergunta_4 = str(input('Devia para a vítima? ').upper())
pergunta_5 = str(input('Já trabalhou com a vítima? ').upper())

classificacao = 0

if pergunta_1 == 'S':
    classificacao += 1
if pergunta_2 == 'S':
    classificacao += 1
if pergunta_3 == 'S':
    classificacao += 1
if pergunta_4 == 'S':
    classificacao += 1
if pergunta_5 == 'S':
    classificacao += 1

if classificacao == 5:
    print('Assassino')
elif 3 <= classificacao <= 4:
    print('Cúmplice')
elif classificacao == 2:
    print('Suspeita')
else:
    print('Inocente')
