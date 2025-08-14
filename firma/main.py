lista_funcionarios = list()
id_global = 5537468

def cadastrar_funcionario(id_global):
    while True:
        try:
            print(f'{'-' * 18} MENU CADASTRAR FUNCIONÁRIO {'-' * 19}')
            nome = input('Por favor entre com o nome do funcionario: ')
            setor = input('Por favor entre com o setor do funcionario: ')
            salario = float(input('Por favor entre com o salario do funcionario: '))
            funcionario = {'id' : id_global, 'nome': nome, 'setor': setor, 'salario': salario}
            lista_funcionarios.append(funcionario)
            break
        except ValueError:
            print('Valores inválidos, tente novamente')

def imprime_funcionario(i):
    print(f''
          f'id: {lista_funcionarios[i]['id']}\n'
          f'nome: {lista_funcionarios[i]['nome']}\n'
          f'setor: {lista_funcionarios[i]['setor']}\n'
          f'salário: {lista_funcionarios[i]['salario']}\n')

def remover_funcionario():
    print(f'{'-' * 19} MENU REMOVER FUNCIONÁRIO {'-' * 20}')
    opcao = int(input('Digite o id do funcionário a ser removido: '))

    for i in range(len(lista_funcionarios)):
        if lista_funcionarios[i]['id'] == opcao:
            lista_funcionarios.pop(i)

def consultar_funcionario():

    while True:
        try:
            print(f'{'-' * 18} MENU CONSULTAR FUNCIONÁRIO {'-' * 19}')
            opcao = int(input('Escolha a opção desejada: \n'
                              '1 - Consultar todos Funcionários \n'
                              '2 - Consultar Funcionário por id\n'
                              '3 - Consultar Funcionário por setor\n'
                              '4 - Retornar \n'
                              '>>' ))
            if opcao == 1:
                for i in range(len(lista_funcionarios)):
                    imprime_funcionario(i)

            elif opcao == 2:
                sub_opcao = int(input('Digite o id do funcionário: '))
                for i in range(len(lista_funcionarios)):
                    if lista_funcionarios[i]['id'] == sub_opcao:
                        imprime_funcionario(i)
                    else:
                        print(f'Funcionário id {sub_opcao} não encontrado')

            elif opcao == 3:
                sub_opcao = input('Digite o setor do(s) funcionário(s): ')
                for i in range(len(lista_funcionarios)):
                    if lista_funcionarios[i]['setor'] == sub_opcao:
                        imprime_funcionario(i)
            elif opcao == 4:
                print('Retornando...')
                break
        except ValueError:
            print('Digite uma opção válida')
print("Bem vindo a Empresa do Deivid Alves da Rocha")

while True:
    try:
        print('-' * 65)
        print(f'{'-' * 24} MENU PRINCIPAL {'-' * 25}')
        opcao = int(input('Escolha a opção desejada: \n'
      '1 - Cadastrar Funcionários \n'
      '2 - Consultar Funcionários \n'
      '3 - Remover Funcionários \n'
      '4 - Sair\n'
      '>>'))
        if opcao == 1:
            cadastrar_funcionario(id_global)
            id_global += 1
        elif opcao == 2:
            consultar_funcionario()
        elif opcao == 3:
            remover_funcionario()
        elif opcao == 4:
            print('Saindo...')
            break
        else:
            raise ValueError
    except ValueError:
        print('Opção inválida')