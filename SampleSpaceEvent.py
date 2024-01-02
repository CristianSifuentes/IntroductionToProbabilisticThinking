'''
Claro, puedo mostrarte un ejemplo avanzado donde implementaremos el concepto de evento 
en el contexto de un espacio muestral. Vamos a considerar un experimento donde lanzamos 
tres monedas, y el espacio muestral consiste en todas las posibles combinaciones de caras (C) 
y sellos (S) para cada moneda. El evento que queremos evaluar es la ocurrencia de al menos dos caras.
 Utilizaremos Python para representar y calcular este evento.
'''

import itertools

# Definir el espacio muestral para lanzar tres monedas
monedas = ['C', 'S']  # C: Cara, S: Sello
espacio_muestral = list(itertools.product(monedas, repeat=3))

# Definir el evento de al menos dos caras
def al_menos_dos_caras(resultado):
    return resultado.count('C') >= 2

# Filtrar el espacio muestral para obtener el conjunto de resultados que satisfacen el evento
evento = list(filter(al_menos_dos_caras, espacio_muestral))

# Mostrar el espacio muestral y el conjunto de resultados del evento
print("Espacio Muestral:")
print(espacio_muestral)

print("\nEvento - Al menos dos caras:")
print(evento)


'''
En este ejemplo, itertools.product genera todas las combinaciones posibles de caras (C) y sellos (S) para cada una de las tres monedas. Luego, definimos una función al_menos_dos_caras que evalúa si un resultado contiene al menos dos caras. Utilizamos esta función para filtrar el espacio muestral y obtener el conjunto de resultados que satisfacen el evento.

Este ejemplo ilustra cómo puedes representar eventos en el contexto de un espacio muestral y utilizar Python para filtrar y trabajar con conjuntos específicos de resultados.
'''