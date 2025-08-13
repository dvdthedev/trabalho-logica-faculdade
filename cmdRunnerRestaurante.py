from Marmita import Marmita

marmitaDeFrango = Marmita(
    sabor='Filé de Frango(FF)',
    precoPorTamanho={'P' : 15.00, 'M' : 17.00, 'G' : 21.00}
)

marmitaDeBifeAcebolado = Marmita(
    sabor='Bife Acebolado(BA)',
    precoPorTamanho={'P' : 16.00, 'M' : 18.00, 'G' : 22.00}
)

chaveP = 'P'
chaveM = 'M'
chaveG = 'G'

def imprimeLinhaPorTamanhoDeMarmita(tamanho,marmita1, marmita2):
    """

    Args:
        tamanho: Obtem a tamanho da marita afim de utilizar visualmente e passar como parametro
        marmita1: recebe um Objeto do tipo Marmita
        marmita2: recebe um Objeto do tipo Marmita

    Returns: exibe na tela uma linha com tamanho e valores das marmitas repassadas por parametro

    """
    print(
        f'{3 * '-'}|     {tamanho}     |{7 * ' '} R${marmita1.getValor(tamanho):.2f}{7 * ' '}'
        f'|{7 * ' '} R${marmita2.getValor(tamanho)}{7 * ' '} |{3 * '-'}')

print(f'{5 * '-'} Bem-vindo a Loja de marmitas do Deivid Alves da Rocha {5 * '-'}')

bemvindo = f'{5 * '-'} Bem-vindo a Loja de marmitas do Deivid Alves da Rocha {5 * '-'}'

print(f'{28 * '-'}Cardápio{29 * '-'}')
print(f'{65 * '-'}')

print(f'{3 * '-'}|  Tamanho  |  {marmitaDeBifeAcebolado.sabor}  |  {marmitaDeFrango.sabor}  |{3 * '-'}')

imprimeLinhaPorTamanhoDeMarmita('P',marmitaDeBifeAcebolado, marmitaDeFrango)
imprimeLinhaPorTamanhoDeMarmita('M',marmitaDeBifeAcebolado, marmitaDeFrango)
imprimeLinhaPorTamanhoDeMarmita('G',marmitaDeBifeAcebolado, marmitaDeFrango)

print(f'{65 * '-'}')
sabor = ''
acumulador = 0
nomeSabor = ''
tamanhoDaMarmita = ''
opcao = 'S'

while opcao == 'S':
    if opcao.upper() == 'N':
        break

    while True:
        try:
            sabor = input('Entre com o sabor desejado: (BA/FF)').upper()
            if 'BA' == sabor:
                nomeSabor = 'Bife Acebolado'
                break
            elif 'FF' == sabor:
                nomeSabor = 'Filé de Frango'
                break
            else:
                continue
        except:
            print('Sabor inválido, tente novamente.')

    while True:
        try:
            tamanhoDaMarmita = input('Entre com a tamanho da marta: (P/M/G): ').upper()
            if tamanhoDaMarmita == 'P':
                break
            if tamanhoDaMarmita == 'M':
                break
            if tamanhoDaMarmita == 'G':
                break
        except:
            print('Tamanho inválido, tente novamente.')

    if nomeSabor == 'Bife Acebolado':
        if tamanhoDaMarmita == 'P':
            acumulador += marmitaDeBifeAcebolado.getValor(tamanhoDaMarmita)

    while True:
        try:
            opcao = input('Deseja mais alguma coisa? (S/N): ').upper()
            if opcao.upper() == 'S':
                break
            if opcao.upper() == 'N':
                break
        except:
            print('Opção inválida!')
print(nomeSabor, tamanhoDaMarmita, acumulador)