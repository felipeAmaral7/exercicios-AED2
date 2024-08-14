class ordena:
	def __init__(self, lista):
		self.chave = lista[0]
		self.valor = lista[1]
		
	def __lt__(self, other):
		return self.chave < other.chave

def hoare(lista):
	if len(lista) % 2 == 1:
		meio = len(lista) // 2
	else:
		meio = len(lista) // 2 - 1
	pivo = lista[meio]
	i = -1
	j = len(lista)
	
	while True:
		i += 1
		while lista[i] < pivo:
			i += 1
			
		j -= 1
		while lista[j] > pivo:
			j -= 1
		if i < j:
			lista[i], lista[j] = lista[j], lista[i]
		else:
			return j

entrada = eval(input())
casos = 1
while entrada != []:
	valores = []
	print("Caso", casos)
	for i in entrada:
		objValores = ordena(i)
		valores.append(objValores)
		
	corte = hoare(valores)
	
	print("esq: ", end="")
	for i in range(0, corte + 1):
		print(valores[i].valor, end=" ")
	print()
	
	print("dir: ", end="")
	for i in range(corte + 1, len(valores)):
		print(valores[i].valor, end=" ")
	print()
	print()
	entrada = eval(input())
	casos += 1