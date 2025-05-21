import os

restaurantes = [
    { 'nome': 'Pit Dog', 'categoria': 'Hamburgueria', 'ativo': False},
    {'nome': 'Grande Sushi', 'categoria': 'Japonesa', 'ativo': True},
    {'nome': 'Burguer King', 'categoria': 'Hamburgueria', 'ativo': False,}
]

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    os.system('cls')
    # os.system('clear') 
    print('Finalizando o app')

def opcao_invalida():
    print("Opção Inválida \n")
    voltar_ao_menu()

def cadastrar_restaurante():
    limpar_tela()
    print("Cadastro de novos restaurante: \n")
    nome_restaurante = input("Qual o nome do restaurante: ")
    categoria = input(f"Digite a categoria do restaurante {nome_restaurante}:")
    dados_do_restaurante = {'nome':nome_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante {nome_restaurante} foi cadastrado! 🆗" )
    voltar_ao_menu()

def listar_restaurantes():
    limpar_tela()
    print("Lista dos restaurantes: \n")

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        print(f"- {nome_restaurante} | {categoria} | {ativo}")

    input("\n Digite uma tecla para voltar ao menu principal:")
    main()

def voltar_ao_menu():
    input("Digite uma tecla e volte ao menu!")
    main()

def limpar_tela():
    os.system("cls")

def alternar_estado_restaurante():
    limpar_tela()
    print("Alterando estado do restaurante \n")

    nome_restaurante = input("Digite o nome do restaurante que deseja aterar o estado:")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso!" if restaurante['ativo'] else f"O restaurante {nome_restaurante} foi desativado com sucesso!"
            print(mensagem)
    if not restaurante_encontrado:
        print("O restaurante não foi encontrado!")

    voltar_ao_menu()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1: 
            cadastrar_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        elif opcao_escolhida == 3: 
            alternar_estado_restaurante()
        elif opcao_escolhida == 4: 
            finalizar_app()
        else: 
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    limpar_tela()
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()