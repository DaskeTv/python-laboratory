#En los diccionarios los datos se almacenan asociados a una clave(asociacion de tipo clave:valor).
#Los elementos almacenados no estan ordenados.
#Pueden almacenar listas y otros diccionarios.

miDiccionario = {"Alemania":"Berlin", "Francia":"Paris", "Reino Unido":"Londres", "Espana":"Madrid"}
miDiccionario["Italia"] = "Lisboa" #Introducimos una nueva clave:valor.

print(miDiccionario["Espana"])
print(miDiccionario["Alemania"])
print(miDiccionario)

miDiccionario["Italia"] = "Roma" #Sobrescribe el valor de una clave.
print(miDiccionario)

del miDiccionario["Reino Unido"] #Elimina una clave:valor
print(miDiccionario)

miTupla = ["Espana", "Francia", "Reino Unido", "Alemania"]
miDiccionario2 = {miTupla[0]:"Madrid", miTupla[1]:"Paris", miTupla[2]:"Londres", miTupla[3]:"Berlin"} #Usamos tupla como clave

miDiccionario3 = {23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "Anillos":[1991, 1992, 1993, 1996, 1997, 1998]}
print(miDiccionario3.keys()) #Devuelve todas las claves del diccionario.
print(miDiccionario3.values()) #Devuelve todos los valores del diccionario.
print(miDiccionario3["Anillos"])