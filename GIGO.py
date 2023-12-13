'''

Sí, en el contexto de probabilidad y estadística, el concepto de "Garbage in, garbage out" (GIGO) sigue siendo relevante. En este contexto, se refiere a que si los datos de entrada que se utilizan para realizar un análisis estadístico o probabilístico son de baja calidad, inexactos o incorrectos, entonces los resultados del análisis también serán poco confiables o incorrectos.

En otras palabras, la calidad de los resultados de un análisis estadístico o probabilístico está directamente relacionada con la calidad de los datos que se utilizan como entrada. Si los datos iniciales son deficientes, sesgados o incompletos, es probable que cualquier conclusión o inferencia derivada de esos datos también sea problemática.

Por lo tanto, en el análisis estadístico y la modelización probabilística, es esencial comenzar con datos de alta calidad y realizar procesos de limpieza y validación de datos para asegurar la confiabilidad de los resultados. La falta de atención a la calidad de los datos puede llevar a conclusiones erróneas o a interpretaciones incorrectas de los resultados estadísticos. Este principio refuerza la importancia de la integridad y la calidad de los datos en cualquier análisis cuantitativo.
'''

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Crear un conjunto de datos simulado con horas de estudio y calificaciones
datos = {
    'Horas_de_Estudio': [2, 3, 4, 5, 6, np.nan, 7, 8, 9, 10],
    'Calificaciones': [60, 65, 70, 75, 80, 90, 85, 88, 92, 95]
}

# Crear un DataFrame de Pandas
df = pd.DataFrame(datos)

# Imprimir el conjunto de datos original
print("Conjunto de datos original:")
print(df)
print("\n")

# Eliminar filas con valores faltantes
df = df.dropna()

# Imprimir el conjunto de datos después de la limpieza
print("Conjunto de datos después de la limpieza:")
print(df)
print("\n")

# Realizar un análisis de correlación y regresión lineal
X = df['Horas_de_Estudio'].values.reshape(-1, 1)
y = df['Calificaciones'].values.reshape(-1, 1)

modelo = LinearRegression()
modelo.fit(X, y)

# Imprimir los resultados del modelo
print("Coeficiente de correlación:", np.corrcoef(X.flatten(), y.flatten())[0, 1])
print("Coeficiente de regresión:", modelo.coef_[0, 0])
print("Error cuadrático medio:", mean_squared_error(y, modelo.predict(X)))
