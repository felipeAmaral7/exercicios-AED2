def valorRoda(config, roda):
	return (config // 10 ** (4 - roda)) % 10

def gira(config, roda, sentido):
	peso = 10 ** (4 - roda)

	digitoAtual = (config // peso) % 10

	if sentido == 'a':
		proximoDigito = (digitoAtual + 9) % 10
	else:
		proximoDigito = (digitoAtual + 1) % 10

	subtrair = digitoAtual * peso
	somar = proximoDigito * peso

	return config - subtrair + somar

class Estado:
	def __init__(self, numero, proibidos, custo):
		# Guarda a configuração atual e a coleção de
		# estados proibidos
		self.numero = numero
		self.proibidos = proibidos

		# Guarda o custo para chegar até o estado atual
		self.custo = custo

	def transicoes(self):
		# Complete-me
		saida = []  # Deve retornar os estados alcançáveis 

	def __repr__(self):
		# Converte o objeto em uma string
		return "{:04d}".format(self.numero)

