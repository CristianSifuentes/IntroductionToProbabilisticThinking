'''
La falacia de "Cum Hoc Ergo Propter Hoc" implica asumir una relación causal simplemente porque dos eventos ocurren juntos en el tiempo. Aquí te proporcionaré un ejemplo en Python que simula dos eventos que ocurren en secuencia, pero que no tienen una relación causal real.
'''
import numpy as np
import matplotlib.pyplot as plt

# Generar datos simulados
np.random.seed(42)

# Evento A: Un aumento en el número de personas usando paraguas
# Evento B: Un aumento en la cantidad de helados vendidos

dias = np.arange(1, 101)
personas_con_paraguas = np.random.randint(10, 100, size=100)
helados_vendidos = np.random.randint(50, 150, size=100)

# Asumir que ambos eventos están correlacionados en el tiempo
correlacion_temporal = 0.6
helados_vendidos = helados_vendidos.astype(np.float64) + correlacion_temporal * personas_con_paraguas.astype(np.float64)

# Graficar los eventos
plt.figure(figsize=(10, 5))
plt.plot(dias, personas_con_paraguas, label='Personas con Paraguas', linestyle='--', marker='o')
plt.plot(dias, helados_vendidos, label='Helados Vendidos', linestyle='--', marker='o')
plt.xlabel('Días')
plt.ylabel('Cantidad')
plt.title('Ejemplo de Cum Hoc Ergo Propter Hoc')
plt.legend()
plt.show()



'''
En este ejemplo, he generado datos simulados para dos eventos: el número de personas que usan paraguas y la cantidad de helados vendidos. Asumimos que hay una correlación temporal (0.6) entre ambos eventos, lo que significa que, en promedio, cuando hay más personas con paraguas, también se venden más helados.

Aunque hemos creado una correlación temporal artificial, es esencial comprender que no hay una relación causal real entre llevar paraguas y comprar helados. Es un ejemplo que ilustra cómo la correlación no implica necesariamente causalidad, y asumir lo contrario podría ser una aplicación de la falacia "Cum Hoc Ergo Propter Hoc". En situaciones del mundo real, es crucial realizar un análisis más profundo y considerar posibles variables confusas antes de hacer afirmaciones causales basadas en la correlación temporal.

'''