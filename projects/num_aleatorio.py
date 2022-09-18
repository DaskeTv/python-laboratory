## Para generar numeros aleatorios tenemos multiples opciones dadas
## por los metodos de la clase random

a = random() # Genera un float entre 0.0 y 1.0
b = uniform(1.0, 20.0) # Genera un float desde 1.0 hasta 20.0
c = randrange(10) # Genera un integer entre 0 y 9 incluido
import random
d = random.randint(1, 10) # Genera un integer entre 1 y 10