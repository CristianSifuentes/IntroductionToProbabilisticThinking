import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Simulación de la población de personas
np.random.seed(42)
poblacion = pd.DataFrame({
    'Edad': np.random.normal(loc=30, scale=5, size=1000),  # Edad media de 30 años
    'Ingreso': np.random.normal(loc=50000, scale=10000, size=1000),  # Ingreso medio de $50,000
    'Participa_en_Estudio': np.random.choice([1, 0], size=1000, p=[0.3, 0.7])  # 30% participan en el estudio
})

# Definir una función que representa una relación entre edad e ingreso
def relacion_ingreso_edad(edad):
    return 2000 + 1000 * edad + np.random.normal(loc=0, scale=5000)

# Aplicar la función para generar ingresos relacionados con la edad
poblacion['Ingreso'] = poblacion.apply(lambda row: relacion_ingreso_edad(row['Edad']), axis=1)

# Seleccionar solo a aquellos que participan en el estudio
muestra_participantes = poblacion[poblacion['Participa_en_Estudio'] == 1]

# Visualización de la relación entre edad e ingreso en la población completa y la muestra de participantes
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.scatter(poblacion['Edad'], poblacion['Ingreso'], alpha=0.5)
plt.title('Relación Edad e Ingreso - Población Completa')
plt.xlabel('Edad')
plt.ylabel('Ingreso')

plt.subplot(1, 2, 2)
plt.scatter(muestra_participantes['Edad'], muestra_participantes['Ingreso'], alpha=0.5, color='orange')
plt.title('Relación Edad e Ingreso - Muestra de Participantes')
plt.xlabel('Edad')
plt.ylabel('Ingreso')

plt.tight_layout()
plt.show()
