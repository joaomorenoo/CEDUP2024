class pessoa:
    def __init__(self, nome="", sexo="", cpf="", ano_nasc=0, salario_bruto=0):
        self.nome = nome  
        self.sexo = sexo
        self.cpf = cpf
        self.ano_nasc = ano_nasc
        self.idade = self.idade()
        self_salario_bruto = salario_bruto

    def idade(self):
        return 2024 - self.ano_nasc

if __name__ == '__main__':
    pessoa1 = pessoa('João Vitor', 'masculino', '112.416.029-99', 2002)
    print(pessoa1.idade)
    pessoa_input = pessoa()
    pessoa_input.nome = input("Digite o seu nome")