def save(lista):
    arquivo = open('arquivos.txt', 'w')

    for ct in lista:
        arquivo.write('{}#{}#{}\n'.format(ct['nome'], ct['email'], ct['tel']))
    arquivo.close()

def load():
    lista = []
    try:
        arquivo = open('arquivos.txt', 'r')

        for linha in arquivo.readlines():
            col = linha.strip().split('#')

            contato = {
                'nome': col[0],
                'email': col[1],
                'tel': col[2]
            }
            lista.append(contato)

        arquivo.close()
    except FileNotFoundError:
        pass

    return lista

def nem(lista, em):
    if len(lista) > 0:
        for ct in lista:
            if ct['email'] == em:
                return True
    return False

def add(lista):
    while True:
        em = input('Digite o e-mail do contato: ')
        if not nem(lista, em):
            break
        else:
            print('E-mail já cadastrado. Tente um e-mail diferente.')

    ct = {
        'email': em,
        'nome': input('Digite como deseja salvar o contato: '),
        'tel': input('Digite o número telefonico deste contato: ')
    }

    lista.append(ct)
    print('{} adicionado à sua Lista de Contatos com êxito.\n'.format(ct['nome']))

def rem(lista):
    if len(lista) > 0:
        em = input('Digite o e-mail do contato a ser removido: ')
        if nem(lista, em):
            for i, ct in enumerate(lista):
                if ct['email'] == em:
                    print('Nome: {}'.format(ct['nome']))
                    print('Email: {}'.format(ct['email']))
                    print('Telefone: {}'.format(ct['tel']))
                    del lista[i]
                    print('Contato excluído com êxito.')
                    break
        else:
            print('Não existe um contato cadastrado com o e-mail {}.'.format(em))
    else:
        print('Não existe nenhum cadastro no sistema.')

def alt(lista):
    if len(lista) > 0:
        em = input('Digite o e-mail do contato que deseja editar: ')
        if nem(lista, em):
            for ct in lista:
                if ct['email'] == em:
                    print('Nome: {}'.format(ct['nome']))
                    print('Email: {}'.format(ct['email']))
                    print('Telefone: {}'.format(ct['tel']))

                    ct['nome'] = input('Insira o novo nome do contato: ')
                    ct['tel'] = input('Insira o novo telefone do contato: ')
                    print('Dados atualizados com êxito.')
                    break
        else:
            print('Não achamos um contato cadastrado com o e-mail de {}.'.format(em))
    else:
        print('Não existe nenhum cadastro no sistema.')

def b1(lista):
    if len(lista) > 0:
        em = input('Digite o e-mail do contato que deseja buscar: ')
        if nem(lista, em):
            for ct in lista:
                if ct['email'] == em:
                    print('Nome: {}'.format(ct['nome']))
                    print('Email: {}'.format(ct['email']))
                    print('Telefone: {}'.format(ct['tel']))
                    break
        else:
            print('Não achamos um contato cadastrado com o e-mail de {}.'.format(em))
    else:
        print('Não existe nenhum cadastro no sistema.')

def look(lista):
    if len(lista) > 0:
        for i, ct in enumerate(lista):
            print('Contato {}:'.format(i + 1))
            print('\tNome: {}'.format(ct['nome']))
            print('\tEmail: {}'.format(ct['email']))
            print('\tTelefone: {}'.format(ct['tel']))
        print('Total de contatos salvos: {}\n'.format(len(lista)))
    else:
        print('Nenhum contato salvo no banco de dados.')

def principal():
    lista = load()
    while True:
        print('''
        1- Adicionar
        2- Remover
        3- Editar
        4- Buscar 1
        5- Visualizar
        6- Sair
        ''')
        op = int(input('Digite sua escolha: '))
        if op == 1:
            add(lista)
            save(lista)
        elif op == 2:
            rem(lista)
            save(lista)
        elif op == 3:
            alt(lista)
            save(lista)
        elif op == 4:
            b1(lista)
        elif op == 5:
            look(lista)
        elif op == 6:
            print('Saindo da Agenda Digital...')
            break
        else:
            print('Opção inválida. Tente novamente.')

principal()