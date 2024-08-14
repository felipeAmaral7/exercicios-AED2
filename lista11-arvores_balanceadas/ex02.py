#colei da questao passada

def pre_ordem(arvore):
	if arvore is not None:
		print(arvore['valor'], end=" ")
		pre_ordem(arvore['esq'])
		pre_ordem(arvore['dir'])
	
def pos_ordem(arvore):
	if arvore is not None:
		pos_ordem(arvore['esq'])
		pos_ordem(arvore['dir'])
		print(arvore['valor'], end=" ")

def cria_vazia():
	return None

def criar_No(valor):
	return {'valor': valor, 'esq': None, 'dir': None, 'h': 1}

def retorna_tamanho(arvore):
	if arvore is None:
		return 0
	else:
		tamanhoSubDireita = 1 + retorna_tamanho(arvore['dir'])
		tamanhoSubEsquerda = 1 + retorna_tamanho(arvore['esq'])
		if tamanhoSubDireita > tamanhoSubEsquerda:
			return tamanhoSubDireita
		else: 
			return tamanhoSubEsquerda

def insereNaArvore(arvore, elemento):
	if arvore is None:
		return criar_No(elemento)
	if arvore['valor'] > elemento:
		arvore['esq'] = insereNaArvore(arvore['esq'], elemento)
	else:
		arvore['dir'] = insereNaArvore(arvore['dir'], elemento)
	
	return arvore

def printa_arvore(arvore):
	print("pre: ", end='')
	pre_ordem(arvore)
	
	print("\npos: ", end='')
	pos_ordem(arvore)
	print("\n")

def rotacaoLL(raizAntiga):
	#arvore esquerda da raiz recebe nulo
	#subarvore esquerda da raiz "sobe" e se torna a nova raiz
	#raiz antiga se torna filho direito da raiz atual
	#raiz antiga recebe o filho direito da raiz atual, na sua esquerda
	novaRaiz = raizAntiga['esq']
	
	subArvoreTemp = novaRaiz['dir']
	
	novaRaiz['dir'] = None
	raizAntiga['esq'] = None
	
	raizAntiga['esq'] = subArvoreTemp

	novaRaiz['dir'] = raizAntiga
	
	return novaRaiz
	
entrada = eval(input())

contador = 0

while entrada != []:
	
	arvore = cria_vazia()
	
	contador += 1
	print("Arvore", contador)
	
	for elemento in entrada:
		arvore = insereNaArvore(arvore, elemento)
	
	arvore = rotacaoLL(arvore)
	fatorBalanceamento = retorna_tamanho(arvore['dir']) - retorna_tamanho(arvore['esq'])
	
	print("h:", retorna_tamanho(arvore))
	print("fb:", fatorBalanceamento)
	printa_arvore(arvore)
		
	entrada = eval(input())