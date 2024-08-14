def heap_sort(vet):
	heapOrdenada = []
	for i in range(len(vet)):
		heapOrdenada.insert(0, remove_elemento(vet))
	return heapOrdenada

def heap_max(vet, raiz, tam):
	maior = raiz
	esquerda = raiz * 2 + 1
	direita = raiz * 2 + 2
	
	if esquerda < tam and vet[esquerda] > vet[maior]:
		maior = esquerda
		
	if direita < tam and vet[direita] > vet[maior]:
		maior = direita
		
	if maior != raiz:
		vet[raiz], vet[maior] = vet[maior], vet[raiz]
		heap_max(vet, maior, tam)
		
def remove_elemento(vet):
	ult = len(vet) -1
	vet[0], vet[ult] = vet[ult], vet[0]
	
	elemento = vet.pop()
	heap_max(vet, 0, ult)
	
	return elemento

def montar_heap(vet, tam):
	ultimo = (tam // 2) - 1
	for i in range(ultimo , -1, -1):
		heap_max(vet, i, tam)

entrada = eval(input())

while entrada != []:
	for i in entrada:
		montar_heap(entrada, len(entrada))
		
	heapOrdenada = heap_sort(entrada)
	
	print(heapOrdenada)
	entrada = eval(input())