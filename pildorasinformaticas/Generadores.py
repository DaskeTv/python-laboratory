def genera_pares(limite):
	num = 0
	while num < limite:
	 	yield num*2
	 	num += 1

devuelvePares = genera_pares(10)

print(next(devuelvePares))		# Devuelve el primer valor del objeto generador.

print("Aqui podria ir mas codigo")

print(next(devuelvePares))		# Entre cada llamada queda en suspension.

print("Aqui podria ir mas codigo")