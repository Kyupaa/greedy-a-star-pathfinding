
import heapq  # permite organizar las posiciones por prioridad
import time   # sirve para medir el tiempo de ejecucion


# mapa con el inicio, la meta, los espacios libres y los obstaculos
mapa = [
    ['S', '.', '.', '#', '.', '.', '.'],
    ['#', '#', '.', '#', '.', '#', '.'],
    ['.', '.', '.', '.', '.', '#', '.'],
    ['.', '#', '#', '#', '.', '.', '.'],
    ['.', '.', '.', '#', '.', '#', '.'],
    ['.', '#', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '#', '#', '.', 'G']
]


# coordenadas del inicio y del objetivo
inicio = (0, 0)
objetivo = (6, 6)


# movimientos permitidos: arriba, abajo, izquierda y derecha
movimientos = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]


# calcula la distancia manhattan para estimar cuanto falta para llegar a la meta
def heuristica(estado, objetivo):
    fila, columna = estado
    fila_obj, columna_obj = objetivo

    return abs(fila - fila_obj) + abs(columna - columna_obj)


# comprueba que la posicion este dentro del mapa y no sea un obstaculo
def movimiento_valido(posicion, mapa):
    fila, columna = posicion

    if not (0 <= fila < len(mapa)):
        return False

    if not (0 <= columna < len(mapa[0])):
        return False

    if mapa[fila][columna] == '#':
        return False

    return True


# reconstruye el camino siguiendo las posiciones anteriores hasta el inicio
def reconstruir_ruta(padres, objetivo):
    ruta = []
    estado = objetivo

    while estado is not None:
        ruta.append(estado)
        estado = padres[estado]

    # invertimos la lista para mostrar el camino desde el inicio hasta la meta
    ruta.reverse()
    return ruta


# greedy elige primero la posicion que parece mas cercana al objetivo
def greedy(mapa, inicio, objetivo):
    frontera = []

    # agregamos el inicio usando su distancia estimada como prioridad
    heapq.heappush(frontera, (heuristica(inicio, objetivo), inicio))

    visitados = set()       # posiciones que ya se procesaron
    descubiertos = {inicio} # posiciones que ya se encontraron
    padres = {inicio: None} # guarda de donde viene cada posicion
    explorados = 0

    while frontera:
        h, actual = heapq.heappop(frontera)

        # evitamos procesar posiciones repetidas
        if actual in visitados:
            continue

        visitados.add(actual)
        explorados += 1

        # si llegamos a la meta, devolvemos la ruta y los estados explorados
        if actual == objetivo:
            ruta = reconstruir_ruta(padres, objetivo)
            return ruta, explorados

        fila, columna = actual

        # revisamos los cuatro vecinos de la posicion actual
        for df, dc in movimientos:
            vecino = (fila + df, columna + dc)

            if not movimiento_valido(vecino, mapa):
                continue

            if vecino in descubiertos:
                continue

            descubiertos.add(vecino)
            padres[vecino] = actual

            # agregamos el vecino usando solamente su distancia estimada
            heapq.heappush(
                frontera,
                (heuristica(vecino, objetivo), vecino)
            )

    # se devuelve none si no se encuentra una ruta
    return None, explorados


# a* considera el costo recorrido y la distancia estimada hasta la meta
def astar(mapa, inicio, objetivo):
    frontera = []
    costos = {inicio: 0}  # costo minimo conocido para llegar a cada posicion
    padres = {inicio: None}

    h = heuristica(inicio, objetivo)

    # guardamos la prioridad total, el costo recorrido y la posicion
    heapq.heappush(frontera, (h, 0, inicio))
    explorados = 0

    while frontera:
        f, costo_actual, actual = heapq.heappop(frontera)

        # ignoramos registros que ya no tienen el mejor costo conocido
        if costo_actual != costos.get(actual):
            continue

        explorados += 1

        if actual == objetivo:
            ruta = reconstruir_ruta(padres, objetivo)
            return ruta, explorados

        fila, columna = actual

        for df, dc in movimientos:
            vecino = (fila + df, columna + dc)

            if not movimiento_valido(vecino, mapa):
                continue

            # cada movimiento tiene un costo de uno
            nuevo_costo = costo_actual + 1

            # actualizamos la posicion solo si encontramos un camino mas barato
            if nuevo_costo < costos.get(vecino, float('inf')):
                costos[vecino] = nuevo_costo
                padres[vecino] = actual

                h = heuristica(vecino, objetivo)

                # sumamos el costo recorrido y la distancia estimada
                f_nuevo = nuevo_costo + h

                heapq.heappush(
                    frontera,
                    (f_nuevo, nuevo_costo, vecino)
                )

    return None, explorados


# muestra la ruta, los movimientos y los estados explorados
def mostrar_resultado(nombre, resultado):
    ruta, explorados = resultado

    print("\n--- resultado de", nombre, "---")

    if ruta is None:
        print("no se encontro una ruta")
        print("estados explorados:", explorados)
        return

    print("ruta encontrada:")

    for posicion in ruta:
        print(posicion, end=" -> ")

    print("fin")
    print("cantidad de movimientos:", len(ruta) - 1)
    print("estados explorados:", explorados)


# menu para elegir el algoritmo y medir su tiempo de ejecucion
def menu():
    while True:
        print("\n--- busqueda de rutas ---")
        print("1. greedy")
        print("2. a*")
        print("3. salir")

        opcion = input("elige una opcion: ")

        if opcion == "1":
            inicio_tiempo = time.perf_counter()
            resultado = greedy(mapa, inicio, objetivo)
            tiempo = time.perf_counter() - inicio_tiempo

            mostrar_resultado("greedy", resultado)
            print(f"tiempo de ejecucion: {tiempo:.8f} segundos")

        elif opcion == "2":
            inicio_tiempo = time.perf_counter()
            resultado = astar(mapa, inicio, objetivo)
            tiempo = time.perf_counter() - inicio_tiempo

            mostrar_resultado("a*", resultado)
            print(f"tiempo de ejecucion: {tiempo:.8f} segundos")

        elif opcion == "3":
            print("programa finalizado")
            break

        else:
            print("opcion no valida")


# muestra el mapa, prueba la heuristica e inicia el menu
if __name__ == "__main__":
    print("mapa:\n")

    for fila in mapa:
        print(" ".join(fila))

    print("\nprueba de manhattan:")
    print(heuristica((1, 2), (6, 5)))

    menu()
