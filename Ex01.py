import tabulate
agenda = {}

def chavescon(agenda, nome): #Essa função busca as chaves de dicionários presentes na agenda.
    chaves = []
    for chave in agenda: #inserir as chaves dos contatos na lista "Chaves".
        if chave.startswith(nome):
            chaves.append(chave)
    return chaves


def adicionar(): #Adicionar um contato na agenda.
    Qtdcontatos = int(input('Quantos contatos deseja adicionar? ')) #Definir a quantidade de contatos a serem add 
    while Qtdcontatos > 0:
        Nome = input("Digite o nome do contato:")
        Telefone1 = input("Digite o telefone 1 do contato: ")
        Telefone2 = input("Digite o telefone 2 do contato: ")
        Email = input("Digite o email do contato: ")
        
        agenda[Nome] = {
            'Nome': Nome,
            'Telefone1': Telefone1,
            'Telefone2': Telefone2,
            'Email': Email}
        print('O contato {} foi cadastrado com sucesso!'.format(Nome))
        Qtdcontatos = Qtdcontatos - 1


def procurarcontato(nome, agenda): #Buscar contato
    contatodebusca = []
    chaves1 = chavescon(agenda, nome)
    if len(chaves1) > 0:
        for chave in chaves1:
            contatodebusca.append([
                agenda[chave]["Nome"], agenda[chave]["Telefone1"], agenda[chave]["Telefone2"],agenda[chave]["Email"],
            ])
            print(contatodebusca)


def apagar(agenda, nome): #Excluir contato
    if len(agenda) > 0:
      for contato in list(agenda):
        if contato == nome:
            agenda.pop(nome)
            print("O contato {} foi apagado da agenda!".format(nome))

def apagartel(agenda, telefone1, telefone2):
  pass

def Editar(agenda, nome): #Editar contato
    if len(agenda) > 0:
        for chavdocontato in agenda:
            if chavdocontato == nome:
                novo_nome = input('Digite o novo nome do contato: ')
                novo_telefone1 = input('Digite o novo telefone 1 do contato: ')
                novo_telefone2 = input('Digite o novo telefone 2 do contato: ')
                novo_email = input('Digite o novo email do contato: ')
                
                agenda[novo_nome] = agenda.pop(nome)
                agenda[novo_nome] = {
                    "Nome": novo_nome,
                    "Telefone1": novo_telefone1,
                    "Telefone2": novo_telefone2,
                    "Email": novo_email
                    
                }
                print("Os dados do contato {} foram alterados com sucesso!".format(nome))
                break

#Esse bloco de código é responsável por gerar um relatorio de todos os contatos que estão cadastrados na agenda
#Obs: só consegui gerar o relatorio usando a biblioteca tabulate. Essa biblioteca mostra os contatos em forma de tabela
def relatorio(agenda):
    contatos = []
    if len(agenda) > 0:
        for chave in agenda:
            contatos.append([
                agenda[chave]["Nome"], agenda[chave]["Telefone1"], agenda[chave]["Telefone2"], agenda[chave]["Email"]
            ])
        print(tabulate.tabulate(contatos, headers=["Nome", "Telefone1", "Telefone2", "E-mail"], tablefmt="grid"))
    else:
        print("Agenda vazia!")


# Esse é o menu da minha agenda, onde estão localizadas todas opções.
def menu():
    while True:
        print('--> AGENDA TELEFONICA <--')
        print('1 - Adicionar contato')
        print('2 - Consultar contato')
        print('3 - Excluir contato')
        print('4 - Editar contato')
        print('5 - Lista de contatos')
        print('6 - Excluir telefones')
        print('7 - Sair')
        opc = int(input('Qual a opção desejada: ->'))

        if opc == 1:
            adicionar()
        elif opc == 2:
            nome = input('Digite o Nome que deseja buscar: ')
            procurarcontato(nome, agenda)
        elif opc == 3:
            nome = input('Digite o Nome do contato que deseja excluir: ')
            apagar(agenda, nome)
        elif opc == 4:
            nome = input('Digite o nome do contato que deseja alterar: ')
            Editar(agenda, nome)
        elif opc == 5:
            relatorio(agenda)
        elif opc == 6: 
            nome = input('Digite o nome do contato que deseja excluir os telefones: ')
        elif opc == 7:
            print('Agenda fechada!')
            break
        else:
            print('Opção invalida, selecione uma opção válida!')
menu()
