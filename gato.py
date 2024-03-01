# Definición de la función para imprimir el tablero
def imprimir_tablero(tablero):
    for fila in tablero:
        print("|".join(fila))  # Imprime cada fila del tablero, separando los elementos por "|"
    print("\n")

# Definición de la función para verificar si hay un ganador
def verificar_ganador(tablero):
    # Verificar filas
    for fila in tablero:
        if fila[0] == fila[1] == fila[2] != ' ':  # Si los tres elementos de la fila son iguales y no son espacios en blanco, hay un ganador
            return True

    # Verificar columnas
    for col in range(3):
        if tablero[0][col] == tablero[1][col] == tablero[2][col] != ' ':  # Si los tres elementos de la columna son iguales y no son espacios en blanco, hay un ganador
            return True

    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != ' ':  # Si los tres elementos de la diagonal principal son iguales y no son espacios en blanco, hay un ganador
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != ' ':  # Si los tres elementos de la diagonal secundaria son iguales y no son espacios en blanco, hay un ganador
        return True

    return False  # Si no hay ganador, devuelve False

# Definición de la función principal del juego
def juego_gato():
    tablero = [[' ' for _ in range(3)] for _ in range(3)]  # Inicializa un tablero de 3x3 con espacios en blanco
    jugadores = ['X', 'O']  # Define los símbolos de los jugadores
    jugador_actual = 0  # Inicializa el jugador actual como el primero en la lista

    while True:  # Bucle principal del juego
        imprimir_tablero(tablero)  # Imprime el tablero actual
        posicion = input(f"Jugador {jugadores[jugador_actual]}, ingresa una posición entre (0-2): ")  # Solicita al jugador que ingrese una posición
        fila, columna = map(int, posicion.split(','))  # Divide la entrada del jugador en fila y columna

        if fila < 0 or fila > 2 or columna < 0 or columna > 2:  # Verifica si la posición está dentro de los límites del tablero
            print("Posición no válida. Debe estar entre 0 y 2.")
            continue  # Si no está dentro de los límites, solicita al jugador que ingrese una posición válida

        if tablero[fila][columna] != ' ':  # Verifica si la posición ya está ocupada
            print("Esta casilla ya está ocupada. Intenta de nuevo.")
            continue  # Si la posición ya está ocupada, solicita al jugador que ingrese una posición válida

        tablero[fila][columna] = jugadores[jugador_actual]  # Coloca el símbolo del jugador actual en la posición indicada

        if verificar_ganador(tablero):  # Verifica si hay un ganador
            imprimir_tablero(tablero)  # Imprime el tablero final
            print(f"¡Jugador {jugadores[jugador_actual]} ha ganado!")  # Imprime el mensaje de victoria
            break  # Si hay un ganador, termina el juego

        if all(' ' not in fila for fila in tablero):  # Verifica si el tablero está lleno
            imprimir_tablero(tablero)  # Imprime el tablero final
            print("¡Empate!")  # Imprime el mensaje de empate
            break  # Si el tablero está lleno, termina el juego

        jugador_actual = (jugador_actual + 1) % 2  # Cambia al siguiente jugador

if __name__ == "__main__":
    juego_gato()  # Ejecuta la función principal del juego si se ejecuta el script directamente
