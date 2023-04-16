AGENDA = {}

AGENDA['guilherme'] = {
    'telefone': '999999999',
    'e-mail':  'guilherme@solyd.com',
    'endereco': 'av. 1'
}

AGENDA['maria'] = {
    'telefone': '466446',
    'e-mail':  'guilherme@solyd',
    'endereco': 'av. 2'
}

def buscarContato(contato):
    print("Nome", contato)
    print('Telefone', AGENDA[contato]['telefone'])
    print('E-mail', AGENDA[contato]['e-mail'])
    print('Endereço', AGENDA[contato]['endereco'])
    print('_____________________________________')

def listarContatos():
    for contato in AGENDA:
        buscarContato(contato)

def adicionarEditarContato(nome, telefone, email, endereco):
    AGENDA[nome] = {
        'telefone': telefone,
        'e-mail':  email,
        'endereco': endereco
    }


def removerContato(contato):
    AGENDA.pop(contato)

def ListarMenu():
    print("Pressione 1 para buscar contato")
    print("Pressione 2 para listas todos contato")
    print("Pressione 3 para adicionar/editar contato")
    print("Pressione 4 para remover contato")
    print("Pressione 5 para sair")

ListarMenu()
opcao = input("Escreva aqui: ")

if opcao == '1':
    opcao_busca = input("Nome do contato ")
    buscarContato(opcao_busca)

elif opcao == '2':
    listarContatos()

elif opcao == '3' or opcao == '4':
    nome = input('Digite o nome ')
    telefone = input('Digite o telefone ')
    endereco = input('Digitte o endereço ')
    email = input('Digite o e-mail ')
    adicionarEditarContato(nome, telefone, endereco, email)

elif opcao == '5':
    pass

else:
    print('Opção inválida ')

