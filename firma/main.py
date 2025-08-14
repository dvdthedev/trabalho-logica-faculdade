lista_funcionarios = list()
id_global = 5537468

def cadastrar_funcionario(id_global):
    while True:
        try:
            print(f'{'-' * 18} MENU CADASTRAR FUNCIONÁRIO {'-' * 19}')
            funcionario = input('Por favor entre com o nome do funcionario: ')
            setor = input('Por favor entre com o setor do funcionario: ')
            salario = float(input('Por favor entre com o salario do funcionario: '))
            funcionario = {'id' : id_global, 'funcionario': funcionario, 'setor': setor, 'salario': salario}
            lista_funcionarios.append(funcionario)
            break
        except ValueError:
            print('Valores inválidos, tente novamente')

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
                return True
            elif opcao == 2:
                return False
            elif opcao == 3:
                return False
            elif opcao == 4:
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
        # elif opcao == 3:
        #     remover_funcionario()
        elif opcao == 4:
            print('Saindo...')
            break
        else:
            raise ValueError
    except ValueError:
        print('Opção inválida')

print(lista_funcionarios)
print(id_global)

