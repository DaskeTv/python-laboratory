def devuelve_ciudades(*ciudades):		# Cuando tiene * va a recibir un numero indeterminado de elementos y sera en tuplas.
	for elemento in ciudades:
	#	for sub_elemento in ciudades:
			yield from elemento


ciudades_devueltas = devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))