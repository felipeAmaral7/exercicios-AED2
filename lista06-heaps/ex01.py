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
	min_heapify(entrada, 0, len(entrada))
	print(entrada)
	entrada = eval(input())