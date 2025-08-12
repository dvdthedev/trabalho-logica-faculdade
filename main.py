print('Bem vindo a loja do Deivid Rocha')
valor = 0
parcelas = 0

while True:
    try:
        valor = float(input('Insira o valor da parcela: R$'))
        if 1 <= valor:
            break
        else:
            continue
    except:
        print('Valor inválido, digite só números e ponto')

while True:
    try:
        parcelas = int(input('Insira a quantidade de parcelas: '))
        if 1 <= valor:
            break
        else:
            continue
    except:
        print('Valor de parcela inválido')
print(valor,parcelas)

def print_parcela (valor_total):

    print(f'O valor das parcelas é de R$ {valor_total / parcelas:.2f}')
    print(f'O valor total parcelado é de: R$ {valor_total:.2f}')


if parcelas < 4:
    print_parcela( valor)

elif parcelas >= 4 and parcelas < 6:
    valor_total = valor * (1 + (4 / 100))
    print_parcela(valor_total)
elif parcelas >= 6 and parcelas < 9:
    valor_total = valor * (1 + (8 / 100))
    print_parcela((valor_total))
elif parcelas >= 9 and parcelas < 13:
    valor_total = valor * (1 + (16 / 100))
    print_parcela((valor_total))
elif parcelas >= 13:
    valor_total = valor * (1 + (32 / 100))
    print_parcela((valor_total))

