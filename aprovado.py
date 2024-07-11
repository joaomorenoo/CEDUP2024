
nome = input("qual o nome do aluno: ")
n1 = float(input("digite a primeira nota: "))
n2 = float(input("digite a segunda nota: "))
n3 = float(input("digite a terceira nota: "))
n4 = float(input("digite a quarta nota: "))

media = (n1+n2+n3+n4)/4

print("O aluno", nome, "terminou com média final de:", media)

if media >= 7:
    print("O aluno está aprovado!")
elif media >= 5:
    print("O aluno está em recuperação!")
else:
    ("O aluno está reprovado")
