'''
La falacia del francotirador de Texas, en el contexto de la probabilidad y la estadística, se refiere a la tendencia de buscar patrones significativos en conjuntos de datos después de que se han recopilado, en lugar de establecer hipótesis a priori y recopilar datos de acuerdo con esas hipótesis.

En términos de probabilidad, esta falacia destaca la importancia de tener cuidado al interpretar patrones o tendencias en los datos, especialmente cuando hay múltiples posibilidades de encontrar algún patrón simplemente por azar.

Un ejemplo podría ser el siguiente: Supongamos que alguien revisa los registros de desempeño de los estudiantes en un examen y encuentra un pequeño grupo de estudiantes que tuvieron un rendimiento excepcional. Luego, esa persona decide analizar en detalle ese grupo en busca de cualquier patrón o característica común, como el color de su ropa, lo que comieron antes del examen, etc. Si encuentra algún patrón significativo, podría cometer la falacia del francotirador de Texas si no tenía una hipótesis clara antes de analizar los datos.

En resumen, en probabilidad y estadística, es esencial establecer hipótesis a priori y realizar análisis de datos de manera rigurosa para evitar caer en la falacia del francotirador de Texas y obtener interpretaciones sesgadas o incorrectas.
'''


'''
Supongamos que tenemos un conjunto de datos que representa el rendimiento de estudiantes en dos exámenes diferentes. Luego, decidimos analizar retrospectivamente el grupo de estudiantes que tuvo un rendimiento excepcional en ambos exámenes y buscar patrones específicos, como si hubieran usado bolígrafos de un color particular.
'''

import random

# Simulación de datos de rendimiento de estudiantes
random.seed(42)  # Establecer semilla para reproducibilidad
num_estudiantes = 1000

# Generar datos aleatorios de rendimiento en dos exámenes
rendimiento_exam1 = [random.randint(70, 100) for _ in range(num_estudiantes)]
rendimiento_exam2 = [random.randint(70, 100) for _ in range(num_estudiantes)]

# Identificar el grupo de estudiantes con rendimiento excepcional en ambos exámenes
grupo_destacado = [i for i in range(num_estudiantes) if rendimiento_exam1[i] > 90 and rendimiento_exam2[i] > 90]

# Simulación de análisis retrospectivo en busca de patrones
patron_boligrafos = ['rojo', 'azul', 'verde', 'negro']
patron_encontrado = random.choice(patron_boligrafos)

# Imprimir resultados
print("Número de estudiantes en el grupo destacado:", len(grupo_destacado))
print(f"Patrón retrospectivo encontrado: Los estudiantes usaron bolígrafos de color {patron_encontrado}.")
