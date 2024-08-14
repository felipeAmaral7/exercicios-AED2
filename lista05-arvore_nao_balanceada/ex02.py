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

entrada = eval(input())

quantArvores = 0
while entrada != []:
	quantArvores += 1
	arvore = cria_vazia()
	for i in entrada:
		arvore = insereNaArvore(arvore, i)
		
	print("Arvore", quantArvores)
	print("Pre-ordem: ", end="")
	pre_ordem(arvore)
	print()
	
	print("In-ordem: ", end="")
	em_ordem(arvore)
	print()
	
	print("Pos-ordem: ", end="")
	pos_ordem(arvore)
	print()
	entrada = eval(input())
	