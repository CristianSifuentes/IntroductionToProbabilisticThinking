# Programación condicional en Python

# Ejemplo: Verificar si un número es positivo, negativo o cero

# Obtener un número del usuario
numero = float(input("Ingrese un número: "))

# Uso de la declaración 'if' para realizar la verificación
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")


'''
1.- Solicitamos al usuario que ingrese un número usando la función input. La función float se utiliza para convertir la entrada en un número de punto flotante.

2.- Luego, utilizamos la declaración if para realizar la verificación condicional. Las partes clave son:

if numero > 0:: Verifica si el número es mayor que cero.
elif numero < 0:: Si la condición anterior no se cumple, verifica si el número es menor que cero (utilizando elif, que es una abreviatura de "else if").
else:: Si ninguna de las condiciones anteriores es verdadera, se ejecuta este bloque.

3.- En cada caso, imprimimos un mensaje indicando si el número es positivo, negativo o cero.
'''
