'''

Claro, aquí tienes un ejemplo avanzado en Python que implementa el concepto de variables aleatorias. 
En este caso, consideraremos una variable aleatoria que representa la suma de los resultados al lanzar dos dados.

'''
import matplotlib.pyplot as plt
import itertools

# Definir el espacio muestral para lanzar dos dados
dados = [1, 2, 3, 4, 5, 6]
espacio_muestral = list(itertools.product(dados, repeat=2))

# Definir la variable aleatoria como la suma de los resultados de los dos dados
def variable_aleatoria(resultados):
    return sum(resultados)

# Aplicar la variable aleatoria a cada resultado en el espacio muestral
valores_variables_aleatorias = [variable_aleatoria(resultado) for resultado in espacio_muestral]

# Visualizar la distribución de la variable aleatoria
plt.hist(valores_variables_aleatorias, bins=range(2, 14), align='left', color='skyblue', edgecolor='black')
plt.title('Distribución de la Variable Aleatoria - Suma de dos dados')
plt.xlabel('Valor de la Variable Aleatoria')
plt.ylabel('Frecuencia')
plt.show()

'''
En este ejemplo, creamos un espacio muestral que representa todas las combinaciones posibles al lanzar dos dados. 
Luego, definimos una variable aleatoria que asigna a cada resultado la suma de los dos dados. 
Aplicamos esta variable aleatoria a cada elemento del espacio muestral y visualizamos la distribución de la variable aleatoria mediante un histograma.

Este es un ejemplo básico, pero el concepto de variables aleatorias se aplica de manera más amplia a situaciones donde queremos asignar valores numéricos a los resultados de un experimento aleatorio para analizar su comportamiento.
'''
