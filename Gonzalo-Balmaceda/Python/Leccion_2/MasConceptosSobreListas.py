# Concatenamos listas.
lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 6, 1]
lista3 = (lista1 + lista2)
print(lista3)

lista3.extend([7, 8, 9]) # Función para agregar elementos a la lista.
print(lista3)

print(lista3.index(5)) # Función para ubicar en que indice esta el valor ingresado.

# Como saber cuantos valores repetidos hay dentro de una lista.
print(lista3.count(1)) # Cuenta cuantos valor repetido hay dentro de la lista.

# Para poner al reves una lista.
lista3.reverse()
print(lista3)

# Para que una lista se multiplique repitiendo sus elementos.
lista = [1, 2, 3] * 2
print(lista)

# Metodos de ordenamientos.
lista3.sort() # Con el metodo .sort() ordenamos la lista ascendentemente.
print(lista3)

lista3.sort(reverse=True) # De esta forma ordenamos la lista descendentemente
print(lista3)

