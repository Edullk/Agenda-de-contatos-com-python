AGENDA = {}

def buscar_contato(contato):
    try:
        print("Nome", contato)
        print('Telefone', AGENDA[contato]['telefone'])
        print('E-mail', AGENDA[contato]['e-mail'])
        print('Endereço', AGENDA[contato]['endereco'])
        print('_____________________________________')
    except KeyError:
        print("Contato inexistente")
    except Exception as error:
        print("Um erro inesperado aconteceu")
        print(error)


def listar_contatos():
    if AGENDA:
        for contato in AGENDA:
            buscar_contato(contato)
    else:
        print("Agenda vazia")


def adicionar_editar_contato(nome, telefone, email, endereco):
    AGENDA[nome] = {
        'telefone': telefone,
        'e-mail':  email,
        'endereco': endereco
    }

def remover_contato(contato):
    try:
        AGENDA.pop(contato)
    except:
        print("Contato inexistente")


def exportar_csv(nome_arquivo):
    try:
        with open(nome_arquivo, 'w') as arquivo:
            for contato in AGENDA:
                telefone = AGENDA[contato]['telefone']
                email = AGENDA[contato]['e-mail']
                endereco = AGENDA[contato]['endereco']
                arquivo.write('{}, {}, {}, {}\n'.format(contato, telefone, email, endereco))
                print("Contatos exportados com sucesso")
    except Exception as error:
        print('Algum erro aconteceu')
        print(error)


def importar_csv(arquivo):
    try:
        with open(arquivo) as arquivo_importado:
            linhas = arquivo_importado.readlines()
            for linha in linhas:
                indices = linha.strip().split(',')
                nome = indices[0]
                telefone = indices[1]
                email = indices[2]
                endereco = indices[3]
                adicionar_editar_contato(nome, telefone, email, endereco)
            print("Contatos importados com sucesso")

    except Exception as error:
        print('Algo deu errado')
        print(error)


def listar_menu():
    print("............MENU...............")
    print("Pressione 1 para buscar contato")
    print("Pressione 2 para listas todos contato")
    print("Pressione 3 para adicionar/editar contato")
    print("Pressione 4 para remover contato")
    print("Pressione 5 para exportar contatos")
    print("Pressione 6 para importar contatos")
    print("Pressione 7 para sair")


def carregar_database():
    importar_csv('database.csv')


carregar_database()
while True:
    listar_menu()
    opcao = input("Escreva aqui: ")

    if opcao == '1':
        opcao_busca = input("Nome do contato ")
        buscar_contato(opcao_busca)

    elif opcao == '2':
        listar_contatos()

    elif opcao == '3':
        nome = input('Digite o nome ')
        telefone = input('Digite o telefone ')
        endereco = input('Digitte o endereço ')
        email = input('Digite o e-mail ')
        adicionar_editar_contato(nome, telefone, endereco, email)

    elif opcao == "4":
        nome = input('Digite o nome do contato: ')
        remover_contato(nome)

    elif opcao == '5':
        nome_arquivo = input('Salvar arquivo como: ')
        exportar_csv(nome_arquivo)

    elif opcao == '6':
        nome_arquivo = input("Digite o nome do arquivo com extensao ")
        importar_csv(nome_arquivo)

    elif opcao == '7':
        break

    else:
        print('Opção inválida ')

