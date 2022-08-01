def evaluacion(var):
	if (var < 0):
		return "Numero negativo"
	else:
		return "Numero positivo"

entrada = input("Introduce un numero entero:") #Solo recoge var como texto.
print(evaluacion(int(entrada)))

entrada2 = int(input("Introduce un numero entero:"))
if (entrada2 > 18):
	print(str(entrada2) + " es mayor que " + str(18)) #Solo se puede imprimir un tipo de variable.
else:
	print(str(entrada2) + " es menor que " + str(18))

entrada3 = input("Escribe texto:")
opcion = entrada3.lower()
if opcion in ("Hola Mundo"):
	print("Correcto")
else:
	print("Incorrecto")