class Coche():

	def __init__(self):	# Constructor de la clase.
		self.__largo = 250	# Encapsulamiento de una propiedad o atributo. No es accesible desde fuera de la clase.
		self.__ancho = 120
		self.__ruedas = 4
		self.__enMarcha = False

	def estado(self):
		if (self.__enMarcha):
			return "El coche esta en marcha"
		else:
			return "El coche esta parado"

	def arrancar(self):	# Un metodo es una funcion que pertenece a una clase. El self es como this, en Java es implicita.
		self.__enMarcha = True ## Self aqui funciona de la misma manera que this.

	def frenar(self):
		self.__enMarcha = False


miCoche = Coche() # Hemos instanciado un objeto, no usamos el operador new.
print("El largo del coche es",miCoche.__largo)
print("El ancho del coche es",miCoche.__ancho)
print("El coche tiene",miCoche.__ruedas, "ruedas.")
print(miCoche.estado())
miCoche.arrancar()
print(miCoche.estado())