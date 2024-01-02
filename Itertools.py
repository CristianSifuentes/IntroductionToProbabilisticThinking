'''
itertools es un módulo en la biblioteca estándar de Python que proporciona una serie de funciones para trabajar 
con iteradores y generar iteradores eficientes. Algunas de las funciones más comunes en itertools incluyen:

'''

'''
itertools.product:
Genera el producto cartesiano de iterables, es decir, todas las posibles combinaciones de elementos de los iterables de entrada.
'''

import itertools

iterable1 = [1, 2]
iterable2 = ['a', 'b']
producto_cartesiano = list(itertools.product(iterable1, iterable2))

print(producto_cartesiano)
# Resultado: [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]


'''
------------------------------------------------------------------------------------------------------------------------------------
'''
'''
itertools.permutations y itertools.combinations:
Generan todas las permutaciones y combinaciones posibles de elementos de un iterable, respectivamente.
'''

iterable = [1, 2, 3]
permutaciones = list(itertools.permutations(iterable, 2))
# Resultado: [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
print(permutaciones)

combinaciones = list(itertools.combinations(iterable, 2))
# Resultado: [(1, 2), (1, 3), (2, 3)]
print(combinaciones)



'''
------------------------------------------------------------------------------------------------------------------------------------
'''
'''
itertools.cycle:
Crea un iterador que repite indefinidamente los elementos de un iterable.
'''

iterable = [1, 2, 3]
iterador_ciclo = itertools.cycle(iterable)

for _ in range(5):
    print(next(iterador_ciclo))
# Resultado: 1, 2, 3, 1, 2


'''
------------------------------------------------------------------------------------------------------------------------------------
'''
'''
itertools.chain:
Combina varios iterables en uno solo.
'''

iterable1 = [1, 2]
iterable2 = ['a', 'b']
iterador_combinado = itertools.chain(iterable1, iterable2)
# Resultado: [1, 2, 'a', 'b']
print(iterador_combinado)


'''
Estas son solo algunas de las funciones disponibles en itertools. Este módulo es muy útil para trabajar con iteradores de manera eficiente y para generar combinaciones, permutaciones y productos cartesianos en situaciones donde se necesitan explorar todas las posibles combinaciones de elementos.
'''