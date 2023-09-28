# Desempaquetado de listas 0 list unpacking
def show(name, lastName):
    print(name + " " + lastName)

person = ["Gonzalo", "Balmaceda"]
show(person[0], person[1]) # Pasamos uno por uno los datos de la lista a la función.
show(*person) # Es lo mismo que la anterior pero le pasamos todo junto.

# Desempaquetamos a traves de una tupla.
tupla = ("Osvaldo", "Giordanini")
show(*tupla)

# Desempaquetamos un diccionario.
diccionario = {"lastName": "Lucero", "Name": "Natalia"}
show(**diccionario)