import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Parámetros de la distribución normal
media = 0
desviacion_estandar = 1

# Crear una distribución normal
distribucion_normal = stats.norm(loc=media, scale=desviacion_estandar)

# Generar valores para la variable aleatoria
valores_variable_aleatoria = np.linspace(-3, 3, 1000)

# Calcular las probabilidades para cada valor
probabilidades = distribucion_normal.pdf(valores_variable_aleatoria)

# Visualizar la distribución de probabilidad normal
plt.plot(valores_variable_aleatoria, probabilidades, color='skyblue', linewidth=2)
plt.title('Distribución Normal - Media: {}, Desviación Estándar: {}'.format(media, desviacion_estandar))
plt.xlabel('Valor de la Variable Aleatoria')
plt.ylabel('Densidad de Probabilidad')
plt.show()
