mcs = {'nome': 'Camiseta Manga Curta Simples', 'valor' : 1.8}
mls = {'nome': 'Camiseta Manga Longa Simples', 'valor' : 2.1}
mce = {'nome': 'Camiseta Manga Curta Com Estampa', 'valor' : 2.9}
mle = {'nome': 'Camiseta Manga Longa Com Estampa', 'valor' : 3.2}

def escolha_modelo():
    """
    Pede ao usuário um modelo de camiseta listado
    Returns: retorna o valor da camiseta escolhida

    """
    while True:
        try:
            opcao = input('Entre com o modelo desejado: \n'
                          'MCS - Manga Curta Simples \n'
                          'MLS - Manga Longa Simples \n'
                          'MCE - Manga Curta Estampada \n'
                          'MLE - Manga Longa Estampada \n'
                          '>>').upper()
            if opcao == 'MCS':
                return mcs.get('valor')

            elif opcao == 'MLS':
                return mls.get('valor')
            elif opcao == 'MCE':
                return mce.get('valor')
            elif opcao == 'MLE':
                return mle.get('valor')
            else:
                raise ValueError
        except ValueError:
            print('Escolha inválida, entre com o modelo novamente.')

def num_camisetas():
    """
    Pede ao usuário pra digitar a quantidade de camisetas (número válido)
    Returns: retorna a quantidade de camisetas (com desconto)

    """
    while True:
        try:
            opcao = int(input('Entre com o número de camisetas:'))
            global quantidade_camiseta
            if opcao > 0 and opcao < 20:
                quantidade_camiseta = opcao
                return opcao
            elif opcao >= 20 and opcao < 200:
                quantidade_camiseta = opcao * 0.95
                return opcao *  0.95
            elif opcao >= 200 and opcao < 2000:
                return opcao *  0.93
            elif opcao >= 2000 and opcao <= 20000:
                return opcao *  0.88
            elif opcao > 20000:
                print('Não aceitamos tantas camisetas de uma vez.')
            else:
                raise ValueError

        except ValueError:
            print('O valor digitado não é um número válido (Maior que 0 menor que 20.000)')

def frete():
    """
    Pergunta ao usuário qual frete deseja
    Returns: Valor do frete

    """
    while True:
        try:
            opcao = int(input('Escolha o tipo de frete:\n'
                              '1- Frete por transportadora - R$ 100.00\n'
                              '2- Frete por Sedex - R$ 200.00\n'
                              '0- Retirar pedido na fábrica - R$ 0.00 \n'
                              '>>'))
            if opcao == 0:
                return 0.0
            elif opcao == 1:
                return 100.0
            elif opcao == 2:
                return 200.0
            else:
                raise ValueError
        except ValueError:
            print('Valor inválido, escolha uma opção (1/2/3)')

print('Bem vindo a fábrica de Camisetas do Deivid Alves da Rocha')

modelo = escolha_modelo()
num_camisetas = num_camisetas()
valor_do_frete = frete()
total_a_pagar = (modelo * num_camisetas) + valor_do_frete

print(f'Total: {total_a_pagar:.2f} (Modelo: {modelo} * Quantidade(com desconto): {num_camisetas:.0f} + frete: {valor_do_frete:.2f}')