'''
Claro, aquí tienes un ejemplo avanzado en Python que implementa la esperanza matemática (media) de una variable aleatoria discreta. En este caso, consideraremos una variable aleatoria que representa el resultado al lanzar un dado justo.
'''
import numpy as np

# Definir el espacio muestral para lanzar un dado
dados = [1, 2, 3, 4, 5, 6]
probabilidades = [1/6] * 6  # Probabilidad uniforme para un dado justo

# Calcular la esperanza matemática (media) de la variable aleatoria
esperanza_matematica = np.dot(dados, probabilidades)

# Mostrar el resultado
print("Espacio Muestral:", dados)
print("Probabilidades:", probabilidades)
print("Esperanza Matemática (Media): {:.2f}".format(esperanza_matematica))

'''
En este ejemplo, hemos definido un espacio muestral para lanzar un dado y asignado probabilidades uniformes para cada resultado. La esperanza matemática se calcula multiplicando cada valor de la variable aleatoria por su probabilidad correspondiente y sumando los resultados. En este caso, como estamos considerando un dado justo, la probabilidad de cada resultado es 1/6.

Este ejemplo muestra cómo calcular la esperanza matemática para una variable aleatoria discreta simple. La fórmula general es:

E(X)= ∑i xi ⋅ P(X = xi) 

donde E(X) es la esperanza matemática, xi son los posibles valores de la variable aleatoria, y 

P(X=xi) son las probabilidades correspondientes.
'''
