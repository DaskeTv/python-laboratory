for i in ["Pildoras", "Informaticas", 3]:
	print("Hola Mundo", end = " ")
	print("Hola Mundo")

for i in range(3):
	print(f"valor de la variable {i}")

for i in range(5, 9): #Desde el 5 hasta el 9
	print(f"valor de la variable {i}")

for i in range(1, 5, 2): #Desde el 5 hasta el 9 en pasos de 2 en 2.
	print(f"valor de la variable {i}")

entrada = int(input("Introduce tu edad:"))

while entrada < 9 or entrada > 100:
	print("La edad introducida es incorrecta.")
	entrada = int(input("Introduce tu edad:"))
