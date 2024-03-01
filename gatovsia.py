import random  # Importa el módulo random para generar números aleatorios

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

# Definición de la función para el turno del jugador
def turno_jugador(tablero):
    imprimir_tablero(tablero)  # Imprime el tablero actual
    while True:
        posicion = input("Tu turno, ingresa la posición (0-2,0-2): ")  # Solicita al jugador que ingrese una posición
        fila, columna = map(int, posicion.split(','))  # Divide la entrada del jugador en fila y columna

        if fila < 0 or fila > 2 or columna < 0 or columna > 2:  # Verifica si la posición está dentro de los límites del tablero
            print("Posición no válida. Debe estar entre 0 y 2.")
            continue  # Si no está dentro de los límites, solicita al jugador que ingrese una posición válida

        if tablero[fila][columna] != ' ':  # Verifica si la posición ya está ocupada
            print("Esta casilla ya está ocupada. Intenta de nuevo.")
            continue  # Si la posición ya está ocupada, solicita al jugador que ingrese una posición válida

        tablero[fila][columna] = 'X'  # Coloca el símbolo del jugador en la posición indicada
        break  # Termina el bucle

# Definición de la función para el turno de la máquina
def turno_maquina(tablero):
    while True:
        fila = random.randint(0, 2)  # Genera un número aleatorio entre 0 y 2 para la fila
        columna = random.randint(0, 2)  # Genera un número aleatorio entre 0 y 2 para la columna

        if tablero[fila][columna] == ' ':  # Verifica si la posición está vacía
            tablero[fila][columna] = 'O'  # Coloca el símbolo de la máquina en la posición indicada
            break  # Termina el bucle

# Definición de la función principal del juego
def juego_gato():
    tablero = [[' ' for _ in range(3)] for _ in range(3)]  # Inicializa un tablero de 3x3 con espacios en blanco
    jugadores = ['X', 'O']  # Define los símbolos de los jugadores
    jugador_actual = 0  # Inicializa el jugador actual como el primero en la lista

    while True:  # Bucle principal del juego
        if jugador_actual == 0:  # Si es el turno del jugador
            turno_jugador(tablero)  # Ejecuta la función para el turno del jugador
        else:  # Si es el turno de la máquina
            turno_maquina(tablero)  # Ejecuta la función para el turno de la máquina

        if verificar_ganador(tablero):  # Verifica si hay un ganador
            imprimir_tablero(tablero)  # Imprime el tablero final
            if jugador_actual == 0:  # Si el jugador ganó
                print("¡Felicidades! Has ganado.")
            else:  # Si la máquina ganó
                print("¡La máquina ha ganado!")
            break  # Termina el juego

        if all(' ' not in fila for fila in tablero):  # Verifica si el tablero está lleno
            imprimir_tablero(tablero)  # Imprime el tablero final
            print("¡Empate!")  # Imprime el mensaje de empate
            break  # Termina el juego

        jugador_actual = (jugador_actual + 1) % 2  # Cambia al siguiente jugador

if __name__ == "__main__":
    juego_gato()  # Ejecuta la función principal del juego si se ejecuta el script directamente
