import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Simulación de la población de estudiantes
np.random.seed(42)
poblacion = pd.DataFrame({
    'Estudiantes': np.arange(1, 1001),
    'Satisfaccion': np.random.normal(loc=7, scale=1, size=1000)  # Satisfacción media de 7
})

# Simulación del muestreo sesgado en la biblioteca a la hora del almuerzo
muestra_biblioteca = poblacion.sample(frac=0.2, random_state=42)

# Simulación de la encuesta en la biblioteca
muestra_biblioteca['Respuestas'] = np.random.normal(loc=8, scale=1, size=len(muestra_biblioteca))

# Comparación de la satisfacción promedio en la población y la muestra
satisfaccion_promedio_poblacion = poblacion['Satisfaccion'].mean()
satisfaccion_promedio_muestra = muestra_biblioteca['Respuestas'].mean()

print(f"Satisfacción promedio en la población: {satisfaccion_promedio_poblacion:.2f}")
print(f"Satisfacción promedio en la muestra de la biblioteca: {satisfaccion_promedio_muestra:.2f}")

# Visualización de la distribución de la satisfacción en la población y la muestra
plt.figure(figsize=(10, 5))
plt.hist(poblacion['Satisfaccion'], alpha=0.5, label='Población', bins=20)
plt.hist(muestra_biblioteca['Respuestas'], alpha=0.5, label='Muestra Biblioteca', bins=20)
plt.xlabel('Satisfacción')
plt.ylabel('Frecuencia')
plt.legend()
plt.title('Ejemplo de Muestreo Sesgado')
plt.show()
