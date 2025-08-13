print('Bem vindo a loja do Deivid Alves da Rocha')
valorDoPedido = 0
quantidadeParcelas = 0

#Laço de repetição para obrigar o usuário digitar um valor float válido para o pedido
while True:
    try:
        valorDoPedido = float(input('Insira o valor do pedido: R$'))
        if 1 <= valorDoPedido:
            break
        else:
            continue
    except:
        print('Valor inválido, digite só números e ponto')

#Laço de repetição para obrigar o usuário digitar um valor int válido de parcelas
while True:
    try:
        quantidadeParcelas = int(input('Insira a quantidade de parcelas: '))
        if 1 <= valorDoPedido:
            break
        else:
            continue
    except:
        print('Valor de parcela inválido')

def print_parcela (valorTotal):
    """
    Args:
        valorTotal : Utilizado para retorno do valor total e para o cálculo de parcelas

    Returns:
        None: print com valores visuais para o usuário

    """

    valorDaParcela = valorTotal / quantidadeParcelas
    print(f'O valor das parcelas é de R$ {valorDaParcela:.2f}')
    print(f'O valor total parcelado é de: R$ {valorTotal:.2f}')


if quantidadeParcelas < 4:
    print_parcela(valorDoPedido)

elif quantidadeParcelas >= 4 and quantidadeParcelas < 6:
    valorTotalParcelado = valorDoPedido * (1 + (4 / 100))
    print_parcela(valorTotalParcelado)
elif quantidadeParcelas >= 6 and quantidadeParcelas < 9:
    valorTotalParcelado = valorDoPedido * (1 + (8 / 100))
    print_parcela((valorTotalParcelado))
elif quantidadeParcelas >= 9 and quantidadeParcelas < 13:
    valorTotalParcelado = valorDoPedido * (1 + (16 / 100))
    print_parcela((valorTotalParcelado))
else:
    valorTotalParcelado = valorDoPedido * (1 + (32 / 100))
    print_parcela((valorTotalParcelado))

