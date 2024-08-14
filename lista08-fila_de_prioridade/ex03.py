class valores:
	def __init__(self, chave, dado):
		self.chave = chave
		self.dado = dado
		
	def __lt__(self, other):
		if self.chave == other.chave:
			return self.dado > other.dado
		return self.chave < other.chave
	
def montar_heap(vet, tam): 
	ult = tam // 2 - 1
	for i in range(ult, -1, -1):
		heapify_max(vet, i, tam)
	
def heapify_max(vet, raiz, tam):
	maior = raiz
	esquerda = raiz * 2 + 1
	direita = raiz * 2 + 2
	
	if esquerda < tam and vet[esquerda] > vet[maior]:
		maior = esquerda
		
	if direita < tam and vet[direita] > vet[maior]:
		maior = direita
		
	if maior != raiz:
		vet[raiz], vet[maior] = vet[maior], vet[raiz]
		heapify_max(vet, maior, tam)

def remove_fila(lista, tam):
	ult = tam - 1
	lista[0], lista[ult] = lista[ult], lista[0]
	
	removido = lista.pop()
	heapify_max(lista, 0, tam - 1)
	
	return removido.dado
entrada = int(input())
lista = []
while entrada != 0:
	if entrada == 1:
		#inserir um elemento na fila
		prioridade = int(input())
		palavra = input()
		obj_valores = valores(prioridade, palavra)
		lista.append(obj_valores)
		
	elif entrada == 2:
		print(remove_fila(lista, len(lista)))
		
	montar_heap(lista, len(lista))
	entrada = int(input())
