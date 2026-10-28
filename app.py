import os

restaurantes = [{'nome':'Central Perk','categoria':'Cafeteria','ativo':False}, 
                {'nome':'Siri Cascudo','categoria':'Hambúguer','ativo':True},
                {'nome':'Ichiraku','categoria':'Japonesa','ativo':False}]

def exibir_nome_do_aplicativo():
    '''Essa função serve para exibir o nome do aplicativo.'''
    print("""

█ █▀▀ █░█ █ █▀█ ▄▀█ █▄▀ █░█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
█ █▄▄ █▀█ █ █▀▄ █▀█ █░█ █▄█   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
""")

def exibir_opcoes():
    '''Essa função serve para exibir as opções disponíveis dentro do aplicativo.'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar status dos restaurante')
    print('4. Sair\n')

def encerrar_app():
    '''Essa função serve para encerrar o aplicativo.'''
    exibir_subtitulo('Encerrando o aplicativo...')

def voltar_ao_menu_principal():
    '''Essa função serve para voltar ao menu.'''
    input('\nDigite uma tecla para voltar ao menu principal.')
    main()

def opcao_invalida():
    '''Essa função serve alertar sobre uma opção inválida.'''
    print('Opção inválida!')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''Essa função serve para exibir os subtítulos dos menus.'''
    os.system('cls')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante.
    Inputs:
    - Nome do restaurante;
    - Categoria.
    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes.
    '''
    exibir_subtitulo('Cadastro de novos restaurantes.')
    nome_do_restaurante = input ('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'\nO restaurante {nome_do_restaurante} foi cadastrado com sucesso.')
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Essa função serve para listar os restaurantes cadastrados no aplicativo.'''
    exibir_subtitulo('Lista de restaurantes cadastrados:')
    
    print(f"{'Nomes'.ljust(22)} | {'Categoria'.ljust(20)} | Status\n")

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu_principal()

def alternar_status_restaurante():
    '''Essa função serve para alternar os status dos restaurantes cadastrados.'''
    exibir_subtitulo('Alternando status do restaurante:')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso.' if restaurante['ativo'] else f'O restaurante foi desativado com sucesso.'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')
    voltar_ao_menu_principal()

def escolher_opcao():
    '''Essa função serve para escolher as opções disponíveis dentro do aplicativo.'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção: {opcao_escolhida}.')
        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3: 
                alternar_status_restaurante()
            case 4:
                encerrar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_aplicativo()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()