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
