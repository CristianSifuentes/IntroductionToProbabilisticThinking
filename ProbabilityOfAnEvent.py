'''

Claro, puedo mostrarte un ejemplo en Python donde calculamos la probabilidad de un evento 
P(A) en un espacio muestral dado. Vamos a continuar con el ejemplo de lanzar tres monedas 
y calcular la probabilidad de que al menos dos de ellas salgan cara.
'''

import itertools

# Definir el espacio muestral para lanzar tres monedas
monedas = ['C', 'S']  # C: Cara, S: Sello
espacio_muestral = list(itertools.product(monedas, repeat=3))

# Definir el evento de al menos dos caras
def al_menos_dos_caras(resultado):
    return resultado.count('C') >= 2

# Calcular la probabilidad del evento P(A)
evento = list(filter(al_menos_dos_caras, espacio_muestral))
probabilidad_evento = len(evento) / len(espacio_muestral)

# Mostrar el espacio muestral, el conjunto de resultados del evento y la probabilidad
print("Espacio Muestral:")
print(espacio_muestral)

print("\nEvento - Al menos dos caras:")
print(evento)

print("\nProbabilidad del Evento P(A): {:.4f}".format(probabilidad_evento))

'''
En este ejemplo, utilizamos la función filter para obtener el conjunto de resultados que satisfacen el evento "al menos dos caras". 
La probabilidad del evento se calcula dividiendo el número de resultados en el evento entre el tamaño total del espacio muestral.

Recuerda que este es un ejemplo simple y con un espacio muestral finito. 
En situaciones más complejas o con espacios muestrales infinitos, el cálculo de probabilidades puede requerir enfoques más avanzados, 
como integrales en el caso continuo o técnicas de conteo más sofisticadas.
'''
