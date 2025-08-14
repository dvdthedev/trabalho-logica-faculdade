mcs = {'nome': 'Camiseta Manga Curta Simples', 'valor' : 1.8}
mls = {'nome': 'Camiseta Manga Longa Simples', 'valor' : 2.1}
mce = {'nome': 'Camiseta Manga Curta Com Estampa', 'valor' : 2.9}
mle = {'nome': 'Camiseta Manga Longa Com Estampa', 'valor' : 3.2}

frete = {'transportadora': 100.0 , 'sedex': 200.0, 'retirar': 0}


def escolha_modelo():
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

quantidade_camiseta = 0
def num_camisetas():
    while True:
        try:
            opcao = int(input('Entre com o número de camisetas:'))
            quantidade_camiseta = opcao
            if opcao > 0 and opcao < 20:
                return (opcao * modelo_escolhido)
            elif opcao >= 20 and opcao < 200:
                quantidade_camiseta * 0.95
                return opcao * (modelo_escolhido * 0.95)
            elif opcao >= 200 and opcao < 2000:
                quantidade_camiseta * 0.93
                return opcao * (modelo_escolhido * 0.93)
            elif opcao >= 2000 and opcao <= 20000:
                quantidade_camiseta * 0.88
                return opcao * (modelo_escolhido * 0.88)
            elif opcao > 20000:
                print('Não aceitamos tantas camisetas de uma vez.')
            else:
                raise ValueError

        except ValueError:
            print('O valor digitado não é um número válido (Maior que 0 menor que 20.000)')

def frete():
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

modelo_escolhido = escolha_modelo()
quantidade_camiseta = num_camisetas()
valor_do_frete = frete()

print(f'Total: {quantidade_camiseta + valor_do_frete:.2f} (Modelo: {modelo_escolhido} * Quantidade(com desconto): {quantidade_camiseta:.0f} + frete: {valor_do_frete:.2f}')