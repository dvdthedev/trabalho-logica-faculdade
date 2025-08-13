#Importa Classe Marmita para o main
from Marmita import Marmita

#Instâncias da Classe Marmita
marmitaDeFrango = Marmita(
    sabor='Filé de Frango(FF)',
    precoPorTamanho={'P' : 15.00, 'M' : 17.00, 'G' : 21.00}
)

marmitaDeBifeAcebolado = Marmita(
    sabor='Bife Acebolado(BA)',
    precoPorTamanho={'P' : 16.00, 'M' : 18.00, 'G' : 22.00}
)
#Parte do código responsável por gerar a parte gráfica do Menu
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

#Variáveis para o funcionamento dos laços
print(f'{65 * '-'}')
sabor = ''
acumulador = 0
tamanho = ''
opcao = 'S'
nomeSabor = ''

while opcao == 'S':
    if opcao.upper() == 'N':
        break
    #Condicionais responsáveis por capturar Sabor e Tamanho.
    while True:
        try:
            sabor = input('Entre com o sabor desejado: (BA/FF)').upper()
            if 'BA' == sabor:
                break
            elif 'FF' == sabor:
                break
            else:
                raise ValueError
        except:
            print('Sabor inválido, tente novamente.')
            print()

    while True:
        try:
            tamanho = input('Entre com a tamanho da marta: (P/M/G): ').upper()
            if tamanho == 'P':
                break
            elif tamanho == 'M':
                break
            elif tamanho == 'G':
                break
            else :
                raise ValueError
        except:
            print('Tamanho inválido, tente novamente.')

    #Condicionais responsáveis por acumular valor e gerar visual
    if sabor == 'BA':
        nomeSabor = 'Bife Acebolado'
        print(f'Você pediu um {nomeSabor} no tamanho {tamanho}: R$ {marmitaDeBifeAcebolado.getValor(tamanho):.2f}')

        if tamanho == 'P':
            acumulador += marmitaDeBifeAcebolado.getValor(tamanho)
        elif tamanho == 'M':
            acumulador += marmitaDeBifeAcebolado.getValor(tamanho)
        elif tamanho == 'G':
            acumulador += marmitaDeBifeAcebolado.getValor(tamanho)
    elif sabor  == 'FF':
        nomeSabor = 'Filé de Frango'
        print(f'Você pediu um {nomeSabor} no tamanho {tamanho}: R$ {marmitaDeFrango.getValor(tamanho):.2f}')

        if tamanho == 'P':
            acumulador += marmitaDeFrango.getValor(tamanho)
        elif tamanho == 'M':
            acumulador += marmitaDeFrango.getValor(tamanho)
        elif tamanho == 'G':
            acumulador += marmitaDeFrango.getValor(tamanho)

    while True:
        try:
            opcao = input('Deseja mais alguma coisa? (S/N): ').upper()
            if opcao.upper() == 'S':
                break
            if opcao.upper() == 'N':
                break
        except:
            print('Opção inválida!')
#Exibe a mensagem de fim do programa, o valor a ser pago.
print(f'O valor total a ser pago: R$ {acumulador:.2f}')