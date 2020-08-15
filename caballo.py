# MOVS = [(DELTA_FILA, DELTA_COL), ...]
MOVS = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

def problema_caballo(n, fila=0, col=0, tablero=None, i=1):
	if tablero is None:
		tablero = []
		for i_ in range(n):
			tablero.append([0] * n)

	tablero[fila][col] = i
	if i == n * n:
		imprimir_tablero(tablero)
	else:
		for mov in MOVS:
			if es_mov_valido(mov, fila, col, tablero):
				problema_caballo(n, fila + mov[0], col + mov[1], tablero, i + 1)
	tablero[fila][col] = 0

def imprimir_tablero(tablero):
	for fila in tablero:
		for col in fila:
			print('%3d' % col, end='')
		print('')
	print('')

def es_mov_valido(mov, fila, col, tablero):
	fila2 = fila + mov[0]
	col2 = col + mov[1]
	return 0 <= fila2 < len(tablero) and 0 <= col2 < len(tablero[fila2]) and tablero[fila2][col2] == 0

problema_caballo(8)