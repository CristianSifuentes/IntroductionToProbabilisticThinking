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

# Calcular la probabilidad condicional P(B|A) de al menos una cara dado que al menos dos caras han ocurrido
probabilidad_condicional = len(list(filter(al_menos_una_cara, evento_A))) / len(evento_A)

# Mostrar los resultados
print("Probabilidad del Evento A - Al menos dos caras: {:.4f}".format(probabilidad_A))
print("Probabilidad del Evento B - Al menos una cara: {:.4f}".format(probabilidad_B))
print("Probabilidad Condicional P(B|A) - Al menos una cara dado que al menos dos caras han ocurrido: {:.4f}".format(probabilidad_condicional))
