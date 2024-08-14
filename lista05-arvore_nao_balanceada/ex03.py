#copiei da questao passada
def max(arvore):
	if arvore is None:
		return None
	while arvore['dir']:
		arvore = arvore['dir']
	return arvore

def remove_No(arvore, elemento):
	if arvore is None:
		return None
	if arvore['valor'] > elemento:
		arvore['esq'] = remove_No(arvore['esq'], elemento)
	elif arvore['valor'] < elemento:
		arvore['dir'] = remove_No(arvore['dir'], elemento)
	else:
		arvore = remove_casos(arvore)
	return arvore

def remove_casos(arvore):
	if arvore['esq'] is None:
		return arvore['dir']
	elif arvore['dir'] is None:
		return arvore['esq']
	else:
		substituto = max(arvore['esq'])
		arvore['valor'] = substituto['valor']
		arvore['esq'] = remove_No(arvore['esq'], substituto['valor'])
	return arvore

def busca_No(arvore, elemento):
	if arvore is None:
		return None
	if arvore['valor'] == elemento:
		return arvore
	if arvore['valor'] > elemento:
		return busca_No(arvore['esq'], elemento)
	else:
		return busca_No(arvore['dir'], elemento)

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

entrada = input().split(',')

arvore = cria_vazia()

while(entrada[0] != "FIM"):
	if len(entrada) == 2:
		entrada[1] = int(entrada[1])

	if entrada[0] == 'I':
		arvore = insereNaArvore(arvore, entrada[1])
	elif entrada[0] == 'INFIXA':
		em_ordem(arvore)
		print()
	elif entrada[0] == 'PREFIXA':
		pre_ordem(arvore)
		print()
	elif entrada[0] == 'POSFIXA':
		pos_ordem(arvore)
		print()
	elif entrada[0] == 'P':
		elementoBuscado = busca_No(arvore, entrada[1])
		if elementoBuscado is not None:
			print(entrada[1], "existe")
		else:
			print(entrada[1], "nao existe")
	elif entrada[0] == 'R':
		arvore = remove_No(arvore,entrada[1])
		
	entrada = input().split(',')