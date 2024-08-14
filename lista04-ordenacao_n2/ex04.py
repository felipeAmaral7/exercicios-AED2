class Time:
	def __init__(self, nome, vitorias, empates, derrotas, golsMarcados, golsRecebidos):
		self.nome = nome
		self.pontos = (vitorias * 3) + empates
		self.jogos = vitorias + empates + derrotas
		self.difGols = golsMarcados - golsRecebidos
		
		self.vitorias = vitorias
		self.empates = empates
		self.derrotas = derrotas
		
		self.golsMarcados = golsMarcados
		self.golsRecebidos = golsRecebidos
	
	def __lt__(self, other):
		if self.pontos == other.pontos:
			if self.vitorias != other.vitorias:
				return self.vitorias > other.vitorias
			else:
				if self.difGols != other.difGols:
					return self.difGols > other.difGols
				else:
					if self.golsMarcados != other.golsMarcados:
						return self.golsMarcados > other.golsMarcados
					else:
						if self.jogos != other.jogos:
							return self.jogos < other.jogos
						else:
							return self.nome.lower() < other.nome.lower()
					
		return self.pontos > other.pontos

def imprimirTime(time, pos):
	print("{} - {}: {} pontos, {} jogos ({}-{}-{}), d.g. {} ({}-{})".format(pos, time.nome, time.pontos, time.jogos, time.vitorias, time.empates, time.derrotas, time.difGols, time.golsMarcados, time.golsRecebidos))
	
def insertionSort(times):
	for i in range(len(times) - 1):
		prox = times[i + 1]
		
		j = i
		while j >= 0 and prox < times[j]:
			times[j + 1] = times[j]
			j -= 1
			
		times[j + 1] = prox

quantTimes = int(input())
times = []

i = 0
while i < quantTimes:
	entrada = eval(input())
	objTime = Time(entrada[0], entrada[1], entrada[2], entrada[3], entrada[4], entrada[5])
	times.append(objTime)
	i += 1
	
insertionSort(times)

pos = 1
for i in times:
	imprimirTime(i, pos)
	pos += 1