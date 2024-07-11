import os
import datetime

saldo = 0
contador = 0
movimentacoes = []
now = []

def deposito():
    global saldo
    os.system("cls")
    valor_deposito = int(input("digite o valor depositado: "))
    if valor_deposito <= 0:
        print("Valor invalido para deposito")
        input("digite qualquer tecla para continuar: ")
    else:
        saldo += valor_deposito
        print(f"Deposito efetuado com sucesso, seu saldo é de R${saldo}")
        input("digite qualquer tecla para continuar: ")
        movimentacoes.append(f"+R${valor_deposito}")
        date = "{}/{}/{}-{}:{}:{}".format(datetime.datetime.today().day, datetime.datetime.today().month, datetime.datetime.today().year, datetime.datetime.today().hour, datetime.datetime.today().minute, datetime.datetime.today().second)
        now.append(date)
        
def sacar():
    global saldo
    os.system("cls")
    print(f"seu saldo é de R${saldo}")
    valor_saque = int(input("Digite o valor a ser sacado: "))
    os.system("cls")
    if saldo - valor_saque < 0:
        print("saldo insuficiente para o saque")
        input("digite qualquer tecla para continuar: ")
    else:
        saldo -= valor_saque
        print(f"saque efetuado com sucesso, seu atual saldo é de R${saldo}")
        input("digite qualquer tecla para continuar: ")
        movimentacoes.append(f"-R${valor_saque}")
        date = "{}/{}/{}-{}:{}:{}".format(datetime.datetime.today().day, datetime.datetime.today().month, datetime.datetime.today().year, datetime.datetime.today().hour, datetime.datetime.today().minute, datetime.datetime.today().second)
        now.append(date)
    
def debug():
    global saldo
    saldo = 10000
    
def extrato():
    max = len(movimentacoes)
    max_10 = max - 10
    if max < 10:
        i = max - 1
        while i >= 0:
            print(f"{now[i]} | {movimentacoes[i]}")
            i -= 1
    else:
        i = max - 1
        while i >= max_10:
            print(f"{now[i]} | {movimentacoes[i]}")
            i -= 1
    print(f"seu saldo é de: R${saldo}")
    input("digite qualquer tecla para continuar: ")
    
def caixa_menu():
    valor = 0
    while valor != 4:
        os.system("cls")
        print("-----ITAÚ------")
        print("[1] EXTRATO")
        print("[2] SACAR")
        print("[3] DEPOSITAR")
        print("[4] SAIR")
        print("-----ITAÚ------")
        valor = int(input("Digite a opção desejada: "))
        os.system('cls')
        
        if valor == 1:
            extrato()
        elif valor == 2:
            sacar()
        elif valor == 3:
            deposito()
        elif valor == 99:
            debug()

caixa_menu()