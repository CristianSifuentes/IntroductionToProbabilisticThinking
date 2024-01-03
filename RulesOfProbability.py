'''
Claro, podemos extender el ejemplo anterior para incluir las reglas de la suma y del producto. En este caso, consideraremos dos eventos: 
�
A representando la ocurrencia de al menos dos caras en tres lanzamientos de monedas y 
�
B representando la ocurrencia de al menos una cara.
'''

import itertools

# Definir el espacio muestral para lanzar tres monedas
monedas = ['C', 'S']  # C: Cara, S: Sello
espacio_muestral = list(itertools.product(monedas, repeat=3))

# Definir eventos
def al_menos_dos_caras(resultado):
    return resultado.count('C') >= 2

def al_menos_una_cara(resultado):
    return 'C' in resultado

# Calcular probabilidades de eventos individuales P(A) y P(B)
evento_A = list(filter(al_menos_dos_caras, espacio_muestral))
probabilidad_A = len(evento_A) / len(espacio_muestral)

evento_B = list(filter(al_menos_una_cara, espacio_muestral))
probabilidad_B = len(evento_B) / len(espacio_muestral)

# Calcular la intersección de eventos P(A ∩ B)
evento_interseccion = list(filter(al_menos_dos_caras, evento_B))
probabilidad_interseccion = len(evento_interseccion) / len(espacio_muestral)

# Aplicar la regla de la suma P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
probabilidad_union = probabilidad_A + probabilidad_B - probabilidad_interseccion

# Aplicar la regla del producto P(A ∩ B) = P(A) * P(B|A)
probabilidad_producto = probabilidad_A * (len(evento_interseccion) / len(evento_A))

# Mostrar los resultados
print("Probabilidad del Evento A - Al menos dos caras: {:.4f}".format(probabilidad_A))
print("Probabilidad del Evento B - Al menos una cara: {:.4f}".format(probabilidad_B))
print("Probabilidad del Evento A ∩ B: {:.4f}".format(probabilidad_interseccion))
print("Probabilidad del Evento A ∪ B (Regla de la Suma): {:.4f}".format(probabilidad_union))
print("Probabilidad del Evento A ∩ B (Regla del Producto): {:.4f}".format(probabilidad_producto))

'''
En este ejemplo, calculamos las probabilidades de los eventos individuales 
P(A) y P(B), la intersección P(A ∩ B), y luego aplicamos las reglas de la suma y del producto para obtener la probabilidad de la unión P(A∪B).
'''
