class cachorro:
    def __init__(self, raça, cor, nome, sexo, peso, altura, data_nasc):
        self.raça = raça
        self.cor = cor
        self.nome = nome
        self.peso = peso
        self.altura = altura
        self.data_nasc = data_nasc
        self.sexo = sexo
        self.comida = 1000
    
    def comer(self):
        self.comida -= 15
        print(F"o cachorro {self.nome} ainda possui {self.comida} gramas.")

    def lista(self):
        print(f"\n Nome: {self.nome}\n Raça: {self.raça}\n Cor: {self.cor}\n Sexo: {self.sexo}\n Peso: {self.peso}\n Altura: {self.altura}\n Nascimento: {self.data_nasc}")
    
    



if __name__ == '__main__':
    meu_primeiro_cachorro = cachorro("salsicha", "marrom", "Vina", "masculino", 5.590, 32.5, "01/01/2024")
    print(meu_primeiro_cachorro.nome)
    segundo_cachorro = cachorro("Vira lata", "caramelo", "Thor", "masculino", 5, 5, "05/05/2023")
    print(segundo_cachorro)
    terceiro_cachorro = cachorro("Pincher", "Dourado", "Laura", "Femea", 5.100, 14.00, "02/11/2021")
    terceiro_cachorro.comer()
    terceiro_cachorro.lista()