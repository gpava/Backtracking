D = '-'  # disponible
M = '#'  # muro
S = 'O'  # salida
V = 'X'  # visitado

laberinto = [
	[D,D,M,D,D,D],
	[M,D,M,D,M,D],
	[D,D,D,D,M,D],
	[D,M,M,D,M,D],
	[D,D,M,D,D,S]]

# MOVS = [(<DELTA_FILA>, <DELTA_COL>), ...]
MOVS = [
	(-1, 0),  # arriba
	(0, 1),  # derecha
	(1, 0),  # abajo
	(0, -1)]  # izquierda

def hallar_caminos(laberinto, fila=0, col=0):
	if laberinto[fila][col] == S:
		imprimir_laberinto(laberinto)
	else:
		laberinto[fila][col] = V
		for mov in MOVS:
			if es_mov_valido(mov, fila, col, laberinto):
				hallar_caminos(laberinto, fila + mov[0], col + mov[1])
		laberinto[fila][col] = D

def imprimir_laberinto(laberinto):
	for fila in laberinto:
		for celda in fila:
			print(celda, end=' ')
		print('')
	print('')

def es_mov_valido(mov, fila, col, laberinto):
	fila2 = fila + mov[0]
	col2 = col + mov[1]
	return (0 <= fila2 < len(laberinto) and 0 <= col2 < len(laberinto[fila2])
			and (laberinto[fila2][col2] == D or laberinto[fila2][col2] == S))

imprimir_laberinto(laberinto)
hallar_caminos(laberinto)