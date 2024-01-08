''''
Claro, puedo proporcionarte un ejemplo avanzado donde implementamos el concepto de independencia de eventos. 
En este caso, consideraremos dos eventos A y B, donde A representa obtener al menos dos caras en tres lanzamientos 
de monedas, y B representa obtener al menos una cara.
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

# Calcular la probabilidad de al menos dos caras P(A)
evento_A = list(filter(al_menos_dos_caras, espacio_muestral))
probabilidad_A = len(evento_A) / len(espacio_muestral)

# Calcular la probabilidad de al menos una cara P(B)
evento_B = list(filter(al_menos_una_cara, espacio_muestral))
probabilidad_B = len(evento_B) / len(espacio_muestral)

# Calcular la intersección P(A ∩ B)
evento_interseccion = list(filter(al_menos_dos_caras, evento_B))
probabilidad_interseccion = len(evento_interseccion) / len(espacio_muestral)

# Verificar la independencia P(A ∩ B) = P(A) * P(B)
independencia = probabilidad_interseccion == probabilidad_A * probabilidad_B

# Mostrar los resultados
print("Probabilidad del Evento A - Al menos dos caras: {:.4f}".format(probabilidad_A))
print("Probabilidad del Evento B - Al menos una cara: {:.4f}".format(probabilidad_B))
print("Probabilidad de la Intersección P(A ∩ B): {:.4f}".format(probabilidad_interseccion))
print("Verificar Independencia (P(A ∩ B) = P(A) * P(B)): {}".format(independencia))


'''
En este ejemplo, calculamos las probabilidades de los eventos 
P(A) y P(B), la intersección P(A ∩ B), y luego verificamos la independencia según la fórmula 
P(A ∩ B)= P(A) × P(B). Si esta igualdad se cumple, los eventos A y B son independientes.
'''