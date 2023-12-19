import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Simulación de la población de estudiantes
np.random.seed(42)
poblacion = pd.DataFrame({
    'Edad': np.random.normal(loc=20, scale=2, size=1000),  # Edad media de 20 años
    'Horas_Estudio_Real': np.random.normal(loc=10, scale=3, size=1000),  # Horas reales de estudio
})

# Definir una función que simula el sesgo de respuesta
def sesgo_respuesta(edad, horas_reales):
    sesgo = (edad - 18) * 0.5  # Cuanto mayor es la edad, mayor es el sesgo positivo
    return horas_reales + sesgo + np.random.normal(loc=0, scale=2)

# Aplicar la función para simular el sesgo de respuesta en las horas de estudio reportadas
poblacion['Horas_Estudio_Reportadas'] = poblacion.apply(lambda row: sesgo_respuesta(row['Edad'], row['Horas_Estudio_Real']), axis=1)

# Visualización de las horas reales de estudio vs. las horas reportadas en la población
plt.scatter(poblacion['Horas_Estudio_Real'], poblacion['Horas_Estudio_Reportadas'], alpha=0.5)
plt.xlabel('Horas Reales de Estudio')
plt.ylabel('Horas Reportadas de Estudio')
plt.title('Sesgo de Respuesta en Horas de Estudio')
plt.show()
