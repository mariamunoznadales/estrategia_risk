from itertools import permutations, product

# Generar combinaciones posibles de tropas
def generar_combinaciones(max_puntos, tropas):
    combinaciones = []
    for inf in range(1, max_puntos // tropas["Infantería"]["costo"] + 1):
        for cab in range(1, max_puntos // tropas["Caballería"]["costo"] + 1):
            for art in range(1, max_puntos // tropas["Artillería"]["costo"] + 1):
                costo_total = (
                    inf * tropas["Infantería"]["costo"] +
                    cab * tropas["Caballería"]["costo"] +
                    art * tropas["Artillería"]["costo"]
                )
                if costo_total <= max_puntos and inf > 0 and cab > 0 and art > 0:
                    combinaciones.append({"Infantería": inf, "Caballería": cab, "Artillería": art})
    return combinaciones

# Generar todas las permutaciones posibles del orden de ataque
def generar_permutaciones_prioritarias(defensas):
    defensas_ordenadas = sorted(enumerate(defensas), key=lambda x: x[1])  # Ordenar por defensa
    indices_ordenados = [indice for indice, _ in defensas_ordenadas]
    return list(permutations(indices_ordenados))

# Representar el tablero
def representar_tablero(defensas):
    tablero = [{"territorio": i + 1, "defensa": defensa} for i, defensa in enumerate(defensas)]
    return tablero

# Calcular conquistas para una combinación y un orden
def calcular_conquistas(tablero, combinacion, tropas):
    conquistas = 0
    tropas_restantes = combinacion.copy()
    for territorio in tablero:
        fuerza_total = (
            tropas_restantes["Infantería"] * tropas["Infantería"]["fuerza"] +
            tropas_restantes["Caballería"] * tropas["Caballería"]["fuerza"] +
            tropas_restantes["Artillería"] * tropas["Artillería"]["fuerza"]
        )
        if fuerza_total >= territorio["defensa"]:
            conquistas += 1
            tropas_restantes["Infantería"] = max(0, tropas_restantes["Infantería"] - territorio["defensa"] // tropas["Infantería"]["fuerza"])
            tropas_restantes["Caballería"] = max(0, tropas_restantes["Caballería"] - territorio["defensa"] // tropas["Caballería"]["fuerza"])
            tropas_restantes["Artillería"] = max(0, tropas_restantes["Artillería"] - territorio["defensa"] // tropas["Artillería"]["fuerza"])
        else:
            break
    return conquistas

# Optimizar conquistas
def optimizar_conquistas(tablero, combinaciones, tropas):
    mejor_combinacion = None
    mejor_orden = None
    max_conquistas = 0
    
    for combinacion in combinaciones:
        for permutacion in generar_permutaciones_prioritarias([t["defensa"] for t in tablero]):
            tablero_ordenado = [tablero[i] for i in permutacion]
            conquistas = calcular_conquistas(tablero_ordenado, combinacion, tropas)
            if conquistas > max_conquistas:
                max_conquistas = conquistas
                mejor_combinacion = combinacion
                mejor_orden = permutacion
    
    return mejor_combinacion, mejor_orden, max_conquistas

# Entrada de datos
def entrada_datos():
    max_puntos = int(input("Introduce el máximo de puntos disponibles para tropas: "))
    cantidad_territorios = int(input("Introduce el número de territorios enemigos: "))
    defensas = []
    for i in range(cantidad_territorios):
        defensa = int(input(f"Introduce la fuerza de defensa del Territorio {i + 1}: "))
        defensas.append(defensa)
    tropas = {
        "Infantería": {"fuerza": 1, "costo": 1},
        "Caballería": {"fuerza": 3, "costo": 3},
        "Artillería": {"fuerza": 5, "costo": 5},
    }
    return max_puntos, defensas, tropas

# Main
def main():
    print("Bienvenido al planificador de ataques de Risk.")
    max_puntos, defensas, tropas = entrada_datos()
    
    # Generar combinaciones de tropas
    combinaciones = generar_combinaciones(max_puntos, tropas)
    print(f"\nCombinaciones posibles de tropas ({len(combinaciones)} encontradas):")
    for combinacion in combinaciones:
        print(combinacion)

    # Representar el tablero
    tablero = representar_tablero(defensas)
    print("\nTablero representado:")
    for territorio in tablero:
        print(territorio)

    # Optimizar conquistas
    mejor_combinacion, mejor_orden, max_conquistas = optimizar_conquistas(tablero, combinaciones, tropas)
    print("\nMejor estrategia encontrada:")
    print(f"Combinación de tropas: {mejor_combinacion}")
    print(f"Orden de ataque: {list(map(lambda x: x + 1, mejor_orden))}")
    print(f"Máximo de conquistas: {max_conquistas}")

if __name__ == "__main__":
    main()
