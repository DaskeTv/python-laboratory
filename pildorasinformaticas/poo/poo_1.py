class Coche():
	largo = 250
	ancho = 120
	ruedas = 4
	enMarcha = False

	def estado(self):
		if (self.enMarcha):
			return "El coche esta en marcha"
		else:
			return "El coche esta parado"

	def arrancar(self):	# Un metodo es una funcion que pertenece a una clase. El self es como this, en Java es implicita.
		self.enMarcha = True ## Self aqui funciona de la misma manera que this.

	def frenar(self):
		self.enMarcha = False


miCoche = Coche() # Hemos instanciado un objeto, no usamos el operador new.
print("El largo del coche es",miCoche.largo)
print("El ancho del coche es",miCoche.ancho)
print("El coche tiene",miCoche.ruedas, "ruedas.")
print(miCoche.estado())
miCoche.arrancar()
print(miCoche.estado())