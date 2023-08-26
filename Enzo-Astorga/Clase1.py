# lista = Ariel, Liliana, Natalia, Osvaldo.

nombres = ['Naty', 'Osvaldo', 'Lily', 'Ariel']
print(nombres)
print(nombres[0:2]) # Solo muestra el índice 0 , 1 pero no el índice 2.

# Ir del inicio de la lista al índice (sin incluirlo):
print(nombres[ :3]) # Indices a mostrar 0, 1 y 2.

# Desde el índice indicado hasta el final:
print(nombres[1: ])

# Modificamos un valor.
nombres[0] = 'Natalia'
nombres[2] = 'Liliana'
print(nombres)

# Iterar nuestra lista:
for nombre in nombres: # nombre es singular, la lista es plural.
    print(nombre)
else:
    print('Se acabaron los elementos de la lista.')

# Preguntamos cuantos elementos tiene:
print(len(nombres)) # Len es una función que nos regresa la cantidad de elementos que contiene una lista.
# Le pasamos como parámetro la lista.

# Agregamos un elemento:
nombres.append('Marcelo')
print(nombres)

# Insertar un elemento en un índice específico:
nombres.insert(1, 'Alberto')
print(nombres)
nombres.insert(3, 'Débora')
print(nombres)

# Eliminamos un elemento:
nombres.remove('Alberto')
print(nombres)

# Eliminar el último elemento:
nombres.pop()
print(nombres)

# Eliminamos un índice específico:
del nombres[2] # del significa delete.
print(nombres)

# Eliminar, borrar o limpiar todos los elementos:
nombres.clear()
print(nombres)

# Eliminar la lista:
del nombres
# print(nombres) # Aquí muestra el error.


# Definimos una tupla:
cocina = ('cuchara', 'cutucuchillo', 'tenedor')
print(len(cocina))

# Acceder a un elemento, para esto utilizamos corchetes no parentesis:
print(cocina[0])

# Mostrar de manera inversa:
print(cocina[-1])

# Acceder a un rango:
print(cocina[0:2])
# Ejemplo:
verduras = ('papa') # Sin la coma pasa a ser un elemento cadena de tipo string y deja de ser una tupla.
print(verduras)

# Recorremos los elementos de la tupla:
for cocinar in cocina: # Print está usando \n para saltos de líneas.
    print(cocinar, end=' ') # Usamos end= para eliminar los saltos de línea.

# Esta conversión de tupla a lista y de lista a tupla NO es una buena práctica de la programación.
cocinaLista = list(cocina)
cocinaLista[0] = 'plato'
cocina = tuple(cocinaLista)
print("\n",cocina)

# En TUPLAS no se pueden utilizar las fuciones append, insert y remove.
# Si el programa necesitara modificarse usaremos una LISTA y si no queremos modificaciones usaremos una TUPLA.


# Eliminamos la tupla:
del cocina
# print(cocina) # Muestra el error.





