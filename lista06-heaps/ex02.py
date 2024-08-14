def montar_heap(vet, tam):
	ultimo = (tam // 2) - 1
	for i in range(ultimo, -1, -1):
		min_heapify(vet, i, tam)

def min_heapify(vet, raiz, tam):
	menor = raiz
	esquerda = raiz * 2 + 1
	if esquerda < tam and vet[esquerda] < vet[menor]:
		menor = esquerda
		
	direita = raiz * 2 + 2
	if direita < tam and vet[direita] < vet[menor]:
		menor = direita
	
	if menor != raiz:
		vet[raiz], vet[menor] = vet[menor], vet[raiz]
		min_heapify(vet, menor, tam)
		
entrada = eval(input())
heapify = []

while entrada != []:
	montar_heap(entrada, len(entrada))
	print(entrada)
	entrada = eval(input())