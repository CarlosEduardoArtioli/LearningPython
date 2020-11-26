# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = str(input('Informe uma letra qualquer: ').lower())

if letra == 'a' or 'e' or 'i' or 'o' or 'u':
    print('A letra informada é uma vogal')
else:
    print('A letra é uma consoante')
