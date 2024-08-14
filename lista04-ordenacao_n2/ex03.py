def semMenor(tupla):
	i = 1
	menor = tupla[1]
	soma = 0
	while i < len(tupla):
		if tupla[i] < menor:
			menor = tupla[i]
		soma += tupla[i]
		i += 1
	return soma - menor

def bubbleSort(lista):
	i = 0
	for i in range(len(lista)):
		for j in range(len(lista) - 1, i, -1):
			if lista[j][1] > lista[j - 1][1]:
				lista[j], lista[j - 1] = lista[j - 1], lista[j]
			elif(lista[j][1] == lista[j - 1][1]):
				if lista[j][2] < lista[j - 1][2]:
					lista[j], lista[j - 1] = lista[j - 1], lista[j]
				
		i += 1
	return lista

tam = int(input())

lis = []
i = 0
while i < tam:
	tup = eval(input())
	nome = tup[0]
	nota = semMenor(tup)
	lis.append((nome, nota, i))
	i += 1
	
lis = bubbleSort(lis)

for i in range(len(lis)):
		print(lis[i][0], ": ", lis[i][1], sep="")