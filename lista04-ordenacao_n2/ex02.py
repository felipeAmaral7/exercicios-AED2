from math import sqrt

class ponto:
	def __init__(self, x, y):
		# Construtor.
		# Guarde os atributos self.x e self.y
		self.x = x
		self.y = y
		self.distOrigem = sqrt(pow(x, 2) + pow(y, 2))

	def __lt__(self, outro):
		# Sobrecarga do operador <
		if self.distOrigem == outro.distOrigem and self.x == outro.x:
			return self.y < outro.y
		if self.distOrigem == outro.distOrigem:
			return self.x < outro.x
		return self.distOrigem < outro.distOrigem

# Leitura da entrada
entrada = eval(input())

# Crie uma lista vazia e insira os objetos da classe ponto nela
pontos = []
for item in entrada:
	# processe...
	objPontos = ponto(item[0], item[1])
	pontos.append(objPontos)

pontos.sort()

i = 0
for i in pontos:
	print(i.x, i.y)

# Ordene e imprima de acordo com o enunciado