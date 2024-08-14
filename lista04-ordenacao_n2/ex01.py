def removedup(lis):
	i = 0
	while i < len(lis) - 1:
		if lis[i] == lis[i + 1]:
			lis.pop(i)
			i -= 1
		
		i += 1
def ordenaLista(lis):
	
	i = 0
	while i < len(lis) - 1:
		menor = i
		j = i + 1
		while j < len(lis):
			if lis[j] < lis[menor]:
				menor = j
			j += 1
			
		if i != menor:
			lis[menor], lis[i] = lis[i], lis[menor]
		i += 1


entrada = eval(input())

while len(entrada) != 0:
	ordenaLista(entrada)

	removedup(entrada)
	print(entrada)
	entrada = eval(input())

