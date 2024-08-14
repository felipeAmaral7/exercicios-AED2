def menorElementoLista(lis):
	menorElemento = lis[0]
	for j in range(0, len(lis)):
		if lis[j] < menorElemento:
			menorElemento = lis[j]
	return menorElemento

def intercalaVetores(lis1, lis2):
	result = []
	
	while lis1 != [] or lis2 != []:
		if lis1 == []:
			result.append(lis2[0])
			lis2.remove(lis2[0])
		elif lis2 == []:
			result.append(lis1[0])
			lis1.remove(lis1[0])
		else:
			removeLis1 = True
			menorLis1 = menorElementoLista(lis1)
			menorLis2 = menorElementoLista(lis2)

			menorListas = menorLis1
			if menorLis2 < menorLis1:
				menorListas = menorLis2
				removeLis1 = False
				
			result.append(menorListas)
			if removeLis1:
				lis1.remove(menorListas)
			else:
				lis2.remove(menorListas)

	return result

lis1 = eval(input())
lis2 = eval(input())
input()

saida = []
while lis1 != [] or lis2 != []:
	saida.append(intercalaVetores(lis1, lis2))
	
	lis1 = eval(input())
	lis2 = eval(input())
	input()
	
for i in range(0, len(saida)):
	print(saida[i])

