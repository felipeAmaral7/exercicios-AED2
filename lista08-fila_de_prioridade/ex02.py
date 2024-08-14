class valores:
	def __init__(self, chave, dado):
		self.chave = chave
		self.dado = dado
		
	def __lt__(self, other):
		return self.chave < other.chave
	
def montar_heap(vetor, tam):
	ult = tam // 2 - 1
	for i in range(ult, -1, -1):
		heapify_min(vetor, i, tam)

def heapify_min(vetor, raiz, tam):
	menor = raiz
	esquerda = raiz * 2 + 1
	if esquerda < tam and vetor[esquerda] < vetor[menor]:
		menor = esquerda
	
	direita = raiz * 2 + 2
	if direita < tam and vetor[direita] < vetor[menor]:
		menor = direita
		
	if menor != raiz:
		vetor[raiz], vetor[menor] = vetor[menor], vetor[raiz]
		heapify_min(vetor, menor, tam)

entrada = eval(input())
vetorHeap = []

while entrada != ():
	obj_entrada = valores(entrada[0], entrada[1])
	vetorHeap.append(obj_entrada)
	montar_heap(vetorHeap, len(vetorHeap))
	
	entrada = eval(input())

for i in vetorHeap:
	print(i.dado)