print("Conversor de decimal a binario (4 bits)")

num = 0
while num < 1 or num > 15:
	num = int(input("Introduce un numero del 1 al 15: "))

salida = ""

if num >= 8:
	salida += "1"
	num -= 8
else:
	salida += "0"

if num >= 4:
	salida += "1"
	num -= 4
else:
	salida += "0"

if num >= 2:
	salida += "1"
	num -= 2
else:
	salida += "0"

if num >= 1:
	salida += "1"
else:
	salida += "0"

print("El numero introducido en binario es", salida)