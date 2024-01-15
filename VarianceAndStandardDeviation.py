import numpy as np

# Definir el espacio muestral para lanzar un dado
dados = [1, 2, 3, 4, 5, 6]
probabilidades = [1/6] * 6  # Probabilidad uniforme para un dado justo

# Calcular la esperanza matemática (media) de la variable aleatoria
esperanza_matematica = np.dot(dados, probabilidades)

# Calcular la varianza de la variable aleatoria
varianza = np.dot((dados - esperanza_matematica)**2, probabilidades)

# Calcular la desviación estándar como la raíz cuadrada de la varianza
desviacion_estandar = np.sqrt(varianza)

# Mostrar los resultados
print("Espacio Muestral:", dados)
print("Probabilidades:", probabilidades)
print("Esperanza Matemática (Media): {:.2f}".format(esperanza_matematica))
print("Varianza: {:.2f}".format(varianza))
print("Desviación Estándar: {:.2f}".format(desviacion_estandar))
