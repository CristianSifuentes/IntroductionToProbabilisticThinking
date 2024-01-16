import numpy as np
import scipy.stats as stats

# Generar un conjunto de datos ficticio
datos = np.array([22, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70])

# Calcular la media
media = np.mean(datos)

# Calcular la mediana
mediana = np.median(datos)

# Calcular la moda
moda_resultado = stats.mode(datos)
moda = moda_resultado.mode[0] if moda_resultado.count[0] > 1 else "No hay moda única"

# Calcular los cuartiles
cuartiles = np.percentile(datos, [25, 50, 75])

# Imprimir los resultados
print("Media: {:.2f}".format(media))
print("Mediana: {:.2f}".format(mediana))
print("Moda: {}".format(moda))
print("Cuartiles (Q1, Q2, Q3): {:.2f}, {:.2f}, {:.2f}".format(*cuartiles))
