# Ejercicio 3: Agregar personajes a una lista
# Escriba un programa donde cree una lista con los siguientes personajes del Señor de los Anillos
# Nombre: Aragorn
# Clase: Guerrero
# Raza: Dúnedain del norte

# Nombre: Gandalf
# Clase: Mago
# Raza: Istar

# Nombre: Légolas
# Clase: Arquero
# Raza: Elfo Sindar

personajes = [] # Creamos una lista vacía
# Creamos diccionarios
P = {'Nombre': 'Aragorn', 'Clase': 'Guerrero', 'Raza': 'Dúnedain del norte'}
personajes.append(P) #Agregamos a la lista un personaje
P = {'Nombre': 'Gandalf', 'Clase': 'Mago', 'Raza': 'Istar'}
personajes.append(P)
P = {'Nombre': 'Legolas', 'Clase': 'Arquero', 'Raza': 'Elfo Sindar'}
personajes.append(P)
P = {'Nombre': 'Gimli', 'Clase': 'Guerrero', 'Raza': 'Enano'}
personajes.append(P)
P = {'Nombre': 'Saruman', 'Clase': 'Mago', 'Raza': 'Istar'}
personajes.append(P)
P = {'Nombre': 'Sauron', 'Clase': 'Nigromante', 'Raza': 'Ainur'}
personajes.append(P)

print(personajes) #Tare: Agregar por lo menos otros tres personajes a elección