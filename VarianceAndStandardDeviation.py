'''
Claro, aquí tienes un ejemplo avanzado en Python que implementa el concepto de varianza y desviación estándar para una variable aleatoria discreta. 
Usaremos el mismo escenario de lanzar un dado justo.
'''

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

'''
En este ejemplo, después de calcular la esperanza matemática, calculamos la varianza utilizando la fórmula:


Varianza(X)=∑i(xi - E(X))2 ⋅ P(X=xi)

Luego, calculamos la desviación estándar como la raíz cuadrada de la varianza. Estas medidas indican cuánto varían los valores de la variable aleatoria alrededor de su media.

Es importante destacar que, para una distribución discreta, la varianza y la desviación estándar son especialmente útiles para describir la dispersión de los valores alrededor de la media.
'''
