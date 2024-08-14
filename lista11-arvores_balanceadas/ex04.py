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

def insereNaArvore(arvore, elemento):
	if arvore is None:
		return criar_No(elemento)
	if arvore['valor'] > elemento:
		arvore['esq'] = insereNaArvore(arvore['esq'], elemento)
		atualiza_tamanho(arvore)
		arvore = verificaAVL(arvore)
	else:
		arvore['dir'] = insereNaArvore(arvore['dir'], elemento)
		atualiza_tamanho(arvore)
		arvore = verificaAVL(arvore)
	
	return arvore

def printa_arvore(arvore):
	print("pre: ", end='')
	pre_ordem(arvore)
	
	print("\npos: ", end='')
	pos_ordem(arvore)
	print("\n")
	
def atualiza_tamanho(arvore):
	if arvore is None:
		return 0
	else:
		tamanhoSubDireita = 1 + atualiza_tamanho(arvore['dir'])
		tamanhoSubEsquerda = 1 + atualiza_tamanho(arvore['esq'])
		if tamanhoSubDireita > tamanhoSubEsquerda:
			arvore['h'] = tamanhoSubDireita
			return tamanhoSubDireita
		else:
			arvore['h'] = tamanhoSubEsquerda
			return tamanhoSubEsquerda

def obter_altura(arvore):
	return arvore['h']

def fator_balanceamento(arvore):
	fatorBalanceamento = 0
	if arvore['dir'] is not None and arvore['esq'] is not None:
		fatorBalanceamento = obter_altura(arvore['dir']) - obter_altura(arvore['esq'])\
		
	elif arvore['dir'] is None:
		fatorBalanceamento = -1 * obter_altura(arvore['esq'])
		
	elif arvore['esq'] is None:
		fatorBalanceamento = obter_altura(arvore['dir'])
		
	return fatorBalanceamento
	
def verificaAVL(arvore):
	fatorPai = fator_balanceamento(arvore)
	if fatorPai == 2:
		fatorFilho = fator_balanceamento(arvore['dir'])
		if fatorFilho < 0:
			arvore['dir'] = rotacaoLL(arvore['dir'])
		arvore = rotacaoRR(arvore)
	elif fatorPai == -2:
		fatorFilho = fator_balanceamento(arvore['esq'])
		if fatorFilho > 0:
			arvore['esq'] = rotacaoRR(arvore['esq'])
		arvore = rotacaoLL(arvore)
		
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
	
	for elemento in entrada:
		arvore = insereNaArvore(arvore, elemento)
	
	print("Arvore", contador)
	printa_arvore(arvore)
	
	entrada = eval(input())