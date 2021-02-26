class Tabela:
    
    def __init__(self):
        self.nomes = ["Mozzarella", "Portuguesa", "Pepperoni", "Alho"]
        self.tamanhos = ["Grande", "Medio", "Pequeno"]
        self.precosTamanhos = [20, 15, 10]
        self.precosSabores = [3, 10, 8, 5]

    def tabelaSabor(self, nome, precoSabor):
        return f"----------------------------------------------------------\n"\
            f"SABOR ->      {nome}\n"\
            f"TAMANHOS ->   {self.tamanhos[0]}   | {self.tamanhos[1]}    | {self.tamanhos[2]}\n"\
            f"VALORES ->    R$ {precoSabor + self.precosTamanhos[0]},00 "\
            f"| R$ {precoSabor + self.precosTamanhos[1]},00 "\
            f"| R$ {precoSabor + self.precosTamanhos[2]},00 "

    def __str__(self):
        return  f"{self.tabelaSabor(self.nomes[0], self.precosSabores[0])}\n"\
                f"{self.tabelaSabor(self.nomes[1], self.precosSabores[1])}\n"\
                f"{self.tabelaSabor(self.nomes[2], self.precosSabores[2])}\n"\
                f"{self.tabelaSabor(self.nomes[3], self.precosSabores[3])}\n"\
                f"----------------------------------------------------------\n"