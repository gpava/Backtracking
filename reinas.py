def n_reinas(n, cols=None, fila=0):
	if cols is None:
		cols = [-1] * n
  
	if fila == n:
		imprimir_tablero(cols)
	else:
		for col in range(n):
			if es_pos_valida(fila, col, cols):
				cols[fila] = col
				n_reinas(n, cols, fila + 1)
				cols[fila] = -1

def imprimir_tablero(cols):
	filas = len(cols)
	for col in cols:
		print('- ' * col + 'X ' + '- ' * (filas - col - 1))
	print('')

def es_pos_valida(fila, col, cols):
	for i in range(fila):
		if cols[i] == col or fila - i == abs(col - cols[i]):
			return False
	return True

n_reinas(8)