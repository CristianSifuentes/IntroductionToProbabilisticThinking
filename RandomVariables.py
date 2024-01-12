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
