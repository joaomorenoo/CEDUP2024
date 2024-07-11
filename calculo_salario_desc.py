class pessoa:
    def __init__(self, nome="", sexo="", cpf="", ano_nasc=0, salario_bruto=0, salario_liq=0,INSS=0, IRRF=0):
        self.nome = nome  
        self.sexo = sexo
        self.cpf = cpf
        self.ano_nasc = ano_nasc
        self.idade = self.calc_idade()
        self.salario_bruto = salario_bruto
        self.salario_liq = 0
        self.INSS = 0
        self.IRRF = 0

    def calc_INSS(self):
        if self.salario_bruto <= 1412:
            self.INSS = (self.salario_bruto*7.5)/100
        elif self.salario_bruto < 2666.68:
            self.INSS = (self.salario_bruto*9.0)/100
        elif self.salario_bruto < 4000.03:
            self.INSS = (self.salario_bruto*12)/100
        elif self.salario_bruto < 7786.02:
            self.INSS = (self.salario_bruto*14)/100

    def calc_IRRF(self):
        if self.salario_bruto > 2259.21 and self.salario_bruto < 2824:
            self.IRRF = 564.80
        elif self.salario_bruto > 2826.65:
           self.IRRF = (self.salario_bruto*7.5)/100
        elif self.salario_bruto > 3751.05:
            self.IRRF = (self.salario_bruto*15)/100
        elif self.salario_bruto > 4664.68:
            self.IRRF = (self.salario_bruto*22.5)/100
        elif self.salario_bruto >= 4664.68:
            self.IRRF = (self.salario_bruto*27.5)/100

    def salario_liquido(self):
        self.calc_INSS()
        self.calc_IRRF()
        self.salario_liq = self.salario_bruto - (self.IRRF + self.INSS)

    def calc_idade(self):
        return 2024 - self.ano_nasc

if __name__ == '__main__':
     pessoa1 = pessoa('João Vitor', 'masculino', '112.416.029-99', 2002)
     pessoa1.salario_bruto = int(input('R$'))
     pessoa1.salario_liquido()    
     print(f"{pessoa1.nome} tem salario bruto de R${pessoa1.salario_bruto} e o salario liquido de R${pessoa1.salario_liq}, faz o L")

