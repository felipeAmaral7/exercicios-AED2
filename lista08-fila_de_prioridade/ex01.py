def aumentar_heap(heap, pos, novo):
	if pos == len(heap):
		heap.append(novo)
	else:
		heap[pos] = novo
	
	while pos > 0 and heap[(pos - 1) // 2] > novo:
		heap[pos], heap[(pos - 1) // 2] = heap[(pos - 1) // 2], heap[pos]
		pos = (pos - 1) //2

entrada = eval(input())

while entrada != []:
	
	pos = int(input())
	num = int(input())
	
	aumentar_heap(entrada, pos, num)
	
	print(entrada)
	entrada = eval(input())