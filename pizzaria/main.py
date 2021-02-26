from tabela import Tabela
from pedidos import Pedidos

class Main:

    def __init__(self):

        quantidade = 0
        sabor = 0
        tamanho = 0
        pedidoFeito = Pedidos(sabor, quantidade, tamanho)

    def inicio(self):
        print("*********************************")
        print("**-----------------------------**")
        print("**| SEJA BEM VINDO A PIZZARIA |**")
        print("**-----------------------------**")
        print("*********************************\n\n")


    def visualizacaoTabela(self):
        print("Deseja ver o nosso menu? (S/N)")
        resposta = input()
        if resposta == 'S':
            print(Tabela())
            print("Lembre-se de digitar as informações referentes a pizza como mostra no menu a cima\n")
            self.pedido()
        else:
            print("Lembre-se de digitar as informações referentes a pizza como mostra no menu a cima\n")
            self.pedido()


    def pedido(self):
        print("Quantas pizzas você deseja consumir? ")
        quantidade = input()

        print("\nQual sabor de pizza você deseja consumir? ")
        sabor = input()

        print("\nQual será o tamanho de sua pizza? ")
        tamanho = input()

        self.pedidoFeito = Pedidos(sabor, quantidade, tamanho)

        print("\nA baixo está o resumo do pedido:\n")
        print(self.pedidoFeito)

        print("\nDeseja fazer alguma alteração? (S/N) ")
        resposta = input()
        if resposta == 'S':
            print("\n\n")
            self.pedido()
        else:
            self.valor()

    def valor(self):
        self.pedidoFeito.valores()
        print('\n----------------------------------------------------------')
        print("Aqui está o comprovante do pedido, só apresenta-lo no caixa e efetuar o pagamento com o atendente.")
        self.pedidoFeito.notaFiscal()
        print("A pizzaria agradece, tenha uma boa refeição")

    def entrada(self):
        self.inicio()
        self.visualizacaoTabela()
        


########################################################

Main().entrada()