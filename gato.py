# Función para imprimir el tablero
def imprimir_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))
        print("-" * 9)

# Función para verificar si hay un ganador
def verificar_ganador(tablero, jugador):
    # Revisar filas, columnas y diagonales
    for i in range(3):
        if all([tablero[i][j] == jugador for j in range(3)]):
            return True
        if all([tablero[j][i] == jugador for j in range(3)]):
            return True

    if tablero[0][0] == jugador and tablero[1][1] == jugador and tablero[2][2] == jugador:
        return True
    if tablero[0][2] == jugador and tablero[1][1] == jugador and tablero[2][0] == jugador:
        return True

    return False

# Función para verificar si el tablero está lleno
def tablero_lleno(tablero):
    return all([cell != ' ' for fila in tablero for cell in fila])

# Función de evaluación del tablero
def evaluar(tablero):
    if verificar_ganador(tablero, 'O'):
        return 10  # IA gana
    elif verificar_ganador(tablero, 'X'):
        return -10  # Jugador gana
    else:
        return 0  # Empate

# Función que devuelve las posiciones vacías
def obtener_movimientos_validos(tablero):
    movimientos = []
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == ' ':
                movimientos.append((i, j))
    return movimientos
            
def minimax(tablero, profundidad, es_ia, alpha, beta):
    if verificar_ganador(tablero, 'O'):
        return 10 - profundidad
    if verificar_ganador(tablero, 'X'):
        return profundidad - 10
    if tablero_lleno(tablero):
        return 0

    if es_ia:
        mejor_puntuacion = -float('inf')
        for i in range(3):
            for j in range(3):
                if tablero[i][j] == ' ':
                    tablero[i][j] = 'O'
                    puntuacion = minimax(tablero, profundidad + 1, False, alpha, beta)
                    tablero[i][j] = ' '
                    mejor_puntuacion = max(mejor_puntuacion, puntuacion)
                    alpha = max(alpha, puntuacion)
                    if beta <= alpha:
                        return mejor_puntuacion
        return mejor_puntuacion
    else:
        mejor_puntuacion = float('inf')
        for i in range(3):
            for j in range(3):
                if tablero[i][j] == ' ':
                    tablero[i][j] = 'X'
                    puntuacion = minimax(tablero, profundidad + 1, True, alpha, beta)
                    tablero[i][j] = ' '
                    mejor_puntuacion = min(mejor_puntuacion, puntuacion)
                    beta = min(beta, puntuacion)
                    if beta <= alpha:
                        return mejor_puntuacion
        return mejor_puntuacion

def mejor_jugada(tablero):
    mejor_puntuacion = -float('inf')
    movimiento = None
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == ' ':
                tablero[i][j] = 'O'
                puntuacion = minimax(tablero, 0, False, -float('inf'), float('inf'))
                tablero[i][j] = ' '
                if puntuacion > mejor_puntuacion:
                    mejor_puntuacion = puntuacion
                    movimiento = (i, j)
    return movimiento

def jugar():
    tablero = [[' ' for _ in range(3)] for _ in range(3)]
    jugador_actual = 'X'

    while True:
        imprimir_tablero(tablero)
        if jugador_actual == 'X':
            fila = int(input("Ingresa la fila (0, 1, 2): "))
            columna = int(input("Ingresa la columna (0, 1, 2): "))
            if tablero[fila][columna] == ' ':
                tablero[fila][columna] = 'X'
                if verificar_ganador(tablero, 'X'):
                    imprimir_tablero(tablero)
                    print("¡Ganaste!")
                    break
                jugador_actual = 'O'
            else:
                print("Movimiento inválido, intenta de nuevo.")
        else:
            print("Turno de la IA (O)")
            movimiento = mejor_jugada(tablero)
            tablero[movimiento[0]][movimiento[1]] = 'O'
            if verificar_ganador(tablero, 'O'):
                imprimir_tablero(tablero)
                print("La IA ha ganado.")
                break
            jugador_actual = 'X'

        if tablero_lleno(tablero):
            imprimir_tablero(tablero)
            print("Es un empate.")
            break

jugar()

