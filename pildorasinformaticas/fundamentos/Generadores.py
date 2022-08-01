# Son mas eficientes que las funciones tradicionales.
# Devuelve el siguinte valor con cada llamada de next.

def genera_pares(limite):		
	num = 0
	while num < limite:
	 	yield num*2 		# Crea un objeto generador iterable. 
	 	num += 1

devuelvePares = genera_pares(10)		# Viene a ser un iterador de Java.

print(next(devuelvePares))		# Devuelve el primer valor del objeto generador.

print("Aqui podria ir mas codigo")

print(next(devuelvePares))		# Entre cada llamada queda en suspension.

print("Aqui podria ir mas codigo")