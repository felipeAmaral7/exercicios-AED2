def pre_ordem(arvore):
	if arvore is not None:
		print(arvore['valor'], end=" ")
		pre_ordem(arvore['esq'])
		pre_ordem(arvore['dir'])
		
def em_ordem(arvore):
	if arvore is not None:
		em_ordem(arvore['esq'])
		print(arvore['valor'], end=" ")
		em_ordem(arvore['dir'])
	
def pos_ordem(arvore):
	if arvore is not None:
		pos_ordem(arvore['esq'])
		pos_ordem(arvore['dir'])
		print(arvore['valor'], end=" ")

def cria_vazia():
	return None

def criar_No(valor):
	return {'valor': valor, 'esq': None, 'dir': None}

def insereNaArvore(arvore, elemento):
	if arvore is None:
		return criar_No(elemento)
	if arvore['valor'] > elemento:
		arvore['esq'] = insereNaArvore(arvore['esq'], elemento)
	else:
		arvore['dir'] = insereNaArvore(arvore['dir'], elemento)
	
	return arvore

def rotacaoRR(raizAntiga):
	#arvore direita da raiz recebe nulo
	#subarvore direita da raiz "sobe" e se torna a nova raiz
	#raiz antiga se torna filho esquerdo da raiz atual
	novaRaiz = raizAntiga['dir']
	
	subArvoreTemp = novaRaiz['esq']
	
	novaRaiz['esq'] = None
	raizAntiga['dir'] = None
	
	raizAntiga['dir'] = subArvoreTemp

	novaRaiz['esq'] = raizAntiga
	
	return novaRaiz
	
entrada = eval(input())

contador = 0

while entrada != []:
	
	arvore = cria_vazia()
	
	contador += 1
	print("Arvore", contador)
	
	for elemento in entrada:
		arvore = insereNaArvore(arvore, elemento)
	
	arvore = rotacaoRR(arvore)
	
	print("pre: ", end='')
	pre_ordem(arvore)
	
	print("\npos: ", end='')
	pos_ordem(arvore)
	print("\n")
		
	entrada = eval(input())