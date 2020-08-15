B = '-'
G = '#'

matriz = [
	[B, B, B, G, G],
	[B, G, B, B, G],
	[B, B, G, B, B],
	[G, B, B, G, B],
	[G, G, B, B, B]]

def acomodar_baldosas(matriz):
	num_B = hallar_num_B(matriz)
	acomodar_baldosas_(matriz, 0, 0, num_B, 1)

def hallar_num_B(matriz):
	num_B = 0
	for fila in matriz:
		for col in fila:
			if col == B:
				num_B += 1
	return num_B

def acomodar_baldosas_(matriz, fila, col, num_B, i):
	if num_B == 0:
		imprimir_matriz(matriz)
		return
	while fila < len(matriz):
		while col < len(matriz[fila]):
			if matriz[fila][col] == B:
				matriz[fila][col] = i
				# baldosa horizontal
				if es_pos_valida(fila, col + 1, matriz):
					matriz[fila][col + 1] = i
					acomodar_baldosas_(matriz, fila, col + 2, num_B - 2, i + 1)
					matriz[fila][col + 1] = B
				# baldosa vertical
				if es_pos_valida(fila + 1, col, matriz):
					matriz[fila + 1][col] = i
					acomodar_baldosas_(matriz, fila, col + 1, num_B - 2, i + 1)
					matriz[fila + 1][col] = B
				matriz[fila][col] = B
			col += 1
		fila += 1
		col = 0

def imprimir_matriz(matriz):
	for fila in matriz:
		for col in fila:
			print(col, end=' ')
		print('')
	print('')

def es_pos_valida(fila, col, matriz):
	return 0 <= fila < len(matriz) and 0 <= col < len(matriz[fila]) and matriz[fila][col] == B

acomodar_baldosas(matriz)