#Son listas inmutables, no se pueden modificar despues de su creacion.
#No permiten anadir, eliminar o mover elementos. No permiten busquedas(excepto comprobar si una var esta en la tupla).
#Permiten extraer porciones.
#Son mas rapidas, ocupan menos espacio, formatean Strings y pueden utilizarse como claves en un diccionario.

miTupla = ("Antonieto", 9, 1, 2003)
print(miTupla[2])

miLista = list(miTupla) #Convertimos una tupla en lista que se almacena en una nueva variable.
miTuplaConvertida = tuple(miLista) #Convertimos una lista a una tupla y la almacenamos en una nueva variable.

print("Antonieto" in miTupla)
print(miTupla.count(9)) #Numero de veces que el paramatro esta almacenado en la tupla.
print(len(miTupla)) #Devuelve el numero de elementos de la tupla.

miTupla2 = ("Juan",) #Tupla unitaria
print(len(miTupla2))

miTupla3 = "Roberta", 2, 3, 1999 #Empaquetado de tupla
nombre, dia, mes, ano = miTupla3 #Desempaquetado de tuplas.
print(nombre)
print(dia)
print(mes)
print(ano)