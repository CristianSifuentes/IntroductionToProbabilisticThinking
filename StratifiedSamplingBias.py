import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.linear_model import LinearRegression

# Simulación de la población de personas con dos estratos (por ejemplo, género)
np.random.seed(42)
num_personas = 1000

# Crear DataFrame de la población con características relacionadas al género
poblacion = pd.DataFrame({
    'Edad': np.random.normal(loc=30, scale=5, size=num_personas),
    'Ingreso': np.random.normal(loc=50000, scale=10000, size=num_personas),
    'Genero': np.random.choice(['Masculino', 'Femenino'], size=num_personas, p=[0.4, 0.6])
})

# Función que simula una relación entre ingreso y edad con variación según el género
def relacion_ingreso_edad(edad, genero):
    if genero == 'Masculino':
        return 2000 + 1000 * edad + np.random.normal(loc=0, scale=5000)
    else:
        return 1800 + 1000 * edad + np.random.normal(loc=0, scale=5000)

# Aplicar la función para generar ingresos relacionados con la edad y el género
poblacion['Ingreso'] = poblacion.apply(lambda row: relacion_ingreso_edad(row['Edad'], row['Genero']), axis=1)

# Visualización de la relación entre ingreso y edad en la población completa
plt.scatter(poblacion['Edad'], poblacion['Ingreso'], c=poblacion['Genero'].map({'Masculino': 'blue', 'Femenino': 'pink'}), alpha=0.7)
plt.xlabel('Edad')
plt.ylabel('Ingreso')
plt.title('Relación Ingreso y Edad en la Población Completa')
plt.show()

# Estratificación de la población por género
estratificador = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in estratificador.split(poblacion, poblacion['Genero']):
    poblacion_estratificada = poblacion.loc[train_index]

# Visualización de la estratificación por género
plt.scatter(poblacion_estratificada['Edad'], poblacion_estratificada['Ingreso'], c=poblacion_estratificada['Genero'].map({'Masculino': 'blue', 'Femenino': 'pink'}), alpha=0.7)
plt.xlabel('Edad')
plt.ylabel('Ingreso')
plt.title('Estratificación por Género en la Muestra')
plt.show()

# Modelado del sesgo de muestreo estratificado utilizando regresión lineal
X_estrato = poblacion_estratificada[['Edad']]
y_estrato = poblacion_estratificada['Ingreso']

modelo_estrato = LinearRegression()
modelo_estrato.fit(X_estrato, y_estrato)

# Coeficientes del modelo
print("Coeficientes del modelo para la muestra estratificada:")
print("Intercept:", modelo_estrato.intercept_)
print("Coeficientes:", modelo_estrato.coef_)
