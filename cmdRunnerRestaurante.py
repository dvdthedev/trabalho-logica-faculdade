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