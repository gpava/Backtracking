B = 0
N = 1
V = 2

def indicar_grupos(tablero):
	grupos = []
	for fila in range(len(tablero)):
		for col in range(len(tablero[fila])):
			if tablero[fila][col] == N:
				tam_grupo = id_grupo(tablero, fila, col)
				if tam_grupo > 1:
					grupos.append((len(grupos) + 1, tam_grupo))
	return grupos

MOVS = ((-1, 0), (1, 0), (0, -1), (0, 1))

def id_grupo(tablero, fila, col):
	tam_grupo = 1
	tablero[fila][col] = V
	for mov in MOVS:
		fila2 = fila + mov[0]
		col2 = col + mov[1]
		if 0 <= fila2 < len(tablero) and 0 <= col2 < len(tablero[fila2]) and tablero[fila2][col2] == N:
			tam_grupo += id_grupo(tablero, fila2, col2)
	return tam_grupo

tablero = [
	[B,B,B,B,B,B,B,B],
	[B,B,B,N,B,B,B,B],
	[B,B,B,N,B,B,B,B],
	[B,B,B,B,B,B,N,B],
	[B,B,N,N,B,N,N,B],
	[B,B,B,B,B,B,N,B],
	[B,B,B,B,B,N,B,B],
	[B,B,B,B,N,B,B,B]]

print(indicar_grupos(tablero))