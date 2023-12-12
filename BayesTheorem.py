class ClasificadorBayesiano:
    def __init__(self, prob_spam, prob_no_spam):
        self.prob_spam = prob_spam
        self.prob_no_spam = prob_no_spam

    def calcular_probabilidad_condicional(self, palabra, spam=True):
        # Simulación de probabilidades condicionales basadas en conocimientos previos o entrenamiento
        if spam:
            return {"viagra": 0.9, "oferta": 0.8}.get(palabra, 0.01)
        else:
            return {"oferta": 0.1, "trabajo": 0.2}.get(palabra, 0.01)

    def clasificar(self, mensaje):
        palabras = mensaje.split()

        # Inicializar probabilidades a priori
        prob_spam_dado_mensaje = self.prob_spam
        prob_no_spam_dado_mensaje = self.prob_no_spam

        # Calcular probabilidades condicionales para cada palabra en el mensaje
        for palabra in palabras:
            prob_spam_dado_mensaje *= self.calcular_probabilidad_condicional(palabra, spam=True)
            prob_no_spam_dado_mensaje *= self.calcular_probabilidad_condicional(palabra, spam=False)

        # Normalizar las probabilidades
        suma_probabilidades = prob_spam_dado_mensaje + prob_no_spam_dado_mensaje
        prob_spam_dado_mensaje /= suma_probabilidades
        prob_no_spam_dado_mensaje /= suma_probabilidades

        # Tomar la decisión final
        if prob_spam_dado_mensaje > prob_no_spam_dado_mensaje:
            return "Spam"
        else:
            return "No Spam"

# Ejemplo de uso
prob_spam = 0.3  # Probabilidad a priori de que un mensaje sea spam
prob_no_spam = 1 - prob_spam  # Probabilidad a priori de que un mensaje no sea spam

clasificador = ClasificadorBayesiano(prob_spam, prob_no_spam)

mensaje_ejemplo = "Oferta especial: trabajo desde casa con la mejor oferta de viagra"
resultado = clasificador.clasificar(mensaje_ejemplo)

print(f"Mensaje: '{mensaje_ejemplo}'")
print(f"Clasificación: {resultado}")
