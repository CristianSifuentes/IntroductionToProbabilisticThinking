'''
Voy a proporcionarte un ejemplo simple para ilustrar la falacia de regresión utilizando datos simulados en Python. En este ejemplo, mostraré cómo la falacia de regresión puede ocurrir si nos basamos únicamente en la correlación sin comprender completamente el contexto.
'''

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Generar datos simulados
np.random.seed(42)
x = np.random.normal(0, 1, 100)  # Variable independiente
y = 2 * x + np.random.normal(0, 1, 100)  # Variable dependiente

# Agregar un punto extremo
x_outlier = np.array([3])
y_outlier = 10

x = np.append(x, x_outlier)
y = np.append(y, y_outlier)

# Ajustar un modelo de regresión lineal
modelo = LinearRegression().fit(x.reshape(-1, 1), y.reshape(-1, 1))

# Graficar los datos y la línea de regresión
plt.scatter(x, y, label='Datos')
plt.plot(x, modelo.predict(x.reshape(-1, 1)), color='red', label='Regresión lineal')
plt.title('Ejemplo de Falacia de Regresión')
plt.xlabel('Variable Independiente')
plt.ylabel('Variable Dependiente')
plt.legend()
plt.show()


'''
En este ejemplo, creamos datos simulados donde hay una relación lineal entre la variable independiente (x) y la variable dependiente (y). Sin embargo, introducimos un punto extremo (x_outlier, y_outlier) que se desvía significativamente de la tendencia general.

La regresión lineal intentará ajustarse a los datos, pero el punto extremo puede tener un impacto desproporcionado en la pendiente de la línea de regresión. Si solo nos basamos en la correlación y ajustamos un modelo de regresión lineal, podríamos inferir incorrectamente que la variable independiente tiene un impacto significativo en la variable dependiente.

Es importante tener en cuenta que la falacia de regresión puede surgir cuando no se consideran adecuadamente los puntos extremos o se asume una relación causal basada únicamente en la correlación observada. En situaciones del mundo real, es fundamental realizar un análisis más profundo y considerar posibles variables confusas antes de hacer afirmaciones causales basadas en la correlación.
'''