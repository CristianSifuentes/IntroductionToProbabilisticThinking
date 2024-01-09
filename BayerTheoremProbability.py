'''
Por supuesto, aquí tienes un ejemplo avanzado en Python que implementa el Teorema de Bayes. 
Vamos a considerar un escenario en el que queremos calcular la probabilidad de que una persona 
tenga una enfermedad dado un resultado positivo en una prueba, teniendo en cuenta la sensibilidad 
y especificidad de la prueba.
'''
# Definir probabilidades y sensibilidad/especificidad de la prueba
probabilidad_enfermedad = 0.01  # P(D)
sensibilidad_prueba = 0.95  # P(Positivo | Enfermedad)
especificidad_prueba = 0.90  # P(Negativo | No Enfermedad)

# Complemento de la probabilidad de tener la enfermedad y de no tenerla
probabilidad_no_enfermedad = 1 - probabilidad_enfermedad  # P(~D)

# Calcular la probabilidad de tener un resultado positivo en la prueba P(Positivo)
probabilidad_positivo = (probabilidad_enfermedad * sensibilidad_prueba) + (probabilidad_no_enfermedad * (1 - especificidad_prueba))

# Aplicar el Teorema de Bayes para calcular la probabilidad de tener la enfermedad dado un resultado positivo
probabilidad_enfermedad_dado_positivo = (probabilidad_enfermedad * sensibilidad_prueba) / probabilidad_positivo

# Mostrar los resultados
print("Probabilidad de tener la enfermedad P(D): {:.4f}".format(probabilidad_enfermedad))
print("Probabilidad de tener un resultado positivo en la prueba P(Positivo): {:.4f}".format(probabilidad_positivo))
print("Probabilidad de tener la enfermedad dado un resultado positivo P(D | Positivo): {:.4f}".format(probabilidad_enfermedad_dado_positivo))

'''
En este ejemplo, estamos utilizando el Teorema de Bayes para calcular la probabilidad de tener la enfermedad dado un resultado positivo en la prueba. La fórmula es:


P(D ∣ Positivo)= P(D) x P(Positivo∣D) / P(Positivo)
​
Esto ilustra cómo el Teorema de Bayes relaciona la probabilidad condicional (probabilidad de tener la enfermedad dado un resultado positivo) con las probabilidades marginales (probabilidad de tener la enfermedad y probabilidad de obtener un resultado positivo en la prueba).
'''
