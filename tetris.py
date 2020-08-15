# piezas = [pieza1, pieza2, ...]
# pieza = [[delta_fila1, delta_col1], [delta_fila2, delta_col2], ...]
"""piezas = [
    [[0,0], [0,1], [1,1], [1,2]],
    [[0,0], [0,1], [1,0], [1,-1]],
    [[0,0], [1,0], [1,-1], [2,-1]],
    [[0,0], [1,0], [1,1], [2,1]]
]
"""

piezas = [
    [[0,0], [1,0], [0,1], [0,2]],
    [[0,0], [1,0], [1,-1], [1,-2]]
]

def tetris(numFilas, numCols, piezas):
    matriz = []
    for i in range(numFilas):
        matriz.append([0] * numCols)
    tetris_(matriz, 0, 0, piezas, numFilas * numCols, 1)

def tetris_(matriz, fila, col, piezas, numDisponibles, i):
    if numDisponibles <= 0:
        imprimir_matriz(matriz)
        return
    while fila < len(matriz):
        while col < len(matriz[fila]):
            for pieza in piezas:
                if es_pieza_valida(pieza, fila, col, matriz):
                    llenar_pieza(pieza, fila, col, matriz, i)
                    tetris_(matriz, fila, col + 1, piezas, numDisponibles - len(pieza), i + 1)
                    llenar_pieza(pieza, fila, col, matriz, 0)
            col += 1
        fila += 1
        col = 0

def es_pieza_valida(pieza, fila, col, matriz):
    for mov in pieza:
        fila2 = fila + mov[0]
        col2 = col + mov[1]
        if (fila2 < 0 or fila2 >= len(matriz)
                or col2 < 0 or col2 >= len(matriz[fila])
                or matriz[fila2][col2] != 0):
            return False
    return True

def llenar_pieza(pieza, fila, col, matriz, i):
    for mov in pieza:
        matriz[fila + mov[0]][col + mov[1]] = i

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)
    print('')

tetris(4, 4, piezas)