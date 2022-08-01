import math

def evalua_edad(edad):

	if edad < 0 or edad > 99:
		raise TypeError("La edad debe estar comprendida entre 0 y 99 anios")

	if edad < 20:
		return "Eres muy joven"
	elif edad < 40:
		return "Eres joven"
	elif edad < 65:
		return "Eres maduro"
	elif edad < 100:
		return "Cuidate..."

print(evalua_edad(15))



def calcula_raiz(num):
	if num < 0:
		raise ValueError("El numero no puede ser negativo")
	else:
		return math.sqrt(num)

op1 = int(input("Introduce un numero:"))

try:
	print(calcula_raiz(op1))

except ValueError as ErrorDeNumeroNegativo:
	print(ErrorDeNumeroNegativo)


print("El programa continuaria su ejecucion")