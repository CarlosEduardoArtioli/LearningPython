# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.

nome_usuario = str(input('Informe o nome do usuário: '))
senha_usuario = str(input('Informe a senha do usuário: '))

while senha_usuario == nome_usuario:
    print()
    senha_usuario = str(input('Por favor, informe uma senha que não seja igual ao nome do usuário: '))

print('Cadastro válido!')
