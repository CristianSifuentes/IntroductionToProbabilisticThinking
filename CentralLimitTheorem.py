'''
Claro, el Teorema del Límite Central es un concepto fundamental en estadísticas que establece que, bajo ciertas condiciones, la distribución de la suma (o el promedio) de un gran número de variables aleatorias independientes se aproxima a una distribución normal, independientemente de la forma de la distribución original de las variables aleatorias.

Aquí hay un ejemplo en Python que ilustra el Teorema del Límite Central utilizando la distribución de Poisson como distribución original:


'''

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Parámetros de la distribución de Poisson
lambda_poisson = 3
num_muestras = 1000
tamano_muestra = 30

# Generar muestras de la distribución de Poisson
muestras_poisson = np.random.poisson(lambda_poisson, size=(num_muestras, tamano_muestra))

# Calcular las medias de cada muestra
medias_muestras = np.mean(muestras_poisson, axis=1)

# Calcular la media y la desviación estándar teóricas de la distribución de Poisson
media_teorica = lambda_poisson
desviacion_teorica = np.sqrt(lambda_poisson)

# Calcular la media y la desviación estándar de las medias de las muestras
media_muestral = np.mean(medias_muestras)
desviacion_muestral = np.std(medias_muestras)

# Crear histograma de las medias de las muestras
plt.hist(medias_muestras, bins=20, color='skyblue', edgecolor='black', density=True)

# Añadir la curva de la distribución normal teórica
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
pdf_normal = stats.norm.pdf(x, media_teorica, desviacion_teorica / np.sqrt(tamano_muestra))
plt.plot(x, pdf_normal, 'k--', linewidth=2, label='Distribución Normal Teórica')

# Etiquetas y título
plt.title('Teorema del Límite Central - Distribución de Poisson')
plt.xlabel('Media de las Muestras')
plt.ylabel('Frecuencia Relativa')

# Mostrar la leyenda
plt.legend()

# Mostrar el gráfico
plt.show()


'''
En este ejemplo, generamos múltiples muestras de una distribución de Poisson y calculamos las medias de cada muestra. Luego, creamos un histograma de las medias de las muestras y superponemos la curva de la distribución normal teórica. Observarás que a medida que aumentamos el número de muestras, la distribución de las medias de las muestras se aproxima cada vez más a una distribución normal. Esto ilustra el Teorema del Límite Central en acción.

'''