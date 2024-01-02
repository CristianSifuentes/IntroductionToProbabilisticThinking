'''

Claro, puedo proporcionarte un ejemplo simple de un espacio muestral en Python. Supongamos que lanzamos dos dados justos. El espacio muestral para este experimento consiste en todas las posibles combinaciones de los resultados de ambos dados. Vamos a representar esto en Python:
'''

import itertools

# Definir los posibles resultados de un dado
dado = [1, 2, 3, 4, 5, 6]

# Obtener todas las posibles combinaciones de dos dados
espacio_muestral = list(itertools.product(dado, repeat=2))

# Mostrar el espacio muestral
print("Espacio Muestral:")
for resultado in espacio_muestral:
    print(resultado)


'''
En este ejemplo, itertools.product se utiliza para generar todas las combinaciones posibles de los resultados de dos dados. El resultado es una lista que representa el espacio muestral.

Este es un espacio muestral simple y finito, pero en situaciones más complejas, el espacio muestral puede ser infinito o continuo. El concepto central es que el espacio muestral abarca todas las posibles salidas de un experimento aleatorio.
'''
