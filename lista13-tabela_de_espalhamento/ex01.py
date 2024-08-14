def insereNaTabela(tabela, valor, tam, i):
	pos = (valor + i) % tam
	if tabela[pos] is None:
		tabela[pos] = valor
	else:
		insereNaTabela(tabela, valor, tam, i + 1)
	
	return tabela

def main():
	tamTabela = int(input())
	tamEntrada = int(input())

	tabela = [None] * tamTabela

	for i in range(tamEntrada):
		valor = int(input())
		tabela = insereNaTabela(tabela, valor, tamTabela, 0)

	for indice in range(len(tabela)):
		if tabela[indice] is not None:
			print("%d: %d" % (indice, tabela[indice]))

main()