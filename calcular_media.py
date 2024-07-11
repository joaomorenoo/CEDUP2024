notas = []

#criar funçoes
def ler_nota():
    notas.append(float(input("Digite uma nota: ")))

ler_nota()
ler_nota()
ler_nota()

media =(sum(notas)/len(notas))

#round serve para arredondar o numero decimal em quantas casas desejadas
print(round(media, 2))



