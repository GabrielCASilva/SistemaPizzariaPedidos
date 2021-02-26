from tabela import Tabela

class Pedidos(Tabela):

    def __init__(self, sabor, quantidade, tamanho):
        super().__init__()
        self.sabor = sabor
        self.quantidade = quantidade
        self.tamanho = tamanho
        self.valor = 0
        self.correspondente = []

    def __str__(self):
        return f'Sabor escolhido: {self.sabor}, \n'\
            f'Quantidade escolhida: {self.quantidade}.\n'\
            f'Tamanho escolhido: {self.tamanho}.\n'

    def valores(self):
        
        for i, nome in enumerate(Tabela().nomes):
            if self.sabor == nome:
                self.correspondente.append(self.sabor)

                for j, precoS in enumerate(Tabela().precosSabores): 

                    if i == j:
                        self.valor = precoS

        for i, tam in enumerate(Tabela().tamanhos):
            if self.tamanho == tam:
                self.correspondente.append(self.tamanho)

                for j, precoT in enumerate(Tabela().precosTamanhos):

                    if i == j:
                        self.valor += precoT

        resultado = self.valor * int(self.quantidade)

        self.correspondente.append(resultado)

    def notaFiscal(self):
        print(  
            f'----------------------------------------------------------\n'\
            f'Sabor escolhido: {self.correspondente[0]}.\n'\
            f'Quantidade pedida: {self.quantidade}.\n'\
            f'Tamanho escolhido: {self.correspondente[1]}.\n'\
            f'Valor total do pedido: R$ {self.correspondente[2]},00.\n'\
            f'----------------------------------------------------------'
        )
            
        