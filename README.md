# Planificador de Ataques para Risk
Link repositorio: (https://github.com/mariamunoznadales/estrategia_risk.git)

Este programa permite optimizar la estrategia de ataque en el juego Risk, con restricciones de recursos y fuerza.

## Reglas del Juego
1. **Tipos de tropas disponibles:**
   - **Infantería:** Fuerza = 1, Costo = 1 punto.
   - **Caballería:** Fuerza = 3, Costo = 3 puntos.
   - **Artillería:** Fuerza = 5, Costo = 5 puntos.
2. **Recursos:** Máximo de 20 puntos para entrenar tropas.
3. **Territorios enemigos:**
   - Tienes 3 territorios con fuerzas de defensa definidas.
   - El orden de ataque puede optimizarse para maximizar conquistas.
4. **Restricciones:**
   - Al menos 1 unidad de cada tipo de tropa.
   - Priorizar ataques a territorios con menor defensa.

## Funcionalidades
1. **Generar combinaciones de tropas:** Crea todas las combinaciones posibles respetando el presupuesto.
2. **Permutaciones de ataque:** Genera órdenes de ataque priorizando territorios más débiles.
3. **Calcular conquistas:** Simula el resultado de cada combinación y orden.
4. **Optimización:** Encuentra la estrategia que maximiza las conquistas.

## Cómo Usar
1. Introduce los datos requeridos:
   - Máximo de puntos disponibles.
   - Fuerza de defensa y número de territorios enemigos.
2. El programa mostrará:
   - Combinaciones posibles de tropas.
   - Mejor estrategia (combinación de tropas y orden de ataque).
   - Máximo número de conquistas alcanzables.

