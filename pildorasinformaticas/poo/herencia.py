class Vehiculos():

	def __init__(self, marca, modelo):
		self.marca = marca
		self.modelo = modelo
		self.enMarcha = False
		self.acelera = False
		self.frena = False

	def arrancar(self):
		self.enMarcha = True

	def acelerar(self):
		self.acelera = True
		self.frena = False

	def frenar(self):
		self.frena = True
		self.acelera = False

	def toString(self):
		print("Marca:", self.marca, "\nModelo:", self.modelo, "\nEn marcha:",
			 self.enMarcha, "\nAcelerando:", self.acelera, "\nFrena:", self.frena)

class Moto(Vehiculos):

	def __init__(self, marca, modelo, caballito):
		super().__init__(marca, modelo)
		self.caballito = caballito

	def hacerCaballito(self, valor):
		self.caballito = valor

	def toString(self):
		super().toString()
		print("Caballito:", self.caballito)	


miMoto = Moto("KTN", "Duke", False)
miMoto.toString()
miMoto.acelerar()
miMoto.hacerCaballito(True)
print("")
miMoto.toString()
print(isinstance(miMoto, Vehiculos))	# Devuelve true si el objeto es una instancia de la clase especificada