#fiz no vscode e passei pra ca

class myClass:
	def __init__(self, lista):
		self.chave = lista[0]
		self.valor = lista[1]

	def __lt__(self, other):
		return self.chave < other.chave
	
	def __le__(self,other):
		return self.chave <= other.chave

def intercala(esquerda, direita):
	lista = []
	posEsq, posDir = 0, 0
	while posEsq < len(esquerda) and posDir < len(direita):
		if esquerda[posEsq] <= direita[posDir]:
			lista.append(esquerda[posEsq])
			posEsq += 1
		else:
			lista.append(direita[posDir])
			posDir += 1

	while posEsq < len(esquerda):
		lista.append(esquerda[posEsq])
		posEsq += 1

	while posDir < len(direita):
		lista.append(direita[posDir])
		posDir += 1

	return lista

def mergeSort(lista):
	if len(lista) > 1:
		meio = len(lista) // 2
		esquerda = mergeSort(lista[:meio])
		direita = mergeSort(lista[meio:])
		lista = intercala(esquerda, direita)

	return lista 

def printLista(lista):
	for i in range(0, len(lista)):
		print(lista[i].valor)

entrada = eval(input())
casos = 1
while entrada != []:
	listaValores = []
	for i in range(0, len(entrada)):
		objValores = myClass(entrada[i])
		listaValores.append(objValores)
	listaOrdenada = mergeSort(listaValores)
	print("Caso", casos)
	printLista(listaOrdenada)
	print()
	entrada = eval(input())
	casos += 1