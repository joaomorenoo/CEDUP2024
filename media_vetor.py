nome = input("digite o nome do aluno: ")
notas = []

#adicionar elemento ao ultimo espaço do vetor
notas.append(7.5)
notas.append(8.5)
notas.append(3.5)
print(notas)

#remover o elemento do ultimo elemento (dentro dos parametros pode ser colocado o indice do vetor)
notas.pop()
print(notas)

#comando usado para mostrar o tamanho do vetor
len(notas)
print(len(notas))

#comando para imprimir o maior valor ou a ordem alfabetica e o menor
print(max(notas))
print(min(notas))

#comando para somar os elementos do vetor
print(sum(notas))