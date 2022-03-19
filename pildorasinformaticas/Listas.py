#Las listas son los equivalentes a los arrays de otros lenguajes de programacion.
#Las listas pueden almacenar distintos tipos de valores, a diferencia de otros lenguajes.
#Se puede expandir dinamicamente durante tiempo de ejecucion.

elem1 = "Pablo"
elem2 = 10
elem3 = 1.5

lista = [elem1, elem2, elem3]

print(lista[:])
print(lista[-2]) #Se puede usar indices negativos.
print(lista[0:2]) #Se puede acceder a una porcion de la lista.
print(lista[1:])

lista.append("Maracas") #Anade una variable al final de la lista.
print(lista[3])

lista.insert(2, 20) #Inserta una variable en una posicion concreta de la lista.
print(lista[:])

lista.extend(["Pepito", "Anabelo", 5]) #Inserta variables al final de la lista.
print(lista[:])

print(lista.index("Pepito")) #Devuelve el indice del valor del parametro. Si hay dos variables de mismo valor,
							 #devuelve el index del primero que encuentra.

print("Pepe" in lista) #Devuelve true o false si se encuentra la variable en la lista.

lista.remove("Pablo") #Elimina una variable en la lista.
print(lista[:])

lista.pop() #Elimina la ultima variable de la lista.
print(lista[:])

lista2 = [1, 2, 3]
lista3 = lista+lista2 #Podemos unir los elementos de diferentes listas en una nueva.
print(lista3[:])