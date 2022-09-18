# # Vamos a ver unos ejemplos de concatenacion de strings
# # Hay varias maneras de hacer esto

# usuario = "Daske"

# print("Hola " + usuario)
# print("Hola {}".format(usuario))
# print(f"Hola {usuario}")

nombre = input("Nombre: ")
adj1 = input("Adjetivo: ")
adj2 = input("Adjetivo: ")
verb1 = input("Verbo: ")
verb2 = input("Verbo: ")

madlib = f"El otro dia conoci a una persona, se llamaba {nombre}. Es {adj1} y {adj2}, le encanta {verb1} y sobretodo {verb2}."
print(madlib)