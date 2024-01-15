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
