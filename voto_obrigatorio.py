idade = int(input("Digite sua idade: "))

if idade == 16 or idade == 17 or idade >= 70:
    print("Voto facultativo!")
elif idade >= 18 and idade < 70:
    print("Voto obrigatorio!")
elif idade < 16:
    print("Idade invalida para o voto!")



#if idade >= 18 and idade <=70:
#   print("voto obrigatorio")
#elif idade > 70 or idade >= 16:
#   print("Voto Facultativo")
#else:
#   print("Voto proibido")
