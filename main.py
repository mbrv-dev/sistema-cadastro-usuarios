import json

def mostrar_menu():
    print('====================')
    print('1. Cadastrar usuario')
    print('2. Mostrar usuarios')
    print('3. Remover usuario')
    print('4. Editar usuario')
    print('5. Buscar usuario')
    print('6. Sair')
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

def remover_usuario():
    if usuarios:
        nome_digitado = input('Digite o nome que quer remover: ')
        encontrado = False

        for usuario in usuarios:
            if nome_digitado == usuario["nome"]:
                usuarios.remove(usuario)
                encontrado = True

                with open("usuarios.json", "w") as arquivo:
                    json.dump(usuarios, arquivo, indent=4)

                print("Usuario removido com sucesso!\n")
                break

        if not encontrado:
            print('Usuário não encontrado!\n')

    else:
        print('Usuário não encontrado!\n')

def editar_usuario():
    if usuarios:
        nome_digitado = input('Digite o nome que quer editar: ')
        encontrado = False

        for usuario in usuarios:
            if nome_digitado == usuario["nome"]:
                encontrado = True

                novo_nome = input('Digite o novo nome: ')
                nova_idade = int(input('Digite a nova idade: '))
                novo_email = input('Digite o novo email: ')

                usuario["nome"] = novo_nome
                usuario["idade"] = nova_idade
                usuario["email"] = novo_email

                with open("usuarios.json", "w") as arquivo:
                    json.dump(usuarios, arquivo, indent=4)

                print("Usuário editado com sucesso!\n")
                break

        if not encontrado:
           print("Usuário não encontrado!\n")
    else:
       print("Nenhum usuário cadastrado!\n")

def buscar_usuario():
    if usuarios:
        nome_digitado = input('Digite o nome que deseja buscar: ')
        encontrado = False

        for usuario in usuarios:
            if nome_digitado == usuario["nome"]:
                print("\nUsuário encontrado:")
                print(f'Nome : {usuario["nome"]}')
                print(f'Idade : {usuario["idade"]}')
                print(f'E-mail : {usuario["email"]}')
                print('-'*15)

                encontrado = True
                break

        if not encontrado:
            print("Usuário não encontrado!\n")

    else:
        print("Nenhum usuário cadastrado!\n")

def sair():
    print('Saindo do programa...')

while True:
    try:
        mostrar_menu()

        opcao = int(input('Escolha uma opção: '))

        if opcao == 1:
            cadastrar_usuario()

        elif opcao == 2:
            mostrar_usuarios()

        elif opcao == 3:
            remover_usuario()

        elif opcao == 4:
            editar_usuario()

        elif opcao == 5:
            buscar_usuario()

        elif opcao == 6:
            sair()
            break

        else:
            print('Opção invalida, tente novamente!\n')

    except ValueError:
        print('Valor invalido, Digite um numero!\n')