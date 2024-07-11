
notas = []

#criar funçoes
def ler_nota():
    notas.append(float(input("Digite uma nota: ")))

ler_nota()
ler_nota()
ler_nota()

print(len(notas))
print(notas)