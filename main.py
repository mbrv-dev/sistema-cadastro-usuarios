import json

def mostrar_menu():
    print('====================')
    print('1. Cadastrar usuario')
    print('2. Mostrar usuarios')
    print('3. Sair')
    print('====================')

try:
    with open("usuarios.json", "r+") as arquivo:
        usuarios = json.load(arquivo)
except (FileNotFoundError, json.decoder.JSONDecodeError):
        usuarios = []

def cadastrar_usuario():
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    email = input('Digite seu email: ')

    usuario = {
        "nome": nome,
        "idade": idade,
        "email": email
    }

    usuarios.append(usuario)

    with open("usuarios.json", "w") as arquivo:
        json.dump(usuarios, arquivo, indent=4)

    print("Usuário cadastrado com sucesso!\n")

def mostrar_usuarios():
    if usuarios:
        print('\n=== Usuários cadastrados ===')
        for usuario in usuarios:
            print(f'Nome : {usuario["nome"]}')
            print(f'Idade : {usuario["idade"]}')
            print(f'E-mail : {usuario["email"]}')
            print('-'*15)
        print('==============================\n')
    else:
        print('Nenhum usuário cadastrado ainda!\n')

while True:
    try:
        mostrar_menu()

        opcao = int(input('Escolha uma opção: '))

        if opcao == 1:
            cadastrar_usuario()

        elif opcao == 2:
            mostrar_usuarios()

        elif opcao == 3:
            print('Saindo do programa...')
            break

        else:
            print('Opção invalida, tente novamente!\n')

    except ValueError:
        print('Valor invalido, Digite um numero!\n')