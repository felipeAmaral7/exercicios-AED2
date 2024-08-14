def transforma_letra(chave, alfabeto):
	if chave == '-':
		return 0
	else:
		return alfabeto[chave]
		
def valor_em_numero(chave, alfabeto):
	somatorio = 0
	for i in chave:
		somatorio += transforma_letra(i, alfabeto)
	
	return somatorio

def inserir_na_tabela(tabela, chave, tam, i, alfabeto):
	
	valorNumerico = valor_em_numero(chave, alfabeto)
	
	hLinha = ((valorNumerico % tam) + i) % tam
	
	if tabela[hLinha] is None:
		tabela[hLinha] = chave
	else:
		inserir_na_tabela(tabela, chave, tam, i + 1, alfabeto)
	return tabela

def main():
	tamTabela = int(input())

	tamEntrada = int(input())

	tabela = [None] * tamTabela

	alfabeto = {}
		#chr(i): i - 96 for i in range(97, 123)
	for i in range(97, 123):
		letra = chr(i)
		num = i - 96
		alfabeto[letra] = num

	for i in range(tamEntrada):
		chave = input()
		if chave is not int:
			tabela = inserir_na_tabela(tabela, chave, tamTabela, 0, alfabeto)

	for i in range(tamTabela):
		if tabela[i] is not None:
			print("%d: %s" % (i, tabela[i]))
			
main()