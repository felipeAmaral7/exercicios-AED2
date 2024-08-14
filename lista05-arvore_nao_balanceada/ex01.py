def buscaNo(arvore, valor):
	if arvore is None:
		return None
	if arvore['valor'] == valor:
		return arvore
	if arvore['valor'] > valor:
		return buscaNo(arvore['esq'], valor)
	else:
		return buscaNo(arvore['dir'], valor)
	
arvore = eval(input())
while arvore != {}:
	busca = int(input())

	chavesBuscadas = 0
	chavesEncontradas = 0
	while(busca != -1):
		elementoBuscado = buscaNo(arvore, busca)
		if elementoBuscado is not None:
			print("Chave {} encontrada".format(busca))
			chavesEncontradas += 1
		else:
			print("Chave {} nao encontrada".format(busca))
		chavesBuscadas += 1
		busca = int(input())
	print("Encontrei {} de {} chaves".format(chavesEncontradas, chavesBuscadas))
	
	arvore = eval(input())