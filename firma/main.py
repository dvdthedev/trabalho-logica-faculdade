
funcionarios = []

def existe_arquivo(arquivo):
    try:
        abrir =  open(arquivo, 'rt', encoding='utf-8')
        abrir.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criar_arquivo(arquivo):
    try:
        abrir =  open(arquivo, 'wt+', encoding='utf-8')
    except FileNotFoundError:
        print('Arquivo não pode ser criado')
    else:
        print('Arquivo criado com sucesso')
    finally:
        abrir.close()

def ler_arquivo(arquivo):
    try:
        a = open(arquivo, 'rt', encoding='utf-8')

        for linha in a:
            linha = linha.rstrip()

        return a.read()
    except FileNotFoundError:
        print('Erro ao ler arquivo')
        return None
    finally:
        a.close()

arquivo = 'file.txt'

if not existe_arquivo(arquivo):
    criar_arquivo(arquivo)

print("Bem vindo a Empresa do Deivid Alves da Rocha")
print('-' * 65)
print(f'{'-' *24} MENU PRINCIPAL {'-' *25}')
print('Escolha a opção desejada: \n'
      '1 - Cadastrar Funcionários \n'
      '2 - Consultar Funcionários \n'
      '3 - Remover Funcionários \n'
      '4 - Sair\n'
      '>>')

print(ler_arquivo(arquivo))