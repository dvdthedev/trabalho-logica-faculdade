class Marmita:
    """
    Uma classe para representar o objeto do tipo Marmita
    """
    def __init__(self, sabor, precoPorTamanho):

        self.sabor = sabor
        self.precoPorTamanho = precoPorTamanho

    def getValor(self, tamanho):
        if tamanho in self.precoPorTamanho:
            return self.precoPorTamanho[tamanho]
        else:
            return f'Erro: tamanho {tamanho} não disponível.'

